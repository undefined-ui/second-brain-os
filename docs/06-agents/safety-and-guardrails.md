# Guardrails

The rule this whole section rests on:

**Keys, not prompts.**

Telling an agent not to do something is a preference. It is not a boundary. If
the agent technically can delete a file, empty a folder or send an email, then
one day, in a context you did not anticipate, it will.

Control what is possible at the permission level. Then the instruction in
`CLAUDE.md` is a preference sitting on top of a boundary, rather than the only
thing between your notes and a bad run.

## Scope write access

The agent needs write access to the vault. It does not need write access to your
home directory, and a scheduled task running with broad filesystem permissions is
a large blast radius for a small convenience.

Same principle for connectors: read-only wherever the option exists. A calendar
connector that can only read cannot cancel a meeting, no matter what a
misinterpreted instruction says.

## Never delete without a record

Deletion is the one operation you cannot recover from by reading a diff, because
the content is gone and only the absence remains.

Rule: no page is deleted without a line in `log.md` naming it and why. Merges
count as deletions. Applied consistently, a page that vanishes is always
traceable, and "where did that page go" stops being an unanswerable question.

## Git is the real safety net

Every guardrail above is preventive. Git is what saves you when one fails.

Commit before any run that writes at scale. Scheduled runs commit their own work.
Then a bad ingest is `git checkout .`, and a bad merge is one revert.

Read the diffs from scheduled runs occasionally, especially in the first weeks.
That is how you learn what your agent actually does at 7am, which is reliably
different from what you assumed.

## Dry runs

For anything that touches many files, run it once in report-only mode.

```
Do a dry run: list every page you would create, update or delete, and the links
you would add. Write nothing.
```

The output takes a minute to read and catches misread instructions before they
become four hundred edits.

## Watch for scope creep

Agents extend the job. Asked to ingest, an agent may also tidy an unrelated page,
fix formatting, rename something for consistency. Each is defensible; together
they mean you cannot tell what a run did without reading everything.

Instruct explicitly: do the job asked, list anything else you noticed, change
nothing else.

## What not to put in the vault

Credentials, API keys, anything you are under obligation to keep confidential,
other people's private information.

Not because the agent will leak it, but because the vault is a single file tree
that gets synced, committed, backed up and occasionally shared. Every copy is
another place that content exists. See
[privacy](../09-maintenance/privacy-and-secrets.md).

## Next

[Retrieval](../07-retrieval/README.md), for getting answers out of what all this
built.
