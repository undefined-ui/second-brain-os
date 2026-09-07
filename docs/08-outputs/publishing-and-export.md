# Publishing and export

Some of your vault is worth showing to other people. Most of it is not, and the
mechanics of that split are worth setting up before you publish anything.

## Deciding what is public

The simplest reliable approach is an explicit opt-in: a `publish: true` field in
frontmatter, and nothing without it ever leaves.

Opt-out is the alternative and it is a mistake. Under opt-out, one forgotten flag
publishes something private, and the failure is silent and permanent because it
is already indexed.

## Static site options

Obsidian Publish is the official route and the least work. Quartz and Obsidian
Digital Garden are the common open-source ones, both build a static site from a
vault and both understand wikilinks and backlinks, which matters because a
published wiki with broken links is worse than a blog.

Whatever you use, check what happens to a link pointing at an unpublished page.
It should degrade to plain text rather than to a 404.

## Publishing a subset safely

The pattern that works: a build step copies only `publish: true` pages into a
separate folder, rewrites links to unpublished pages as plain text, and builds
from that copy.

Never point a publishing tool at your live vault directly. One misconfigured
include pattern publishes everything, and there is no way to unpublish something
that was crawled.

## What publishing does to your writing

A public wiki changes how you write pages, and not entirely for the better. You
start writing for an audience: hedging more, explaining more, keeping tentative
thoughts out.

Tentative thoughts are exactly what a personal vault is for. If you publish,
consider keeping the private vault primary and publishing a deliberately selected
subset, rather than making the whole thing public and unconsciously sanitising
it.

## Other exports

PDF and HTML for a single report, straight from markdown with pandoc. Fine for
sharing one document.

Do not export the vault as a whole to any format you cannot regenerate. The
markdown is the artifact.

## Next

[Learning from your own vault](teaching-yourself.md)
