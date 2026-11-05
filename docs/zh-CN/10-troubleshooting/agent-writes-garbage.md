# 智能体写出的内容很糟

页面主题看似正确，却完全没有阅读价值。

<a id="diagnose-the-source-first"></a>

## 先检查来源

修改指令之前，先检查输入。打开 `raw/` 中的文件，读一遍。

人们归咎于智能体的糟糕页面，有一半其实来自错误的提取：PDF 的多栏文本交错在一起、自动字幕没有标点，或者网页剪藏抓到的是 Cookie 横幅而非文章。

智能体无法从混乱文本写出好页面，而且不会告诉你它正在吃力地处理。参见 [PDF](../03-ingestion/pdfs-and-books.md) 和[转录文本](../03-ingestion/youtube-transcripts.md)。

<a id="then-check-claudemd"></a>

## 然后检查 CLAUDE.md

如果来源干净，问题就在页面规范。

这些具体问题会导致页面空泛：没有定义每种页面类型应包含什么；任何地方出现了“概括总结”这样的要求；没有要求面向未读过来源的读者写作；没有链接要求。

重写页面规范，把页面结构明确写出来。参见[页面类型](../04-structuring/page-types.md)。

<a id="add-an-example-not-another-rule"></a>

## 增加一个示例，而不是又一条规则

这是效果最好，却最少被采用的修复办法。把一个好的概念页面完整放进 `CLAUDE.md`，作为目标示例。

规则只能抽象描述输出，每条新规则还会与其他规则相互作用。一个示例能直接传达目标，就像你让别人模仿一种风格时，对方也会先向你索要示例。

<a id="ask-what-it-was-working-from"></a>

## 询问它依据了什么

```
You wrote [[page]]. Which parts of the source did you use, and what did you leave
out?
```

回答通常会立即指出问题：它只读了片段，分不清来源自身的论断与转述的说法，或者指令把它引向了摘要写作。

<a id="roll-back-and-re-run"></a>

## 回滚并重跑

修正规范，撤回糟糕页面，重新导入。

```bash
git checkout HEAD~1 -- wiki/
```

不要手动修补这些页面。如果规范错了，那次运行生成的每一页都会有相同缺陷。只修复你注意到的三页，其他问题仍然留着。

<a id="next"></a>

## 下一步

[失效链接与孤立页面](broken-links.md)
