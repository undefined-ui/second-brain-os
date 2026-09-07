# index.md and log.md

Two files that are not knowledge, but without which the knowledge is hard to
reach and impossible to audit.

## index.md

The catalog. Every page, grouped by type, with the gaps listed at the bottom.

Its real job is retrieval economy. When the agent gets a question, reading the
index first tells it what exists and which pages are worth opening. Without it,
the alternative is a full-text sweep, which is slower, costs more context, and
misses pages whose wording differs from the question.

Keep it navigable rather than exhaustive-looking:

```markdown
## Concepts

### Retrieval
- [[Retrieval augmented generation]] - chunking, embeddings, when it beats a wiki
- [[GraphRAG]] - entity graph plus community summaries

### Agents
- [[Agent harness]] - the loop around a model
```

One line of description per entry. That line is what lets the agent decide
whether to open the page, and it is worth the tokens.

## Gaps

At the bottom of the index, the pages that are linked and do not exist.

This section is the most actionable thing in the vault. It is a list of what
your own material keeps referring to and you have never written down, which is
usually a precise map of what to read next.

## log.md

One line per operation, appended, newest at the bottom.

```
2026-09-07 ingest raw/karpathy-gist.md -> 1 source, 2 concepts, 1 entity, 9 links
2026-09-07 merge [[RAG]] <- [[Retrieval-augmented generation]]
2026-09-08 lint -> 3 broken links fixed, 2 orphans flagged
```

The log is what makes an agent-maintained vault auditable. When a page says
something you do not recognise, the log tells you which run produced it. When
something disappears, the log is the difference between a traceable merge and a
mystery.

It also gives the [review skill](../../skills/README.md) its raw material: what
changed this week comes from here, not from guessing at file timestamps.

## Keeping both from bloating

The index grows with the vault, which is fine, but flat lists stop being
navigable somewhere around two hundred entries. Group by theme, and once a theme
has more than about thirty entries, give it its own index page and link it from
the main one.

The log grows forever and nobody reads old entries. Roll entries older than a
few months into one summary line per month, or archive them into a dated file.
Keep recent detail, compress history.

## The rule that matters

Both files update in the same run as the work they describe.

An index that lags is worse than no index, because the agent trusts it and stops
looking for pages it does not list. A log written later is a reconstruction, not
a record.

## Next

[Graphs](../05-graphs/README.md), where these structures start paying off.
