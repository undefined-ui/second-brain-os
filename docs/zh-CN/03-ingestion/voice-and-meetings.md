# 语音笔记与会议

值得捕捉的想法很少恰好出现在桌前。走路、开车或排队时，语音是唯一可行的采集方式，却也是大多数知识库从未接入的方式。

<a id="capture"></a>

## 采集

任何录音应用都可以，只要文件最终能到达知识库可访问的位置。需要消除的阻力是传输：如果将音频从手机送入知识库需要不止一个动作，你终究会停止。

最简单可靠的配置是：使用手机默认应用录音，分享到云端文件夹，然后让定时任务把新音频转写到 `raw/`。

Obsidian 手机应用可以直接录音到知识库。如果你已经在同步移动端内容，就可以完全省去传输环节。

<a id="transcription"></a>

## 转写

Whisper 可在本地运行，足以处理在伸手距离内录制的语音笔记。对于这类来源，本地处理比其他场景更重要，因为语音笔记包含尚未成形的想法，而会议录音包含他人的发言。

要预料到姓名和技术术语会被识别错误。应在导入时修正，而不是拖到以后，趁你还记得当时说了什么。

<a id="voice-notes-are-drafts-not-sources"></a>

## 语音笔记是草稿，不是来源文献

语音笔记是你大声思考的过程，包含起头后放弃的话语和未说完的句子。原封不动地导入，会产生不连贯的来源页面。

将转写文本当作提炼单一想法的原始输入：

```
This is a voice note, my own thinking out loud. Extract the actual idea, drop
the false starts and repetition, and write it as one short concept page in my
words. If there are two unrelated ideas, make two pages. Keep the recording date.
```

<a id="meetings"></a>

## 会议

会议会产生三类值得保留的东西，以及大量不值得保留的内容：决策、具有责任人的承诺，以及尚未解决的问题。

```
This is a meeting transcript. Extract decisions made, commitments with who owns
each one, and open questions. Link every person mentioned to their entity page.
Skip discussion that did not lead anywhere.
```

将承诺放到相关项目的 `Inputs/`，而不是 wiki。承诺是工作，不是知识，而且一周后就可能过时。[两个层次](../01-concepts/two-layers.md)解释了这种分离为什么重要。

<a id="consent-and-other-people"></a>

## 同意与他人信息

录制他人发言的法律要求因司法辖区而异，这不是走形式。有些地区要求所有参与者同意。

除了合法性，还要考虑：会议转写包含他人在非公开场合的自然发言。不要把这些内容放入可能对外分享的知识库；也要考虑会议是否真的需要进入知识层，还是只提取其中三项决策就足够了。

<a id="next"></a>

## 下一篇

[电子简报与邮件](newsletters-and-email.md)
