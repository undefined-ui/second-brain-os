#!/usr/bin/env python3
"""Generate tree.html - the full component tree as one interactive page.

Every line is a hyperlink: guide and handbook pages route into the site,
code artefacts route to GitHub. Descriptions come from the artefacts
themselves (frontmatter, docstrings, page titles), so a rerun stays true.

    python3 scripts/build_tree.py
"""
import io, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GH = "https://github.com/undefined-ui/second-brain-os/blob/main/"
GHT = "https://github.com/undefined-ui/second-brain-os/tree/main/"

COMMAND_GROUPS = {
    "ingestion": ["ingest", "ingest-url", "ingest-youtube", "ingest-pdf",
                  "ingest-paper", "ingest-chats", "ingest-voice",
                  "ingest-newsletter", "ingest-highlights", "backfill"],
    "structuring": ["link", "dedupe", "merge", "rename", "split", "retype",
                    "schema", "tags", "aliases", "contradictions", "index"],
    "graph": ["graph", "graph-export", "orphans", "hubs", "bridges",
              "clusters", "typed-links", "stale"],
    "retrieval": ["ask", "know", "connect", "compare", "sources", "gaps",
                  "contradicts", "timeline", "trace", "changed-my-mind"],
    "maintenance": ["lint", "health", "metrics", "review", "weekly",
                    "monthly", "prune", "archive", "commit"],
    "outputs": ["outline", "draft", "report", "publish", "export", "quiz",
                "explain", "ingest-mine"],
    "projects": ["project", "project-status", "decisions", "commitments",
                 "handoff", "scope"],
    "safety": ["privacy", "secrets", "dry-run", "rollback", "audit"],
    "setup": ["init", "claude-md", "install", "doctor", "schedule"],
}

TOP_FILES = [
    ("README.md", "Guide index, quickstart, curated catalog"),
    ("CONTRIBUTING.md", "Primary sources only, no affiliate links"),
    ("LICENSE", "MIT"),
]

VAULT = [
    ("CLAUDE.md", "Page contracts, linking rules, contradictions"),
    ("raw/", "Sources land here, never edited after"),
    ("wiki/", "The artefact the agent maintains"),
    ("wiki/sources/", "One page per ingested item"),
    ("wiki/entities/", "People, orgs, projects, tools"),
    ("wiki/concepts/", "Ideas. The pages that compound"),
    ("wiki/synthesis/", "Only when it says what no source did"),
    ("wiki/index.md", "Catalog. Read first, always"),
    ("wiki/log.md", "One line per run. Makes it auditable"),
    ("projects/", "Inputs / Process / Outputs / Feedback"),
    ("templates/", "Source, concept, entity, synthesis"),
    ("output/", "Reports and drafts, ingested back later"),
]

RESOURCES_DESC = {
    "papers.md": "GraphRAG, HippoRAG, Lost in the Middle",
    "plugins.md": "Obsidian plugins ranked by installs",
    "reading.md": "Karpathy's gist, Ahrens, Forte, Matuschak",
    "repositories.md": "GraphRAG, agent memory, RAG frameworks",
    "skills.md": "More skills counted across the ecosystem",
    "tools.md": "Editors, capture, search, graph, publishing",
}


def esc(t):
    return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def clip(t, n=72):
    t = re.sub(r"\s+", " ", (t or "").strip())
    t = t.split(". ")[0].rstrip(".")
    return t[: n - 1] + "…" if len(t) > n else t


def fm_desc(path):
    try:
        s = io.open(path, encoding="utf-8").read()
    except OSError:
        return ""
    m = re.match(r"---\n(.*?)\n---", s, re.S)
    if not m:
        return ""
    fm = m.group(1)
    d = re.search(r"description:\s*(?:>-?\s*\n)?((?:.|\n)*?)(?:\n\w+:|\Z)", fm)
    return clip(d.group(1).replace("\n", " ")) if d else ""


def docstring(path):
    s = io.open(path, encoding="utf-8").read()
    m = re.search(r'"""(.*?)(?:\n|""")', s, re.S)
    return clip(m.group(1)) if m else ""


def site_pages():
    """Page titles and section order, read from the site's own graph data."""
    s = io.open(os.path.join(ROOT, "assets", "site", "graph-data.js"), encoding="utf-8").read()
    G = json.loads(s[s.index("=") + 1:].rstrip().rstrip(";"))
    N = {n["id"]: n for n in G["nodes"]}
    order = {sid[4:]: N[sid]["pages"] for sid in G["order"]}
    return {"pages": [{"id": n["id"], "title": n["label"]} for n in G["nodes"] if n["type"] == "page"],
            "order": order,
            "sections": {sec: {"title": N["sec:" + sec]["label"]} for sec in order}}


def row(name, href, desc, cls=""):
    return (f'<div class="r {cls}"><a href="{href}">{esc(name)}</a>'
            f'<span class="c"># {esc(desc)}</span></div>')


def branch(label, href, desc, rows, open_=True):
    inner = "".join(rows)
    return (f'<details{" open" if open_ else ""}><summary><a href="{href}">'
            f'{esc(label)}</a><span class="c"># {esc(desc)}</span></summary>'
            f'<div class="kids">{inner}</div></details>')


def main():
    D = site_pages()
    title = {p["id"]: p["title"] for p in D["pages"]}
    out = []

    out.append('<div class="sec">'
               + "".join(row(n, GH + n, d, "top") for n, d in TOP_FILES)
               + "</div>")

    # agents
    ag = sorted(f for f in os.listdir(os.path.join(ROOT, "agents"))
                if f.endswith(".md") and f != "README.md")
    out.append('<div class="sec">' + branch(
        "agents/", GHT + "agents", f"{len(ag)} subagents, 4 of them read-only",
        [row(a, GH + "agents/" + a, fm_desc(os.path.join(ROOT, "agents", a)))
         for a in ag]) + "</div>")

    # skills
    sk = sorted(d for d in os.listdir(os.path.join(ROOT, "skills"))
                if os.path.isdir(os.path.join(ROOT, "skills", d)))
    out.append('<div class="sec">' + branch(
        "skills/", GHT + "skills", f"{len(sk)} skills, one per workflow",
        [row(d + "/", GH + f"skills/{d}/SKILL.md",
             fm_desc(os.path.join(ROOT, "skills", d, "SKILL.md")))
         for d in sk]) + "</div>")

    # plugins: each plugin's skills and agents, flattened under one branch
    plug_rows, n_plug_tools = [], 0
    plug_root = os.path.join(ROOT, "plugins")
    for pl in sorted(os.listdir(plug_root)):
        pdir = os.path.join(plug_root, pl)
        if not os.path.isdir(pdir):
            continue
        for d in sorted(os.listdir(os.path.join(pdir, "skills"))
                        if os.path.isdir(os.path.join(pdir, "skills")) else []):
            plug_rows.append(row(
                f"/{pl}:{d}", GH + f"plugins/{pl}/skills/{d}/SKILL.md",
                fm_desc(os.path.join(pdir, "skills", d, "SKILL.md"))))
            n_plug_tools += 1
        adir = os.path.join(pdir, "agents")
        for f in sorted(os.listdir(adir)) if os.path.isdir(adir) else []:
            if f.endswith(".md"):
                plug_rows.append(row(
                    f"{pl}:{f[:-3]}", GH + f"plugins/{pl}/agents/{f}",
                    fm_desc(os.path.join(adir, f))))
                n_plug_tools += 1
    out.append('<div class="sec">' + branch(
        "plugins/", GHT + "plugins",
        "the course's tools as a Claude Code plugin, installable in "
        "two commands", plug_rows) + "</div>")

    # commands, grouped
    cmd_desc = {}
    for f in os.listdir(os.path.join(ROOT, "commands")):
        if f.endswith(".md") and f != "README.md":
            cmd_desc[f[:-3]] = fm_desc(os.path.join(ROOT, "commands", f))
    grouped = set(c for g in COMMAND_GROUPS.values() for c in g)
    stray = sorted(set(cmd_desc) - grouped)
    groups_html = []
    for g, names in COMMAND_GROUPS.items():
        names = [n for n in names if n in cmd_desc]
        groups_html.append(branch(
            g + "/", GHT + "commands", f"{len(names)}",
            [row("/" + n, GH + f"commands/{n}.md", cmd_desc[n]) for n in names],
            open_=False))
    if stray:
        groups_html.append(branch(
            "other/", GHT + "commands", f"{len(stray)}",
            [row("/" + n, GH + f"commands/{n}.md", cmd_desc[n]) for n in stray],
            open_=False))
    out.append('<div class="sec"><details open><summary>'
               f'<a href="{GHT}commands">commands/</a>'
               f'<span class="c"># {len(cmd_desc)} slash commands, thin by design'
               '</span></summary><div class="kids">'
               + "".join(groups_html) + "</div></details></div>")

    # scripts
    py = sorted(f for f in os.listdir(os.path.join(ROOT, "scripts"))
                if f.endswith(".py"))
    out.append('<div class="sec">' + branch(
        "scripts/", GHT + "scripts", "Dependency-free Python",
        [row(f, GH + "scripts/" + f, docstring(os.path.join(ROOT, "scripts", f)))
         for f in py]) + "</div>")

    # vault template
    out.append('<div class="sec">' + branch(
        "vault-template/", GHT + "vault-template",
        "Clone this folder, open it in Obsidian, run /init",
        [row(n, GHT + "vault-template/" + n.rstrip("/") if n.endswith("/")
             else GH + "vault-template/" + n, d) for n, d in VAULT]) + "</div>")

    # the second-brain project, listed after the course and the handbooks
    guide_secs = []
    n_guide = 0
    for sec, ids in D["order"].items():
        if sec.startswith("track-") or sec.startswith("course-"):
            continue
        meta = D["sections"][sec]
        n_guide += len(ids)
        guide_secs.append(branch(
            sec + "/", "index.html#" + ids[0],
            f"{meta['title']} · {len(ids)} pages",
            [row(i.split("/")[1] + ".md", "index.html#" + i, title[i])
             for i in ids], open_=False))
    guide_block = ('<div class="sec"><details open><summary>'
                   f'<a href="index.html">docs/</a><span class="c"># Second brain, '
                   f'a hands-on project. 10 sections, {n_guide} pages</span></summary>'
                   '<div class="kids">' + "".join(guide_secs) + "</div></details></div>")

    # the course
    course_secs, n_course = [], 0
    for sec, ids in D["order"].items():
        if not sec.startswith("course-"):
            continue
        meta = D["sections"][sec]
        n_course += len(ids)
        course_secs.append(branch(
            sec + "/", "index.html#" + ids[0],
            f"{meta['title']} · {len(ids)} pages",
            [row(i.split("/")[1] + ".md", "index.html#" + i, title[i])
             for i in ids], open_=False))
    out.append('<div class="sec"><details open><summary>'
               f'<a href="index.html">docs/course-*/</a><span class="c"># '
               f'The agents course. 7 modules, {n_course} pages'
               '</span></summary><div class="kids">'
               + "".join(course_secs) + "</div></details></div>")

    # the tracks
    track_secs, n_track = [], 0
    for sec, ids in D["order"].items():
        if not sec.startswith("track-"):
            continue
        meta = D["sections"][sec]
        n_track += len(ids)
        track_secs.append(branch(
            sec + "/", "index.html#" + ids[0],
            f"{meta['title']} · {len(ids)} pages",
            [row(i.split("/")[1] + ".md", "index.html#" + i, title[i])
             for i in ids], open_=False))
    out.append('<div class="sec"><details open><summary>'
               f'<a href="index.html">docs/track-*/</a><span class="c"># '
               f'Five handbooks, {n_track} pages, each ends in a build'
               '</span></summary><div class="kids">'
               + "".join(track_secs) + "</div></details></div>")
    out.append(guide_block)

    # resources
    res = sorted(f for f in os.listdir(os.path.join(ROOT, "resources"))
                 if f.endswith(".md") and f != "README.md")
    nlinks = sum(io.open(os.path.join(ROOT, "resources", f), encoding="utf-8")
                 .read().count("](http") for f in res)
    out.append('<div class="sec">' + branch(
        "resources/", "resources.html",
        f"{nlinks} vetted links, checked September to November 2026",
        [row(f, "resources.html", RESOURCES_DESC.get(f, "")) for f in res])
        + "</div>")

    counts = (f"{len(sk)} skills · {len(cmd_desc)} commands · "
              f"{len(ag)} subagents · {n_plug_tools} plugin tools · "
              f"{len(py)} scripts · "
              f"{n_course} course pages · {n_track} handbook pages · "
              f"{n_guide} second-brain pages · "
              f"{nlinks} vetted links")

    page = TEMPLATE.replace("{{TREE}}", "".join(out)) \
                   .replace("{{COUNTS}}", counts)
    io.open(os.path.join(ROOT, "tree.html"), "w", encoding="utf-8",
            newline="\n").write(page)
    print("tree.html written ·", counts)


TEMPLATE = """<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<script>try{var t=JSON.parse(localStorage.getItem('sbos:theme'));if(t==='dark'||t==='light')document.documentElement.dataset.theme=t}catch(e){}</script><title>The full component tree - Second Brain OS</title>
<meta name="description" content="Every component in second-brain-os on one page: the agents course, five handbooks, the second-brain project, skills, commands, agents, scripts and resources, each line a link.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%23F7F9F6'/%3E%3Crect x='.5' y='.5' width='31' height='31' rx='6.5' fill='none' stroke='%23D2DACF'/%3E%3Cpath d='M10 21 L16 11 L22 19 M16 11 L23 9' stroke='%231F6B52' stroke-width='1.6' fill='none'/%3E%3Ccircle cx='10' cy='21' r='3' fill='%23F7F9F6' stroke='%231F6B52' stroke-width='1.6'/%3E%3Ccircle cx='16' cy='11' r='3' fill='%23F7F9F6' stroke='%231F6B52' stroke-width='1.6'/%3E%3Ccircle cx='22' cy='19' r='3' fill='%23F7F9F6' stroke='%231F6B52' stroke-width='1.6'/%3E%3Ccircle cx='24' cy='8' r='2' fill='%231F6B52'/%3E%3C/svg%3E">
<style>
:root{--paper:#EAEEE9;--card:#F7F9F6;--ink:#15201B;--soft:#4B5A52;--faint:#7C8A82;
  --rule:#D2DACF;--accent:#1F6B52;--accent-bg:#E1EDE5;color-scheme:light}
/* dark: follows the system unless the visitor picked a theme */
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#0F1513;--card:#171F1B;--ink:#E2E8E3;--soft:#A7B4AC;--faint:#7B8981;--rule:#29342F;--accent:#5DBB94;--accent-bg:#1B2C24;--num:#D4AC52;--paper-rgb:15,21,19;--on-accent:#0F1513;color-scheme:dark}}
:root[data-theme="dark"]{--paper:#0F1513;--card:#171F1B;--ink:#E2E8E3;--soft:#A7B4AC;--faint:#7B8981;--rule:#29342F;--accent:#5DBB94;--accent-bg:#1B2C24;--num:#D4AC52;--paper-rgb:15,21,19;--on-accent:#0F1513;color-scheme:dark}
.theme{font:15px/1 ui-monospace,Menlo,monospace;color:var(--soft);background:none;border:1px solid var(--rule);border-radius:6px;width:32px;height:30px;cursor:pointer;flex:none}
.theme:hover{color:var(--ink);border-color:var(--accent)}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--paper);color:var(--ink);
  font:13px/1.7 ui-monospace,Menlo,Consolas,monospace}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
header{border-bottom:1px solid var(--rule);background:var(--card)}
.bar{max-width:1240px;margin:0 auto;padding:14px 22px;display:flex;gap:22px;align-items:baseline}
.brand{font-weight:700;color:var(--ink)}
.brand span{color:var(--accent)}
nav{display:flex;gap:14px}
nav a{color:var(--soft)}nav a.on{color:var(--ink);font-weight:600}
.wrap{max-width:1240px;margin:0 auto;padding:26px 22px 60px}
h1{font:700 26px/1.2 Georgia,'Times New Roman',serif;margin-bottom:6px}
.lede{color:var(--soft);margin-bottom:14px;max-width:70ch}
.ctl{margin-bottom:16px;display:flex;gap:8px}
.ctl button{font:inherit;font-size:11.5px;color:var(--soft);background:var(--card);
  border:1px solid var(--rule);border-radius:99px;padding:3px 12px;cursor:pointer}
.ctl button:hover{border-color:var(--accent);color:var(--accent)}
.cols{columns:1;column-gap:36px}
@media(min-width:1080px){.cols{columns:2}}
.sec{break-inside:avoid;margin-bottom:14px;background:var(--card);
  border:1px solid var(--rule);border-radius:8px;padding:10px 14px}
details>summary{cursor:pointer;list-style:none;white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis}
details>summary::before{content:'\\25B8';color:var(--faint);margin-right:7px;
  display:inline-block;transition:transform .12s}
details[open]>summary::before{transform:rotate(90deg)}
summary a{font-weight:700}
.kids{margin-left:9px;padding-left:14px;border-left:1px solid var(--rule)}
.kids details{margin:1px 0}
.r{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.r.top{margin:1px 0}
.c{color:var(--faint);margin-left:10px;font-size:12px}
.counts{margin-top:26px;border-top:1px solid var(--rule);padding-top:12px;
  color:var(--soft);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}
.counts b{color:var(--ink);font-weight:600}
footer{border-top:1px solid var(--rule);padding:22px;text-align:center;color:var(--faint)}
</style><!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "251090521ca24c01bde87a953db3dea4"}'></script><!-- End Cloudflare Web Analytics -->
</head><body>
<header><div class="bar">
  <a class="brand" href="index.html">[[ second<span>brain</span>os ]]</a>
  <nav>
    <a href="index.html">Map</a>
    <a href="resources.html">Resources</a>
    <a href="tree.html" class="on">Tree</a>
    <a href="https://github.com/undefined-ui/second-brain-os">Repo</a>
  </nav>
  <button class="theme" id="theme" aria-label="Switch between light and dark theme">&#9790;</button>
</div></header>
<div class="wrap">
  <h1>The full component tree</h1>
  <p class="lede">Everything in the repository on one page, annotated. Every line is a link: pages open on this site, code opens on GitHub. Click a branch to fold it.</p>
  <div class="ctl">
    <button onclick="document.querySelectorAll('details').forEach(d=>d.open=true)">expand all</button>
    <button onclick="document.querySelectorAll('details').forEach(d=>d.open=false)">collapse all</button>
  </div>
  <div class="cols">{{TREE}}</div>
  <div class="counts"><b>{{COUNTS}}</b><span>generated from the repo</span></div>
</div>
<footer>Generated from the repository. <a href="https://github.com/undefined-ui/second-brain-os">github.com/undefined-ui/second-brain-os</a> · by <a href="https://x.com/undefinedKi" rel="noopener">@undefinedKi</a></footer>
<script>(function(){var b=document.getElementById('theme'),r=document.documentElement,m=matchMedia('(prefers-color-scheme: dark)');function d(){return (r.dataset.theme||(m.matches?'dark':'light'))==='dark'}function p(){b.textContent=d()?'\u2600':'\u263E';b.title=d()?'Light theme':'Dark theme'}b.onclick=function(){var t=d()?'light':'dark';r.dataset.theme=t;try{localStorage.setItem('sbos:theme',JSON.stringify(t))}catch(e){}p()};m.addEventListener('change',p);p()})()</script></body></html>"""


if __name__ == "__main__":
    main()
