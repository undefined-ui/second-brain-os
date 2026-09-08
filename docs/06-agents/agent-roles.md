# Agent roles

One agent doing everything produces mediocre work at every job. The instructions
that make a good ingestor are not the ones that make a good reviewer, and stuffed
into one prompt they dilute each other.

Six roles cover a vault, four of them read-only. The definitions are in
[`agents/`](../../agents/README.md).

## Ingestor

Reads `raw/`, writes wiki pages, links them, updates the index and log. Writes
more than any other role and is the one whose output quality determines
everything downstream.

Its instructions are narrow on purpose: it does not answer questions, does not
restructure existing pages beyond adding links, and does not delete. An ingestor
that reorganises while ingesting produces runs you cannot review, because content
changes and structural changes arrive mixed in the same diff.

## Linker

Finds connections between existing pages that ingestion missed.

Runs after imports and weekly. Adds links, creates nothing, rewrites nothing.
Separating it from the ingestor matters because linking well requires reading
broadly across the vault, which is a different job from reading one source
closely.

Its one rule: a link it adds must be one you would agree with on reading both
pages side by side. A linker optimising for link count degrades the graph while
appearing productive.

## Reviewer

Read-only. Produces the periodic review: what changed, where attention went,
what contradicts what, what to read next.

Read-only is not caution, it is what makes the review trustworthy. A reviewer
that can edit will fix small things as it goes, and then its report describes a
vault that no longer exists.

## Researcher

Read-only. Answers questions from the vault, cites pages, names what is missing.

Also the role you talk to most, and the one that most needs the rule about not
falling back on general knowledge. See the
[query skill](../../skills/README.md).

## Graph analyst

Read-only. Runs the metrics, finds hubs, bridges and clusters, and says what the
numbers mean for retrieval. Monthly.

Separate from the linter because analysis and repair want opposite dispositions:
one should notice everything, the other should touch as little as possible.

## Curator

Read-only. Proposes what to prune, archive or merge, quarterly.

Proposals only, never actions. Deletion is the one operation you cannot recover
from by reading a diff, so it stays a decision the owner makes.

## Roles not worth creating

**A deleter.** Deletion should be a decision you make, executed with a record.
The curator proposes; you dispose.

**A summariser.** Summaries of pages that are already summaries produce a layer
that is less true than what is under it and gets read instead of it.

**A tagger.** Tagging is a five-second judgement made during ingest with full
context. A separate pass has less context and produces worse tags.

## Handoffs

Roles communicate through the vault, not through each other. The ingestor writes
gaps into `index.md`; the linker reads them. The ingestor logs its run; the
reviewer reads the log.

That is deliberate. Files as the interface means any run is inspectable
afterwards, and a role can be replaced without touching the others.

## Next

[Scheduling](scheduled-maintenance.md)
