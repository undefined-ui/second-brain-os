---
name: second-brain-metrics
description: >-
  Record a dated snapshot of the vault's health numbers and compare against
  previous snapshots so trends are visible. Use this skill for a monthly or
  quarterly check, when the user asks whether the vault is improving, or asks to
  track its numbers over time. Do NOT use for a one-off graph analysis, which is
  second-brain-graph, or for structural repairs.
---

# Record metrics

A single reading tells you almost nothing. Direction over months is the
information, and nobody remembers what last quarter's orphan rate was.

## Core rule

Four numbers, appended to a dated log, compared against the last entry. Never
page count or word count.

## Workflow

1. **Run** `scripts/vault_stats.py` and `scripts/link_check.py`.
2. **Record:** orphan rate, average degree, component count, stale-concept rate,
   with the date and total pages for context.
3. **Append** to the metrics note. Never overwrite previous entries.
4. **Compare** against the last snapshot and name what moved.
5. **Interpret only what changed.** A stable number needs no commentary.

## Output format

```
<date> | pages <n>
orphan rate    <n>%   (<+/-n> since <date>)
avg degree     <n>    (<+/-n>)
components     <n>    (main <n>%)
stale concepts <n>%   (<+/-n>)

Moved: <what changed and the likely cause>
Watch: <the one number to fix, or none>
```

## Calibration

A rising orphan rate with a rising page count means ingestion has stopped
linking. That is the single most important pattern in this report and it should
be called out explicitly, not left in the numbers.

Do not recommend more than one thing to fix. A metrics report with five action
items gets ignored.
