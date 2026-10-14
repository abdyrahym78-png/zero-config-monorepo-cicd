import subprocess
from typing import List

def get_changed_files(base: str = "HEAD~1", head: str = "HEAD") -> List[str]:
    """Возвращает список файлов, измененных между двумя коммитами/ветками."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", base, head],
            capture_output=True,
            text=True,
            check=True,
        )
        return [f.strip() for f in result.stdout.splitlines() if f.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Error getting changed files: {e}")
        return []
