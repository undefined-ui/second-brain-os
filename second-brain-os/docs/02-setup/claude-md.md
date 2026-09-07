# Writing your CLAUDE.md

`CLAUDE.md` at the vault root is the file the agent reads at the start of every
session. It is the difference between an assistant that knows your situation and
one you brief from scratch every time.

An empty vault with a good `CLAUDE.md` is more useful than a full vault without
one, because context about you shapes every page the agent writes afterwards.

## Do not type it, get interviewed

Writing this file cold produces a thin, generic version. Answering questions
produces a specific one. Paste this into the agent:

```
You are setting up my second brain. Interview me ONE question at a time to
build my profile. Ask about: who I am and what I do, my goals for this year,
how I want you to talk to me, my strengths and weaknesses, and my current
projects. Wait for each answer before the next question. When finished, write
everything into CLAUDE.md at the vault root, structured with headers.
```

Answer as if briefing a co-founder on their first day. Vague answers produce a
vague file, and every session inherits it.

## What belongs in it

- **Who you are and what you work on.** Enough that a stranger could act on it.
- **Goals with a horizon.** This year, this quarter. Undated goals age badly.
- **How to talk to you.** Length, tone, how much pushback you want.
- **Your strengths and weak spots.** This is what lets the agent know when to
  challenge you rather than agree.
- **Current projects,** one line each, linked to their folders.
- **The vault's own rules:** folder layout, page contracts, linking rules. The
  version in [`vault-template/CLAUDE.md`](../../vault-template/CLAUDE.md) is a
  working starting point.

## What does not belong in it

- Anything that changes weekly. That goes in the project files.
- Long explanations of things the model already knows.
- Credentials of any kind.
- Aspirational statements you will not act on. The agent takes them literally.

## Two levels

The root `CLAUDE.md` is the strategy layer: who you are, what you are aiming
at, how the vault works. Each project folder gets its own `CLAUDE.md` covering
that project only. When you open a project as its own vault, the agent reads
just that one and stops carrying your entire life into every task. See
[project scoping](project-scoping.md).

## Iterate on it

When the agent does something wrong twice, that is a `CLAUDE.md` problem, not a
prompting problem. Add the rule, with the reason attached, because a rule
without a reason gets applied too literally in the cases you did not anticipate.

Re-read the file monthly. Goals move, projects close, and a stale profile
quietly degrades everything the agent writes.

## Next

[Vault structure](vault-structure.md)
