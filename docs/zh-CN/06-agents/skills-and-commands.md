# 技能与斜杠命令

这两种机制看起来相似，承担的工作却不同。

**技能**教会智能体可重复执行的行为。无论你明确调用它，还是只描述了任务，它都会在相关时加载，并影响智能体的执行方式。

**命令**是常用任务的快捷方式。它指向一个技能，让你不必重复输入指令。

行为应该定义在技能中。这样，无论导入由 `/ingest`、定时任务，还是你说的一句“把这个加入我的知识库”触发，执行方式都一致。

<a id="what-this-repo-ships"></a>

## 本仓库提供什么

[`skills/`](../../../skills/README.md) 中有十八个技能，对应本指南中的各项工作流。[`commands/`](../../../commands/README.md) 中有七十二条命令，每条只用几行内容指向某个技能并限定范围。

这种比例是有意设计的。行为应集中在少量精心编写的技能中；命令创建成本很低，所以没必要让你记住每周都会提出的请求应该如何措辞。

将它们安装到知识库中的 `.claude/skills/` 和 `.claude/commands/`，这样它们就能和笔记一起纳入版本管理，并随知识库迁移。

<a id="writing-your-own"></a>

## 编写自己的技能

值得编写的技能有三个特征：你会反复做这件事，对具体做法有自己的要求，而且这些要求并不明显到模型能够自行猜出。

一种有效的结构是：

```markdown
---
name: skill-name
description: >-
  What it does. When to use it, written pushy, because agents under-trigger
  skills. Do NOT use for the tempting near-misses.
---

# Name

[Why this skill exists: what failure it prevents. This paragraph is the rubric
for every case the rules below do not cover.]

## Core rule
## Workflow
## Output format
## Calibration
## Example
```

开头的段落比具体规则发挥的作用更大。规则覆盖你想到的情况，原因则覆盖其他情况。

<a id="explain-the-why"></a>

## 解释原因

“绝不覆盖矛盾”会被按字面执行，却在边界情况中失效。“绝不覆盖矛盾，因为你曾经相信什么的历史，正是这个知识库拥有而搜索引擎没有的东西”，则可以推广到你从未描述过的情况。

没有原因、只有全大写 NEVER 的指令，通常意味着少了一段解释。

<a id="versioning"></a>

## 版本管理

技能放在知识库中，因此由 git 跟踪。输出质量发生变化时，首先应查看技能的差异。

让定时任务使用某个技能之前，先用三到四个真实案例测试它。一个每晚运行的技能如果存在缺陷，到年底就会在三百个页面上留下同样的缺陷。

<a id="next"></a>

## 下一步

[安全护栏](safety-and-guardrails.md)
