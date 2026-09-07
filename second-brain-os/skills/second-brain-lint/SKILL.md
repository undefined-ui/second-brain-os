---
name: second-brain-lint
description: >-
  Audit a second-brain vault for structural problems and repair them: broken
  wikilinks, orphan pages, empty stubs, frontmatter that violates the schema,
  near-duplicate pages, and stale index entries. Use this skill whenever the
  user asks to lint, clean, audit or check the health of their vault, says
  pages feel messy or links are broken, after a large bulk import, or when a
  scheduled maintenance run fires. Do NOT use for ingesting new sources, for
  answering questions from the vault, or for rewriting page content that is
  structurally fine but reads badly.
---

# Lint the vault

Structural rot is silent. Nothing errors, nothing crashes, the vault just
slowly stops answering questions well because a third of its pages are
unreachable. Linting is the only thing that catches it before the owner does.

## Core rule

Report before repairing. Fix the mechanical problems automatically, but never
delete or merge a page without listing it first and getting a yes, because the
owner may have written it by hand.

## Workflow

1. **Inventory.** Count pages by type. Build the link graph by parsing every
   `[[wikilink]]`.
2. **Broken links.** Links pointing at pages that do not exist. Distinguish
   two cases: a typo or rename, which you fix, and a genuine gap, which goes
   into `index.md` under Gaps.
3. **Orphans.** Pages with no inbound links. For each, either find where it
   should be linked from and add the link, or flag it as a candidate for
   deletion.
4. **Stubs.** Pages under roughly 40 words with no links. Usually a failed
   ingest. Flag for re-ingest from the original source in `raw/`.
5. **Schema.** Missing or malformed frontmatter, wrong `type`, missing dates,
   tags outside the existing vocabulary.
6. **Near-duplicates.** Pages with very similar titles or aliases. Propose
   merges; do not perform them unsolicited.
7. **Index drift.** Pages missing from `index.md`, index entries pointing
   nowhere.
8. **Repair**, then append the run to `log.md`.

## Output format

```
Vault: <n> pages (<n> sources, <n> concepts, <n> entities, <n> synthesis)
Link graph: <n> links, average <n> per page, <n> orphans

Fixed automatically:
- <list>

Needs a decision:
- <list, each with the recommended action>

Health: orphan rate <n>%, broken link rate <n>%, stub rate <n>%
```

## Calibration

An aggressive linter that merges pages on its own judgement destroys work. A
timid one that only reports produces a list nobody acts on. The split above is
the useful line: mechanical fixes happen, semantic decisions get proposed.

Do not run a full lint after every ingest. Weekly, or after an import of more
than about twenty sources.
