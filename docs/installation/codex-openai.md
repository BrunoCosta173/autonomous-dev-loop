# Codex/OpenAI Installation

This document describes the initial installation strategy for Codex/OpenAI-compatible Skills.

## Purpose

Use this installation target when working with:

- Codex CLI
- Codex Desktop/App
- OpenAI/Codex Skills-compatible agents

## Skill Folder

The Codex/OpenAI Skill lives at:

```text
.agents/skills/autonomous-dev-loop/
```

## Manual Installation

For version `0.0.1`, install manually by copying the Skill folder into the target Codex/OpenAI Skills location used by your agent environment.

Copy this folder:

```text
.agents/skills/autonomous-dev-loop/
```

The exact destination may depend on the agent environment.

## Agent-Assisted Installation

An AI coding agent can also install the Skill by copying `.agents/skills/autonomous-dev-loop/` into the target project's compatible Skills directory.

The agent should not modify the Skill behavior during installation.

## Future Installer

A terminal installation command or executable installer is planned for a future version.

No installation scripts are included in version `0.0.1`.
