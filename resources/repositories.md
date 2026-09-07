# Repositories

Beyond the implementations of this pattern in [skills.md](skills.md). Every link
here was opened and checked; anything I could not verify is named without a link
rather than guessed at.

## Graph views for Obsidian

The built-in graph view is a viewer with no notion of relationship types. These
replace it when you want the graph to do work.

- **[HEmile/juggl](https://github.com/HEmile/juggl)**. An interactive, stylable,
  expandable graph built on Cytoscape.js. Its workspace mode is the real feature:
  you build a graph of just the nodes relevant to what you are working on, expand
  and hide selectively, pin positions, and save it for later. Supports link types
  on edges, which plain Obsidian does not. Has an API other plugins build on.
- **[zsviczian/excalibrain](https://github.com/zsviczian/excalibrain)**. A
  structured mind-map of the vault rather than a force-directed cloud. It derives
  five relationship types from your links, Dataview fields, tags and frontmatter:
  parents, children, friends, other friends, siblings. Requires Dataview and
  Excalidraw. The closest thing to [typed
  links](../docs/05-graphs/typed-links.md) with no extra work from you.
- **[michaelpporter/breadcrumbs](https://github.com/michaelpporter/breadcrumbs)**.
  Typed links plus navigation over them: breadcrumb trails, tree and matrix
  views, Mermaid and Markmap rendering, export to Canvas. Reads typed frontmatter
  links, tags, lists, folder notes and Dataview queries, and derives implied
  relations. Maintained by michaelpporter since May 2026, originally by
  SkepticMystic.
- **[SkepticMystic/graph-analysis](https://github.com/SkepticMystic/graph-analysis)**.
  Runs actual graph algorithms over your vault, including similarity measures
  like Adamic Adar, to surface connections you never linked. The closest thing to
  the [metrics](../docs/05-graphs/metrics.md) page without leaving Obsidian.
- **[AlexW00/obsidian-3d-graph](https://github.com/AlexW00/obsidian-3d-graph)**.
  The vault as a 3D force graph, built on D3 and 3d-force-graph. Genuinely useful
  for spotting cluster structure that a 2D hairball hides, and the source of most
  good vault screenshots. The actively maintained fork is published as "3D Graph
  New".
- **[brianpetro/obsidian-smart-connections](https://github.com/brianpetro/obsidian-smart-connections)**.
  Semantic similarity between notes using a local embedding model, no API key,
  shown as a graph and a list while you write. This is the embeddings side of
  [graph vs embeddings](../docs/05-graphs/graph-vs-vectors.md) in the one place
  it clearly earns its keep: suggesting links you have not made yet.

## Building a graph from your own material

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)**. A
  `/graphify` skill for Claude Code, Cursor, Codex and Gemini CLI that reads a
  folder and builds a queryable knowledge graph from it. Local deterministic AST
  parsing for code, and multimodal extraction for docs, PDFs, screenshots and
  diagrams. No vector store, and every edge is labelled as extracted or inferred,
  which is the same honesty about provenance this guide asks of page contracts.

  Directly relevant here: it was built around the problem of a `raw/` folder full
  of papers, screenshots and notes, which is exactly the folder this pattern
  creates. Output includes an interactive `graph.html` and an Obsidian-openable
  vault. The project reports large token savings versus reading raw files; that
  figure is self-reported and depends heavily on corpus size.

  Originally by Safi Shamsi. Several widely linked repos named `graphify` are
  forks of it.

## GraphRAG implementations

Read these if you want to see what an automated version of the graph looks like
before deciding you do not need one. See
[GraphRAG and where it fits](../docs/05-graphs/graphrag.md).

- **[microsoft/graphrag](https://github.com/microsoft/graphrag)**. The reference
  implementation of the [paper](papers.md). Entity extraction, community
  detection, community summaries, global and local search.
- **[gusye1234/nano-graphrag](https://github.com/gusye1234/nano-graphrag)**. The
  same idea in roughly 1,100 lines, written to be read and modified. This is the
  one to open if you want to understand the pipeline rather than run it.
  Pluggable storage: networkx by default, Neo4j available.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)**. A dual-layer approach
  holding both a knowledge graph and vector embeddings, aimed at cheaper
  incremental updates than the original. Published at EMNLP 2025. Structurally
  based on nano-graphrag.
- **[DEEP-PolyU/Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG)**.
  A curated list of surveys, papers, benchmarks and open-source projects in this
  area. The right starting point if you want the landscape rather than one tool.

Also worth knowing by name: Graphiti and Cognee, both graph-based memory layers
for agents rather than knowledge bases for people. Different problem, adjacent
techniques.

## Publishing

- **[jackyzha0/quartz](https://github.com/jackyzha0/quartz)**. Publishes a vault
  as a static site with backlinks, link previews, a local graph and full-text
  search. Understands both wikilinks and markdown links, which is the thing to
  check in any publishing tool. Docs at
  [quartz.jzhao.xyz](https://quartz.jzhao.xyz/).

  One caveat that applies to every publishing tool: check how it handles links to
  unpublished pages before you publish anything. See [publishing and
  export](../docs/08-outputs/publishing-and-export.md).

## How to judge one of these

Two questions answer most of it.

**Does it own your data or read it?** Anything that reads your markdown and
writes derived output is safe to try and safe to abandon. Anything that becomes
the only place a piece of knowledge lives has taken the portability you chose
markdown for.

**Is it maintained?** Check the commit history, not the star count. This
ecosystem produces a lot of repos in the weeks after a popular gist, and most of
them stop within a month.
