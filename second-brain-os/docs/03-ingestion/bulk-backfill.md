# Backfilling years of material

At some point you will want to import everything: the bookmark folder, the
downloads directory, three years of chat history, the read-later queue with
eight hundred unread items.

This is the run that goes wrong. It is expensive, it takes hours, and done in
the wrong order it produces a wiki that reads like a pile rather than a
structure. It is also the run that makes the vault genuinely useful in one
sitting, so it is worth doing carefully.

## Order matters

Process oldest first.

The reason is that later sources should update pages that earlier sources
created. Run it that way and the wiki records how your understanding developed:
the early page on a topic, then the correction, then the current position.

Run it newest first and every old source arrives as a contradiction to be
reconciled against a page that already has the final answer. The agent spends
its work reconciling, the history comes out inverted, and you lose the one thing
this structure gives you over a search index.

## Batch, always

Ten sources per batch. After each batch: update `index.md`, append to `log.md`,
commit, report.

```
/backfill raw/archive/2024
```

The `backfill` command in [`commands/`](../../commands/README.md) works this
way and stops between batches for a go-ahead.

Batching exists for three reasons. Cost stays visible while you can still stop.
Quality stays checkable, so you catch a bad page contract on page ten rather
than page four hundred. And a crash costs you one batch instead of the run.

## Check the first batch properly

Read every page the first batch produced. All of them.

This is the moment to catch systematic problems: pages that are summaries rather
than explanations, concepts that are too granular, links that are decorative,
frontmatter that is wrong. Fix `CLAUDE.md` and re-run the batch before
continuing.

A flaw you let through in batch one is a flaw in four hundred pages by the end,
and fixing it afterwards costs more than the original run.

## Cost control

Backfilling a thousand sources is a real bill. Ways to keep it sane:

- **Filter first.** Most archives are half dead links and things you saved and
  never opened. Have the agent triage titles before ingesting anything.
- **Cap the batch size** and watch what the first few cost before scaling.
- **Skip the archive tier.** Not everything needs a wiki page; leaving material
  in `raw/` still leaves it searchable.

## Dead links

Old bookmark exports are full of pages that no longer exist. Check before
ingesting rather than discovering it halfway:

```bash
python3 -c "import sys,urllib.request as u;[print(l.strip()) for l in sys.stdin]"
```

For anything valuable that is gone, the Internet Archive usually has a copy.
Clip from there and note in the frontmatter that the original is dead, because a
source page whose URL 404s is unverifiable a year later.

## Resuming

Record progress in `log.md` as you go, one line per batch with the folder and
range covered. When the run stops halfway, and it will, you resume from the log
instead of guessing which files were done.

## After the backfill

Run a full lint. A large import always leaves orphans, near-duplicates and
broken links.

```
/lint
```

Then run a review to see what the vault now contains, because after a backfill
it knows things you have forgotten you saved. That moment is the payoff for the
whole exercise.

## Next

[Structuring](../04-structuring/README.md), for the rules that decide what all
these pages actually look like.
