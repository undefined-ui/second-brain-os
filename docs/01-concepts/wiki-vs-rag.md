# Wiki vs RAG

The default advice for asking questions of your own documents is to embed them
in a vector database. This guide does something else, and the reason is
structural rather than a preference about tools.

## The two approaches

**RAG** stores your documents as chunks with embeddings. A question retrieves the
most similar chunks and the model answers from them. Nothing is written; the
corpus stays as it was.

**A wiki** processes documents once, into pages an agent wrote and linked.
Questions are answered by navigating those pages. The corpus is transformed and
keeps improving.

The difference is where the work happens. RAG does it at query time, every time,
from scratch. A wiki does it once, at ingest, and the result is reused.

## What that buys

**Understanding accumulates.** The tenth source about a topic improves the page
the first nine built. In RAG, the tenth document is just another chunk, and
nothing gets better as the corpus grows, only larger.

**Contradictions are visible.** Two documents disagreeing produce two chunks that
may never be retrieved together. On a page, the disagreement is written down,
dated, and unavoidable.

**Answers are checkable.** The page cites sources you can open. Retrieved chunks
are fragments without the reasoning that connected them.

**No infrastructure.** No index, no re-embedding, no drift between the store and
the files.

## What it costs

**Ingest is expensive.** Writing and linking pages costs model time up front,
where RAG's ingest is nearly free.

**Quality depends on the ingest.** A bad page contract produces a bad vault, and
you find out later. RAG's failures are at query time and are more visible.

**Recall depends on linking.** A page nobody linked is a page the graph cannot
reach. RAG will find it by similarity regardless.

## The honest position

This trade is right for a personal, curated corpus of a few thousand pages and
wrong for a million documents nobody organised.

Which is to say it is right for a second brain and wrong for a search product,
and most advice about RAG is written for the second case. See [adding RAG when
you need it](../07-retrieval/rag-on-top.md) for the threshold where the answer
flips, and [graph vs embeddings](../05-graphs/graph-vs-vectors.md) for the
retrieval mechanics.

## Next

[What good looks like](what-good-looks-like.md)
