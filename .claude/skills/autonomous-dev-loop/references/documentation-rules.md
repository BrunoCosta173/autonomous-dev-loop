# Documentation Rules

Update documentation when it improves continuity, traceability, or future autonomous cycles.

Do not force every control file into every project.

## Useful Control Files

Create or update when useful:

- `AGENTS.md`
- `CLAUDE.md`
- `BACKLOG.md`
- `ROADMAP.md`
- `DEVELOPMENT_LOG.md`
- `TEST_PLAN.md`
- `DECISIONS.md`
- `KNOWN_ISSUES.md`

## When To Use Each File

- `AGENTS.md`: project-local guidance for AI coding agents.
- `CLAUDE.md`: project-local guidance for Claude Code.
- `BACKLOG.md`: future improvements or out-of-scope findings.
- `ROADMAP.md`: planned larger milestones.
- `DEVELOPMENT_LOG.md`: chronological notes from autonomous runs.
- `TEST_PLAN.md`: test strategy, gaps, and validation expectations.
- `DECISIONS.md`: durable architecture or product decisions.
- `KNOWN_ISSUES.md`: unresolved bugs, failing commands, or blockers.

## Documentation Rules

- Keep notes concise and actionable.
- Separate facts from assumptions.
- Include dates only when useful for traceability.
- Do not expose secrets or private environment details.
- Do not add project control files when a final report is enough.
- Respect existing documentation structure and naming.

## End-Of-Run Documentation

At the end of a loop, update durable docs when:

- The project needs future agents to know what changed.
- There are unresolved issues or deferred ToDos.
- Tests could not run and the reason should persist.
- A decision was made that future work should not revisit casually.
