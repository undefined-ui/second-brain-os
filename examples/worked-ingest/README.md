# A worked ingest: one article in, the exact pages that came out

One source went into an empty copy of `vault-template/` and the
`second-brain-ingest` skill was run on it once. Everything under this folder is
what came out, unedited: the wiki pages, the index and log diffs, and the
output of `scripts/vault_stats.py` and `scripts/link_check.py` before and
after. Where the result is weaker than the skill's own description, the numbers
are left as they are.

## Setup

The vault was built exactly as the README Quickstart says, into a temporary
folder instead of `~/brain`:

```bash
cp -r second-brain-os/vault-template brain
mkdir -p brain/.claude
cp -r second-brain-os/skills   brain/.claude/skills
cp -r second-brain-os/commands brain/.claude/commands
cp -r second-brain-os/agents   brain/.claude/agents
cp -r second-brain-os/scripts  brain/scripts
rm brain/.claude/*/README.md brain/scripts/README.md
```

The source is the one the skill uses in its own example, Karpathy's `llm-wiki`
gist, saved as `raw/karpathy-llm-wiki.md`:

```bash
curl -sL https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ \
  -o brain/raw/karpathy-llm-wiki.md
```

The file is not copied into this folder, because it is someone else's text;
the download above reproduces it. What was ingested: 11,985 bytes, 75 lines,
1,959 words, md5 `7953122eebc7aca33db25cd86a89a19a`. Note that this is the bare
gist body with no URL or date line at the top, which is not what Obsidian Web
Clipper would have produced; that shows up in the result below.

Before the run the vault had the two template pages (`before/`).

## The run

Claude Code 2.1.291, model `claude-fable-5-1`, 2026-10-19. The command was
`/ingest raw/karpathy-llm-wiki.md`, which is `commands/ingest.md`: it tells
the agent to follow the `second-brain-ingest` skill.

One deviation to be aware of. The run was not `cd brain && claude` followed by
`/ingest`. The headless `claude -p` on the machine used was logged out, so the
ingest was executed by a Claude Code subagent started from another session,
pointed at the vault folder, and told to follow only the vault's `CLAUDE.md`,
the skill file and the command file. Same skill text, same vault, same model
family; a different launcher. The agent's final report is in
`after/agent-report.txt`, verbatim. Wall time 217 seconds, 10 tool calls,
142,707 tokens including cache reads, as reported by the harness.

## What came out

Nine new pages and two updated ones. The skill's own example for this very
source predicts "3 new, 3 updated, 11 links" into a vault that already has
pages for Obsidian and Claude Code; into an empty vault it produced:

| | before | after |
|---|---|---|
| pages (`vault_stats.py`) | 2 | 11 |
| words | 75 | 3,260 |
| links (`vault_stats.py`) | 0 | 72 |
| links (`link_check.py`) | 0 | 44 |
| links (agent's own report) | | 41 |
| avg degree | 0.00 | 6.55 |
| orphans | 0 | 0 |
| broken links (`link_check.py`) | 0 | 12 |

New pages, with word counts from `wc -w`:

| page | type | words |
|---|---|---|
| `wiki/sources/LLM Wiki (Karpathy).md` | source | 1,192 |
| `wiki/concepts/LLM wiki.md` | concept | 508 |
| `wiki/concepts/Retrieval-augmented generation.md` | concept | 305 |
| `wiki/concepts/Memex.md` | concept | 246 |
| `wiki/entities/Obsidian.md` | entity | 190 |
| `wiki/entities/qmd.md` | entity | 142 |
| `wiki/entities/Claude Code.md` | entity | 140 |
| `wiki/entities/Andrej Karpathy.md` | entity | 125 |
| `wiki/entities/Vannevar Bush.md` | entity | 93 |

`after/index.diff` and `after/log.diff` are `git diff` of the two files the
template ships. The log got the one line `CLAUDE.md` asks for. The index was
filled in all four sections plus three entries under Gaps.

## What worked

- The source page keeps claims attributable ("the source says") as `CLAUDE.md`
  requires, and the three concept pages each say explicitly which of their
  sections no source in the vault covers, instead of filling the gap.
- Nothing was written to `raw/`; the file's md5 is unchanged after the run.
- Index and log were updated in the same run. Zero orphans.
- The agent noticed that the raw file carries no author line and no URL, and
  wrote the attribution as the filename's claim rather than the file's. That is
  the correct behaviour under `CLAUDE.md`; it also means the source page has an
  empty `url:` and `published: unknown`, which a clipped page with a header
  would not have had.

## What did not

- Three concept pages from one idea file is the top of the skill's own
  calibration band ("one to three concepts worth their own page"). Memex and
  Retrieval-augmented generation are each built from a single paragraph of the
  source, and both pages say so themselves. A stricter run would have kept
  them inside the source page.
- The source page is 1,192 words for a 1,959-word source. It is a faithful
  claim-by-claim restatement, not a summary. Whether that is the right length
  is a judgement call; the skill text does not set one.
- The three repo scripts and the agent disagree on how many links exist in the
  same vault: 72 (`vault_stats.py`), 44 (`link_check.py`), 41 (agent).
  `vault_stats.py` counts every occurrence of a wikilink that resolves to
  another page; `link_check.py` keeps one entry per (page, target) pair, so a
  target linked twice from the same page counts once. Both include
  `index.md`. The agent's number is distinct page-to-page links excluding
  `index.md`, which is what the skill's "Links added" line asks for. If you track
  "links added" week over week, pick one counter and stay with it.
- `link_check.py` reports 12 broken links. All 12 are occurrences of the three
  pages the agent listed under Gaps in `index.md` (Obsidian Web Clipper, Marp,
  Dataview), which `CLAUDE.md` explicitly allows. The script has no notion of a
  declared gap, so after a run that follows the rules, `/health` will still
  show red until the gap pages are written or the links removed.
- The source page lists each entity link twice (once in the body, once in the
  closing Links section), which is why the per-occurrence counters are higher
  than the per-page ones.

## Reproducing

```bash
cd brain
python3 scripts/vault_stats.py .  > before-stats.txt
python3 scripts/link_check.py .   > before-links.txt
claude   # then: /ingest raw/karpathy-llm-wiki.md
python3 scripts/vault_stats.py .  > after-stats.txt
python3 scripts/link_check.py .   > after-links.txt
```

Running it again will not give the same pages; it is a model, not a script.
The structure (one source page, a handful of concept and entity pages, index
and log touched) should be stable; the page count and wording will move.
