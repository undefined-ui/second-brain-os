# 运行框架实践

理论讲完了，现在来加固一个真实智能体。示例是通过 Claude Code 运行、为使用 Postgres 数据库的 Web 应用工作的编程智能体，但每一步都适用于任何运行框架——包括[构建循环](../track-harness/build-the-loop.md)中的七十行循环。按顺序逐层推进。

> 本次练习中的审查部分已经封装为一项技能：安装[课程插件](../../../plugins/README.md)，在动手加固之前运行 `/agents-course:harness-audit`。

开始前先明确范围：本次练习是加固你已经在运行的智能体。从零构建整套机制——七十行循环及其防护措施——属于[运行框架手册的实作](../track-harness/build-the-loop.md)。

<a id="step-one-build-the-walls"></a>

## 第一步：筑起围墙

在输入第一个提示词前，确定智能体无法访问哪些东西。给它一个 worktree，而非你的工作副本；再给它一个只读的数据库用户：

```bash
git worktree add ../agent-workspace -b agent/task-one
```

```sql
CREATE USER agent_ro WITH PASSWORD 'rotate-me';
GRANT CONNECT ON DATABASE app TO agent_ro;
GRANT USAGE ON SCHEMA public TO agent_ro;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO agent_ro;
```

如果智能体需要安装软件包或调用 API，让它在带有网络允许名单的容器中运行（只允许软件包注册表和模型 API，不允许其他地址）。检验这一步的方法是：设想一次可能出现的最糟糕会话，检查影响范围是否仅仅是删除一个 worktree。

<a id="step-two-write-the-guides"></a>

## 第二步：编写指南

在仓库根目录放一个 AGENTS.md，简短到每次会话都能阅读：

```markdown
- App code in src/, tests in tests/, run everything from the repo root.
- `make check` must pass before you call any task done.
- Never hand-edit files in migrations/ — generate them with `make migration`.
- Your database user is read-only. Ask before proposing any schema change.
```

每一行都陈述一条智能体能够付诸行动的规则。不要哲学讨论，也不要历史沿革。

<a id="step-three-wire-the-sensors"></a>

## 第三步：接上传感器

将确定性检查整合为一个命令，再让运行框架在每次修改后执行，而不是指望模型记得：

```make
check:
	ruff check .
	mypy src
	pytest -q
```

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "make check" }
        ]
      }
    ]
  }
}
```

失败结果会立刻进入会话记录，此时距犯错才刚过去一次编辑。

<a id="step-four-strip-the-permissions"></a>

## 第四步：收紧权限

先落实最小权限，再只为不可逆操作设置审批：

```json
{
  "permissions": {
    "allow": ["Read", "Grep", "Glob", "Bash(make check)", "Bash(git diff:*)", "Bash(git status)"],
    "ask": ["Bash(git commit:*)", "Bash(git push:*)"],
    "deny": ["WebFetch", "Bash(rm:*)"]
  }
}
```

人们几乎会批准所有看到的提示，因此只有简短的待审批列表才会被认真阅读。如果你发现自己每天都不假思索地批准某件事，就把它改为允许——或者更好，让该操作根本无法发生，直接移除提示。

<a id="step-five-add-one-hook"></a>

## 第五步：添加一个钩子

从 AGENTS.md 中选出违反后代价最高的一条规则，强制执行它：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | grep -q 'migrations/' && { echo 'Blocked: generate migrations with make migration' >&2; exit 2; } || exit 0"
          }
        ]
      }
    ]
  }
}
```

一个选得好的钩子，胜过十个不停触发的钩子。

<a id="the-quarterly-review"></a>

## 每季度复查

运行框架的每个部分，都建立在模型做不到某件事的假设上，而这些假设会过时——Anthropic 在一次模型升级后，删除了整套辅助组件（用于解决过早结束工作的上下文重置机制），因为它已经成了累赘。因此，请在日历中安排定期复查。针对每个钩子、每条指南和每项禁止权限，写下“它存在是因为模型无法完成 X”，然后用当前模型测试 X。删除不再值得保留的部分；一个只增不减的运行框架，是在弥补一个早已不存在的模型的缺陷。

<a id="tips"></a>

## 实用建议

- 只有在智能体将同一件事做错两次后，才向 AGENTS.md 添加规则。凭猜想制定的规则容易失效。
- 记录钩子阻止操作的触发情况。从不触发的钩子，是复查时可以考虑删除的候选项。
- 工具描述也是指南——添加工具前，先阅读[工具与 MCP](../track-harness/tools-and-mcp.md)。

<a id="prove-it-to-yourself"></a>

## 亲自验证

1. 分别在有 AGENTS.md 和没有 AGENTS.md 的情况下运行同一任务，每次使用全新会话。比较会话记录。
2. 统计一个工作日内收到多少权限提示、批准了多少。计算你自己的批准率。
3. 禁用一个运行框架组件，重新运行它原本要保护的任务，看看实际表现是否退化。

下一篇：传感器值得单独讲一个模块——[两类检查](../course-5-evals/two-kinds-of-checks.md)。

深入阅读 → [智能体运行框架手册](../track-harness/what-a-harness-is.md)：深入介绍内部机制、工具生态，并用约 150 行代码构建可运行的框架。
