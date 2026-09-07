# Live data connectors

Static notes are half a brain. The other half is what is changing: your
calendar, your inbox, the channels where decisions actually get made.

MCP connects those the same way it connects Obsidian.

## Calendar

```bash
claude mcp add google-workspace uvx workspace-mcp --tools calendar
```

An OAuth sign-in opens in the browser. Grant read access.

Then the vault can act on it:

```
Read my calendar for today, log what I committed to in each meeting into my
tasks project, and flag anything without a clear next step.
```

Email, Slack and Notion connect through their own MCP servers, registered the
same way.

## Grant read, not write

Give every connector the narrowest scope that does the job, and prefer read-only
wherever the option exists. The brain should read your data, not delete it or
send things on your behalf.

## The rule that matters most

**Keys, not prompts.**

Telling an agent "do not delete this" is a suggestion. It is not a safety
setting. If the agent technically can delete a file, empty a folder or send an
email, then one day, in some context you did not predict, it will.

Control what is possible at the permission level: read-only tokens, scoped keys,
separate credentials per connector. Then the instruction in your `CLAUDE.md` is
a preference on top of a boundary, rather than the only thing standing between
your inbox and a bad run.

This applies to your own vault too. See
[guardrails](../06-agents/safety-and-guardrails.md).

## What is worth connecting

Connect the sources where decisions and commitments live: calendar first, then
whichever of email or chat you actually use for work.

Skip the ones that produce volume without signal. A connector that floods the
vault with notifications makes every future query worse, because the agent has
to read past all of it.

## Next

[Plugins worth installing](obsidian-plugins.md)
