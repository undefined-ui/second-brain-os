"""Shared repository link resolution for both article languages."""
import re


def tool_for_path(rel, nodes):
    """Map a repo-relative path to a toolkit node, if it is one."""
    rel = rel.rstrip("/")
    m = re.match(r"^skills/([a-z0-9-]+)(?:/SKILL\.md)?$", rel)
    if m and f"skill:{m.group(1)}" in nodes:
        return f"skill:{m.group(1)}"
    for pat, pre in ((r"^commands/([a-z0-9-]+)\.md$", "cmd"), (r"^agents/([a-z0-9-]+)\.md$", "agent"),
                     (r"^scripts/([a-z0-9_]+\.py)$", "script"),
                     (r"^plugins/agents-course/(?:skills|agents)/([a-z0-9-]+)(?:/SKILL\.md|\.md)?$", "plug")):
        m = re.match(pat, rel)
        if m and f"{pre}:{m.group(1)}" in nodes:
            return f"{pre}:{m.group(1)}"
    if rel in ("skills", "skills/README.md"):
        return "hub:skills"
    if rel in ("commands", "commands/README.md"):
        return "hub:commands"
    if rel in ("agents", "agents/README.md"):
        return "hub:agents"
    if rel in ("scripts", "scripts/README.md"):
        return "hub:scripts"
    if rel.startswith("plugins"):
        return "hub:plugin"
    if rel.startswith("vault-template"):
        return "hub:vault"
    m = re.match(r"^resources/([a-z]+)\.md$", rel)
    if m and f"rcat:{m.group(1)}" in nodes:
        return f"rcat:{m.group(1)}"
    if rel in ("resources", "resources/README.md"):
        return "col:resources"
    return None
