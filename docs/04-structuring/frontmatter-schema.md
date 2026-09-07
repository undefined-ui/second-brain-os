# Frontmatter schema

Frontmatter is what makes the vault queryable by something other than text
search. It costs nothing to write and it is what Dataview, scripts and the agent
itself use to find things by shape.

## The schema

```yaml
---
title: Canonical name
type: source | entity | concept | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases: [other names this is known by]
tags: [two or three]
---
```

Source pages add:

```yaml
url: https://...
author:
published: YYYY-MM-DD
```

Entity pages add `kind: person | org | product | tool`.

## Why each field earns its place

`type` drives every structural query and every lint check. Without it you cannot
ask how many concepts you have, or find sources with no concepts attached.

`updated` is what makes review possible. Stale concept pages are the main way a
vault rots, and you cannot find them without a date.

`aliases` is what makes wikilinks resolve when the same thing has three names.
See [naming and aliases](naming-and-aliases.md).

`url` on a source page is what separates a citation from a claim. A source page
without it is unverifiable.

## Tags

Two or three per page, from a small controlled vocabulary you actually maintain.

Tags fail in one specific way: the vocabulary grows until it is meaningless.
Fifty tags used once each are worse than no tags, because they create the
impression of a taxonomy while doing none of the work.

Keep the list in `CLAUDE.md` and instruct the agent to use existing tags or
propose a new one explicitly rather than inventing them silently.

Folders and links carry the structural load. Tags are for cross-cutting
qualities that do not fit either: `unverified`, `to-revisit`, `disputed`.

## Empty fields

Leave a field out rather than filling it with a guess. An absent `published`
means unknown, which the agent can say honestly. A guessed date becomes a fact
in a concept page three weeks later.

## Keep it stable

Adding a field to the schema means either backfilling every page or living with
a mixed vault where queries miss the older half.

Decide the schema early, keep it small, and change it rarely. When you do change
it, run a backfill pass over the whole vault in one go rather than letting the
change apply only to new pages.

## Next

[Naming and aliases](naming-and-aliases.md)
