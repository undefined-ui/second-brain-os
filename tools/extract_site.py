#!/usr/bin/env python3
"""Extracts guide pages, the doc link graph, and the resource catalog into JSON."""
import os, re, json, glob
import markdown

ROOT = "."
md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list"])

SECTION_TITLES = {}
pages = []          # {id, section, section_title, title, html, headings, links}

for secdir in sorted(glob.glob(f"{ROOT}/docs/*/")):
    sec = os.path.basename(secdir.rstrip("/"))
    idx = open(secdir + "README.md").read()
    stitle = re.search(r"^# (.+)$", idx, re.M).group(1)
    sblurb = ""
    m = re.search(r"^#[^\n]+\n\n([^\n].*?)\n\n", idx, re.S)
    if m: sblurb = " ".join(m.group(1).split())
    SECTION_TITLES[sec] = {"title": stitle, "blurb": sblurb}
    listed = re.findall(r"^- \[[^\]]+\]\(([a-z0-9-]+)\.md\)", idx, re.M)
    files = [f + ".md" for f in listed]
    for extra in sorted(os.path.basename(x) for x in glob.glob(secdir + "*.md")):
        if extra != "README.md" and extra not in files: files.append(extra)
    for name in files:
        p = secdir + name
        if not os.path.exists(p): continue
        raw = open(p).read()
        title = re.search(r"^# (.+)$", raw, re.M).group(1)
        body = re.sub(r"^# .+\n", "", raw, count=1)
        # collect internal links before converting
        links = []
        for lm in re.finditer(r"\[([^\]]+)\]\((?!https?://)([^)#]+\.md)\)", body):
            tgt = os.path.normpath(os.path.join(secdir, lm.group(2)))
            links.append((lm.group(1), tgt))
        heads = [h for h in re.findall(r"^## (.+)$", body, re.M)]
        md.reset()
        html = md.convert(body)
        pages.append({
            "id": f"{sec}/{name[:-3]}",
            "path": os.path.relpath(p, ROOT),
            "section": sec, "section_title": stitle,
            "title": title, "html": html, "headings": heads,
            "raw_links": links,
            "words": len(body.split()),
            "text": " ".join(re.sub(r"[`*#>\[\]()]", " ", body).split())[:4000],
        })

by_path = {p["path"]: p["id"] for p in pages}
sec_index = {}
for p in pages:
    sec_index.setdefault(p["section"], []).append(p["id"])

# resolve links to page ids
for p in pages:
    out = []
    for label, tgt in p["raw_links"]:
        rel = os.path.relpath(tgt, ROOT)
        if rel in by_path:
            out.append({"to": by_path[rel], "label": label})
    p["links"] = out
    del p["raw_links"]

# ---- section-level cross-reference weights for the hero figure
w = {}
for p in pages:
    for l in p["links"]:
        a, b = p["section"], l["to"].split("/")[0]
        if a != b:
            k = tuple(sorted((a, b)))
            w[k] = w.get(k, 0) + 1
nodes = [{"id": s, "title": SECTION_TITLES[s]["title"], "n": len(sec_index[s])}
         for s in SECTION_TITLES]
edges = [{"a": a, "b": b, "w": n} for (a, b), n in w.items()]

# ---- resources: parse every markdown table row that carries a link
res = []
CAT = {"plugins.md": "Obsidian plugin", "tools.md": "Tool", "skills.md": "Skills",
       "repositories.md": "Repository", "papers.md": "Paper", "reading.md": "Reading"}
for f in sorted(glob.glob(f"{ROOT}/resources/*.md")):
    fn = os.path.basename(f)
    if fn == "README.md": continue
    group = ""
    for line in open(f):
        h = re.match(r"^## (.+)$", line)
        if h: group = h.group(1).strip(); continue
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or set("".join(cells)) <= set("-: "): continue
        link = re.search(r"\[([^\]]+)\]\((https?://[^)]+)\)", cells[0])
        if not link: continue
        rest = cells[1:]
        metric = ""
        desc = ""
        for c in rest:
            if re.fullmatch(r"[\d,.]+[KM]?|community plugin|small", c.strip()):
                metric = c.strip()
            else:
                desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", c)
        res.append({"file": fn, "kind": CAT.get(fn, "Link"), "group": group,
                    "name": link.group(1), "url": link.group(2),
                    "metric": metric, "desc": desc.strip()})

# extra links that live in prose, not tables
for f in [f"{ROOT}/resources/reading.md", f"{ROOT}/resources/papers.md"]:
    txt = open(f).read()
    group = ""
    for block in txt.split("\n\n"):
        h = re.search(r"^## (.+)$", block, re.M)
        if h: group = h.group(1).strip()
        for m in re.finditer(r"\*\*\[([^\]]+)\]\((https?://[^)]+)\)\*\*", block):
            if any(r["url"] == m.group(2) for r in res): continue
            clean = re.sub(r"\s+", " ", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", block))
            clean = re.sub(r"[*#>]", "", clean).strip()
            desc = clean.split(". ", 1)[1] if ". " in clean else clean
            res.append({"file": os.path.basename(f), "kind": CAT[os.path.basename(f)],
                        "group": group, "name": m.group(1), "url": m.group(2),
                        "metric": "", "desc": desc[:240]})

data = {"pages": pages, "sections": SECTION_TITLES, "order": sec_index,
        "graph": {"nodes": nodes, "edges": edges}, "resources": res,
        "stats": {"pages": len(pages), "words": sum(p["words"] for p in pages),
                  "sections": len(SECTION_TITLES), "links": len(res)}}
json.dump(data, open("site_data.json", "w"))
print("pages:", len(pages), "| resources:", len(res), "| section edges:", len(edges),
      "| words:", data["stats"]["words"])
