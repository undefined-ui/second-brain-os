# Privacy

A mature second brain is one of the highest-signal documents about a person that
exists. Everything you read, worked on, worried about and asked, connected and
indexed.

That is the point, and it is the reason to be deliberate about what goes in and
where it lives.

## Decide at capture, not later

Redaction after ingest does not work. By the time you decide something should not
be there, it has propagated into concept pages, links and synthesis pages, and
removing it means finding all of them.

Decide before the file lands in `raw/`. See [chat
exports](../03-ingestion/chat-exports.md), which is where this bites hardest,
because chat history contains more than any other source and is imported in bulk.

## What does not belong

**Credentials of any kind.** Not because the agent leaks them, but because the
vault gets synced, committed, backed up and occasionally shared. Every copy is
another place the key exists.

**Other people's private information.** Meeting transcripts, personal messages,
anything told to you in confidence. Your notes are not the right home for
someone else's confidences, and they did not consent to being ingested.

**Material you are contractually bound to keep confidential.** Client work under
NDA in a vault that syncs to a personal cloud account is a real exposure.

## Separate vaults over careful filtering

If you have material that must not mix, use a separate vault rather than tags or
folders inside one.

A single vault with a private section relies on every query, every export and
every publish step respecting the boundary. Two vaults cannot leak into each
other, and the cost is having to pick which one to open.

## Local models for sensitive material

If a category of material should not leave your machine at all, a local model
handles ingestion for that vault. Quality is lower than a frontier model, which
is the trade.

Worth it for medical, legal or financial material. Usually not worth it for
articles about software.

## Publishing

Explicit opt-in only. See [publishing and
export](../08-outputs/publishing-and-export.md).

## Before sharing a vault

Search it for keys, run through the frontmatter for personal identifiers, and
read the log for what was ingested from where. Once shared, it is out, and the
graph makes it easy for a reader to assemble a picture you did not intend to
give.

## Next

[Scaling past a thousand pages](scaling.md)
