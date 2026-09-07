# Naming and aliases

Wikilinks resolve by name, so the name is not cosmetic. It is the key the whole
graph is built on.

## Canonical titles

One page, one canonical title, and it is the name you would use talking to
someone in the field.

Practical rules that avoid most of the pain:

- **Singular, not plural.** `Vector database`, not `Vector databases`.
- **Spell out acronyms in the title, put the acronym in aliases.** The title is
  for the reader, the alias is for the link.
- **No dates, no versions in the title** unless the thing genuinely is a
  version. A page called `MCP spec 2026-07` becomes wrong in a month; a page
  called `MCP` with a version history does not.
- **No your-vault-specific prefixes.** `Concept - RAG` fights the link syntax
  for no benefit.

## Aliases

Everything the same subject gets called, listed in frontmatter:

```yaml
title: Retrieval augmented generation
aliases: [RAG, retrieval-augmented generation]
```

Aliases are what stop the vault from quietly growing three pages for one thing.
Without the alias, a source that says RAG creates `RAG`, and a source that
spells it out creates a second page, and neither knows about the other.

Add aliases at creation, not later. By the time you notice the duplicate, both
pages have inbound links.

## Two things with the same name

Disambiguate in the title, not with a suffix nobody would type:

```
Mercury (planet)
Mercury (element)
```

Then alias the bare word to whichever one is dominant in your vault, or to
neither if both matter, which forces the agent to pick explicitly rather than
guessing.

Same applies to people who share a name and to your own projects that collide
with a well-known product.

## Renaming

Obsidian updates links when you rename inside the app. The agent renaming a file
directly does not, and that is the single most common source of broken links in
an agent-maintained vault.

Rule for `CLAUDE.md`: renames go through a documented procedure. Update the
file, update every inbound link, add the old name as an alias, and record it in
`log.md`. The alias matters because it keeps external references and your own
memory working.

Then run `scripts/link_check.py` to confirm nothing dangled.

## Next

[Deduplication and merging](dedupe-and-merge.md)
