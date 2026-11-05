# 评估实践

本篇是最小化实作：一个下午、五个步骤、一份案例文件和一个运行器，无需搭建基础设施。[评估工程手册](../track-evals/why-evals.md)通过三次实作组装完整流水线；你在这里做出的所有内容，都可以直接沿用过去。

> 以下整个实作也已经封装为一项技能：安装[课程插件](../../../plugins/README.md)，在智能体仓库中运行 `/agents-course:evals-bootstrap`。

<a id="step-1-mine-twenty-failures-into-cases"></a>

## 第一步：从二十次失败中提炼案例

取出智能体最近的运行记录，逐一阅读，直到找到二十个真实失败——不能是想象出来的。针对每个失败写一行：输入是什么，以及哪个具体行为本该发生却没有发生。“未搜索知识库就回复了。”“未请求批准就退款了。”“声称笔记已创建，实际上没有。”二十次失败通常会归为四到八类行为。

<a id="step-2-write-one-behavioural-check-per-case"></a>

## 第二步：为每个案例编写一个行为检查

每个案例变成一条 YAML 记录：输入、用文字描述的预期行为，以及可由机器检查的轨迹断言。

```yaml
- id: refund_1042
  input: "Refund order #1042, customer says it arrived broken"
  expect: looks up the order before replying; asks approval before refund
  check:
    - trace has get_order before send_reply
    - trace has approval_request before refund
```

将二十个案例全部保存为 `cases.yaml`。`expect` 一行供人阅读；`check` 各行才是测试。

<a id="step-3-run-the-checks-on-traces"></a>

## 第三步：对轨迹运行检查

将每次运行的轨迹保存为 `traces/<id>.json`——一个包含工具调用在内的事件列表：

```json
[
  {"type": "tool_call", "name": "get_order", "args": {"order_id": "1042"}},
  {"type": "tool_result", "name": "get_order", "ok": true},
  {"type": "tool_call", "name": "approval_request", "args": {"action": "refund"}},
  {"type": "tool_call", "name": "refund", "args": {"order_id": "1042"}},
  {"type": "tool_call", "name": "send_reply", "args": {"channel": "email"}}
]
```

将以下运行器保存为 `check_traces.py`（需要 `pip install pyyaml`）：

```python
import json
import re
import sys
from pathlib import Path

import yaml


def tool_calls(trace: list) -> list:
    return [e["name"] for e in trace if e.get("type") == "tool_call"]


def check_rule(rule: str, calls: list) -> tuple[bool, str]:
    m = re.fullmatch(r"trace has (\w+) before (\w+)", rule.strip())
    if m:
        first, second = m.group(1), m.group(2)
        if first not in calls:
            return False, f"{first} never called"
        if second not in calls:
            return False, f"{second} never called"
        if calls.index(first) < calls.index(second):
            return True, "ok"
        return False, f"{second} came before {first}"
    m = re.fullmatch(r"trace has (\w+)", rule.strip())
    if m:
        name = m.group(1)
        return name in calls, "ok" if name in calls else f"{name} never called"
    m = re.fullmatch(r"trace lacks (\w+)", rule.strip())
    if m:
        name = m.group(1)
        return name not in calls, "ok" if name not in calls else f"{name} was called"
    return False, f"unparseable rule: {rule!r}"


def main() -> None:
    cases = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
    trace_dir = Path(sys.argv[2])
    failures = 0
    for case in cases:
        trace_file = trace_dir / f"{case['id']}.json"
        trace = json.loads(trace_file.read_text(encoding="utf-8"))
        calls = tool_calls(trace)
        for rule in case["check"]:
            passed, reason = check_rule(rule, calls)
            print(f"{'PASS' if passed else 'FAIL'}  {case['id']}  {rule}  ({reason})")
            failures += not passed
    print(f"\n{failures} failing check(s)")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
```

运行 `python check_traces.py cases.yaml traces/`。它不调用模型，因此耗时远低于五秒预算，并会在失败时以非零退出码供 CI 使用。逐项报告检查结果，保持程序打印的形式——绝不要将这些结果压缩成一个通过率。

<a id="step-4-calibrate-one-narrow-judge"></a>

## 第四步：校准一个范围明确的评判器

对于代码看不出来的行为（例如“回复以检索到的笔记为依据”），编写一个只问一个问题、给出二元判定的评判器。在信任它之前，先亲自标注十份输出并测量一致率——[构建测试套件](../track-evals/build-suite.md)中的十样本标注脚本用三十行代码就能完成这件事，[以 LLM 为评判器](../track-evals/llm-as-judge.md)则介绍需要留意的偏差。如果一致率低于十次中八次，应修正评分标准，而不是调整阈值。

<a id="step-5-schedule-weekly-hand-grading"></a>

## 第五步：安排每周人工评分

每周随机抽取五次真实运行，按自己的预期人工评分。与测试套件存在分歧的情况，变成新案例；套件从未识别的失败，变成新检查。每周十五分钟，才能阻止案例集老化。

<a id="tips"></a>

## 实用建议

- 凡是两种方法都能胜任的地方，优先用 `trace has` 断言，而不是评判器。
- 保持案例 ID 稳定且便于搜索；六个月后你还会搜索它们。
- 当某项检查忽过忽不过，说明这种行为确实不确定——这是一个发现，不是测试缺陷。
- 每种行为都增加一个正常路径案例，以便发现矫枉过正。

<a id="prove-it-to-yourself"></a>

## 亲自验证

1. 从某条轨迹中删除 `get_order` 事件，确认运行器会失败，并给出正确原因。
2. 让评判器对同一份输出运行三次；若判定不一致，就收紧评分标准，直到不再出现分歧。
3. 故意破坏退款行为，确认总分几乎不变，但相应的单项检查会变红。

下一模块：[从原型走向生产](../course-6-production/from-prototype.md)。

深入阅读 → 从刚刚写好的 `cases.yaml` 出发，继续手册中的三次实作：[阅读你的执行轨迹](../track-evals/build-traces.md)，从分类阶段开始（采集已经完成）；[构建测试套件](../track-evals/build-suite.md)，加入经过校准的评判器；以及 [CI 关卡](../track-evals/build-ci.md)。这里做的任何工作都不会浪费。
