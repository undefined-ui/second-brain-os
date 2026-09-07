# Contradictions and supersession

This is the rule that separates a second brain from a search engine, and the one
most implementations get wrong.

When a new source disagrees with what a page already says, the page records
both. It does not overwrite.

## Why overwriting is the worst failure mode

A vault that silently updates to the latest claim has no memory of what you
believed and why. It always presents the most recent thing you read as the
truth, which is a ranking by recency, not by evidence.

Worse, it is invisible. Nothing errors. The page simply says something different
than it did last month, with the same confidence, and you have no way to notice
or to check what changed.

The history is the asset. Knowing that you believed X because of a 2024 source,
then revised to Y after better evidence, is more valuable than either claim
alone, because it tells you how firm Y actually is.

## What a contradiction looks like on a page

Both positions, each attributed and dated:

```markdown
## Current position

Retrieval quality degrades past roughly 50k tokens of context
([[Lost in the Middle]], 2023).

## Contested

[[Some 2026 benchmark]] reports no degradation up to 200k on the same task
family. The two use different evaluation setups: the first measures position
sensitivity, the second end-task accuracy. Unresolved.
```

The reader can act on that. A page that had silently adopted whichever was
ingested last cannot be acted on at all.

## Supersession

Sometimes it is not a genuine disagreement, it is old information. A tool
changed its API, a company was acquired, a paper was retracted.

Mark the old claim as superseded and keep it:

```markdown
~~Requires Node 18 or later~~ superseded 2026-05: the native installer no
longer requires Node ([[source]]).
```

Deleting it means that when you read something written before the change, you
have no way to reconcile it with what the vault now says.

## Confidence

Not everything ingested deserves equal weight. A tag or a frontmatter field is
enough:

- **stated** by a primary source you trust
- **reported** by secondary coverage
- **self-reported** by the party it benefits
- **unverified**

Self-reported numbers in particular should never lose that label. A company's
own performance claim repeated as fact in a concept page is how a vault becomes
confidently wrong.

## The instruction

In `CLAUDE.md`, worded so it generalises rather than covering only the obvious
case:

```
When a new source disagrees with an existing page, do not overwrite. Record both
positions with sources and dates, and say what would settle it. If the new
source is clearly better evidence, mark the older claim superseded rather than
deleting it. Never resolve a contradiction by picking the more recent source.
```

## Next

[index.md and log.md](index-and-log.md)
