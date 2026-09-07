# The vault got too big

## Symptoms

Answers get slower and vaguer. The agent reads twenty pages and returns something
general. The graph view is a hairball. You cannot remember whether a topic is
covered, and checking takes longer than searching the web.

## What it usually is not

Disk, search speed, or Obsidian. Those all scale fine.

What it actually is: retrieval economy. The index is long enough that reading it
costs real context, so the agent either skips it or spends its budget there
instead of on pages.

## First, check it is size and not rot

Run the [metrics](../05-graphs/metrics.md). A vault with a twenty percent orphan
rate does not have a size problem, it has a linking problem, and splitting it
will not help.

Genuinely large and healthy looks like: low orphan rate, one dominant component,
average degree in range, and an index over a few hundred entries.

## Summary layers

The first fix and usually enough. One index per topic area between the master
index and the pages, so the agent makes three cheap reads instead of one
expensive one. See [scaling](../09-maintenance/scaling.md).

## Splitting

By domain, never by date. Two vaults that genuinely do not inform each other.

Accept that cross-domain connections stop happening. Those are often the
interesting ones, which is why splitting is a late move rather than a first
response.

## Archiving

Cold material to `archive/`, outside `wiki/`. Still searchable, out of the index
and the graph, reversible.

Better than deleting, because "cold" is a guess and archived material can come
back.

## Rebuild the index

Sometimes the index has simply drifted: entries for pages that moved, missing
entries for pages added by runs that failed halfway.

```
Rebuild index.md from the actual contents of wiki/. Group by type and theme, one
line of description per entry, and list gaps at the bottom.
```

Cheap, and it fixes a surprising share of "the vault feels broken" complaints.

## Next

[FAQ](faq.md)
