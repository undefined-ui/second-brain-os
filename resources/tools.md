# Tools

## The core stack

- **[Obsidian](https://obsidian.md)**. Local markdown editor. The vault is a
  plain folder, which is the whole reason agents work well with it.
- **[Obsidian Web Clipper](https://obsidian.md/clipper)**. Official browser
  extension for saving articles into the vault, built by the Obsidian team. Uses
  Mozilla Readability, the engine behind Firefox Reader View.
- **[Claude Code](https://code.claude.com/docs/en/setup)**. The agent that
  maintains the wiki. Runs in the vault folder and edits files directly.
  Requires a paid account; the free plan does not include access.

## Obsidian plugins

- **[Dataview](https://github.com/blacksmithgu/obsidian-dataview)**. A query
  language over your frontmatter, rendered inline. This is what answers
  structural questions like "which concept pages have not been touched in ninety
  days". Docs at
  [blacksmithgu.github.io/obsidian-dataview](https://blacksmithgu.github.io/obsidian-dataview/).
- **[Templater](https://github.com/SilentVoid13/Templater)**. Templates with
  variables and dates, for the page shapes in `vault-template/templates/`. The
  agent does not need it; you will, for pages you write by hand.
- **[Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api)**.
  Serves your vault over a local API. Worth reading the README before choosing
  an MCP route: the plugin now ships a **built-in MCP server** at `/mcp/`, which
  removes the need for a separate server in most setups.

## MCP

- **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)**. The
  widely used third-party MCP server, run via `uvx mcp-obsidian`, talking to the
  Local REST API plugin. Still the most documented path, and the one most guides
  including this one describe.

Worth knowing before you pick: at least one maintained fork
([proofsh/obsidian-mcp](https://github.com/proofsh/obsidian-mcp)) has been
archived with the explicit reasoning that routing through a REST plugin adds
complexity when the vault is markdown files on disk. That is the same argument
this guide makes for starting on the filesystem.

## Capture

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**. Subtitles and audio from video
  platforms. `--write-auto-sub --skip-download` is the flag pair you want.
- **[youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)**.
  Python library for pulling transcripts directly.
- **[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)**. Adds a text layer to
  scanned PDFs without changing the visible document.
- **[Zotero](https://www.zotero.org)**. Reference manager with a markdown export
  path, worth it if you read papers regularly.
- **[Readwise](https://readwise.io)**. Kindle and read-later highlights, syncs
  into Obsidian. Paid.

## Search and graph

- **[ripgrep](https://github.com/BurntSushi/ripgrep)**. Fast enough that most
  vaults never need an index.
- **[NetworkX](https://networkx.org)**. Graph analysis in Python once you have
  exported an edge list.
- **[Kuzu](https://kuzudb.com)**. Embedded graph database, no server to run.
- **[Neo4j](https://neo4j.com)**. The full version. Overkill unless you are
  building something on top.
- **[Gephi](https://gephi.org)**. Visual graph exploration beyond what Obsidian's
  graph view does.

## Alternatives to Obsidian

- **[Logseq](https://logseq.com)**. Outliner, also plain markdown, block-level
  references.
- **[Foam](https://foambubble.github.io/foam/)**. The same pattern inside VS
  Code.
- **Plain folders plus git.** Genuinely viable. Obsidian is a viewer for the
  graph, not a requirement of it.
