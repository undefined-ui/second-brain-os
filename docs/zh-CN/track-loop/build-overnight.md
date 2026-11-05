# 实践：通宵循环

最后的实践将实现无人值守运行。[第一、二部分](build-goal-test.md)中的规则仍然适用；改变的是没有人在旁边看着，所以防线必须让最坏情况也平淡可控：迭代次数预算、进展一停就结束运行的棘轮、Markdown 晨间报告，以及作为安全网的 git——独立分支、退步时硬重置，而且绝不推送。

棘轮是核心。每次迭代都必须超过此前最佳分数——这里指通过的测试数——否则循环就撤销这次尝试并停止。要么单调前进，要么结束；被允许原地踏步一整夜的循环，真的会这样做。理由见[停止条件](stop-conditions.md)。

<a id="the-code"></a>

## 代码

```python
#!/usr/bin/env python3
"""overnight.py — unattended agent loop: budgeted, ratcheted, reported."""
import datetime
import json
import pathlib
import re
import subprocess

TASK = ("Open TODO.md. Implement the top unchecked item, add tests for it, "
        "and tick the item off. Do not delete, skip or weaken any existing test.")
MAX_ITERATIONS = 10
RATCHET = pathlib.Path("ratchet.json")
REPORT = pathlib.Path("MORNING-REPORT.md")


def sh(cmd, timeout=2400):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True,
                          timeout=timeout)


def score():
    """Progress metric: tests passing. Higher is better; it must never fall."""
    out = sh("python -m pytest -q --tb=no").stdout
    m = re.search(r"(\d+) passed", out)
    return int(m.group(1)) if m else 0


def main():
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    sh(f"git checkout -b overnight/{stamp}")  # rail 1: own branch, never pushed
    best = score()
    RATCHET.write_text(json.dumps({"best": best}))
    lines = [f"# Overnight report {stamp}", "",
             f"Baseline: {best} tests passing.", ""]

    for i in range(1, MAX_ITERATIONS + 1):
        sh('claude -p "{}" '
           '--allowedTools "Read,Edit,Bash(python -m pytest *)" '
           '--permission-mode acceptEdits '
           '--permission-prompts none'.format(TASK))
        now = score()
        if now > best:
            best = now
            RATCHET.write_text(json.dumps({"best": best}))
            sh(f'git add -A && git commit -m "overnight {i}: {now} passing"')
            lines.append(f"- iteration {i}: improved to {now} passing, committed")
        else:
            sh("git reset --hard")            # rail 2: a bad attempt never survives
            lines.append(f"- iteration {i}: {now} passing, no improvement; stopped")
            break
    else:
        lines.append(f"- iteration budget of {MAX_ITERATIONS} spent")

    lines += ["", f"Final: {best} passing on branch overnight/{stamp}. "
                  "Nothing was pushed; review and merge by hand."]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
```

睡前运行 `python overnight.py`；喝咖啡时阅读 `MORNING-REPORT.md`。

<a id="the-rails-spelled-out"></a>

## 明确说明各道防线

**建立分支、提交、绝不推送。** 每次改进都提交到 `overnight/<stamp>`，因此早晨要做的决策，就是对普通分支进行普通代码审查。脚本中没有推送操作，智能体也完全没有 git 权限——它的 `--allowedTools` 只涵盖读取、编辑和 pytest，没有其他内容。`--permission-prompts none` 告诉运行框架没有人在场：任何需要询问的操作都会被拒绝，而不是悬挂到天亮。

**退步时重置。** 分数没有提高时，`git reset --hard` 会先丢弃这次尝试，再停止。结合棘轮，可以维持一个强不变量：分支中的每个状态都在可衡量的意义上优于上一个状态，因此你无需重新阅读所有差异，也能信任报告。

**报告就是信箱。** 无人值守循环也会犯无人值守的错误；报告会逐轮呈现这些错误，以及触发的刹车。迭代之间，只保留 `TODO.md` 和棘轮文件——这是按照[上下文清理](context-hygiene.md)有意做出的选择。每个会话都从空白状态醒来，读取待办，再做一件范围明确的事。
