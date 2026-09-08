---
name: second-brain-merge
description: >-
  Merge two pages that describe the same thing, preserving every distinct claim,
  redirecting inbound links, and recording the merge. Use this skill when the
  user approves a duplicate merge, says "these are the same page", "merge X into
  Y", or asks to clean up near-duplicates that a lint run proposed. Do NOT use
  to merge pages on your own judgement, to delete a page outright, or to split
  one page into several.
---

# Merge duplicate pages

A merge is irreversible in the way that matters: afterwards you cannot tell
which claim came from which page. Two ideas that look identical from their
summaries are often a general case and a specific one.

## Core rule

Never merge unprompted. Propose, wait for approval, then follow the procedure
exactly.

## Workflow

1. **Pick the survivor** by canonical name, not by which page is longer.
2. **Merge content.** Every distinct claim survives with its source. Overlapping
   claims collapse; differing ones both stay, following the contradiction rules.
3. **Merge aliases,** including the dead page's title as an alias on the
   survivor. This is what keeps old links and the user's memory working.
4. **Redirect inbound links** to the survivor. Check every backlink.
5. **Delete the old page,** or leave a stub only if it was linked from outside
   the vault.
6. **Record in `log.md`:** both names, the date, and why.

## Output format

```
Merged: [[old]] -> [[survivor]]
Claims kept from old page: <n>
Aliases added: <list>
Inbound links redirected: <n>
Conflicts recorded: <none | description>
```

## Calibration

If the two pages disagree about anything factual, that is a signal they may not
be duplicates. Surface the disagreement and ask before proceeding.

Never merge a page marked `maintained_by: human` into another without explicit
confirmation naming that page.
