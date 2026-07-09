# Step 1 Repository Structure

Status: **Completed**

## Step Goal

Define and prepare the official repository structure and installation strategy for version `0.0.1`.

This step creates the initial architecture for future implementation without writing the full autonomous development loop behavior.

## Official Version 0.0.1 Structure

The project adopts the following structure as the official initial direction:

```text
autonomous-dev-loop/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── PROJECT_BRIEF.md
├── AGENTS.md
├── CLAUDE.md
├── docs/
│   ├── planning/
│   │   ├── STEP_0_FOUNDATION.md
│   │   └── STEP_1_REPOSITORY_STRUCTURE.md
│   ├── installation/
│   │   ├── codex-openai.md
│   │   ├── claude-code.md
│   │   └── generic-agents.md
│   └── design/
│       ├── repository-structure.md
│       └── skill-architecture.md
├── .agents/
│   └── skills/
│       └── autonomous-dev-loop/
│           ├── SKILL.md
│           ├── agents/
│           │   └── openai.yaml
│           ├── references/
│           └── assets/
├── .claude/
│   └── skills/
│       └── autonomous-dev-loop/
│           ├── SKILL.md
│           ├── references/
│           └── assets/
├── adapters/
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   └── GENERIC_AGENT.md
└── examples/
    ├── nextjs-app/
    ├── fastapi-api/
    └── laravel-app/
```

This structure may evolve later, but it is the official structure for version `0.0.1`.

## Dual Installation Strategy

The repository supports two separate Skill installation targets from the beginning:

- Codex/OpenAI Skills: `.agents/skills/autonomous-dev-loop/`
- Claude Code Skills: `.claude/skills/autonomous-dev-loop/`

Users should install the version that matches the agent they are using.

## Separate Skill Files

The project uses Option A:

- Maintain a Codex/OpenAI Skill version.
- Maintain a Claude Code Skill version.
- Keep both `SKILL.md` files behaviorally equivalent.
- Do not create a sync or build script yet.

Future versions may add a terminal installation command, executable installer, or sync/build utility.

## Manual And Agent-Assisted Installation

Version `0.0.1` prepares for:

- Manual installation by copying the correct Skill folder.
- Agent-assisted installation where an AI agent copies the correct Skill folder into the target project.

Installer scripts are intentionally deferred.

## Claude Code Compatibility

Claude Code compatibility requires three distinct file types:

- Root-level `CLAUDE.md`: instructions for Claude Code agents contributing to this repository.
- `adapters/CLAUDE.md`: reusable template for users to copy into their own projects.
- `.claude/skills/autonomous-dev-loop/SKILL.md`: Claude Skill entry point.

These files serve different purposes and should not be merged.

## Root Agent Instruction Files

The repository includes:

- `AGENTS.md` for AI agents contributing to this repository.
- `CLAUDE.md` for Claude Code agents contributing to this repository.

These files are not the reusable end-user adapters.

## User-Facing Adapter Templates

The repository includes:

- `adapters/AGENTS.md`
- `adapters/CLAUDE.md`
- `adapters/GENERIC_AGENT.md`

These files are reusable templates intended for users to copy into their own projects when they want project-local agent guidance.

## Installation Documentation

The repository includes concise installation notes for:

- Codex/OpenAI Skills
- Claude Code Skills
- Generic AI coding agents

These documents explain manual copy installation, agent-assisted installation, and the planned future installer direction.

## Examples

The repository reserves example folders for:

- Next.js app
- FastAPI API
- Laravel app

Complete examples are intentionally deferred.

## Explicit Non-Goals For Step 1

Step 1 does not:

- Implement the full autonomous development loop behavior.
- Add installer scripts.
- Add sync/build automation between Skill files.
- Add complete examples.
- Add stack-specific implementation references.
- Finalize the public marketing README.

## Future Roadmap Notes

Future versions may add:

- A terminal installation command.
- A sync/build utility to keep Skill variants aligned.
- Full Skill behavior for objective intake, inspection, planning, execution, testing, repair, documentation, and final reporting.
- Stack-specific reference files.
- Example project walkthroughs.
- More complete adapter documentation.

## Completion Criteria

Step 1 is complete because the official version `0.0.1` repository structure and installation strategy are documented, and the initial folders and placeholders are prepared for future implementation.
