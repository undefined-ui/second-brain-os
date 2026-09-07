# Skills and implementations

Agent skills that run this pattern, and open-source builds worth reading before
writing your own.

## In this repo

Four skills in [`skills/`](../skills/README.md): ingest, lint, query, review.
Five commands in [`commands/`](../commands/README.md). Four subagent definitions
in [`agents/`](../agents/README.md), two of them read-only by design.

All plain `SKILL.md` files, so they work with any agent that reads the Agent
Skills format, not only Claude Code.

## Community implementations

Reading someone else's page contracts is the fastest way to improve your own.
These are worth opening even if you never install them.

- **[Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki)**.
  The pattern packaged as a single installable skill for Claude Code, Cursor and
  Codex. Ingest into `raw/`, compile into `wiki/`, cited answers, lint. Includes
  a design spec and a list of what the author deliberately did not build, which
  is the most useful section in it.
- **[micuintus/llm-wiki](https://github.com/micuintus/llm-wiki)**. A deliberately
  minimal skill: no dependencies, no JSON metadata, convention-based guardrails
  rather than code-based ones. Good counterpoint to the heavier
  implementations, and its README lists several others in the same family.
- **[NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain)**.
  Four skills installable through npm, close to the original gist, with a setup
  wizard.
- **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)**.
  Around 43 ready commands, works across Claude, Codex and Gemini. The author's
  write-up of what the gist leaves undefined is worth reading alongside it.

Two more get recommended often and are worth a look if the above do not fit:
`AgriciDaniel/claude-obsidian`, which ships role presets, and
`coleam00/second-brain-starter`, which interviews you and generates a plan
before building anything.

## Writing your own

The format is a `SKILL.md` with frontmatter and a body. The four in this repo
follow a consistent shape: why the skill exists, one core rule, a workflow, an
output template, calibration, and a worked example.

Two authoring rules that matter more than the rest. Explain the reason behind
every rule, because rules cover the cases you thought of and reasons cover the
rest. And name the near-misses where the skill should not fire, because
over-triggering is what makes people uninstall skills.

Details in [skills and commands](../docs/06-agents/skills-and-commands.md).
