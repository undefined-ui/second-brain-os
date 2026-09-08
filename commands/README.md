# commands

Seventy-two slash commands for Claude Code, grouped by what you are doing.

```bash
cp commands/*.md ~/brain/.claude/commands/
```

Commands are thin on purpose: each one points at a skill and sets its scope. The
behaviour lives in the skill, so `/ingest-youtube` and a scheduled task and you
asking in plain language all produce the same result.

Most take an optional argument. With none, they default to the sensible whole:
`/lint` audits everything, `/ingest` takes whatever is waiting in `raw/`.

### Ingestion

| Command | What it does |
|---|---|
| `/ingest` | Ingest new material from raw/ into the wiki |
| `/ingest-url` | Clip and ingest a web page |
| `/ingest-youtube` | Ingest a video or podcast transcript |
| `/ingest-pdf` | Ingest a PDF |
| `/ingest-paper` | Ingest an academic paper |
| `/ingest-chats` | Import an exported chat history |
| `/ingest-voice` | Ingest a voice note |
| `/ingest-newsletter` | Ingest newsletters without duplicating |
| `/ingest-highlights` | Ingest book or article highlights |
| `/backfill` | Bulk import an archive in batches |

### Structuring

| Command | What it does |
|---|---|
| `/link` | Find and add missing connections |
| `/dedupe` | Find near-duplicate pages |
| `/merge` | Merge two pages |
| `/rename` | Rename a page and fix every link |
| `/split` | Split an overloaded page |
| `/retype` | Fix a page's type |
| `/schema` | Check frontmatter against the schema |
| `/tags` | Audit the tag vocabulary |
| `/aliases` | Find missing aliases |
| `/contradictions` | List unresolved contradictions |
| `/index` | Rebuild the index |

### Graph

| Command | What it does |
|---|---|
| `/graph` | Report the shape of the graph |
| `/graph-export` | Export the graph for outside analysis |
| `/orphans` | Find unreachable pages |
| `/hubs` | Find pages that swallowed the graph |
| `/bridges` | Find the pages holding the graph together |
| `/clusters` | Show what the vault is actually about |
| `/typed-links` | Add relation types where they matter |
| `/stale` | Find concept pages nobody has touched |

### Retrieval

| Command | What it does |
|---|---|
| `/ask` | Ask a question answered only from the vault |
| `/know` | What do I know about a topic |
| `/connect` | Find the path between two ideas |
| `/compare` | Compare two things from your own sources |
| `/sources` | Show what a claim rests on |
| `/gaps` | What is missing from my understanding |
| `/contradicts` | Argue against me |
| `/timeline` | How my sources developed over time |
| `/trace` | Show which pages an answer used |
| `/changed-my-mind` | What I have revised |

### Maintenance

| Command | What it does |
|---|---|
| `/lint` | Audit structure and repair what is mechanical |
| `/health` | Quick health check |
| `/metrics` | Record a dated metrics snapshot |
| `/review` | Periodic review of what the vault learned |
| `/weekly` | The weekly review |
| `/monthly` | The monthly structural review |
| `/prune` | Find what is safe to remove |
| `/archive` | Move cold material out of the wiki |
| `/commit` | Commit the current state with a useful message |

### Outputs

| Command | What it does |
|---|---|
| `/outline` | Outline a piece from your concept pages |
| `/draft` | Draft from the vault |
| `/report` | Write a research report |
| `/publish` | Check what is safe to publish |
| `/export` | Export a page or set of pages |
| `/quiz` | Test yourself on your own pages |
| `/explain` | Explain it back and find the gaps |
| `/ingest-mine` | Ingest your own finished work |

### Projects

| Command | What it does |
|---|---|
| `/project` | Create a project |
| `/project-status` | Where a project stands |
| `/decisions` | List decisions made |
| `/commitments` | List open commitments |
| `/handoff` | Prepare a handoff brief |
| `/scope` | Pull knowledge into a project |

### Safety

| Command | What it does |
|---|---|
| `/privacy` | Audit what should not be in the vault |
| `/secrets` | Scan for credentials |
| `/dry-run` | Preview a run without writing |
| `/rollback` | Undo the last run |
| `/audit` | Audit what an agent did |

### Setup

| Command | What it does |
|---|---|
| `/init` | Scaffold a new vault |
| `/claude-md` | Build or update your CLAUDE.md |
| `/install` | Install the skills, commands and agents |
| `/doctor` | Check the setup is working |
| `/schedule` | Set up scheduled maintenance |

## Why so many

Nine of these do the real work and the rest are scoped entry points into the same
skills. That is the point: you should not have to remember how to phrase a
request for a thing you do every week.

If a command you want is missing, it is usually one line pointing at an existing
skill. Copy the closest file and change the scope.
