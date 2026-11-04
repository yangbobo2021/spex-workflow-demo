"""Black-box tests: every assertion runs the real CLI process."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "add.py"


def run_cli(*args, cwd=None):
    return subprocess.run(
        [sys.executable, "-B", str(SCRIPT), *map(str, args)],
        cwd=cwd, capture_output=True, text=True, timeout=10,
    )


class AdditionCliTests(unittest.TestCase):
    def test_exact_sums(self):
        cases = [
            (2, 3, "5\n"),
            (-2, -3, "-5\n"),
            (0, 0, "0\n"),
            (2147483647, 1, "2147483648\n"),
            (9007199254740992, 1, "9007199254740993\n"),
            (10**18, 10**18, "2000000000000000000\n"),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                result = run_cli(a, b)
                self.assertEqual((result.returncode, result.stdout, result.stderr),
                                 (0, expected, ""))

    def test_invalid_arguments(self):
        for args in [(), (1,), (1, 2, 3), ("x", 2), ("1.5", 2),
                     (1, 2, "--unknown")]:
            with self.subTest(args=args):
                result = run_cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertTrue(result.stderr.strip())

    def test_other_working_directory_stays_empty(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run_cli(2, 3, cwd=directory)
            self.assertEqual((result.returncode, result.stdout, result.stderr),
                             (0, "5\n", ""))
            self.assertEqual(list(Path(directory).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
