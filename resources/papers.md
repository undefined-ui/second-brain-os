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

## New in October 2026

Submitted to arXiv between September and October 2026. Preprints, so read them
with the same habit as above.

**[Follow the Entities: A Corpus Map for Agentic Search](https://arxiv.org/abs/2609.37226)** (arXiv:2609.37226, 29 September 2026). An offline pass writes one page per recurring entity that links to every document mentioning it, and agents walk that map instead of searching flat files. Across seven models and three benchmarks they found more evidence with fewer tokens. It is close to a measurement of the llm-wiki pattern itself.

**[Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses](https://arxiv.org/abs/2610.41172)** (arXiv:2610.41172, 30 October 2026). A harness with only grep and BM25 answered 85% of BrowseComp-Plus and 91% of FRAMES with no vector index. Compiled artifacts such as entity graphs and wikis added no accuracy, but a claim-evidence tree cut query tokens by 38% on average. Support for "no vector database until you need one", and a reminder of what the wiki is for.

**[Keep Your Receipts: Trustworthy Cleanup of Agent-Built Knowledge Graphs](https://arxiv.org/abs/2610.17719)** (arXiv:2610.17719, 13 October 2026). Every merge, edge and summary sentence the model writes records the evidence behind it, so deleting a retracted source becomes set arithmetic with no model calls. Two builds of the same 300 documents differed in 29,475 artifacts, which is why rebuilding from scratch is not a fix.

**[LiteRAG: Cost-Efficient Graph-Based Retrieval-Augmented Generation](https://arxiv.org/abs/2609.10239)** (arXiv:2609.10239, 9 September 2026). Graph retrieval steered by algorithms at query time, with adaptive thresholds and a penalty on hub nodes, instead of an LLM on every hop. Against GraphRAG Global and DRIFT it cut latency over 100x and cost over 99% while matching quality.

**[EvalMem: An Operation-Level Diagnostic Framework for Long-Term Memory Systems](https://arxiv.org/abs/2609.22231)** (arXiv:2609.22231, 3 September 2026). Splits every memory failure into not stored, not retrieved or not used, and retrieval was the most common. Adding a wiki-style layer of source pages, hub pages and versioned facts improved accuracy by 2.5 points on LoCoMo.

**[CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents](https://arxiv.org/abs/2609.26779)** (arXiv:2609.26779, 22 September 2026). Compaction that only truncates or drops content and never compacts an earlier compaction. Up to 50% cheaper under a bounded context, with Terminal-Bench scores held or improved, and simple enough to copy.

**[The Unreliable Progress Bar: Can LLM Agents Reliably Report Task Progress Throughout Execution?](https://arxiv.org/abs/2609.08589)** (arXiv:2609.08589, 8 September 2026). Most models lose accuracy reporting their own progress mid-task, and the newest turn conservative near the finish. The authors conclude that frameworks should not drive task flow on self-reports alone, which is the case for stop rules owned by the runtime.

**[Frozen Judges, Moving Agents: Version-Dependent LLM-Judge Error](https://arxiv.org/abs/2609.34198)** (arXiv:2609.34198, 28 September 2026). A fixed LLM judge makes different errors on different agent versions. On SWE-bench Verified, eight judge-only comparisons declared upgrades that execution results could not confirm. Do not sign off an upgrade on judge scores alone.
