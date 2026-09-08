---
name: second-brain-backfill
description: >-
  Import a large archive into the vault in controlled batches: triage what is
  worth ingesting, process oldest first, checkpoint after every batch, and keep
  cost visible. Use this skill whenever the user wants to import years of
  bookmarks, an export from another notes app, a downloads folder, a chat
  history dump, or says "backfill", "bulk import", "process my archive". Do NOT
  use for ingesting one or a few new sources, which is second-brain-ingest.
---

# Backfill an archive

A backfill is where cost and quality both go wrong quietly. Done in the wrong
order it also inverts the vault's history, because later sources should update
pages that earlier ones created.

## Core rule

Oldest first, ten sources per batch, stop for a go-ahead between batches.

## Workflow

1. **Triage before ingesting.** Read titles and first paragraphs. Sort into
   worth-ingesting, keep-in-raw, and delete. Most archives are half dead links
   and things saved but never opened.
2. **Order by date, oldest first.** Run it the other way and every old source
   arrives as a contradiction against a page that already has the final answer.
3. **Batch of ten.** Ingest following `second-brain-ingest`.
4. **Checkpoint:** update `index.md`, append to `log.md`, commit with the batch
   range in the message, report counts.
5. **Stop and wait** before the next batch.
6. **Full lint at the end.** Large imports always leave orphans and duplicates.

## Output format

```
Batch <n>/<total>: <range>
Ingested: <n> sources -> <n> new pages, <n> updated, <n> links
Skipped: <n> (reason)
Running total: <n> of <n>
Next batch: <what it contains>
```

## Calibration

Read every page the first batch produced, all of them. A flaw you let through in
batch one is a flaw in four hundred pages by the end, and fixing it afterwards
costs more than the original run.

If the archive is over about two hundred sources, propose a filter before
starting rather than quoting the full cost.
