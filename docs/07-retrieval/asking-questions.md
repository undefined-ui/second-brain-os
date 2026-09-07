# Asking the vault

You built the vault so answers would come from what you actually read. An agent
that quietly falls back on its own knowledge destroys that, and it does so
invisibly: the answer is fluent, plausible, and unverifiable.

## The rule

Every claim in an answer comes from a page, and names the page.

```
Answer from my vault only. Cite the page for each claim. If the vault does not
cover part of the question, say which part rather than filling it in.
```

That instruction belongs in `CLAUDE.md`, not typed each time. A rule you have to
remember is a rule that lapses on the day it matters.

## Start from the index

The agent should read `index.md` first, then open the pages that look relevant,
then follow links outward from those.

The alternative, a full-text sweep, is slower, spends context on near-misses, and
misses pages whose wording differs from your question. The index exists to make
this cheap; see [index.md and log.md](../04-structuring/index-and-log.md).

## Outside knowledge, labelled

Sometimes the model knows something useful that the vault does not contain. That
is fine as long as it is marked:

```
Cite vault pages for anything from my notes. Anything you know that my vault
does not contain, put under a separate heading marked outside the vault.
```

Separated, it is useful context. Blended, it makes the whole answer unreliable,
because you no longer know which parts you can trace.

## Empty is a valid answer

If the vault has nothing on a topic, the right response is one sentence saying
so.

An agent padding an empty result with general knowledge is the failure mode to
watch for, because it feels like a good answer. Notice when an answer contains no
page references at all; that is the signal.

## Answers should end with what is missing

```
Read: [[page]], [[page]], [[page]]
Not covered: whether this holds for the streaming case
```

Two lines, and they do more than they look. They tell you how much of the vault
the answer rests on, and the gap line is often the more useful half, because it
is a precise statement of what to go read next.

## Next

[Query patterns](query-patterns.md)
