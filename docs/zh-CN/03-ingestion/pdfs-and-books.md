# PDF、论文与书籍

PDF 是最容易以乱码般形式进入知识库的格式：双栏内容变成交错行，表格散架，脚注插入句子中间，然后智能体悄悄在这一团混乱之上建立页面。

导入前检查提取质量。只需十秒钟，就能省去以后重写页面的麻烦。

<a id="extraction"></a>

## 提取文本

```bash
# text, layout preserved reasonably well
pdftotext -layout paper.pdf raw/paper.md
```

对于结构化内容，`pymupdf` 提供更细的控制，也能单独提取图片和表格。无论用什么工具，都要打开输出，读一段中间的文字。如果句子不连贯，应先修复提取过程，而不是寄希望于智能体能应付。

<a id="scanned-documents"></a>

## 扫描文档

扫描件是图片，文本提取不会得到内容，或只能得到很少的内容。先使用 `ocrmypdf` 执行 OCR，它会在不改变可见文档的情况下增加文本层。要预料到专有名词和数字可能识别错误；OCR 来源中的任何数值，在作为事实写入 wiki 页面之前都应核实。

<a id="papers"></a>

## 论文

论文需要与普通文章不同的处理方式，因为日后需要的内容分布并不均匀。摘要、方法、结果和局限几乎承载了全部价值。

一种有用的导入指令：

```
This is an academic paper. Build the source page around: the question it asks,
the method, the result with its actual numbers, and the limitations the authors
state themselves. Record sample sizes. Do not report a finding without the
condition it holds under.
```

最后一条规则能让 wiki 保持诚实。剥离了适用条件的研究结论，两年后会变成信心十足的胡说。

如果你经常读论文，Zotero 值得使用。它管理元数据，也能导出 Markdown，从而整洁地进入 `raw/`。

<a id="books"></a>

## 书籍

整本书太大，不适合作为单一来源导入，而且大多不值得这样做。真正值得导入的是你的划线摘录。

Kindle 划线可以从 Kindle 应用导出，也可以通过 Readwise 直接同步到 Obsidian。划线通常是一组引用段落，因此应为每本书建立一个来源页面，再让智能体根据想法，而不是根据引文本身构建概念页面。

Wiki 中的引用应保持简短，并保留出处。一个重现半章内容的页面，同时构成版权问题和检索问题。

<a id="figures-and-tables"></a>

## 图与表

文本提取会丢失这两者。当某张图承载了论证时，将它截图保存到 `raw/assets/`，并在来源页面中引用，让页面上的主张有据可查。

<a id="next"></a>

## 下一篇

[聊天记录导出](chat-exports.md)
