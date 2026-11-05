# 实作：基于置信度设置关卡的路由器

[具有明确类型的决策端点](build-decision-endpoint.md)放在智能体前面，才能发挥价值。[智能体技术栈中的 Jev](jev-in-an-agent-stack.md)描述了这个模式：以低成本对传入请求分类，分类器有把握时直接行动，没把握时交给完整 LLM。决策头是快捷路径，绝不是唯一的路径。

<a id="the-design"></a>

## 设计

三条规则就能完成全部工作：

- 只要路由具有确定性的处理程序，就可以不调用大模型而完成处理。
- 只有置信度超过阈值，*并且*路由具有处理程序时，才进入快捷路径。其他情况全部交给后备路径。
- 记录每一次决策，无论是否成功分流。日志就是未来的评估集：一旦这些工单有了人工标注，你就可以测量分类器准确率，根据真实错误成本调整阈值，之后还能在相同输入上比较 Jev 的答案。

<a id="the-code"></a>

## 代码

把上一篇的 `decision.py` 放在同一目录中，就可以直接运行。

```python
# router.py
import json
import time

import anthropic

from decision import decide

client = anthropic.Anthropic()
FULL_MODEL = "claude-opus-5"   # the fall-through: full-strength, full price
THRESHOLD = 0.8                # start conservative; tune against labels later
LOG_PATH = "decisions.jsonl"

# Routes with a handler get a fast path. "other" is a deliberate catch-all
# with no handler, so anything unfamiliar always falls through.
ROUTES = {
    "billing": lambda t: "Routed to billing queue with a receipt request.",
    "password_reset": lambda t: "Sent the automated password-reset link.",
    "cancellation": lambda t: "Escalated to a human retention agent.",
    "other": None,
}
ROUTE_SCHEMA = {"type": "string", "enum": list(ROUTES)}
QUESTION = "Which route should handle this support ticket?"

def log_decision(entry: dict) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def fall_through(ticket: str) -> str:
    response = client.messages.create(
        model=FULL_MODEL,
        max_tokens=16000,
        messages=[{"role": "user", "content": f"Handle this support ticket:\n{ticket}"}],
    )
    return next(b.text for b in response.content if b.type == "text")

def handle(ticket: str) -> str:
    start = time.perf_counter()
    decision = decide(ROUTE_SCHEMA, QUESTION, ticket)
    decide_ms = round((time.perf_counter() - start) * 1000)

    handler = ROUTES.get(decision["value"])
    fast = handler is not None and decision["confidence"] >= THRESHOLD
    outcome = handler(ticket) if fast else fall_through(ticket)

    log_decision({
        "ts": time.time(),
        "ticket": ticket,
        "value": decision["value"],
        "confidence": decision["confidence"],
        "threshold": THRESHOLD,
        "path": "fast" if fast else "fall_through",
        "decide_ms": decide_ms,
    })
    return outcome

if __name__ == "__main__":
    print(handle("I was charged twice for the same invoice this month."))
    print(handle("Your app deleted three years of my data and I am furious."))
```

<a id="what-to-watch"></a>

## 需要观察什么

阈值是一项业务决策，而非建模决策——依据快捷路径做错操作的代价确定，详见上文链接中的阈值讨论。使用替代实现时，要记住置信度是样本一致率，而不是经过校准的概率：对于一张含糊的工单，五次采样全部一致并不罕见，因此要保留兜底路由，在降低阈值之前，每周对照人工判断审查日志。唯一不能省略的就是日志记录。拿到 Jev 访问权限后，这份包含输入、决策和置信度的文件，正好可以原样回放给它——这就是下一篇的内容：[替换为 Jev](build-swap-in-jev.md)。
