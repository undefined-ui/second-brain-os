# 实践：阅读执行轨迹

这是三个实践页面中的第一篇：带你从“机器人有时会出错”，走到磁盘上的黄金数据集文件。[构建套件](build-suite.md)会让它可以运行；发布关卡一页会将它接入 CI。一个下午可以完成三篇。如果跳过了背景，请先看[为什么需要评估](why-evals.md)。

从[模块 5 的练习](../course-5-evals/evals-practice.md)过来的？你已经有二十个用例和一个运行器——跳过收集，直接进入下面的分类步骤；黄金数据集会在你已有内容的基础上成长。

<a id="collect-30-traces"></a>

## 收集 30 条轨迹

从生产环境提取三十份真实对话记录——日志、数据库导出，有什么就用什么。真实输入总是比编造的更好。还没有流量？针对你自己的应用生成一个起始集：将三十个合理用户可能提出的问题写入 `starter_inputs.txt`（变化角色、措辞、长度；加入几个应该拒绝的问题），然后通过实际入口运行它们：

```python
import json

from app import answer  # your product's entry point: str -> str

with open("starter_inputs.txt", encoding="utf-8") as f:
    inputs = [line.strip() for line in f if line.strip()]

with open("traces.jsonl", "w", encoding="utf-8") as out:
    for text in inputs:
        out.write(json.dumps({"input": text, "output": answer(text)}) + "\n")
```

<a id="the-error-analysis-pass"></a>

## 错误分析

按顺序阅读每条轨迹，并在普通文本文件中为每条写一行。下面的格式可用：

```
trace_id | verdict | one-sentence failure note | verbatim quote
014 | fail | invented an order number not present in context | "your order #88412 shipped"
015 | ok   |  |
016 | fail | apologised and asked a question instead of acting | "could you clarify which invoice"
```

四条规则：每个失败只写一句话；始终引用输出；将成功记为 `ok`，以便明确总数；读完全部三十条之前，不修复任何问题。这一步花费的一小时，是整个实践中最有价值的一小时。

<a id="cluster-into-a-taxonomy"></a>

## 聚类成分类体系

三十条笔记可以手动分类，不过 LLM 也能胜任初步整理。将笔记粘贴到以下提示词中：

```text
Below are failure notes from an error-analysis pass over one AI product,
one note per line, prefixed with a trace id.

Cluster them into 3 to 8 failure modes. For each mode give:
- a snake_case name
- a one-sentence definition
- the trace ids it covers

Every note must land in exactly one mode. Put genuine one-offs in a mode
called "other" rather than inventing a mode for a single note. Do not
propose fixes. Return a markdown list.

<notes>
PASTE YOUR NOTES HERE
</notes>
```

把结果当作草稿：合并本质上相同的模式，为模糊的名称重新命名，将你不同意的项降级处理。模型负责整理；分类体系由你负责。

<a id="write-the-golden-set"></a>

## 编写黄金数据集

将分类体系转成 `golden.jsonl`，每行一个用例：

```json
{"id": "hallucinated_id_003", "failure_mode": "hallucinated_order_id", "input": "where is my order?", "checks": {"must_not_contain": ["#"]}, "judge_expectation": null, "source": "trace 014"}
{"id": "clarify_loop_001", "failure_mode": "clarify_instead_of_acting", "input": "cancel my March invoice", "checks": null, "judge_expectation": "The reply cancels or begins cancelling the invoice rather than asking a clarifying question.", "source": "trace 016"}
{"id": "happy_path_002", "failure_mode": "none", "input": "what is your refund window?", "checks": {"must_contain": ["30 days"]}, "judge_expectation": null, "source": "trace 015"}
```

五个字段。`id` 应稳定且便于搜索。`failure_mode` 来自分类体系（正常路径用例使用 `none`）。`input` 是产品收到的内容。`checks`（可以由代码评分的字符串断言：`must_contain`、`must_not_contain`）与 `judge_expectation`（由评判者验证的一句话）必须且只能设置其中一个——只要 `checks` 能覆盖用例，就优先使用它。`source` 指回原始轨迹，因为某个用例开始失败时，你会需要原始记录。

每个有名称的失效模式都要有几个用例，还要加上普通的成功案例，避免过度适应异常情况——理由见[设计评估](designing-evals.md)。将文件与代码一起提交，然后继续构建套件。
