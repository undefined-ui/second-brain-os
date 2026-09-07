# The agent writes garbage

Pages that are technically about the right thing and useless to read.

## Diagnose the source first

Before touching instructions, check the input. Open the file in `raw/` and read
it.

Half of the bad pages people blame on the agent come from a bad extraction: a PDF
whose columns interleaved, an auto-caption transcript with no punctuation, a
clipped page that captured the cookie banner instead of the article.

The agent cannot write a good page from mangled text, and it will not tell you it
is struggling. See [PDFs](../03-ingestion/pdfs-and-books.md) and
[transcripts](../03-ingestion/youtube-transcripts.md).

## Then check CLAUDE.md

If the source is clean, the page contract is the problem.

The specific things that produce vague pages: no definition of what each page
type contains, the word "summarise" anywhere, no instruction to write for a
reader who has not seen the source, no requirement to link.

Rewrite the contract with the shape spelled out. See [page
types](../04-structuring/page-types.md).

## Add an example, not another rule

The highest-leverage fix and the least used. Put one good concept page in
`CLAUDE.md`, in full, as the target.

Rules describe the output abstractly and each new rule interacts with the others.
One example communicates the target directly, and it is what a person would ask
for if you told them to match a style.

## Ask what it was working from

```
You wrote [[page]]. Which parts of the source did you use, and what did you leave
out?
```

The answer usually identifies the problem immediately: it read a fragment, it
could not tell what the source claimed versus reported, or the instructions
pulled it toward summarising.

## Roll back and re-run

Fix the contract, revert the bad pages, re-ingest.

```bash
git checkout HEAD~1 -- wiki/
```

Do not patch the bad pages by hand. If the contract was wrong, every page from
that run has the same flaw, and hand-fixing the three you noticed leaves the rest.

## Next

[Broken links and orphans](broken-links.md)
