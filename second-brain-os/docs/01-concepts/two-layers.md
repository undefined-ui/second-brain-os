# The two layers

Most second-brain setups fail because they pick one shape and try to make it do
two jobs.

**The knowledge layer** answers "what do I know about X". It is organised by
idea, it grows forever, and its value is in the links between pages. This is the
LLM wiki pattern: sources in, concepts out, everything connected.

**The project layer** answers "what am I doing this week". It is organised as a
pipeline, inputs to outputs, and most of it goes cold the moment the project
ships.

They fail differently when merged. A wiki with project folders in it fills up
with dead task lists that make every search worse. A project system with
conceptual notes in it buries the working files under material nobody opens
while working.

## How they connect

Projects consume the knowledge layer and feed it back:

```
        wiki/concepts ──────> project Inputs/
              ▲                      │
              │                      ▼
        ingest what                Process/ ──> Outputs/
        you learned                              │
              └──────────────────────────────────┘
```

Work produces material worth keeping. Ingesting your own finished work is the
step almost everyone skips, and it is the one that makes the second project in
a domain meaningfully faster than the first.

## Which to build first

The knowledge layer, if you read a lot and retain little.

The project layer, if your problem is that you re-explain your situation to a
chat window every morning.

Both eventually. See [vault structure](../02-setup/vault-structure.md) for the
layout that keeps them separate inside one folder.
