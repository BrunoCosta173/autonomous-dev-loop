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
- `TODO.md`
- `FINAL_REPORT.md`

## When To Use Each File

- `AGENTS.md`: project-local guidance for AI coding agents.
- `CLAUDE.md`: project-local guidance for Claude Code.
- `BACKLOG.md`: future improvements or out-of-scope findings.
- `ROADMAP.md`: planned larger milestones.
- `DEVELOPMENT_LOG.md`: chronological notes from autonomous runs.
- `TEST_PLAN.md`: test strategy, gaps, and validation expectations.
- `DECISIONS.md`: durable architecture or product decisions.
- `KNOWN_ISSUES.md`: unresolved bugs, failing commands, or blockers.
- `TODO.md`: active execution plan for the current autonomous run.
- `FINAL_REPORT.md`: persistent final report when the user wants durable run output.

## Template Assets

Reusable templates live in `assets/`:

- `assets/AGENTS.template.md`
- `assets/CLAUDE.template.md`
- `assets/BACKLOG.template.md`
- `assets/ROADMAP.template.md`
- `assets/DEVELOPMENT_LOG.template.md`
- `assets/TEST_PLAN.template.md`
- `assets/DECISIONS.template.md`
- `assets/KNOWN_ISSUES.template.md`
- `assets/TODO.template.md`
- `assets/FINAL_REPORT.template.md`

Use these templates as copy-ready starting points. Adapt placeholders to the target project before or after copying.

## Template Usage Policy

Do not force every template into every project.

Instead:

- Create or suggest `AGENTS.md` when a generic agent instruction file is useful.
- Create or suggest `CLAUDE.md` when the user is using Claude Code.
- Create or suggest `BACKLOG.md` and `DEVELOPMENT_LOG.md` for longer autonomous work.
- Create or suggest `TEST_PLAN.md` when testing strategy is unclear or missing.
- Create or suggest `DECISIONS.md` when architectural or product decisions are being made.
- Create or suggest `KNOWN_ISSUES.md` when blockers, bugs, or unrelated issues are found.
- Create or suggest `TODO.md` for the current autonomous run when the task has multiple steps.
- Create or suggest `FINAL_REPORT.md` when the user wants a persistent run report.
- Create or suggest `ROADMAP.md` when high-level project direction is missing or actively being shaped.

## Documentation Rules

- Keep notes concise and actionable.
- Separate facts from assumptions.
- Include dates only when useful for traceability.
- Do not expose secrets or private environment details.
- Do not add project control files when a final report is enough.
- Respect existing documentation structure and naming.
- Prefer updating existing equivalent files over creating duplicates with different names.

## End-Of-Run Documentation

At the end of a loop, update durable docs when:

- The project needs future agents to know what changed.
- There are unresolved issues or deferred ToDos.
- Tests could not run and the reason should persist.
- A decision was made that future work should not revisit casually.
