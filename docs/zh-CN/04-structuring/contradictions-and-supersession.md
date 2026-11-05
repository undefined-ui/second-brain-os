# 矛盾与替代关系

这条规则是第二大脑与搜索引擎的分界线，也是大多数实现都会弄错的一条规则。

当新来源与页面中已有的内容不一致时，页面应同时记录两者，而不是覆盖旧内容。

<a id="why-overwriting-is-the-worst-failure-mode"></a>

## 为什么覆盖是最糟糕的失败方式

一个悄悄更新为最新主张的知识库，不会记得你曾经相信什么、为什么相信。它总把你最近读到的内容当作事实，这相当于按时间新旧排序，而不是按证据排序。

更糟的是，这种变化看不见。没有任何报错。页面只是用同样肯定的语气，说出了与上个月不同的内容，而你无从察觉，也无法核查变化。

历史本身就是资产。知道你曾因为一份 2024 年的来源相信 X，后来又在更好的证据出现后改信 Y，比单独保留任何一个主张都更有价值，因为这段历史能说明 Y 到底有多可靠。

<a id="what-a-contradiction-looks-like-on-a-page"></a>

## 页面上如何呈现矛盾

同时列出两种立场，各自注明来源与日期：

```markdown
## Current position

Retrieval quality degrades past roughly 50k tokens of context
([[Lost in the Middle]], 2023).

## Contested

[[Some 2026 benchmark]] reports no degradation up to 200k on the same task
family. The two use different evaluation setups: the first measures position
sensitivity, the second end-task accuracy. Unresolved.
```

读者可以据此采取行动。如果页面只是悄悄采纳最后导入的那个说法，它就无法为行动提供可靠依据。

<a id="supersession"></a>

## 替代关系

有时并不是真正的分歧，而是旧信息过时了。比如工具更改了 API、公司被收购，或者论文被撤稿。

将旧主张标记为已被替代，并保留下来：

```markdown
~~Requires Node 18 or later~~ superseded 2026-05: the native installer no
longer requires Node ([[source]]).
```

如果删除它，你以后读到变更之前写下的内容时，就无法解释它为什么与知识库当前的说法不同。

<a id="confidence"></a>

## 可信程度

并非所有导入的内容都应具有相同权重。一个标签或 frontmatter 字段就足够了：

- **直接陈述**：由你信任的一手来源提出
- **转述报道**：来自二手报道
- **自行报告**：由会从该说法中受益的一方提出
- **未经验证**

尤其是自行报告的数据，绝不能丢掉这个标签。把公司自己的性能声明当作事实写进概念页面，正是让知识库变得自信却错误的方式。

<a id="the-instruction"></a>

## 指令

将下面的规则写入 `CLAUDE.md`，用能适用于普遍情况的表述，而不只覆盖显而易见的特例：

```
When a new source disagrees with an existing page, do not overwrite. Record both
positions with sources and dates, and say what would settle it. If the new
source is clearly better evidence, mark the older claim superseded rather than
deleting it. Never resolve a contradiction by picking the more recent source.
```

<a id="next"></a>

## 下一步

[index.md 与 log.md](index-and-log.md)
