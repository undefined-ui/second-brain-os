# 版本管理

Git 让智能体可以安全地无人值守运行。没有它，出错的一次运行就是谜团；有了它，每项变更都有可阅读的差异，也能用一条命令撤回。

<a id="commit-granularity"></a>

## 提交粒度

每次运行一次提交，并在提交信息中写明任务：

```
ingest 2026-09-07: 4 sources, 9 pages
lint 2026-09-07: 3 broken links, 1 merge
```

不要每个文件提交一次，那会淹没历史；也不要每周只提交一次，那样就无法在保留正确运行结果的同时，单独撤回一次错误运行。

定时任务应把提交自身工作作为运行流程的一部分。参见[定时维护](../06-agents/scheduled-maintenance.md)。

<a id="reading-diffs-of-generated-pages"></a>

## 阅读生成页面的差异

最初几周值得经常做，之后也应偶尔检查。

主要看两件事：不该改的页面是否发生变化，以及本应局部更新的页面是否被整篇重写。智能体明明只被要求追加内容，却悄悄重写整个页面，这种行为只有查看差异才会发现。

一周后执行 `git log --stat`，能看到自动化最常修改哪些页面，通常很有启发。

<a id="reverting"></a>

## 撤回

```bash
git revert HEAD          # undo one run, keep the history
git checkout .           # discard uncommitted work
git checkout HEAD~3 -- wiki/concepts/some-page.md   # one page back
```

中间那条命令说明了为什么每次大操作前都应该提交。批量补录如果中途出错，你损失的只是这次运行，而不是整个知识库。

<a id="branches"></a>

## 分支

对于会触及结构的实验，分支值得使用，例如新的页面规范、数据结构变更，或者在不同指令下批量重新导入。

```bash
git checkout -b new-schema
```

运行实验、阅读结果，然后合并或删除分支。在 `main` 上直接做，事后再决定，往往会让知识库卡在迁移了一半、没人愿意收尾的状态。

<a id="what-not-to-commit"></a>

## 不该提交什么

`.obsidian/workspace*`、缓存，以及任何包含密钥的文件。Local REST API 的密钥保存在插件数据中，因此首次推送前要检查 `.obsidian/plugins/`。

除非已经明确决定公开知识库，否则远程仓库应保持私有。

<a id="next"></a>

## 下一步

[备份与可迁移性](backups-and-portability.md)
