# 电子简报与邮件

电子简报最容易自动采集，也最容易过量导入。自动化采集后，要严格决定哪些内容值得获得 wiki 页面，因为能自行归档的信息流，完全可能每月向知识库塞进一百个你从未要求过的页面。

<a id="a-dedicated-address"></a>

## 使用专用地址

创建一个只用于知识库的邮箱地址，将电子简报重新订阅到这个地址。仅这一步，就能将想保留的资料与收件箱中的其他内容隔离，也意味着自动化从不会碰到你真正使用的邮箱。

之后，用你现有的自动化工具，将这个地址收到的内容转存到 `raw/`。任何能够写入文件的规则都可以。

<a id="deduplicate"></a>

## 去重

电子简报常常重复报道。同一项发布，会在同一周的四份不同摘要中出现；事实相同，开场白不同。

如果直接导入，你会得到四个讲同一件事的来源页面，而概念页面会引用全部四个，仿佛形成了互相佐证。简报之间的交叉引用不是独立确认；把它们当作独立确认的 wiki，会夸大某件事已经得到证实的程度。

明确给导入过程设置指令：

```
These are newsletters. Several will cover the same item. Group them by topic
first, write one source page per actual item citing every newsletter that
mentioned it, and note where they disagree. Do not treat repetition across
newsletters as confirmation.
```

<a id="what-deserves-a-page"></a>

## 什么内容值得建立页面

电子简报大多是附带评论的链接。评论本身很少值得建立概念页面，被链接的原始内容有时值得。

实用做法是让智能体阅读摘要，然后给出候选清单：

```
Read this week's newsletters in raw/newsletters/. List anything worth reading in
full, with one line on why. Ingest nothing yet.
```

接着，认真剪藏其中两三个一手来源，并导入这些原始资料。简报完成了筛选的工作，而知识库最终保存的是实际来源，不是它的摘要。

<a id="regular-email"></a>

## 普通邮件

大多数邮件不应该进入第二大脑。安排日程的邮件、收据、关于事务细节的来回沟通，都不是知识，只会增加数量。

值得导入的，是作出了真实决策或把某件事解释清楚的邮件会话。把这些会话转发到采集地址，每次一条，有意识地处理。

绝不要定时将整个收件箱接入 `raw/`。那会导入与你通信的每个人的所有信息，而其中大部分并不是你有权长期保留的。

<a id="next"></a>

## 下一篇

[批量导入多年积累的资料](bulk-backfill.md)
