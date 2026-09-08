---
name: second-brain-chat-import
description: >-
  Triage an exported chat history into what to ingest, what to archive and what
  to delete, with a privacy pass first. Use this skill when the user has exported
  their Claude or ChatGPT history, asks to import old conversations, or asks what
  in their chat archive is worth keeping. Do NOT use for ingesting a single
  pasted conversation, or for any material the user has not explicitly asked to
  bring into the vault.
---

# Import chat history

Chat history is the most underrated source a person owns and the most sensitive.
It records their reasoning, not just facts, and it also records things they would
not want in a file that gets synced, committed and backed up.

## Core rule

Privacy pass before triage, triage before ingestion. Never ingest an export
wholesale.

## Workflow

1. **Convert** with `scripts/chat_export_to_md.py` into one file per
   conversation, filtering out short exchanges.
2. **Privacy pass.** List conversations touching health, money, other people's
   private information, or confidential work. The user decides; you delete
   nothing on your own.
3. **Triage the rest** into three piles: worth ingesting (they worked something
   out, decided something, or got an explanation that landed), worth archiving
   in `raw/`, and delete.
4. **Report the lists.** Move nothing yet.
5. **On approval, ingest** the first pile, with the instruction that these are
   the user's own thinking: build pages around what they were working out and
   what they concluded, not around the assistant's explanations.

## Output format

```
Converted: <n> conversations (<n> skipped as too short)

Privacy review needed: <n>
  <title> - <why>

Worth ingesting: <n>
  <title> - <what it worked out>

Archive only: <n>
Delete suggested: <n>
```

## Calibration

Expect roughly nine in ten conversations to be throwaway lookups. A triage that
recommends ingesting most of the export has not filtered.

Record dates on every page. A position from two years ago is not a current
belief, and the vault has to be able to tell the difference.
