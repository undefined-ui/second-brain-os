# 值得安装的插件

即使一个都不安装，Obsidian 也能正常工作。当你遇到某个插件所解决的具体问题时，再添加它。

<a id="local-rest-api"></a>

## Local REST API

只有选择 [MCP 路径](mcp-obsidian.md)时才需要。它通过本地 HTTP API 提供知识库访问，使智能体能够在 Obsidian 打开时，从任何会话访问知识库。

<a id="dataview"></a>

## Dataview

对 frontmatter 进行查询，并将结果渲染在笔记中。当页面数量多到你需要仪表盘时，它就值得安装：

````
```dataview
TABLE updated, tags
FROM "wiki/concepts"
WHERE updated < date(today) - dur(90 days)
SORT updated ASC
```
````

这条查询列出三个月内无人修改的概念页面，是知识库中最有用的复查查询。

<a id="templater"></a>

## Templater

支持变量和日期的模板，可用于 [`vault-template/templates/`](../../../vault-template/templates/) 中定义的页面结构。它对手写笔记有用。智能体不需要它，因为智能体会直接写入 frontmatter。

<a id="worth-adding-later"></a>

## 以后值得添加的插件

- **[Git](https://github.com/Vinzent03/obsidian-git)**，目录中安装量排名第三的插件。可在 Obsidian 内提交更改，与[版本管理](../09-maintenance/versioning-with-git.md)配合使用。
- **[Importer](https://github.com/obsidianmd/obsidian-importer)**，官方插件，能导入 Notion、Evernote、Roam、Bear 和 Apple Notes。迁移现有资料堆时，应先用它。
- **[查找孤立文件和损坏链接](https://github.com/Vinzent03/find-unlinked-files)**，无需离开应用，就能执行与[结构检查](../09-maintenance/lint-and-health.md)相同的检查。
- **[Omnisearch](https://github.com/scambier/obsidian-omnisearch)**，提供更好的全文搜索，也能搜索 PDF 内文。

完整排名及安装量见：[resources/plugins.md](../../../resources/plugins.md)。

<a id="what-to-avoid"></a>

## 应该避免什么

避免在后台改写文件的插件。任何自动格式化、自动排序 frontmatter 或定时重命名的插件，都会与智能体互相干扰。最终你可能花一整个晚上，才搞清楚到底是谁弄坏了页面。

在有值得查看的资料之前，也应避免安装复杂的图谱或仪表盘插件。一个装了十五个插件的空知识库，只是拖延的产物，还称不上系统。

<a id="next"></a>

## 下一篇

[Git、同步与备份](git-and-sync.md)
