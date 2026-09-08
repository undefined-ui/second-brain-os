---
name: second-brain-privacy
description: >-
  Audit the vault for material that should not be in it: credentials, other
  people's private information, confidential work, and anything the user would
  not want synced or backed up. Use this skill when the user asks about privacy,
  is about to share or sync the vault, has just imported chat history or meeting
  notes, or asks what is sensitive in their notes. Do NOT use to delete anything
  on your own, or as a substitute for the publishing check.
---

# Audit privacy

A mature vault is one of the highest-signal documents about a person that
exists, and it lives in a folder that gets synced, committed, backed up and
occasionally shared. Every copy is another place the content exists.

## Core rule

Find and report. Delete nothing without an explicit instruction naming what to
remove.

## Workflow

1. **Scan for credentials:** API keys, tokens, passwords, connection strings.
   Check `.obsidian/plugins/` too, where plugin data lives.
2. **Find other people's information:** meeting transcripts, personal messages,
   anything told in confidence, health or financial detail about someone else.
3. **Find confidential work:** material under NDA or employer restriction.
4. **Check the git remote.** Private material in a public repo is the most
   expensive version of this problem.
5. **Report by severity,** with the specific file and why.

## Output format

```
Critical: <credentials, must be removed and rotated>
High: <other people's private information>
Review: <material the user should decide about>
Repo visibility: <public | private> - <verdict>
```

## Calibration

Never quote the credential itself in the report. Name the file and the type.

Redaction after ingest is unreliable, because material has already propagated
into concept pages and links. When something should not be there, say what else
would need removing with it.
