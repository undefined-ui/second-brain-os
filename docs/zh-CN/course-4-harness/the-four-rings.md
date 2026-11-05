# 四层防护

从外到内构建运行框架：隔离、指南、传感器、权限。顺序很重要，因为每一层都必须能在内侧所有防护失效时仍然守住边界。指南可能被忽略，传感器可能漏检，审批可能被误点；但围墙不在乎这些。因此，在写下第一个提示词之前，就要先筑起最外层。

![](fig-four-rings.svg)

<a id="ring-one-containment"></a>

## 第一层：隔离

隔离决定智能体从物理上无法触及什么，也是唯一完全不需要模型配合就能生效的防护层。标准配置包括：使用容器或虚拟机，而非笔记本电脑上的 shell；使用可丢弃的分支或 git worktree，而非 main；使用只读数据库用户，而非应用程序的凭据；使用网络允许名单，而非开放的互联网。这些都不涉及提示词。只要在智能体第一次运行之前配置妥当，最糟糕的一次会话也不过是丢弃一个分支，再浪费一笔 API 费用。

<a id="ring-two-guides"></a>

## 第二层：指南

指南是智能体行动前阅读的一切：AGENTS.md 文件、工具描述、示例。它们成本低，却承载着日常工作质量的大部分保障。一份有用的 AGENTS.md 只需四行，无需四页：

```markdown
- Monorepo: services live in services/, shared code in packages/. Run everything from the repo root.
- `make test` must pass before you call any task done.
- Never hand-edit files in migrations/ — generate them with `make migration`.
- Your database user is read-only. Ask before proposing any schema change.
```

工具设计是这一层的另一半。Google 在 Kaggle 发布的白皮书[智能体工具与 MCP 互操作性](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp)将工具分为函数工具、内置工具和智能体工具，其最佳实践本质上都在教你写指南：每个工具的文档要清晰到让模型仅凭描述就能选中它；围绕任务而非 API 接口设计工具；返回简洁的输出；让错误信息说明修复方法。优先使用有明确类型的工具，而不是原始访问权限——`search_orders(customer_id)` 比直接交出一个 SQL 连接更好，因为数据模式本身也是隔离。白皮书支持 MCP 的理由是互操作性：采用一个开放协议（通过 stdio 或流式 HTTP 传输 JSON-RPC 2.0），N 个客户端和 M 个工具服务器就各自只需集成一次，而不是进行 N×M 次集成。完整讨论见[工具与 MCP](../track-harness/tools-and-mcp.md)。

<a id="ring-three-sensors"></a>

## 第三层：传感器

传感器用确定性的方式告诉你，工作是否可靠。廉价检查要用于所有改动：每次修改后运行代码检查器、类型检查器、测试套件——它们只花几秒，而且永不疲倦。昂贵检查——让另一个模型审阅差异，或请人阅读——只用在重要内容上：身份验证代码、数据库迁移，以及任何涉及资金流动的地方。自动执行 `make test` 的运行框架，比指望审阅者记得执行它的框架能发现更多问题。

<a id="ring-four-permissions"></a>

## 第四层：权限

Anthropic 报告称，[Claude Code 用户会批准 93% 的权限请求](https://www.anthropic.com/engineering/claude-code-auto-mode)。一个每一百次会放行九十三次的关卡，会训练人们不再阅读它。真正的保护来自第一层——某些操作根本不可用——因此审批提示只应留给真正不可逆的行为：推送到共享分支、发送任何内容、删除任何内容。每天三次提示，人们会阅读；每天三十次，人们只会点击。

<a id="hooks-guides-with-teeth"></a>

## 钩子：有执行力的指南

模型可能只是扫一眼的指南，可以变成运行框架强制执行的规则。在 Claude Code 中，PreToolUse 钩子在每次工具调用前运行，并能阻止调用；下面这个钩子执行“永远不要推送到 main”的规则：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' | grep -qE 'git push.*\\bmain\\b' && { echo 'Blocked: never push to main' >&2; exit 2; } || exit 0"
          }
        ]
      }
    ]
  }
}
```

退出码 2 会阻止调用，并将消息反馈给智能体，让它修正方向，而不是悄无声息地失败。

<a id="the-bets-expire"></a>

## 假设会过时

每一层的每个组件，都建立在“模型做不到某件事”的假设上。Anthropic 曾因 Claude Sonnet 4.5 接近上下文上限时会过早结束工作，而在运行框架中加入上下文重置机制；后来 Opus 4.5 不再出现这一问题，他们便[彻底删除了该机制](https://www.anthropic.com/engineering/harness-design-long-running-apps)。你的假设同样会过时。[运行框架实践](harness-practice.md)会把这件事变成每季度的固定复查。
