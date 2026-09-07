# Subagents and parallel work

Subagents run with their own context. That is the whole point: a subagent
reading thirty pages to answer a question does not fill the main session's
context with those thirty pages, only with the answer.

## When to fan out

**Research across many pages.** Send a subagent to read a cluster and come back
with a summary. The main session keeps its budget for the actual work.

**Independent sources.** Ingesting ten unrelated articles parallelises cleanly,
because none of them touch the same wiki pages.

**Verification.** One agent writes, another checks the pages against the sources.
Separate context is what makes the check meaningful; the same agent rereading its
own work mostly agrees with itself.

## When not to

**Related sources.** Three articles about the same topic must be ingested
sequentially. In parallel, each one creates the concept page independently and
you get three versions of it, or two of them are overwritten.

**Anything touching the index.** `index.md` and `log.md` are single files that
every run wants to append to. Parallel writes to them conflict or silently lose
entries.

**Small jobs.** Spawning a subagent costs a full context setup. For two files it
is slower than doing it directly.

## Merging parallel work

The rule that avoids most conflicts: subagents write to disjoint paths, the
parent merges.

Have each subagent report what it would write rather than writing shared files
directly. The parent applies the index and log updates in one pass, after all
subagents return. Page files themselves are safe to write in parallel as long as
two subagents were never given overlapping material.

Commit before any parallel run. When it goes wrong, it goes wrong across many
files at once.

## Cost

Parallelism does not reduce total token use, it reduces wall-clock time and
protects the main context. Four subagents cost roughly four times one.

That trade is worth it for a large backfill and pointless for a daily ingest of
five clipped articles.

## Next

[Hooks](hooks.md)
