# Tools

Everything outside the Obsidian plugin catalog. For plugins, see
[plugins.md](plugins.md). Star counts are from GitHub, September 2026.

## The core stack

| Tool | What it does |
|---|---|
| [Obsidian](https://obsidian.md) | Local markdown editor. The vault is a plain folder, which is why agents work well with it |
| [Obsidian Web Clipper](https://obsidian.md/clipper) | Official browser extension, saves articles into `raw/`. Uses Mozilla Readability |
| [Claude Code](https://code.claude.com/docs/en/setup) | The agent that maintains the wiki. Paid account required |

## Alternative homes for a vault

| Tool | Stars | Notes |
|---|---|---|
| [AFFiNE](https://github.com/toeverything/AFFiNE) | 72,292 | Docs, whiteboard and database in one. Heavier than markdown files |
| [memos](https://github.com/usememos/memos) | 62,837 | Self-hosted quick capture, markdown-native. A good `raw/` inbox |
| [Joplin](https://github.com/laurent22/joplin) | 56,264 | Privacy-focused notes with sync across every platform |
| [SiYuan](https://github.com/siyuan-note/siyuan) | 46,225 | Self-hosted knowledge workspace, block-based |
| [Logseq](https://github.com/logseq/logseq) | 44,818 | Outliner, plain markdown, block-level references |
| [Outline](https://github.com/outline/outline) | 40,483 | Team knowledge base. The right answer when it is not just you |
| [Trilium](https://github.com/TriliumNext/Trilium) | 37,762 | Hierarchical personal knowledge base with scripting |
| [Foam](https://github.com/foambubble/foam) | 17,386 | The same wikilink pattern inside VS Code |
| [Anytype](https://github.com/anyproto/anytype-ts) | 8,764 | Local-first, encrypted, object-based |
| [Dendron](https://github.com/dendronhq/dendron) | 7,465 | Hierarchical PKM in VS Code |

Worth being honest about the tradeoff: everything below Obsidian in this table
stores knowledge in its own structure. Markdown files in a folder are the only
format where leaving the tool costs nothing.

## AI-native knowledge apps

| Tool | Stars | Notes |
|---|---|---|
| [Khoj](https://github.com/khoj-ai/khoj) | 37,186 | Self-hostable AI second brain over your docs, with custom agents and scheduled automations |
| [Quivr](https://github.com/The-Vibe-Company/quivr) | 39,498 | Opinionated RAG you embed in your own app |
| [Reor](https://github.com/reorproject/reor) | 8,563 | Local-first AI note app that links notes automatically as you write |

These are products, not patterns. They do the job for you, at the cost of the
portability this guide is built around. Worth knowing before you decide the
file-based approach is too much work.

## Capture and processing

| Tool | What it does |
|---|---|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Subtitles and audio from video platforms |
| [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) | Transcripts from Python |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | Text layer for scanned PDFs |
| [Zotero](https://github.com/zotero/zotero) | Reference manager, 15,184 stars, markdown export path |
| [Readwise](https://readwise.io) | Kindle and read-later highlights into Obsidian. Paid |

## Search and graph

| Tool | What it does |
|---|---|
| [ripgrep](https://github.com/BurntSushi/ripgrep) | Fast enough that most vaults never need an index |
| [NetworkX](https://networkx.org) | Graph analysis once you have exported an edge list |
| [Kuzu](https://kuzudb.com) | Embedded graph database, no server |
| [Neo4j](https://neo4j.com) | Full graph database. Overkill unless you build on top |
| [Gephi](https://gephi.org) | Visual graph exploration beyond Obsidian's view |
| [txtai](https://github.com/neuml/txtai) | 12,931 stars. Semantic search and LLM workflows, if you decide you need embeddings |

## Publishing

| Tool | Stars | Notes |
|---|---|---|
| [Quartz](https://github.com/jackyzha0/quartz) | 13,185 | Vault to static site with backlinks, local graph and search |
