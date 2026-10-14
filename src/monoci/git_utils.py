import subprocess

def get_changed_files(base: str = "HEAD~1", head: str = "HEAD") -> list[str]:
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
        raise RuntimeError(f"Git command failed: {e.stderr}")
