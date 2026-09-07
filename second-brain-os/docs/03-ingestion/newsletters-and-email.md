# Newsletters and email

Newsletters are the easiest source to automate and the easiest to over-ingest.
Automate the capture, then be strict about what gets a wiki page, because a feed
that files itself will happily fill your vault with a hundred pages a month that
you never asked for.

## A dedicated address

Make an address that exists only for the vault, and resubscribe your newsletters
to it. That single move separates the material you want to keep from everything
else in your inbox, and it means automation never touches your real mail.

From there, forward that address into `raw/` with whatever automation you
already use. Any rule that can write a file works.

## Deduplicate

Newsletters repeat themselves. The same launch appears in four different digests
in the same week, each with the same facts and a different opening line.

Ingested straight, you get four source pages saying one thing and a concept page
citing all four as if that were corroboration. Cross-references between
newsletters are not independent confirmation, and a wiki that treats them as
such will overstate how well established something is.

Instruct the ingest explicitly:

```
These are newsletters. Several will cover the same item. Group them by topic
first, write one source page per actual item citing every newsletter that
mentioned it, and note where they disagree. Do not treat repetition across
newsletters as confirmation.
```

## What deserves a page

Newsletters are mostly links with commentary. The commentary is rarely worth a
concept page; the thing being linked sometimes is.

The useful pattern is to let the agent read the digests and hand you a shortlist:

```
Read this week's newsletters in raw/newsletters/. List anything worth reading in
full, with one line on why. Ingest nothing yet.
```

Then clip the two or three primary sources properly and ingest those. The
newsletter did its job as a filter, and the vault ends up with the actual source
instead of a summary of it.

## Regular email

Most email should not be in a second brain. Threads about scheduling, receipts,
back and forth about logistics: none of it is knowledge, all of it is volume.

Worth ingesting: threads where a real decision was made or something was
explained properly. Route those in by forwarding to the capture address, one
thread at a time, deliberately.

Never wire your whole inbox into `raw/` on a schedule. It ingests everything
about everyone you correspond with, most of it not yours to keep.

## Next

[Backfilling years of material](bulk-backfill.md)
