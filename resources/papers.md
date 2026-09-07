# Papers

Research relevant to how a knowledge base retrieves and reasons. Read these if
you want to decide for yourself whether you need a vector database.

## GraphRAG

**[From Local to Global: A Graph RAG Approach to Query-Focused
Summarization](https://arxiv.org/abs/2404.16130)** (arXiv:2404.16130). Edge,
Trinh, Cheng, Bradley, Chao, Mody, Truitt, Metropolitansky, Ness, Larson.
Microsoft Research. Implementation at
[microsoft/graphrag](https://github.com/microsoft/graphrag).

The paper that named the approach. Its argument is specific and worth getting
right: RAG fails on global questions about an entire corpus, such as what the
main themes are, because that is a summarization task rather than a retrieval
task. Their pipeline derives an entity graph from the documents, pregenerates
summaries for communities of closely related entities, and answers global
questions from those summaries.

Relevant to a second brain because the failure it targets, questions about the
whole corpus, is exactly what people want from one. See
[GraphRAG and where it fits](../docs/05-graphs/graphrag.md) for why you probably
do not need to run it at personal scale.

## HippoRAG

**[HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language
Models](https://arxiv.org/abs/2405.14831)** (arXiv:2405.14831). Gutiérrez, Shu,
Gu, Yasunaga, Su.

Retrieval over a knowledge graph using personalised PageRank, aimed at multi-hop
questions. The closest published analogue of what an agent does walking links
outward from a starting page, which makes it the more directly relevant of the
two graph papers here.

## Lost in the Middle

**[Lost in the Middle: How Language Models Use Long
Contexts](https://arxiv.org/abs/2307.03172)** (arXiv:2307.03172). Liu, Lin,
Hewitt, Paranjape, Bevilacqua, Petroni, Liang. Published in TACL.

The empirical basis for not pasting your whole vault into context. Performance
is highest when the relevant information sits at the beginning or end of the
input and degrades significantly when the model has to use something in the
middle of a long context, including for models built for long contexts.

This is why [progressive
disclosure](../docs/07-retrieval/context-budget.md) beats loading everything,
and why an answer citing five pages is more trustworthy than one assembled from
four hundred.

## How to read these

All three are specific about the conditions their results hold under. Those
conditions are what decide whether the finding transfers to a personal vault of
a few thousand curated pages, which is a very different setting from the
corpora they evaluate on.

Read the limitations sections. That is the habit this whole guide is trying to
encode.
