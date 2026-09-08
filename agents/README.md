# agents

Six subagent definitions for Claude Code. Copy into `.claude/agents/` in your
vault.

| Agent | Writes | Runs |
|---|---|---|
| `ingestor` | yes | when material lands in `raw/` |
| `linker` | links only | after imports, or weekly |
| `reviewer` | no | weekly |
| `researcher` | no | on demand |
| `graph-analyst` | no | monthly, or when navigation gets hard |
| `curator` | no | quarterly |

Four of the six are read-only by design. Splitting write access this way means a
bad research or analysis run cannot damage the vault, and it keeps the git
history readable: every content change traces back to an ingest or a link pass.

The two that write are also the two with the narrowest instructions. That is not
a coincidence.

See [scheduling](../docs/06-agents/scheduled-maintenance.md) for wiring these to
a cadence.
