# Release Notes 0.1.2

Status: Draft release notes for the `0.1.2` documentation patch.

## Overview

`0.1.2` is a documentation-focused patch that improves README clarity and human-facing polish.

No Skill behavior, installer logic, validation scripts, or packaging were changed.

## What changed

- **Added "What this installs" section**: a clear table showing installed files per target, plus an explanation that the installer only adds instructions and templates.
- **Added "What it does" section**: step-by-step breakdown of the agent workflow in plain English.
- **Added "How to use it after installing" section**: a concrete example prompt and what to expect from the agent.
- **Added "When to use it" section**: a table matching task types to concrete examples.
- **Added "When not to use it" section**: cases where the full loop is unnecessary.
- **Improved "How the loop works" section**: added a visual ASCII diagram showing the vertical flow.
- **Improved safety model explanation**: made safety gates more prominent with explicit categories.
- **Added "Project control files" section**: a table of all file types with purposes and usage policy.
- **Added "Review before done" section**: made the review cycle explicit with a clear flow diagram.
- **Expanded usage examples** to 4 with A0 review-only and continuation modes.
- **Updated version references** from `0.1.1` to `0.1.2`.
- Added Step 15 planning documentation.
- Updated README documentation links to point to `0.1.2` release notes.

## What was not changed

- Skill behavior.
- References and assets.
- Installer, update, uninstall, packaging, and validation scripts.
- CI workflows.
- Published `v0.1.0` and `v0.1.1` releases remain unchanged.

## Installation

Installation is unchanged from `0.1.1`:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target codex --scope project
```

## Validation

All repository validation, Skill equivalence, private-content scanning, installer tests, and packaging tests pass.

## Next steps

After merge and tag, publish `v0.1.2` as a GitHub release.
