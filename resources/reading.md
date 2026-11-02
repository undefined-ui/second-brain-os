# Reading

## The source document

**[Karpathy's llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**,
published 4 April 2026. The pattern everything in this repo builds on.

It is short, and it is written as an idea file meant to be pasted into your own
agent rather than as a spec. The core argument: most people's use of LLMs with
documents is RAG, where the model rediscovers knowledge from scratch on every
question and nothing accumulates.

Read it first. Everything else, including this guide, is one interpretation of
it.

## The pattern at company scale

**[An organizational second brain: AI that learns from experts](https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/)**,
Meta Engineering, September 2026. The same pattern this guide teaches, run
inside Meta with a whole domain team as the user.

Worth reading for the architecture alone: 200+ structured knowledge files with
YAML frontmatter forming a dependency graph — position files, taxonomies,
routing indexes, gateway files — kept apart from "recipes", the reasoning
procedures that reference knowledge without containing it. Fixes stay
surgical: a knowledge edit touches no procedure, a methodology fix touches no
facts. Their split rule matches ours: dense, frequently-used knowledge lives
in the wiki; sparse reference material stays behind retrieval. Expert
corrections flow through a diagnose-compile-validate-land loop with regression
tests, no retraining. Six weeks in: assessment time down from days to minutes,
zero regressions. The strongest public evidence yet that a maintained wiki
beats rediscovery-by-RAG at scale.

## The tradition it comes from

- **How to Take Smart Notes**, Sönke Ahrens. The Zettelkasten method. The
  argument for atomic notes and dense linking still holds; the manual labour it
  demands is the part that killed it for most people.
- **Building a Second Brain**, Tiago Forte. Where the term comes from, and the
  PARA method. Written before agents existed, which is what makes it useful now:
  most of the book is about the maintenance work an agent removes.
- **[Andy Matuschak's notes](https://notes.andymatuschak.org)**. Evergreen notes,
  written in public as a working example of the idea. The strongest case for
  notes written to be reread, and a useful counterweight to this whole approach:
  his position is that the writing is the thinking, so delegating it means not
  doing it.

## Why the maintenance argument matters

Every method above works. They fail on the same thing, which is that the person
maintaining them gets tired. That single constraint shaped all of their design
decisions, and it is the constraint that changed.

Reading the originals is worth it for that reason specifically: you can see
which parts were about knowledge and which were workarounds for human effort.

## New in October 2026

**[Anthropic donates Agent Skills to the Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)**, 22 October 2026. The `SKILL.md` format moves to the Linux Foundation's agent foundation, name, spec and site included. The skills in this repo are now written to a neutral standard.

**[Building agents: when to fold subagents into your main agent loop](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop)**, Anthropic, 22 October 2026. The case that one loop with skills and progressively disclosed tools often matches a fleet of subagents, when subagents are still worth it, and a migration plan that starts from ten golden eval cases.

**[Building effective agent automations](https://claude.dev/blog/building-effective-agent-automations/)**, Anthropic, 8 October 2026. A scheduled agent built end to end: a bookmark per source, a ledger of what was already reported, a per-run spend cap, and a failed source reported as a failure rather than a quiet day. Every pattern carries over to a nightly ingest.

**[Automating eval design and hillclimbing with Claude](https://claude.dev/blog/automating-eval-design-and-hillclimbing/)**, Anthropic, 28 September 2026. Two commands that build an eval in your codebase and then improve against it, keeping a change only when both the train split and a held-out split improve. Read it with [Hamel Husain's critique](https://hamel.dev/blog/posts/claude-auto-evals/).

**[How to use decision models for evals](https://hamel.dev/blog/posts/decision-model-evals/)**, Hamel Husain and Antaripa Saha, 20 October 2026. Jev, OpenAI's [Decisions API](https://developers.openai.com/api/docs/guides/decisions) and three other decision models compared as cheap pass or fail judges on 98 human-labelled agent traces, with the advice to tune the threshold rather than keep 0.5.

**[How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)**, Anthropic, 15 October 2026. Parallel finders, a separate voting verifier and a three-round cap took first-round passes from 65% to 78%. Real numbers on making a critic loop converge.

## Talks and videos

This section is deliberately empty rather than padded with whatever ranks well
on YouTube. If you have watched something on this topic that was worth the time,
open an issue or a pull request with the link and one line on why.
