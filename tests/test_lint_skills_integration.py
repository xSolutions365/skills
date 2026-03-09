from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINT_SCRIPT = REPO_ROOT / "scripts" / "lint_skills.py"
FIXTURES_ROOT = REPO_ROOT / "tests" / "fixtures" / "lint_skills"


class LintSkillsIntegrationTest(unittest.TestCase):
    def run_lint(self, fixture_name: str) -> subprocess.CompletedProcess[str]:
        fixture_root = FIXTURES_ROOT / fixture_name
        self.assertTrue(fixture_root.is_dir(), f"missing fixture repo: {fixture_root}")
        return subprocess.run(
            [sys.executable, str(LINT_SCRIPT), "--root", str(fixture_root)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_compact_skill_fixture_passes(self) -> None:
        result = self.run_lint("compact_repo")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("skills: lint passed", result.stdout)

    def test_structured_skill_fixture_passes(self) -> None:
        result = self.run_lint("structured_repo")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("skills: lint passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
