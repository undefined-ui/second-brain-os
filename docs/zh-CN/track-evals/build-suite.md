# 实践：评估套件

你已经从[阅读执行轨迹](build-traces.md)中得到 `golden.jsonl`。这一页将它变成可运行的套件：一个普通 Python 文件，不用框架。能用代码断言评分的都交给代码；其余部分由一个范围明确的评判者处理，遵循 [LLM 评判者](llm-as-judge.md)中的方法。示例目标是由单一提示词驱动的客服助手——根据你应用的调用方式替换 `run_target` 即可。

<a id="the-script"></a>

## 脚本

保存为 `eval_suite.py`。需要执行 `pip install anthropic`，并设置 `ANTHROPIC_API_KEY`。评判者刻意使用与目标不同的模型。

```python
import argparse
import json
import re
import sys

import anthropic

client = anthropic.Anthropic()

TARGET_MODEL = "claude-opus-5"
JUDGE_MODEL = "claude-sonnet-5"

SYSTEM_PROMPT = (
    "You are the support assistant for Acme Invoicing. Answer only from the "
    "provided account context. If the context does not contain the answer, say so."
)

JUDGE_PROMPT = """You are grading one output from an invoicing assistant.

Statement to verify:
{expectation}

Assistant output:
<output>
{output}
</output>

First write one or two sentences of reasoning. Then, on the final line, write
exactly VERDICT: pass if the statement is true of the output, or VERDICT: fail
if it is not. Do not reward length, politeness, or effort.
"""


def run_target(case: dict) -> str:
    response = client.messages.create(
        model=TARGET_MODEL,
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": case["input"]}],
    )
    return "".join(b.text for b in response.content if b.type == "text")


def grade_code(output: str, checks: dict) -> tuple[bool, str]:
    for needle in checks.get("must_contain", []):
        if needle.lower() not in output.lower():
            return False, f"missing required text: {needle!r}"
    for needle in checks.get("must_not_contain", []):
        if needle.lower() in output.lower():
            return False, f"contains forbidden text: {needle!r}"
    return True, "code checks passed"


def grade_judge(output: str, expectation: str) -> tuple[bool, str]:
    response = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": JUDGE_PROMPT.format(expectation=expectation, output=output),
        }],
    )
    text = "".join(b.text for b in response.content if b.type == "text")
    match = re.search(r"VERDICT:\s*(pass|fail)", text, re.IGNORECASE)
    passed = bool(match) and match.group(1).lower() == "pass"
    return passed, text.strip().splitlines()[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("golden", help="path to golden.jsonl")
    parser.add_argument("--limit", type=int, default=0, help="run only the first N cases")
    parser.add_argument("--threshold", type=float, default=0.0, help="exit 1 below this pass rate")
    args = parser.parse_args()

    with open(args.golden, encoding="utf-8") as f:
        cases = [json.loads(line) for line in f if line.strip()]
    if args.limit:
        cases = cases[: args.limit]

    results = []
    for case in cases:
        output = run_target(case)
        if case.get("checks"):
            passed, reason = grade_code(output, case["checks"])
        else:
            passed, reason = grade_judge(output, case["judge_expectation"])
        results.append({"id": case["id"], "passed": passed, "reason": reason})
        print(f"{'PASS' if passed else 'FAIL'}  {case['id']}  {reason}")

    rate = sum(r["passed"] for r in results) / len(results)
    print(f"\npass rate: {rate:.0%}")
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump({"pass_rate": rate, "results": results}, f, indent=2)
    if args.threshold and rate < args.threshold:
        sys.exit(1)


if __name__ == "__main__":
    main()
```

使用 `python eval_suite.py golden.jsonl` 运行。它会为每个用例打印一行，写入 `results.json`，并在使用 `--threshold` 时对表现不佳的运行返回非零退出码——这就是 CI 所需的一切。

<a id="calibrate-the-judge-before-trusting-it"></a>

## 信任评判者之前先校准

先人工标注十个经模型评判的输出：写入 `labels.jsonl`，每行一个输出，包含 `id`、`output`、`expectation`，以及你自己的 `label`（true/false）。然后检查一致性：

```python
import json

from eval_suite import grade_judge

with open("labels.jsonl", encoding="utf-8") as f:
    labels = [json.loads(line) for line in f if line.strip()]

agree = 0
for row in labels:
    verdict, reason = grade_judge(row["output"], row["expectation"])
    agree += verdict == row["label"]
    if verdict != row["label"]:
        print(f"disagree on {row['id']}: judge={verdict} you={row['label']} - {reason}")
print(f"agreement: {agree}/{len(labels)}")
```

阅读每一个分歧；通常是预期描述太含糊，有时是你的标签不明确。十个标签是一个下午版本的做法——完整的 50–100 个标签流程见 [LLM 评判者](llm-as-judge.md)。

<a id="when-a-framework-earns-its-keep"></a>

## 何时值得使用框架

对于一个目标、一个评判者和几百个用例，这个文件已经足够。如果想并排比较多个提示词或模型，又不想自己编写比较矩阵，就使用 promptfoo；如果需要沙箱智能体环境、求解器和逐步骤评分，就使用 Inspect。[工具](tooling.md)一章介绍了两者；它们都不能替代分类工作，只是把它扩大规模运行。
