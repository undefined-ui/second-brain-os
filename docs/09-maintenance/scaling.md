# Scaling past a thousand pages

Most of this guide assumes a vault of a few hundred to a few thousand pages,
which is where personal vaults live for years. Past that, some things strain.

## What actually breaks

**Not search.** Ripgrep over ten thousand markdown files is still instant.

**Not Obsidian,** although the global graph view stops being usable somewhere
around a thousand nodes.

**Retrieval economy.** The index gets long enough that reading it costs real
context, which is the first genuine constraint.

**Your attention.** A thousand pages is more than you can hold a mental map of,
which is precisely when the vault becomes more useful and also when you stop
noticing that parts of it have rotted.

## Summary layers

The fix for the index problem: one level between the master index and the pages.

A short page per topic area, listing what is in it and what each page covers. The
agent reads the master index, opens the one topic index that matters, then opens
pages. Three cheap reads instead of one expensive one.

Two levels is enough. Three means summaries of summaries, which drift from what
they describe and get read instead of it.

## Splitting vaults

Split by domain when two areas genuinely do not inform each other: work and a
hobby, two unrelated fields.

Do not split by date or by size. The whole value is that old material connects to
new, and a vault split chronologically severs exactly the connections worth
having.

The cost of splitting is that cross-domain connections stop happening, and those
are often the interesting ones. Split late and reluctantly.

## Archiving

Move cold material to an `archive/` folder outside `wiki/`: still on disk, still
searchable with ripgrep, no longer in the index or the graph.

Reversible, which matters, because "cold" is a guess. A topic you archived can be
brought back if it turns out to matter again.

## Pruning what never mattered

Concept pages with one source and no inbound links after a year were never
concepts, they were paragraphs. Deleting them improves everything else by
reducing what queries have to read past.

Run this once a year, not continuously.

## The honest ceiling

Somewhere past ten thousand pages, a curated wiki stops being the right structure
for a single person, because nobody can curate at that rate and the curation is
what made it work.

If you are there, either the vault has stopped being personal, or ingestion has
been running without judgement for a long time. The second is far more common,
and the fix is upstream, in what you feed it.

## Next

[Troubleshooting](../10-troubleshooting/README.md).
