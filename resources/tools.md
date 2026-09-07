# Tools

## The core stack

- **[Obsidian](https://obsidian.md)** - local markdown editor. The vault is a
  plain folder, which is the whole reason agents work well with it.
- **[Obsidian Web Clipper](https://obsidian.md/clipper)** - official browser
  extension for saving articles into the vault. Built by the Obsidian team.
- **[Claude Code](https://claude.com/claude-code)** - the agent that maintains
  the wiki. Runs in the vault folder and edits files directly.

## Obsidian plugins

- **Dataview** - queries over frontmatter. Useful for dashboards of what needs
  review.
- **Templater** - templates with variables, for the page shapes in
  `vault-template/templates/`.
- **Local REST API** - required only if you want the agent to reach the vault
  over MCP rather than through the filesystem.

## Capture

- **yt-dlp** - subtitles and audio from video platforms.
- **youtube-transcript-api** - Python library for pulling transcripts directly.
- **Zotero** - reference manager with a markdown export path for papers.
- **Readwise** - highlights from Kindle and read-later apps, exports to
  Obsidian.

## Search and graph

- **ripgrep** - fast enough that most vaults never need an index.
- **NetworkX** - graph analysis in Python once you have exported an edge list.
- **Kuzu** - embedded graph database, no server to run.
- **Neo4j** - full graph database, worth it only at scale.
- **Gephi** - visual graph exploration beyond what Obsidian's graph view does.

## Alternatives to Obsidian

- **Logseq** - outliner, also plain markdown, block-level references.
- **Foam** - the same pattern inside VS Code.
- **Plain folders plus git** - genuinely viable. Obsidian is a viewer for the
  graph, not a requirement of it.
