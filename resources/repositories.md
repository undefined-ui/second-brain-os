# Repositories

Graph, retrieval and memory projects worth knowing. Stars from the GitHub API,
September 2026. For agent skills see [skills.md](skills.md); for Obsidian
plugins see [plugins.md](plugins.md).

## GraphRAG and graph retrieval

| Repo | Stars | What it is |
|---|---|---|
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 39,467 | Dual-layer graph plus vectors, aimed at cheap incremental updates. EMNLP 2025. Since [1.5.7](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.7) (September 2026) it can build the graph first and add vectors later |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 35,875 | The reference implementation of the [paper](papers.md) |
| [gusye1234/nano-graphrag](https://github.com/gusye1234/nano-graphrag) | 3,983 | The same idea in about 1,100 readable lines. Open this one to understand the pipeline |
| [OSU-NLP-Group/HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | 3,985 | The NeurIPS'24 paper's implementation. Personalised PageRank over a knowledge graph |
| [DEEP-PolyU/Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | 2,635 | Curated map of surveys, benchmarks and projects in the area |

## Agent memory

Adjacent problem, same techniques. These give an agent persistent memory; this
guide gives a person a knowledge base. Worth reading for the retrieval design
even if you never run one.

| Repo | Stars | What it is |
|---|---|---|
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 64,863 | Drop-in memory layer for agents and apps |
| [getzep/graphiti](https://github.com/getzep/graphiti) | 30,680 | Real-time temporal knowledge graphs for agents |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 30,568 | Turns data into knowledge graphs, combining graph and vector retrieval |
| [doobidoo/mcp-memory-service](https://github.com/doobidoo/mcp-memory-service) | 1,928 | Persistent memory over MCP, REST API plus knowledge graph |

## RAG frameworks

If you decide your vault has outgrown files. See [adding RAG when you need
it](../docs/07-retrieval/rag-on-top.md) for the threshold, which most personal
vaults never reach.

| Repo | Stars | What it is |
|---|---|---|
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 90,216 | Full RAG engine with document understanding |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 52,058 | Document agent and ingestion framework |
| [neuml/txtai](https://github.com/neuml/txtai) | 12,931 | Embeddings database and LLM workflows, small enough to read |

## MCP

| Repo | Stars | What it is |
|---|---|---|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 94,575 | The index of MCP servers |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 90,141 | The official reference servers, including filesystem and memory |
| [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | 4,376 | Third-party MCP server for Obsidian over the REST plugin |

Since the Local REST API plugin now ships its own MCP server, a separate one is
optional. See [MCP for Obsidian](../docs/02-setup/mcp-obsidian.md).

## New in October 2026

Released or shipped a major version between September and October 2026. Stars
from the GitHub API on 1 November 2026.

| Repo | Stars | What it is |
|---|---|---|
| [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) | 4,445 | A local MCP server whose knowledge graph is plain markdown with typed `relation [[WikiLink]]` lines, indexed into SQLite. Reads and writes Obsidian vaults. 1.0 shipped on 29 October. AGPL-3.0 |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | 14,856 | A Rust memory server whose source of truth is a git-backed wiki of ordinary `.md` files, fed by hooks from 20+ agent harnesses. 3.0 (13 October) installs as a Claude Code plugin marketplace. MIT |
| [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory) | 4,306 | One markdown file per memory under a `MEMORY.md` index. The SQLite and BM25 index is a cache you can delete and rebuild, and Claude Code and Codex share one store. MIT |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | 57,739 | The database-backed alternative: retain, recall and reflect over vector, BM25, graph and time search, with knowledge pages it can write out as markdown. 1.0 on 13 October. MIT |
| [vshulcz/deja-vu](https://github.com/vshulcz/deja-vu) | 1,408 | Indexes the JSONL and SQLite transcripts 43 coding agents already write to disk into a local FTS5 store, with hooks, MCP and a git-committed `.deja/memory.jsonl` file. MIT |
| [decodingai-magazine/llm-wiki-workshop](https://github.com/decodingai-magazine/llm-wiki-workshop) | 43 | A self-paced workshop: three exercises, each a working system, from a basic `raw/` to `wiki/` setup to a wiki that learns from queries. MIT |
| [LadybugDB/ladybug](https://github.com/LadybugDB/ladybug) | 1,895 | An embedded, serverless Cypher graph database, formerly Kuzu, which was archived in October 2025. 0.22 on 25 October. MIT |
| [google-research/harness2](https://github.com/google-research/harness2) | 21,920 | Harness², recursive harness tuning: the weights stay frozen while prompts, tools and memory are edited per task and the lessons kept. Apache-2.0 |
| [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) | 3,620 | Four opt-in add-ons for the Pi harness that keep its score with 45 to 49 per cent less token traffic. MIT |

## How to judge one of these

**Does it own your data or read it?** Anything that reads your markdown and
writes derived output is safe to try and safe to abandon. Anything that becomes
the only place a piece of knowledge lives has taken the portability you chose
markdown for.

**Is it maintained?** Check the last push date, not the star count. This
ecosystem produces a lot of repos in the weeks after a popular gist, and most
stop within a month.

**Are the stars measuring the right thing?** For plugins, installs are the
better signal, and the two diverge by an order of magnitude in places.
