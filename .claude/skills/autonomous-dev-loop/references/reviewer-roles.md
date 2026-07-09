# Reviewer Roles

Use this reference to select reviewers for the Review Subagent Loop.

Do not call every reviewer every time. Select reviewers based on the objective, changed files, and risk profile.

## Default Selection

- Scope Reviewer: always.
- Code Quality Reviewer: when code changed.
- Test Reviewer: when logic, tests, APIs, or validation changed.
- Security Reviewer: when authentication, permissions, inputs, APIs, data handling, secrets, or dependencies are involved.
- UX/UI Reviewer: when UI, flows, forms, layouts, copy, accessibility, or user-facing behavior changed.
- Documentation Reviewer: when docs, README, templates, specs, instructions, or public-facing content changed.
- Architecture Reviewer: when structure, cross-cutting concerns, dependencies, module boundaries, frameworks, or large refactors changed.

## Scope Reviewer

Focus:

- Original objective alignment
- Non-goals
- Scope drift
- Completeness of planned ToDos
- Whether unrelated issues were deferred correctly

Reject or require fixes when the implementation expands scope materially without confirmation.

## Code Quality Reviewer

Focus:

- Correctness
- Maintainability
- Simplicity
- Consistency with local patterns
- Error handling
- Duplication

Prefer targeted, actionable feedback.

## Test Reviewer

Focus:

- Whether relevant validation commands ran
- Test coverage for changed behavior
- Missing tests
- Failed or skipped tests
- Whether test claims match actual command output

Flag any claim that tests passed without execution.

## Security Reviewer

Focus:

- Authentication and authorization risks
- Input validation
- Data handling
- Secrets and environment variables
- Dependency risk
- External system effects

Trigger safety gates for risky auth, permission, secret, dependency, or data handling changes.

## UX/UI Reviewer

Focus:

- User-facing behavior
- Flows and forms
- Accessibility
- Copy clarity
- Layout consistency
- Interaction states

Do not invent product direction beyond the objective.

## Documentation Reviewer

Focus:

- Accuracy
- Completeness
- Public readiness
- Template usefulness
- Consistency with project terminology
- Whether durable context is captured

Flag stale or misleading docs.

## Architecture Reviewer

Focus:

- Module boundaries
- Cross-cutting concerns
- Dependency direction
- Framework fit
- Long-term maintainability
- Whether the change is too broad for the objective

Trigger a safety gate for major rewrites or framework replacement.
