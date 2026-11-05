# 人人都会遇到的问题

<a id="the-vault-stalls-after-two-weeks"></a>

## 两周后，知识库停滞了

几乎总是采集环节的问题，而不是系统本身。剪藏需要三次点击而非一次，或者手机没有资料进入知识库的路径，导致新材料不再到来，也就没有东西可处理。

修复采集路径，而不是重建知识库。参见[资料导入](../03-ingestion/README.md)。

另一个原因是过早期待回报。只有三十页时，还没有多少东西可以连接。参见[理想的效果](../01-concepts/what-good-looks-like.md)，了解真实的时间线。

<a id="pages-are-summaries-of-summaries"></a>

## 页面成了摘要的摘要

来源页面概括原文，概念页面再概括来源页面。每一层都丢失信息，最后被阅读的却是最末一层。

原因在于页面规范里出现了“概括总结”的要求。概念页面应该用平实语言、自己的话解释一个想法，而且可以独立理解。在 `CLAUDE.md` 中重写规范，重新导入几个来源来验证。

<a id="the-agent-rewrites-work-you-did-by-hand"></a>

## 智能体重写了你手写的成果

这令人恼火，但可以预防。在 frontmatter 中标记手写页面：

```yaml
maintained_by: human
```

并在 `CLAUDE.md` 中规定：绝不重写标记为 `maintained_by: human` 的页面，只能追加链接，并把问题标出来交给所有者处理。

<a id="ingest-quality-drops-as-the-vault-grows"></a>

## 知识库越大，导入质量越低

这确实会发生，原因通常在上下文。向一个已有三百页的知识库导入时，智能体应先检查已经存在什么；如果没有，就会不断新建页面，而不是更新现有页面。

检查导入流程是否先读取 `index.md` 再写入。这一步能让知识库扩大时，质量仍然稳定。

<a id="everything-connects-to-everything"></a>

## 所有内容都连到所有内容

少数枢纽页面积累了几乎所有链接，图谱因此不再表达有意义的信息。把这些枢纽拆分成人们真正想链接的具体概念。参见[链接规则](../04-structuring/linking-rules.md)。

<a id="you-stopped-opening-it"></a>

## 你不再打开它了

这是最真实的失败。通常是采集几个月前就出了问题，知识库一直没有变化，或者回顾太长，根本读不下去。

两者都能修。它们都不是换个工具重新开始的理由，尽管那往往是人的第一反应，而代价总是再花一个月。

<a id="next"></a>

## 下一步

[智能体写出的内容很糟](agent-writes-garbage.md)
