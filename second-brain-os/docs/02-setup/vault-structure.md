# Vault structure

The vault does two different jobs, and they want different shapes. Keeping them
in one folder tree while keeping the shapes separate is what makes the system
hold up past the first month.

**The knowledge layer** is what you have read and understood. It grows forever
and it is organised by idea.

**The project layer** is what you are working on now. It is organised by
pipeline and most of it goes cold when the project ships.

```
brain/
  CLAUDE.md            who you are, how the vault works
  raw/                 source material, never edited after it lands
    assets/
  wiki/                the knowledge layer
    sources/           one page per ingested item
    entities/          people, organisations, products, tools
    concepts/          ideas, methods, frameworks
    synthesis/         comparisons, themes, open questions
    index.md           catalog of every page
    log.md             what the agent did, chronologically
  projects/            the project layer
    youtube-channel/
      CLAUDE.md        this project only
      Inputs/          ideas, briefs, raw material
      Process/         work in progress
      Outputs/         finished work
      Feedback/        results, metrics, what happened
  output/              generated reports and drafts
```

## Why the split

A project pipeline answers "what am I doing this week". A wiki answers "what do
I know about X". Force one structure to do both and you get either a knowledge
base full of dead task folders, or projects buried under conceptual pages
nobody opens while working.

They connect through links. A project page links to the concepts it depends on;
concept pages accumulate references from the projects that used them. That is
where the compounding shows up: the second time you start a project in a domain,
the knowledge layer already has it.

## Set the projects up by asking

```
Create a project folder in my vault called youtube-channel. Inside it, create
four folders: Inputs, Process, Outputs, Feedback. Then write a CLAUDE.md inside
that project folder describing what this project is, its one goal, and your
specific role in helping me hit it. Interview me if you need details.
```

Repeat per area: content, finances, clients. One goal per project, stated in
the project's own `CLAUDE.md`. Projects with three goals produce work that
serves none of them.

## Rules that keep it working

- **Never edit `raw/`.** It is the archive. If a source is wrong, replace the
  file and re-ingest, so it stays a faithful record of what you actually saved.
- **Do not nest deeply.** Folders four levels down stop getting opened. The
  graph is the navigation, not the tree.
- **Everything the agent generates for outside use goes to `output/` or the
  project's `Outputs/`,** never loose in the vault root.

## Next

[Project scoping](project-scoping.md)
