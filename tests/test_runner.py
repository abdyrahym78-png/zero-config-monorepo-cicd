import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from monoci.runner import run_command_in_packages

class TestRunner(unittest.TestCase):
    def test_run_command_in_packages(self):
        res = run_command_in_packages({}, "echo test")
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()
