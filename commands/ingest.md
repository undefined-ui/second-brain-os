---
description: Ingest new material from raw/ into the wiki
---

Process uningested sources in `raw/`.

$ARGUMENTS is an optional file path. With no argument, find every file in
`raw/` that has no corresponding page in `wiki/sources/` and process them
oldest first.

Follow the `second-brain-ingest` skill. Stop and report if more than twenty
files are pending, so the owner can decide on batching rather than discovering
a large bill afterwards.
