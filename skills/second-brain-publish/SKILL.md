---
name: second-brain-publish
description: >-
  Prepare a subset of the vault for publishing: check opt-in flags, find private
  material, and report what would leak through links before anything is exported.
  Use this skill when the user wants to publish notes as a site or digital
  garden, asks what is safe to make public, or is setting up an export. Do NOT
  use for exporting a single document, or for running the publishing tool itself.
---

# Prepare to publish

Once something is crawled, it is out. Every check here is cheap; the failure it
prevents is permanent.

## Core rule

Explicit opt-in only. A page publishes because it says `publish: true`, never
because nothing excluded it.

## Workflow

1. **List the opt-in set.** Every page marked for publication.
2. **Follow their links.** A published page linking to a private one either
   leaks the title or produces a dead link. Report both.
3. **Scan for anything that should never ship:** credentials, other people's
   private information, confidential work, personal detail in examples.
4. **Check the frontmatter** for fields not meant to be public, such as
   confidence labels or private source paths.
5. **Report, do not export.** The user runs the build.

## Output format

```
Publishable: <n> pages
Links to unpublished pages: <n>
  [[public page]] -> [[private page]]
Flagged content: <list with reasons>
Frontmatter to strip: <fields>
Verdict: <safe to build | fix these first>
```

## Calibration

Err toward flagging. A false positive costs the user ten seconds; a miss is
permanent.

If the user asks to publish the whole vault, ask what they intend to do about
the private material rather than proceeding.
