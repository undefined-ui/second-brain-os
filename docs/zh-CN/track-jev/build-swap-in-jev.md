# 实作：替换为 Jev

前两篇的目的，就是让本篇变得平淡简单。[决策端点](build-decision-endpoint.md)和[路由器](build-router.md)遵循同一个约定——`decide(schema, question, state)` 返回一个值和一个置信度——因此，用 Jev 替换 LLM 临时代用品，应该只需修改一个文件，而非重写。现在能否进行替换取决于候补名单；最新访问状态见[入门](getting-started.md)。

<a id="the-seam"></a>

## 衔接点

为路由器提供一个不体现具体实现的统一导入点。以后需要变动的只有这个文件：

```python
# decider.py — the seam. Swapping implementations is an edit here, nowhere else.
from decision import decide  # today: the LLM stand-in

# from jev_decider import decide  # later: Jev, once access arrives
```

将 `router.py` 改为 `from decider import decide`，就为替换做好了准备。Jev 一侧将数据模式映射到它的基本类型——枚举变为 `Choice`，布尔值变为 `Noul`，而开放式内容一律拒绝，因为 Jev 只回答边界明确的问题：

```python
# jev_decider.py — written from TypeSafe's published docs, UNTESTED until you
# have quota. Verify call shapes against docs.typesafe.ai before relying on it.
from typesafe import TypeSafe, Choice, Noul  # pip install typesafe-sdk

client = TypeSafe()  # reads TYPESAFE_API_KEY

def decide(schema: dict, question: str, state: str) -> dict:
    if "enum" in schema:
        q = Choice(instructions=question,
                   criteria={str(o): str(o) for o in schema["enum"]})
    elif schema.get("type") == "boolean":
        q = Noul(instructions=question)
    else:
        raise ValueError("Jev answers bounded questions only; keep this on the LLM.")
    answer = client.decide(state=state, questions={"value": q})["value"]
    return {"value": answer.value, "confidence": answer.probability}
```

<a id="shadow-mode-first"></a>

## 先采用影子模式

不要第一天就切换导入。先让 Jev 在影子模式下运行：替代实现仍然回答每个请求，Jev 在旁边回答相同请求，两者都写入日志。因为还没有任何组件读取 Jev 的答案，所以它即使失败也不会影响生产。

```python
# shadow.py — point the seam here during the trial period.
import json
import time

import decision as standin
import jev_decider as jev

LOG_PATH = "shadow.jsonl"

def decide(schema: dict, question: str, state: str) -> dict:
    t0 = time.perf_counter()
    live = standin.decide(schema, question, state)
    live_ms = round((time.perf_counter() - t0) * 1000)
    try:
        t1 = time.perf_counter()
        shadow = jev.decide(schema, question, state)
        shadow_ms = round((time.perf_counter() - t1) * 1000)
    except Exception as exc:
        shadow, shadow_ms = {"error": str(exc)}, None
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": time.time(), "state": state,
                            "live": live, "live_ms": live_ms,
                            "shadow": shadow, "shadow_ms": shadow_ms}) + "\n")
    return live  # callers only ever see the stand-in
```

<a id="what-to-measure-before-flipping"></a>

## 切换前要测量什么

先让替代实现运行一周，建立基线，再根据影子日志比较：

- **延迟。** 比较 `live_ms` 与 `shadow_ms` 的 p50 和 p95，从你自己的基础设施测量，而不是采用 TypeSafe 声称的 70–500 毫秒。
- **成本。** 按每千次决策计算，对比每个决策五次 Haiku 调用的费用，与 Jev 按输入 token 计量的费用。
- **一致率。** 两个 `value` 有多频繁相同。一致率高且延迟更低，就具备了放行条件；一致率低，说明其中有人错了，只有标注才能告诉你是谁。
- **校准。** 将 Jev 的概率分桶，对照你的标注检查每个桶的准确率——在自己的流量上验证供应商最核心的主张。

当数字证明值得时，在 `decider.py` 中切换导入，并保留替代实现作为回滚方案，只需改动一行注释就能恢复。
