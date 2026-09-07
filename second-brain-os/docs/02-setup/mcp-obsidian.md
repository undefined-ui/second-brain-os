# MCP for Obsidian

MCP is the standard way Claude talks to other applications. For a vault, it
adds a door into Obsidian itself rather than into the folder underneath, which
means the agent can work with the vault from any session, not only one started
inside that directory.

You do not need this to start. Add it when you want scheduled tasks, or when
you are working from the desktop app rather than a terminal in the vault.

## Step 1: enable the plugin

In Obsidian: **Settings** (gear, bottom left) → **Community plugins** → **Turn
on community plugins** → **Browse** → search `Local REST API` → **Install** →
**Enable**.

Open the plugin's settings. There is an **API Key**, a long string of letters
and numbers. Copy it.

Obsidian displays the key with the word `Bearer` in front of it. That word is
not part of the key. Copy only the string after it. This is the single most
common reason the connection fails on the first try.

## Step 2: register the server

In the Claude Code tab or terminal, with your key pasted in place of
`PASTE-YOUR-KEY-HERE`:

```bash
claude mcp add-json obsidian-vault '{
  "type": "stdio",
  "command": "uvx",
  "args": ["mcp-obsidian"],
  "env": {
    "OBSIDIAN_API_KEY": "PASTE-YOUR-KEY-HERE",
    "OBSIDIAN_HOST": "127.0.0.1",
    "OBSIDIAN_PORT": "27124"
  }
}'
```

`uvx` runs the server without a permanent install. If the command is not found,
install `uv` first.

## Step 3: test it

```
List every file in my Obsidian vault.
```

If the agent reads your notes back, the connection works.

## When it does not work

- **Obsidian is closed.** The plugin serves the API from inside the app, so the
  connection only exists while Obsidian is running.
- **`Bearer` in the key.** Strip it.
- **Wrong port.** Check the port shown in the plugin settings against the value
  in your config. The default is 27124.
- **Plugin disabled.** Community plugins get turned off when restricted mode is
  re-enabled after an update.

## Security

This opens a local HTTP server with a key that grants full read and write access
to your notes. Keep it on `127.0.0.1`, never expose the port, and treat the key
like a password. If you paste it anywhere public, rotate it in the plugin
settings.

## Next

[Writing your CLAUDE.md](claude-md.md)
