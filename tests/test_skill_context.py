from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents" / "skills" / "agentmaxxing" / "scripts" / "context.py"


class ContextScriptTests(unittest.TestCase):
    def run_script(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_init_and_check(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_script(
                "init",
                "--root",
                directory,
                "--project",
                "Example Project",
                "--goal",
                "Ship one bounded change",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("3 created, 0 preserved", result.stdout)

            check = self.run_script("check", "--root", directory)
            self.assertEqual(check.returncode, 0, check.stderr)

    def test_init_preserves_existing_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = self.run_script("init", "--root", directory)
            self.assertEqual(first.returncode, 0, first.stderr)
            state = Path(directory) / ".agentmaxxing" / "state.md"
            state.write_text("user-owned\n", encoding="utf-8")

            second = self.run_script("init", "--root", directory)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(state.read_text(encoding="utf-8"), "user-owned\n")
            self.assertIn("0 created, 3 preserved", second.stdout)

    def test_check_reports_missing_context(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_script("check", "--root", directory)
            self.assertEqual(result.returncode, 1)
            self.assertIn("missing file", result.stderr)


if __name__ == "__main__":
    unittest.main()
