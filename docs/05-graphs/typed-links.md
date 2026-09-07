# Typed links

A plain `[[wikilink]]` says two pages are related. It does not say how, and at
scale that is a real loss.

You cannot ask an untyped graph what contradicts a claim, what evidence supports
it, or which pages extend a method. Every edge is the same edge, so every
question collapses to "what is nearby".

## A minimal vocabulary

Small enough to remember, expressive enough to be worth it:

- **supports** - this page is evidence for that one
- **contradicts** - this page argues against it
- **extends** - builds on it, adds to it
- **part-of** - a component of a larger thing
- **applies** - a use of a method in practice

Five is deliberately few. Every additional type is one the agent has to choose
between correctly on every link, and a vocabulary of twenty produces
inconsistent tagging, which is worse than none.

## Two ways to encode it

**Inline, next to the link:**

```markdown
The position sensitivity result (supports:: [[Lost in the Middle]]) suggests
context length alone does not fix retrieval.
```

Dataview reads inline fields, so this is queryable inside Obsidian without extra
tooling.

**In frontmatter, per page:**

```yaml
contradicts: ["[[Long context replaces RAG]]"]
extends: ["[[Retrieval augmented generation]]"]
```

Cleaner to query, further from the sentence the link came from. Frontmatter for
page-level relationships, inline for claim-level ones.

## What it buys you

```dataview
LIST FROM "wiki/concepts"
WHERE contains(contradicts, this.file.link)
```

That is "everything in my vault that argues against this page", which is a
question a plain graph cannot answer at all.

At the agent level it is stronger still. An ingest that records a new source as
`contradicts` an existing page has done the work of flagging the disagreement
structurally, rather than burying it in prose that only surfaces if someone
reads the page.

## Do not type everything

Most links are plain mentions and should stay plain. Typing every link makes the
vocabulary meaningless and makes ingestion slower and more error-prone.

Type the links where the relationship is the point: evidence, disagreement,
extension. Roughly one in five links, in practice.

## The instruction

```
When a source supports, contradicts or extends a claim on an existing page,
record the relationship with a typed link. Plain wikilinks for ordinary
mentions. Do not type a relationship you are inferring; only type what the
source states.
```

That last sentence matters. An agent guessing at relationships produces a graph
that looks rigorous and encodes its own assumptions.

## Next

[Graph vs embeddings](graph-vs-vectors.md)
