# The guide

Ten sections, ordered the way you would actually build the system: understand the
pattern, set it up, feed it, shape it, make the graph work, automate it, query it,
get things out of it, keep it alive, and fix it when it breaks.

---

### [Concepts](01-concepts/README.md)

Why an LLM-maintained knowledge base beats the note system you abandoned, and what the pattern actually is.

- [What a second brain actually is](01-concepts/what-is-a-second-brain.md)
- [The save-for-later paradox](01-concepts/the-save-for-later-paradox.md)
- [The LLM wiki pattern](01-concepts/llm-wiki-pattern.md)
- [Why markdown and plain text](01-concepts/why-markdown-and-plain-text.md)
- [Zettelkasten, PARA, evergreen notes](01-concepts/pkm-lineage.md)
- [Wiki vs RAG](01-concepts/wiki-vs-rag.md)
- [What good looks like](01-concepts/what-good-looks-like.md)
- [The two layers](01-concepts/two-layers.md)

### [Setup](02-setup/README.md)

From zero to a vault your agent maintains, in one evening.

- [Obsidian and your first vault](02-setup/obsidian-install-and-vault.md)
- [Vault structure](02-setup/vault-structure.md)
- [Claude Code in the vault](02-setup/claude-code-setup.md)
- [Writing your CLAUDE.md](02-setup/claude-md.md)
- [Plugins worth installing](02-setup/obsidian-plugins.md)
- [MCP for Obsidian](02-setup/mcp-obsidian.md)
- [Project scoping](02-setup/project-scoping.md)
- [Live data connectors](02-setup/live-data.md)
- [Git, sync and backups](02-setup/git-and-sync.md)

### [Ingestion](03-ingestion/README.md)

Getting everything you read, watch and write into raw/ with as little friction as possible.

- [Web articles](03-ingestion/web-clipper.md)
- [YouTube and podcasts](03-ingestion/youtube-transcripts.md)
- [PDFs, papers and books](03-ingestion/pdfs-and-books.md)
- [Chat exports](03-ingestion/chat-exports.md)
- [Voice notes and meetings](03-ingestion/voice-and-meetings.md)
- [Newsletters and email](03-ingestion/newsletters-and-email.md)
- [Backfilling years of material](03-ingestion/bulk-backfill.md)

### [Structuring](04-structuring/README.md)

The rules that decide whether your vault becomes a graph or a landfill.

- [One page, one idea](04-structuring/atomic-pages.md)
- [The four page types](04-structuring/page-types.md)
- [Linking rules](04-structuring/linking-rules.md)
- [Frontmatter schema](04-structuring/frontmatter-schema.md)
- [Naming and aliases](04-structuring/naming-and-aliases.md)
- [Deduplication and merging](04-structuring/dedupe-and-merge.md)
- [Contradictions and supersession](04-structuring/contradictions-and-supersession.md)
- [index.md and log.md](04-structuring/index-and-log.md)

### [Graphs](05-graphs/README.md)

The part most second-brain guides skip: what the graph is for and how to make it do work.

- [Graph basics for a knowledge base](05-graphs/graph-basics.md)
- [Reading the Obsidian graph view](05-graphs/obsidian-graph-view.md)
- [Typed links](05-graphs/typed-links.md)
- [Graph vs embeddings](05-graphs/graph-vs-vectors.md)
- [GraphRAG and where it fits](05-graphs/graphrag.md)
- [Exporting the graph](05-graphs/exporting-your-graph.md)
- [Graph metrics worth tracking](05-graphs/metrics.md)

### [Agents](06-agents/README.md)

Turning a one-off setup into a system that maintains itself.

- [Agent roles](06-agents/agent-roles.md)
- [Scheduling](06-agents/scheduled-maintenance.md)
- [Subagents and parallel work](06-agents/subagents.md)
- [Hooks](06-agents/hooks.md)
- [Skills and slash commands](06-agents/skills-and-commands.md)
- [Guardrails](06-agents/safety-and-guardrails.md)

### [Retrieval](07-retrieval/README.md)

How to actually ask your vault things and get answers worth trusting.

- [Asking the vault](07-retrieval/asking-questions.md)
- [Query patterns](07-retrieval/query-patterns.md)
- [Search tools](07-retrieval/search-tools.md)
- [Adding RAG when you need it](07-retrieval/rag-on-top.md)
- [Context budget](07-retrieval/context-budget.md)

### [Outputs](08-outputs/README.md)

The vault earns its keep when things come out of it.

- [Writing from the vault](08-outputs/writing-from-the-vault.md)
- [Research reports](08-outputs/research-reports.md)
- [Publishing and export](08-outputs/publishing-and-export.md)
- [Learning from your own vault](08-outputs/teaching-yourself.md)

### [Maintenance](09-maintenance/README.md)

What keeps the thing alive after the novelty wears off.

- [Linting the vault](09-maintenance/lint-and-health.md)
- [Review cadence](09-maintenance/review-cadence.md)
- [Versioning](09-maintenance/versioning-with-git.md)
- [Backups and portability](09-maintenance/backups-and-portability.md)
- [Privacy](09-maintenance/privacy-and-secrets.md)
- [Scaling past a thousand pages](09-maintenance/scaling.md)

### [Troubleshooting](10-troubleshooting/README.md)

Concrete failures, with fixes.

- [The failures everyone hits](10-troubleshooting/common-failures.md)
- [The agent writes garbage](10-troubleshooting/agent-writes-garbage.md)
- [Broken links and orphans](10-troubleshooting/broken-links.md)
- [The vault got too big](10-troubleshooting/vault-too-big.md)
- [FAQ](10-troubleshooting/faq.md)

---

[Back to the repo](../README.md)
