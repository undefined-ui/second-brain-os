# Web articles

Articles are the bulk of what most people save, and the browser is where the
decision to save happens. Anything that requires switching windows loses.

## Obsidian Web Clipper

The [official extension](https://obsidian.md/clipper) from the Obsidian team.
Chrome, Firefox, Safari, Edge, Brave and Arc. It extracts the readable content
of a page using Mozilla Readability, the same engine behind Firefox Reader View,
and saves it as markdown straight into your vault.

Install it, open the settings, and set the destination folder to `raw/`.

## Template

The default template saves the page body. Add frontmatter so the agent knows
what it is holding without re-reading the whole file:

```
---
title: {{title}}
source: {{url}}
author: {{author}}
published: {{published}}
clipped: {{date}}
type: article
---

{{content}}
```

`{{author}}` and `{{published}}` come back empty on plenty of sites. That is
fine, an empty field is better than a guessed one, and the agent handles the
gap by saying the source is undated rather than inventing a date.

## What to clip

Clip what you would want to find again in a year: primary sources, engineering
posts, papers, documentation, arguments you disagree with and want to answer
later.

Skip news that will be stale in a week, listicles, and anything you are saving
out of guilt. Every low-value page you ingest costs twice: once at ingest, and
again every time the agent reads past it looking for something else.

The honest test at clip time is whether you can name what you would ask this
source later. If you cannot, do not clip it.

## Awkward pages

- **Paywalls.** The clipper saves what the browser rendered. If you can read it,
  it can save it. If you cannot, it saves the paywall notice, so check before
  moving on.
- **Documentation sites.** Clipping page by page is a losing game. Save the
  entry point and let the agent fetch the rest, or clone the docs repo into
  `raw/` if it is open source.
- **Single-page apps and dynamic content.** Readability sometimes returns a
  fragment. Look at the file before ingest.
- **Threads and comment sections.** The value is usually in the replies, which
  the clipper drops. Copy the thread manually or screenshot it into
  `raw/assets/`.

## Clip now, ingest later

Clipping and ingesting are separate steps on purpose. Clip freely during the
day, run `/ingest` in one batch later, because ingesting one source at a time
gives the agent no chance to spot that three things you saved this week are
about the same idea.

## Next

[YouTube and podcasts](youtube-transcripts.md)
