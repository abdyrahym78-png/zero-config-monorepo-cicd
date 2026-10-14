import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from monoci.cli import app
from typer.testing import CliRunner

class TestCli(unittest.TestCase):
    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Zero-config Monorepo CI/CD CLI Tool", result.output)

if __name__ == "__main__":
    unittest.main()
