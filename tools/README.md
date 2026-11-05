# tools

The site at [secondbrainos.dev](https://secondbrainos.dev/)
is generated from this repository, so it cannot drift from the guide.

## The home page: one graph of the whole site

```bash
pip install markdown
python3 tools/build_graph_site.py   # -> graph-data.js, pages-data.js, pages-zh-cn.js
python3 -m http.server 4173         # then open http://localhost:4173
```

`index.html` draws every section, page, term, skill, command, subagent, script
and resource as a node in a 3D graph, and every real link between them as an
edge. Click a node to fly to it, see what it links to and what links to it, and
open a page in the reader without leaving the graph.

| File | What it is |
|---|---|
| `index.html` | The page shell. Hand-written |
| `assets/site/app.css` | Layout and type. Palette and fonts are the guide's |
| `assets/site/app.js` | The graph, the panels, the reader, search, routing |
| `assets/site/graph-data.js` | Generated: nodes and edges |
| `assets/site/pages-data.js` | Generated: rendered guide pages |
| `assets/site/pages-zh-cn.js` | Generated: rendered Simplified Chinese guide pages |
| `tools/build_graph_site.py` | Builds graph data and both article languages from the markdown |
| `tools/build_translations.py` | Renders Chinese articles with the original page and heading IDs |
| `tools/glossary.json` | The only hand-kept data: the terms on the graph |

`build_graph_site.py` keeps the reading order declared in each section's
`README.md`, resolves every relative link to a page, section or toolkit node,
links commands to the skill they follow, pages to the resources whose URLs they
cite, and terms to the pages that mention them most. Add a term by adding a line
to `glossary.json` and rerunning.

The graph is drawn with [3d-force-graph](https://github.com/vasturiano/3d-force-graph)
and three.js, loaded from jsDelivr at pinned versions. Everything else is in the
repo. Old links such as `index.html#02-setup/claude-md` still open that page.

The builder also stamps every asset URL in `index.html` with a content hash
(`app.js?v=…`), so a fresh page never runs against a cached old script. Rerun it
after editing `app.css` or `app.js` as well, not only after changing the docs.

## The other pages

```bash
python3 tools/extract_site.py   # docs and resources -> site_data.json
python3 tools/build_site.py     # -> resources.html
python3 scripts/build_tree.py   # -> tree.html
```

`resources.html` and `tree.html` are still built the old way. Neither script
touches `index.html`, and neither does `scripts/build_tracks.py`, which now only
keeps the course and handbook READMEs in the declared order.


## Local preview and translations

The generated pages are committed, so a local preview does not need a build:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
# Open http://127.0.0.1:8000
```

The map loads its pinned graph libraries from jsDelivr and needs WebGL. The
resource catalog and component tree can also be opened directly from the preview.

All three pages share an English / Simplified Chinese switch. A saved choice
wins over the browser's preferred language; a Chinese browser preference selects
Simplified Chinese, and other languages fall back to English. The choice is
stored locally under `sbos:language`.

| File | Translation responsibility |
|---|---|
| `assets/site/i18n.js` | Locale selection, English fallback, shared interface messages and DOM translation |
| `assets/site/i18n.css` | Shared language switch styling |
| `assets/site/graph-i18n.js` | Chinese graph navigation labels and glossary metadata, keyed by stable node IDs |
| `assets/site/catalog-i18n.js` | Resource catalog, component tree and graph grouping messages |
| `assets/site/resource-i18n.js` | Chinese resource descriptions, keyed by the original resource name |
| `docs/zh-CN/` | Complete Chinese articles, section indexes and local SVG diagrams |

Translations cover the interface, navigation, glossary, tool and resource
descriptions, and all 130 reader articles. Switching languages also changes
article text, headings, tables, captions, diagrams and the source link. Search
matches both languages. Product names, executable code and external references
retain their original forms. English source articles remain unchanged.

Chinese Markdown mirrors the English directory structure under `docs/zh-CN/`.
When updating an article, translate every prose section and keep its heading
levels, lists, tables, code blocks and link destinations aligned with the source.
Local links to translated documents and diagrams stay within the Chinese tree;
links to repository files outside that tree need one more `../`. Explicit
anchors before headings preserve the original English fragments on GitHub. The
site renderer assigns those IDs to the translated headings, so existing table
of contents links continue to work. New untranslated upstream pages fall back
to English with a visible notice; the coverage test reports missing translations.

Use English source text as the message key, with named placeholders such as
`{count}` for variable values. Add the matching Chinese text to the relevant
catalog. Static elements use `data-i18n`; attributes use `data-i18n-title`,
`data-i18n-placeholder` or `data-i18n-aria-label`. Dynamic UI uses
`SBOS_I18N.t(message, parameters)` and redraws on `sbos:languagechange`.
An optional third locale argument supplies search aliases in either language.
Missing translations fall back to English. Keep URLs, file paths, command names
and node IDs unchanged.

Edit `tools/build_site.py` or `scripts/build_tree.py` for generated page markup,
then run the corresponding commands above. Run `tools/build_graph_site.py` after
changing home page assets to refresh its asset hashes. Commit regenerated pages
alongside their source changes.

Run the dependency-free locale regression tests with Node.js 18 or later:

```bash
node --test tests/i18n.test.cjs
```

After building, validate the article coverage, structure, code examples, link
targets and diagrams with Python 3.9 or later and the build's Markdown dependency:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

In the browser, check both languages on all three pages, refresh and navigate
between pages to check persistence, and exercise search, filters, tree folding,
the reader and the theme switch. Check translated body paragraphs, in-page
anchors and diagrams, then switch back to English on the same article. Repeat
the header check at mobile and tablet widths so the language switch remains
reachable.
