# 实践：目标测试

三个实践页面将围绕一个无界面的编程智能体，组装出可运行的循环。这一页提供骨架：用脚本定义完成、运行智能体、运行目标测试、反馈失败、限制尝试次数。示例使用 Claude Code 的非交互模式（`claude -p`），也就是[运行框架手册](../track-harness/claude-code-as-harness.md)中的参考实现，不过任何接收提示词并编辑文件的 CLI 智能体都可以替换进去。

你需要让 `claude` 和 `jq` 位于可执行路径中，并准备一个带测试套件的仓库。以下标志截至 2026 年 9 月有效：`-p` 运行一次非交互会话；`--allowedTools` 使用权限规则语法预先批准工具（末尾的 ` *` 表示前缀匹配）；`--permission-mode acceptEdits` 允许它无需询问便写入文件；`--output-format json` 返回结果及元数据，其中包括 `total_cost_usd`。

<a id="done-as-a-script"></a>

## 用脚本定义完成

目标测试就是整个设计的核心。它必须可执行、结果二元明确，并且不受智能体控制——这里使用测试加静态检查：

```bash
#!/usr/bin/env bash
# goal-loop.sh — run a coding agent until the goal test passes or attempts run out.
set -u

TASK="Make every test under tests/ pass. Do not delete, skip or weaken any test."
MAX_ATTEMPTS=5

goal_test() {
    python -m pytest -q --tb=short && ruff check .
}

feedback=""
attempt=1
while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
    echo "=== attempt $attempt of $MAX_ATTEMPTS ==="

    prompt="$TASK"
    if [ -n "$feedback" ]; then
        prompt="$TASK

The previous attempt failed the goal test with this output:
$feedback

Fix these specific failures."
    fi

    claude -p "$prompt" \
        --allowedTools "Read,Edit,Bash(python -m pytest *),Bash(ruff *)" \
        --permission-mode acceptEdits \
        --output-format json | jq -r '.total_cost_usd as $c | "agent done (cost $\($c))"'

    if feedback=$(goal_test 2>&1); then
        echo "PASS: goal test green on attempt $attempt"
        exit 0
    fi
    echo "FAIL: goal test still red"
    attempt=$((attempt + 1))
done

echo "STOP: $MAX_ATTEMPTS attempts spent; handing back to the human"
exit 1
```

保存它，执行 `chmod +x goal-loop.sh`，在存在失败测试的仓库中运行，然后观察它收敛或停止。

<a id="why-each-piece-is-there"></a>

## 为什么需要每个部分

**目标测试运行在外层封装中，而不是智能体中。** 智能体工作时也会运行 pytest——这没问题，它就是这样找到方向的。但结束循环的判定来自你的 shell，运行在模型无法触碰的进程中。这是[评审器与验证](critics-and-verification.md)中“检查，绝不只是询问”规则的最小实现。

**只有失败输出会传递下去。** 每次尝试都是全新的 `claude -p` 会话：干净的上下文、任务，以及对尚存问题提炼出的证据。上一次尝试中充满困惑的对话记录不会随行——这就是[上下文清理](context-hygiene.md)所主张的每次尝试使用全新上下文。

**次数上限很小，退出码如实反映结果。** 五次尝试后，以退出码 1 退出，并给出直接说明。这让脚本可以组合使用：CI 可以据此把关，cron 可以据此告警，接下来的两个实践页面也可以继续封装它。

<a id="what-it-is-not-yet"></a>

## 目前还缺什么

这个循环接受任何检查通过的结果。即使智能体用糟糕的方式通过测试——死代码、吞掉错误、在测试覆盖之外悄悄改动——也会顺利过关。第二部分正是为此加入评判者：[实践：评审器](build-critic.md)。
