---
name: second-brain-review
description: >-
  Produce a periodic review of a second-brain vault: what was added, which
  topics are growing, what contradicts what, which questions are still open,
  and what is worth reading next. Use this skill whenever the user asks for a
  weekly or monthly review, asks what changed in their vault, what they have
  been learning about lately, or what they should look at next, and when a
  scheduled review task fires. Do NOT use for structural linting, for ingesting
  sources, or for answering a specific factual question.
---

# Review the vault

Capture systems fail at the point where nothing comes back out. A review is the
loop that closes: it turns a week of ingestion into something the owner reads
and acts on, and it is what makes the vault feel alive rather than archival.

## Core rule

A review reports on the vault, not on the agent's activity. Nobody needs to
know how many tool calls ran; they need to know what they now know.

## Workflow

1. **Diff the period.** New and updated pages since the last review, from
   `log.md` and frontmatter dates.
2. **Find the clusters.** Which concepts gained the most links. That is where
   the owner's attention actually went, which is often not where they think it
   went.
3. **Surface contradictions** recorded during the period and still unresolved.
4. **List open questions** from concept and synthesis pages.
5. **Find the neglected.** Pages linked often but thin, or gaps in `index.md`
   that keep getting referenced.
6. **Recommend three things to read or write next**, each tied to a specific
   page.

## Output format

```
## Week of <date>

Added: <n> pages, <n> sources ingested

### Where your attention went
<two or three sentences on the clusters>

### Unresolved
<contradictions and open questions, each linked>

### Thin spots
<pages that are referenced more than they deserve given their content>

### Next
1. <specific action tied to a page>
2.
3.
```

## Calibration

Reviews that list everything get skimmed and then ignored. Keep it under a
page. Three recommendations, not ten. If a week produced nothing worth
reporting, say that in one line instead of manufacturing insight.
