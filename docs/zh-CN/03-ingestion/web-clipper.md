# 网页文章

文章构成大多数人收藏内容的主体，而决定收藏的时刻发生在浏览器中。任何要求切换窗口的方式，都处于劣势。

<a id="obsidian-web-clipper"></a>

## Obsidian Web Clipper

这是 Obsidian 团队的[官方扩展](https://obsidian.md/clipper)，支持 Chrome、Firefox、Safari、Edge、Brave 和 Arc。它使用 Mozilla Readability 提取网页中适合阅读的内容——也就是 Firefox 阅读模式背后的同一引擎——并以 Markdown 直接保存到知识库。

安装后打开设置，将目标文件夹设为 `raw/`。

<a id="template"></a>

## 模板

默认模板只保存页面正文。添加 frontmatter，让智能体无需重读整个文件，就知道自己拿到的是什么：

```
---
title: {{title}}
source: {{url}}
author: {{author}}
published: {{published}}
clipped: {{date}}
type: article
---

{{content}}
```

在许多网站中，`{{author}}` 和 `{{published}}` 会返回空值。这没有问题：空字段比猜测出来的字段好。智能体应该说明来源没有日期，而不是编造一个日期。

<a id="what-to-clip"></a>

## 应该剪藏什么

剪藏那些你一年后仍想找回的内容：一手来源、工程实践文章、论文、文档，以及你不赞同、想以后回应的论点。

跳过一周后就过时的新闻、清单文章，以及出于内疚而收藏的任何东西。每个低价值页面都会产生两次成本：导入时一次，之后每当智能体为了寻找其他内容而读过它时，又付出一次。

剪藏时最诚实的判断是：你能否说出以后会针对这个来源提出什么问题？如果不能，就别剪藏。

<a id="awkward-pages"></a>

## 难处理的页面

- **付费墙。** 剪藏工具保存浏览器实际渲染的内容。你能读到，就能保存；如果读不到，保存的就是付费墙提示，所以离开页面前要检查。
- **文档网站。** 逐页剪藏得不偿失。保存入口，让智能体获取剩余内容；如果文档开源，也可以将文档仓库克隆到 `raw/`。
- **单页应用和动态内容。** Readability 有时只返回片段。导入前先查看文件。
- **讨论串和评论区。** 价值通常在回复中，而剪藏工具会丢弃它们。手动复制讨论串，或截图到 `raw/assets/`。

<a id="clip-now-ingest-later"></a>

## 先剪藏，后导入

剪藏和导入被有意设计成两个步骤。白天随时剪藏，之后再批量运行 `/ingest`。因为逐个来源导入时，智能体没有机会发现你本周收藏的三样东西，其实都在讨论同一个想法。

<a id="next"></a>

## 下一篇

[YouTube 与播客](youtube-transcripts.md)
