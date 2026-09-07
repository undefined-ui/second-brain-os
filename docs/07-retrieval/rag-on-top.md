# Adding RAG when you need it

This guide argues against a vector database for a personal vault. That argument
has a threshold, and it is worth naming rather than treating as doctrine.

## When it starts to pay

Three conditions, roughly together:

**Scale past a few thousand pages,** where reading the index plus following
links stops fitting the context budget.

**Questions phrased in wording your pages do not use.** If you regularly fail to
find things you know are there, that is a recall problem, which is what
embeddings solve.

**A corpus you did not curate.** A vault that absorbed ten thousand documents
without a human deciding what mattered has no reliable structure to navigate,
so similarity is what is left.

Most personal vaults never hit all three. Mine has not, and I would not add the
maintenance for two out of three.

## What to embed

Not raw sources. Embed the wiki pages.

They are already semantic units, written by something that understood them, one
idea each. That is what chunking tries to approximate and rarely achieves.
Re-chunking them into fixed-size windows destroys the structure you paid for.

Embed the page title, aliases and body together. Titles carry a lot of signal
in a curated vault, because you chose them.

## Hybrid, not replacement

The useful arrangement keeps the graph in charge:

1. Embeddings find entry-point pages, including ones whose wording differs.
2. The graph expands from those entry points through links.
3. The agent reads the expanded set and answers with citations.

Embeddings supply recall, the graph supplies structure and the reason two pages
are related. Using similarity for the whole pipeline throws away the links,
which is the part of your vault that took work.

## Keeping the index fresh

This is the maintenance nobody accounts for. Every ingest changes pages, and a
stale embedding index returns pages whose content has moved on.

Re-embed changed pages as part of the ingest run, not on a separate schedule. An
index that lags by a week is quietly wrong in a way that produces plausible bad
answers.

If that sounds like more upkeep than it is worth, that is the correct reading for
most vaults, and it is the honest reason this section is short.

## Simpler things to try first

Before adding infrastructure, check whether the problem is actually recall.

Missing aliases are the most common cause of "I cannot find it". So is a bad
index. So is an ingest that stopped linking properly two months ago and left a
growing pile of orphans, which no retrieval method can reach.

Run `scripts/link_check.py` and read your index before concluding you need
vectors.

## Next

[Context budget](context-budget.md)
