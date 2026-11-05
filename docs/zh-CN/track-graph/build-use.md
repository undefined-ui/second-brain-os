# 实作：将图谱接入循环

第三部分。图谱已经存在，也能回答问题；现在要让智能体无需你居中操作就能访问它。不需要 MCP 服务器，也不需要框架——工具接口就是“通过 shell 调用一个打印文本的脚本”。Claude Code 原生就能做到，而且这种接口经得起每一次框架迁移。

<a id="a-slash-command-not-a-server"></a>

## 使用斜杠命令，无需服务器

将以下内容放入知识库的 `.claude/commands/connects.md`：

```markdown
---
description: What connects two pages
---

Regenerate the edge list with `python scripts/graph_export.py . edges.csv`,
then run `python scripts/graph_query.py connects` with the two page names
from $ARGUMENTS, each in quotes. Explain the chain in one short paragraph,
naming the edge types, and say plainly if nothing connects them.
```

现在，`/connects "Jerry Liu" "Lost in the Middle"` 会给智能体一条计算得到的链，让它解释，而不是让它凭空联想关系。先重新导出很重要：智能体不断编辑页面，查询昨天的 CSV，回答的就是昨天的知识库。带类型的边老化得慢一些——每月，或在一次大批量资料导入之后，重新运行[实作：抽取图谱](build-extract.md)中的抽取过程。

更深层的变化在智能体的常驻指令中。向知识库的 `CLAUDE.md` 添加一行：

```text
Before answering any question about how two topics relate, run
scripts/graph_query.py connects with both page names and ground
the answer in the chain it returns.
```

这会让图谱从智能体“可以使用”的工具，变成它“确实会使用”的工具——就像拥有一本参考书与实际引用它之间的区别。

<a id="the-weekly-health-check"></a>

## 每周健康检查

图谱会老化，[为什么需要图谱](why-graphs.md)直言，过时的图谱比没有图谱更糟。因此，图谱也要像知识库中的其他部分一样，拥有维护循环。每周手动或定时运行以下内容：

```text
Run python scripts/graph_export.py . edges.csv, then
python scripts/graph_query.py communities. Report three things:

1. Orphans: pages under wiki/ that appear in no edge at all
   (compare filenames against the nodes in edges.csv). Propose a
   page each should be linked from, or flag it for deletion.
2. Weak clusters: communities of three pages or fewer that are not
   from this week's ingestion. Say whether each should be linked
   into a larger cluster or left to grow.
3. One bridge worth building: the two largest communities with no
   typed edge between them, and the page or link that would
   connect them.

Keep the report to ten lines. Do not change anything without asking.
```

孤立页面代表捕获环节的失败，弱小聚类代表始终没有发展起来的主题，而缺失的桥梁通常是报告里最有意思的一行——你拥有的两块知识，从未相遇过。只读规则很重要：如果健康检查悄悄重连链接，知识库就会逐渐不再属于你。

<a id="when-to-graduate"></a>

## 什么时候需要升级

CSV 加 NetworkX 这一层不再够用的信号，按通常出现的先后顺序排列：

- 查询需要历史——“三月份我相信什么”——而平铺的边没有时间戳。
- 多个智能体并发写入，CSV 的后写覆盖前写开始吞掉边。
- 节点数超过几万后，重新加载从几毫秒变成了几秒钟。

每一种情况都对应[图谱存储](graph-stores.md)阶梯上的一个台阶；迁移只需一个下午，因为边列表就是各种工具都支持导入的交换格式。在确实出现这些信号之前，留在当前方案即可：整层架构只是两个脚本、一个提示词和两个 CSV，而且每一部分，拥有它的人都能读懂。

<a id="what-you-have"></a>

## 你得到了什么

一个抽取器、一个查询工具、一个斜杠命令和一个维护循环——只花一个晚上，就在自己的笔记上构建了能运行的轻量 GraphRAG。如果接下来需求继续增长，[工具](tools.md)中介绍的框架也是同样的结构，只是规模更大。
