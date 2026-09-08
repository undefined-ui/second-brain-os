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

| Source | What it gives you |
|---|---|
| **[Karpathy's llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** (4 Apr 2026) | The pattern everything here builds on. Short, written as an idea file to paste into your agent rather than as a spec. Read it first. |
| **[From Local to Global: GraphRAG](https://arxiv.org/abs/2404.16130)** arXiv:2404.16130 | Why chunk retrieval fails on questions about a whole corpus, which is exactly what people want from a second brain. Code: [microsoft/graphrag](https://github.com/microsoft/graphrag). |
| **[HippoRAG](https://arxiv.org/abs/2405.14831)** arXiv:2405.14831 | Graph retrieval with personalised PageRank for multi-hop questions. The closest published analogue of an agent walking links outward. |
| **[Lost in the Middle](https://arxiv.org/abs/2307.03172)** arXiv:2307.03172, TACL | The empirical reason not to paste your whole vault into context, and the basis for the [context budget](docs/07-retrieval/context-budget.md) rules. |
| **[Andy Matuschak's notes](https://notes.andymatuschak.org)** | Evergreen notes, written in public. Also the strongest argument against this approach: if the writing is the thinking, delegating it means not doing it. |
| **How to Take Smart Notes** (Ahrens) | Zettelkasten. Atomic notes and dense linking still hold; the manual labour is what killed it for most people. |
| **Building a Second Brain** (Forte) | Where the term comes from, and PARA. Most of the book is about maintenance work an agent removes. |

Full notes: [reading.md](resources/reading.md) and [papers.md](resources/papers.md).

## Tools and plugins

Obsidian plugins ranked by installs from the official community stats, September
2026. The full catalog is in [plugins.md](resources/plugins.md) and
[tools.md](resources/tools.md).

| Purpose | Pick | Installs |
|---|---|---|
| Agent in the editor | [Claudian](https://github.com/yishentu/claudian) | 2.0M |
| Agent in the editor | [Copilot](https://github.com/logancyang/obsidian-copilot) | 1.8M |
| Suggests links | [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) | 1.2M |
| MCP access | [Local REST API with MCP](https://github.com/coddingtonbear/obsidian-local-rest-api) | 712K |
| Queries over frontmatter | [Dataview](https://github.com/blacksmithgu/obsidian-dataview) | 4.9M |
| Templates | [Templater](https://github.com/SilentVoid13/Templater) | 5.5M |
| Version control | [Git](https://github.com/Vinzent03/obsidian-git) | 3.1M |
| Migrating in | [Importer](https://github.com/obsidianmd/obsidian-importer) | 1.6M |
| Broken links and orphans | [Find unlinked files](https://github.com/Vinzent03/find-unlinked-files) | 225K |
| Flashcards from notes | [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 592K |
| Structured mind-map | [ExcaliBrain](https://github.com/zsviczian/excalibrain) | 336K |
| Interactive graph | [Juggl](https://github.com/HEmile/juggl) | 136K |

Outside Obsidian: [Web Clipper](https://obsidian.md/clipper) for capture,
[Claude Code](https://code.claude.com/docs/en/setup) for maintenance,
[yt-dlp](https://github.com/yt-dlp/yt-dlp) and
[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) for processing,
[ripgrep](https://github.com/BurntSushi/ripgrep),
[NetworkX](https://networkx.org), [Kuzu](https://kuzudb.com) and
[Gephi](https://gephi.org) for the graph, and
[Quartz](https://github.com/jackyzha0/quartz) to publish.

## Skills and other implementations

Counted individually: a repo shipping sixteen skills counts as sixteen. Stars
from the GitHub API, September 2026.

| Repo | Stars | Ships |
|---|---|---|
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 14.7K | 16 skills, 3 subagents, role presets |
| [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | 2.2K | 1 skill covering ingest, compile, query, lint |
| [ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm) | 1.9K | 13 skills, 4 subagents, full starter kit |
| [coleam00/second-brain-starter](https://github.com/coleam00/second-brain-starter) | 768 | 1 skill that interviews you first |
| [NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain) | 704 | 4 skills, npm installer |
| [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | small | 47 commands, works across three agents |
| [micuintus/llm-wiki](https://github.com/micuintus/llm-wiki) | small | 1 skill, deliberately minimal |

Where the format itself is defined:
[anthropics/skills](https://github.com/anthropics/skills) (20 skills),
[obra/superpowers](https://github.com/obra/superpowers) (14),
[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
(index of 1,000+). Notes on each: [skills.md](resources/skills.md).

## Graph, RAG and memory repos

| Purpose | Repo | Stars |
|---|---|---|
| Build a graph from any folder | [Graphify](https://github.com/Graphify-Labs/graphify) | 116K |
| Graph RAG, incremental | [LightRAG](https://github.com/HKUDS/LightRAG) | 39K |
| Graph RAG, reference | [microsoft/graphrag](https://github.com/microsoft/graphrag) | 36K |
| Graph RAG, readable | [nano-graphrag](https://github.com/gusye1234/nano-graphrag) | 4.0K |
| Multi-hop retrieval | [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | 4.0K |
| The landscape | [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | 2.6K |
| Agent memory | [mem0](https://github.com/mem0ai/mem0) | 65K |
| Temporal knowledge graphs | [graphiti](https://github.com/getzep/graphiti) | 31K |
| Graph plus vector memory | [cognee](https://github.com/topoteretes/cognee) | 31K |
| MCP server index | [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 95K |

Alternative homes for a vault, from Logseq to AFFiNE, plus RAG frameworks and
AI-native note apps: [repositories.md](resources/repositories.md) and
[tools.md](resources/tools.md).

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
