# Hooks

Hooks fire on events rather than on a schedule. They are the right tool for
things that must happen every time, which is exactly the set of things a prompt
instruction will eventually miss.

## Worth hooking

**Validation before a write.** Check frontmatter parses and required fields are
present. A malformed page caught at write time is a non-event; caught a month
later it is a page that has been invisible to every query since.

**Lint after a run.** Broken links appear at the moment they are created, which
is the moment there is enough context to fix them properly.

**Commit after a scheduled run.** Removes the possibility of a run that changed
forty files and left no commit.

**Notify on deletion.** Any delete, any time, surfaces. Deletions are rare enough
that a notification costs nothing and matters when it fires.

## Not worth hooking

Anything slow. A hook that runs on every file write and takes two seconds turns a
forty-page ingest into a ninety-second pause, and you will disable it.

Anything that needs judgement. Hooks are mechanical checks. A hook trying to
decide whether a page is good enough will be wrong in both directions.

## Keep them fast and quiet

A hook should complete in well under a second and print nothing when it passes.
Hooks that log on success train you to ignore hook output, which is the same as
having no hooks the day one fails.

## Failure behaviour

Decide explicitly whether a failing hook blocks the operation.

Validation hooks should block: a page that fails schema validation should not be
written. Notification hooks should not: a failed notification is not a reason to
lose the work.

The bad case is a blocking hook that fails for an unrelated reason and silently
stops your scheduled ingest for a week. Whatever blocks must be simple enough
that it only fails for the reason it exists.

## Next

[Skills and slash commands](skills-and-commands.md)
