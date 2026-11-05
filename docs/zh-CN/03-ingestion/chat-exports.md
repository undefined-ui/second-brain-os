# 聊天记录导出

聊天历史是你拥有的最被低估、也最敏感的来源。里面有你多年间解决的问题、推敲过的决策，以及针对你当时不理解之处给出的解释。

其中也充满了你不愿放进可能对外分享的文件里的信息。运行这里的任何步骤之前，先阅读下方的隐私部分。

<a id="exporting"></a>

## 导出

Claude 和 ChatGPT 都能在账户设置中将全部历史导出为 JSON。导出完成后，你会收到包含下载链接的邮件，通常只需几分钟。

<a id="converting-to-markdown"></a>

## 转换为 Markdown

一整块 JSON 不适合直接导入。将它拆成每次对话一个文件：

```bash
python3 scripts/chat_export_to_md.py conversations.json ./raw --min-words 150
```

脚本位于 [`scripts/`](../../../scripts/README.md)。它支持常见的导出结构，写入包含标题和日期的 frontmatter，并跳过低于指定词数门槛的对话。

如果输出大部分是只有一句话的交流，就提高 `--min-words`。大多数人的历史中，大约九成都是短暂、一次性的问题，它们除了增加数量，几乎没有其他价值。

<a id="filter-before-ingesting"></a>

## 导入前先筛选

不要导入整份导出记录。一千次对话会产生一千个来源页面，最终得到一个所有内容都隐约互相关联的 wiki。

分成三类：

- **值得导入。** 你想清楚了某件事、作出了决策，或得到了真正听懂的解释的对话。它们承载你的推理，而不只是事实。
- **值得保留，但不值得导入。** 将它们留在 `raw/` 中归档。智能体可以按需搜索，不必为每次对话建立 wiki 页面。
- **删除。** 调试会话、一次性查询，以及任何你在搜索结果中看到后会感到烦躁的内容。

让智能体帮助分类，而不是自己逐条处理：

```
Read the titles and first exchange of every file in raw/chats/. Group them into
worth-ingesting, archive, and delete, with one line of reasoning each. Do not
move or delete anything, just give me the lists.
```

<a id="what-makes-these-sources-different"></a>

## 这些来源有什么不同

聊天日志记录的是你的思考，因此有用的提取内容往往不是答案，而是你提出的问题、最初理解错的地方，以及什么改变了你的想法。

明确告诉智能体这一点：

```
These are my own past conversations. Build pages around what I was trying to
work out and what conclusion I reached, not around the assistant's explanations.
Note where I changed position, and record the date, because my views may have
moved since.
```

<a id="privacy"></a>

## 隐私

聊天历史比知识库中的任何其他文件都包含更多关于你的信息：健康、财务、不能公开谈论的工作，以及你无意提到的他人情况。

导入之前，决定哪些内容根本不应进入知识库，并从 `raw/` 中删除对应文件。事后脱敏并不可靠，因为资料已经传播到了概念页面和链接中。

如果知识库存放在 Git 仓库中，请让远程仓库保持私有。请参阅[隐私](../09-maintenance/privacy-and-secrets.md)。

<a id="next"></a>

## 下一篇

[语音笔记与会议](voice-and-meetings.md)
