import unittest
import subprocess
import tempfile
import os
import shutil
from pathlib import Path
from src.monoci.git_utils import get_changed_files

class TestGitUtils(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)
        
        # Initialize git repo
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test User"], check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], check=True, capture_output=True)
        
        # Create initial commit
        Path("file1.txt").write_text("hello")
        subprocess.run(["git", "add", "file1.txt"], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "initial commit"], check=True, capture_output=True)
        
        # Create second commit
        Path("file2.txt").write_text("world")
        subprocess.run(["git", "add", "file2.txt"], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "second commit"], check=True, capture_output=True)

    def tearDown(self):
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_get_changed_files(self):
        files = get_changed_files("HEAD~1", "HEAD")
        self.assertIn("file2.txt", files)

if __name__ == "__main__":
    unittest.main()
