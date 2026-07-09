#!/usr/bin/env python3
"""Run lightweight repository validation for autonomous-dev-loop."""

from __future__ import annotations

from pathlib import Path
import re
import sys

from check_private_content import scan_repository
from check_skill_equivalence import compare_skill_targets


ROOT = Path(__file__).resolve().parents[1]
CURRENT_VERSION = "0.0.9"

CODEX_SKILL = ROOT / ".agents" / "skills" / "autonomous-dev-loop"
CLAUDE_SKILL = ROOT / ".claude" / "skills" / "autonomous-dev-loop"

SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

REQUIRED_REPOSITORY_DOCS = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "PROJECT_BRIEF.md",
    "AGENTS.md",
    "CLAUDE.md",
    "docs/design/repository-structure.md",
    "docs/design/skill-architecture.md",
    "docs/design/packaging-strategy.md",
    "docs/design/compatibility-matrix.md",
    "docs/design/validation-strategy.md",
    "docs/design/release-readiness.md",
]

REQUIRED_INSTALLATION_DOCS = [
    "docs/installation/codex-openai.md",
    "docs/installation/claude-code.md",
    "docs/installation/generic-agents.md",
    "docs/installation/agent-assisted-installation.md",
    "docs/installation/troubleshooting.md",
]

REQUIRED_PLANNING_DOCS = [
    "docs/planning/STEP_0_FOUNDATION.md",
    "docs/planning/STEP_1_REPOSITORY_STRUCTURE.md",
    "docs/planning/STEP_2_INTERNAL_SKILL_ARCHITECTURE.md",
    "docs/planning/STEP_3_PROJECT_CONTROL_TEMPLATES.md",
    "docs/planning/STEP_4_STACK_DETECTION_COMMAND_DISCOVERY.md",
    "docs/planning/STEP_5_AUTONOMY_SAFETY_REVIEW_LOOP.md",
    "docs/planning/STEP_6_OBJECTIVE_INTAKE_KICKOFF.md",
    "docs/planning/STEP_7_GOAL_MEMORY_HANDOFF.md",
    "docs/planning/STEP_8_PACKAGING_INSTALLATION_EXAMPLES.md",
    "docs/planning/STEP_9_VALIDATION_RELEASE_READINESS.md",
]

REQUIRED_EXAMPLES = [
    "examples/nextjs-app/README.md",
    "examples/fastapi-api/README.md",
    "examples/laravel-app/README.md",
]

DISALLOWED_SECRET_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.development",
    ".env.production",
    ".env.test",
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
}

DISALLOWED_SECRET_SUFFIXES = {
    ".key",
    ".pem",
    ".p12",
    ".pfx",
}


def _rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _iter_repository_files(root: Path = ROOT):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def _read_text(path: Path) -> str | None:
    data = path.read_bytes()
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def _check_required_paths(paths: list[str], label: str) -> list[str]:
    failures: list[str] = []
    for relative_path in paths:
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"{label} missing: {relative_path}")
            continue
        text = _read_text(path)
        if text is not None and not text.strip():
            failures.append(f"{label} is empty: {relative_path}")
    return failures


def _parse_frontmatter(path: Path) -> dict[str, str] | None:
    text = _read_text(path)
    if text is None:
        return None

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    try:
        end_index = lines[1:].index("---") + 1
    except ValueError:
        return None

    frontmatter: dict[str, str] = {}
    for line in lines[1:end_index]:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"').strip("'")

    return frontmatter


def _check_skill_targets() -> list[str]:
    failures: list[str] = []

    for label, directory in (
        ("Codex/OpenAI Skill", CODEX_SKILL),
        ("Claude Skill", CLAUDE_SKILL),
    ):
        if not directory.is_dir():
            failures.append(f"{label} directory missing: {_rel(directory)}")
            continue

        skill_md = directory / "SKILL.md"
        if not skill_md.is_file():
            failures.append(f"{label} SKILL.md missing: {_rel(skill_md)}")
            continue

        text = _read_text(skill_md)
        if text is None or not text.strip():
            failures.append(f"{label} SKILL.md is empty or unreadable: {_rel(skill_md)}")
            continue

        frontmatter = _parse_frontmatter(skill_md)
        if frontmatter is None:
            failures.append(f"{label} SKILL.md frontmatter is invalid: {_rel(skill_md)}")
            continue

        for required_key in ("name", "description"):
            if not frontmatter.get(required_key):
                failures.append(
                    f"{label} SKILL.md frontmatter missing {required_key}: {_rel(skill_md)}"
                )

    return failures


def _check_text_hygiene() -> list[str]:
    failures: list[str] = []
    conflict_markers = ("<<<<<<< ", "=======", ">>>>>>> ")

    for path in _iter_repository_files(ROOT):
        rel_path = _rel(path)
        lower_name = path.name.lower()
        lower_suffix = path.suffix.lower()

        if lower_name in DISALLOWED_SECRET_FILE_NAMES:
            failures.append(f"secret-like file should not be tracked: {rel_path}")

        if lower_suffix in DISALLOWED_SECRET_SUFFIXES:
            failures.append(f"secret-like file suffix should not be tracked: {rel_path}")

        text = _read_text(path)
        if text is None:
            continue

        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.endswith(" ") or line.endswith("\t"):
                failures.append(f"trailing whitespace: {rel_path}:{line_number}")
            if line.startswith(conflict_markers):
                failures.append(f"merge conflict marker: {rel_path}:{line_number}")

    return failures


def _check_changelog() -> list[str]:
    changelog = ROOT / "CHANGELOG.md"
    text = _read_text(changelog)
    if text is None:
        return ["CHANGELOG.md is missing or unreadable"]

    if f"## {CURRENT_VERSION}" not in text:
        return [f"CHANGELOG.md does not include {CURRENT_VERSION}"]

    version_headings = re.findall(r"^##\s+(\d+\.\d+\.\d+)\s*$", text, flags=re.MULTILINE)
    if not version_headings:
        return ["CHANGELOG.md does not contain semantic version headings"]

    if version_headings[0] != CURRENT_VERSION:
        return [
            f"CHANGELOG.md latest version is {version_headings[0]}, expected {CURRENT_VERSION}"
        ]

    return []


def _report_section(title: str, failures: list[str]) -> bool:
    if failures:
        print(f"[fail] {title}")
        for failure in failures:
            print(f"  - {failure}")
        return False

    print(f"[ok] {title}")
    return True


def run_validation() -> list[str]:
    failures: list[str] = []

    checks = [
        ("Skill target structure and frontmatter", _check_skill_targets()),
        ("Skill target equivalence", compare_skill_targets(ROOT)),
        ("Private content scan", scan_repository(ROOT)),
        ("Required repository docs", _check_required_paths(REQUIRED_REPOSITORY_DOCS, "repository doc")),
        ("Required installation docs", _check_required_paths(REQUIRED_INSTALLATION_DOCS, "installation doc")),
        ("Required planning docs", _check_required_paths(REQUIRED_PLANNING_DOCS, "planning doc")),
        ("Required example READMEs", _check_required_paths(REQUIRED_EXAMPLES, "example README")),
        ("Changelog current version", _check_changelog()),
        ("Text hygiene", _check_text_hygiene()),
    ]

    print("Repository validation")
    print("=====================")
    for title, check_failures in checks:
        if not _report_section(title, check_failures):
            failures.extend(check_failures)

    return failures


def main() -> int:
    failures = run_validation()

    print()
    if failures:
        print(f"Validation failed with {len(failures)} issue(s).")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
