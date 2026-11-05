# 实作：抽取图谱

用一个晚上的时间完成三部分实作：在智能体已经维护的知识库之上，添加可查询的图谱层。本篇从一个 Markdown 文件夹出发，生成两个边文件；[实作：查询图谱](build-query.md)将它们加载到 NetworkX；[实作：将图谱接入循环](build-use.md)则把查询能力交给智能体。

前提来自[为什么需要图谱](why-graphs.md)：拥有经过整理的链接的 wiki，本身就是知识图谱。它缺少的是类型——每条边都说“相关”，却没有说明怎样相关。因此，计划是先机械式导出普通链接图，再让 Claude Code 遍历页面，做一轮带类型的抽取。

<a id="the-link-graph-in-one-command"></a>

## 一个命令导出链接图

仓库自带 `scripts/graph_export.py`，只依赖标准库。在知识库根目录运行：

```
python scripts/graph_export.py . edges.csv
```

Mac 上使用 `python3`；Windows 上这个名字通常只是 Microsoft Store 的占位程序。脚本遍历隐藏文件夹、模板文件夹和脚本文件夹之外的每个页面，对照文件名以不区分大小写的方式解析 `[[wikilinks]]`，然后写出：

```csv
source,target
GraphRAG,RAG
Lost in the Middle,RAG
```

指向不存在页面的链接会被丢弃，这适合本次实作：没有终点的边是需要修复的缺口，不是可查询的关系。`--format graphml` 则会生成适合 Gephi 的版本——如何使用见[工具](tools.md)。

<a id="schema-before-extraction"></a>

## 先定数据模式，再做抽取

[用 LLM 构建图谱](building-graphs-with-llms.md)提出，应先决定本体；即使是知识库规模，这也适用。对于页面由人物、工具、论文和主张组成的语料库，六种边类型就足够了。类型越多，每条链接选错的机会也越多，因此，在第六种类型尚未证明价值之前，不要急着添加第七种。

<a id="the-extraction-prompt"></a>

## 抽取提示词

在知识库根目录的 Claude Code 中运行：

```text
Read every markdown page under wiki/, skipping templates and raw.
Build a typed edge list on top of the plain wikilinks.

For each page, note its type from the frontmatter (person, tool,
claim, concept, paper, note). Then emit one row per relationship
you can ground in the text, using only these edge types:

  built        person -> tool
  authored     person -> paper or claim
  uses         page -> tool
  supports     paper or claim -> claim
  contradicts  paper or claim -> claim
  extends      page -> page

Rules:
- Source and target must both be existing page names, spelt
  exactly as the filenames are, without the .md.
- Only record what a page states. If the relationship is your
  inference rather than the page's claim, skip it.
- Append rows to typed_edges.csv with the header
  source,target,type,found_in — where found_in is the page the
  relationship was stated on.

Work in batches of twenty pages and append after each batch, so
an interruption keeps partial work. When finished, report the row
count and the five most connected nodes.
```

其中两条规则承担了大部分工作。将端点限制为现有页面名，可以让带类型的边与链接图处于同一个命名空间，从而在下一步中将两个文件加载进同一个结构。“只记录页面明确陈述的内容”则是知识库带类型链接的规则：如果让智能体推断关系，生成的图谱就会悄悄编码它自己的假设。

<a id="what-comes-out"></a>

## 生成的结果

```csv
source,target,type,found_in
Jerry Liu,LlamaIndex,built,Jerry Liu
RAG,LlamaIndex,uses,RAG
Lost in the Middle,Long context replaces RAG,contradicts,Long context replaces RAG
```

`found_in` 列表示出处——回答“图谱为什么认为这是真的”。如果想要更丰富的出处信息，可以要求输出 JSONL：每行一个对象，字段相同，再加一个 `quote` 键，保存这条边所依据的原句。下一篇会加载 CSV，因此仍应将它保留为主要输出。

<a id="read-it-before-you-trust-it"></a>

## 信任之前，先阅读

继续之前，抽取二十行，对照其来源页面检查。可能会遇到几条形式上有依据却没有用的边，偶尔也会有方向颠倒。修正提示词，而不是手工改行，然后重新运行——遍历几百个页面只需几分钟。接着在[实作：查询图谱](build-query.md)中加载结果。
