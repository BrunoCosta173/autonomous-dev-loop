# Step 11 Release Candidate README

Status: **Completed**

## Step Purpose

Prepare the first release candidate structure for `autonomous-dev-loop`.

This step organizes the public README, release candidate checklist, and draft release notes so the project is ready for final review before merging to `main` and publishing the first release.

## README Structure Decisions

The README was reworked into a release-candidate public structure:

1. Project title
2. Short tagline
3. What it does
4. Why it exists
5. Key features
6. How it works
7. Quick install
8. Install for Codex/OpenAI
9. Install for Claude Code
10. Install for generic agents
11. Agent-assisted installation
12. Basic usage examples
13. Autonomy levels
14. Safety gates
15. Review Subagent Loop
16. Goal Completion Mode
17. Persistent project memory
18. Supported stacks
19. Validation and CI
20. Packaging
21. Roadmap
22. Contributing
23. License

## User Install Versus Agent Install

For end users and vibe-coders, the README prominently offers one-command install as the easiest path.

For agents and agent-assisted installation, documentation prefers transparent installation:

- Inspect the repository.
- Confirm the target agent environment.
- Use the local installer or manual copy.
- Avoid piping remote scripts into a shell unless explicitly authorized.
- Verify installed files.
- Report what changed.

## Main Branch Latest Channel

The README uses GitHub raw links from the `main` branch for public one-command install examples.

This makes `main` the latest channel for users.

## Tagged Release Reproducibility

The README states that tagged releases should be used for reproducible installs when available.

This keeps one-command install convenient without presenting it as safer than local or tagged installation.

## Release Candidate Checklist

Step 11 adds:

```text
docs/release/RELEASE_CANDIDATE_CHECKLIST.md
```

The checklist covers required checks, manual smoke tests, and release blockers.

## Release Notes Draft

Step 11 adds:

```text
docs/release/RELEASE_NOTES_0.0.11.md
```

These are draft release notes only. They are not a published GitHub release.

## Known Limitations

Step 11 does not:

- Publish a GitHub release.
- Merge into `main`.
- Create a pull request.
- Add complete example applications.
- Add external dependencies.
- Claim marketplace or plugin availability.
- Claim universal support for real subagents.
- Claim `/goal` is universally available.

## Future Improvements

Future steps may add:

- Final pre-merge review.
- Release candidate validation.
- PR preparation.
- First tagged release.
- More example walkthroughs.
- Additional release packaging polish.

## Completion Criteria

Step 11 is complete because the README is release-candidate ready, one-command and agent-assisted install positioning are documented, release checklist and draft release notes exist, release-readiness docs are updated, and validation includes the new release candidate files.
