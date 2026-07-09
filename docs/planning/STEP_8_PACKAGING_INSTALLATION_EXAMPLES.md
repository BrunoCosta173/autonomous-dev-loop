# Step 8 Packaging Installation Examples

Status: **Completed**

## Step Goal

Define the public installation experience, packaging strategy, compatibility matrix, and first usage examples for `autonomous-dev-loop`.

This step makes the project easier to understand, install, and try in real projects without adding installer scripts, dependencies, or complete example applications.

## Packaging Strategy

The project now documents four package boundaries:

1. Repository package
2. Codex/OpenAI Skill package
3. Claude Code Skill package
4. Generic agent adapter package

## Repository Package

The full GitHub repository contains:

- Codex/OpenAI Skill target
- Claude Code Skill target
- Adapters
- Docs
- Examples
- Planning history
- License and changelog

Use the repository package for contribution, review, development, and manual installation source files.

## Codex/OpenAI Skill Package

The installable Codex/OpenAI Skill folder is:

```text
.agents/skills/autonomous-dev-loop/
```

Users can copy this folder into:

- A project repository under `.agents/skills/`
- A personal user Skills directory, when supported
- Another location supported by their agent setup

## Claude Code Skill Package

The installable Claude Code Skill folder is:

```text
.claude/skills/autonomous-dev-loop/
```

Users can copy this folder into:

- A project repository under `.claude/skills/`
- A personal Claude Skills directory, when supported
- Another location supported by their Claude Code setup

## Generic Agent Adapter Package

Generic agents can use:

- `adapters/AGENTS.md`
- `adapters/GENERIC_AGENT.md`
- Control file templates from the Skill `assets/` directories

Claude Code projects can use:

- `adapters/CLAUDE.md`

## Installation Documentation

Step 8 adds or expands:

- `docs/installation/codex-openai.md`
- `docs/installation/claude-code.md`
- `docs/installation/generic-agents.md`
- `docs/installation/agent-assisted-installation.md`
- `docs/installation/troubleshooting.md`

The documentation covers manual installation, agent-assisted installation, update notes, uninstall notes, troubleshooting, and future automated installation plans.

## Compatibility Matrix

The compatibility matrix covers:

- Codex/OpenAI Skills
- Claude Code Skills
- Generic AI coding agents

It documents install path, invocation style, persistent instruction files, Skill folder support, Review Subagent Loop support, fallback behavior, best use case, and notes.

The matrix explicitly states that real subagents and native goal modes are environment-dependent.

## First Usage Examples

Step 8 adds lightweight public usage examples for:

- Next.js app workflow improvement
- FastAPI API testing
- Laravel invoice workflow improvement

These examples are documentation only. They are not complete sample applications.

Each example includes:

- Example objective prompt
- Suggested constraints
- Expected Skill behavior
- Example validation commands
- Expected final report content
- Safety gates to watch

## Future Technology Notes

Future versions may add:

- Terminal installer command
- Shell and PowerShell installation scripts
- Sync script to keep Codex/OpenAI and Claude Skill targets equivalent
- GitHub Actions validation workflow
- Release packaging workflow
- Example project smoke tests
- Optional marketplace or plugin packaging if an ecosystem supports it
- More example stacks

## Explicit Non-Goals For Step 8

Step 8 does not:

- Create installer scripts.
- Create complete example applications.
- Polish the final marketing README.
- Add dependencies.
- Claim guaranteed compatibility across all agents.
- Claim `/goal` is universally available.
- Claim real subagents are universally available.

## Completion Criteria

Step 8 is complete because the repository now documents packaging boundaries, installation flows, agent-assisted installation, troubleshooting, compatibility expectations, and first public usage examples.
