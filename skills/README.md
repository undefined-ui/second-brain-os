# skills

Agent skills for running the vault. They are plain `SKILL.md` files, so they
work with Claude Code, and with any other agent that supports the Agent Skills
format.

| Skill | What it does | When it fires |
|---|---|---|
| `second-brain-ingest` | Raw source into linked wiki pages | New material lands in `raw/` |
| `second-brain-lint` | Structural audit and repair | Weekly, or after a bulk import |
| `second-brain-query` | Answers grounded in your own pages | You ask the vault something |
| `second-brain-review` | Periodic review of what changed | Weekly or monthly |

## Install

Copy the folders into your skills directory:

```bash
cp -r skills/* ~/.claude/skills/
```

Or keep them inside the vault at `.claude/skills/` so they travel with it and
get versioned alongside your notes.

## Editing them

These are opinionated. The linking rules in `second-brain-ingest` and the
citation rule in `second-brain-query` are the two that matter most; loosen
those and the vault degrades into a folder of summaries. Everything else is
fair game to adapt.
