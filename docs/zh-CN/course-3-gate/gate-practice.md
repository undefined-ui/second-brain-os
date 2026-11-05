# 决策关卡实践

用一句话概括这项纪律：在评估任何供应商之前，先标注几百个真实样本，训练一个基础分类器。这只需三十分钟；所有宣传主张都必须先在你的数据上击败这个基线，才有资格进入你的处理流水线。

> 这套审查与建立基线的流程已经封装为一项技能：安装[课程插件](../../../plugins/README.md)，在你的处理流水线上运行 `/agents-course:gate-check`。

<a id="label-two-hundred-real-examples"></a>

## 标注两百个真实样本

从智能体实际处理的数据流中取出最近 200 个条目——不要用合成样本，也不要用别人的公开数据集。使用三个标签：

- `file`——纯参考内容：新闻简报、收据、摘要。直接存储，不需要模型。
- `act`——产生明确任务：待支付的发票、待签署的表单、待确认的会议。
- `judge`——需要真正的判断：含糊的请求、提案，以及任何涉及重要后果的内容。

标注时遵守三条规则。根据条目本身标注，而不是根据你希望分类体系长成什么样来标注。拿不准该用两个标签中的哪一个时，选择 `judge`——你会犹豫，说明关卡也可能犹豫。不要中途创造新类别；记下候选类别，然后完成这一轮。每个条目用五秒，总共大约十五分钟。保存为 `labels.csv`：

```csv
text,label
"Weekly digest: ten AI papers you missed",file
"Invoice 2214 attached, due Friday, please confirm receipt",act
"Fwd: any thoughts on this partnership proposal?",judge
```

<a id="train-the-baseline"></a>

## 训练基线

先用 `pip install scikit-learn pandas joblib` 安装依赖，然后运行：

```python
# train_gate.py
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

df = pd.read_csv("labels.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.25,
    stratify=df["label"], random_state=42,
)

gate = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
])
gate.fit(X_train, y_train)

print(classification_report(y_test, gate.predict(X_test), digits=3))
joblib.dump(gate, "gate.joblib")
```

<a id="measure-then-decide"></a>

## 先测量，再决定

阅读每个类别的精确率和召回率，不要只看总体准确率。这些数字就是你的基线。到这时，关于供应商的问题才有了明确含义：更复杂的方案能否在这份数据上超越基线，而且提升幅度足以抵偿网络调用、账单和新增依赖？根据目前的独立证据——见[决策关卡的实际运用](gates-in-practice.md)——对于固定且有标注数据的任务，答案通常是否定的。

<a id="wire-the-winner-in"></a>

## 接入胜出的方案

```python
# gate.py
import joblib

gate = joblib.load("gate.joblib")
THRESHOLD = 0.85
HANDLED = {"file", "act"}

def route(text: str) -> tuple[str, float]:
    probs = gate.predict_proba([text])[0]
    best = probs.argmax()
    label = gate.classes_[best]
    confidence = float(probs[best])
    if label not in HANDLED or confidence < THRESHOLD:
        return "escalate", confidence
    return label, confidence
```

所有返回 `escalate` 的条目都交给主模型——默认拒绝放行。包含日志和 LLM 后备路径的完整分流框架见[基于置信度设置关卡的路由器](../track-jev/build-router.md)；这条流水线无需修改就能接入其中的快捷路径。

<a id="tips"></a>

## 实用建议

- 记录每一次决策及其置信度，无论是否成功分流。这些日志就是你未来的评估集。
- 每周重新训练。主模型解决的升级处理案例就是免费的标注——把它们追加到 `labels.csv`。
- 永远保留 `judge`。没有后备出口的关卡，只能靠猜。
- 阈值从 0.85 开始，只有在留出数据上按置信度区间测量过准确率后，才能调整。

<a id="prove-it-to-yourself"></a>

## 亲自验证

1. 将留出集的预测结果按置信度分组（0–0.5、0.5–0.85、0.85–1.0），报告每组的准确率。如果最高置信度组的准确率还不接近完美，就提高阈值。
2. 分别在阈值为 0.7、0.85 和 0.95 时重新生成报告，记录各自的升级处理比例和快捷路径错误率。有意识地选择取舍。
3. 影子运行一周：关卡给出决策，但所有条目仍由主模型处理。统计两者分歧后，再决定是否信任快捷路径。

有了决策关卡分流输入，昂贵模型终于能腾出空间做真正值得它做的事——这就是下一模块的主题：[工作环境](../course-4-harness/the-office.md)。

深入阅读 → [Jev 工程手册](../track-jev/system-one-models.md)：System One 模型、它们擅长的任务，以及基于置信度设置关卡的路由器实作。
