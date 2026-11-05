# 实践：构建循环

[组成结构一章](what-a-harness-is.md)说，每个运行框架的核心都是一个 while 循环。这一页就来证明它。用大约七十行 Python，你就能得到一个调用真实 Claude API、读取文件并运行命令的智能体；[下一部分](build-guardrails.md)会补上让它成为运行框架的配套机制。三页内容总共约 150 行代码，预留一个晚上即可。

你需要 Python 3.10+，执行 `pip install anthropic`（1.x 版 SDK），并在环境中设置 `ANTHROPIC_API_KEY`。

<a id="two-tools"></a>

## 两个工具

工具由 JSON 模式和函数组成。描述和代码同样重要——模型通过阅读描述来选择工具，[工具与 MCP](tools-and-mcp.md) 对此有详细说明。

<a id="the-code"></a>

## 代码

```python
import json
import subprocess
import sys

import anthropic

MODEL = "claude-opus-5"
SYSTEM = "You are a coding agent working in the current directory. Investigate before you conclude."

TOOLS = [
    {
        "name": "read_file",
        "description": "Read a text file and return its full contents. Use for source files, configs and logs. Paths are relative to the working directory.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "File path, e.g. src/main.py"}},
            "required": ["path"],
        },
    },
    {
        "name": "run_command",
        "description": "Run a shell command and return its exit code, stdout and stderr. Use for listing files, searching and running tests. Times out after 30 seconds.",
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string", "description": "The command, e.g. ls -la"}},
            "required": ["command"],
        },
    },
]


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
    return f"exit code {result.returncode}\n{result.stdout}{result.stderr}"


def execute(name, tool_input):
    if name == "read_file":
        return read_file(tool_input["path"])
    if name == "run_command":
        return run_command(tool_input["command"])
    raise ValueError(f"unknown tool: {name}")


def agent(task):
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": task}]
    while True:
        response = client.messages.create(
            model=MODEL, max_tokens=8000, system=SYSTEM, tools=TOOLS, messages=messages
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


if __name__ == "__main__":
    agent(" ".join(sys.argv[1:]) or "List the files here and describe this project.")
```

<a id="what-each-part-is-doing"></a>

## 各部分在做什么

API 通过 `stop_reason` 表达意图。当它的值为 `tool_use` 时，响应中会包含 `tool_use` 块，每一块都有 `id`、`name` 和已经解析的 `input` 字典。你需要原样追加助手的整个 `response.content`（当前模型会包含思考块，这些块必须随它一同传递），执行每个工具调用，再把所有结果作为 `tool_result` 块放进同一条用户消息中返回，通过 `tool_use_id` 与调用对应。失败也要返回，并标记 `is_error`——好的错误信息能让模型在一轮内恢复，而不必猜测。

把它保存为 `agent.py`，运行 `python agent.py "find the TODO comments in this repo and summarise them"`，观察循环如何运转。[资源](resources.md)中的 Thorsten Ball 教程用 Go 做了同样的事；重点是在你自己的终端中亲眼看到它运行。

<a id="what-it-is-not-yet"></a>

## 目前还缺什么

这还只是演示。它会运行模型想运行的任何命令，而且长任务会让对话记录无限增长。修复这两件事——权限与上下文——就是[第二部分](build-guardrails.md)的内容。
