# tools

The site at [undefined-ui.github.io/second-brain-os](https://undefined-ui.github.io/second-brain-os/)
is generated from this repository, so it cannot drift from the guide.

```bash
pip install markdown
python3 tools/extract_site.py   # docs and resources -> site_data.json
python3 tools/build_site.py     # -> index.html, resources.html
```

`extract_site.py` reads every page in `docs/`, keeps the reading order declared in
each section's `README.md`, resolves internal links to page ids, and parses every
table row in `resources/` that carries a link.

`build_site.py` writes two self-contained HTML files. No build step, no
framework, no external requests at runtime: the content is embedded, so the pages
work offline and from `file://`.

One dependency, `markdown`. The paths at the top of both scripts assume the repo
root.
