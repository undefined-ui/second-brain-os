#!/usr/bin/env python3
"""Sync the course and handbook READMEs with the editorial order below.

COURSE and TRACKS hold each folder's title, blurb and page order. This script
checks every listed page exists, renders it once as a sanity check, and writes
docs/<folder>/README.md so the order on GitHub and on the site agree. The site
reads that order back from the READMEs:

    pip install markdown
    python3 scripts/build_tracks.py
    python3 tools/build_graph_site.py

It used to inject the pages into the old single-file index.html; the graph
page has its own builder now, so index.html is not touched here.
"""
import io, json, os, re, sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# the course: seven modules, three lessons each - theory, mechanics, practice.
# Built on Google's agent whitepapers and the five-layer frame.
COURSE = {
    "course-0-map": {
        "title": "0 · The map",
        "blurb": "What an agent is, the five layers around the model, and "
                 "when a workflow beats a loop.",
        "order": ["what-an-agent-is", "five-layers", "agents-or-workflows"],
    },
    "course-1-context": {
        "title": "1 · Context",
        "blurb": "What the model sees: attention, caching, the four places, "
                 "sessions and memory.",
        "order": ["how-models-read", "the-four-places", "context-practice"],
    },
    "course-2-loop": {
        "title": "2 · Loop",
        "blurb": "Who decides the next step: goal, checker, stop rule, "
                 "budget - and the hybrid that survives production.",
        "order": ["loops-vs-workflows", "the-four-parts", "loop-practice"],
    },
    "course-3-gate": {
        "title": "3 · The gate",
        "blurb": "Cheap decisions in front of expensive models: classifiers "
                 "first, System One models where they earn it.",
        "order": ["cheap-decisions", "gates-in-practice", "gate-practice"],
    },
    "course-4-harness": {
        "title": "4 · Harness",
        "blurb": "The office around the model: containment, guides, sensors, "
                 "permissions - built from the outside in.",
        "order": ["the-office", "the-four-rings", "harness-practice"],
    },
    "course-5-evals": {
        "title": "5 · Evals",
        "blurb": "The same test every month: behavioural checks on traces, "
                 "judged judges, golden sets that include failures.",
        "order": ["two-kinds-of-checks", "judges-and-golden-sets",
                  "evals-practice"],
    },
    "course-6-production": {
        "title": "6 · Production",
        "blurb": "From demo to deployed: gateways, tracing, cost, security - "
                 "and the day-one plan across all five layers.",
        "order": ["from-prototype", "operating-agents", "day-one-plan"],
    },
}

# page order inside each track is editorial, not alphabetical
TRACKS = {
    "track-graph": {
        "title": "Knowledge graphs",
        "blurb": "Graphs as agent memory: GraphRAG, extraction pipelines, "
                 "stores — then an evening build of a graph layer over "
                 "your own vault.",
        "order": ["why-graphs", "graphrag", "building-graphs-with-llms",
                  "graph-stores", "tools",
                  "build-extract", "build-query", "build-use", "resources"],
    },
    "track-jev": {
        "title": "Jev engineering",
        "module": ("3", "course-3-gate"),
        "blurb": "The gate is the layer; Jev is one way to build it. Typed "
                 "decisions with confidence scores instead of generated text "
                 "— and a build you can run before your Jev access lands.",
        "order": ["system-one-models", "what-jev-is-good-for",
                  "jev-in-an-agent-stack", "getting-started",
                  "build-decision-endpoint", "build-router",
                  "build-swap-in-jev", "resources"],
    },
    "track-harness": {
        "title": "Agent harnesses",
        "module": ("4", "course-4-harness"),
        "blurb": "The machinery around the model: loops, tools, context "
                 "engineering, the landscape — and a working harness in "
                 "an evening, about 150 lines.",
        "order": ["what-a-harness-is", "claude-code-as-harness",
                  "context-engineering", "tools-and-mcp",
                  "harness-landscape",
                  "build-the-loop", "build-guardrails", "build-graduate",
                  "resources"],
    },
    "track-loop": {
        "title": "Loop engineering",
        "module": ("2", "course-2-loop"),
        "blurb": "The control system around the agent: stop conditions, "
                 "critics, context hygiene — and an overnight loop you can "
                 "trust by morning.",
        "order": ["what-loop-engineering-is", "stop-conditions",
                  "critics-and-verification", "context-hygiene", "patterns",
                  "build-goal-test", "build-critic", "build-overnight",
                  "resources"],
    },
    "track-evals": {
        "title": "Eval engineering",
        "module": ("5", "course-5-evals"),
        "blurb": "Measurement as the discipline of AI products: golden sets, "
                 "judges that do not lie, agent trajectories — and your "
                 "first suite built in an afternoon.",
        "order": ["why-evals", "designing-evals", "llm-as-judge",
                  "agent-evals", "tooling",
                  "build-traces", "build-suite", "build-ci", "resources"],
    },
}

MD = markdown.Markdown(extensions=["fenced_code", "tables"])


def render_page(sec, fname):
    meta = COURSE.get(sec) or TRACKS[sec]
    path = os.path.join(ROOT, "docs", sec, fname + ".md")
    src = io.open(path, encoding="utf-8").read().strip()
    lines = src.split("\n")
    if not lines[0].startswith("# "):
        raise SystemExit(f"{path}: first line must be an H1 title")
    title = lines[0][2:].strip()
    body = "\n".join(lines[1:]).strip()
    MD.reset()
    html = MD.convert(body)
    # relative images resolve against the repo, wherever the page renders
    html = re.sub(r'(<img[^>]+src=")(?!https?:|/|docs/)',
                  lambda m: m.group(1) + f"docs/{sec}/", html)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    headings = re.findall(r"<h2[^>]*>(.*?)</h2>", html)
    links = []
    for href, label in re.findall(r'href="([^"]+\.md)"[^>]*>(.*?)</a>', html):
        to = sec + "/" + href.replace("./", "").replace(".md", "")
        links.append({"to": to, "label": re.sub(r"<[^>]+>", "", label)})
    return {
        "id": f"{sec}/{fname}",
        "path": f"docs/{sec}/{fname}.md",
        "section": sec,
        "section_title": meta["title"],
        "title": title,
        "html": html,
        "headings": headings,
        "words": len(text.split()),
        "text": text[:4000],
        "links": links,
    }


def main():
    D = {"pages": [], "sections": {}, "order": {}}
    build_group(D, COURSE, "course")
    build_group(D, TRACKS, "track")
    print("READMEs synced - now run: python3 tools/build_graph_site.py")


def build_group(D, group, kind):
    cards = []
    for sec, meta in group.items():
        missing = [f for f in meta["order"]
                   if not os.path.exists(os.path.join(ROOT, "docs", sec, f + ".md"))]
        if missing:
            print(f"skip {sec}: missing {', '.join(missing)}")
            continue
        pages = [render_page(sec, f) for f in meta["order"]]
        D["pages"].extend(pages)
        D["sections"][sec] = {"title": meta["title"], "blurb": meta["blurb"],
                              kind: True}
        D["order"][sec] = [p["id"] for p in pages]
        cards.append(
            f'<article><h3><a href="#{pages[0]["id"]}">{meta["title"]}</a></h3>'
            f'<p>{meta["blurb"]}</p>'
            f'<div class="pg">{len(pages)} pages</div></article>')
        # a browsable README per folder, kept in sync with the order
        toc = "\n".join(f"{n}. [{p['title']}]({os.path.basename(p['path'])})"
                        for n, p in enumerate(pages, 1))
        if kind == "course":
            label = ("A module of [the agents course](../README.md)"
                     " — read it on the site or in order below.")
        elif meta.get("module"):
            n, mdir = meta["module"]
            label = (f"The handbook for [module {n}](../{mdir}/README.md) of "
                     "the agents course: the module teaches the idea once; "
                     "this holds the full menu — techniques, tools and "
                     "builds. Read it on the site or dip in below.")
        else:
            label = ("One of [the handbooks](../README.md) — "
                     "the full menu for one layer; dip in anywhere.")
        io.open(os.path.join(ROOT, "docs", sec, "README.md"), "w",
                encoding="utf-8", newline="\n").write(
            f"# {meta['title']}\n\n{meta['blurb']}\n\n{label}\n\n{toc}\n")
        print(f"{sec}: {len(pages)} pages, "
              f"{sum(p['words'] for p in pages)} words")
    return cards


if __name__ == "__main__":
    main()
