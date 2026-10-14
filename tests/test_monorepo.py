import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from monoci.monorepo import discover_packages

class TestMonorepo(unittest.TestCase):
    def test_discover_packages(self):
        pkgs = discover_packages()
        self.assertIsInstance(pkgs, dict)

if __name__ == "__main__":
    unittest.main()
