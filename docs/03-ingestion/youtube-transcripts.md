# YouTube and podcasts

Video is the highest-volume, lowest-retention source most people have. An hour
of a conference talk leaves almost nothing behind a week later. Transcripts fix
that, and a transcript is just text, which is exactly what the vault wants.

## Pulling a transcript

Most videos have captions, auto-generated or uploaded. Two dependable routes:

```bash
# yt-dlp: subtitles only, no video download
yt-dlp --write-auto-sub --skip-download --sub-format vtt --sub-lang en URL
```

```python
# youtube-transcript-api, if you want it in a script
from youtube_transcript_api import YouTubeTranscriptApi
lines = YouTubeTranscriptApi.get_transcript("VIDEO_ID")
```

Save the result into `raw/` with frontmatter naming the video, the channel and
the URL. Without the URL, a transcript is an anonymous wall of text and the
agent cannot cite it properly.

## Keep the timestamps

Auto-generated transcripts arrive as timestamped fragments. Strip the
formatting, keep coarse timestamps every few minutes.

The reason is retrieval: when the wiki says a claim came from minute 34 of a
talk, you can verify it in ten seconds. Without that, checking means rewatching,
which means you will not check.

## Clean before ingest

Auto-captions have no punctuation, no speaker labels, and mangle technical
terms. Have the agent do a pass first:

```
Read raw/talk-transcript.md. Add punctuation and paragraph breaks, label
speakers where they change, and fix obvious mistranscriptions of technical
terms. Do not summarise, do not cut anything, and flag anything you could not
make sense of.
```

Do not skip to ingesting the raw caption dump. Concept pages built from
unpunctuated text come out noticeably worse, because the model spends its
attention reconstructing sentence boundaries instead of understanding claims.

## Long videos

A three-hour podcast is not one source. Split it by topic before ingesting,
either by chapter markers if the uploader added them, or by asking the agent to
propose split points from the transcript.

Ingested whole, a long interview produces one bloated source page and two or
three vague concepts. Split, it produces the four ideas that were actually in
it.

## Podcasts and audio

Podcasts rarely ship transcripts. Options, in order of effort: check the show
notes, many now publish one; run local transcription with Whisper; or use a
transcription service.

Local transcription is worth setting up if you listen daily. The audio never
leaves your machine, which matters more for meeting recordings than for
podcasts.

## What is worth transcribing

Talks, lectures, interviews with practitioners, anything with a specific claim
you might need later.

Not tutorials you watched to do a task once, and not anything you would not
reread as an article. Video feels valuable while watching because it takes an
hour. That feeling is not a signal about the content.

## Next

[PDFs, papers and books](pdfs-and-books.md)
