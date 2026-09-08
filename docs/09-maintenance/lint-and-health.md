# Linting the vault

Structural rot is silent. Nothing errors. The vault just slowly stops answering
well because a third of its pages are unreachable and nobody noticed.

## What a lint checks

**Broken links.** Two distinct cases: a typo or rename, which gets fixed, and a
genuine gap, which goes into `index.md` under Gaps.

**Orphans.** Pages nothing links to. Either find where they belong and link
them, or delete them.

**Stubs.** Pages under about forty words with no links, usually a failed ingest.
Flag for re-ingest from the original in `raw/`.

**Schema violations.** Missing frontmatter, wrong type, tags outside the
vocabulary.

**Near-duplicates.** Similar titles, overlapping aliases, shared inbound links.

**Index drift.** Pages missing from `index.md`, entries pointing nowhere.

## Report before repairing

Mechanical fixes happen automatically. Anything requiring judgement gets
proposed and waits for you.

That line matters because a linter that merges pages on its own judgement
destroys work, and one that only reports produces a list nobody acts on. Broken
links and schema errors are mechanical. Merges and deletions are not.

## Running it

```
/lint
```

Weekly, or after any import of more than about twenty sources. Not after every
ingest, where it costs more than it catches.

Run it on a clean git state, so a wrong repair is one `git checkout` away.

Inside Obsidian, [Find orphaned files and broken
links](https://github.com/Vinzent03/find-unlinked-files) covers the same two
checks visually.

For a fast read without invoking the agent:

```bash
python3 scripts/link_check.py ~/brain
```

## Reading the output

The counts matter more than the individual items. Three broken links after a
week is normal. Forty means something in the ingest instructions changed and is
producing links to pages it never creates.

Track the rates over time rather than the raw numbers, since both grow with the
vault. See [metrics](../05-graphs/metrics.md).

## Next

[Review cadence](review-cadence.md)
