# 评估资源

这里刻意保持简短。每个条目都有入选理由；它们链接到的其他资料都属选读。所讲概念与[为什么需要评估](why-evals.md)及本手册其余部分相对应。

<a id="the-canon"></a>

## 经典资料

- [你的 AI 产品需要评估](https://hamel.dev/blog/posts/evals/)——Hamel Husain。让评估成为一项系统方法的文章：将单元测试、人工审查和 A/B 测试分为三个层次，并解释为什么要看自己的数据。从这里开始。
- [AI 评估常见问题](https://hamel.dev/blog/posts/evals-faq/)——Husain 和 Shreya Shankar 持续回答每个团队都会问的问题：二元判断还是李克特量表、需要多少标签、由谁标注、自建还是购买。内容密集，而且免费。
- [面向工程师与产品经理的 AI 评估](https://maven.com/parlance-labs/evals)——上述常见问题背后的 Maven 课程；已有数千名工程师和产品经理参加，到 2026 年仍在开班。付费，也是这个领域值得花钱上的一门课。
- [谁来验证验证者？](https://arxiv.org/abs/2404.12272)——Shankar 等人。为 LLM 评判者与人工标签对齐提供研究基础；解释了为什么随着人工评判更多输出，评分标准会漂移。
- [揭开 AI 智能体评估的神秘面纱](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)——Anthropic 的工程指南（2026 年 1 月）：任务选择、轨迹与结果评分、评判者校准、作为 CI 的评估。它最接近[智能体评估](agent-evals.md)的官方操作手册。
- [评估最佳实践](https://developers.openai.com/api/docs/guides/evaluation-best-practices)——OpenAI 的指南；补充上述内容，并可搭配[实用示例中的评估部分](https://developers.openai.com/cookbook/topic/evals)阅读完整的评判示例。

<a id="repos-worth-reading"></a>

## 值得阅读的仓库

- [inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals)——基于英国 AISI 的 Inspect 实现的 200 多项评估。读几个评分器和求解器，看看生产级评估代码是什么样子。
- [terminal-bench](https://github.com/laude-institute/terminal-bench)——在 Docker 中运行、经人工审查并配有可执行评分器的任务。它是构建自己的环境评估时最清晰的参考；更多背景见[智能体评估](agent-evals.md)。

<a id="start-here-three-steps"></a>

## 从这里开始：三个步骤

1. **阅读 30 条轨迹。** 今晚从产品中提取三十份真实（或足够真实）的对话记录，为每个失败写一句话。不需要工具，只用电子表格。这就是错误分析，它会重塑你的路线图。
2. **为失败命名，编码最常见的三类。** 将笔记聚类成分类体系，再把最常见的三种失效模式转成检查——能用代码断言就用代码，不能时就用一个范围明确、经过校准的评判者。具体方法见[设计评估](designing-evals.md)和 [LLM 评判者](llm-as-judge.md)。
3. **将套件放入 CI，每周重跑。** 为检查设置阈值并接入流水线，修复最大的失效模式，再带着新轨迹回到第一步。反复运行这条循环，就是整套方法。
