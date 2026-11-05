# 资源

精选清单，而非全面罗列。这里所有资源均在 2026 年 9 月确认可以访问。

<a id="papers"></a>

## 论文

- [从局部到全局：面向查询摘要的图谱 RAG 方法](https://arxiv.org/abs/2404.16130)——Microsoft GraphRAG 论文。阅读时既要关注方法，也要关注问题如何界定；[GraphRAG](graphrag.md)篇是简明版本。
- [HippoRAG：受神经生物学启发的 LLM 长期记忆](https://arxiv.org/abs/2405.14831)——知识图谱加个性化 PageRank，用于多跳检索，发表于 NeurIPS 2024。这是最接近“智能体从一个页面出发沿链接向外走”这一行为的形式化方案。
- [从 RAG 到记忆：LLM 的非参数持续学习](https://arxiv.org/abs/2502.14802)——HippoRAG 2。论证了图谱记忆可以超越向量 RAG，同时在简单查找上也不落下风。
- [LightRAG：简单快速的检索增强生成](https://arxiv.org/abs/2410.05779)——大多数 2026 年系统默默借鉴的图谱加向量双层设计。
- [Zep：面向智能体记忆的时序知识图谱架构](https://arxiv.org/abs/2501.13956)——Graphiti 背后的设计论文；对“智能体记忆为什么需要在边上记录时间”给出了最清楚的书面解释。
- [何时在 RAG 中使用图谱](https://arxiv.org/abs/2506.05690)——冷静比较图谱检索在哪些地方有帮助、在哪些地方只是额外开销。读完上面那些热情洋溢的论文后，值得用它校正判断。

<a id="guides-and-courses"></a>

## 指南与课程

- [面向 RAG 的知识图谱](https://www.deeplearning.ai/courses/knowledge-graphs-rag)——DeepLearning.AI 与 Neo4j 合作的短课。几小时、动手实践，也讲 Cypher。
- [Neo4j GraphAcademy：知识图谱与 GraphRAG](https://graphacademy.neo4j.com/knowledge-graph-rag/)——免费、更深入、可按自己的节奏学习。
- [使用 LLM Graph Transformer 构建知识图谱](https://medium.com/data-science/building-knowledge-graphs-with-llm-graph-transformer-a91045c49b59)——Tomaz Bratanic 对受模式约束的抽取流程的讲解；这是该主题最有用的一篇实践文章。
- [使用 Neo4j 与 LangChain 实现“从局部到全局”GraphRAG](https://neo4j.com/blog/developer/global-graphrag-neo4j-langchain/)——逐步复现完整流水线，让你具体看到成本从何而来。
- [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)——Microsoft Research 介绍如何将索引成本延后到查询时承担。

<a id="repos-worth-reading"></a>

## 值得阅读的仓库

阅读 [Graphiti](https://github.com/getzep/graphiti)，学习如何正确处理时序边与实体消解；阅读 [LightRAG](https://github.com/HKUDS/LightRAG)，理解一条足够精简、能在脑中完整掌握的端到端流水线；将 [microsoft/graphrag](https://github.com/microsoft/graphrag) 作为已冻结的参考实现。持续更新的生态综述见[工具](tools.md)。

<a id="start-here"></a>

## 从这里开始

1. 阅读[为什么需要图谱](why-graphs.md)，针对自己的真实语料和真实问题进行门槛判断。如果达不到门槛，就停下来；你的 wiki 链接本来就是图谱。
2. 学习 DeepLearning.AI 的短课，再用 LightRAG 处理自己的一百篇文档，阅读抽取出的三元组。没有什么比这更快地揭示抽取的失败模式。
3. 阅读 Zep 论文，再借助[图谱存储](graph-stores.md)有意识地选择存储方案——先用文件，只有并发写入者迫使你升级时，才使用服务器。
