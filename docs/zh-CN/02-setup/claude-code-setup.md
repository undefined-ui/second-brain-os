# 在知识库中使用 Claude Code

Claude Code 是系统中负责读写的那一半。运行它有两种方式，区别只在于你在哪里输入，不影响执行结果。

<a id="option-a-the-desktop-app"></a>

## 方案 A：桌面应用

从 [claude.com/download](https://claude.com/download) 下载 Claude Desktop 并登录。应用中的 **Code** 标签页提供无需终端的 Claude Code。如果你从未使用过命令行，可以从这里开始。

<a id="option-b-the-terminal"></a>

## 方案 B：终端

安装 Claude Code，然后在知识库文件夹中运行 `claude`：

```bash
cd ~/brain
claude
```

以这种方式启动时，智能体通过文件系统直接读写知识库，不涉及任何插件或 MCP 服务器。这是最简单的配置，足以完成本指南资料导入、组织结构和检索章节中的全部工作。

各平台的安装方法见[官方安装文档](https://code.claude.com/docs/en/setup)。

<a id="option-c-inside-obsidian"></a>

## 方案 C：在 Obsidian 中运行

社区插件现在可以将智能体嵌入编辑器，而且使用量很大：[Claudian](https://github.com/yishentu/claudian) 的安装量已超过两百万，[Copilot](https://github.com/logancyang/obsidian-copilot) 紧随其后。两者都能在笔记旁边的面板中运行 Claude Code、Codex 或本地智能体。

值得了解它们，因为这样可以完全省去切换窗口的操作。也值得谨慎使用，原因与本指南建议定时导入相同：编辑器里的智能体容易诱发临时修改，而这些修改可能从未记录到 `log.md` 中。没有日志的知识库无法审计。

合理的分工是：用插件进行对话和起草，用终端或定时任务执行任何写入 wiki 页面的工作。

<a id="plan-requirement"></a>

## 订阅要求

Claude Code 需要付费账户：Pro、Max、Team、Enterprise，或按 token 计费的 Console 账户。根据 Anthropic 自己的安装文档，免费的 Claude.ai 方案不包含 Claude Code 访问权限。如果 Code 标签页提示升级，原因就在这里。

<a id="filesystem-or-mcp"></a>

## 文件系统还是 MCP

两者都能用。它们的差异很具体，选择前值得了解：

| | 文件系统 | MCP |
|---|---|---|
| 配置 | 无需配置，只需 `cd` 到知识库目录 | 插件加一条配置命令 |
| 是否需要打开 Obsidian | 不需要 | 需要，由插件提供 API |
| 访问范围 | 启动时所在的文件夹 | 从任何位置访问整个知识库 |
| 失败方式 | 基本没有额外故障点 | 插件关闭、应用关闭、端口错误 |

先使用文件系统。当你希望智能体从知识库目录之外启动的会话中访问它时，再迁移到 [MCP](mcp-obsidian.md)；这通常在引入定时任务后才重要。

<a id="first-run"></a>

## 第一次运行

提出其他要求之前，先让它了解结构：

```
Read CLAUDE.md and wiki/index.md, then tell me what this vault currently
contains and what is missing.
```

答案会立即表明智能体是否理解了指令。如果它开始编造你没要求的结构，说明 `CLAUDE.md` 太模糊。请参阅[编写你的 CLAUDE.md](claude-md.md)。

<a id="permissions"></a>

## 权限

智能体会在编辑文件之前询问。只授予它知识库的写入权限，不要扩展到其他位置。如果文件夹中存放着任何不能丢失的内容，不要授予不受限制的 shell 权限。在安排定时自动化之前，请阅读[防护措施](../06-agents/safety-and-guardrails.md)。

<a id="next"></a>

## 下一篇

[Obsidian 的 MCP 连接](mcp-obsidian.md)
