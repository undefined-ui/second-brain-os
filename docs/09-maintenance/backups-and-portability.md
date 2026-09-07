# Backups and portability

## Sync is not backup

This is the whole page, and it is the mistake almost everyone makes.

Sync propagates. If an automation rewrites two hundred pages badly, sync
faithfully copies the damage to every device within seconds. If a file is
deleted, it is deleted everywhere.

Backup means a copy that does not follow. At least one, disconnected from the
sync path.

## A workable arrangement

**Git remote,** private, pushed after every run. Versioned, so it covers the
"what did it look like three weeks ago" case that a file backup does not.

**Sync** for working across machines, whichever kind you already use.

**A periodic archive** to external or separate cloud storage, not connected to
either of the above. Monthly is enough.

Three copies, one of which is dumb and slow, is the arrangement that survives the
failure modes that actually happen.

## Test a restore

Once. Take the archive, restore it somewhere else, open it in Obsidian, and check
the links work.

Untested backups fail at a reliably bad moment, and the common failure is not
corruption. It is discovering that the archive excluded a folder, or captured the
vault mid-sync in a half-written state.

## What you are protecting against

Not disk failure, which is rare and which sync handles.

The real risk is an automation that quietly did something wrong three weeks ago,
which you notice now. That needs history, which is why git carries more of the
load here than file backups.

## Portability

The vault is markdown and wikilinks, so leaving any particular tool costs
nothing structural. What is worth checking occasionally:

**Nothing important lives outside the files.** Plugin-specific metadata, canvas
files, database exports. All fine as extras, none of it should carry knowledge
that exists nowhere else.

**Links resolve without Obsidian.** `scripts/link_check.py` verifies this, since
it parses wikilinks itself.

**The agent instructions are in the vault,** not in a chat history or an app
setting. `CLAUDE.md`, skills and commands travel with the folder.

## Next

[Privacy](privacy-and-secrets.md)
