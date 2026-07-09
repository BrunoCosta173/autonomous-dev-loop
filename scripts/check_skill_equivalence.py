#!/usr/bin/env python3
"""Check equivalence between the Codex/OpenAI and Claude Skill targets."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CODEX_SKILL = ROOT / ".agents" / "skills" / "autonomous-dev-loop"
CLAUDE_SKILL = ROOT / ".claude" / "skills" / "autonomous-dev-loop"


def _relative_files(directory: Path) -> dict[str, Path]:
    if not directory.exists():
        return {}

    files: dict[str, Path] = {}
    for path in sorted(directory.rglob("*")):
        if path.is_file():
            files[path.relative_to(directory).as_posix()] = path
    return files


def _compare_named_files(label: str, codex_dir: Path, claude_dir: Path) -> list[str]:
    failures: list[str] = []

    codex_files = _relative_files(codex_dir)
    claude_files = _relative_files(claude_dir)

    codex_names = set(codex_files)
    claude_names = set(claude_files)

    for name in sorted(codex_names - claude_names):
        failures.append(f"{label}: missing from Claude target: {name}")

    for name in sorted(claude_names - codex_names):
        failures.append(f"{label}: missing from Codex/OpenAI target: {name}")

    for name in sorted(codex_names & claude_names):
        codex_bytes = codex_files[name].read_bytes()
        claude_bytes = claude_files[name].read_bytes()
        if codex_bytes != claude_bytes:
            failures.append(f"{label}: content differs: {name}")

    return failures


def compare_skill_targets(root: Path = ROOT) -> list[str]:
    """Return a list of equivalence failures."""

    codex_skill = root / ".agents" / "skills" / "autonomous-dev-loop"
    claude_skill = root / ".claude" / "skills" / "autonomous-dev-loop"

    failures: list[str] = []

    for label, directory in (
        ("Codex/OpenAI Skill", codex_skill),
        ("Claude Skill", claude_skill),
    ):
        if not directory.is_dir():
            failures.append(f"{label} directory is missing: {directory.relative_to(root)}")
        if not (directory / "SKILL.md").is_file():
            failures.append(f"{label} SKILL.md is missing")

    if failures:
        return failures

    failures.extend(
        _compare_named_files(
            "references",
            codex_skill / "references",
            claude_skill / "references",
        )
    )
    failures.extend(
        _compare_named_files(
            "assets",
            codex_skill / "assets",
            claude_skill / "assets",
        )
    )

    return failures


def main() -> int:
    failures = compare_skill_targets(ROOT)

    print("Skill equivalence check")
    print("=======================")
    print("Allowed target-specific differences:")
    print("- SKILL.md may contain platform-specific wording.")
    print("- agents/openai.yaml is expected only in the Codex/OpenAI target.")
    print()

    if failures:
        print("FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASSED")
    print("- Reference filenames match.")
    print("- Asset filenames match.")
    print("- Matching reference files are byte-for-byte equivalent.")
    print("- Matching asset files are byte-for-byte equivalent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
