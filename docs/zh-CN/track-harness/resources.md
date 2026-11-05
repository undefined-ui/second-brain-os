# 资源

这里提供精选资源，并非穷尽所有资料。所有条目都在 2026 年 9 月检查过，且有明确的入选理由。搭配[什么是运行框架](what-a-harness-is.md)阅读，可以掌握相关术语。

<a id="foundational-posts"></a>

## 奠基文章

- [构建有效的智能体](https://www.anthropic.com/engineering/building-effective-agents)——Anthropic，2024 年 12 月。至今仍是最清晰的分类说明：工作流与智能体的区别，以及人人引用、很少有人遵循的建议——从简单方案开始。
- [面向 AI 智能体的有效上下文工程](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)——Anthropic。为[上下文工程](context-engineering.md)中讨论的领域正式命名。
- [AI 智能体的上下文工程：构建 Manus 的经验](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)——生产环境中积累的教训：KV 缓存的成本效益、只追加的上下文，以及屏蔽工具而不是移除工具。
- [为智能体编写有效工具](https://www.anthropic.com/engineering/writing-tools-for-agents)——[工具与 MCP](tools-and-mcp.md)的工具设计配套读物。

<a id="deep-guides-and-talks"></a>

## 深入指南与演讲

- [如何构建智能体](https://ampcode.com/notes/how-to-build-an-agent)——Thorsten Ball。用不到 400 行 Go 构建代码编辑智能体。在采用任何框架之前先做一遍；没有什么比这更快消除神秘感。
- [智能体的十二要素](https://github.com/humanlayer/12-factor-agents)——HumanLayer。让智能体在生产环境中可靠工作的原则：掌控提示词、掌控上下文窗口、构建小而专注的智能体。
- [我们如何构建多智能体研究系统](https://www.anthropic.com/engineering/multi-agent-research-system)——Anthropic。介绍编排者与执行者的模式，并坦诚承认多智能体会消耗约 15 倍的令牌。
- [上下文衰退](https://www.trychroma.com/research/context-rot)——Chroma。提供证据说明，模型表现会随着输入增长而下降，远早于窗口填满。
- [致命三要素](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)——Simon Willison。适用于所有读取不可信内容的智能体的安全思考框架。他持续更新的博客，也是了解智能体领域最好的长期评论来源。
- [2026-07-28 MCP 规范](https://blog.modelcontextprotocol.io/posts/2026-07-28/)——协议团队解释 MCP 转向无状态后发生了哪些变化。

- [提高令牌效率](https://cursor.com/blog/improved-token-efficiency)——Cursor。通过六项调整精简生产环境运行框架：随着模型能力提升，删除三分之二的系统提示词；按需加载工具（去掉 60% 的静态工具令牌）；显式设置缓存断点；减少行号密度；规范子智能体使用。少见地为各项调整提供了具体数据；[这个复现提示词](https://x.com/undefinedKi/status/2103219508605555033)可以将同样的审计方法应用到你自己的配置。

- [Palantir AIP 架构](https://www.palantir.com/docs/foundry/architecture-center/aip-architecture)——一个在严格受限的组织内部运行的平台所采用的智能体技术栈，其中大部分设计也能借鉴到小项目中：通过包含类型化对象和允许操作的本体提供访问，而不是直接访问原始数据；所有模型调用都经过统一网关（脱敏、缓存、重试、令牌计量）；通过配置切换模型；三种触发方式（定时、事件、API）；将评估纳入发布周期；追踪每个操作。[这篇拆解](https://x.com/undefinedKi/status/2103883647501652057)将各个部分对应到个人项目可采用的工具。

<a id="repos-worth-reading"></a>

## 值得阅读的仓库

- [pi](https://github.com/earendil-works/pi)——足够小、真正可以读完的完整运行框架；循环、工具、扩展，没有繁文缛节。
- [smolagents](https://github.com/huggingface/smolagents)——用约 1,000 行核心代码展示以代码作为行动的模式。
- [OpenHands](https://github.com/OpenHands/OpenHands)——生产规模下的沙箱运行时和事件流是什么样子。
- [Claude Code 文档](https://code.claude.com/docs/en/overview)——虽然不是仓库，却是参考运行框架的操作手册；仅[钩子参考](https://code.claude.com/docs/en/hooks)就足以上一堂生命周期设计课。

<a id="start-here"></a>

## 从这里开始

1. **构建最基础的循环。** 用你喜欢的语言完成 Thorsten Ball 的教程。只需一个下午，就会永久改变你阅读框架文档的方式。
2. **读两篇文章。** 先读《构建有效的智能体》，再读《有效上下文工程》。两篇合起来，能覆盖你将面临的 80% 的判断问题。
3. **采用一个运行框架，并加入观测能力。** 从[生态概览](harness-landscape.md)中选择一个，接入真实任务，并阅读每次失败的原始对话记录。对话记录就是课程；本手册中的一切都能在那里看到。
