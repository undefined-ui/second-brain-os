---
name: second-brain-project
description: >-
  Set up or update a project in the vault: the four-stage folder pipeline, a
  project-scoped CLAUDE.md with one goal, and links to the concept pages it
  depends on. Use this skill when the user starts something new they will work on
  over time, says "create a project", "set up a folder for X", or asks to define
  the goal and structure of ongoing work. Do NOT use for one-off tasks, for wiki
  pages about a topic, or for scoping an existing project down to work in it.
---

# Set up a project

The knowledge layer answers what you know. The project layer answers what you
are doing this week. Merging them fills a wiki with dead task lists and buries
working files under conceptual notes.

## Core rule

One goal per project, stated in its own `CLAUDE.md`. A project with three goals
is three projects.

## Workflow

1. **Interview if needed.** What this produces, for whom, by when, and what the
   agent's role is. Vague answers produce a file that makes every future session
   worse.
2. **Create the folders:** `Inputs/`, `Process/`, `Outputs/`, `Feedback/`.
3. **Write the project `CLAUDE.md`:** what this is, the one goal with a date,
   your role, working rules, current state. Name what the agent should not do
   here as well.
4. **Link the knowledge layer.** Find concept pages the project depends on and
   reference them from the project file. Copy into `Inputs/` only the few that
   genuinely matter.
5. **Register it** in the root `CLAUDE.md` project list.

## Output format

```
Project: <name>
Goal: <one measurable outcome with a date>
Folders created: Inputs, Process, Outputs, Feedback
Concept pages linked: <list>
Agent role: <one line>
```

## Calibration

`Feedback/` is the folder people skip and the one that makes the system improve.
If the user has no idea what would go in it, that is worth surfacing: it usually
means the goal is not measurable yet.

Do not create a project for work that finishes this week. That is a task.
