---
name: second-brain-quiz
description: >-
  Generate questions from the user's own concept pages so they can find out what
  they saved but never learned, and compare their answers against what the pages
  say. Use this skill when the user wants to test themselves, revise, make
  flashcards from their notes, or asks what they have forgotten. Do NOT use for
  generic quizzing on a topic the vault does not cover, or for answering a
  question from the vault.
---

# Quiz from your own pages

Reading something is not learning it. A vault of well-written pages nobody
revisits is a library, and libraries do not make anyone knowledgeable.

## Core rule

Questions come from the user's pages, at the depth those pages record. Never
from general knowledge about the topic.

## Workflow

1. **Pick the scope:** a topic, a cluster, or pages updated recently.
2. **Write questions of two kinds:** recall of what the page states, and
   application of the idea to a new case.
3. **Withhold answers** until the user has attempted them.
4. **Grade against the page, not against what is true.** If they answered
   correctly but the page says otherwise, that is a page problem worth
   surfacing.
5. **Report the gaps:** which pages they could not answer from. Those are things
   saved and never learned.

## Output format

```
<n> questions from <n> pages

1. <question>
...

[after answers]
Solid: <topics>
Shaky: <topics, with the pages to reread>
Page problems found: <pages that are unclear or wrong>
```

## Calibration

Keep it to a handful of pages that matter. Quizzing everything ever saved is a
job, not a habit.

A page that cannot generate a good application question is usually a page that
records the source's wording rather than an understanding of it. Say so.
