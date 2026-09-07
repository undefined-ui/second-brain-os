# Graph basics for a knowledge base

Your vault is a graph whether you plan it or not. Pages are nodes, wikilinks are
edges. Every structural decision in the previous section was a decision about
what shape that graph takes.

Four terms are enough to reason about it.

**Degree** is how many links a page has. In-degree is how many point at it,
out-degree how many it points out. A page with zero in-degree is unreachable by
following links, which is what makes orphans a problem rather than a cosmetic
issue.

**Path length** is how many hops separate two pages. This is the one that
matters for answers: the agent following links from a starting page can only
reach what is a few hops away before the context budget runs out. Two related
ideas eight hops apart will never be connected in an answer.

**Clustering** is how much a page's neighbours link to each other. High
clustering means a genuine topic area. Low clustering with high degree usually
means a page that collects unrelated things.

**Components** are the disconnected islands. A vault in five components is five
vaults, and nothing in one will ever inform an answer about another.

## The shapes that go wrong

**The star.** Everything links to two or three hub pages and to nothing else.
Path length between any two leaves is short, but only through the hub, so the
graph tells you nothing beyond "these are all in my vault". Usually caused by
linking to broad concepts instead of specific ones.

**The chain.** Sources link to the concept they introduced and nothing links
sideways. Common after a bulk import that ran without checking existing pages.
The vault grows and never connects.

**Islands.** Distinct topic clusters with no bridges. Sometimes legitimate: your
cooking notes and your database notes genuinely do not connect. Often not: two
clusters about related things that were built under different vocabulary and
never linked because the aliases were missing.

## What a healthy graph looks like

Dense within topics, sparse but present between them. Most pages reachable from
most pages within three or four hops. Hubs that exist but do not dominate. A
small number of bridge pages that connect clusters, which are usually your most
valuable pages, because they hold the connections you could not have made from
one source alone.

## Why any of this matters

When you ask the vault something, the agent starts at the pages that match and
walks outward. The graph is the search space. A well-shaped graph means the walk
reaches the relevant material in a few hops; a badly shaped one means it either
reaches nothing or reaches everything.

That is the whole argument for the linking rules. They are not tidiness, they
are what determines whether retrieval works.

## Next

[Reading the Obsidian graph view](obsidian-graph-view.md)
