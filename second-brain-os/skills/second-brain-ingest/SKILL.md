---
name: second-brain-ingest
description: >-
  Turn raw source material in a second-brain vault into linked wiki pages:
  read the source, split it into concepts and entities, write or update pages,
  connect them to existing pages, and record the run in the log. Use this skill
  whenever the user drops a file into raw/, pastes an article, transcript or
  PDF and asks to add it to the vault, says "ingest this", "add this to my
  second brain", "process raw", or asks to catch up on unprocessed sources,
  even if they do not name the ingest command. Do NOT use for answering
  questions from an existing vault, for linting or repairing pages, or for
  editing notes the user wrote by hand.
---

# Ingest a source

An ingest that only writes a summary page produces a vault that grows without
getting smarter. The whole value is in the second half of the job: connecting
the new material to what is already there. A page that lands unlinked is
invisible within a week.

## Core rule

Nothing is ingested until it is linked. Every run ends with the new pages
connected to existing pages in both directions.

## Workflow

1. **Read the source completely** before writing anything. Partial reads
   produce pages built from the introduction, which is where sources are least
   specific.
2. **Check what already exists.** Search the wiki for the main entities and
   concepts. Ingesting into an empty vault and ingesting into a vault of 300
   pages are different jobs: in the second, most of your work is updating
   pages, not creating them.
3. **Write the source page** in `wiki/sources/`. Record claims as claims, with
   the source attached.
4. **Extract concepts and entities.** One page per idea. If a concept page
   exists, add what this source contributes and update `updated:`. If it
   contradicts what is there, record both positions rather than replacing.
5. **Link in both directions.** The source page links to every concept and
   entity it touches; each of those links back. Add any missing target pages,
   or list them under Gaps in `index.md`.
6. **Update `index.md` and append to `log.md`** in the same run, because an
   index that lags is how a vault starts drifting.
7. **Report** what changed.

## Output format

End every run with this exact shape:

```
Ingested: <source name>
New pages: <n> (list)
Updated pages: <n> (list)
Links added: <n>
Contradictions found: <none | description>
Gaps created: <list of linked pages that do not exist yet>
```

## Calibration

Over-extraction is the common failure: ten thin concept pages from one article,
each a restated paragraph. A source usually yields one to three concepts worth
their own page. If a candidate concept cannot be explained without referring
back to this one source, it belongs inside the source page instead.

Under-extraction shows up as source pages that contain three separate ideas and
link to nothing. If a page needs section headings for unrelated topics, split
it.

## Example

Input: the user drops `raw/karpathy-llm-wiki.md`, a clipped gist, into a vault
that already has pages for `[[Obsidian]]` and `[[Claude Code]]`.

Output: one source page; a new concept page `[[LLM wiki]]` explaining the
pattern in plain language; an entity page `[[Andrej Karpathy]]`; updates to
`[[Obsidian]]` and `[[Claude Code]]` noting their role in the pattern; a link
from the existing `[[Personal knowledge management]]` concept to the new one;
index and log updated; report showing 3 new, 3 updated, 11 links.
