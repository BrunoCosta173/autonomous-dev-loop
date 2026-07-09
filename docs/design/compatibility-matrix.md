# Compatibility Matrix

`autonomous-dev-loop` is stack-agnostic and agent-oriented. Compatibility depends on the current agent environment, local Skill support, available tools, and project files.

Do not treat this matrix as a guarantee that every platform supports every feature.

| Agent target | Install path | Invocation style | Persistent instruction file | Skill folder support | Review Subagent Loop support | Fallback behavior | Best use case | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Codex/OpenAI Skills | `.agents/skills/autonomous-dev-loop/` | Ask the agent to use `autonomous-dev-loop` with a scoped objective | Optional `AGENTS.md` from `adapters/AGENTS.md` | Environment-dependent Codex/OpenAI Skill support | Real subagents only when supported by the environment | Independent review passes using reviewer roles and rubrics | Codex/OpenAI-compatible Skill workflows | Install path may vary for personal Skill directories. |
| Claude Code Skills | `.claude/skills/autonomous-dev-loop/` | Ask Claude Code to use `autonomous-dev-loop` with a scoped objective | Optional `CLAUDE.md` from `adapters/CLAUDE.md` | Environment-dependent Claude Code Skill support | Real subagents only when supported by the environment | Independent review passes using reviewer roles and rubrics | Claude Code projects that support local Skills or persistent project instructions | Keep root repository `CLAUDE.md` separate from reusable adapter `adapters/CLAUDE.md`. |
| Generic AI coding agents | `adapters/AGENTS.md` or `adapters/GENERIC_AGENT.md` copied into the target project | Ask the agent to follow the autonomous-dev-loop instructions | `AGENTS.md`, `GENERIC_AGENT.md`, or another file supported by the agent | No native Skill folder assumed | Real subagents only when supported by the agent environment | Independent review passes, ToDos, validation, and final report | Agents that read project-local instructions but do not support native Skill packages | Use selected control templates from Skill `assets/` only when useful. |

## Feature Notes

- Native `/goal` or long-run modes are optional platform features, not universal requirements.
- Real review subagents are environment-dependent.
- Independent review passes are the required fallback when real subagents are unavailable.
- Validation commands are project-dependent and should be discovered from files and scripts.
- The Skill should not claim tests passed unless validation commands actually ran.
