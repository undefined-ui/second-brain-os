# Plugins worth installing

Obsidian works fine with none of these. Add them when you hit the specific
problem each one solves.

## Local REST API

Required only for the [MCP path](mcp-obsidian.md). Serves your vault over a
local HTTP API so the agent can reach it while Obsidian is open, from any
session.

## Dataview

Queries over frontmatter, rendered inside a note. Worth it once you have enough
pages to want dashboards:

````
```dataview
TABLE updated, tags
FROM "wiki/concepts"
WHERE updated < date(today) - dur(90 days)
SORT updated ASC
```
````

That one lists concept pages nobody has touched in three months, which is the
most useful review query in the vault.

## Templater

Templates with variables and dates, for the page shapes in
[`vault-template/templates/`](../../vault-template/templates/). Useful for the
notes you write by hand. The agent does not need it, it writes frontmatter
directly.

## What to avoid

Plugins that rewrite files in the background. Anything that auto-formats,
auto-sorts frontmatter, or renames on a schedule will fight the agent, and you
will spend an evening working out which of the two mangled a page.

Also avoid heavy graph or dashboard plugins until you have material worth
looking at. An empty vault with fifteen plugins is a procrastination artifact,
not a system.

## Next

[Git, sync and backups](git-and-sync.md)
