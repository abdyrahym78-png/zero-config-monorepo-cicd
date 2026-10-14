import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from monoci.monorepo import discover_packages, get_affected_packages

class TestMonorepo(unittest.TestCase):
    def test_discover_packages(self):
        pkgs = discover_packages()
        self.assertIsInstance(pkgs, dict)

    def test_get_affected_packages(self):
        packages = {"app1": "apps/app1"}
        changed = ["apps/app1/main.py", "README.md"]
        affected = get_affected_packages(changed, packages)
        self.assertIn("app1", affected)

if __name__ == "__main__":
    unittest.main()
