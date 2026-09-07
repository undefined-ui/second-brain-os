# commands

Slash commands for Claude Code. Copy them into `.claude/commands/` inside your
vault:

```bash
cp commands/*.md ~/second-brain/.claude/commands/
```

Then `/ingest`, `/ask`, `/lint`, `/review` and `/backfill` are available in any
session started in the vault.

Commands are thin on purpose: each one points at a skill. The behaviour lives
in the skill, so it stays consistent whether it was triggered by a command, by
a schedule, or by you asking in plain language.
