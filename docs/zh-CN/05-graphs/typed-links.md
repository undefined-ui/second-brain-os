# 带类型的链接

一个普通的 `[[wikilink]]` 只说明两个页面相关，却不说明如何相关；规模一大，这就成了实实在在的损失。

你无法向一个没有类型的图谱询问：什么与某个主张矛盾，什么证据支持它，或者哪些页面扩展了某种方法。所有边都一样，于是所有问题最后都退化成“附近有什么”。

<a id="a-minimal-vocabulary"></a>

## 一套最小词表

规模小到容易记住，表达力又足够值得使用：

- **supports** —— 本页面为另一个页面提供证据
- **contradicts** —— 本页面提出反对意见
- **extends** —— 在其基础上继续发展或补充
- **part-of** —— 属于更大事物的一个组成部分
- **applies** —— 在实践中应用某种方法

只选五种是有意的。每增加一种类型，智能体就必须在每次建立链接时多做一次正确区分；二十种类型的词表会造成标注不一致，而这比没有类型更糟。

<a id="two-ways-to-encode-it"></a>

## 两种编码方式

**内联，紧邻链接：**

```markdown
The position sensitivity result (supports:: [[Lost in the Middle]]) suggests
context length alone does not fix retrieval.
```

Dataview 可以读取内联字段，因此无需额外工具，就能在 Obsidian 内查询。

**放入每个页面的 frontmatter：**

```yaml
contradicts: ["[[Long context replaces RAG]]"]
extends: ["[[Retrieval augmented generation]]"]
```

查询更简洁，但离产生该链接的原句更远。页面级关系使用 frontmatter，主张级关系使用内联字段。

<a id="what-it-buys-you"></a>

## 它带来什么

```dataview
LIST FROM "wiki/concepts"
WHERE contains(contradicts, this.file.link)
```

这表示“知识库中所有反对当前页面的内容”，而普通图谱完全无法回答这个问题。

在智能体层面，它的作用更大。导入时将新来源记录为与现有页面存在 `contradicts` 关系，就已经从结构上标出了分歧，而不是把分歧埋在只有读到页面才会发现的正文中。

<a id="do-not-type-everything"></a>

## 不要给所有链接加类型

大多数链接只是普通提及，应当保持普通形式。给每条链接都加类型，会让词表失去意义，也会使导入更慢、更容易出错。

当关系本身就是重点时，才给链接加类型，例如证据、分歧、扩展。在实践中，大约每五条链接有一条需要类型。

<a id="the-instruction"></a>

## 指令

```
When a source supports, contradicts or extends a claim on an existing page,
record the relationship with a typed link. Plain wikilinks for ordinary
mentions. Do not type a relationship you are inferring; only type what the
source states.
```

最后一句很重要。让智能体猜测关系，会生成一张看起来严谨、实则编码了自身假设的图谱。

<a id="next"></a>

## 下一步

[图谱与嵌入向量](graph-vs-vectors.md)
