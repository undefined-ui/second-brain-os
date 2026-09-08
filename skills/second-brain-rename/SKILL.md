---
name: second-brain-rename
description: >-
  Rename a page safely: update the file, fix every inbound wikilink, add the old
  name as an alias, and log it. Use this skill whenever a page needs a different
  canonical title, the user says "rename X to Y", asks to fix an inconsistent
  title, or after a lint run flags naming problems. Do NOT use for merging two
  pages, for moving a page between folders without a name change, or for
  renaming files outside the wiki.
---

# Rename a page

An agent renaming a file directly is the single most common source of broken
links in an agent-maintained vault. Obsidian fixes links when you rename inside
the app; writing the file directly does not.

## Core rule

A rename is four operations, not one. All four, or none.

## Workflow

1. **Check the new name** against existing pages and aliases. A rename that
   collides with an existing alias creates ambiguity the graph cannot resolve.
2. **Rename the file** and update the `title` in frontmatter.
3. **Add the old title to `aliases`.** This keeps external references, the
   user's memory, and any link you miss working.
4. **Update every inbound link.** Search the whole vault, including `index.md`.
5. **Log it:** old name, new name, links updated.
6. **Verify** with a link check.

## Output format

```
Renamed: [[old]] -> [[new]]
Inbound links updated: <n> across <n> pages
Alias added: <old>
Remaining references: <none | list>
```

## Calibration

Do not rename to fix a style preference on a page with many inbound links. The
cost is real and the benefit is cosmetic.

If the correct name is genuinely ambiguous, ask rather than picking. A second
rename is more disruptive than the first.
