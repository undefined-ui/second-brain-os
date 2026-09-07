# Reading the Obsidian graph view

The global graph is the screenshot everyone posts. It is the least useful view
in the app.

At two hundred pages it is a hairball, and a hairball tells you nothing except
that you have pages. What it is good for is spotting shape at a glance: isolated
clumps, a single dominant hub, a scatter of unconnected dots around the edge.

## Local graph

This is the view that does work. Open a page, show the local graph, set depth to
two.

You are looking for two things. What is one hop away should be obviously
related; anything surprising there is either a decorative link to delete or a
connection worth reading. What is missing at two hops tells you where the page
is under-connected.

Reviewing the local graph of a page you just wrote is the fastest quality check
there is, and it takes five seconds.

## Filters that make the global view usable

- **Filter by type.** `-path:sources` hides source pages and leaves the concept
  graph, which is the part with meaning in it. Sources outnumber concepts
  heavily and drown them visually.
- **Groups by colour.** Colour concepts, entities and synthesis differently. A
  cluster with no concept pages in it is a pile of sources nobody has processed.
- **Orphan toggle.** Turn orphans on deliberately, look at what appears, then
  fix or delete them.
- **Depth and forces.** Lower link force spreads clusters apart enough to see
  bridges.

## What to look for

**Dots at the edge, connected to one thing.** Failed ingests, usually. The
source page was written and the concepts never linked back.

**One giant node in the middle.** A hub that has swallowed the graph. Split it.

**Two clusters with a single connecting page.** That page is doing real work.
It is also fragile: if it is wrong, both clusters are wrong about each other.

**A cluster you do not recognise.** Usually the most interesting thing on
screen. It means the vault has accumulated material on a topic you have not
consciously been tracking.

## What the view cannot tell you

It shows that pages are connected, never why. Every edge looks the same whether
it means "supports", "contradicts" or "mentioned once in passing".

That limitation is the entire argument for the next page.

## Next

[Typed links](typed-links.md)
