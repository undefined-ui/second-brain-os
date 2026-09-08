---
name: second-brain-transcript
description: >-
  Clean a raw transcript before ingestion: punctuate, paragraph, label speakers,
  fix mistranscribed technical terms, and split long recordings by topic. Use
  this skill when the user drops an auto-generated transcript, subtitle file,
  podcast or lecture transcript, meeting recording text, or asks to process a
  video or audio source. Do NOT use for text that is already prose, for
  summarising a transcript, or for the ingestion itself.
---

# Clean a transcript

Concept pages built from unpunctuated caption dumps are noticeably worse,
because the model spends its attention reconstructing sentence boundaries
instead of understanding claims.

## Core rule

Clean, never summarise. Nothing is cut. This is a formatting pass on the record,
and the record has to stay faithful.

## Workflow

1. **Punctuate and paragraph.** Sentence boundaries first, then paragraphs at
   topic shifts.
2. **Label speakers** where they change. In an interview this is most of the
   value.
3. **Fix technical terms.** Auto-captions mangle proper nouns and jargon
   consistently. Flag anything you could not resolve rather than guessing.
4. **Keep coarse timestamps** every few minutes, so a claim on a wiki page can
   be verified in ten seconds instead of a rewatch.
5. **Propose split points** if the recording covers separate topics. A
   three-hour podcast is not one source.
6. **Write frontmatter:** title, channel or speaker, URL, date.

## Output format

The cleaned transcript, then:

```
Cleaned: <source>
Speakers labelled: <n>
Terms corrected: <list>
Uncertain: <list of what could not be resolved>
Suggested splits: <topics with timestamps, or none>
```

## Calibration

Never drop filler that carries meaning, such as hedging or a speaker correcting
themselves. Those are exactly what distinguish a claim from an aside.

If the transcript is too garbled to clean reliably, say so and recommend
re-pulling it rather than producing a plausible reconstruction.
