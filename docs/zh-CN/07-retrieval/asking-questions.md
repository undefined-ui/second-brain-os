# 向知识库提问

建立知识库，是为了让答案来自你真正读过的内容。如果智能体悄悄退回到自身知识，就破坏了这一目的，而且很难察觉：答案流畅、似乎合理，却无法核实。

<a id="the-rule"></a>

## 规则

答案中的每个论断都要来自某个页面，并指出那个页面。

```
Answer from my vault only. Cite the page for each claim. If the vault does not
cover part of the question, say which part rather than filling it in.
```

这条指令应写进 `CLAUDE.md`，而不是每次手动输入。需要靠你记住的规则，往往会在最关键的一天失效。

<a id="start-from-the-index"></a>

## 从索引开始

智能体应先读 `index.md`，再打开看起来相关的页面，然后沿着这些页面的链接向外探索。

另一种做法是全文扫读。这更慢，会把上下文花在仅仅沾边的内容上，也会漏掉措辞与你的问题不同的页面。索引就是为了降低这项成本；参见 [index.md 和 log.md](../04-structuring/index-and-log.md)。

<a id="outside-knowledge-labelled"></a>

## 标明外部知识

有时模型知道一些有用的信息，而知识库里没有。只要明确标注，就没有问题：

```
Cite vault pages for anything from my notes. Anything you know that my vault
does not contain, put under a separate heading marked outside the vault.
```

分开放，它就是有用的背景信息；混在一起，整个答案都会变得不可靠，因为你不再知道哪些部分可以追溯。

<a id="empty-is-a-valid-answer"></a>

## 没有结果也是有效答案

如果知识库中没有某个主题的内容，正确做法就是用一句话说明。

要警惕智能体用通用知识填充空结果，因为这种失败看起来很像一个好答案。如果答案完全没有页面引用，这就是信号。

<a id="answers-should-end-with-what-is-missing"></a>

## 答案应以缺失内容收尾

```
Read: [[page]], [[page]], [[page]]
Not covered: whether this holds for the streaming case
```

只有两行，但作用比看起来大。它们告诉你答案依赖了多少知识库内容，而指出缺口的那一行往往更有价值，因为它准确说明了下一步应该读什么。

<a id="next"></a>

## 下一步

[查询模式](query-patterns.md)
