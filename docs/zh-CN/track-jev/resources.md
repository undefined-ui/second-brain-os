# Jev 资源

Jev 于 2026 年 9 月 15 日发布。这个领域才出现一周：以下链接于 2026 年 9 月 21 日检查过，本篇会很快过时。概念见 [System One 模型](system-one-models.md)。

<a id="official"></a>

## 官方资源

- [介绍 System One 模型与 Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)——发布文章；主张、定价、命名
- [TypeSafe 文档](https://docs.typesafe.ai/)与 [System One 概念](https://docs.typesafe.ai/concepts/system-one)——API 结构、基本类型、限制
- [HTTP API 参考](https://docs.typesafe.ai/api)与[工作流评估](https://evals.typesafe.ai/)——供应商自己的基准测试方法
- [控制台](https://console.typesafe.ai/)——候补名单、密钥、试用区
- SDK：[JavaScript](https://github.com/typesafe-ai/typesafe-sdk-js)、[Python](https://github.com/typesafe-ai/typesafe-sdk-python)

<a id="third-party-explainers-and-writeups"></a>

## 第三方解读与文章

- [维基百科：Jev（AI 模型）](https://en.wikipedia.org/wiki/Jev_(AI_model))——中立概述；公司、融资、版本
- [LangChain：使用 Jev 构建运行框架](https://www.langchain.com/blog/building-a-harness-with-jev)——智能体技术栈集成；见[智能体技术栈中的 Jev](jev-in-an-agent-stack.md)
- [DataCamp：System One 模型与 Jev](https://www.datacamp.com/blog/system-one-models-jev)——不错的基准对比表
- [Valyu：如何使用 Jev](https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e)——目前最好的实践指南；模式与易错点
- [MindStudio 发布报道](https://www.mindstudio.ai/blog/jev-system-one-model-launch)——包含真实成本数字的模拟器演示
- [AI News：ChatGPT 先驱发布 Jev](https://www.artificialintelligence-news.com/news/chatgpt-pioneer-launches-jev-model-for-programmatic-logic/)——创始人背景
- [awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev)——社区维护的链接清单、演示、集成
- 网关集成：[Pydantic AI](https://pydantic.dev/docs/ai/models/typesafe/)、[LiteLLM](https://docs.litellm.ai/docs/pass_through/typesafe)、[Cloudflare](https://developers.cloudflare.com/ai/models/typesafe/jev/)、[Netlify](https://www.netlify.com/changelog/typesafe-jev-ai-gateway/)

<a id="sceptical-takes"></a>

## 质疑观点

- [Anthony Maio：不会说话的语言模型](https://anthonymaio.substack.com/p/jev-the-language-model-that-wont)——最值得阅读的批判文章；校准与分布偏移方面的能力仍未得到证明
- [KDnuggets：大家对 Jev 的误解](https://www.kdnuggets.com/what-everyone-is-getting-wrong-about-typesafe-ais-jev)——“零幻觉”指零模式之外的输出，不是零错误答案
- [MindStudio：RLCD 与 RLHF](https://www.mindstudio.ai/blog/typesafe-jev-rlcd-vs-rlhf)——训练方法的主张究竟是什么

请记住，目前流传的每个性能数字，最终都来自 TypeSafe 自己的评估。写作时还没有独立的大规模评估；等它们出现后，应该放在本页最上方。

<a id="start-here"></a>

## 从这里开始

1. 先读发布文章，紧接着读 Maio 的质疑文章——一次读完供应商的主张与平衡它的观点。
2. 阅读 [Jev 擅长什么](what-jev-is-good-for.md)，判断自己的工作负载中是否有适合 Jev 的任务。
3. 加入候补名单，然后用自己的标注数据运行[入门](getting-started.md)中的分流评估，再决定是否相信任何基准数字。
