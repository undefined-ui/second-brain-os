# Graph metrics worth tracking

Four numbers, checked monthly. Their direction over time tells you whether the
system is working, which is not obvious from using it day to day.

```bash
python3 scripts/vault_stats.py ~/brain
```

## Orphan rate

Pages with no inbound links, as a share of all pages.

The single most diagnostic number in the vault. A rising orphan rate means
ingestion is writing pages without connecting them, which is the exact failure
mode that turns a wiki back into a folder.

Under five percent is healthy. Over fifteen and something is broken in the
ingest instructions, not in your habits.

## Average degree

Links per page.

Below two, the graph is barely connected and retrieval cannot do better than
search. Between three and eight is the working range for a personal vault. Much
above ten, check whether links are being added decoratively, which inflates the
number while making the graph less useful.

Watch it alongside page count. Degree that stays flat while the vault doubles is
fine; degree that falls means new pages are attaching to less than the existing
ones did.

## Component count

How many disconnected islands.

Ideally one large component holding most pages, plus a few genuinely separate
topics. If the main component holds less than about eighty percent of pages, the
vault is fragmented and answers will be systematically incomplete without
anything appearing wrong.

## Stale page rate

Concept pages whose `updated` date is older than ninety days, as a share of
concept pages.

Some staleness is correct: a well-written page on a settled idea does not need
touching. But a vault where most concept pages have not been touched in months
while sources keep arriving means new material is landing in new pages instead
of updating existing ones. That is how you end up with four pages about one
thing.

```dataview
TABLE updated FROM "wiki/concepts"
WHERE updated < date(today) - dur(90 days)
SORT updated ASC
```

## What not to track

Page count and word count. Both go up regardless of whether the vault is getting
better, which makes them satisfying and useless. A vault that doubled its pages
while doubling its orphan rate got worse.

## Recording them

Append the four numbers to a note monthly. Trend is the information; a single
reading tells you almost nothing, and you will not remember what last quarter's
orphan rate was.

## Next

[Agents](../06-agents/README.md), for running all of this without you.
