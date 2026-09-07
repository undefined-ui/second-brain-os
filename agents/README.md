# agents

Subagent definitions for Claude Code. Copy into `.claude/agents/` in your
vault.

| Agent | Writes | Runs |
|---|---|---|
| `ingestor` | yes | when material lands in `raw/` |
| `linker` | links only | after imports, or weekly |
| `reviewer` | no | weekly |
| `researcher` | no | on demand |

Two of the four are read-only by design. Splitting write access this way means
a bad research run cannot damage the vault, and it keeps the git history
readable: every content change traces back to an ingest or a link pass.

See [scheduling](../docs/06-agents/scheduled-maintenance.md) for wiring these
to a cadence.
