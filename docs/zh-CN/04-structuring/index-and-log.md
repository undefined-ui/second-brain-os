# index.md 与 log.md

这两个文件本身不是知识，但没有它们，知识就难以触达，也无法审计。

<a id="indexmd"></a>

## index.md

它是目录：按类型列出所有页面，并在底部列出内容缺口。

它的真正作用是降低检索成本。智能体收到问题时，先阅读索引就能知道已有些什么，以及哪些页面值得打开。没有索引，就只能进行全文扫描，这样更慢、占用更多上下文，还会漏掉措辞与问题不同的页面。

让索引便于浏览，而不只是看起来包罗万象：

```markdown
## Concepts

### Retrieval
- [[Retrieval augmented generation]] - chunking, embeddings, when it beats a wiki
- [[GraphRAG]] - entity graph plus community summaries

### Agents
- [[Agent harness]] - the loop around a model
```

每个条目用一行描述。这一行能帮助智能体决定是否打开页面，值得为它花费 token。

<a id="gaps"></a>

## 内容缺口

在索引底部，列出已经被链接、但尚不存在的页面。

这部分是知识库中最能直接指导行动的内容。它列出了你自己的资料不断提及、但你从未写下来的东西，通常也是一张精确的下一步阅读地图。

<a id="logmd"></a>

## log.md

每次操作记一行，以追加方式写入，最新的记录位于底部。

```
2026-09-07 ingest raw/karpathy-gist.md -> 1 source, 2 concepts, 1 entity, 9 links
2026-09-07 merge [[RAG]] <- [[Retrieval-augmented generation]]
2026-09-08 lint -> 3 broken links fixed, 2 orphans flagged
```

日志让由智能体维护的知识库可以被审计。当页面出现你不熟悉的说法时，日志会告诉你是哪次运行生成了它。当某个内容消失时，有了日志，它就是一次可以追溯的合并；没有日志，它就成了谜。

日志也为[复查技能](../../../skills/README.md)提供原始材料：本周发生了哪些变化，应从这里获取，而不是通过文件时间戳猜测。

<a id="keeping-both-from-bloating"></a>

## 避免两个文件膨胀

索引随知识库增长是正常的，但平铺列表达到大约两百个条目时，就开始难以浏览。按主题分组；某个主题超过大约三十个条目后，为它建立独立索引页，并从主索引链接过去。

日志会无限增长，而旧记录几乎没人读。将几个月以前的条目汇总成每月一行，或者归档到带日期的文件中。保留近期细节，压缩较早历史。

<a id="the-rule-that-matters"></a>

## 最重要的规则

这两个文件必须在所记录工作发生的同一次运行中更新。

滞后的索引比没有索引更糟，因为智能体会相信它，并停止寻找未列出的页面。事后补写的日志是一份重建记录，而不是当时的记录。

<a id="next"></a>

## 下一步

[图谱](../05-graphs/README.md)：这些结构将从这里开始发挥价值。
