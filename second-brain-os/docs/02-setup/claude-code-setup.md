# Claude Code in the vault

Claude Code is the half that reads and writes. Two ways to run it, and the
choice only affects where you type, not what happens.

## Option A: the desktop app

Download Claude Desktop from [claude.com/download](https://claude.com/download)
and sign in. The app has a **Code** tab, which is Claude Code without a
terminal. If you have never used a command line, start here.

## Option B: the terminal

Install Claude Code and run `claude` from inside the vault folder:

```bash
cd ~/brain
claude
```

Started this way, the agent reads and writes the vault directly through the
filesystem, with no plugin and no MCP server involved. This is the simplest
possible setup and it is enough for everything in the ingestion, structuring
and retrieval sections of this guide.

Installation instructions for each platform are in the [official setup
docs](https://code.claude.com/docs/en/setup).

## Plan requirement

Claude Code needs a paid account: Pro, Max, Team, Enterprise, or a Console
account billed per token. The free Claude.ai plan does not include Claude Code
access, per Anthropic's own setup documentation. If the Code tab prompts you to
upgrade, that is why.

## Filesystem or MCP

Both work. The difference is narrow and worth knowing before you pick:

| | Filesystem | MCP |
|---|---|---|
| Setup | none, just `cd` into the vault | plugin plus a config command |
| Obsidian open | not required | required, the plugin serves the API |
| Scope | whatever folder you started in | the whole vault, from anywhere |
| Failure mode | none to speak of | plugin off, app closed, wrong port |

Start on the filesystem. Move to [MCP](mcp-obsidian.md) when you want the agent
to reach the vault from sessions that are not running inside it, which mostly
matters once you add scheduled tasks.

## First run

Point it at the structure before asking for anything else:

```
Read CLAUDE.md and wiki/index.md, then tell me what this vault currently
contains and what is missing.
```

The answer tells you immediately whether the agent understood its instructions.
If it starts inventing a structure you did not ask for, your `CLAUDE.md` is too
vague. See [writing your CLAUDE.md](claude-md.md).

## Permissions

The agent will ask before editing files. Grant it write access to the vault and
nothing else. Do not grant blanket shell access on a folder that holds anything
you cannot lose, and read [guardrails](../06-agents/safety-and-guardrails.md)
before you automate anything on a schedule.

## Next

[MCP for Obsidian](mcp-obsidian.md)
