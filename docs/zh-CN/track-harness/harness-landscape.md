# 运行框架生态概览

这里介绍截至 2026 年 9 月仍活跃的方案，并为每个方案给出一个坦诚的评价。它们运行的都是[什么是运行框架](what-a-harness-is.md)中描述的同一个循环；差别在于围绕循环封装了多少机制，以及你会继承谁的设计取向。

<a id="the-main-options"></a>

## 主要选择

- **[Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)**（Anthropic，Python/TS）。将 Claude Code 的循环封装成库，内含权限、钩子、子智能体、技能和压缩。这是你能整体采用的最完整的运行框架——代价是接受 Anthropic 的设计取向，而且在其中表现最佳的是 Anthropic 自家的模型。详见[作为运行框架的 Claude Code](claude-code-as-harness.md)。

- **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)**（Python，TS 版本进度较慢）。轻量，提供智能体、任务交接、防护措施和会话。2026 年 4 月的更新加入了原生沙箱，以及为 GPT-5 级别模型调优的“模型原生运行框架”。它属于更广泛的 [AgentKit](https://openai.com/index/introducing-agentkit/) 套件——注意，拖放式 Agent Builder 将于 2026 年 11 月退役，因此应押注 SDK，而不是画布。

- **[LangGraph](https://www.langchain.com/langgraph)**（LangChain，Python/JS）。将智能体表示为显式状态图，2025 年末发布 1.0，提供持久执行和人工参与的中断机制。它经过了真实生产环境验证，也确实很重。需要可审计的控制流时再选它，而不是因为它名气大。

- **[Vercel AI SDK 6](https://ai-sdk.dev)**（TypeScript）。从流式工具包演进为真正的运行框架：`ToolLoopAgent`、工具审批、完整 MCP 支持。如果智能体位于 Web 产品内部，它是合理的默认选择。发布说明：[AI SDK 6](https://vercel.com/blog/ai-sdk-6)。

- **[smolagents](https://github.com/huggingface/smolagents)**（Hugging Face，Python）。核心约 1,000 行；智能体通过编写 Python 代码来行动，而不是发出 JSON 工具调用。它是最快获得可运行循环的途径，也是最适合学习的代码库。出于设计选择，对生产环境需求的覆盖较少。

- **[OpenHands](https://github.com/OpenHands/OpenHands)**（原名 OpenDevin；组织从 All-Hands-AI 迁移至 OpenHands）。开源自主软件工程平台：沙箱运行时、浏览器，以及位于 [openhands.dev](https://www.openhands.dev/) 的云平台。它展示了完整沙箱化的编程运行框架应有的样子；自行托管比使用 CLI 更复杂。

- **[pi](https://github.com/earendil-works/pi)**（Mario Zechner，原 badlogic/pi-mono，现隶属 Earendil；文档见 [pi.dev](https://pi.dev)）。刻意保持极简的终端运行框架，通过 TypeScript 扩展，而非不断堆叠配置。Databricks 的基准测试发现，它在通过率上胜过更重的框架，而每轮发送的上下文约为对方的三分之一——这是将极简主义用于[上下文工程](context-engineering.md)，也证明运行框架会影响成绩。

- **[Pydantic AI](https://ai.pydantic.dev)**（Python）。由验证工具团队打造的类型安全智能体。平实而可靠；如果工作的全部重点就是结构化输出，这是很好的选择。

<a id="how-to-choose"></a>

## 如何选择

基于 Claude 构建：Agent SDK。TypeScript Web 产品：Vercel AI SDK。需要显式工作流控制：LangGraph。学习：smolagents，然后读 pi 的源码。自主编程基础设施：OpenHands。大多数团队需要的是一个运行框架，以及为它提供良好输入的纪律，而不是把所有框架都逛一遍。
