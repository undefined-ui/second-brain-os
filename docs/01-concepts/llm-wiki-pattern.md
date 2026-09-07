# The LLM wiki pattern

The specific pattern this guide implements, published by Andrej Karpathy as a
gist on 2026-04-04.

The inversion in one sentence: instead of you maintaining notes and occasionally
asking an AI about them, the AI maintains the wiki and you read it.

## What the pattern specifies

**The wiki is primary.** Raw sources are an archive you keep and rarely open.
The wiki is what you and the agent both work from, written in plain language,
one idea per page, densely linked.

**Compilation, not summarization.** Each new source is integrated into existing
pages rather than added beside them as another summary. A page about a concept
improves as sources accumulate; it does not turn into a list of what each source
said.

**Three operations.** Ingest brings new material in. Lint keeps the structure
sound. Query answers from the wiki. Everything else is variation on those.

## Why it holds up

Because it removes the one task that killed every previous system. Linking fifty
notes to each other every time you read a paper is genuinely boring work that
humans stop doing, and the wiki dies when the maintainer gets tired.

The other reason is that it needs no infrastructure. Markdown files, wikilinks,
an agent that can read and write files. No database, no index to keep fresh, no
service to depend on.

## Where the gist stops

It describes intent, not implementation. Integrate new sources, lint
periodically, treat the wiki as primary.

The mechanics are left open, which is why every implementation of it differs.
How integration handles contradictions, what a page must contain, when lint
runs, who the wiki is written for. This guide's answers to those are in
[Structuring](../04-structuring/README.md), and they are opinions, not the
pattern itself.

## What people build on top

The common extensions are a journal layer, a project layer, and scheduled
automation. This guide covers the second and third as [the two
layers](two-layers.md) and [Agents](../06-agents/README.md).

The pattern also spread quickly because the primitives are ordinary: anyone with
an agent and a folder can run it, and the implementations are all readable
markdown. See [resources](../../resources/repos.md) for the ones worth reading.

## Next

[The two layers](two-layers.md)
