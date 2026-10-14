import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from monoci.git_utils import get_changed_files

class TestGitUtils(unittest.TestCase):
    def test_get_changed_files(self):
        files = get_changed_files()
        self.assertIsInstance(files, list)

if __name__ == "__main__":
    unittest.main()
