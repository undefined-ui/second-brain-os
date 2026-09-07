# Git, sync and backups

A vault is a folder of text files, which makes it close to an ideal git
repository, and git is what makes an agent safe to run unattended.

Without version control, a bad run is a mystery. With it, every change the agent
made is a diff you can read and revert in one command.

```bash
cd ~/brain
git init
git add .
git commit -m "initial vault"
```

## What to ignore

```
.obsidian/workspace*
.obsidian/cache
.DS_Store
.trash/
```

Commit the rest of `.obsidian/`, so your plugin list and settings travel with
the vault. Never commit API keys; the Local REST API key lives in plugin data,
so check what `.obsidian/plugins/` contains before the first push.

If any part of the vault is private, keep the remote private. A second brain is
one of the highest-signal documents about a person that exists.

## Commit around agent runs

Commit before a big ingest and after it. Then a bad batch is
`git checkout .` rather than an afternoon of manual repair. Scheduled tasks
should commit their own work with a message naming the run, so the history stays
readable months later.

## Sync across machines

- **Git remote:** free, versioned, works everywhere, needs a pull and push
  habit.
- **Obsidian Sync:** paid, end-to-end encrypted, handles mobile properly.
- **Generic cloud drives:** work, with a caveat. A sync client rewriting files
  while an agent writes them produces conflict copies. If you go this route,
  keep long-running agent work to one machine.

## Backups

Sync is not backup. Sync propagates a bad delete to every device.

Keep one copy that is not connected to the sync path: a periodic archive to
external storage or a separate remote. Test a restore once, before you need it.
The failure mode you are protecting against is not disk death, it is an
automation that quietly rewrote two hundred pages three weeks ago.

## Next

The vault is set up. Go to [Ingestion](../03-ingestion/README.md) to start
feeding it, or [Structuring](../04-structuring/README.md) for the rules that
decide what the pages look like.
