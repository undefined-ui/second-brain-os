# scripts

Small, dependency-free Python scripts. Everything here reads the vault as
plain files, so nothing breaks if you switch editors or agents.

| Script | What it does |
|---|---|
| `link_check.py` | Broken wikilinks, orphan pages, stubs |
| `vault_stats.py` | Page counts, link density, orphan rate, most-linked pages |
| `graph_export.py` | Wikilink graph as CSV edges or GraphML for Gephi |
| `chat_export_to_md.py` | Chat history export into per-conversation markdown |

```bash
python3 scripts/vault_stats.py ~/second-brain
python3 scripts/link_check.py ~/second-brain
python3 scripts/graph_export.py ~/second-brain graph.graphml --format graphml
```

The agent can do all of this in natural language, but a script gives the same
answer every time and costs nothing to run, which is what you want for anything
you check weekly.
