# 循环实践：先过滤，再循环，最后回退

生产环境中的模式并不是“把一切都交给智能体”，而是先过滤，短暂循环，然后回退。Atlan 关于值班智能体的工程文章展示了这一模式在规模化场景中的形态：在 30 天窗口内，确定性的非 LLM 过滤器先过滤掉约 11,000 条告警中的约 86%，此时尚未花费任何 token，因此只有约 14% 的告警进入智能体。智能体随后进行约三轮推理；如果置信度仍低于约 50%，就升级交给纯 Python 编写的确定性回退工作流。原先耗时十几分钟、花费几美元的调查，降到了每次约两分钟、0.28 美元。便宜的代码处理常见情况，模型处理剩余部分，固定路径兜住模型无法结案的事项。


> 这个模式中的目标测试部分已经打包为技能：安装[课程插件](../../../plugins/README.md)，运行 `/agents-course:goal-test`；检查器角色则由随附的 `loop-critic` 智能体承担。

在看代码前，先明确范围：本实践采用的是分诊模式，即先过滤、短暂循环、最后回退。另一种生产模式是在编程智能体外面包一层循环，由目标测试驱动，详见[循环手册的实践项目](../track-loop/build-goal-test.md)。两者有同样的四个部分，只是内部执行的工作不同。

<a id="the-build"></a>

## 动手实现

整个混合方案可以放在一个文件里，原样就能运行。把 `model_next_step` 替换为真实 API 调用，控制流程也不需要改变。

```python
"""Hybrid alert triage: deterministic filter, bounded loop, fixed fallback."""

MAX_TURNS = 3          # Atlan runs about three reasoning cycles before escalating
BUDGET_USD = 0.10      # spend ceiling per alert
COST_PER_TURN = 0.02   # replace with real usage figures from your API responses

ALERTS = [
    {"id": 1, "source": "cron", "message": "nightly backup finished OK"},
    {"id": 2, "source": "api", "message": "TimeoutError in /sync after 30s"},
    {"id": 3, "source": "api", "message": "intermittent 502 from payments"},
]

def prefilter(alert):
    """Deterministic, costs nothing. Returns a verdict, or None for the loop."""
    message = alert["message"].lower()
    if alert["source"] == "cron" or "finished ok" in message:
        return {"cause": "known-benign pattern", "next_step": "close", "via": "filter"}
    return None

def checker(diagnosis):
    """External judge: a diagnosis must name a cause and a concrete next step."""
    return bool(diagnosis.get("cause")) and bool(diagnosis.get("next_step"))

def model_next_step(alert, history):
    """Stub standing in for the model call. Swap in a real API call here."""
    if "timeout" in alert["message"].lower():
        return {"cause": "client timeout on /sync", "next_step": "raise limit to 60s"}
    return {"cause": "", "next_step": ""}   # the stub cannot close this one

def fallback_workflow(alert):
    """Fixed path, no model: always produces a defensible answer."""
    return {"cause": "unresolved by agent", "next_step": "page on-call with raw alert",
            "via": "fallback"}

def triage(alert):
    verdict = prefilter(alert)
    if verdict is not None:
        return verdict                                   # most alerts stop here
    history, spent = [], 0.0
    for turn in range(MAX_TURNS):
        diagnosis = model_next_step(alert, history)
        history.append(diagnosis)
        spent += COST_PER_TURN
        if checker(diagnosis):
            diagnosis["via"] = "loop, turn %d" % (turn + 1)
            return diagnosis                             # exit 1: checker passed
        if len(history) >= 2 and history[-1] == history[-2]:
            break                                        # exit 2: spinning
        if spent > BUDGET_USD:
            break                                        # exit 3: over budget
    return fallback_workflow(alert)                      # every other exit lands here

if __name__ == "__main__":
    for alert in ALERTS:
        print(alert["id"], triage(alert))
```

第 1 条告警完全不会接触模型，第 2 条在循环第一轮就能结案，第 3 条重复两次后进入回退。每条路径返回相同的数据形状，因此调用方无需知道是哪一层给出的答案。

<a id="tips"></a>

## 建议

- 扩展过滤器，而不是延长循环。循环两次给出相同诊断时，就可以考虑把它变成 `prefilter` 的一条规则。
- 每个结果都记录 `via`。过滤、循环、回退的比例就是健康指标；回退占比不断上升，说明循环正在悄悄失效。
- 让回退保持朴素。它的工作是不依靠模型给出有依据的答案，而不是再尝试一次聪明办法。
- 检查器应严格到让人觉得不太客气，因为它是模型唯一无法靠说服绕过的部分。如何针对真实编程智能体加固它，见[目标测试实践](../track-loop/build-goal-test.md)；完整的停止机制见[停止条件](../track-loop/stop-conditions.md)。

<a id="prove-it-to-yourself"></a>

## 亲自验证

1. 运行文件，然后设置 `MAX_TURNS = 0` 再运行一次。每条未被过滤的告警都应进入回退；如果出现崩溃，就说明漏了一条退出路径。
2. 让 `model_next_step` 永远返回同一个错误答案。确认重复检测在第二轮退出，而不是第三轮。
3. 添加一条能被过滤器捕获的第四条告警，并记录整批任务现在调用模型多少次。在覆盖率不下降的情况下让这个数字降低，就是这种模式的全部经济逻辑。至于哪些决策根本值得调用模型，是下一模块[低成本决策](../course-3-gate/cheap-decisions.md)的主题。

深入阅读 → [循环工程手册](../track-loop/what-loop-engineering-is.md)：停止条件、批评者、上下文维护，以及一个能让你放心跑到第二天早晨的循环。
