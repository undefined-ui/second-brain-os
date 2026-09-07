# The failures everyone hits

## The vault stalls after two weeks

Almost always capture, not the system. Clipping takes three clicks instead of
one, or the phone has no path into the vault, so material stops arriving and
there is nothing to process.

Fix the capture path, not the vault. See
[Ingestion](../03-ingestion/README.md).

The other cause is expecting the payoff too early. At thirty pages there is
nothing to connect. See [what good looks
like](../01-concepts/what-good-looks-like.md) for the real timeline.

## Pages are summaries of summaries

Source pages that summarise the article, concept pages that summarise the source
pages. Each layer loses information and the bottom layer is what gets read.

The cause is a page contract that says "summarise" anywhere in it. Concept pages
explain an idea in plain language, in your words, standing on their own. Rewrite
the contract in `CLAUDE.md` and re-ingest a few sources to check.

## The agent rewrites work you did by hand

Infuriating and preventable. Mark hand-written pages in frontmatter:

```yaml
maintained_by: human
```

And in `CLAUDE.md`: never rewrite a page marked `maintained_by: human`, only
append links and flag issues for the owner.

## Ingest quality drops as the vault grows

Real, and the cause is usually context. Ingesting into a vault of three hundred
pages means the agent should be checking what exists first, and if it is not, it
creates new pages instead of updating.

Check that ingestion reads `index.md` before writing. That one step is what keeps
quality flat as the vault grows.

## Everything connects to everything

A few hub pages have accumulated every link, so the graph says nothing. Split
the hubs into the specific ideas people are actually linking to. See [linking
rules](../04-structuring/linking-rules.md).

## You stopped opening it

The honest failure. Usually capture broke months ago and the vault has been
static, or the review is too long to read.

Both are fixable. Neither is a reason to start over with a different tool, which
is the instinct and always costs another month.

## Next

[The agent writes garbage](agent-writes-garbage.md)
