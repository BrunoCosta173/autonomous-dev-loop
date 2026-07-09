#!/usr/bin/env python3
"""Scan repository text files for obvious private or secret-like content."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    "dist",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

DISALLOWED_FILE_NAMES = {
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

DISALLOWED_SUFFIXES = {
    ".key",
    ".pem",
    ".p12",
    ".pfx",
}

CONTENT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "absolute local path",
        re.compile(r"(?<![\w/])(?:/home/[A-Za-z0-9._-]+|/Users/[A-Za-z0-9._-]+|[A-Za-z]:\\Users\\[A-Za-z0-9._-]+)"),
    ),
    ("OpenAI-style API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    (
        "private key block",
        re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    ),
    (
        "secret assignment",
        re.compile(
            r"\b(?:api[_-]?key|token|secret|password|private[_-]?key)\s*=\s*['\"]?[^'\"\s<>`]{8,}",
            re.IGNORECASE,
        ),
    ),
    (
        "private company placeholder",
        re.compile(r"\b(?:" + "|".join(
            re.escape(marker)
            for marker in (
                "PRIVATE_" + "COMPANY",
                "INTERNAL_" + "ONLY",
                "CONFIDENTIAL_" + "COMPANY",
                "COMPANY_" + "INTERNAL",
                "CLIENT_SECRET_" + "VALUE",
            )
        ) + r")\b"),
    ),
)


def _iter_repository_files(root: Path):
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


def scan_repository(root: Path = ROOT) -> list[str]:
    """Return private-content findings without printing secret values."""

    findings: list[str] = []

    for path in _iter_repository_files(root):
        rel = path.relative_to(root).as_posix()
        lower_name = path.name.lower()
        lower_suffix = path.suffix.lower()

        if lower_name in DISALLOWED_FILE_NAMES:
            findings.append(f"{rel}: disallowed secret-like filename: {path.name}")

        if lower_suffix in DISALLOWED_SUFFIXES:
            findings.append(f"{rel}: disallowed secret-like file suffix: {path.suffix}")

        text = _read_text(path)
        if text is None:
            continue

        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in CONTENT_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{rel}:{line_number}: {label}")

    return findings


def main() -> int:
    findings = scan_repository(ROOT)

    print("Private content scan")
    print("====================")

    if findings:
        print("FAILED")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("PASSED")
    print("- No obvious private, company-specific, environment-specific, or secret-like content found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
