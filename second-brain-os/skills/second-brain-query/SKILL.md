---
name: second-brain-query
description: >-
  Answer a question from a second-brain vault by reading its own pages, citing
  the pages used, and saying plainly when the vault does not contain the
  answer. Use this skill whenever the user asks what they know about a topic,
  what they have read on something, what connects two ideas, what they have
  changed their mind about, or asks any question that should be answered from
  their own notes rather than general knowledge. Do NOT use for ingesting new
  material, for general questions the vault has nothing to do with, or when the
  user explicitly wants an answer from the open web.
---

# Query the vault

A query that quietly falls back on general knowledge is the most damaging thing
this system can do. The owner built the vault so answers would be grounded in
what they actually read, and an answer that blends the model's priors with
their notes is worse than no answer, because it cannot be checked.

## Core rule

Every claim in the answer comes from a page in the vault and names that page.
Anything you know but the vault does not is labelled as outside knowledge or
left out.

## Workflow

1. **Start from `index.md`**, not from a full-text sweep. The index is the map;
   reading it first keeps the context budget for actual pages.
2. **Follow links outward** from the most relevant pages, one hop at a time.
   Stop when new pages stop adding anything.
3. **Answer in plain language**, with `[[page]]` references inline.
4. **Name the gaps.** If the question has three parts and the vault covers two,
   say which one it does not.
5. **Offer the next move** when there is an obvious one: a source worth
   ingesting, a synthesis page worth writing.

## Output format

Plain prose, then:

```
Read: <pages consulted>
Not covered: <what the vault does not answer>
```

## Calibration

Reading too little is the common failure: answering from three pages when the
vault has fifteen relevant ones. Reading everything is the opposite failure and
burns the budget on pages that add nothing.

If the vault has nothing on the topic, say so in one sentence and stop. Do not
pad the answer with general knowledge to avoid an empty result.
