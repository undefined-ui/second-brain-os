# Second Brain OS

Guides and resources for AI engineers: a course on building agents, five
handbooks that go deep on one layer each, hands-on projects, and the links worth
your time.

**Read it on the web:** [secondbrainos.dev](https://secondbrainos.dev/) puts
every page, term and tool from this repo on one interactive map.

## Why this repo?

AI engineering moves fast, and the useful parts are scattered across
whitepapers, engineering blogs and repos. This collects them into one path you
can follow: theory with sources, a build in every module, and a reading list
where every entry has a reason to be here. Here you will find:

- **The agents course:** seven modules from a single prompt to a production agent, covering context, loops, gates, harnesses, evals and production
- **Five handbooks** that go deep on one layer each: knowledge graphs, gates, harnesses, loops and evals
- **A hands-on project:** a second brain, a knowledge base an agent builds and maintains for you in plain markdown
- **A working toolkit:** a Claude Code plugin for the course, plus 18 skills, 72 slash commands and 6 subagents for the project
- **114 vetted resources**, and what landed this month, checked at the source
- **Plain markdown, MIT licensed.** No signup, nothing to install to read it

## Table of contents

- [Getting started](#getting-started)
- [New this month](#new-this-month)
- [Learn by level](#learn-by-level)
  - [🟢 Beginner (30 pages)](#-beginner)
  - [🟡 Intermediate (47 pages)](#-intermediate)
  - [🔴 Advanced (53 pages)](#-advanced)
- [Toolkit](#toolkit)
- [Resources](#resources)
- [How the second brain works](#how-the-second-brain-works)
- [Contributing](#contributing)
- [License and credit](#license-and-credit)

---

## Getting started

1. **New to building agents:** read [What an agent is](docs/course-0-map/what-an-agent-is.md), then the [agents course](docs/README.md#the-agents-course) in order. Seven modules, three lessons each.
2. **One layer of your agent is hurting:** open its [handbook](#-advanced). Graphs, gates, harnesses, loops or evals, and every one ends in a build.
3. **Want a project to practise on:** build the [second brain](docs/01-concepts/what-is-a-second-brain.md), a knowledge base an agent maintains for you. The quickstart is below.
4. **Staying current:** [New this month](#new-this-month) lists what landed recently, each item checked at its source.

<details>
<summary><b>Second brain quickstart</b></summary>

```bash
# copy the starter vault, skills, commands, agents and scripts
git clone https://github.com/undefined-ui/second-brain-os.git
cp -r second-brain-os/vault-template ~/brain

mkdir -p ~/brain/.claude
cp -r second-brain-os/skills   ~/brain/.claude/skills
cp -r second-brain-os/commands ~/brain/.claude/commands
cp -r second-brain-os/agents   ~/brain/.claude/agents
cp -r second-brain-os/scripts  ~/brain/scripts

# the folder READMEs are for reading on GitHub, not for the agent
rm ~/brain/.claude/*/README.md ~/brain/scripts/README.md

cd ~/brain && claude
```

Then follow the nine [Setup](docs/02-setup/README.md) pages in order. The
`scripts/` copy is what lets `/metrics`, `/health` and `/graph-export` run from
inside the vault. On Windows, use `python` where the guide says `python3`.

</details>

---

## New this month

What landed in September and October 2026 that changes how you would build any
of this. Checked on 1 November 2026, stars from the GitHub API that day. Notes
on each are in [`resources/`](resources/README.md).

#### Second brain and memory
- [**Basic Memory 1.0**](https://github.com/basicmachines-co/basic-memory/releases/tag/v1.0.0) - A local MCP server whose graph is plain markdown with wikilinks, and it reads and writes Obsidian vaults · 4.4K, AGPL-3.0
- [**ai-memory 3.0**](https://github.com/akitaonrails/ai-memory/releases/tag/v3.0.0) - A git-backed wiki of `.md` files fed by hooks from 20+ agents, now installable as a Claude Code plugin · 14.9K, MIT
- [**agent-memory**](https://github.com/tigerless-labs/agent-memory) - One markdown file per memory under a `MEMORY.md` index, with a search index you can delete and rebuild · 4.3K, MIT
- [**Hindsight 1.0**](https://github.com/vectorize-io/hindsight/releases/tag/v1.0.0) - The database-backed alternative, with knowledge pages it can write out as markdown · 57.7K, MIT
- [**deja-vu**](https://github.com/vshulcz/deja-vu) - Indexes the JSONL and SQLite transcripts 43 coding agents already write to disk into a local FTS5 store, with a git-committed `.deja/memory.jsonl` file · 1.4K, MIT
- [**LLM Wikis From First Principles**](https://github.com/decodingai-magazine/llm-wiki-workshop) - A hands-on workshop: three exercises, from a basic `raw/` to `wiki/` setup to a wiki that learns from queries
- [**EvalMem**](https://arxiv.org/abs/2609.22231) - Splits memory failures into not stored, not found and not used; a wiki layer on top gained 2.5 points

#### Graphs and retrieval
- [**Follow the Entities**](https://arxiv.org/abs/2609.37226) - One page per entity, linked to every document that mentions it: more evidence for fewer tokens. The llm-wiki pattern, measured
- [**Context as Infrastructure**](https://arxiv.org/abs/2610.41172) - A grep and BM25 harness with no vector index answered 85% of BrowseComp-Plus; compiled wikis saved tokens, not accuracy
- [**Keep Your Receipts**](https://arxiv.org/abs/2610.17719) - Record the evidence behind every merge and edge, and deleting a retracted source needs no model calls
- [**LiteRAG**](https://arxiv.org/abs/2609.10239) - Graph retrieval without an LLM on every hop: over 100x faster and 99% cheaper than GraphRAG Global and DRIFT
- [**LightRAG 1.5.7**](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.7) - Opt-in graph-first ingestion: build the graph with no embedding calls, add vectors later
- [**Ladybug**](https://github.com/LadybugDB/ladybug) - The maintained continuation of Kuzu, the embedded Cypher database archived in October 2025 · 1.9K, MIT

#### Claude Code and skills
- [**Agent Skills move to the Linux Foundation**](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation) - Anthropic handed the `SKILL.md` standard to the Agentic AI Foundation on 22 October, so the skills here are a neutral format now
- [**Mods**](https://code.claude.com/docs/en/plugins/mods/overview) - A new plugin part: JS or TS handlers that watch or rewrite tool calls and prompts and draw their own panes
- [**claude plugin eval**](https://code.claude.com/docs/en/plugin-evals) - Runs each case with and without your plugin and fails CI below a threshold
- [**/skill-doctor**](https://code.claude.com/docs/en/skills#find-unused-skills) - What each loaded skill costs in context on every turn, and which ones never fire
- [**AGENTS.md support**](https://code.claude.com/docs/en/memory#agents-md) - Claude Code reads `AGENTS.md` when there is no `CLAUDE.md`, so one file can serve several agents
- [**When to fold subagents into your main loop**](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop) - Anthropic's case for one loop with skills over a fleet of subagents, with a migration plan
- [**Elephant-Goldfish Model**](https://github.com/google/elephant-goldfish-model) - Google's plugin where reviewers with no prior context check a spec; installs in Claude Code, Codex and Antigravity · 9.1K, Apache-2.0

#### Agent engineering
- [**Harness²**](https://github.com/google-research/harness2) - Google Research tunes the harness, not the weights: prompts, tools and memory edited per task, lessons kept · 21.9K, Apache-2.0
- [**SoL-Pi**](https://github.com/NVlabs/SoL-Pi) - Four add-ons to the Pi harness that keep its score with 45 to 49 per cent less token traffic · 3.6K, MIT
- [**CliffCompaction**](https://arxiv.org/abs/2609.26779) - Compaction that only truncates or drops, never summarises a summary; up to 50% cheaper
- [**The Unreliable Progress Bar**](https://arxiv.org/abs/2609.08589) - Models misreport their own progress mid-task, so the runtime should own the stop rule
- [**Building effective agent automations**](https://claude.dev/blog/building-effective-agent-automations/) - Bookmarks, a ledger and a spend cap for an agent that runs on a schedule
- [**Automating eval design and hillclimbing**](https://claude.dev/blog/automating-eval-design-and-hillclimbing/) - Keep a change only if the train and the held-out split both improve. Read with [Hamel Husain's critique](https://hamel.dev/blog/posts/claude-auto-evals/)
- [**Frozen Judges, Moving Agents**](https://arxiv.org/abs/2609.34198) - A fixed LLM judge errs differently on each agent version, so judge-only scores cannot certify an upgrade
- [**OpenAI Decisions API**](https://developers.openai.com/api/docs/guides/decisions) - Typed answers instead of text, generally available on 22 October: the course's gate as an API. [Compared with Jev and others](https://hamel.dev/blog/posts/decision-model-evals/) as cheap judges
- [**How the Claude Code team does code review**](https://claude.dev/blog/solving-code-review-at-anthropic/) - Parallel finders, a voting verifier and a three-round cap took first-round passes from 65% to 78%

---

## Learn by level

Every page in the repo, in reading order. The course runs through all three
levels, the second-brain project runs from beginner to intermediate, and the
handbooks are references for when one layer of your agent starts hurting.

### 🟢 Beginner

What an agent is and what it actually sees, then a first project: a knowledge base an agent builds for you. No agent experience needed.

#### [The map](docs/course-0-map/README.md) <sub>course module 0</sub>
- [**What an agent is**](docs/course-0-map/what-an-agent-is.md) - An application that plans and acts toward a goal, not a model
- [**Five layers, one system**](docs/course-0-map/five-layers.md) - Context, loop, gate, harness, evals: the system around the model
- [**Agents or workflows**](docs/course-0-map/agents-or-workflows.md) - If you can write the steps down, build a workflow

#### [Context](docs/course-1-context/README.md) <sub>course module 1</sub>
- [**How models read context**](docs/course-1-context/how-models-read.md) - Attention, caching and why a bigger window is not free
- [**The four places**](docs/course-1-context/the-four-places.md) - System prompt, tools, history, tail: what goes where
- [**Context in practice**](docs/course-1-context/context-practice.md) - Audit and restructure a real agent's context

#### [Concepts](docs/01-concepts/README.md) <sub>second brain 01</sub>
- [**What a second brain actually is**](docs/01-concepts/what-is-a-second-brain.md) - One folder of plain text an agent reads, writes and answers from
- [**The save-for-later paradox**](docs/01-concepts/the-save-for-later-paradox.md) - Why saved links never compound, and what has to change
- [**The LLM wiki pattern**](docs/01-concepts/llm-wiki-pattern.md) - Karpathy's April 2026 gist, the pattern this repo implements
- [**The two layers**](docs/01-concepts/two-layers.md) - A wiki for what you know, projects for what you are doing
- [**Why markdown and plain text**](docs/01-concepts/why-markdown-and-plain-text.md) - Why the file format decides whether the system survives
- [**Zettelkasten, PARA, evergreen notes**](docs/01-concepts/pkm-lineage.md) - The old methods were mostly right; which parts still apply
- [**Wiki vs RAG**](docs/01-concepts/wiki-vs-rag.md) - Why a linked wiki beats a vector database for a personal corpus
- [**What good looks like**](docs/01-concepts/what-good-looks-like.md) - Concrete signs it is working, from week one to month six

#### [Setup](docs/02-setup/README.md) <sub>second brain 02</sub>
- [**Obsidian and your first vault**](docs/02-setup/obsidian-install-and-vault.md) - The storage half: free, local, plain text, with a graph view
- [**Claude Code in the vault**](docs/02-setup/claude-code-setup.md) - Run Claude Code in the vault, in the terminal or the desktop app
- [**MCP for Obsidian**](docs/02-setup/mcp-obsidian.md) - Give the agent a door into Obsidian over MCP. Optional on day one
- [**Writing your CLAUDE.md**](docs/02-setup/claude-md.md) - Get interviewed for the file the agent reads every session
- [**Vault structure**](docs/02-setup/vault-structure.md) - Lay out the wiki and project layers in one folder tree
- [**Project scoping**](docs/02-setup/project-scoping.md) - Scope the agent to one project so quality holds as the vault grows
- [**Live data connectors**](docs/02-setup/live-data.md) - Connect calendar, email and chat so the vault sees what changes
- [**Plugins worth installing**](docs/02-setup/obsidian-plugins.md) - The plugins worth adding, each for one specific problem
- [**Git, sync and backups**](docs/02-setup/git-and-sync.md) - Git, sync and backups that make unattended runs safe

#### [Ingestion](docs/03-ingestion/README.md) <sub>second brain 03</sub>
- [**Web articles**](docs/03-ingestion/web-clipper.md) - Clip articles into raw/ in one click
- [**YouTube and podcasts**](docs/03-ingestion/youtube-transcripts.md) - Turn videos and podcasts into transcripts the agent can file
- [**PDFs, papers and books**](docs/03-ingestion/pdfs-and-books.md) - Get PDFs, papers and books in without garbled text
- [**Chat exports**](docs/03-ingestion/chat-exports.md) - Import your chat history, your richest and most sensitive source
- [**Voice notes and meetings**](docs/03-ingestion/voice-and-meetings.md) - Capture voice notes and meetings away from the desk
- [**Newsletters and email**](docs/03-ingestion/newsletters-and-email.md) - Automate newsletter capture without flooding the wiki
- [**Backfilling years of material**](docs/03-ingestion/bulk-backfill.md) - Import years of bookmarks and downloads in controlled batches

---

### 🟡 Intermediate

How an agent loops and decides, and the second brain grown into a graph that maintains itself and answers real questions.

#### [Loop](docs/course-2-loop/README.md) <sub>course module 2</sub>
- [**Loops versus workflows**](docs/course-2-loop/loops-vs-workflows.md) - When the model, not your code, should choose the next step
- [**The four parts of a loop**](docs/course-2-loop/the-four-parts.md) - Goal, an outside checker, a stop rule, a budget
- [**Loop practice: filter, loop, fall back**](docs/course-2-loop/loop-practice.md) - Filter first, loop briefly, fall back: the production pattern

#### [The gate](docs/course-3-gate/README.md) <sub>course module 3</sub>
- [**Cheap Decisions**](docs/course-3-gate/cheap-decisions.md) - Cheap classifiers in front of expensive models
- [**Gates in Practice**](docs/course-3-gate/gates-in-practice.md) - Measuring a gate: how often it is right, and how sure it is
- [**Gate Practice**](docs/course-3-gate/gate-practice.md) - Label a few hundred examples and train a baseline first

#### [Structuring](docs/04-structuring/README.md) <sub>second brain 04</sub>
- [**One page, one idea**](docs/04-structuring/atomic-pages.md) - One idea per page, explained so it stands alone
- [**The four page types**](docs/04-structuring/page-types.md) - Source, concept, entity, synthesis: four types, four jobs
- [**Linking rules**](docs/04-structuring/linking-rules.md) - The rules that turn a folder of files into a graph
- [**Frontmatter schema**](docs/04-structuring/frontmatter-schema.md) - The YAML fields that make the vault queryable
- [**Naming and aliases**](docs/04-structuring/naming-and-aliases.md) - Names and aliases, the keys every wikilink resolves by
- [**Deduplication and merging**](docs/04-structuring/dedupe-and-merge.md) - Find and merge duplicate pages without breaking links
- [**Contradictions and supersession**](docs/04-structuring/contradictions-and-supersession.md) - Record disagreements with dates and sources, never overwrite
- [**index.md and log.md**](docs/04-structuring/index-and-log.md) - The catalog the agent reads first and the log that makes runs auditable

#### [Graphs](docs/05-graphs/README.md) <sub>second brain 05</sub>
- [**Graph basics for a knowledge base**](docs/05-graphs/graph-basics.md) - Your vault is already a graph: what that means in practice
- [**Reading the Obsidian graph view**](docs/05-graphs/obsidian-graph-view.md) - The graph views that actually tell you something
- [**Typed links**](docs/05-graphs/typed-links.md) - Links that say how two pages relate, and when to type them
- [**Graph vs embeddings**](docs/05-graphs/graph-vs-vectors.md) - Why structured links answer what similarity search cannot
- [**GraphRAG and where it fits**](docs/05-graphs/graphrag.md) - What GraphRAG is and why you probably do not need it yet
- [**Exporting the graph**](docs/05-graphs/exporting-your-graph.md) - Get the graph out of Obsidian to compute on it
- [**Graph metrics worth tracking**](docs/05-graphs/metrics.md) - Four numbers, checked monthly, that show whether it works

#### [Agents](docs/06-agents/README.md) <sub>second brain 06</sub>
- [**Agent roles**](docs/06-agents/agent-roles.md) - Ingestor, linker, reviewer: one job per agent
- [**Scheduling**](docs/06-agents/scheduled-maintenance.md) - Scheduled runs that file, link and report while you sleep
- [**Subagents and parallel work**](docs/06-agents/subagents.md) - Subagents with their own context for parallel reading
- [**Hooks**](docs/06-agents/hooks.md) - Hooks for the rules a prompt instruction will eventually forget
- [**Skills and slash commands**](docs/06-agents/skills-and-commands.md) - Skills vs slash commands, and when to use each
- [**Guardrails**](docs/06-agents/safety-and-guardrails.md) - What the agent may touch, and the walls that hold when it is wrong

#### [Retrieval](docs/07-retrieval/README.md) <sub>second brain 07</sub>
- [**Asking the vault**](docs/07-retrieval/asking-questions.md) - Answers grounded in your pages, not the model's memory
- [**Query patterns**](docs/07-retrieval/query-patterns.md) - The questions a vault answers better than a search engine
- [**Search tools**](docs/07-retrieval/search-tools.md) - Grep, ripgrep and Obsidian search: almost always enough
- [**Adding RAG when you need it**](docs/07-retrieval/rag-on-top.md) - The threshold where adding RAG starts to pay
- [**Context budget**](docs/07-retrieval/context-budget.md) - Why reading more pages makes answers worse, and the budget rules

#### [Outputs](docs/08-outputs/README.md) <sub>second brain 08</sub>
- [**Writing from the vault**](docs/08-outputs/writing-from-the-vault.md) - Write from research that is already done, cited and linked
- [**Research reports**](docs/08-outputs/research-reports.md) - Reports for questions the vault cannot answer yet
- [**Publishing and export**](docs/08-outputs/publishing-and-export.md) - Publish the public part of your vault, keep the rest private
- [**Learning from your own vault**](docs/08-outputs/teaching-yourself.md) - Quizzes and review that turn saved pages into things you know

#### [Maintenance](docs/09-maintenance/README.md) <sub>second brain 09</sub>
- [**Linting the vault**](docs/09-maintenance/lint-and-health.md) - Catch broken links, orphans and missing fields before they rot
- [**Review cadence**](docs/09-maintenance/review-cadence.md) - Weekly and monthly reviews that keep you in the loop
- [**Versioning**](docs/09-maintenance/versioning-with-git.md) - Every agent change as a diff you can read and revert
- [**Backups and portability**](docs/09-maintenance/backups-and-portability.md) - The backup mistake almost everyone makes
- [**Privacy**](docs/09-maintenance/privacy-and-secrets.md) - Keep secrets out of pages, prompts and public exports
- [**Scaling past a thousand pages**](docs/09-maintenance/scaling.md) - What strains past a thousand pages, and what to change

#### [Troubleshooting](docs/10-troubleshooting/README.md) <sub>second brain 10</sub>
- [**The failures everyone hits**](docs/10-troubleshooting/common-failures.md) - The failures everyone hits, usually in capture, with fixes
- [**The agent writes garbage**](docs/10-troubleshooting/agent-writes-garbage.md) - Fix pages that are on topic and useless to read
- [**Broken links and orphans**](docs/10-troubleshooting/broken-links.md) - Repair broken links and orphans after agent renames
- [**The vault got too big**](docs/10-troubleshooting/vault-too-big.md) - When answers get slow and vague as the vault grows
- [**FAQ**](docs/10-troubleshooting/faq.md) - MCP, other agents, cost, local models, Notion imports

---

### 🔴 Advanced

Harden, measure and ship agents, then go deep on one layer at a time. Every handbook ends in a build you can finish in an evening.

#### [Harness](docs/course-4-harness/README.md) <sub>course module 4</sub>
- [**The Office**](docs/course-4-harness/the-office.md) - The model is only as good as the office around it
- [**The Four Rings**](docs/course-4-harness/the-four-rings.md) - Containment, guides, sensors, permissions, built from the outside in
- [**Harness Practice**](docs/course-4-harness/harness-practice.md) - Harden a real coding agent, step by step

#### [Evals](docs/course-5-evals/README.md) <sub>course module 5</sub>
- [**Two Kinds of Checks**](docs/course-5-evals/two-kinds-of-checks.md) - Behavioural checks on traces vs end-to-end grading
- [**Judges and Golden Sets**](docs/course-5-evals/judges-and-golden-sets.md) - LLM judges you can trust and golden sets that include failures
- [**Evals Practice**](docs/course-5-evals/evals-practice.md) - A minimal eval suite in one afternoon

#### [Production](docs/course-6-production/README.md) <sub>course module 6</sub>
- [**From Prototype to Production**](docs/course-6-production/from-prototype.md) - What changes when other people, or a 3am scheduler, depend on it
- [**Operating Agents**](docs/course-6-production/operating-agents.md) - What it is doing, what it costs, what it could break
- [**The Day-One Plan**](docs/course-6-production/day-one-plan.md) - The whole course compressed into one working day

#### [Knowledge graphs](docs/track-graph/README.md) <sub>handbook T1</sub>
- [**Why Knowledge Graphs**](docs/track-graph/why-graphs.md) - Facts arrive connected; a graph keeps the connections
- [**GraphRAG**](docs/track-graph/graphrag.md) - How GraphRAG works and when it earns its cost
- [**Building Graphs with LLMs**](docs/track-graph/building-graphs-with-llms.md) - Entity and relation extraction pipelines with LLMs
- [**Graph Stores**](docs/track-graph/graph-stores.md) - Where the graph should live, from plain text upward
- [**Tools**](docs/track-graph/tools.md) - The graph tooling landscape, September 2026
- [**Build: Extract the Graph**](docs/track-graph/build-extract.md) - Build 1: extract a graph from your vault
- [**Build: Query It**](docs/track-graph/build-query.md) - Build 2: query it
- [**Build: Put It in the Loop**](docs/track-graph/build-use.md) - Build 3: put it in the agent's loop
- [**Resources**](docs/track-graph/resources.md) - Papers, repos and tools, checked September 2026

#### [Jev engineering](docs/track-jev/README.md) <sub>handbook T2</sub>
- [**System One Models**](docs/track-jev/system-one-models.md) - Small models that return typed decisions instead of text
- [**What Jev Is Good For**](docs/track-jev/what-jev-is-good-for.md) - Tasks that reduce to picking an answer from a schema
- [**Jev in an Agent Stack**](docs/track-jev/jev-in-an-agent-stack.md) - Jev next to an LLM, making the small decisions
- [**Getting Started With Jev**](docs/track-jev/getting-started.md) - Access, the API shape and a realistic first project
- [**Build: a Typed Decision Endpoint**](docs/track-jev/build-decision-endpoint.md) - Build 1: a typed decision endpoint
- [**Build: the Confidence-Gated Router**](docs/track-jev/build-router.md) - Build 2: a confidence-gated router
- [**Build: the Jev Swap**](docs/track-jev/build-swap-in-jev.md) - Build 3: swap Jev in behind the same contract
- [**Jev Resources**](docs/track-jev/resources.md) - Links on Jev and System One models

#### [Agent harnesses](docs/track-harness/README.md) <sub>handbook T3</sub>
- [**What a Harness Is**](docs/track-harness/what-a-harness-is.md) - Loop, tools, prompts, permissions: everything around the model
- [**Claude Code as Harness**](docs/track-harness/claude-code-as-harness.md) - Claude Code and the Agent SDK as a reference harness
- [**Context Engineering**](docs/track-harness/context-engineering.md) - What the model sees at each step, and why
- [**Tools and MCP**](docs/track-harness/tools-and-mcp.md) - Tool design and MCP, where agents quietly fail
- [**Harness Landscape**](docs/track-harness/harness-landscape.md) - The harnesses alive in September 2026, one honest take each
- [**Build: the Loop**](docs/track-harness/build-the-loop.md) - Build 1: an agent loop in about seventy lines of Python
- [**Build: Permissions and Context**](docs/track-harness/build-guardrails.md) - Build 2: permissions and context limits
- [**Build: Know When to Graduate**](docs/track-harness/build-graduate.md) - Build 3: when to move to a real framework
- [**Resources**](docs/track-harness/resources.md) - Harness reading, checked September 2026

#### [Loop engineering](docs/track-loop/README.md) <sub>handbook T4</sub>
- [**What Loop Engineering Is**](docs/track-loop/what-loop-engineering-is.md) - The control system that runs an agent
- [**Stop Conditions**](docs/track-loop/stop-conditions.md) - Making a loop stop, and not report success it has not earned
- [**Critics and Verification**](docs/track-loop/critics-and-verification.md) - Judges that verify the work outside the model
- [**Context Hygiene**](docs/track-loop/context-hygiene.md) - Fresh context for every attempt, and why it works
- [**Patterns**](docs/track-loop/patterns.md) - Five loop shapes and their failure modes
- [**Build: the Goal Test**](docs/track-loop/build-goal-test.md) - Build 1: define done as a script
- [**Build: the Critic**](docs/track-loop/build-critic.md) - Build 2: add a critic pass
- [**Build: the Overnight Loop**](docs/track-loop/build-overnight.md) - Build 3: an overnight loop you can trust by morning
- [**Resources**](docs/track-loop/resources.md) - Loop engineering reading

#### [Eval engineering](docs/track-evals/README.md) <sub>handbook T5</sub>
- [**Why Evals**](docs/track-evals/why-evals.md) - Evals are the tests of AI products
- [**Designing Evals**](docs/track-evals/designing-evals.md) - From failure modes to test cases
- [**LLM as Judge**](docs/track-evals/llm-as-judge.md) - When a model grades, and how to check the grader
- [**Agent Evals**](docs/track-evals/agent-evals.md) - Evaluating trajectories, not just final answers
- [**Eval Tooling**](docs/track-evals/tooling.md) - Eval platforms, frameworks and CLIs worth knowing
- [**Build: Read Your Traces**](docs/track-evals/build-traces.md) - Build 1: from traces to a golden set
- [**Build: the Suite**](docs/track-evals/build-suite.md) - Build 2: a runnable suite in one Python file
- [**Build: the Gate**](docs/track-evals/build-ci.md) - Build 3: gate every pull request in GitHub Actions
- [**Eval Resources**](docs/track-evals/resources.md) - A short eval reading list

---

## Toolkit

#### [The agents-course plugin](plugins/README.md) <sub>each tool does one module's practice page in your repo</sub>

```bash
claude plugin marketplace add undefined-ui/second-brain-os
claude plugin install agents-course@second-brain-os
```

- [**context-audit**](plugins/agents-course/skills/context-audit/SKILL.md) - Measure the four places, find cache killers and window bloat
- [**goal-test**](plugins/agents-course/skills/goal-test/SKILL.md) - Turn a task into a testable done, with the script and a bounded loop
- [**gate-check**](plugins/agents-course/skills/gate-check/SKILL.md) - Find the decisions that do not need the big model
- [**harness-audit**](plugins/agents-course/skills/harness-audit/SKILL.md) - Walk the four rings, state the blast radius, rank the fixes
- [**evals-bootstrap**](plugins/agents-course/skills/evals-bootstrap/SKILL.md) - Mine real failures into cases and generate the trace checker
- [**loop-critic**](plugins/agents-course/agents/loop-critic.md) - An agent that reviews loop results in a clean context

#### [Skills](skills/README.md) <sub>second brain, one per workflow</sub>
- [**second-brain-ingest**](skills/second-brain-ingest/SKILL.md) - Turn raw sources into linked wiki pages
- [**second-brain-backfill**](skills/second-brain-backfill/SKILL.md) - Import a large archive in checkpointed batches
- [**second-brain-chat-import**](skills/second-brain-chat-import/SKILL.md) - Triage an exported chat history, privacy pass first
- [**second-brain-transcript**](skills/second-brain-transcript/SKILL.md) - Clean a raw transcript before it is ingested
- [**second-brain-lint**](skills/second-brain-lint/SKILL.md) - Find and repair broken links, orphans, stubs and bad frontmatter
- [**second-brain-merge**](skills/second-brain-merge/SKILL.md) - Merge duplicate pages, keep every claim, redirect the links
- [**second-brain-rename**](skills/second-brain-rename/SKILL.md) - Rename a page and fix every inbound link
- [**second-brain-graph**](skills/second-brain-graph/SKILL.md) - Report the graph's shape: orphans, hubs, bridges, clusters
- [**second-brain-metrics**](skills/second-brain-metrics/SKILL.md) - Dated health snapshots so trends are visible
- [**second-brain-query**](skills/second-brain-query/SKILL.md) - Answer from the vault's own pages, with citations
- [**second-brain-changed-my-mind**](skills/second-brain-changed-my-mind/SKILL.md) - Trace where your recorded position has shifted
- [**second-brain-report**](skills/second-brain-report/SKILL.md) - Research reports with gaps, citations and disagreements
- [**second-brain-write**](skills/second-brain-write/SKILL.md) - Draft from your concept pages, citations kept
- [**second-brain-quiz**](skills/second-brain-quiz/SKILL.md) - Find out what you saved but never learned
- [**second-brain-review**](skills/second-brain-review/SKILL.md) - The periodic review: what grew, what conflicts, what is open
- [**second-brain-project**](skills/second-brain-project/SKILL.md) - Set up a project pipeline with its own `CLAUDE.md`
- [**second-brain-publish**](skills/second-brain-publish/SKILL.md) - Check what would leak before anything is published
- [**second-brain-privacy**](skills/second-brain-privacy/SKILL.md) - Find credentials and private material in the vault

#### [Subagents](agents/README.md) <sub>second brain, four of them read-only</sub>
- [**ingestor**](agents/ingestor.md) - Processes new material in `raw/` into linked wiki pages
- [**linker**](agents/linker.md) - Finds and adds missing connections between existing pages
- [**researcher**](agents/researcher.md) - Answers a question that spans many pages and flags what is missing. Read-only
- [**reviewer**](agents/reviewer.md) - Writes the periodic review of what the vault learned. Read-only
- [**graph-analyst**](agents/graph-analyst.md) - Reports graph metrics, hubs, bridges and clusters. Read-only
- [**curator**](agents/curator.md) - Proposes what to prune, archive or merge, never acts. Read-only

#### [Slash commands](commands/README.md) <sub>second brain, 72</sub>
Scoped entry points into the skills, in nine groups: ingestion, structuring,
graph, retrieval, maintenance, outputs, projects, safety and setup. Start with
`/ingest`, `/ask`, `/lint` and `/review`.

#### [Scripts](scripts/README.md) <sub>dependency-free Python</sub>
- [**link_check.py**](scripts/link_check.py) - Broken wikilinks, orphan pages, stubs
- [**vault_stats.py**](scripts/vault_stats.py) - Page counts, link density, orphan rate, most-linked pages
- [**graph_export.py**](scripts/graph_export.py) - The wikilink graph as CSV edges or GraphML for Gephi
- [**chat_export_to_md.py**](scripts/chat_export_to_md.py) - A chat history export as per-conversation markdown

#### [Starter vault](vault-template/)
- [**vault-template/**](vault-template/) - `CLAUDE.md` with page contracts and linking rules, the `raw/` to `wiki/` layout, a project pipeline and four page templates

---

## Resources

Curated, not comprehensive. The full catalog, filterable, is at
[secondbrainos.dev/resources.html](https://secondbrainos.dev/resources.html),
with notes on every entry in [`resources/`](resources/README.md).

#### Reading lists by topic
- [**Agent harnesses**](docs/track-harness/resources.md) - Harness reading, checked September 2026
- [**Loop engineering**](docs/track-loop/resources.md) - Long-running loops, critics and stop conditions
- [**Eval engineering**](docs/track-evals/resources.md) - A short eval reading list where everything earns its place
- [**Knowledge graphs**](docs/track-graph/resources.md) - Papers, repos and tools, checked September 2026
- [**Jev and System One models**](docs/track-jev/resources.md) - Links on decision models, checked a week after Jev launched

#### Graph, RAG and memory <sub>stars, September 2026</sub>
- [**Graphify**](https://github.com/Graphify-Labs/graphify) - Builds a graph from any folder · 116K
- [**LightRAG**](https://github.com/HKUDS/LightRAG) - Graph RAG with incremental updates · 39K
- [**microsoft/graphrag**](https://github.com/microsoft/graphrag) - The reference GraphRAG implementation · 36K
- [**nano-graphrag**](https://github.com/gusye1234/nano-graphrag) - The same pipeline in readable code · 4.0K
- [**HippoRAG**](https://github.com/OSU-NLP-Group/HippoRAG) - Multi-hop retrieval over a knowledge graph · 4.0K
- [**Awesome-GraphRAG**](https://github.com/DEEP-PolyU/Awesome-GraphRAG) - The landscape in one list · 2.6K
- [**mem0**](https://github.com/mem0ai/mem0) - Memory for agents · 65K
- [**graphiti**](https://github.com/getzep/graphiti) - Temporal knowledge graphs · 31K
- [**cognee**](https://github.com/topoteretes/cognee) - Graph plus vector memory · 31K
- [**awesome-mcp-servers**](https://github.com/punkpeye/awesome-mcp-servers) - An index of MCP servers · 95K

#### Second brain: start here
- [**Karpathy's llm-wiki gist**](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) - The pattern the project builds on, 4 April 2026. Read it first
- [**From Local to Global: GraphRAG**](https://arxiv.org/abs/2404.16130) - Why chunk retrieval fails on questions about a whole corpus
- [**HippoRAG**](https://arxiv.org/abs/2405.14831) - Graph retrieval with personalised PageRank, the closest analogue of an agent walking links
- [**Lost in the Middle**](https://arxiv.org/abs/2307.03172) - The evidence for keeping context small, and the basis for the [context budget](docs/07-retrieval/context-budget.md)
- [**Andy Matuschak's notes**](https://notes.andymatuschak.org) - Evergreen notes, and the strongest argument against delegating the writing
- **How to Take Smart Notes** (Ahrens) and **Building a Second Brain** (Forte) - Zettelkasten and PARA, the methods an agent now does the upkeep for

#### Second brain: Obsidian plugins <sub>installs, September 2026</sub>
- [**Claudian**](https://github.com/yishentu/claudian) - An agent in the editor · 2.0M
- [**Copilot**](https://github.com/logancyang/obsidian-copilot) - An agent in the editor · 1.8M
- [**Smart Connections**](https://github.com/brianpetro/obsidian-smart-connections) - Suggests links · 1.2M
- [**Local REST API with MCP**](https://github.com/coddingtonbear/obsidian-local-rest-api) - MCP access to the vault · 712K
- [**Dataview**](https://github.com/blacksmithgu/obsidian-dataview) - Queries over frontmatter · 4.9M
- [**Templater**](https://github.com/SilentVoid13/Templater) - Templates · 5.5M
- [**Git**](https://github.com/Vinzent03/obsidian-git) - Version control · 3.1M
- [**Importer**](https://github.com/obsidianmd/obsidian-importer) - Migrating in from other apps · 1.6M
- [**Find unlinked files**](https://github.com/Vinzent03/find-unlinked-files) - Broken links and orphans · 225K
- [**Spaced Repetition**](https://github.com/st3v3nmw/obsidian-spaced-repetition) - Flashcards from your notes · 592K
- [**ExcaliBrain**](https://github.com/zsviczian/excalibrain) - A structured mind map · 336K
- [**Juggl**](https://github.com/HEmile/juggl) - An interactive graph · 136K

#### Second brain: other implementations <sub>stars, September 2026</sub>
- [**AgriciDaniel/claude-obsidian**](https://github.com/AgriciDaniel/claude-obsidian) - 16 skills, 3 subagents, role presets · 14.7K
- [**Astro-Han/karpathy-llm-wiki**](https://github.com/Astro-Han/karpathy-llm-wiki) - 1 skill covering ingest, compile, query and lint · 2.2K
- [**ballred/obsidian-claude-pkm**](https://github.com/ballred/obsidian-claude-pkm) - 13 skills, 4 subagents, a full starter kit · 1.9K
- [**coleam00/second-brain-starter**](https://github.com/coleam00/second-brain-starter) - 1 skill that interviews you first · 768
- [**NicholasSpisak/second-brain**](https://github.com/NicholasSpisak/second-brain) - 4 skills with an npm installer · 704
- [**eugeniughelbur/obsidian-second-brain**](https://github.com/eugeniughelbur/obsidian-second-brain) - 47 commands across three agents
- [**micuintus/llm-wiki**](https://github.com/micuintus/llm-wiki) - 1 skill, deliberately minimal
- Where the skill format itself is defined: [anthropics/skills](https://github.com/anthropics/skills), [obra/superpowers](https://github.com/obra/superpowers) and the [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) index of 1,000+

#### Second brain: outside Obsidian
[Web Clipper](https://obsidian.md/clipper) for capture,
[Claude Code](https://code.claude.com/docs/en/setup) for maintenance,
[yt-dlp](https://github.com/yt-dlp/yt-dlp) and
[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) for processing,
[ripgrep](https://github.com/BurntSushi/ripgrep),
[NetworkX](https://networkx.org), [Ladybug](https://github.com/LadybugDB/ladybug) and
[Gephi](https://gephi.org) for the graph, and
[Quartz](https://github.com/jackyzha0/quartz) to publish.

---

## How the second brain works

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

Raw material is an archive you never read. The wiki is the artifact: plain
language, one idea per page, densely linked. New sources update existing pages
instead of piling up beside them, which is why the vault gets better as it
grows rather than just bigger. Beside the wiki sits a project layer, one folder
per project with its own `CLAUDE.md`. The wiki holds what you know, the
projects hold what you are doing. [The two layers](docs/01-concepts/two-layers.md)
covers why keeping them apart matters.

Three rules the project rests on:

- **Nothing is ingested until it is linked.** A page that lands unconnected is invisible within a week, so linking happens in the same run or the ingest is not finished.
- **Contradictions are recorded, never overwritten.** Both positions stay, with dates and sources. The history of what you believed and why is the one thing your vault has that a search engine does not.
- **No vector database until you need one.** Structured pages plus links answer questions chunk similarity cannot, at zero infrastructure cost. [When RAG earns its place](docs/07-retrieval/rag-on-top.md) names the threshold.

---

## Contributing

Corrections, resources and real examples are welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md) first: every factual claim needs a primary
source, and tool listings need a reason to exist.

## License and credit

MIT licensed. The agents course builds on Google's agent whitepapers. The
second-brain project implements Andrej Karpathy's LLM wiki pattern, published
as a [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
on 4 April 2026, plus the parts the gist deliberately leaves undefined.

<!-- TODO before publishing:
     - add the link to the original article
     - screenshots: graph view at 30 days, an example concept page
     - social preview image in Settings -> General -->
