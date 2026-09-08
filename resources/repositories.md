# Repositories

Graph, retrieval and memory projects worth knowing. Stars from the GitHub API,
September 2026. For agent skills see [skills.md](skills.md); for Obsidian
plugins see [plugins.md](plugins.md).

## GraphRAG and graph retrieval

| Repo | Stars | What it is |
|---|---|---|
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 39,467 | Dual-layer graph plus vectors, aimed at cheap incremental updates. EMNLP 2025 |
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
