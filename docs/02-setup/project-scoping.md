# Project scoping

This is the step that most setups skip and then wonder why output quality drops
as the vault grows.

When the agent is pointed at the whole vault, every task competes with
everything you have ever saved. It reads a root `CLAUDE.md` covering your entire
life, plus whatever else it decides is relevant. Answers get broader and
shallower.

When it is pointed at one project, it reads that project's `CLAUDE.md`, sees
that project's files, and does the job in front of it.

## How to scope

In Obsidian, click the vault name in the bottom left, then:

**Manage vaults → Open folder as a vault → pick your project folder → Trust**

From a terminal, the same thing is just:

```bash
cd ~/brain/projects/youtube-channel
claude
```

The agent now reads only that project's instructions.

## When to use which

**The full vault** for anything that spans domains: planning, review, asking
what you know about a topic, weekly maintenance, ingestion. The knowledge layer
is the whole point of a wide view.

**A single project** for producing anything: drafting, building, analysing this
week's numbers. Narrow context, one goal, no drift.

The rough rule: the full vault plans, a single project ships.

## Passing knowledge into a project

Scoping down cuts the agent off from the wiki, which is usually what you want
and occasionally not. Two ways to bridge it:

- Link the relevant concept pages from the project's `CLAUDE.md`, and copy the
  handful that genuinely matter into the project's `Inputs/`.
- Or run the research question against the full vault first, save the answer
  into the project's `Inputs/`, then scope down and work.

The second is better. It keeps the decision about what matters with you, which
is the part you should not be delegating.

## Next

[Live data connectors](live-data.md)
