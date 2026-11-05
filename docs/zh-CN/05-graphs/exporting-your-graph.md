# 导出图谱

Obsidian 的图谱视图只是一个查看器。要进行计算，就需要把图谱导出到外部。

<a id="export"></a>

## 导出

```bash
python3 scripts/graph_export.py ~/brain edges.csv
python3 scripts/graph_export.py ~/brain graph.graphml --format graphml
```

脚本会将每个 wikilink 解析为边列表中的一条边，将页面的 `type` 保留为节点属性，而且无需任何依赖。CSV 适合代码处理，GraphML 适合 Gephi。

<a id="analysis"></a>

## 分析

```python
import networkx as nx, csv

g = nx.DiGraph()
with open("edges.csv") as f:
    next(f)
    g.add_edges_from(tuple(r) for r in csv.reader(f))

print(nx.number_weakly_connected_components(g))
print(sorted(nx.pagerank(g).items(), key=lambda kv: -kv[1])[:10])
print([n for n in g if g.in_degree(n) == 0])
```

十行代码回答三个问题：知识库有多碎片化、哪些页面在结构上处于核心位置，以及哪些页面无法到达。

值得对知识图谱运行一次 PageRank。排名最靠前的页面，揭示了你的知识库实际上围绕什么展开，而这往往与你自己描述的主题不同。

<a id="betweenness-the-one-worth-the-compute"></a>

## 介数：值得花计算资源的指标

```python
b = nx.betweenness_centrality(g)
```

介数衡量一个页面出现在另外两个页面之间最短路径上的频率。介数高的页面，是不同簇之间的桥梁。

它们重要的原因有两个。一是它们是最有价值的页面，保存着任何单个来源都未曾包含的联系。二是它们也是薄弱点：如果桥梁页面出错，或者在合并时被删除，知识库的两个领域就会悄悄失去相互提供信息的能力。

<a id="graph-databases"></a>

## 图数据库

[Ladybug](https://github.com/LadybugDB/ladybug) 是嵌入式数据库，无需服务器，可以[直接读取 CSV](https://docs.ladybugdb.com/import/csv)。用 Cypher 查询自己的笔记，足够让你愉快地探索一晚上。它是 Kuzu 的持续维护版本，Kuzu 已于 2025 年 10 月归档。Neo4j 则是功能更完整的选择，除非你打算在此基础上构建应用，否则有些大材小用。

要明确它的定位：这是分析层，而不是替代品。Markdown 仍是权威来源，数据库只是可以重新生成的衍生数据。一旦你开始写入只存在于数据库中的知识，就失去了让这整套方法值得选择的可移植性。

<a id="gephi"></a>

## Gephi

它适合查看图谱，而不是计算。加载 GraphML，运行 ForceAtlas2，按度设置节点大小，按类型着色。它能以 Obsidian 无法实现的方式渲染大型图谱；如果你想得到一张值得展示的截图，就使用它。

<a id="keep-it-in-sync"></a>

## 保持同步

导出结果是快照，生成后就开始过时。重新生成它，而不是维护它；也绝不要修改导出的图谱，并期待知识库随之更新。

<a id="next"></a>

## 下一步

[值得跟踪的图谱指标](metrics.md)
