# Search tools

Retrieval in a plain-text vault is mostly grep. That sounds primitive and is
almost always enough.

## ripgrep

```bash
rg -i "graph rag" ~/brain --type md -l
rg -i "supersed" ~/brain -C 2
```

Instant on tens of thousands of files. The agent uses it by default when working
on the filesystem, and for "where did I mention this" it beats every fancier
option on both speed and predictability.

Its limit is exact wording. It cannot find the page about a concept you
described differently, which is what the graph and the index are for.

## Obsidian search

Fine for interactive use. Operators worth knowing: `path:`, `file:`, `tag:` and
`line:` for terms co-occurring on the same line, which cuts most false positives.

## Dataview

Queries over frontmatter, which is where structural questions get answered:

````
```dataview
TABLE updated, tags FROM "wiki/concepts"
WHERE contains(tags, "unverified")
SORT updated ASC
```
````

Anything phrased as "which pages have property P" is a Dataview query, and
answering those by asking the agent to read files is slower and less reliable.

## Combining them

The pattern that works: Dataview or ripgrep to get a candidate set, the graph to
expand from it, the agent to read and synthesise.

```
Find every page tagged unverified, follow their links, and tell me which claims
depend on unverified sources.
```

Mechanical filtering first, judgement second. Asking the agent to do the
filtering by reading everything wastes context on pages a query would have
excluded in milliseconds.

## When search gets slow

It will not, at personal scale. Ripgrep over ten thousand markdown files is
still instant, and if search feels slow the cause is usually the agent reading
too many files, not the search itself.

That is a context problem, not a search problem. See [context
budget](context-budget.md).

## Next

[Adding RAG when you need it](rag-on-top.md)
