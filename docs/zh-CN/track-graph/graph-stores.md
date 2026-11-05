# 图谱存储

图谱存放在哪里，没有人们想的那么重要，却比供应商承认的更重要。对于个人和智能体的规模，合理的选择顺序应当从纯文本向上走，而不是从数据库向下选。

<a id="wikilinks-as-the-graph"></a>

## 用双向链接构成图谱

一个文件夹里放着 Markdown 文件，以 `[[Page]]` 链接作为边，这就是知识图谱。整个网站正是建立在这个模式之上：实体是页面，关系是链接——如果遵循[带类型的链接](../05-graphs/typed-links.md)，关系也可以有类型——存储层就是文件系统。智能体用 grep 和沿链接访问来查询，你则用 Obsidian 查询。没有服务器、没有驱动、没有迁移，而且图谱的主人可以直接阅读它。规模为几千个节点时，这不是妥协，而是正确选择。

<a id="networkx-in-files"></a>

## 将 NetworkX 图保存为文件

当你需要算法——PageRank、社区发现、中心性分析——就把图谱加载到 [NetworkX](https://networkx.org)，并以 GraphML 或 JSON 形式与笔记一起保存。它在 Python 内存中运行，不需要基础设施，几万个节点也能胜任。多个 [GraphRAG](graphrag.md) 实现默认就采用这种后端，这也说明了它们实际预期的规模。

<a id="embedded-databases-and-the-kuzu-lesson"></a>

## 嵌入式数据库与 Kuzu 的教训

Kuzu 曾是嵌入式方案的显然选择——图数据库版 DuckDB、支持 Cypher、单文件存储。后来 Kùzu Inc. 被 Apple 收购，[仓库](https://github.com/kuzudb/kuzu)于 2025 年 10 月归档，最终版本停在 0.11.3。它仍然可用，也有社区分支，但这件事恰好为上面的方案提供了理由：MIT 许可证保住了代码，而普通文件本来就无需谁来保全。[Kuzu 之后的生态](https://gdotv.com/blog/kuzu-legacy-embedded-graph-database-landscape/)仍在重整之中。

<a id="servers-neo4j-and-falkordb"></a>

## 服务器：Neo4j 与 FalkorDB

[Neo4j](https://neo4j.com) 是老牌方案：支持 Cypher，生态最大，各个框架都有一流集成，免费层也足以满足个人使用。代价在于运维——它是一台服务器，现在你得负责运行它。[FalkorDB](https://www.falkordb.com/) 是更轻量的替代品，作为 Redis 模块运行的图数据库，明确面向 GraphRAG 工作负载，并拥有正在积极开发的 SDK。当一组智能体共享同一个图谱，而且查询延迟很重要时，这类方案就比较合理。

<a id="what-fits-what"></a>

## 不同场景适合什么

- 一个人、经过整理的语料：双向链接。你正在阅读的就是概念验证。
- 个人语料加图算法：在导出的链接上使用 NetworkX。
- 单个智能体的记忆：使用记忆库默认的方案即可——[Graphiti](https://github.com/getzep/graphiti) 需要 Neo4j 或 FalkorDB，其他库可能内置 NetworkX。见[工具](tools.md)。
- 多智能体共享、并发写入：使用真正的服务器，此时你也就多了一个需要运维的数据库。

先让抽取流水线正常工作，再选择存储方案，不要反过来。文件中的图谱，一个下午就能迁移到 Neo4j；而反向迁移，往往是项目发现自己的图谱从来不值得维护一台服务器的过程。判断门槛的逻辑见[为什么需要图谱](why-graphs.md)。
