# Scheduling

Scheduled runs are what make the vault feel alive. You wake up and it has filed
what you clipped, noticed a contradiction, and left you three lines about what
changed.

They are also unattended writes to your notes, so the order matters: get the
[guardrails](safety-and-guardrails.md) right first, then schedule.

## Cadence per job

**Ingest, daily.** Overnight, on whatever accumulated in `raw/` during the day.
Daily is right because a batch gives the agent a chance to notice that three
things you saved are about the same idea. Hourly does not.

**Link, weekly.** Connections need material to connect. Run it after a week of
ingestion.

**Lint, weekly.** After the linker, so it catches what that pass broke.

**Review, weekly.** The one output you actually read. Put it on the morning you
plan.

**Metrics, monthly.** Four numbers appended to a note. See
[metrics](../05-graphs/metrics.md).

## Setting one up

In Claude Desktop, the Schedule tab, then a new task:

```
Frequency:  Daily, 7:00am
Folder:     your vault
Prompt:     File anything new in raw/ into the wiki following CLAUDE.md.
            Link it to existing pages. Update index.md and log.md. Commit
            with a message naming the run. Then write me three lines on
            what changed.
```

Or ask for it in a session: "set up a daily task at 7am that ingests raw/ and
summarises what changed".

From a terminal, `cron` or Task Scheduler calling Claude Code headless works the
same way, and is the better option if you want the run inside a git commit
automatically.

## What a run must produce

Three things, every time.

**A log entry.** Otherwise you cannot audit what happened while you were asleep.

**A commit.** One per run, with the run named in the message. This is what makes
a bad run revertible in one command instead of an evening.

**A report to you.** Even one line. A scheduled task that produces nothing
visible is one you stop trusting and then stop reading.

## Detecting silent failure

The failure mode is not a crash. It is a run that completes and does nothing
useful: the source was empty, the API call failed halfway, the instructions
matched no files.

Two cheap checks. Have the run report counts, not just completion, so "ingested
0 sources" is visible. And look at commit frequency once a month: a week with no
commits from the daily task means it has been failing quietly since Tuesday.

## Start manual

Run each job by hand for a week before scheduling it. You are checking that the
output is good enough to accept without reading it closely, because that is
exactly what scheduling means.

Schedule the ingest last. It is the one that writes most.

## Next

[Subagents and parallel work](subagents.md)
