# Skill Architecture

`autonomous-dev-loop` uses a dual Skill architecture for version `0.0.1`.

## Installation Targets

The repository maintains two Skill entry points:

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/SKILL.md`
- Claude Code: `.claude/skills/autonomous-dev-loop/SKILL.md`

Each target exists because different agent environments may expect different local installation paths and project conventions.

## Behavioral Equivalence

The Codex/OpenAI and Claude Code Skill versions must remain behaviorally equivalent.

Behavioral equivalence means:

- They describe the same purpose.
- They guide the same autonomous development loop.
- They use the same safety gate model.
- They support the same project categories.
- They differ only where the target agent environment requires different wording or metadata.

The two Skill files should not drift into separate products.

## Placeholder Status

In version `0.0.1`, both Skill files are minimal placeholders.

They exist to establish the repository architecture and installation targets. They do not yet contain the full autonomous development loop behavior.

## Deferred Sync Strategy

No sync or build script is included in version `0.0.1`.

This is intentional. The project first needs a clear internal Skill design before introducing automation that copies, transforms, or validates content across Skill targets.

Future versions may add:

- A sync script to compare or update both Skill files.
- A build step that generates target-specific Skill files from shared source content.
- A validation command to check behavioral equivalence.
- A terminal installer for supported agent environments.

## References And Assets

Both Skill targets include reserved `references/` and `assets/` directories.

Planned use:

- `references/`: detailed guidance loaded by an agent only when needed.
- `assets/`: templates or other files used as output resources.

These directories are intentionally empty in Step 1.

## Design Constraint

Keep installable Skill folders focused.

Public documentation, planning notes, installation guides, and contribution instructions belong in `docs/` or root-level files, not inside the Skill folders.
