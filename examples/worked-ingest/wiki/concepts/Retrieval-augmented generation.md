---
title: Retrieval-augmented generation
type: concept
created: 2026-10-19
updated: 2026-10-19
aliases: [RAG]
tags: [llm, knowledge-management]
---

# Retrieval-augmented generation

## In one paragraph

Retrieval-augmented generation is the common way of letting a language model answer questions about a set of documents. The documents are indexed in advance, usually as chunks. When a question comes in, the system retrieves the chunks that look most relevant and hands them to the model along with the question, and the model writes an answer from them. The documents themselves are not changed and nothing is written back; each question starts from the raw material again.

## Where it came from

In this vault the concept appears only through [[LLM Wiki (Karpathy)]], which uses it as the baseline the [[LLM wiki]] pattern departs from. That source names NotebookLM, ChatGPT file uploads and most RAG products as examples. The general history of the technique is not covered by any source here.

## What supports it

The source grants that the approach works for answering questions over uploaded files, and it is the default behaviour of mainstream tools.

## What argues against it

The source's objection is that nothing accumulates: a subtle question that needs five documents synthesised forces the model to find and piece together the same fragments every time, so the connections, contradictions and syntheses are rediscovered rather than kept. The same source also notes that at moderate scale a maintained index file can replace embedding-based retrieval entirely.

## Open questions

Whether the two approaches are alternatives or layers: the source suggests a search engine such as [[qmd]], which itself uses vector search, as an aid to an LLM wiki once it outgrows the index file. No source here addresses how retrieval over a maintained wiki compares with retrieval over raw documents.

## Related

[[LLM wiki]], [[qmd]], [[LLM Wiki (Karpathy)]].
