# 实践：权限与上下文

[第一部分](build-the-loop.md)留下的是一个演示：智能体可以随意运行命令，对话记录也会无限增长。这一部分补上让它成为运行框架的三个要素：权限决策关卡、上下文预算和停止条件。[组成结构一章](what-a-harness-is.md)说，正是这些部件让智能体可以无人值守地运行；在这里，约八十行代码就能实现它们。

第一部分中的所有内容——导入、`TOOLS`、`read_file`、`run_command`——保持原样。替换 `execute` 和 `agent`，再添加其余代码。

<a id="the-code"></a>

## 代码

```python
MAX_TURNS = 30
CONTEXT_BUDGET = 100_000  # characters, roughly 25k tokens

ALLOWLIST = ["ls", "pwd", "cat", "head", "grep", "find",
             "git status", "git diff", "git log", "python", "pytest"]


def permitted(command):
    command = command.strip()
    if any(command == entry or command.startswith(entry + " ") for entry in ALLOWLIST):
        return True
    answer = input(f"\nAgent wants to run: {command}\nAllow? [y/N] ")
    return answer.strip().lower() in ("y", "yes")


def execute(name, tool_input):
    if name == "read_file":
        return read_file(tool_input["path"])
    if name == "run_command":
        if not permitted(tool_input["command"]):
            return "The user declined to run this command. Try another approach or ask them why."
        return run_command(tool_input["command"])
    raise ValueError(f"unknown tool: {name}")


def size_of(message):
    content = message["content"]
    if isinstance(content, str):
        return len(content)
    return sum(len(json.dumps(b)) if isinstance(b, dict) else len(b.model_dump_json())
               for b in content)


def describe(message):
    content = message["content"]
    if isinstance(content, str):
        return content[:150]
    parts = []
    for block in content:
        if isinstance(block, dict):
            parts.append(f"tool output, {len(json.dumps(block))} chars")
        elif block.type == "text":
            parts.append(block.text[:150])
        elif block.type == "tool_use":
            parts.append(f"ran {block.name}({json.dumps(block.input)[:100]})")
    return "; ".join(parts) or "(empty turn)"


def enforce_budget(messages, summaries):
    while sum(size_of(m) for m in messages) > CONTEXT_BUDGET and len(messages) > 5:
        summaries.append(describe(messages.pop(1)))
        summaries.append(describe(messages.pop(1)))


def with_summary(messages, task, summaries):
    if not summaries:
        return messages
    header = (task + "\n\n[Older turns were removed to fit the context budget. "
              "Summary of what happened in them:\n- " + "\n- ".join(summaries) + "]")
    return [{"role": "user", "content": header}] + messages[1:]


def agent(task):
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": task}]
    summaries = []
    for turn in range(MAX_TURNS):
        enforce_budget(messages, summaries)
        response = client.messages.create(
            model=MODEL, max_tokens=8000, system=SYSTEM, tools=TOOLS,
            messages=with_summary(messages, task, summaries),
        )
        for block in response.content:
            if block.type == "text":
                print(block.text)
        if response.stop_reason != "tool_use":
            return
        messages.append({"role": "assistant", "content": response.content})
        results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            print(f"-> {block.name} {json.dumps(block.input)}")
            try:
                results.append({"type": "tool_result", "tool_use_id": block.id,
                                "content": execute(block.name, block.input)})
            except Exception as exc:
                results.append({"type": "tool_result", "tool_use_id": block.id,
                                "content": f"Error: {exc}", "is_error": True})
        messages.append({"role": "user", "content": results})
    print("Stopped: hit the turn limit without finishing.")
```

<a id="the-permission-gate"></a>

## 权限决策关卡

允许列表中的只读命令会直接运行；其他操作都会通过 `input()` 征询你的意见。被拒绝的命令会作为普通工具结果返回，而不是抛出异常——模型将它作为数据读取，并相应调整。这里必须坦诚说明：前缀匹配存在漏洞（`git diff; rm -rf ~` 也是以 `git diff ` 开头），所以生产环境的运行框架会正确解析命令，并且还会在沙箱中执行。这个决策关卡演示的是结构，不是安全保障。

<a id="the-context-budget"></a>

## 上下文预算

当对话记录超过预算时，会成对删除任务之后最旧的轮次——助手轮次连同对应的工具结果，这样任何 `tool_use` 块都不会失去匹配项——并将每对内容的一行摘要加入持续积累的总结，随第一条消息一起传递。这里刻意采用了粗略的方式：工具输出体积很大，却很少需要再次使用，这正是[上下文工程](context-engineering.md)中描述的取舍。

<a id="the-stop-condition"></a>

## 停止条件

当模型在无法完成的任务上不断循环时，`MAX_TURNS` 会限制账单。每个真正的运行框架都有这一限制；每个开发者都曾忘记过一次。

现在，你已经拥有一个微型运行框架。它还缺什么，以及这些缺失何时会变得重要，是[第三部分](build-graduate.md)的内容。
