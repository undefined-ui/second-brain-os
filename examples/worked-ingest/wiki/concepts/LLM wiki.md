---
title: LLM wiki
type: concept
created: 2026-10-19
updated: 2026-10-19
aliases: [LLM-maintained wiki, persistent wiki pattern, compounding wiki]
tags: [knowledge-management, llm, agents]
---

# LLM wiki

## In one paragraph

An LLM wiki is a personal knowledge base where the owner collects sources and an LLM agent writes and maintains everything else. The sources sit in a folder the agent never edits. The wiki is a folder of interlinked markdown pages the agent creates and keeps current: one page per source, plus pages for the people, tools, ideas and arguments those sources mention. A short schema file tells the agent how the wiki is organised and what to do when a source arrives, a question is asked, or the wiki needs a health check. The point is that the work of connecting a new source to everything already known is done once, at ingest time, and then stays done. Later questions are answered from pages that already hold the cross-references and the flagged contradictions, instead of being reassembled from raw fragments each time. The owner reads the wiki, usually in [[Obsidian]], and steers; the agent does the filing.

## Where it came from

The pattern as described here comes from one source, [[LLM Wiki (Karpathy)]], an idea file attributed to [[Andrej Karpathy]] and written to be handed to an agent such as [[Claude Code]]. That source positions the pattern against [[Retrieval-augmented generation]], which retrieves from raw documents at query time and accumulates nothing between questions, and traces its spirit to [[Vannevar Bush]]'s [[Memex]], a curated store whose value lay in the trails between documents.

## What supports it

The main argument in the source is about maintenance cost. People abandon wikis because the bookkeeping (cross-references, stale summaries, noting contradictions) grows faster than the value, while an agent can update fifteen pages in one pass without getting bored or forgetting a link. The source also says that at moderate scale, around a hundred sources, a well-kept index file read first is enough for retrieval and no embedding infrastructure is needed, and that answers to questions can be filed back as pages so that exploration compounds the same way ingestion does. This vault itself is a working instance, which is weak evidence of feasibility but not yet of value at scale.

## What argues against it

No source in this vault argues against the pattern. The source itself concedes that it is abstract and untested in any specific form: directory layout, page formats, and tooling are left to each owner, and the author's own practice is supervised, one source at a time, rather than unattended batch ingestion.

## Open questions

Whether index-first retrieval still works past the few-hundred-page scale the source mentions, and at what point a search tool such as [[qmd]] becomes necessary. How much human review an ingest needs before errors written into pages start to compound along with the knowledge. How to tell, over months, whether the wiki is getting smarter or only getting bigger.

## Related

[[Retrieval-augmented generation]], [[Memex]], [[Obsidian]], [[Claude Code]], [[qmd]], [[LLM Wiki (Karpathy)]].
