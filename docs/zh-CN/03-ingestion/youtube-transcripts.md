# YouTube 与播客

视频通常是人们接触量最大、记忆留存最低的来源。一小时的会议演讲，一周后几乎不会留下什么。转写文本可以解决这个问题，而转写就是纯文本，恰好是知识库需要的形式。

<a id="pulling-a-transcript"></a>

## 获取转写文本

大多数视频都有自动生成或上传的字幕。两条可靠的路径是：

```bash
# yt-dlp: subtitles only, no video download
yt-dlp --write-auto-sub --skip-download --sub-format vtt --sub-lang en URL
```

```python
# youtube-transcript-api, if you want it in a script
from youtube_transcript_api import YouTubeTranscriptApi
lines = YouTubeTranscriptApi.get_transcript("VIDEO_ID")
```

将结果保存到 `raw/`，并在 frontmatter 中注明视频名称、频道和 URL。没有 URL 的转写文本，只是一堵匿名文字墙，智能体无法正确引用。

<a id="keep-the-timestamps"></a>

## 保留时间戳

自动生成的转写由带时间戳的片段组成。去掉格式，但每隔几分钟保留一个粗略时间戳。

原因是检索：当 wiki 说明某个主张来自演讲第 34 分钟时，你可以用十秒钟核实。没有时间戳，核查就意味着重看整个视频，也意味着你不会去核查。

<a id="clean-before-ingest"></a>

## 导入之前先清理

自动字幕没有标点，没有说话人标签，还会把技术术语识别错。先让智能体处理一遍：

```
Read raw/talk-transcript.md. Add punctuation and paragraph breaks, label
speakers where they change, and fix obvious mistranscriptions of technical
terms. Do not summarise, do not cut anything, and flag anything you could not
make sense of.
```

不要直接导入未经整理的原始字幕。用缺少标点的文本构建的概念页面，质量会明显下降，因为模型把注意力花在重建句子边界上，而不是理解主张。

<a id="long-videos"></a>

## 长视频

三小时的播客不应当作单一来源。导入前按主题拆分：如果上传者提供了章节标记，就按章节拆；否则，让智能体根据转写文本建议切分位置。

整段导入时，长访谈会产生一个臃肿的来源页面和两三个模糊概念；拆分后，才能提炼出其中真正存在的四个想法。

<a id="podcasts-and-audio"></a>

## 播客与音频

播客很少自带转写。按所需投入从少到多排序，你可以：先检查节目说明，许多节目现在会发布转写；用 Whisper 本地转写；或者使用转写服务。

如果每天都听播客，值得配置本地转写。音频始终不会离开你的设备；对于会议录音，这比对于播客更重要。

<a id="what-is-worth-transcribing"></a>

## 什么值得转写

演讲、讲座、实践者访谈，以及任何包含你日后可能需要的具体主张的内容。

不包括你只为完成一次任务而观看的教程，也不包括那些即使变成文章你也不会重读的东西。观看视频时，你会因为投入了一小时而感觉它有价值，但这种感觉并不是内容质量的信号。

<a id="next"></a>

## 下一篇

[PDF、论文与书籍](pdfs-and-books.md)
