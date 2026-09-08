---
name: second-brain-changed-my-mind
description: >-
  Trace where the user's recorded position on something has shifted: superseded
  claims, contradictions between sources of different dates, and what evidence
  moved them. Use this skill when the user asks what they have changed their mind
  about, how their thinking on a topic developed, what they used to believe, or
  wants a quarterly look back at their own positions. Do NOT use for finding
  contradictions between sources with no time dimension, or for a current-state
  answer.
---

# Trace changed positions

This is the query a vault can answer that nothing else can, and the reason the
supersession rules exist. It only works because contradictions are recorded
rather than overwritten.

## Core rule

Report the change with both positions, both dates and the evidence between them.
A conclusion without its history is just the current claim.

## Workflow

1. **Find superseded claims** across concept pages, and contradictions where the
   sources differ in date.
2. **Reconstruct the sequence:** what the page said, when, based on what; what
   changed it, when.
3. **Distinguish real revision from correction.** A factual error being fixed is
   not a change of mind. A conclusion being revised on better evidence is.
4. **Flag unresolved ones.** Contradictions still sitting open are the most
   actionable output here.
5. **Say how firm the current position is,** based on what moved it.

## Output format

```
## <topic>
Was: <claim> (<source>, <date>)
Now: <claim> (<source>, <date>)
What moved it: <evidence>
Firmness: <what would move it again>

## Still unresolved
<contradictions with no current position>
```

## Calibration

If nothing has changed in the period, say so in one line. Manufacturing an
apparent revision from two pages that never disagreed is worse than an empty
result.

Never present the more recent source as correct by virtue of being recent.
