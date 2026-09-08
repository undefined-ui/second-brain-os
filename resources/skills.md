# Skills and agents

Counted individually: a repo shipping sixteen skills counts as sixteen, because
that is what you install. Counts were taken by reading each repository's file
tree in September 2026.

## This repo

| Type | Count | Where |
|---|---|---|
| Skills | 18 | [`skills/`](../skills/README.md). One per workflow in the guide |
| Commands | 72 | [`commands/`](../commands/README.md). Scoped entry points into those skills |
| Subagents | 6 | [`agents/`](../agents/README.md). Four of them read-only by design |
| Scripts | 4 | [`scripts/`](../scripts/README.md). Link check, stats, graph export, chat import |

Plain `SKILL.md` files, so they work with any agent that reads the Agent Skills
format.

## Implementations of this pattern

| Repo | Stars | Ships |
|---|---|---|
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 14,706 | 16 skills, 3 subagents. Self-organizing vault with role presets |
| [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | 2,174 | 1 skill covering the full ingest, compile, query, lint loop |
| [ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm) | 1,856 | 13 skills, 4 subagents. A complete starter kit |
| [coleam00/second-brain-starter](https://github.com/coleam00/second-brain-starter) | 768 | 1 skill that interviews you and generates a build plan |
| [NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain) | 704 | 4 skills, npm installer, close to the original gist |
| [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | small | 47 commands across Claude, Codex and Gemini |
| [micuintus/llm-wiki](https://github.com/micuintus/llm-wiki) | small | 1 skill, deliberately minimal, no dependencies. Good counterpoint |

The two at the bottom are small on purpose and still worth reading. Star count
measures reach, not quality, and in this corner of the ecosystem it mostly
measures who posted about it.

## General skill libraries

Not second-brain specific, but this is where the format itself is defined and
where the best-written examples live.

| Repo | Stars | Ships |
|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 282,827 | 14 skills. An agentic skills framework and development methodology |
| [anthropics/skills](https://github.com/anthropics/skills) | 175,035 | 20 skills, 3 subagents. The official reference for the format |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 33,894 | A curated index of 1,000+ community skills |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 53,661 | Commands, hooks, workflows and tooling for Claude Code |

## Graph builders

| Repo | Stars | What it does |
|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 115,697 | A `/graphify` skill that turns any folder of code, docs, PDFs and screenshots into a queryable graph. Every edge labelled extracted or inferred |

Graphify is the one to try first if you already have a full `raw/` folder. It
was built around exactly that problem, it runs locally with deterministic
parsing for code, and it outputs an interactive `graph.html` plus an
Obsidian-openable vault. Its reported token savings are self-reported and depend
heavily on corpus size.

## Writing your own

Three properties make a skill worth writing: you do it repeatedly, you have
opinions about how, and the opinions are not obvious enough for a model to
guess.

Read `anthropics/skills` for the format and one of the small implementations
above for a full worked example. Details in [skills and
commands](../docs/06-agents/skills-and-commands.md).
