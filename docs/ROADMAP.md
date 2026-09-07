# Roadmap

What each planned page will cover. Sections marked done are written in full; the rest are outlines.

Pull requests against any outline are welcome. Read [CONTRIBUTING.md](../CONTRIBUTING.md) first: every factual claim needs a primary source.

---

## Concepts (1 of 7 written)

Why an LLM-maintained knowledge base beats the note system you abandoned, and what the pattern actually is.

- [ ] **What a second brain actually is**
  - The definition that matters here: one local, plain-text place your agent can read and write
  - What it is not: a prettier Notion, a chatbot with your PDFs attached
  - The three jobs it does: capture, connect, answer
  - The compounding effect and why it only shows up after ~50 sources
- [ ] **The save-for-later paradox**
  - Why you save things you never reopen
  - Cost of retrieval vs cost of capture
  - Where bookmarks, read-later apps and screenshots break down
  - What changes when something else does the filing
- [ ] **The LLM wiki pattern**
  - Karpathy's llm-wiki gist (published April 4, 2026) and what it specifies
  - Compilation over summarization: the wiki is primary, raw sources are the archive
  - Ingest, lint, query as the three operations
  - Where the gist stops and implementation begins
- [ ] **Why markdown and plain text**
  - Agents read and write files better than they drive APIs
  - Portability: no lock-in, no export step, git-friendly
  - Wikilinks as a graph format that survives any tool
  - Limits of plain text and when to add a database
- [ ] **Zettelkasten, PARA, evergreen notes**
  - What each system got right and what it demanded from you
  - Why maintenance load is the thing that kills note systems
  - Which parts of the old methods still apply
  - What the LLM removes from the workload and what it does not
- [ ] **Wiki vs RAG**
  - Why a personal corpus rarely needs a vector database
  - Retrieval quality: structured pages vs chunk similarity
  - Cost, latency and debuggability compared
  - When RAG genuinely earns its place
- [ ] **What good looks like**
  - Concrete success criteria for a working vault
  - Health signals: orphan rate, link density, page freshness
  - Failure signals you should catch early
  - A realistic timeline for the first month

## Setup (9 of 7 written)

From zero to a vault your agent maintains, in one evening.

- [x] **Obsidian and your first vault**
  - Install and create a local vault
  - Why the vault is just a folder
  - Settings worth changing on day one
  - Mobile and sync considerations
- [x] **Vault structure**
  - raw/, wiki/, output/ and what belongs in each
  - Page-type folders: sources, entities, concepts, synthesis
  - index.md and log.md as the agent's control surface
  - Structures to avoid and why deep folder trees fight the graph
- [x] **Claude Code in the vault**
  - Installing and starting Claude Code inside the vault folder
  - Permissions and what to allow
  - First run: pointing it at the structure
  - Working sessions vs scheduled runs
- [x] **Writing your CLAUDE.md**
  - What belongs in the instruction file and what does not
  - Page contracts: shape of each page type
  - Linking rules the agent must follow every time
  - Iterating on CLAUDE.md as the vault grows
- [x] **Plugins worth installing**
  - Web Clipper
  - Dataview and what it buys you
  - Templater
  - Plugins that conflict with agent-maintained files
- [x] **MCP for Obsidian**
  - When you need MCP and when files are enough
  - Local REST API plugin plus claude mcp add
  - What MCP unlocks: working while Obsidian is closed
  - Security notes for a local server
- [x] **Git, sync and backups**
  - Why a vault is an ideal git repo
  - What to commit and what to ignore
  - Sync options across machines
  - Recovering from a bad agent run

## Ingestion (outline)

Getting everything you read, watch and write into raw/ with as little friction as possible.

- [ ] **Web articles**
  - Obsidian Web Clipper setup and templates
  - Clipping to raw/ with consistent frontmatter
  - Paywalls, newsletters and dynamic pages
  - What to clip and what to skip
- [ ] **YouTube and podcasts**
  - Pulling transcripts reliably
  - Timestamps and why to keep them
  - Long videos: chunking before ingest
  - Audio-only sources and transcription options
- [ ] **PDFs, papers and books**
  - Text extraction that preserves structure
  - Scanned documents and OCR
  - Highlights from ebook readers
  - Handling papers with figures and tables
- [ ] **Chat exports**
  - Exporting Claude and ChatGPT history
  - Converting a JSON export into per-conversation markdown
  - Filtering noise: which conversations are worth ingesting
  - Privacy pass before anything enters the vault
- [ ] **Voice notes and meetings**
  - Capture on mobile
  - Transcription pipeline
  - Turning a meeting into decisions and entities
  - Keeping personal audio out of shared vaults
- [ ] **Newsletters and email**
  - A dedicated capture address
  - Automated forwarding into raw/
  - Deduplicating recurring newsletters
  - When email is not worth ingesting
- [ ] **Backfilling years of material**
  - Ordering the backfill so early pages do not get overwritten
  - Batching: how many sources per run
  - Cost control on large imports
  - Checkpoints and resuming

## Structuring (outline)

The rules that decide whether your vault becomes a graph or a landfill.

- [ ] **One page, one idea**
  - What atomic means in practice
  - Splitting a source into concepts
  - How long a page should be
  - When to merge instead of split
- [ ] **The four page types**
  - Sources: one page per ingested item
  - Entities: people, orgs, products, tools
  - Concepts: ideas, frameworks, methods
  - Synthesis: comparisons, themes, open questions
- [ ] **Linking rules**
  - Link on first mention, every page type
  - Minimum and maximum links per page
  - Links as claims, not decoration
  - Preventing hub pages from swallowing the graph
- [ ] **Frontmatter schema**
  - Required fields per page type
  - Dates, source URLs, confidence
  - Tags: a small controlled vocabulary
  - Keeping the schema stable as the vault grows
- [ ] **Naming and aliases**
  - Canonical titles and why they matter for wikilinks
  - Aliases for acronyms and alternate names
  - Disambiguating two things with the same name
  - Renaming without breaking links
- [ ] **Deduplication and merging**
  - Detecting near-duplicate pages
  - Merge procedure that preserves backlinks
  - Redirect stubs
  - Scheduling dedupe rather than doing it live
- [ ] **Contradictions and supersession**
  - Two sources disagree: what the page should say
  - Marking superseded claims instead of deleting them
  - Confidence and provenance fields
  - Why silent overwrites are the worst failure mode
- [ ] **index.md and log.md**
  - The index as a navigable catalog, not a dump
  - What the agent must record in the log
  - Using the log to audit and roll back
  - Keeping both files from growing unbounded

## Graphs (outline)

The part most second-brain guides skip: what the graph is for and how to make it do work.

- [ ] **Graph basics for a knowledge base**
  - Nodes, edges, direction and weight in plain terms
  - Why a knowledge base is a graph whether you plan it or not
  - Density, clustering, path length and what they tell you
  - The failure shapes: stars, chains and islands
- [ ] **Reading the Obsidian graph view**
  - Local vs global graph
  - Filters and groups that make it useful
  - Spotting orphans and over-linked hubs
  - Why a pretty graph is not a healthy one
- [ ] **Typed links**
  - Untyped wikilinks lose meaning at scale
  - A minimal relation vocabulary: supports, contradicts, extends, part-of
  - Encoding types in frontmatter or inline
  - Querying by relation type
- [ ] **Graph vs embeddings**
  - What each retrieval method is actually good at
  - Why similarity misses reasoning across sources
  - Hybrid setups
  - Cost and maintenance compared
- [ ] **GraphRAG and where it fits**
  - The idea in one page
  - Entity and relation extraction from your own vault
  - Community detection and summary layers
  - Whether a personal vault is big enough to need it
- [ ] **Exporting the graph**
  - Parsing wikilinks into an edge list
  - Loading into Kuzu, Neo4j or NetworkX
  - Visualizing outside Obsidian
  - Keeping the export in sync
- [ ] **Graph metrics worth tracking**
  - Orphan rate
  - Average degree and its healthy range
  - Clusters as evidence of your real interests
  - Tracking metrics over time

## Agents (outline)

Turning a one-off setup into a system that maintains itself.

- [ ] **Agent roles**
  - Ingestor, linker, reviewer, researcher
  - One job per agent and why
  - Handoffs between agents
  - Roles that are not worth automating
- [ ] **Scheduling**
  - Cadence per job: hourly, daily, weekly
  - Scheduled tasks, cron and CI options
  - What a run should produce
  - Detecting silent failures
- [ ] **Subagents and parallel work**
  - When to fan out
  - Context isolation between subagents
  - Merging parallel edits without conflicts
  - Cost of parallelism
- [ ] **Hooks**
  - Triggering on file changes in raw/
  - Pre-write validation
  - Post-run linting
  - Keeping hooks fast
- [ ] **Skills and slash commands**
  - Skills for repeated behavior, commands for repeated tasks
  - Where to store them so any agent can use them
  - Versioning your skills alongside the vault
  - Testing a skill before trusting it with the vault
- [ ] **Guardrails**
  - Never let an agent delete without a log entry
  - Write scopes: which folders are off limits
  - Dry-run mode
  - Reviewing agent output in git diffs

## Retrieval (outline)

How to actually ask your vault things and get answers worth trusting.

- [ ] **Asking the vault**
  - Question shapes that work
  - Anchoring answers to pages and sources
  - Requiring citations from your own vault
  - What to do when the answer is not in there
- [ ] **Query patterns**
  - What do I know about X
  - What connects X and Y
  - What have I changed my mind about
  - What is missing from my understanding of X
- [ ] **Search tools**
  - ripgrep as the default
  - Dataview queries
  - Full-text index options
  - When search is slow enough to matter
- [ ] **Adding RAG when you need it**
  - The size threshold where it starts to pay
  - Chunking a wiki that is already chunked
  - Keeping the index fresh
  - Hybrid: graph for structure, vectors for recall
- [ ] **Context budget**
  - Why you should not paste the whole vault
  - Progressive disclosure: index first, pages second
  - Summary layers
  - Measuring what the agent actually read

## Outputs (outline)

The vault earns its keep when things come out of it.

- [ ] **Writing from the vault**
  - Outlining from concept pages
  - Keeping citations to your own sources
  - Voice: your notes, not the model's
  - Publishing loop back into the vault
- [ ] **Research reports**
  - Scoping a question against existing pages
  - Filling gaps with new ingestion
  - Report structure that survives review
  - Storing outputs so they become sources
- [ ] **Publishing and export**
  - Static site options for a public wiki
  - Deciding what stays private
  - HTML and PDF export
  - Keeping public and private in one vault
- [ ] **Learning from your own vault**
  - Generating questions from concept pages
  - Spaced repetition against your notes
  - Finding what you saved but never understood
  - Measuring learning instead of collecting

## Maintenance (outline)

What keeps the thing alive after the novelty wears off.

- [ ] **Linting the vault**
  - Broken links, orphan pages, empty stubs
  - Schema violations
  - Automating the lint run
  - Reading a lint report
- [ ] **Review cadence**
  - Weekly review that takes ten minutes
  - Monthly structural review
  - What to prune and what to archive
  - Reviews that the agent prepares for you
- [ ] **Versioning**
  - Commit granularity for agent runs
  - Reading diffs of generated pages
  - Reverting a bad ingest
  - Branching for experiments
- [ ] **Backups and portability**
  - Local, cloud and offline copies
  - Testing a restore
  - Moving to another editor or agent
  - Avoiding formats that trap you
- [ ] **Privacy**
  - Deciding what never enters the vault
  - Redaction before ingest
  - Local models for sensitive material
  - Sharing a vault safely
- [ ] **Scaling past a thousand pages**
  - Where the plain-text approach strains
  - Splitting vaults by domain
  - Summary layers and hierarchical indexes
  - Performance tuning

## Troubleshooting (outline)

Concrete failures, with fixes.

- [ ] **The failures everyone hits**
  - Vault stalls after two weeks
  - Pages that are summaries of summaries
  - The agent rewrites work you did by hand
  - Ingest quality drops as the vault grows
- [ ] **The agent writes garbage**
  - Diagnosing whether it is CLAUDE.md or the source
  - Tightening page contracts
  - Adding examples instead of adding rules
  - Rolling back and re-running
- [ ] **Broken links and orphans**
  - Why renames break wikilinks
  - Bulk fixing safely
  - Preventing orphans at ingest time
  - Auditing after a big import
- [ ] **The vault got too big**
  - Symptoms
  - Splitting vs summarizing
  - Archiving cold material
  - Rebuilding the index
- [ ] **FAQ**
  - Do I need MCP
  - Does this work with other agents
  - How much does it cost to run
  - Can I use a local model

---

[Back to the guide](README.md)
