# Obsidian plugins

Ranked by installs from Obsidian's own community stats, September 2026. The
catalog holds over 7,400 plugins; these are the ones that matter for an
agent-maintained vault.

## Agents inside Obsidian

A route this guide's [setup](../docs/02-setup/claude-code-setup.md) originally
skipped: instead of running the agent in a terminal pointed at the vault folder,
run it inside Obsidian.

| Plugin | Installs | What it does |
|---|---|---|
| [Claudian](https://github.com/yishentu/claudian) | 2,035,966 | Embeds Claude Code, Codex and other local agents as collaborators in the vault |
| [Copilot](https://github.com/logancyang/obsidian-copilot) | 1,832,464 | Runs Claude Code, Codex and OpenCode inside your vault |
| [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) | 1,189,513 | Local embedding model surfaces related notes while you write. No API key |
| [Local REST API with MCP](https://github.com/coddingtonbear/obsidian-local-rest-api) | 712,443 | Vault over a secure local API, now with a built-in MCP server |
| [Agent Client](https://github.com/rait-09/obsidian-agent-client) | 261,371 | Chat with Claude Code, Codex and Gemini CLI over the Agent Client Protocol |
| [Smart Composer](https://github.com/glowingjade/obsidian-smart-composer) | 171,863 | AI chat with note context and one-click edits |

## Structure and queries

| Plugin | Installs | What it does |
|---|---|---|
| [Templater](https://github.com/SilentVoid13/Templater) | 5,527,936 | Dynamic templates. For the pages you write by hand |
| [Dataview](https://github.com/blacksmithgu/obsidian-dataview) | 4,918,446 | Query language over your frontmatter. Answers "which pages have property P" |
| [Metadata Menu](https://github.com/mdelobelle/metadatamenu) | 330,430 | Manage frontmatter fields at scale. Useful once your [schema](../docs/04-structuring/frontmatter-schema.md) is fixed |
| [Supercharged Links](https://github.com/mdelobelle/obsidian_supercharged_links) | 210,926 | Styles links by the target note's frontmatter, so page type is visible inline |

## Graph

| Plugin | Installs | What it does |
|---|---|---|
| [ExcaliBrain](https://github.com/zsviczian/excalibrain) | 336,025 | Structured mind-map deriving five relationship types from links, Dataview fields and tags |
| [Juggl](https://github.com/HEmile/juggl) | 135,614 | Interactive Cytoscape.js graph with typed edges and a saveable workspace mode |
| [Graph Analysis](https://github.com/SkepticMystic/graph-analysis) | community plugin | Graph algorithms and similarity measures over the vault, surfaces unlinked connections |
| [Breadcrumbs](https://github.com/michaelpporter/breadcrumbs) | community plugin | Typed links plus trees, matrices, Mermaid and Canvas export |
| [3D Graph](https://github.com/AlexW00/obsidian-3d-graph) | community plugin | The vault as a 3D force graph. Shows cluster structure a 2D hairball hides |

## Maintenance

| Plugin | Installs | What it does |
|---|---|---|
| [Git](https://github.com/Vinzent03/obsidian-git) | 3,110,571 | Commit and sync the vault from inside Obsidian. See [versioning](../docs/09-maintenance/versioning-with-git.md) |
| [Omnisearch](https://github.com/scambier/obsidian-omnisearch) | 1,837,484 | Better full-text search, including inside PDFs |
| [Importer](https://github.com/obsidianmd/obsidian-importer) | 1,638,001 | Official importer from Notion, Evernote, Roam, Bear, Apple Notes. The first step for anyone [backfilling](../docs/03-ingestion/bulk-backfill.md) |
| [Linter](https://github.com/platers/obsidian-linter) | 1,044,521 | Formats notes to consistent rules. Set it carefully, it rewrites files |
| [Find orphaned files and broken links](https://github.com/Vinzent03/find-unlinked-files) | 224,687 | Exactly what [lint](../docs/09-maintenance/lint-and-health.md) checks, without leaving Obsidian |

## Capture and study

| Plugin | Installs | What it does |
|---|---|---|
| [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) | 7,795,993 | The most installed plugin in the catalog. Diagrams that live in the vault as files |
| [QuickAdd](https://github.com/chhoumann/quickadd) | 2,082,182 | One-keystroke capture into a chosen folder and template |
| [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 592,497 | Flashcards from your own notes. See [learning from your vault](../docs/08-outputs/teaching-yourself.md) |
| [Zotero Integration](https://github.com/obsidian-community/obsidian-zotero-integration) | 550,881 | Citations, bibliographies and PDF annotations from Zotero |
| [ReadItLater](https://github.com/DominikPieper/obsidian-ReadItLater) | 134,982 | Saves online content into the vault with a template |
| [Webpage HTML Export](https://github.com/KosmosisDire/obsidian-webpage-export) | 152,194 | Export notes, canvases or the whole vault as HTML |

## A warning about plugin count

Every plugin is code with write access to your notes, running alongside an agent
that also writes to them. Two things that rewrite files on their own schedule
will eventually disagree.

Install what solves a problem you actually have. An empty vault with fifteen
plugins is a procrastination artifact.
