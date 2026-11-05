# 用 LLM 构建图谱

抽取决定一切。图谱存储会忠实保存你放进去的任何东西；那究竟是知识还是噪声，取决于流水线。本篇介绍这条流水线在实践中应当是什么样。

<a id="schema-before-extraction"></a>

## 先定数据模式，再做抽取

不加约束的抽取会产生一个杂物抽屉：同一个事实，被 `WORKS_AT`、`WORKS_FOR`、`EMPLOYED_BY` 三种不同的边表示。先确定本体，哪怕很小也好——五类实体、十类关系，就足以覆盖大多数个人语料和智能体语料。成熟工具都允许你将其作为约束传入：LangChain 的 [LLMGraphTransformer](https://reference.langchain.com/python/langchain-neo4j/graph_transformers/llm/LLMGraphTransformer) 接受 `allowed_nodes` 和 `allowed_relationships`；LlamaIndex 的[属性图索引](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/)提供 `SchemaLLMPathExtractor`，在抽取时强制执行类型约束。

起步时的范围要比直觉认为合适的再窄一些。日后扩展数据模式很便宜；收拢一大堆近似重复的谓词，却并不便宜。

<a id="the-extraction-pass"></a>

## 抽取过程

不同工具的基本机制是一致的：切分源文本，提示模型输出带类型的三元组，并为每个实体附上一段简短描述，同时保留出处——每个三元组来自哪个文本块、哪篇文档、哪个日期。出处信息让你能够回答“图谱为什么认为这是真的”，也能在来源撤回时删除对应的边。结构化输出模式让解析更加可靠；剩下的失败是语义问题，而非语法问题，因此每一批都要抽样阅读几十个三元组，不要只信通过率。

<a id="incremental-updates"></a>

## 增量更新

原始 [GraphRAG](graphrag.md) 流水线假定采用批量重建索引，但对于每天变化的语料库，这种成本难以承受。新一代方案从一开始就围绕增量更新设计。[Graphiti](https://github.com/getzep/graphiti) 在这方面的设计最为出色：每个新事件片段都会被抽取，并与现有图谱核对；相互矛盾的边不会被删除，而是带时间戳标记为失效——图谱会同时保留“三月之前为真”和“三月起为真”。对于智能体记忆，这个时间层就是记忆与缓存的区别。

<a id="dedup-and-entity-resolution"></a>

## 去重与实体消解

同一个人可能以 `J. Smith`、`John Smith` 和 `john from ops` 三种形式出现。合并策略按成本递增依次是：精确名称匹配和规范化名称匹配；对实体描述计算嵌入相似度并设置阈值；由 LLM 裁决候选实体对。先做廉价层，只有剩余的模糊情况才交给模型。在写入时就完成消解——如果把去重留给之后的批处理作业，那么在执行之前，每次查询看到的都是碎片化图谱。

<a id="keep-the-loop-small"></a>

## 保持迭代循环精简

先抽取一百篇文档，查看图谱，修正数据模式，然后重新运行。失败的流水线，往往是那些在任何人查看之前就处理了整个语料库的流水线。结果应该放在哪里——嵌入式数据库、文件，还是普通双向链接——是[图谱存储](graph-stores.md)的主题；现成实现则在[工具](tools.md)篇中综述。
