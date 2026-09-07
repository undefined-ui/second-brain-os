# Voice notes and meetings

The ideas worth capturing rarely arrive at your desk. Voice is the only capture
method that works while walking, driving or standing in a queue, and it is the
one most vaults never wire up.

## Capture

Any recorder app works, as long as the file ends up somewhere the vault can
reach. The friction to eliminate is the transfer: if getting audio from phone to
vault takes more than one action, you will stop.

Simplest reliable setup: record in the phone's default app, share to a cloud
folder, and have a scheduled task transcribe anything new into `raw/`.

Obsidian's mobile app can record directly into the vault, which removes the
transfer entirely if you already sync mobile.

## Transcription

Whisper runs locally and is good enough for a voice note recorded at arm's
length. Local matters more here than for other sources, because voice notes
carry half-formed thoughts and meeting audio carries other people's words.

Expect names and technical terms to come out wrong. Correct them at ingest, not
later, while you still remember what you said.

## Voice notes are drafts, not sources

A voice note is you thinking out loud, with false starts and abandoned
sentences. Ingesting it verbatim produces an incoherent source page.

Treat the transcript as raw input to a single idea:

```
This is a voice note, my own thinking out loud. Extract the actual idea, drop
the false starts and repetition, and write it as one short concept page in my
words. If there are two unrelated ideas, make two pages. Keep the recording date.
```

## Meetings

Meetings produce three things worth keeping and a great deal that is not: the
decisions, the commitments with owners, and the open questions.

```
This is a meeting transcript. Extract decisions made, commitments with who owns
each one, and open questions. Link every person mentioned to their entity page.
Skip discussion that did not lead anywhere.
```

Route the commitments into the relevant project's `Inputs/` rather than the
wiki. A commitment is work, not knowledge, and it goes stale in a week. The
[two layers](../01-concepts/two-layers.md) page covers why that separation
matters.

## Consent and other people

Recording other people has legal requirements that vary by jurisdiction, and
they are not a formality. Some places require every participant to consent.

Separately from legality: a meeting transcript contains other people's
unguarded words. Keep those out of any vault you might share, and think about
whether the meeting needs to be in the knowledge layer at all, or whether the
three extracted decisions are enough.

## Next

[Newsletters and email](newsletters-and-email.md)
