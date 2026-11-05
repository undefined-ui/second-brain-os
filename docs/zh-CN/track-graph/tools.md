# 工具

截至 2026 年 9 月的生态综述。这个领域在 2025 年经历了明显整合：批量索引那一代方案逐渐沉寂，面向增量更新和记忆的新一代接过了主导地位。

<a id="memory-and-graph-rag-frameworks"></a>

## 记忆与图谱 RAG 框架

- [Graphiti](https://github.com/getzep/graphiti)——由 Zep 开发、用于智能体记忆的时序知识图谱。每条边都带有有效时间区间，遇到矛盾时会将旧边标为失效而不是覆盖，并支持时间点查询。它是长期运行智能体的最强选项，也支撑着 Zep 的托管[记忆平台](https://www.getzep.com)。
- [Cognee](https://github.com/topoteretes/cognee)——自托管记忆引擎，在同一条流水线中结合图谱与向量；集成生态不断扩大（包括 n8n、智能体框架），Rust 核心正在开发中。项目活跃、维护良好。
- [LightRAG](https://github.com/HKUDS/LightRAG)——务实的 GraphRAG：图谱加向量双索引、增量更新、多种存储后端（Neo4j、PostgreSQL、MongoDB）。论文发表于 EMNLP 2025，目前仍在积极开发。
- [fast-graphrag](https://github.com/circlemind-ai/fast-graphrag)——Circlemind 基于 PageRank 的实现；跳过社区摘要，以低成本进行遍历。
- [microsoft/graphrag](https://github.com/microsoft/graphrag)——原始实现，现已进入维护模式。适合阅读，不宜基于它继续构建；背景见 [GraphRAG](graphrag.md)。

<a id="framework-integrations"></a>

## 框架集成

- [LlamaIndex 属性图索引](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/)——最完整的框架原生选项：可插拔的抽取器（支持模式约束或自由格式），以及适用于任何属性图存储的检索器。
- [LangChain LLMGraphTransformer](https://reference.langchain.com/python/langchain-neo4j/graph_transformers/llm/LLMGraphTransformer)——输入文档，输出图文档。注意，它已从 `langchain-experimental` 移入 `langchain-neo4j` 软件包，旧导入路径已经失效。
- [Neo4j LLM 知识图谱构建器](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/)——托管的点击式流水线，可将 PDF、网页和 YouTube 字幕转为 Neo4j 图谱。在写代码之前，适合先用它看看抽取会如何处理你的材料。
- [FalkorDB GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)——基于 FalkorDB、优先设计本体的 SDK，已具备生产稳定性，而且迭代迅速。

<a id="visualisers"></a>

## 可视化工具

[Gephi](https://gephi.org) 仍是离线分析导出图谱的主力工具——加载 GraphML，运行布局和社区着色，找出此前未曾察觉的结构。Neo4j 自带的 Browser 和 Bloom 则覆盖数据库原生可视化场景。

<a id="obsidian-graph-tooling"></a>

## Obsidian 图谱工具

内置关系图谱视图更像一幅画，而不是分析仪器；真正的工作靠插件。[InfraNodus](https://github.com/noduslabs/infranodus-obsidian-plugin) 为知识库加入正式的网络分析——主题聚类、中心性、结构空缺——并用 AI 针对空缺生成问题。[Extended Graph](https://www.obsidianstats.com/plugins/extended-graph) 用过滤和按类型设置样式来增强原生视图。Obsidian Hub 维护着持续更新的[图谱插件列表](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.01+Plugins+by+Category/Graph+plugins)。

<a id="choosing"></a>

## 如何选择

智能体记忆：Graphiti 或 Cognee。查询文档语料库：LightRAG。已经在使用 LlamaIndex 或 LangChain：采用它们的原生抽取器，并写入[图谱存储](graph-stores.md)中介绍的某种存储。经过整理的知识库：你的链接就是图谱；需要分析功能时，再添加 InfraNodus。
