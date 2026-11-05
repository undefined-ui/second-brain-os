# 评估工具

市场逐渐集中为两种形态：先做评估、再补上可观测性的平台，以及先做轨迹追踪、再补上评估的平台。以下方案截至 2026 年末都仍活跃且有人维护。选一个就继续前进；[为什么需要评估](why-evals.md)中的飞轮，比供应商重要得多。

<a id="platforms"></a>

## 平台

- [Braintrust](https://www.braintrust.dev/)——围绕 `Eval()` 循环构建、以评估为核心的商业平台：数据集、实验、并排的回归差异、CI 关卡。对于由工程主导、从评估而非仪表盘起步的团队，它是默认选择。
- [Langfuse](https://langfuse.com/)——最成熟的开源选择；提供 OpenTelemetry 风格的轨迹追踪，一个下午即可自行托管，再在上面叠加数据集和 LLM 评判评估。如果数据驻留或开放许可证不可妥协，就选它。
- [LangSmith](https://www.langchain.com/langsmith)——LangChain 的平台。如果你使用 LangChain/LangGraph，只需修改一行代码即可接入观测，而且数据集工作流很扎实；如果没有使用这套技术栈，就没有太多理由特意选择它。
- [W&B Weave](https://weave-docs.wandb.ai/)——Weights & Biases 提供的评估与追踪工具；给函数加上装饰器，即可获得带版本的轨迹和评估仪表盘。如果你的组织已在使用 W&B，它是自然选择。

<a id="frameworks-and-clis"></a>

## 框架与 CLI

- [promptfoo](https://www.promptfoo.dev/)——开源 CLI：在 YAML 中声明提示词、提供商和断言，获得比较矩阵。它是最快回答“哪个提示词／模型更好”的方式，还提供完善的红队测试模式。非常适合 CI。
- [Inspect](https://inspect.aisi.org.uk/)——英国 AI 安全研究所的开源 Python 框架：可组合的求解器、评分器和沙箱智能体环境，并在 [inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals) 中提供 200 多项现成评估。为严谨性而设计，是安全测试领域的标准，也很适合一般的[智能体评估](agent-evals.md)。
- [OpenAI Evals](https://github.com/openai/evals)——2023 年的注册表仓库仍然存在，但 OpenAI 当前支持的路径是 API 和控制面板中的 Evals 产品，并配有[评估最佳实践指南](https://developers.openai.com/api/docs/guides/evaluation-best-practices)。使用文档，而不是仓库。
- [DeepEval](https://github.com/confident-ai/deepeval)——pytest 风格的评估框架，提供现成指标（忠实度、答案相关性）。便于接入 CI；把内置指标当作起点，而不是事实——按 [LLM 评判者](llm-as-judge.md)一章的方法校准。

<a id="claude-code-plugin-evals"></a>

## Claude Code 插件评估

Anthropic 将评估框架直接加入了 Claude Code（v2.1.269+，2026 年 9 月）：`claude plugin eval` 会用一组真实感较强的提示词测试插件或技能，以六种评分器（`regex`、`tool_used`、`tool_order`、`file_exists`、`llm`、`baseline`）为结果评分，而且——这是坦诚之处——还会在*不使用*插件时再运行一遍，报告插件实际带来的增量。`claude plugin eval init` 会交互式提出用例；`--threshold` 用作 CI 关卡。文档见 [code.claude.com/docs/en/plugin-evals](https://code.claude.com/docs/en/plugin-evals)。如果你为智能体编写技能，这就是把同一套方法应用到提示词支撑结构上。

<a id="honest-advice"></a>

## 坦诚的建议

每个平台用玩具数据集演示时都很漂亮。真正的区别，是你的团队是否真的会每周在里面阅读轨迹。签下任何协议前，先用自己的失效分类试用两周。
