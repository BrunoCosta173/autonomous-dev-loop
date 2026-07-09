# Step 15 — README clarity and human-facing polish

Status: Completed

## Why this patch exists

After the `0.1.0` public release and the `0.1.1` audit-fix patch, the README had good structure but moved too quickly from installation into technical flow details without explaining the practical value and usage of the Skill to a human reader.

A visitor to the repository should immediately understand what `autonomous-dev-loop` is, what the installation adds to their project, how to use the Skill after install, and why it is useful — before diving into the technical loop protocol.

## What was unclear in README

- The README jumped from Quick Install directly into a detailed 13-step flow without explaining what the Skill actually does for the user.
- There was no section explaining what files the installer adds and what they are for.
- There was no section guiding the user on how to actually use the Skill after installing it.
- The safety model and compatibility sections were present but not prominent enough for a first-time visitor.
- Project control files were listed without context about when they are useful.
- There were only 4 examples total, with only one A0 "review-only" example.

## What was improved

1. **Restructured the opening flow** so a human reader progresses naturally: tagline -> why it exists -> quick install -> what it installs -> what it does -> how to use.
2. **Added "What this installs" section** with a clear table showing which target installs which files, plus an explanation that the installer only adds instructions — it does not modify app code, install dependencies, or deploy anything.
3. **Added "What it does" section** with a step-by-step breakdown of the agent workflow in plain English, followed by the clarifying statement: "The goal is not to make the agent reckless. The goal is to make it more autonomous while keeping it bounded, reviewable, and safer."
4. **Added "How to use it after installing" section** with a concrete example prompt and a bullet list of what the agent will do in response.
5. **Added "When to use it" section** with a table matching task types to concrete examples.
6. **Added "When not to use it" section** listing cases where the full loop is unnecessary.
7. **Improved "How the loop works"** with a visual ASCII diagram showing the vertical flow from objective through handoff.
8. **Improved the safety model explanation** making it clear that safety gates are not optional and listing the categories explicitly.
9. **Added "Project control files" section** with a table of all 8 files, their purposes, and a clear policy that the Skill should not create all files by default.
10. **Added "Review before done" section** making the review cycle explicit.
11. **Expanded examples to 4** including A0 review-only mode and continuation mode.
12. **Kept all existing badges, compatibility table, install instructions, validation commands, and documentation links.**
13. **Updated version references** from `0.1.1` to `0.1.2`.

## What was not changed

- Skill behavior was not modified.
- References and assets were not changed.
- Installer, packaging, and validation scripts were not changed.
- No external dependencies were introduced.
- The MIT license was not changed.
- Existing published releases were not modified.

## Validation performed

```bash
python3 scripts/validate_repository.py
python3 scripts/check_skill_equivalence.py
python3 scripts/check_private_content.py
python3 scripts/test_installer.py
python3 scripts/test_packaging.py
python3 scripts/package_release.py --version 0.1.2 --dry-run
git diff --check
```

All checks passed.

## Commit

Commit message: `0.1.2`
