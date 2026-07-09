# Packaging Strategy

This document defines the initial packaging model for `autonomous-dev-loop`.

## Package Types

The project has four practical package boundaries:

1. Repository package
2. Codex/OpenAI Skill package
3. Claude Code Skill package
4. Generic agent adapter package

Version `0.0.12` includes local installer and package-generation scripts plus release-candidate install positioning and final pre-merge audit corrections.

It does not include release publishing automation.

## Repository Package

The full GitHub repository contains:

- Codex/OpenAI Skill target
- Claude Code Skill target
- Adapters
- Docs
- Examples
- Planning history
- License and changelog

Use the repository package for development, review, contribution, and manual installation source files.

## Codex/OpenAI Skill Package

The installable Codex/OpenAI Skill folder is:

```text
.agents/skills/autonomous-dev-loop/
```

Users can copy this folder into:

- A project repository under `.agents/skills/`
- A personal user Skills directory, when supported
- Another location supported by their agent setup

This package includes:

- `SKILL.md`
- `agents/openai.yaml`
- `references/`
- `assets/`

## Claude Code Skill Package

The installable Claude Code Skill folder is:

```text
.claude/skills/autonomous-dev-loop/
```

Users can copy this folder into:

- A project repository under `.claude/skills/`
- A personal Claude Skills directory, when supported
- Another location supported by their Claude Code setup

This package includes:

- `SKILL.md`
- `references/`
- `assets/`

## Generic Agent Adapter Package

Generic agents can use:

- `adapters/AGENTS.md`
- `adapters/GENERIC_AGENT.md`
- Control file templates from the Skill `assets/` directories

Claude Code projects can also use:

- `adapters/CLAUDE.md`

Adapters are not full Skill packages. They are project-local instruction templates for agents that can read persistent instructions.

## File Role Boundaries

Repository development files:

- Root `AGENTS.md`
- Root `CLAUDE.md`
- `PROJECT_BRIEF.md`
- `CONTRIBUTING.md`
- `docs/`
- `examples/`

User-facing Skill installation files:

- `.agents/skills/autonomous-dev-loop/`
- `.claude/skills/autonomous-dev-loop/`

Reusable adapter templates:

- `adapters/AGENTS.md`
- `adapters/CLAUDE.md`
- `adapters/GENERIC_AGENT.md`

Example documentation:

- `examples/nextjs-app/README.md`
- `examples/fastapi-api/README.md`
- `examples/laravel-app/README.md`

## Versioning

The repository uses semantic versioning.

Commit and release titles should use only the version number, such as:

```text
0.0.12
```

## Install Channels

The public README treats `main` as the latest channel for end-user one-command install:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target codex --scope project
```

For reproducible installs, use a tagged release when available.

Agent-assisted installation should prefer transparent manual copy or local installer commands after inspecting the repository.

## Installer Package

The main installer is:

```text
scripts/install.py
```

Wrappers:

```text
install.sh
install.ps1
```

Supported actions:

- `install`
- `update`
- `uninstall`

Supported targets:

- `codex`
- `claude`
- `both`
- `generic`

Supported scopes:

- `project`
- `user`

Generic adapters support project scope only.

The installer is conservative:

- It prints planned operations.
- It supports `--dry-run`.
- It refuses accidental overwrites unless `--force` or update behavior allows them.
- It asks before destructive update or uninstall actions unless `--yes`, `--force`, or `--dry-run` is used.
- It removes only known installed Skill folders and matching adapter files.

## Release Packages

The release packaging script is:

```text
scripts/package_release.py
```

It creates:

```text
dist/autonomous-dev-loop-<version>.zip
dist/autonomous-dev-loop-codex-<version>.zip
dist/autonomous-dev-loop-claude-<version>.zip
dist/autonomous-dev-loop-adapters-<version>.zip
```

Generate packages:

```bash
python3 scripts/package_release.py --version 0.0.12 --clean
```

Generated `dist/` files are local release artifacts and are ignored by Git.

## Future Packaging Work

Future versions may add:

- Sync script to keep Codex/OpenAI and Claude Skill targets equivalent
- Release packaging workflow
- Example project smoke tests
- Optional marketplace or plugin packaging if an ecosystem supports it
- More example stacks
