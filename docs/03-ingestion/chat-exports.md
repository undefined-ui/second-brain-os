# Chat exports

Your chat history is the most underrated source you own and the most sensitive.
Years of problems you worked through, decisions you reasoned about, and
explanations tailored to what you did not understand at the time.

It is also full of things you would not want in a file you might later share.
Read the privacy section below before running anything here.

## Exporting

Both Claude and ChatGPT export the full history as JSON from account settings.
The export arrives by email as a download link, usually within minutes.

## Converting to markdown

One JSON blob is not ingestible. Split it into one file per conversation:

```bash
python3 scripts/chat_export_to_md.py conversations.json ./raw --min-words 150
```

The script is in [`scripts/`](../../scripts/README.md). It handles the common
export shapes, writes frontmatter with the title and date, and skips
conversations shorter than the word threshold.

Raise `--min-words` if the output is dominated by one-line exchanges. Most
people's history is roughly ninety percent short throwaway questions, and those
add nothing but volume.

## Filter before ingesting

Do not ingest the whole export. A thousand conversations produce a thousand
source pages and a wiki where everything is faintly connected to everything.

Sort into three piles:

- **Worth ingesting.** Conversations where you worked something out, decided
  something, or got an explanation that landed. These carry your reasoning, not
  just facts.
- **Worth keeping, not ingesting.** Leave them in `raw/` as an archive. The
  agent can search them on demand without every one having a wiki page.
- **Delete.** Debugging sessions, one-off lookups, anything you would be
  annoyed to find in a search result.

Have the agent help with the sort rather than doing it by hand:

```
Read the titles and first exchange of every file in raw/chats/. Group them into
worth-ingesting, archive, and delete, with one line of reasoning each. Do not
move or delete anything, just give me the lists.
```

## What makes these sources different

A chat log is a record of you thinking, which means the useful extraction is
often not the answer. It is the question you asked, the thing you had wrong at
the start, and what changed your mind.

Tell the agent so:

```
These are my own past conversations. Build pages around what I was trying to
work out and what conclusion I reached, not around the assistant's explanations.
Note where I changed position, and record the date, because my views may have
moved since.
```

## Privacy

Chat history contains more about you than any other file in the vault: health,
money, work you cannot discuss, other people's information you happened to
mention.

Before ingesting, decide what does not belong in the vault at all and delete
those files from `raw/`. Redaction after the fact is unreliable, because the
material will already have propagated into concept pages and links.

If the vault lives in a git repo, keep the remote private. See
[privacy](../09-maintenance/privacy-and-secrets.md).

## Next

[Voice notes and meetings](voice-and-meetings.md)
