# FAQ

**Do I need MCP?**

No. Claude Code started inside the vault folder reads and writes it directly.
MCP adds the ability to reach the vault from sessions not running in it, which
matters mainly for scheduled tasks. See [MCP for
Obsidian](../02-setup/mcp-obsidian.md).

**Does this work with agents other than Claude Code?**

Yes. The vault is markdown and the skills are `SKILL.md` files, a format several
agents read. Anything that can read and write files in a folder can maintain the
vault; the instructions in `CLAUDE.md` may need renaming for other tools.

**How much does it cost to run?**

Depends entirely on volume. A daily ingest of a handful of articles is small. A
one-time backfill of a thousand sources is not, which is why the
[backfill](../03-ingestion/bulk-backfill.md) page insists on batches with visible
costs.

**Can I use a local model?**

For ingestion of sensitive material, yes, with lower quality. Local models are
weaker at the judgement calls that matter here: what deserves its own page, when
two sources genuinely disagree. A workable split is a local model for private
material and a frontier model for everything else.

**Do I need Obsidian?**

No. The vault is a folder of markdown files. Obsidian is a good viewer for the
graph and has the Web Clipper, which is the strongest practical reason to use it.
Logseq, Foam, or a plain editor all work.

**What if I already have a Notion or Evernote full of notes?**

Export to markdown, drop it in `raw/`, and backfill oldest first. Expect the
export to be messy. Fix extraction before ingesting rather than hoping the agent
copes.

**How is this different from a memory feature?**

Memory features remember facts about you across sessions and belong to the tool.
This is a body of knowledge you own as files, that outlives the tool, and that
you can read, edit and publish yourself.

**Will the agent make things up?**

It can, which is why every rule in [structuring](../04-structuring/README.md) is
about attribution: claims recorded as claims, sources attached, gaps stated
rather than filled. A page with no source behind a specific number is the thing
to watch for.

**Is the graph view actually useful or is it just pretty?**

The global view is mostly pretty. The local graph is genuinely useful as a
five-second quality check on any page. See [reading the graph
view](../05-graphs/obsidian-graph-view.md).

**How long before it is worth it?**

Weeks two to four for the first real payoff, month six for the state people
describe as the whole point.

---

Something missing here? Open an issue.
