# 实践：发布关卡

只有在有人记得时才运行的套件，迟早会停止运行。这一页将[构建套件](build-suite.md)中的 `eval_suite.py` 接入 GitHub Actions：一个子集为每个 PR 把关，完整套件每晚运行，分数则写入提交到仓库的记分板。原则见[智能体评估](agent-evals.md)中的 CI 部分。

<a id="the-workflow"></a>

## 工作流

保存为 `.github/workflows/evals.yml`。先在仓库密钥中添加 `ANTHROPIC_API_KEY`。

```yaml
name: evals

on:
  pull_request:
  schedule:
    - cron: "30 2 * * *"

permissions:
  contents: write

concurrency:
  group: evals-${{ github.ref }}
  cancel-in-progress: true

env:
  ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}

jobs:
  pr-gate:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - run: pip install anthropic
      - name: Run the smoke subset
        run: python eval_suite.py golden.jsonl --limit 20 --threshold 0.85

  nightly:
    if: github.event_name == 'schedule'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - run: pip install anthropic
      - name: Run the full suite
        run: python eval_suite.py golden.jsonl --threshold 0.85
      - name: Append to the scoreboard
        if: always()
        run: |
          rate=$(python -c "import json; print(f\"{json.load(open('results.json'))['pass_rate']:.0%}\")")
          echo "| $(date -u +%Y-%m-%d) | ${rate} | ${GITHUB_SHA::7} |" >> scoreboard.md
          git config user.name "eval-bot"
          git config user.email "actions@users.noreply.github.com"
          git add scoreboard.md
          git commit -m "scoreboard: nightly eval run"
          git push
```

<a id="choosing-the-threshold"></a>

## 选择阈值

阈值应低于当前通过率，而不是恰好等于它。模型评判用例具有随机性：一个通常达到 90% 的套件，即使什么都没变，也偶尔会输出 87%；如果关卡设为 90%，这种噪声就会变成没人信任的失败构建。完整运行套件三次，取最差的数字，再低几个百分点设置关卡。只有实际改进连续一周在每晚运行中都成立后，才提高标准。还要在脚本中固定模型 ID——模型别名背后的版本悄悄变化，也是一项变更，应通过 PR 引入，像其他修改一样接受关卡检查。

<a id="cost-control"></a>

## 成本控制

PR 任务运行前二十个用例；把最便宜、最有诊断价值的放在前面——优先选择最大失效模式中由代码评分的用例，因为调整 `golden.jsonl` 的顺序没有成本，而昂贵的是评判调用。二十个用例、每个两次调用，每个 PR 的开销很小；包含所有评判用例的完整套件，每晚运行一次，不受仓库繁忙程度影响。`cancel-in-progress` 会防止强制推送堆积重复运行。如果每晚的花费仍然让你吃不消，说明套件已经超出一个下午版本的规模，而[设计评估](designing-evals.md)中的样本量指南能帮助判断哪些用例值得保留。

<a id="the-scoreboard"></a>

## 记分板

手动初始化 `scoreboard.md`：

```markdown
# Eval scoreboard

| date | pass rate | commit |
|---|---|---|
```

每晚的任务都会追加一行并提交，即使运行失败也如此——日志中的差分数是事实，缺失的一行则是谜。记分板的意义不在形式，而在于数字成为仓库每份克隆中都可见的历史。当分数下降时，`git log scoreboard.md` 和夜间日志会准确说明发生在哪一天、哪个提交。这条循环——阅读轨迹、编码失败、设置关卡、观察数字——就是[为什么需要评估](why-evals.md)中的飞轮，现在它已经能自行运行。
