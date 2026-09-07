# PDFs, papers and books

PDFs are the format most likely to arrive in your vault as garbage. Two columns
become interleaved lines, tables collapse, footnotes land mid-sentence, and the
agent quietly builds pages on top of the mess.

Check extraction quality before ingesting. It takes ten seconds and saves
rewriting pages later.

## Extraction

```bash
# text, layout preserved reasonably well
pdftotext -layout paper.pdf raw/paper.md
```

For anything structured, `pymupdf` gives better control and can pull images and
tables separately. Whatever you use, open the output and read a paragraph from
the middle. If the sentences do not flow, fix extraction rather than hoping the
agent copes.

## Scanned documents

A scan is an image, and text extraction returns nothing or near-nothing. Run OCR
first with `ocrmypdf`, which adds a text layer without changing the visible
document. Expect errors in proper nouns and numbers, and treat any figure from
an OCR'd source as needing verification before it goes into a wiki page as
fact.

## Papers

Papers deserve different handling than articles, because the parts you will
want later are not spread evenly. Abstract, method, results and limitations
carry almost everything.

A useful ingest instruction:

```
This is an academic paper. Build the source page around: the question it asks,
the method, the result with its actual numbers, and the limitations the authors
state themselves. Record sample sizes. Do not report a finding without the
condition it holds under.
```

That last rule is what keeps a wiki honest. Findings stripped of their
conditions become confident nonsense two years later.

Zotero is worth using if you read papers regularly. It handles metadata and
exports markdown, which lands in `raw/` cleanly.

## Books

A full book is too large to ingest as one source and mostly not worth it. What
is worth it is your highlights.

Kindle highlights export from the Kindle app or through Readwise, which syncs
into Obsidian directly. Highlights arrive as a list of quoted passages, so
ingest them as one source page per book, and let the agent build concept pages
from the ideas rather than from the quotes.

Keep the quotes short in the wiki and keep the citation. A page that reproduces
half a chapter is a copyright problem and a retrieval problem at the same time.

## Figures and tables

Text extraction drops both. When a figure carries the argument, screenshot it
into `raw/assets/` and reference it from the source page, so the claim on the
page has something behind it.

## Next

[Chat exports](chat-exports.md)
