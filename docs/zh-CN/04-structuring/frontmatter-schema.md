# Frontmatter 字段规范

Frontmatter 让知识库除了文本搜索之外，还能通过其他方式查询。写这些字段几乎不费力，而 Dataview、脚本和智能体自身都会利用它们，按结构特征查找内容。

<a id="the-schema"></a>

## 字段规范

```yaml
---
title: Canonical name
type: source | entity | concept | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases: [other names this is known by]
tags: [two or three]
---
```

来源页面额外添加：

```yaml
url: https://...
author:
published: YYYY-MM-DD
```

实体页面额外添加 `kind: person | org | product | tool`。

<a id="why-each-field-earns-its-place"></a>

## 每个字段为什么值得保留

`type` 支撑着每一次结构查询和质量检查。没有它，就无法询问知识库中有多少概念，也无法找出没有关联任何概念的来源。

`updated` 使复查成为可能。陈旧的概念页面是知识库腐化的主要原因，而没有日期就无法找出它们。

当同一事物有三个名字时，`aliases` 能让 wikilink 正确解析。参见[命名与别名](naming-and-aliases.md)。

来源页面上的 `url` 是引用与无依据主张的分界线。没有它，来源页面就无法核实。

<a id="tags"></a>

## 标签

每个页面使用两到三个标签，从一份规模小、确实有人维护的受控词表中选择。

标签有一种典型的失败方式：词表不断膨胀，最后失去意义。五十个各用一次的标签比没有标签更糟，因为它们营造了分类体系的假象，却没有起到任何分类作用。

把标签列表放在 `CLAUDE.md` 中，并要求智能体使用现有标签，或明确提出新增建议，而不是悄悄发明标签。

结构方面的重任由文件夹和链接承担。标签用于表达不适合放入这两者的跨类别属性，例如 `unverified`、`to-revisit`、`disputed`。

<a id="empty-fields"></a>

## 空字段

宁可省略一个字段，也不要靠猜测填充。缺少 `published` 表示日期未知，智能体可以如实说明。而一个猜出来的日期，三周后就会在概念页面上变成事实。

<a id="keep-it-stable"></a>

## 保持稳定

给规范增加一个字段，意味着要么为所有页面补齐它，要么接受一个新旧混杂的知识库，让查询漏掉较早的一半页面。

尽早确定规范，保持精简，尽量少改。确实要修改时，一次性对整个知识库执行字段补齐，而不是让变更只适用于新页面。

<a id="next"></a>

## 下一步

[命名与别名](naming-and-aliases.md)
