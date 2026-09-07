# Context budget

Every page the agent reads costs context, and quality degrades well before the
window is full. Reading more is not reading better.

## Progressive disclosure

The pattern that works:

1. **Index first.** What exists, one line each.
2. **Open the pages that matter.** Usually three to eight.
3. **Follow links one hop at a time,** stopping when new pages stop adding.

Each step is cheap and informs the next. The alternative, loading everything
plausibly related up front, spends most of the budget on pages that turn out
irrelevant, and pushes the useful ones into the middle of a long context where
attention is weakest.

## Why not paste the whole vault

Long-context models can hold a lot, and it is tempting to skip retrieval
entirely.

Two reasons not to. Attention is uneven across a long context, and material in
the middle is used less reliably than material at the edges, which is the finding
in "Lost in the Middle" and the reason position matters at all. And an answer
built from everything cannot be checked: you have no idea which pages it actually
used.

An answer citing five pages you can open beats a fluent answer built from four
hundred you cannot.

## Summary layers

Past a few hundred pages, add one level of index between the master index and
the pages: a short page per topic area, listing what is in that area and what
each page covers.

The agent reads the master index, opens the one topic index that matters, then
opens pages. Three cheap reads instead of one expensive one.

Do not let summary layers accumulate. Two levels is enough; three means you are
building a hierarchy nobody maintains, and summaries of summaries drift from
what is underneath them.

## Measuring what was read

```
List the pages you read to answer that, in the order you opened them.
```

Worth running occasionally. It exposes two problems: an agent reading thirty
pages when six would do, and an agent answering from three when the vault has
twenty relevant ones. Both are fixable by adjusting the instructions, and neither
is visible from the answer alone.

## Subagents for wide reads

When a question genuinely needs a lot of material, send a
[subagent](../06-agents/subagents.md). It reads in its own context and returns a
summary, so the main session pays for the answer rather than for the sources.

## Next

[Outputs](../08-outputs/README.md), where the vault starts producing rather than
answering.
