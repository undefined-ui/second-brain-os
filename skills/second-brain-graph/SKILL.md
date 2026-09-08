---
name: second-brain-graph
description: >-
  Analyse the vault's link graph and report on its shape: orphan rate, average
  degree, components, hubs, bridges and clusters, with what each number means for
  retrieval. Use this skill when the user asks about the health or structure of
  their graph, wants metrics, asks which pages are most connected or most
  isolated, or asks whether the vault is fragmented. Do NOT use for fixing what
  it finds, which is second-brain-lint, or for answering a content question.
---

# Analyse the graph

The graph is the search space every answer is drawn from. Its shape decides
whether retrieval reaches the relevant material in a few hops or reaches nothing.

## Core rule

Report shape and what it means, never fix anything. This skill is read-only.

## Workflow

1. **Run the scripts** rather than reading files: `scripts/vault_stats.py` for
   counts and degree, `scripts/link_check.py` for orphans and breaks,
   `scripts/graph_export.py` when deeper analysis is wanted.
2. **Compute the four metrics:** orphan rate, average degree, component count,
   stale-page rate.
3. **Identify hubs** (pages that have swallowed the graph) and **bridges**
   (pages connecting otherwise separate clusters).
4. **Name the clusters.** These are what the vault is actually about, which is
   reliably different from what the user would say it is about.
5. **Say what each number means** for answering questions, not just the value.

## Output format

```
Pages <n> | links <n> | avg degree <n>
Orphan rate <n>%      (healthy under 5)
Components <n>        (main holds <n>%)
Stale concepts <n>%   (untouched 90+ days)

Hubs: <pages with outsized degree, and whether to split them>
Bridges: <pages connecting clusters, and what breaks if they are wrong>
Clusters: <what the vault is actually about>

What this means: <two or three sentences>
```

## Calibration

Never report page count or word count as a health signal. Both rise whether the
vault is improving or not.

A single reading says little. If the user has recorded previous numbers, compare
against them; if not, suggest recording these.
