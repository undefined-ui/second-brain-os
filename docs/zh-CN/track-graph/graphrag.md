# GraphRAG

GraphRAG 是一种检索增强生成：它的索引是从语料库构建的图谱，而不是一堆经过嵌入的文本块。经典版本来自 Microsoft Research 2024 年的论文[从局部到全局](https://arxiv.org/abs/2404.16130)，针对的正是向量 RAG 最不擅长的问题：关于整个语料库的查询。

<a id="the-pattern"></a>

## 基本模式

四个阶段，全部发生在建立索引时：

1. **实体抽取。** LLM 阅读每个文本块，输出实体与关系，通常是带描述的 `(subject, predicate, object)` 三元组。
2. **图谱构建。** 将三元组合并为图谱，并消解重复实体。
3. **社区发现。** 聚类算法（原版使用 Leiden）找出连接密集的邻域。
4. **社区摘要。** LLM 按层级为每个社区撰写报告，使语料库在多个缩放层级上都有摘要。

局部查询从匹配到的实体出发遍历图谱。全局查询则遍历各社区摘要，再归并为一个答案——因此，“主要主题是什么”终于能得到回答。

<a id="microsoft-graphrag-and-its-successors"></a>

## Microsoft GraphRAG 及其后继者

[microsoft/graphrag](https://github.com/microsoft/graphrag) 仓库现已进入维护模式：只修复缺陷和 CVE 漏洞，不再开发新功能。应把它当作值得阅读的参考实现，而不是准备采用的框架。

有意思的进展已经转向成本更低的后继方案。[LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) 将几乎全部 LLM 工作延后到查询时进行——不预先生成摘要——据称索引成本仅为原版的 0.1%，不过它最终进入了 Microsoft 的 Azure 产品，而非开放库。在开源领域，[LightRAG](https://github.com/HKUDS/LightRAG)（EMNLP 2025，仍在积极开发）维护图谱加向量的双索引，并支持增量更新；[fast-graphrag](https://github.com/circlemind-ai/fast-graphrag) 则用 PageRank 遍历替代社区摘要。2026 年的大部分新部署会从这些方案中选择；[工具](tools.md)篇会综述这一领域。

<a id="costs-and-trade-offs"></a>

## 成本与取舍

原始流水线的昂贵之处很具体：导入时，每个文本块都要经过 LLM；接着每个社区都要生成摘要，再沿着层级逐级生成摘要。即使语料库规模适中，建立索引也要花真金白银，内容编辑后重新索引还要再花一次。后继方案正是为了避免这笔开销而存在——采用惰性求值、增量更新，或者干脆省略摘要。

不那么显眼的取舍是保真度。抽取会把细微含义压平为三元组；保留措辞、日期限定或信息归属可能因此消失。社区摘要终究是摘要——让模型压缩它并不理解的文本时，所有可能的失败模式，它都会继承。GraphRAG 能回答向量 RAG 无法回答的全局问题，但它的答案距离原始来源又多隔了一层模型生成内容。

<a id="when-it-earns-its-keep"></a>

## 什么时候值得使用

适合大规模、未经整理，而且确实存在多跳和主题类问题的语料库——门槛判断见[为什么需要图谱](why-graphs.md)。对于经过整理的个人知识库，你已经手动完成了抽取；仍然值得借鉴的是流水线的结构，见[用 LLM 构建图谱](building-graphs-with-llms.md)。
