#!/usr/bin/env python3
"""Render Chinese articles using the English site's stable IDs and link graph.

Called by build_graph_site.py after the English pages and graph are written.
Translation sources live in docs/zh-CN/<section>/<page>.md. Missing future
translations use the English reader fallback; the validator reports coverage.
"""
import html
import json
from pathlib import Path
import posixpath
import re

import markdown
from site_links import tool_for_path

ROOT = Path(__file__).resolve().parent.parent
LOCALE = "zh-CN"
PREFIX = f"docs/{LOCALE}/"
GH_BLOB = "https://github.com/undefined-ui/second-brain-os/blob/main/"
GH_TREE = "https://github.com/undefined-ui/second-brain-os/tree/main/"


def plain(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def canonical(path):
    return "docs/" + path[len(PREFIX):] if path.startswith(PREFIX) else path


def render_translations(nodes, english_pages):
    """Produce reader content only; English nodes/edges/statistics stay intact."""
    by_id = {node["id"]: node for node in nodes}
    resources = {n["url"].rstrip("/"): n["id"] for n in nodes if n["type"] == "resource"}
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])
    output = {}
    for pid, english in english_pages.items():
        source = ROOT / PREFIX / (pid + ".md")
        if not source.exists():
            continue
        raw = source.read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", raw, re.M).group(1).strip()
        body = re.sub(r"^# .+\n", "", raw, count=1)
        # Explicit source anchors keep links working when read on GitHub. In the
        # website the corresponding heading receives the same ID instead.
        body = re.sub(r'^<a id="[^"]+"></a>\s*\n', '', body, flags=re.M)
        md.reset()
        rendered = md.convert(body)
        source_headings = re.findall(r'<h([1-6]) id="([^"]+)"', english["html"])
        translated_headings = re.findall(r'<h([1-6]) id="([^"]+)"', rendered)
        if [h[0] for h in source_headings] != [h[0] for h in translated_headings]:
            raise ValueError(f"Heading structure differs from English: {source.relative_to(ROOT)}")
        anchors = {zh[1]: en[1] for zh, en in zip(translated_headings, source_headings)}
        rendered = re.sub(r'(<h[1-6] id=")([^"]+)(")',
                          lambda m: m[1] + anchors[m[2]] + m[3], rendered)
        here = source.parent.relative_to(ROOT).as_posix()

        def fix_link(match):
            href, rest = match[1], match[2]
            if href.startswith("#"):
                fragment = anchors.get(href[1:], href[1:])
                return f'<a href="#{fragment}" data-anchor="{fragment}"{rest}>'
            if re.match(r"^(https?:|mailto:)", href):
                rid = resources.get(html.unescape(href).rstrip("/"))
                data = f' data-node="{rid}"' if rid else ""
                return f'<a href="{href}" class="ext"{data} target="_blank" rel="noopener"{rest}>'
            path, _, fragment = href.partition("#")
            rel = posixpath.normpath(posixpath.join(here, path))
            target = canonical(rel)
            if target.startswith("docs/") and target.endswith(".md"):
                parts = target[5:-3].split("/")
                if len(parts) == 2:
                    tid = "/".join(parts)
                    if tid in by_id and by_id[tid]["type"] == "page":
                        return f'<a href="#/read/{tid}" class="wiki" data-node="{tid}"{rest}>'
                    sid = "sec:" + parts[0]
                    if parts[1] == "README" and sid in by_id:
                        return f'<a href="#/n/{sid}" class="wiki" data-node="{sid}"{rest}>'
            if target in ("docs/README.md", "README.md", "docs/ROADMAP.md"):
                return f'<a href="#/" class="wiki" data-node="root"{rest}>'
            tool = tool_for_path(target, by_id)
            data = f' class="ext tool" data-node="{tool}"' if tool else ' class="ext"'
            url = (by_id[tool].get("url") or GH_BLOB + rel) if tool else (GH_TREE if (ROOT / rel).is_dir() else GH_BLOB) + rel
            if fragment:
                url += "#" + fragment
            return f'<a href="{url}"{data} target="_blank" rel="noopener"{rest}>'

        rendered = re.sub(r'<a href="([^"]*)"([^>]*)>', fix_link, rendered)
        rendered = re.sub(r'(<img[^>]+src=")(?!https?:|/|data:)([^"]+)"',
                          lambda m: m[1] + posixpath.normpath(posixpath.join(here, m[2])) + '"', rendered)
        heads = [{"id": a, "t": plain(b)} for a, b in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', rendered)]
        first = re.search(r"<p>(.*?)</p>", rendered, re.S)
        output[pid] = {"title": title, "html": rendered, "heads": heads,
                       "text": plain(rendered), "desc": plain(first[1]) if first else "",
                       "path": source.relative_to(ROOT).as_posix(), "lang": LOCALE}
    out = ROOT / "assets/site/pages-zh-cn.js"
    out.write_text("/* generated by tools/build_translations.py - do not edit */\nwindow.SBOS_PAGES_ZH=" +
                   json.dumps(output, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(f"Chinese articles: {len(output)}/{len(english_pages)}")
    return output


if __name__ == "__main__":
    def read_data(name, assignment):
        text = (ROOT / "assets/site" / name).read_text(encoding="utf-8")
        return json.loads(text.split(assignment, 1)[1].rstrip(";\n"))
    render_translations(read_data("graph-data.js", "window.SBOS_GRAPH=")["nodes"],
                        read_data("pages-data.js", "window.SBOS_PAGES="))
