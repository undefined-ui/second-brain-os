# projects/

One folder per project. Each holds its own `CLAUDE.md` and the four-stage
pipeline:

```
project-name/
  CLAUDE.md    what this project is, its one goal, the agent's role
  Inputs/      ideas, briefs, source material for this project
  Process/     work in progress
  Outputs/     finished work
  Feedback/    results, metrics, what actually happened
```

`Feedback/` is the folder people skip and the one that makes the system
improve. Without it the agent has no idea whether last month's output worked.

Open a project as its own vault when you are working in it, so the agent sees
one goal instead of your whole life. See
[project scoping](../../docs/02-setup/project-scoping.md).
