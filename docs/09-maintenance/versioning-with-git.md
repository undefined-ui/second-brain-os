# Versioning

Git is what makes an agent safe to run unattended. Without it, a bad run is a
mystery; with it, every change is a diff you can read and revert in one command.

## Commit granularity

One commit per run, with the run named:

```
ingest 2026-09-07: 4 sources, 9 pages
lint 2026-09-07: 3 broken links, 1 merge
```

Not one commit per file, which buries the history, and not one commit per week,
which makes reverting a single bad run impossible without losing the good ones.

Scheduled tasks commit their own work as part of the run. See
[scheduling](../06-agents/scheduled-maintenance.md).

## Reading diffs of generated pages

Worth doing in the first weeks, and occasionally after.

You are looking for two things: pages that changed when they should not have,
and rewrites where an update was expected. An agent quietly rewriting a page it
was asked to append to is the kind of behaviour that only shows up in a diff.

`git log --stat` after a week tells you which pages your automation touches most,
which is usually informative.

## Reverting

```bash
git revert HEAD          # undo one run, keep the history
git checkout .           # discard uncommitted work
git checkout HEAD~3 -- wiki/concepts/some-page.md   # one page back
```

The middle one is the reason to commit before any large operation. A backfill
that went wrong halfway costs you the run rather than the vault.

## Branches

Worth it for experiments that touch structure: a new page contract, a schema
change, a bulk re-ingest under different instructions.

```bash
git checkout -b new-schema
```

Run it, read the result, merge or delete the branch. Doing this on `main` and
deciding afterwards is how vaults end up in a half-migrated state that nobody
wants to finish.

## What not to commit

`.obsidian/workspace*`, caches, and anything containing a key. The Local REST API
key lives in plugin data, so check `.obsidian/plugins/` before the first push.

Keep the remote private unless you have deliberately made the vault public.

## Next

[Backups and portability](backups-and-portability.md)
