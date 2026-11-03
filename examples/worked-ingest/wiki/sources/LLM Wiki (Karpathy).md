---
title: LLM Wiki (Karpathy)
type: source
created: 2026-10-19
updated: 2026-10-19
url:
path: raw/karpathy-llm-wiki.md
author: Andrej Karpathy
published: unknown
aliases: [karpathy-llm-wiki, LLM Wiki idea file]
tags: [knowledge-management, llm, agents]
---

# LLM Wiki (Karpathy)

## What it is

A short idea file, clipped from a gist, describing a pattern for building a personal knowledge base with an LLM agent. The file is written to be pasted into an agent such as [[Claude Code]], OpenAI Codex or OpenCode so that the agent builds a concrete implementation with its owner. The text does not name its author; the filename attributes it to [[Andrej Karpathy]], and that attribution is carried here as the filename's claim, not the file's. No publication date is given in the file.

## Claims

The source says most people's experience of LLMs with documents is [[Retrieval-augmented generation]]: files are uploaded, relevant chunks are retrieved at query time, and an answer is generated. It says this works but accumulates nothing, because the model rediscovers the same connections on every question. NotebookLM, ChatGPT file uploads and most RAG systems are named as examples.

The proposed alternative, the [[LLM wiki]], is that the LLM incrementally builds and maintains a persistent, interlinked collection of markdown files that sits between the owner and the raw sources. On each new source the LLM reads it, extracts what matters, and integrates it: updating entity pages, revising topic summaries, flagging where new data contradicts old claims. The source's phrase for the key difference is that the wiki is a persistent, compounding artifact: the cross-references and contradictions are already recorded before any question is asked.

The source says the owner rarely writes the wiki. The owner curates sources and asks questions; the LLM does the summarising, cross-referencing, filing and bookkeeping. The author describes working with the agent on one side of the screen and [[Obsidian]] on the other, browsing links and the graph view as the agent edits. The analogy given is that Obsidian is the IDE, the LLM is the programmer, and the wiki is the codebase.

Suggested uses: personal tracking (goals, health, journal entries), long-running research with an evolving thesis, reading a book chapter by chapter into a companion wiki of the kind fan communities build, an internal team wiki fed by Slack threads and meeting transcripts, and smaller accumulations such as due diligence, trip planning or course notes.

The architecture has three layers. Raw sources are an immutable curated collection the LLM reads but never modifies. The wiki is a directory of LLM-generated markdown that the LLM owns entirely. The schema is a document such as CLAUDE.md or AGENTS.md that tells the LLM the structure, conventions and workflows; the source calls this the key configuration file, the thing that makes the LLM a disciplined maintainer rather than a generic chatbot, and says it should co-evolve with the owner over time.

Three operations are described. Ingest: drop a source into raw, have the LLM read it, discuss takeaways, write a summary page, update the index, update entity and concept pages across the wiki, and append to the log; a single source may touch 10 to 15 pages. The author prefers ingesting one source at a time with supervision but says batch ingestion with less supervision is also possible. Query: the LLM searches the wiki, reads relevant pages and synthesises an answer with citations, in whatever form fits (markdown page, comparison table, Marp slide deck, matplotlib chart, canvas); the source stresses that good answers should be filed back into the wiki so that explorations compound like ingested sources do. Lint: periodically ask the LLM to look for contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, concepts mentioned but lacking a page, missing cross-references, and gaps a web search could fill.

Two navigation files are described. index.md is a content catalog: every page with a link, a one-line summary and optional metadata, grouped by category, updated on every ingest. The source says reading the index first and then drilling into pages works well at moderate scale (around 100 sources, hundreds of pages) and avoids embedding-based RAG infrastructure. log.md is an append-only chronological record of ingests, queries and lint passes; the source suggests a consistent entry prefix such as `## [2026-04-02] ingest | Article Title` so the log can be parsed with grep and tail.

On tooling, the source says a search engine over the wiki becomes useful as it grows and names [[qmd]] as a good option: a local markdown search engine with hybrid BM25 and vector search and LLM re-ranking, offering both a CLI and an MCP server. It also says a naive search script can be vibe-coded when needed.

Tips given: [[Obsidian Web Clipper]] converts web articles to markdown for the raw collection. Images should be downloaded locally by setting Obsidian's attachment folder to a fixed directory such as raw/assets/ and binding a hotkey to "Download attachments for current file"; the source notes LLMs cannot read markdown with inline images in one pass, so the workaround is to read the text first and view images separately. Obsidian's graph view shows which pages are hubs and which are orphans. [[Marp]] produces slide decks from markdown and has an Obsidian plugin. [[Dataview]] runs queries over YAML frontmatter, so frontmatter on wiki pages enables dynamic tables. The wiki being a git repo gives version history, branching and collaboration for free.

The source's explanation of why the pattern works is that the tedious part of a knowledge base is bookkeeping, not reading or thinking; humans abandon wikis because the maintenance burden grows faster than the value, while an LLM does not get bored, does not forget a cross-reference, and can touch 15 files in one pass, so the cost of maintenance is near zero. The human's job is to curate sources, direct the analysis, ask good questions and think about what it means.

The source relates the idea to [[Vannevar Bush]]'s [[Memex]] of 1945: a private, curated knowledge store with associative trails between documents, in which the connections are as valuable as the documents. It says the part Bush could not solve was who does the maintenance, and that the LLM handles that.

The closing note says the document is intentionally abstract: directory structure, schema conventions, page formats and tooling all depend on the domain, the owner's preferences and the chosen LLM, and every element described is optional and modular.

## Why it matters here

This vault is an instance of the pattern the source describes: raw/ is the immutable source layer, wiki/ is the LLM-owned layer, and CLAUDE.md is the schema. The vault's conventions are one specific instantiation and differ from the source in places. The source suggests log entries as headed blocks with a bracketed date prefix; this vault's CLAUDE.md specifies one plain line per operation. The source leaves page formats open; this vault fixes four page types with frontmatter contracts and templates. Where this vault's rules and the source's suggestions differ, the vault's own CLAUDE.md is the one that applies.

## Links

Concepts: [[LLM wiki]], [[Retrieval-augmented generation]], [[Memex]].

Entities: [[Andrej Karpathy]], [[Obsidian]], [[Claude Code]], [[qmd]], [[Vannevar Bush]], [[Obsidian Web Clipper]], [[Marp]], [[Dataview]].
