---
title: qmd
type: entity
kind: tool
created: 2026-10-19
updated: 2026-10-19
aliases: []
tags: [tools, search]
---

# qmd

## What it is

A local search engine for markdown files, published at github.com/tobi/qmd. According to [[LLM Wiki (Karpathy)]] it combines BM25 and vector search with LLM re-ranking, runs entirely on-device, and exposes both a command-line interface and an MCP server.

## Why it appears here

The source names it as the obvious tool to add once an [[LLM wiki]] outgrows index-first retrieval: the CLI lets the agent shell out to it and the MCP server lets the agent call it as a native tool. It is not installed in this vault. The source's view is that a small wiki does not need it and that a naive search script can be written when the need arises.

## Mentioned in

[[LLM Wiki (Karpathy)]]
