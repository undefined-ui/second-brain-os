# Why markdown and plain text

The format looks like a detail. It decides whether the system works.

## Agents handle files better than APIs

An agent reading a folder does what it is best at: reading text and writing text.
No schema to learn, no API to call correctly, no failure mode where a request
half-succeeds.

That reliability compounds over thousands of operations. A pipeline that writes
markdown files fails in ways you can see in a diff; one that writes through an
API fails in ways you find out about later.

## Portability is not theoretical

Every previous notes tool people trusted either shut down, changed pricing, or
made export deliberately awkward.

Plain files remove the question. Your vault opens in any text editor, syncs with
any tool, and works with any agent that reads files. Switch models, switch
editors, switch operating systems, and the vault is unaffected because it was
never in anything.

This matters more than usual here, because a second brain accumulates value over
years. A format that traps you is a format that eventually costs you the whole
thing.

## Wikilinks as a graph format

`[[Page name]]` is a two-character convention that produces a real graph, is
readable as text, and survives every tool that does not understand it, because
in the worst case it is still just words in a sentence.

You can parse it with a regex, which is what `scripts/graph_export.py` does. Try
that with a proprietary block reference format.

## Git works on it

Text diffs. That single property is what makes an agent safe to run unattended:
every change it makes is reviewable, revertible, and attributable to a run.

Binary formats and database-backed apps give you no equivalent. You either trust
the automation completely or you do not automate.

## The limits

Plain text is bad at a few things, and pretending otherwise is how people end up
frustrated.

**Structured queries at scale.** Dataview covers a lot, but past a few thousand
pages, relational questions want a real database. Export the graph rather than
abandoning markdown; see [exporting the
graph](../05-graphs/exporting-your-graph.md).

**Rich media.** Images live beside the text as files, not in it. Diagrams are
attachments.

**Concurrent editing.** Two agents writing the same file conflict in the way
files conflict, which is to say badly.

None of those outweigh portability for a personal vault. All of them are worth
knowing before you hit them.

## Next

[Zettelkasten, PARA, evergreen notes](pkm-lineage.md)
