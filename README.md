# AI Second Brain

A knowledge base that an AI agent builds and maintains for you, in plain
markdown files you own. Everything you read, watch and save gets turned into
linked wiki pages, connected to everything already there, and you can ask it
questions.

This repo is the full version of the guide: the concepts, the setup, the vault
template, the agent skills, the scripts, and the resources. Free, no signup,
nothing to install beyond Obsidian and an agent.

## The problem it solves

You save things with the intention of coming back. You never do. Bookmarks,
screenshots, read-later queues and half-filled Notion pages accumulate without
compounding, because filing and linking them is boring work that humans stop
doing after two weeks.

Hand that work to an agent and the system stays alive. That is the whole idea.

## Quickstart

One evening. Nine steps, each with a full page behind it.

```bash
# copy the starter vault, skills, commands and agents
git clone https://github.com/undefined-ui/second-brain-os.git
cp -r second-brain-os/vault-template ~/brain

mkdir -p ~/brain/.claude
cp -r second-brain-os/skills   ~/brain/.claude/skills
cp -r second-brain-os/commands ~/brain/.claude/commands
cp -r second-brain-os/agents   ~/brain/.claude/agents

cd ~/brain && claude
```

1. [Install Obsidian](docs/02-setup/obsidian-install-and-vault.md) and open
   `~/brain` with "Open folder as vault"
2. [Set up Claude Code](docs/02-setup/claude-code-setup.md), in the terminal or
   the Code tab of the desktop app
3. [Connect over MCP](docs/02-setup/mcp-obsidian.md) if you want the agent to
   reach the vault from anywhere. Optional, skip it on day one
4. [Get interviewed for your CLAUDE.md](docs/02-setup/claude-md.md) instead of
   writing it by hand
5. [Set up the two layers](docs/02-setup/vault-structure.md): a wiki for what
   you know, projects for what you are doing
6. [Scope down to one project](docs/02-setup/project-scoping.md) when you want
   to ship something
7. Install the [Web Clipper](https://obsidian.md/clipper), clip an article to
   `raw/`, run `/ingest`
8. [Connect live data](docs/02-setup/live-data.md): calendar, email, chat
9. [Put maintenance on a schedule](docs/06-agents/scheduled-maintenance.md) and
   wake up to a vault that filed itself

Then feed it ten more sources before judging it. The graph is not interesting
at five pages and it is hard to look away from at fifty.

Full walkthrough: [Setup](docs/02-setup/README.md).

## How it works

```
   you                    raw/                 agent                 wiki/
 ┌───────┐          ┌──────────────┐      ┌────────────┐      ┌──────────────┐
 │ clip  │  ──────> │ articles     │ ───> │  ingest    │ ───> │ sources/     │
 │ save  │          │ transcripts  │      │  extract   │      │ concepts/    │
 │ dump  │          │ pdfs         │      │  link      │      │ entities/    │
 └───────┘          │ chat exports │      │  lint      │      │ synthesis/   │
                    └──────────────┘      └────────────┘      └──────────────┘
                                                │                     │
                                                │   ask anything      │
                                                └─────────────────────┘
```

Raw material is an archive you never read. The wiki is the artifact, written in
plain language, one idea per page, densely linked. New sources update existing
pages instead of piling up beside them, which is why the vault gets better as
it grows rather than just bigger.

Alongside the wiki sits a project layer: one folder per project, each with its
own `CLAUDE.md` and an `Inputs / Process / Outputs / Feedback` pipeline. The
wiki holds what you know, the projects hold what you are doing, and they feed
each other. [The two layers](docs/01-concepts/two-layers.md) covers why keeping
them separate matters more than it sounds.

## What is in here

| Folder | What it holds |
|---|---|
| [`docs/`](docs/README.md) | The guide. Ten sections, from the concept to troubleshooting |
| [`vault-template/`](vault-template/) | A starter vault: wiki structure, project pipeline, `CLAUDE.md` and page templates |
| [`skills/`](skills/README.md) | Agent skills: ingest, lint, query, review |
| [`commands/`](commands/README.md) | Slash commands for Claude Code |
| [`agents/`](agents/README.md) | Subagent definitions, two of them read-only by design |
| [`scripts/`](scripts/README.md) | Dependency-free Python for link checking, stats and graph export |
| [`resources/`](resources/README.md) | Tools, repos, papers and reading worth your time |
| [`examples/`](examples/README.md) | Real vaults and real output |

## The guide

Ten sections, 77 pages, written to be followed rather than skimmed. From the
concept through setup, capture, structure, the graph, automation, retrieval,
publishing, and what to do when each of them breaks.

| Section | What it covers |
|---|---|
| [Concepts](docs/01-concepts/README.md) | what the pattern is and why the old note systems died|
| [Setup](docs/02-setup/README.md) | Obsidian, Claude Code, `CLAUDE.md`, MCP, projects, git|
| [Ingestion](docs/03-ingestion/README.md) | articles, video, PDFs, chat exports, voice, backfilling|
| [Structuring](docs/04-structuring/README.md) | page types, linking rules, schema, contradictions|
| [Graphs](docs/05-graphs/README.md) | what the graph is for, typed links, GraphRAG, metrics|
| [Agents](docs/06-agents/README.md) | roles, schedules, hooks, guardrails|
| [Retrieval](docs/07-retrieval/README.md) | query patterns, search, context budget|
| [Outputs](docs/08-outputs/README.md) | writing, reports, publishing, learning|
| [Maintenance](docs/09-maintenance/README.md) | linting, review cadence, git, privacy, scaling|
| [Troubleshooting](docs/10-troubleshooting/README.md) | the failures everyone hits, with fixes|

## Design decisions

This setup is opinionated. The three rules that matter most, and why:

**Nothing is ingested until it is linked.** A page that lands unconnected is
invisible within a week. Linking is the entire value, so it happens in the same
run or the ingest is not finished.

**Contradictions are recorded, never overwritten.** When a new source disagrees
with a page, both positions stay, with dates and sources. The history of what
you believed and why is the one thing your vault has that a search engine does
not.

**No vector database until you need one.** A personal corpus is small and
already structured. Structured pages plus links answer questions that chunk
similarity cannot, at zero infrastructure cost. [When RAG earns its
place](docs/07-retrieval/rag-on-top.md) covers the threshold.

## Who this is for

Anyone who reads a lot and retains less than they want to: researchers,
engineers, writers, students, people who watch three hours of technical video a
week and remember none of it.

It is not for team wikis, it is not a Notion replacement, and it will not
organise a vault you never add to.

## Portability

Everything here is markdown files, wikilinks and `SKILL.md` files. It works with
Claude Code, and with any agent that reads files. Obsidian is a viewer for the
graph, not a dependency. If you walk away from every tool named in this repo,
you keep the folder and everything in it.

## Learning materials

The source document, and the research behind the design decisions in this guide.

**[Karpathy's llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**
(4 April 2026). The pattern everything here builds on. Short, written as an idea
file to paste into your own agent rather than as a spec. Read it first.

**[From Local to Global: A Graph RAG Approach to Query-Focused
Summarization](https://arxiv.org/abs/2404.16130)** (arXiv:2404.16130, Microsoft
Research). Why chunk retrieval fails on questions about a whole corpus, which is
exactly what people want from a second brain. Code:
[microsoft/graphrag](https://github.com/microsoft/graphrag).

**[HippoRAG: Neurobiologically Inspired Long-Term Memory for
LLMs](https://arxiv.org/abs/2405.14831)** (arXiv:2405.14831). Graph retrieval
with personalised PageRank for multi-hop questions. The closest published
analogue of an agent walking links outward from a page.

**[Lost in the Middle: How Language Models Use Long
Contexts](https://arxiv.org/abs/2307.03172)** (arXiv:2307.03172, TACL). The
empirical reason not to paste your whole vault into context, and the basis for
the [context budget](docs/07-retrieval/context-budget.md) rules here.

**[Andy Matuschak's notes](https://notes.andymatuschak.org)**. Evergreen notes,
written in public. Also the strongest argument against this whole approach: if
the writing is the thinking, delegating it means not doing it.

Plus **How to Take Smart Notes** (Ahrens) and **Building a Second Brain**
(Forte), both written before agents existed, which is what makes them worth
reading now. Full list with notes: [resources/reading.md](resources/reading.md)
and [resources/papers.md](resources/papers.md).

## Tools

**Core stack.** [Obsidian](https://obsidian.md) for storage,
[Web Clipper](https://obsidian.md/clipper) for capture,
[Claude Code](https://code.claude.com/docs/en/setup) for maintenance.

**Plugins.** [Dataview](https://github.com/blacksmithgu/obsidian-dataview) for
queries over frontmatter,
[Templater](https://github.com/SilentVoid13/Templater) for pages you write by
hand, and
[Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) if
you want MCP access. That plugin now ships a built-in MCP server, so a separate
one is often unnecessary; see [MCP for Obsidian](docs/02-setup/mcp-obsidian.md).

**Capture and processing.** [yt-dlp](https://github.com/yt-dlp/yt-dlp),
[youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api),
[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF),
[Zotero](https://www.zotero.org).

**Graph and search.** [ripgrep](https://github.com/BurntSushi/ripgrep),
[NetworkX](https://networkx.org), [Kuzu](https://kuzudb.com),
[Gephi](https://gephi.org).

Full list, including alternatives to Obsidian:
[resources/tools.md](resources/tools.md).

## Other implementations

Worth reading before writing your own page contracts.

- **[Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki)**.
  The pattern as one installable skill for Claude Code, Cursor and Codex.
  Its list of what the author deliberately did not build is the most useful part.
- **[micuintus/llm-wiki](https://github.com/micuintus/llm-wiki)**. Deliberately
  minimal, convention-based rather than code-enforced. Good counterpoint.
- **[NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain)**.
  Four skills installable through npm, close to the original gist.
- **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)**.
  Around 43 commands, works across Claude, Codex and Gemini.

More context on each: [resources/skills.md](resources/skills.md).

## Graph and publishing repos

Beyond implementations of the pattern itself.

**Graph views for Obsidian.** [Juggl](https://github.com/HEmile/juggl) for an
interactive workspace graph with typed edges,
[ExcaliBrain](https://github.com/zsviczian/excalibrain) for a structured
mind-map derived from your links and Dataview fields, and
[Breadcrumbs](https://github.com/michaelpporter/breadcrumbs) for typed links plus
trees, matrices and Mermaid views over them.

**GraphRAG.** [microsoft/graphrag](https://github.com/microsoft/graphrag) is the
reference implementation;
[nano-graphrag](https://github.com/gusye1234/nano-graphrag) is the same idea in
about 1,100 readable lines; [LightRAG](https://github.com/HKUDS/LightRAG) adds a
vector layer for cheaper incremental updates.
[Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) covers the
rest of the landscape.

**Publishing.** [Quartz](https://github.com/jackyzha0/quartz) turns a vault into
a static site with backlinks, local graph and search.

Notes on each, and how to judge a repo in this ecosystem:
[resources/repositories.md](resources/repositories.md).

## Contributing

Corrections, resources and real examples are welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md) first: every factual claim needs a primary
source, and tool listings need a reason to exist.

## Credit

The LLM wiki pattern is Andrej Karpathy's, published as a
[gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) on
4 April 2026. This repo is one implementation of it, plus the parts the gist
deliberately leaves undefined.

<!-- TODO before publishing:
     - add the link to the original article
     - screenshots: graph view at 30 days, an example concept page
     - social preview image in Settings -> General -->

MIT licensed.
