#!/usr/bin/env python3
"""Build the data behind the graph home page.

Reads everything the site shows - docs/, skills/, commands/, agents/,
scripts/, plugins/, resources/ and tools/glossary.json - and writes two
scripts that index.html loads:

  assets/site/graph-data.js   every node and edge on the home graph
  assets/site/pages-data.js   the rendered guide pages, for the reader

Nothing is hand-maintained except the glossary: sections, page order, links
between pages, which command follows which skill and which page cites which
resource all come from the files, so a rerun stays true.

    pip install markdown
    python3 tools/build_graph_site.py
"""
import glob, html as H, importlib.util, io, json, math, os, posixpath, re

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "site")
GH_BLOB = "https://github.com/undefined-ui/second-brain-os/blob/main/"
GH_TREE = "https://github.com/undefined-ui/second-brain-os/tree/main/"

MD = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])


def read(rel):
    return io.open(os.path.join(ROOT, rel), encoding="utf-8").read()


def exists(rel):
    return os.path.exists(os.path.join(ROOT, rel))


def plain(fragment):
    t = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", H.unescape(t)).strip()


def clip(t, n=280):
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(" ", 1)[0].rstrip(",;:-—")
    return cut + "…"


def first_para(md_text):
    """First prose paragraph after the H1: skips lists, tables, quotes, code."""
    for block in re.split(r"\n\s*\n", md_text):
        b = block.strip()
        if not b or b.startswith(("#", "|", "```", "<", "- ", "* ", "1.")):
            continue
        b = re.sub(r"^>\s?", "", b, flags=re.M)
        b = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", b)
        b = re.sub(r"[*_`]", "", b)
        return " ".join(b.split())
    return ""


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    out, key = {}, None
    for line in m.group(1).split("\n"):
        km = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            out[key] = "" if val in (">-", ">", "|", "|-") else val.strip("\"'")
        elif key:
            out[key] = (out[key] + " " + line.strip()).strip()
    return out


# ---------------------------------------------------------------- the graph
nodes, edges = {}, []
edge_seen = set()


def node(nid, **kw):
    nodes.setdefault(nid, {"id": nid})
    nodes[nid].update(kw)
    return nodes[nid]


def edge(s, t, kind, w=1, hidden=False):
    if s == t or s not in nodes or t not in nodes:
        return
    key = (min(s, t), max(s, t), kind)
    if key in edge_seen:
        return
    edge_seen.add(key)
    e = {"s": s, "t": t, "k": kind}
    if w != 1:
        e["w"] = w
    if hidden:
        e["h"] = 1
    edges.append(e)


node("root", type="root", group="root", label="Second Brain OS",
     desc="Guides and resources for AI engineers: a course on building agents "
          "from a single prompt to production, five handbooks that go deep on "
          "one layer each, a hands-on second-brain project, the toolkit, and "
          "the links worth your time.")

COLLECTIONS = {
    "course":   ("The agents course", "course",
                 "Seven modules from a single prompt to a production agent: theory "
                 "from the whitepapers, a build in every module. Read in order."),
    "handbook": ("Handbooks", "handbook",
                 "Not a path - references. The full menu of techniques, tools and "
                 "builds for one layer of the course. Dip in anywhere."),
    "guide":    ("Second brain", "guide",
                 "A hands-on project: a knowledge base an agent builds and maintains "
                 "for you, in plain markdown. One evening to set up."),
    "glossary": ("Glossary", "term",
                 "The ideas the whole site keeps coming back to. Each one links to "
                 "the pages that lean on it hardest."),
    "toolkit":  ("Toolkit", "tool",
                 "What you install: agent skills, slash commands, subagents, "
                 "scripts, the course plugin and the starter vault."),
    "resources": ("Resources", "res",
                  "Every vetted link: papers, tools, Obsidian plugins, repositories "
                  "and reading."),
}
for cid, (label, group, desc) in COLLECTIONS.items():
    node(f"col:{cid}", type="collection", group=group, label=label, desc=desc)
    edge("root", f"col:{cid}", "contains")

# ---------------------------------------------------------------- sections
index_md = read("docs/README.md")
sec_order = []
for m in re.finditer(r"\]\(([a-z0-9-]+)/README\.md\)", index_md):
    if m.group(1) not in sec_order and exists(f"docs/{m.group(1)}/README.md"):
        sec_order.append(m.group(1))
for d in sorted(glob.glob(os.path.join(ROOT, "docs", "*", "README.md"))):
    s = os.path.basename(os.path.dirname(d))
    if s not in sec_order:
        sec_order.append(s)


def collection_of(sec):
    if sec.startswith("course-"):
        return "course"
    if sec.startswith("track-"):
        return "handbook"
    return "guide"


pages, page_src = {}, {}
counters = {"guide": 0, "course": 0, "handbook": 0}
for sec in sec_order:
    readme = read(f"docs/{sec}/README.md")
    title = re.search(r"^# (.+)$", readme, re.M).group(1).strip()
    blurb = first_para(re.sub(r"^# .+\n", "", readme, count=1))
    col = collection_of(sec)
    n = counters[col]
    counters[col] += 1
    badge = {"guide": f"{n + 1:02d}", "course": f"C{n}", "handbook": f"T{n + 1}"}[col]
    order = []
    for m in re.finditer(r"^\s*(?:\d+\.|[-*])\s+\[[^\]]+\]\(([a-z0-9-]+)\.md\)", readme, re.M):
        if m.group(1) != "README" and exists(f"docs/{sec}/{m.group(1)}.md"):
            order.append(m.group(1))
    for f in sorted(glob.glob(os.path.join(ROOT, "docs", sec, "*.md"))):
        name = os.path.basename(f)[:-3]
        if name != "README" and name not in order:
            order.append(name)
    sid = f"sec:{sec}"
    node(sid, type="section", group=col, label=title, badge=badge, desc=blurb,
         pages=[f"{sec}/{p}" for p in order])
    edge(f"col:{col}", sid, "contains")
    hb = re.search(r"handbook for \[module (\d+)\]\(\.\./(course-[a-z0-9-]+)/README\.md\)", readme)
    if hb:
        nodes[sid]["module"] = f"sec:{hb.group(2)}"
    for i, p in enumerate(order):
        pid = f"{sec}/{p}"
        raw = read(f"docs/{sec}/{p}.md")
        ptitle = re.search(r"^# (.+)$", raw, re.M).group(1).strip()
        body = re.sub(r"^# .+\n", "", raw, count=1)
        page_src[pid] = body
        node(pid, type="page", group=col, label=ptitle, sec=sid, pos=i + 1, of=len(order),
             path=f"docs/{sec}/{p}.md", desc=clip(first_para(body), 300))
        edge(sid, pid, "contains")

# handbook -> the course module it deepens
for nid, n in list(nodes.items()):
    if n.get("module") in nodes:
        edge(nid, n["module"], "handbook")

# ---------------------------------------------------------------- toolkit
TOOL_HUBS = {
    "skills": ("Skills", "One per workflow in the second-brain project. The agent loads a skill only when the task matches it."),
    "commands": ("Slash commands", "Scoped entry points into the skills, typed as /name."),
    "agents": ("Subagents", "Six subagents, four of them read-only by design."),
    "scripts": ("Scripts", "Dependency-free Python for link checking, stats, graph export and chat import."),
    "plugin": ("agents-course plugin", ""),
    "vault": ("Starter vault", "vault-template/: the wiki structure, the project pipeline, CLAUDE.md and page templates, ready to copy."),
}
for hid, (label, desc) in TOOL_HUBS.items():
    node(f"hub:{hid}", type="hub", group="tool", label=label, desc=desc)
    edge("col:toolkit", f"hub:{hid}", "contains")
nodes["hub:vault"].update(url=GH_TREE + "vault-template")

for f in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
    name = os.path.basename(os.path.dirname(f))
    fm = frontmatter(read(f"skills/{name}/SKILL.md"))
    node(f"skill:{name}", type="skill", group="tool", label=name,
         desc=clip(fm.get("description", ""), 320), url=GH_TREE + f"skills/{name}")
    edge("hub:skills", f"skill:{name}", "contains")

cmd_groups = {}
try:
    spec = importlib.util.spec_from_file_location("build_tree", os.path.join(ROOT, "scripts", "build_tree.py"))
    bt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bt)
    for g, names in bt.COMMAND_GROUPS.items():
        for c in names:
            cmd_groups[c] = g
except Exception:
    pass

for f in sorted(glob.glob(os.path.join(ROOT, "commands", "*.md"))):
    name = os.path.basename(f)[:-3]
    if name == "README":
        continue
    text = read(f"commands/{name}.md")
    fm = frontmatter(text)
    cid = f"cmd:{name}"
    node(cid, type="command", group="tool", label="/" + name, desc=fm.get("description", ""),
         sub=cmd_groups.get(name, ""), url=GH_BLOB + f"commands/{name}.md")
    sk = re.search(r"Follow the `([a-z0-9-]+)` skill", text)
    if sk and f"skill:{sk.group(1)}" in nodes:
        nodes[cid]["via"] = f"skill:{sk.group(1)}"
        edge(cid, f"skill:{sk.group(1)}", "follows")
        edge("hub:commands", cid, "contains", hidden=True)
    else:
        edge("hub:commands", cid, "contains")

for f in sorted(glob.glob(os.path.join(ROOT, "agents", "*.md"))):
    name = os.path.basename(f)[:-3]
    if name == "README":
        continue
    fm = frontmatter(read(f"agents/{name}.md"))
    node(f"agent:{name}", type="agent", group="tool", label=name, desc=fm.get("description", ""),
         tools=fm.get("tools", ""), url=GH_BLOB + f"agents/{name}.md")
    edge("hub:agents", f"agent:{name}", "contains")

for f in sorted(glob.glob(os.path.join(ROOT, "scripts", "*.py"))):
    name = os.path.basename(f)
    if name.startswith("build_"):
        continue
    doc = re.search(r'"""(.*?)"""', read(f"scripts/{name}"), re.S)
    node(f"script:{name}", type="script", group="tool", label=name,
         desc=doc.group(1).strip().split("\n")[0] if doc else "", url=GH_BLOB + f"scripts/{name}")
    edge("hub:scripts", f"script:{name}", "contains")

PLUG = "plugins/agents-course"
if exists(f"{PLUG}/.claude-plugin/plugin.json"):
    pj = json.loads(read(f"{PLUG}/.claude-plugin/plugin.json"))
    nodes["hub:plugin"].update(desc=pj.get("description", ""), url=GH_TREE + PLUG,
                               label=f"{pj['name']} plugin")
    for f in sorted(glob.glob(os.path.join(ROOT, PLUG, "skills", "*", "SKILL.md"))):
        name = os.path.basename(os.path.dirname(f))
        fm = frontmatter(read(f"{PLUG}/skills/{name}/SKILL.md"))
        node(f"plug:{name}", type="skill", group="tool", label=name, sub="plugin",
             desc=clip(fm.get("description", ""), 320), url=GH_TREE + f"{PLUG}/skills/{name}")
        edge("hub:plugin", f"plug:{name}", "contains")
    for f in sorted(glob.glob(os.path.join(ROOT, PLUG, "agents", "*.md"))):
        name = os.path.basename(f)[:-3]
        fm = frontmatter(read(f"{PLUG}/agents/{name}.md"))
        node(f"plug:{name}", type="agent", group="tool", label=name, sub="plugin",
             desc=clip(fm.get("description", ""), 320), url=GH_BLOB + f"{PLUG}/agents/{name}.md")
        edge("hub:plugin", f"plug:{name}", "contains")

# ---------------------------------------------------------------- resources
RES_CAT = {"papers.md": "Papers", "tools.md": "Tools", "plugins.md": "Obsidian plugins",
           "repositories.md": "Repositories", "skills.md": "Skills catalogs", "reading.md": "Reading"}
resources = []
for fn, label in RES_CAT.items():
    if not exists(f"resources/{fn}"):
        continue
    hid = f"rcat:{fn[:-3]}"
    node(hid, type="hub", group="res", label=label, url=GH_BLOB + f"resources/{fn}",
         desc=first_para(re.sub(r"^# .+\n", "", read(f"resources/{fn}"), count=1)))
    edge("col:resources", hid, "contains")
    group = ""
    text = read(f"resources/{fn}")
    for line in text.split("\n"):
        h = re.match(r"^## (.+)$", line)
        if h:
            group = h.group(1).strip()
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        link = re.search(r"\[([^\]]+)\]\((https?://[^)]+)\)", cells[0]) if cells else None
        if not link:
            continue
        metric, desc = "", ""
        for c in cells[1:]:
            if re.fullmatch(r"[\d,.]+[KkM]?|community plugin|small", c):
                metric = c
            else:
                desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", c)
        resources.append((hid, group, link.group(1), link.group(2), metric, desc))
    for block in text.split("\n\n"):
        h = re.search(r"^## (.+)$", block, re.M)
        if h:
            group = h.group(1).strip()
        for m in re.finditer(r"\*\*\[([^\]]+)\]\((https?://[^)]+)\)\*\*", block, re.S):
            if any(r[3] == m.group(2) for r in resources):
                continue
            clean = re.sub(r"\s+", " ", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", block))
            clean = re.sub(r"[*#>]", "", clean).strip()
            desc = clean.split(". ", 1)[1] if ". " in clean else clean
            resources.append((hid, group, " ".join(m.group(1).split()), m.group(2), "", clip(desc, 240)))

url_to_res = {}
for i, (hid, group, name, url, metric, desc) in enumerate(resources):
    rid = f"res:{i}"
    node(rid, type="resource", group="res", label=name, url=url, metric=metric,
         sub=group, desc=clip(desc, 260))
    edge(hid, rid, "contains")
    url_to_res[url.rstrip("/")] = rid

# ---------------------------------------------------------------- pages
pages_out = {}
mentions = {}  # tool or resource id -> {page id: count}


def tool_for_path(rel):
    """Map a repo-relative path to a toolkit node, if it is one."""
    rel = rel.rstrip("/")
    m = re.match(r"^skills/([a-z0-9-]+)(?:/SKILL\.md)?$", rel)
    if m and f"skill:{m.group(1)}" in nodes:
        return f"skill:{m.group(1)}"
    for pat, pre in ((r"^commands/([a-z0-9-]+)\.md$", "cmd"), (r"^agents/([a-z0-9-]+)\.md$", "agent"),
                     (r"^scripts/([a-z0-9_]+\.py)$", "script"),
                     (r"^plugins/agents-course/(?:skills|agents)/([a-z0-9-]+)(?:/SKILL\.md|\.md)?$", "plug")):
        m = re.match(pat, rel)
        if m and f"{pre}:{m.group(1)}" in nodes:
            return f"{pre}:{m.group(1)}"
    if rel in ("skills", "skills/README.md"):
        return "hub:skills"
    if rel in ("commands", "commands/README.md"):
        return "hub:commands"
    if rel in ("agents", "agents/README.md"):
        return "hub:agents"
    if rel in ("scripts", "scripts/README.md"):
        return "hub:scripts"
    if rel.startswith("plugins"):
        return "hub:plugin"
    if rel.startswith("vault-template"):
        return "hub:vault"
    m = re.match(r"^resources/([a-z]+)\.md$", rel)
    if m and f"rcat:{m.group(1)}" in nodes:
        return f"rcat:{m.group(1)}"
    if rel in ("resources", "resources/README.md"):
        return "col:resources"
    return None


def bump(target, pid, n=1):
    mentions.setdefault(target, {})
    mentions[target][pid] = mentions[target].get(pid, 0) + n


for pid, body in page_src.items():
    sec = pid.split("/")[0]
    here = f"docs/{sec}"
    MD.reset()
    html = MD.convert(body)

    def fix_link(m):
        href, rest = m.group(1), m.group(2)
        if href.startswith("#"):
            return f'<a href="{href}" data-anchor="{href[1:]}"{rest}>'
        if re.match(r"^(https?:|mailto:)", href):
            rid = url_to_res.get(H.unescape(href).rstrip("/"))
            if rid:
                bump(rid, pid)
                return f'<a href="{href}" class="ext" data-node="{rid}" target="_blank" rel="noopener"{rest}>'
            return f'<a href="{href}" class="ext" target="_blank" rel="noopener"{rest}>'
        path, _, frag = href.partition("#")
        rel = posixpath.normpath(posixpath.join(here, path))
        if rel.startswith("docs/") and rel.endswith(".md"):
            parts = rel[5:-3].split("/")
            if len(parts) == 2 and parts[1] != "README" and parts[0] + "/" + parts[1] in nodes:
                tid = parts[0] + "/" + parts[1]
                edge(pid, tid, "link")
                return f'<a href="#/read/{tid}" class="wiki" data-node="{tid}"{rest}>'
            if len(parts) == 2 and f"sec:{parts[0]}" in nodes:
                edge(pid, f"sec:{parts[0]}", "link")
                return f'<a href="#/n/sec:{parts[0]}" class="wiki" data-node="sec:{parts[0]}"{rest}>'
        if rel in ("docs/README.md", "README.md", "docs/ROADMAP.md"):
            return f'<a href="#/" class="wiki" data-node="root"{rest}>'
        tool = tool_for_path(rel)
        if tool:
            bump(tool, pid, 3)
            url = nodes[tool].get("url") or (GH_BLOB + rel)
            return f'<a href="{url}" class="ext tool" data-node="{tool}" target="_blank" rel="noopener"{rest}>'
        isdir = os.path.isdir(os.path.join(ROOT, rel))
        return f'<a href="{(GH_TREE if isdir else GH_BLOB) + rel}" class="ext" target="_blank" rel="noopener"{rest}>'

    html = re.sub(r'<a href="([^"]*)"([^>]*)>', fix_link, html)
    html = re.sub(r'(<img[^>]+src=")(?!https?:|/|data:)([^"]+)"',
                  lambda m: m.group(1) + posixpath.normpath(posixpath.join(here, m.group(2))) + '"', html)
    heads = [{"id": a, "t": plain(b)} for a, b in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)]
    text = plain(html)
    nodes[pid]["words"] = len(text.split())
    nodes[pid]["heads"] = len(heads)
    pages_out[pid] = {"html": html, "heads": heads, "text": text[:6000]}

    # mentions of toolkit items in the prose, beyond explicit links
    for cid in [k for k in nodes if k.startswith("cmd:")]:
        n = len(re.findall(r"(?<![\w/.-])/" + re.escape(cid[4:]) + r"(?![\w-])", body))
        if n:
            bump(cid, pid, n)
    for sid in [k for k in nodes if k.startswith(("skill:", "plug:"))]:
        n = len(re.findall(r"(?<![\w-])" + re.escape(sid.split(":", 1)[1]) + r"(?![\w-])", body))
        if n:
            bump(sid, pid, n)
    for sid in [k for k in nodes if k.startswith("script:")]:
        n = body.count(sid.split(":", 1)[1])
        if n:
            bump(sid, pid, n)
    if not sec.startswith(("course-", "track-")):
        for aid in [k for k in nodes if k.startswith("agent:")]:
            n = len(re.findall(r"\b" + re.escape(aid[6:]) + r"\b", body))
            if n:
                bump(aid, pid, n)

# toolkit / resource -> page edges: the strongest few per item
for target, per in mentions.items():
    ranked = sorted(per.items(), key=lambda kv: -kv[1])
    nodes[target]["inpages"] = [[p, c] for p, c in ranked]
    kind = "cites" if target.startswith("res:") else "uses"
    for p, c in ranked[:8]:
        edge(p, target, kind, w=c)

# ---------------------------------------------------------------- glossary
G = json.loads(read("tools/glossary.json"))
for t in G["terms"]:
    flags = 0 if t.get("case") else re.I
    alts = sorted(t["aliases"], key=len, reverse=True)
    rx = re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(a) for a in alts) + r")(?![\w])", flags)
    found = []
    for pid, body in page_src.items():
        n = len(rx.findall(pages_out[pid]["text"]))
        titled = bool(rx.search(nodes[pid]["label"])) or any(rx.search(h["t"]) for h in pages_out[pid]["heads"])
        if n or titled:
            found.append((pid, n, titled))
    found.sort(key=lambda h: (-(h[2] * 1000 + h[1])))
    # a passing mention is noise for common terms, but all there is for rare ones
    hits = [h for h in found if h[1] >= 2 or h[2]]
    if len(hits) < 4:
        hits = found[:4]
    if not hits:
        continue
    tid = f"term:{t['id']}"
    node(tid, type="term", group="term", label=t["label"], desc=t["def"],
         inpages=[[p, n] for p, n, _ in hits], total=sum(n for _, n, _ in hits))
    edge("col:glossary", tid, "contains", hidden=True)
    for p, n, titled in hits[:10]:
        edge(tid, p, "mentions", w=n)
    for p, n, _ in hits:
        nodes[p].setdefault("terms", []).append(tid)
    for r in [k for k in nodes if k.startswith("res:")]:
        if rx.search(nodes[r]["label"]):
            edge(r, tid, "related")

# ---------------------------------------------------------------- sizes
deg = {}
for e in edges:
    if not e.get("h"):
        deg[e["s"]] = deg.get(e["s"], 0) + 1
        deg[e["t"]] = deg.get(e["t"], 0) + 1
for nid, n in nodes.items():
    d = deg.get(nid, 0)
    n["val"] = round({
        "root": 34, "collection": 14,
        "section": 5 + 0.45 * len(n.get("pages", [])),
        "hub": 4.5,
        "page": 1.4 + 0.11 * d,
        "term": 1.1 + 0.3 * math.sqrt(len(n.get("inpages", []))),
        "skill": 2.0, "agent": 2.0, "script": 1.6, "command": 0.8,
        "resource": 0.7,
    }[n["type"]], 2)

stats = {
    "pages": sum(1 for n in nodes.values() if n["type"] == "page"),
    "sections": sum(1 for n in nodes.values() if n["type"] == "section"),
    "words": sum(n.get("words", 0) for n in nodes.values()),
    "terms": sum(1 for n in nodes.values() if n["type"] == "term"),
    "tools": sum(1 for n in nodes.values() if n["group"] == "tool" and n["type"] != "hub"),
    "resources": sum(1 for n in nodes.values() if n["type"] == "resource"),
    "links": sum(1 for e in edges if e["k"] == "link"),
    "edges": sum(1 for e in edges if not e.get("h")),
    "nodes": len(nodes),
}

os.makedirs(OUT, exist_ok=True)
with io.open(os.path.join(OUT, "graph-data.js"), "w", encoding="utf-8", newline="\n") as f:
    f.write("/* generated by tools/build_graph_site.py - do not edit */\nwindow.SBOS_GRAPH=")
    json.dump({"stats": stats, "order": [f"sec:{s}" for s in sec_order],
               "nodes": list(nodes.values()), "edges": edges},
              f, ensure_ascii=False, separators=(",", ":"))
    f.write(";\n")
with io.open(os.path.join(OUT, "pages-data.js"), "w", encoding="utf-8", newline="\n") as f:
    f.write("/* generated by tools/build_graph_site.py - do not edit */\nwindow.SBOS_PAGES=")
    json.dump(pages_out, f, ensure_ascii=False, separators=(",", ":"))
    f.write(";\n")

print(" | ".join(f"{k}: {v}" for k, v in stats.items()))
