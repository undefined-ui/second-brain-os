# 实作：查询图谱

这是实作的第二部分。[实作：抽取图谱](build-extract.md)在知识库根目录留下了两个文件：保存普通链接的 `edges.csv`，以及保存带类型抽取结果的 `typed_edges.csv`。本篇用四十多行 Python，将它们变成答案。

存储层是在内存中运行的 NetworkX，每次调用都重新从 CSV 加载——这是[图谱存储](graph-stores.md)阶梯中的第二级。没有服务器，无需模式迁移，而且在个人知识库的规模下，完整加载只需几毫秒。只需一个依赖：

```
pip install networkx
```

写作时 NetworkX 的版本是 3.7；3.x 系列的任意版本都可以。

<a id="the-script"></a>

## 脚本

将以下内容保存为知识库中的 `scripts/graph_query.py`：

```python
#!/usr/bin/env python3
"""Query the vault graph. Reads edges.csv and typed_edges.csv from the
current directory.

Usage:
    python graph_query.py neighbors "Page"
    python graph_query.py path "Page A" "Page B"
    python graph_query.py communities
    python graph_query.py connects "Page A" "Page B"
"""
import csv
import os
import sys

import networkx as nx

FILES = ["edges.csv", "typed_edges.csv"]


def load():
    g = nx.DiGraph()
    for name in FILES:
        if not os.path.exists(name):
            continue
        with open(name, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                g.add_edge(row["source"], row["target"],
                           type=row.get("type", "links-to"))
    return g


def neighbors(g, node):
    out = [f"-> {t} ({g.edges[node, t]['type']})" for t in sorted(g.successors(node))]
    out += [f"<- {s} ({g.edges[s, node]['type']})" for s in sorted(g.predecessors(node))]
    return "\n".join(out) or "No links."


def path(g, a, b):
    try:
        return nx.shortest_path(g.to_undirected(as_view=True), a, b)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return None


def communities(g):
    found = nx.community.label_propagation_communities(g.to_undirected())
    groups = sorted((sorted(c) for c in found), key=len, reverse=True)
    return "\n".join(f"[{len(c)}] " + ", ".join(c) for c in groups)


def connects(g, a, b):
    p = path(g, a, b)
    if p is None:
        return f"Nothing connects {a} and {b}."
    hops = []
    for s, t in zip(p, p[1:]):
        d = g.get_edge_data(s, t)
        hop = f"{s} -[{d['type']}]-> {t}" if d else f"{s} <-[{g.edges[t, s]['type']}]- {t}"
        hops.append(hop)
    return "\n".join(hops)


if __name__ == "__main__":
    g = load()
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "neighbors":
        print(neighbors(g, args[0]))
    elif cmd == "path":
        print(" -> ".join(path(g, args[0], args[1]) or ["No path."]))
    elif cmd == "communities":
        print(communities(g))
    elif cmd == "connects":
        print(connects(g, args[0], args[1]))
    else:
        print(__doc__)
```

简要说明几个设计点。先加载普通边，再加载带类型的边，意味着同一对节点之间，带类型的边会覆盖 `links-to`——这是有意的，因为类型边更准确地描述了同一个链接。路径查询在无向视图上运行，因为“它们如何关联”并不在意究竟是哪个页面链接到哪个页面。标签传播则代替 [GraphRAG](graphrag.md) 中的 Leiden 步骤：虽然粗糙一些，但只需标准库加 NetworkX，而且在这个规模下几乎瞬间完成。

<a id="what-each-command-answers"></a>

## 每个命令回答什么

```
$ python scripts/graph_query.py neighbors "RAG"
-> GraphRAG (links-to)
-> LlamaIndex (uses)
<- GraphRAG (extends)
<- Lost in the Middle (links-to)

$ python scripts/graph_query.py communities
[4] GraphRAG, Long context replaces RAG, Lost in the Middle, RAG
[2] Jerry Liu, LlamaIndex
```

`neighbors` 展示一个页面的一跳邻居，包括两个方向，并标明关系。`communities` 展示主题层：每行一个聚类，最大的排在最前面。

<a id="what-connects-x-and-y"></a>

## X 与 Y 之间有什么连接

这正是本次实作存在的理由。`connects` 返回两个页面之间最短的链，每一跳都标有类型：

```
$ python scripts/graph_query.py connects "Jerry Liu" "Lost in the Middle"
Jerry Liu -[built]-> LlamaIndex
LlamaIndex <-[uses]- RAG
RAG <-[links-to]- Lost in the Middle
```

这是通过计算得到、而非猜测出来的多跳连接——正是[为什么需要图谱](why-graphs.md)中所说向量检索无法很好回答的问题。它同时也是一个普通函数，接收两个字符串、返回一个字符串，恰好符合智能体工具所需要的形式。接入方式见[实作：将图谱接入循环](build-use.md)。
