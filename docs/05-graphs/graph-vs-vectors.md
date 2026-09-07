# Graph vs embeddings

The usual advice for asking questions of your own documents is to embed them and
retrieve by similarity. This guide does not, and the reason is worth
understanding rather than taking on faith.

## What each is good at

**Embeddings** find text that means something similar to your query, including
when the wording is completely different. They are good at recall, they need no
structure, and they work on a pile of documents you have never organised.

**A graph** finds things that are explicitly connected, in a direction you can
follow, with a reason attached if the links are typed. It is good at
multi-hop questions and at telling you why two things are related.

## Where similarity fails

The failure is specific: similarity retrieves chunks that resemble the question,
and the answer to a good question often does not resemble it.

Ask what connects two ideas, and the passages that establish the connection may
share no vocabulary with either. Ask what you have changed your mind about, and
no chunk is similar to that, because the answer lives in the relationship
between two pages written a year apart.

There is also the ranking problem. Twenty chunks that all half-answer the
question crowd out the one page that answers it fully, because similarity has no
notion of completeness.

## Where the graph fails

Recall. If a page was never linked, the graph cannot reach it, and the linking
rules are exactly the thing that degrades quietly when ingestion gets sloppy.

The graph also cannot find the thing you half-remember but cannot name. That is
a search problem, and full-text search on a vault of a few thousand pages is
instant, which is why `ripgrep` covers most of this in practice.

## Why a personal vault leans graph

Three reasons specific to this scale.

Your corpus is small. A few thousand pages is not a retrieval problem, it is a
folder. The infrastructure that embeddings require pays off at millions of
documents and costs more than it returns below that.

Your corpus is already chunked. Atomic pages are semantic units written by
something that understood them. Splitting them again into fixed-size chunks
destroys the structure you paid to create.

Your questions are relational. What do I know about X, what connects X and Y,
what argues against Z. Those are graph queries.

## Hybrid, when you get there

The combination that makes sense: full-text search or embeddings to find
entry points, the graph to expand from them.

That way recall comes from search and structure comes from the graph, each doing
what it is good at. See [adding RAG when you need
it](../07-retrieval/rag-on-top.md) for the threshold where it starts to be worth
the maintenance.

## Next

[GraphRAG and where it fits](graphrag.md)
