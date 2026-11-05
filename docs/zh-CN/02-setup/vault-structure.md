# 知识库结构

知识库承担两种不同的工作，也需要两种不同的结构。在同一棵文件夹树中保留它们，同时让两种结构彼此分离，才能使系统在第一个月之后继续运作。

**知识层**保存你读过并理解的内容。它不断增长，按想法组织。

**项目层**保存你目前正在处理的工作。它按流水线组织，其中大部分内容在项目交付后不再活跃。

```
brain/
  CLAUDE.md            who you are, how the vault works
  raw/                 source material, never edited after it lands
    assets/
  wiki/                the knowledge layer
    sources/           one page per ingested item
    entities/          people, organisations, products, tools
    concepts/          ideas, methods, frameworks
    synthesis/         comparisons, themes, open questions
    index.md           catalog of every page
    log.md             what the agent did, chronologically
  projects/            the project layer
    youtube-channel/
      CLAUDE.md        this project only
      Inputs/          ideas, briefs, raw material
      Process/         work in progress
      Outputs/         finished work
      Feedback/        results, metrics, what happened
  output/              generated reports and drafts
```

<a id="why-the-split"></a>

## 为什么要分开

项目流水线回答“我这周在做什么”，wiki 回答“我对 X 知道些什么”。强迫一种结构同时承担两者，结果要么是知识库塞满失效任务文件夹，要么是项目被埋在工作时无人打开的概念页面之下。

两者通过链接连接。项目页面链接到它依赖的概念；概念页面不断积累使用过它们的项目引用。这就是复利出现的地方：当你第二次在同一领域启动项目时，知识层已经备好了相应内容。

<a id="set-the-projects-up-by-asking"></a>

## 通过提问建立项目

```
Create a project folder in my vault called youtube-channel. Inside it, create
four folders: Inputs, Process, Outputs, Feedback. Then write a CLAUDE.md inside
that project folder describing what this project is, its one goal, and your
specific role in helping me hit it. Interview me if you need details.
```

对每个领域重复这一过程：内容、财务、客户。每个项目只有一个目标，写在项目自己的 `CLAUDE.md` 中。具有三个目标的项目，产出往往对哪个目标都没有帮助。

<a id="rules-that-keep-it-working"></a>

## 让系统持续运行的规则

- **不要编辑 `raw/`。** 它是档案。如果某份来源有误，就替换文件并重新导入，让它始终忠实记录你实际保存的内容。
- **不要嵌套得太深。** 深到四层的文件夹，人们会停止打开。导航依靠图谱，而不是文件夹树。
- **智能体为外部使用生成的所有内容，都放到 `output/` 或项目的 `Outputs/`，**不要散落在知识库根目录。

<a id="next"></a>

## 下一篇

[项目范围限定](project-scoping.md)
