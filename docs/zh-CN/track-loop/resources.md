# 资源

先说明一个背景：“循环工程”一词于 2026 年 6 月出现，撰写这一页时才三个月。背后的实践比名称更稳固——到 7 月中旬，Steinberger 自己已经在问，讨论是否已从循环转向图。阅读时关注机制，对术语保持灵活。

<a id="the-naming"></a>

## 命名的起点

- [Peter Steinberger 的帖子](https://x.com/steipete/status/2063697162748260627)——2026 年 6 月引起广泛传播的那句话：“你不应该再亲自给编程智能体写提示词。你应该设计循环，让循环给智能体写提示词。”
- [循环工程](https://www.oreilly.com/radar/loop-engineering/)——Addy Osmani 的文章，由 O'Reilly Radar 转载。梳理自动化、工作树、技能、连接器、子智能体和外部状态，并在结尾坦诚提醒验证负担和理解债务。
- [AI 时代的代码审查](https://addyosmani.com/blog/code-review-ai/)——Osmani 的配套文章；“你的工作是交付你已确认能正常运行的代码”，这句原文仅九个词的话概括了本手册。
- [什么是循环工程？](https://www.ibm.com/think/topics/loop-engineering)——IBM 的主题页；作为冷静的机构性定义很有用，尤其着重讨论风险：理解债务、意图债务和认知上的放弃。

<a id="papers"></a>

## 论文

- [别再手把手带着你的编程智能体](https://arxiv.org/pdf/2607.00038)——Sandeco Macedo。学术层面的论述：把终止条件、验证和评审器组件视为循环的一等基础设施。
- [更少的上下文，更好的智能体](https://arxiv.org/pdf/2606.10209)——面向长期使用工具的智能体的高效上下文工程；为[上下文清理](context-hygiene.md)主张的裁剪提供测量证据。

<a id="anthropic-material"></a>

## Anthropic 资料

- [在 Claude 开发者平台上管理上下文](https://claude.com/blog/context-management)——上下文编辑和记忆工具，以及本手册引用的数据：在 100 轮评估中减少 84% 的令牌；单独使用编辑提升 29%，结合记忆工具提升 39%。
- 运行框架手册的[资源页](../track-harness/resources.md)收录了其他 Anthropic 经典资料，包括构建有效的智能体、有效上下文工程等；本手册以这些内容为基础，不再重复。

<a id="practice"></a>

## 实践

- [作为“软件工程师”的 Ralph Wiggum](https://ghuntley.com/ralph/)——Geoffrey Huntley。开启这一切的 bash 循环，以及少见地坦诚的失败记录。
- [设计智能体循环](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/)——Simon Willison，2025 年 9 月。哪些任务适合循环，以及允许循环运行时应采取的安全措施。

<a id="repos-worth-reading"></a>

## 值得阅读的仓库

- [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)——让智能体在生产环境中可靠工作的原则；其中几项要素就是换了名字的循环纪律。
- [anthropics/claude-code](https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md)——`ralph-wiggum` 插件：以持续维护、可供检查的代码实现放进循环运行的模式。
- [vercel-labs/ralph-loop-agent](https://github.com/vercel-labs/ralph-loop-agent)——在 AI SDK 上重建同一模式，明确呈现验证和迭代。

<a id="start-here"></a>

## 从这里开始

1. **编写一个目标测试。** 选择一个你一直手动写提示词的任务，用返回退出码 0 的脚本表达完成条件。如果做不到，按照[什么是循环工程](what-loop-engineering-is.md)的说法，它还不适合交给循环。
2. **构建重试循环。** 在一个存在失败测试的小仓库中完成[实践：目标测试](build-goal-test.md)。一个晚上即可。
3. **加入评判者，再加入防线。** 先加入评审轮次，再加入棘轮和报告——只有循环每次都能清楚说明停止原因后，才让它在你睡觉时运行。
