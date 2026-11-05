# Jev 入门

Jev 的公开文档问世大约一周。本篇反映的是截至 2026 年 9 月 21 日已发布的信息，预计会很快过时。

<a id="access"></a>

## 获取访问权限

Jev 目前处于需要加入候补名单的早期访问阶段。你可以在 [console.typesafe.ai](https://console.typesafe.ai/) 注册，TypeSafe 表示会分批向候补名单中的开发者开放。API 密钥位于 `console.typesafe.ai/settings/keys`；部分网关（Vercel AI Gateway、Netlify、Cloudflare）也提供代理访问。控制台有免费试用区，在获得额度之前也能先体验。

<a id="the-api-shape"></a>

## API 结构

整个 API 只有一个端点——`POST https://api.typesafe.ai/v1/systemone`——默认模型为 `jev-latest`（目前是 `jev-1.13.0`）。官方 SDK 的安装命令为 `pip install typesafe-sdk` 和 `npm install @typesafe-ai/sdk`，两者均从环境变量读取 `TYPESAFE_API_KEY`。

请求由一个 `state`（字符串、JSON 对象或文本数组——目前只支持文本），加上使用三种基本类型定义的命名问题组成：

```python
from typesafe import Choice, Score, Noul

questions = {
    "team": Choice(instructions="Which team should handle this",
                   criteria={"billing": "Payment issues", "technical": "Bugs"}),
    "frustration": Score(instructions="Customer frustration level",
                         criteria=["Calm", "Frustrated but civil", "Very angry"]),
    "refund": Noul(instructions="Customer explicitly requesting a refund"),
}
```

所有问题都在一次并行处理中回答。文档记载的限制：状态最多 64k token，状态加最长问题最多 32k token，每个 `Choice` 最多 255 个选项。价格为每百万输入 token 0.042 美元，输出不计量。

<a id="a-realistic-first-project"></a>

## 一个务实的入门项目

支持工单分流是典型的入门项目：拿出 200 张已经标注过的历史工单，让 Jev 回答上面的三个问题，再将答案和概率与你的标注比较。这样就能得到最重要的两点：在*你的*数据分布上的准确率，以及置信分数是否足够诚实、可以据此设置阈值，方法见[智能体技术栈中的 Jev](jev-in-an-agent-stack.md)。早期有人报告不到一小时就做出了可运行的演示，这并不难相信；但真正的里程碑应是你自己的评估。

注意文档记录的易错点：Jev 按字面阅读（否定表达容易出问题），不会可靠计数，不会给日期排序，而且上下文臃肿时表现会下降——发送状态前，先在代码中检索和过滤。如果状态中包含用户文本，应测试对抗性注入。

<a id="what-is-still-unknown-or-unreleased"></a>

## 仍然未知或尚未发布的内容

直白地说：架构、模型规模和权重都未公开。无法自托管，无法微调，不支持图像、音频或视频输入，没有公开的速率限制或 SLA 文档，没有独立基准测试，也没有证据证明定价可持续而不是靠补贴。正式开放的日期尚未公布。如果其中任何一项阻碍你的使用，那就等待——是否值得排队，见 [Jev 擅长什么](what-jev-is-good-for.md)；文档见[资源](resources.md)。
