# 实作：具有明确类型的决策端点

Jev 需要排候补名单，因此大多数读者现在还无法调用——访问状态见[入门](getting-started.md)。但今天就能构建适合接入它的结构：一个函数，接收数据模式和状态，返回带置信分数、具有明确类型的决策。现在先用普通 LLM 建好这个衔接点，之后就能直接换入 [System One 模型](system-one-models.md)。本篇构建端点；下一篇将它接入路由器。

<a id="the-contract"></a>

## 接口约定

一个函数 `decide(schema, question, state)`，返回 `{"value": ..., "confidence": ...}`；其中 `value` 符合数据模式，`confidence` 介于 0 和 1 之间。这对应 Jev 基本类型所提供的内容——带类型的答案加概率——但并不假装与其生成机制相同。

<a id="why-self-consistency-not-logprobs"></a>

## 为什么用自洽性，而不是 logprobs

从 LLM 获取有意义的置信数字，有两条途径。Token 的 logprobs 本来是更直接的一条，但目前行不通：Claude API 根本不暴露 logprobs，而对于 OpenAI 当前的模型，开发者报告只要启用结构化输出（`json_schema`），返回的 logprobs 数组就是空的——恰好这种模式又是本方案所依赖的。可行的途径是自洽性：对同一个问题采样多次，采用多数答案，将一致比例作为置信度。虽然更粗略，但它测量的是真实存在的东西——模型对你的输入做出判断的稳定程度。

<a id="the-code"></a>

## 代码

通过 Claude API 的结构化输出（`output_config`，已正式可用，无需 beta 标头）约束输出，在小型快速模型上并行采样五次。需要 `pip install anthropic`，以及 `ANTHROPIC_API_KEY`。

```python
# decision.py
import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

import anthropic  # pip install anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-haiku-4-5"      # small and fast: this seat is System One work
SAMPLES = 5

def _ask_once(schema: dict, question: str, state: str) -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        temperature=1.0,  # the default, stated on purpose: samples must vary
        messages=[{"role": "user", "content": f"{question}\n\nState:\n{state}"}],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {"value": schema},
                    "required": ["value"],
                    "additionalProperties": False,
                },
            }
        },
    )
    text = next(b.text for b in response.content if b.type == "text")
    return json.dumps(json.loads(text)["value"], sort_keys=True)  # normalise for voting

def decide(schema: dict, question: str, state: str) -> dict:
    with ThreadPoolExecutor(max_workers=SAMPLES) as pool:
        futures = [pool.submit(_ask_once, schema, question, state) for _ in range(SAMPLES)]
        answers = [f.result() for f in futures]
    winner, votes = Counter(answers).most_common(1)[0]
    return {"value": json.loads(winner), "confidence": votes / SAMPLES}

if __name__ == "__main__":
    print(decide(
        schema={"type": "string", "enum": ["billing", "technical", "account", "other"]},
        question="Which team should handle this support ticket?",
        state="My card was charged twice for the same invoice this month.",
    ))
```

<a id="how-this-differs-from-a-real-system-one-model"></a>

## 与真正的 System One 模型有何不同

要清楚看到差距。Jev 是非自回归的，会在一次并行处理中回答一整组问题；这里则针对每个问题发起五次生成调用。Jev 的置信度是使用 RLCD 训练得到、经过校准的概率；我们的是投票计数，只能取六种值，并不代表已经校准。这里的延迟是一两秒，对方声称 70–500 毫秒；每次决策的成本是五次 Haiku 调用，对方则为每百万 token 0.042 美元。替换后保留下来的是接口约定——而这正是你的代码所依赖的部分。下一篇：[基于置信度设置关卡的路由器](build-router.md)。
