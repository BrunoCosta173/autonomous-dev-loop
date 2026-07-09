#!/usr/bin/env python3
"""Standard-library tests for scripts/install.py."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.py"


def run_installer(*args: str, expect_success: bool = True, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(INSTALLER), *args]
    result = subprocess.run(
        command,
        cwd=cwd or ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if expect_success and result.returncode != 0:
        raise AssertionError(
            f"Expected success for {' '.join(command)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    if not expect_success and result.returncode == 0:
        raise AssertionError(f"Expected failure for {' '.join(command)}")
    return result


def assert_exists(path: Path) -> None:
    if not path.exists():
        raise AssertionError(f"Expected path to exist: {path}")


def assert_missing(path: Path) -> None:
    if path.exists():
        raise AssertionError(f"Expected path to be missing: {path}")


def test_project_codex_install() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "codex", "--project-dir", str(project))
        assert_exists(project / ".agents" / "skills" / "autonomous-dev-loop" / "SKILL.md")


def test_project_claude_install() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "claude", "--project-dir", str(project))
        assert_exists(project / ".claude" / "skills" / "autonomous-dev-loop" / "SKILL.md")


def test_project_both_install() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "both", "--project-dir", str(project))
        assert_exists(project / ".agents" / "skills" / "autonomous-dev-loop" / "SKILL.md")
        assert_exists(project / ".claude" / "skills" / "autonomous-dev-loop" / "SKILL.md")


def test_generic_adapter_install() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "generic", "--project-dir", str(project))
        assert_exists(project / "AGENTS.md")
        assert_exists(project / "GENERIC_AGENT.md")
        assert_missing(project / "CLAUDE.md")


def test_dry_run_does_not_create_files() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "codex", "--project-dir", str(project), "--dry-run")
        assert_missing(project / ".agents")


def test_shell_wrapper_dry_run() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        result = subprocess.run(
            ["sh", str(ROOT / "install.sh"), "--target", "codex", "--scope", "project", "--dry-run"],
            cwd=project,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode != 0:
            raise AssertionError(
                f"Expected shell wrapper dry-run to succeed\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
            )
        assert_missing(project / ".agents")


def test_existing_destination_without_force_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "codex", "--project-dir", str(project))
        run_installer("--target", "codex", "--project-dir", str(project), expect_success=False)


def test_existing_destination_with_force_succeeds() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "codex", "--project-dir", str(project))
        run_installer("--target", "codex", "--project-dir", str(project), "--force")
        assert_exists(project / ".agents" / "skills" / "autonomous-dev-loop" / "SKILL.md")


def test_update_existing_install_succeeds() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "codex", "--project-dir", str(project))
        run_installer("--action", "update", "--target", "codex", "--project-dir", str(project), "--yes")
        assert_exists(project / ".agents" / "skills" / "autonomous-dev-loop" / "SKILL.md")


def test_uninstall_removes_known_skill_folders() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "both", "--project-dir", str(project))
        run_installer("--action", "uninstall", "--target", "both", "--project-dir", str(project), "--yes")
        assert_missing(project / ".agents" / "skills" / "autonomous-dev-loop")
        assert_missing(project / ".claude" / "skills" / "autonomous-dev-loop")


def test_uninstall_skips_user_modified_adapters_unless_force() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp)
        run_installer("--target", "generic", "--project-dir", str(project))
        agents = project / "AGENTS.md"
        agents.write_text(agents.read_text(encoding="utf-8") + "\nLocal project note.\n", encoding="utf-8")

        run_installer(
            "--action",
            "uninstall",
            "--target",
            "generic",
            "--project-dir",
            str(project),
            "--with-adapters",
            "--yes",
        )
        assert_exists(agents)
        assert_missing(project / "GENERIC_AGENT.md")

        run_installer(
            "--action",
            "uninstall",
            "--target",
            "generic",
            "--project-dir",
            str(project),
            "--with-adapters",
            "--force",
        )
        assert_missing(agents)


def main() -> int:
    tests = [
        test_project_codex_install,
        test_project_claude_install,
        test_project_both_install,
        test_generic_adapter_install,
        test_dry_run_does_not_create_files,
        test_shell_wrapper_dry_run,
        test_existing_destination_without_force_fails,
        test_existing_destination_with_force_succeeds,
        test_update_existing_install_succeeds,
        test_uninstall_removes_known_skill_folders,
        test_uninstall_skips_user_modified_adapters_unless_force,
    ]

    for test in tests:
        test()
        print(f"[ok] {test.__name__}")

    print("Installer tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
