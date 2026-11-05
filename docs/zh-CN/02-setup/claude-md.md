# 编写你的 CLAUDE.md

知识库根目录中的 `CLAUDE.md`，是智能体在每次会话开始时读取的文件。有了它，助手就知道你的情况；没有它，你每次都得从头介绍。

一个空知识库配上一份好的 `CLAUDE.md`，比没有这份文件的满库资料更有用，因为关于你的上下文会影响智能体之后撰写的每个页面。

<a id="do-not-type-it-get-interviewed"></a>

## 不要直接写，先接受访谈

毫无准备地直接编写这份文件，通常只会得到单薄、泛泛的版本；回答问题则能得到具体的版本。将下面这段内容粘贴给智能体：

```
You are setting up my second brain. Interview me ONE question at a time to
build my profile. Ask about: who I am and what I do, my goals for this year,
how I want you to talk to me, my strengths and weaknesses, and my current
projects. Wait for each answer before the next question. When finished, write
everything into CLAUDE.md at the vault root, structured with headers.
```

回答时，把对方当作第一天入职的联合创始人。模糊的回答会产生模糊的文件，而每次会话都会继承它。

<a id="what-belongs-in-it"></a>

## 应该包含什么

- **你是谁，在做什么。** 具体到一个陌生人也能据此采取行动。
- **有时间范围的目标。** 今年、本季度。没有日期的目标很容易过时。
- **如何与你交流。** 篇幅、语气，以及你希望它提出多少反对意见。
- **你的优势和薄弱点。** 这能让智能体知道什么时候该质疑你，而不是附和。
- **当前项目，**每个一行，链接到对应文件夹。
- **知识库自身的规则：** 文件夹布局、页面规范和链接规则。[`vault-template/CLAUDE.md`](../../../vault-template/CLAUDE.md) 中的版本是一个可用的起点。

<a id="what-does-not-belong-in-it"></a>

## 不应该包含什么

- 每周都变化的信息。这些应放到项目文件中。
- 对模型已经知道的事物作长篇解释。
- 任何类型的凭据。
- 你不会付诸行动的愿望宣言。智能体会按字面理解它们。

<a id="two-levels"></a>

## 两个层级

根目录的 `CLAUDE.md` 是战略层：你是谁、想实现什么、知识库如何运作。每个项目文件夹有自己的 `CLAUDE.md`，只描述该项目。当你将项目作为独立知识库打开时，智能体只读取那一份文件，不再把你整个人生的背景带入每项任务。请参阅[项目范围限定](project-scoping.md)。

<a id="iterate-on-it"></a>

## 持续改进

如果智能体连续两次做错同一件事，那是 `CLAUDE.md` 的问题，而不是提示词的问题。把规则补进去，并附上理由，因为没有理由的规则，在未预料的场景中容易被过度按字面执行。

每月重新读一遍这份文件。目标会变化，项目会结束，过时的个人背景会悄悄降低智能体所有产出的质量。

<a id="next"></a>

## 下一篇

[知识库结构](vault-structure.md)
