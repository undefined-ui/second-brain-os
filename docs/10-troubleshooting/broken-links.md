# Broken links and orphans

```bash
python3 scripts/link_check.py ~/brain
```

## Why renames break links

Obsidian updates links when you rename inside the app. An agent renaming a file
directly does not, and that is the most common cause of broken links in an
agent-maintained vault.

Prevent it with a rule in `CLAUDE.md`: renames update every inbound link, add the
old name as an alias, and get recorded in `log.md`. See [naming and
aliases](../04-structuring/naming-and-aliases.md).

## Fixing in bulk

Two categories, handled differently.

**Typos and renames** get fixed: point the link at the right page. Safe to
automate.

**Genuine gaps**, where the target never existed, go into `index.md` under Gaps.
Do not create empty pages to satisfy them; an empty page is worse than a
recorded gap because it looks like coverage.

Always on a clean git state, so a bad bulk fix is one command to undo.

## Orphans

Pages nothing links to. Three cases.

**Should be linked and is not.** Find the pages that ought to reference it and
add the links. This is the common case after a bulk import.

**Genuinely standalone.** Rare and usually a sign the material does not belong in
the wiki. Reference material and checklists belong in a project folder.

**Failed ingest.** A stub that never got connected. Re-ingest from the original
in `raw/`.

## Preventing both at ingest

The rule that removes most of this work: nothing is ingested until it is linked,
in both directions, in the same run.

An ingest that ends with unlinked pages is an ingest that did not finish. Enforce
it in the skill rather than cleaning up weekly.

## After a big import

Always lint. A large backfill reliably produces orphans and near-duplicates,
because the agent was moving fast through material that overlapped.

Budget for it: a thousand-source import is followed by a lint pass and a merge
review, and skipping that step is what leaves a vault permanently messy.

## Next

[The vault got too big](vault-too-big.md)
