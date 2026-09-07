# Skills and slash commands

Two mechanisms that look similar and do different jobs.

**A skill** teaches repeatable behaviour. It loads when relevant and shapes how
the agent does something, whether you invoked it explicitly or just described the
task.

**A command** is a shortcut for a task you run often. It points at a skill and
saves you typing the instructions.

The behaviour belongs in the skill. That way ingestion works the same whether it
was triggered by `/ingest`, by a scheduled task, or by you saying "add this to my
vault".

## What this repo ships

Four skills in [`skills/`](../../skills/README.md): ingest, lint, query, review.
Five commands in [`commands/`](../../commands/README.md), each a few lines
pointing at a skill.

Install them inside the vault at `.claude/skills/` and `.claude/commands/` so
they are versioned alongside your notes and travel with the vault.

## Writing your own

A skill worth writing has three properties: you do it repeatedly, you have
opinions about how, and the opinions are not obvious enough for the model to
guess.

Structure that works:

```markdown
---
name: skill-name
description: >-
  What it does. When to use it, written pushy, because agents under-trigger
  skills. Do NOT use for the tempting near-misses.
---

# Name

[Why this skill exists: what failure it prevents. This paragraph is the rubric
for every case the rules below do not cover.]

## Core rule
## Workflow
## Output format
## Calibration
## Example
```

The opening paragraph does more work than the rules. Rules cover the cases you
thought of; the reason covers the rest.

## Explain the why

"Never overwrite a contradiction" gets applied literally and fails on the edge
cases. "Never overwrite a contradiction, because the history of what you believed
is the thing this vault has that a search engine does not" generalises to
situations you never described.

All-caps NEVER without a reason is usually a missing explanation.

## Versioning

Skills live in the vault, so git tracks them. When output quality changes, the
skill diff is the first place to look.

Test a skill on three or four real cases before letting a scheduled task use it.
A flaw in a skill that runs nightly is a flaw in three hundred pages by the end
of the year.

## Next

[Guardrails](safety-and-guardrails.md)
