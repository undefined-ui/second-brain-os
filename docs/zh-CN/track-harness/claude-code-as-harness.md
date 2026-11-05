# 作为运行框架的 Claude Code

Claude Code 是最值得研究的运行框架，因为 Anthropic 将同一套机制以两种形式交付：终端产品，以及 [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)——一个 Python 和 TypeScript 库，让你自己的智能体也能使用完全相同的循环、权限系统和上下文管理。请先阅读[组成结构一章](what-a-harness-is.md)；这一页会将各个组成部分对应到具体功能。

<a id="claudemd-and-memory"></a>

## CLAUDE.md 与记忆

`CLAUDE.md` 是会话开始时读取的普通 Markdown 文件，用来保存项目约定、构建命令和内部规则。它按层级组合：用户级、项目级、目录级。自动记忆文件则将这些能力延伸到多个会话。这里的经验是：持久指令应该放在智能体读取的文件里，而不是放在每次都要重新输入的提示词里。[上下文工程](context-engineering.md)会解释，为什么这优于把所有内容塞进一个提示词。

<a id="hooks"></a>

## 钩子

[钩子](https://code.claude.com/docs/en/hooks)是绑定到生命周期事件的 shell 命令，包括 `PreToolUse`、`PostToolUse`、`SessionStart`、`PreCompact`，以及截至 2026 年新增的其他数十个事件。它们是确定性执行的约束，而非建议：`PreToolUse` 钩子可以每一次都阻止危险命令，而提示词指令只能降低危险发生的概率。经验法则是：用提示词做判断，用钩子执行策略。

<a id="subagents"></a>

## 子智能体

子智能体在各自的上下文窗口中运行，拥有独立的系统提示词和工具限制。父智能体只看到最终报告，看不到中间过程的噪声——这样既能保持编排对话记录清晰，又能有效增加可用上下文。子智能体可以通过 `.claude/agents/` 中的 Markdown 文件定义，也可以通过 SDK 以编程方式定义。

<a id="skills"></a>

## 技能

技能是一个文件夹，其中包含 `SKILL.md`，以及可选的脚本和模板。只有一行描述会常驻上下文；正文在相关时才加载。这是面向指令的按需检索模式，能避免能力丰富的智能体被自己的操作手册淹没。文档：[智能体技能](https://code.claude.com/docs/en/agent-sdk/skills)。

<a id="mcp"></a>

## MCP

Claude Code 是一个 MCP 客户端：外部服务器提供的工具与内置工具并列，可按项目或按用户配置。它功能强大，也是主要的注入攻击入口——[工具与 MCP](tools-and-mcp.md)会完整讨论这个问题。

<a id="permissions"></a>

## 权限

每次工具调用都要经过权限层：`settings.json` 中的允许列表、逐次调用提示、`plan` 模式（只读），以及沙箱执行。设计假设是模型偶尔会做出不明智的事情，因此刹车掌握在运行框架手里，而不是模型手里。

<a id="headless-and-sdk-use"></a>

## 无界面运行与 SDK 使用

`claude -p "prompt"` 可以在脚本和 CI 中执行单次任务，并输出 JSON。Agent SDK 更进一步：简单调用用 `query()`，钩子和流式处理用客户端类，还能通过编程方式配置子智能体和 MCP 服务器。你不是在用脚本操控 CLI，而是把运行框架嵌入自己的应用。

<a id="the-honest-take"></a>

## 坦诚的评价

它是 2026 年最完整的开箱即用运行框架，也是其他产品用来界定自身定位的一套参照词汇——见[生态概览](harness-landscape.md)。代价是你要接受 Anthropic 的设计取向和令牌消耗。对大多数开发者来说，这个取舍值得。
