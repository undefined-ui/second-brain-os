# Linking rules

Links are the entire value of the structure. Without them you have a folder of
files with good filenames, which is a search index, and search indexes already
exist.

## The rule

Link the first mention of any concept or entity, on every page.

That is it. Applied consistently, it produces the graph on its own, with no
separate linking pass and no maintenance ritual.

## Link, do not restate

If you are explaining something that already has a page, link it and move on.

This is what keeps knowledge in one place. When the explanation of a concept
lives on four pages in four slightly different versions, updating it means
finding all four, and you will not. Linked, it lives once and improves once.

## Both directions

A new page links out to what it references. What it references links back.

One-directional linking produces pages that reference the vault but that the
vault never reaches. They exist, they are correct, and nothing finds them.
Obsidian shows unlinked backlinks, which helps you spot these, but the agent
should be closing the loop at ingest rather than leaving it to you.

## Links that do not exist yet

Write the link anyway, then either create the target page in the same run or
record it under Gaps in `index.md`.

Gaps are useful information. A page that three sources have linked to and that
does not exist yet is exactly what to write next, or exactly what to go read
about.

What is not acceptable is a permanent gap. Links to pages that will never exist
make the graph lie about its own coverage.

## How many

There is no target number, but the shape matters. A page with no outbound links
is a dead end. A page with forty is usually a list pretending to be a page.

Watch the average across the vault rather than any single page. Below roughly
two links per page, the graph is not connected enough to answer anything the
individual pages could not. Track it with `scripts/vault_stats.py`.

## Hub pages

Some pages accumulate links until everything routes through them. A general
concept that every source touches becomes a hub, and once it is a hub, the graph
around it stops being informative: everything is two hops from everything.

The fix is to split the hub into the specific ideas people are actually linking
to. If forty pages link to a single broad concept, they are linking to four
different aspects of it.

## Decorative links

A link is a claim that two pages are related in a way worth following. Links
added because a word happened to appear are noise, and enough of them make the
graph unusable in exactly the way an empty graph is unusable.

The test: would you follow this link while researching the topic? If not,
delete it.

## Next

[Frontmatter schema](frontmatter-schema.md)
