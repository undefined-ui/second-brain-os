# 实践：评审器

[第一部分](build-goal-test.md)在检查通过时停止。这一部分加入第二道判断：不仅通过，还要干净。独立的评审轮次会依据范围明确的标准检查差异，再把具体缺陷而不是模糊建议反馈给下一次尝试。理论见[评审器与验证](critics-and-verification.md)；这里则是额外的四十行代码。

两条设计规则支撑整个机制。评审器使用**独立会话**：一次全新的 `claude -p` 调用，只看差异和评分标准，绝不看工作对话记录，因此不会继承执行者的自我辩解。评分标准则必须**范围明确且可检查**：四条规则、强制的判定格式，以及明确禁止评论其他内容。

<a id="the-code"></a>

## 代码

```bash
#!/usr/bin/env bash
# critic-loop.sh — the goal test decides correct; a critic pass decides acceptable.
set -u

TASK="Make every test under tests/ pass. Do not delete, skip or weaken any test."
MAX_ATTEMPTS=5
BASE_REF=$(git rev-parse HEAD)

goal_test() {
    python -m pytest -q --tb=short && ruff check .
}

critic() {
    git diff "$BASE_REF" | claude -p \
"You are a code reviewer. Judge this diff against exactly four rules:
1. No test was deleted, skipped or weakened.
2. No debug prints, dead code or commented-out blocks were added.
3. Errors are handled, not silently swallowed.
4. The change stays inside the task; no drive-by refactoring.
If all four hold, reply with the single word PASS.
Otherwise list each violation as: file, the problem, the one-line fix.
Judge only these rules. Never comment on style or architecture." \
        --output-format json | jq -r '.result'
}

feedback=""
for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
    echo "=== attempt $attempt of $MAX_ATTEMPTS ==="

    prompt="$TASK"
    if [ -n "$feedback" ]; then
        prompt="$TASK

The previous attempt was rejected:
$feedback

Fix exactly these points, nothing else."
    fi

    claude -p "$prompt" \
        --allowedTools "Read,Edit,Bash(python -m pytest *),Bash(ruff *)" \
        --permission-mode acceptEdits > /dev/null

    if ! feedback=$(goal_test 2>&1); then
        echo "goal test red; retrying with failures"
        continue
    fi

    verdict=$(critic)
    case "$verdict" in
        PASS*)
            echo "green and clean on attempt $attempt"
            exit 0
            ;;
        *)
            feedback="The goal test passes, but the reviewer found defects:
$verdict"
            echo "critic rejected; retrying with defects"
            ;;
    esac
done

echo "STOP: $MAX_ATTEMPTS attempts spent; handing back to the human"
exit 1
```

<a id="how-the-pieces-fit"></a>

## 各部分如何配合

顺序很重要：先运行目标测试，再运行评审器。花钱审查根本不能工作的代码没有意义，因此确定性评审器先为 LLM 评审器筛选——先用便宜的评判者，再用贵的。差异相对于循环开始前固定的 `BASE_REF` 获取，因此评审器始终检查完整变更，而不是最后一段增量。

注意评审器的输出会变成什么：下一次尝试的 `feedback`，表述为“只修复这些问题，不做其他事”。附带位置、可以采取行动的缺陷，能直接转化为边界明确的任务。这就是评分标准禁止风格评论的原因——如果评审器说“考虑采用更函数式的方式”，下一次尝试就会跑去进行大范围重构，你的五次机会也会在反复改动中耗尽。

评审器仍会有任何 LLM 评判者共有的失效模式——宽松，以及执行者和检查者使用同一模型时的自我偏好。这里，评分标准的第一条也仅由评审器来执行；更严格的实现会直接禁止智能体写入 `tests/`。这两道防线，以及如何让整个流程无人值守运行，都是[第三部分](build-overnight.md)的内容。
