"""Run the real program once and check its complete result."""

from pathlib import Path
import subprocess
import sys
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "hello.py"


class HelloTests(unittest.TestCase):
    def test_default_output(self):
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT)],
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual((result.returncode, result.stdout, result.stderr),
                         (0, "hello\n", ""))


if __name__ == "__main__":
    unittest.main()
