# 搜索工具

纯文本知识库中的检索，大部分靠 grep。这听起来很原始，但几乎总是够用。

<a id="ripgrep"></a>

## ripgrep

```bash
rg -i "graph rag" ~/brain --type md -l
rg -i "supersed" ~/brain -C 2
```

面对数万个文件也能瞬间完成搜索。智能体操作文件系统时默认就会使用它；对于“我在哪里提到过这件事”这一类问题，它在速度和可预测性上都胜过那些更复杂的选项。

它的局限是措辞必须匹配。它找不到你用其他说法描述的概念页面，图谱和索引就是用来补这个缺口的。

<a id="obsidian-search"></a>

## Obsidian 搜索

适合交互式使用。值得掌握的操作符包括 `path:`、`file:`、`tag:`，以及查找同一行中共同出现词语的 `line:`；后者能去掉大部分误匹配。

<a id="dataview"></a>

## Dataview

对 frontmatter 进行查询，正好可以回答结构性问题：

````
```dataview
TABLE updated, tags FROM "wiki/concepts"
WHERE contains(tags, "unverified")
SORT updated ASC
```
````

任何可以表述为“哪些页面具有属性 P”的问题，都是一个 Dataview 查询。让智能体读文件来回答这些问题，会更慢，也更不可靠。

<a id="combining-them"></a>

## 组合使用

有效的模式是：用 Dataview 或 ripgrep 得到候选集合，用图谱向外扩展，再由智能体阅读和综合。

```
Find every page tagged unverified, follow their links, and tell me which claims
depend on unverified sources.
```

先做机械筛选，再做判断。让智能体通读全部内容来筛选，会把上下文浪费在查询几毫秒就能排除的页面上。

<a id="when-search-gets-slow"></a>

## 搜索变慢时

在个人规模下，通常不会。对一万个 Markdown 文件运行 ripgrep，结果仍然是瞬间返回。如果你感觉搜索慢，原因通常是智能体读了太多文件，而不是搜索本身。

这是上下文问题，而不是搜索问题。参见[上下文预算](context-budget.md)。

<a id="next"></a>

## 下一步

[在需要时加入 RAG](rag-on-top.md)
