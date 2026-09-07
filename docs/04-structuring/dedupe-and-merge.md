# Deduplication and merging

Duplicates are inevitable. Two sources use different words for the same idea, an
alias was missing, a bulk import ran before the vault had the concept. The
question is not how to prevent them entirely but how to catch them before they
both accumulate links.

## Finding them

Signals, in order of reliability:

- **Similar titles.** Cheap to check, catches the plural and acronym cases.
- **Overlapping aliases.** Two pages claiming the same alias is always a bug.
- **Shared inbound links.** Two pages that the same five sources both link to
  are usually one page.
- **Content similarity.** Expensive, but catches the cases where the names look
  unrelated.

`second-brain-lint` runs the first three and proposes merges. It does not
perform them, which is deliberate.

## Why merging is not automatic

A merge is irreversible in the way that matters: once two pages are one, you
cannot tell which claim came from which, and the agent's judgement about "these
are the same thing" is exactly the judgement that goes wrong.

Two ideas that look identical from their summaries are often a general case and
a specific one, and merging them loses the distinction permanently.

So: the agent proposes, you decide. Reviewing a merge takes fifteen seconds.

## The procedure

When you approve one:

1. **Pick the survivor** by canonical name, not by which is longer.
2. **Merge content,** keeping every distinct claim with its source. Overlapping
   claims collapse, differing ones both stay.
3. **Merge aliases,** including the dead page's title as an alias on the
   survivor.
4. **Redirect inbound links** to the survivor.
5. **Leave a stub** at the old path only if it was linked from outside the
   vault. Otherwise delete it.
6. **Record it in `log.md`** with both names, so a page that vanishes is
   traceable.

Step 6 is the one agents skip and the one you will need. A page that disappears
without a record is indistinguishable from a page that was deleted by mistake.

## Do not dedupe live

Merging during an ingest run means the agent is restructuring the vault while
adding to it, and a bad merge lands in the middle of otherwise good work.

Run dedupe as its own pass, weekly or after a large import, on a clean git
state. Then a wrong merge is one `git checkout` away from undone.

## Next

[Contradictions and supersession](contradictions-and-supersession.md)
