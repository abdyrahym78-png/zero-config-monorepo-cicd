import os
from pathlib import Path
from typing import Dict, List

def discover_packages(root_dir: str = ".") -> Dict[str, str]:
    """Автоматически находит пакеты в стандартных директориях монорепозитория.
    Ищет индикаторы: package.json, pyproject.toml, Cargo.toml, pom.xml
    """
    packages = {}
    search_dirs = ["apps", "packages", "libs", "services", "modules"]
    indicators = [
        "package.json",
        "pyproject.toml",
        "Cargo.toml",
        "pom.xml",
        "go.mod",
    ]
    for d in search_dirs:
        dir_path = Path(root_dir) / d
        if not dir_path.exists() or not dir_path.is_dir():
            continue
        for item in dir_path.iterdir():
            if item.is_dir():
                for indicator in indicators:
                    if (item / indicator).exists():
                        packages[item.name] = str(item.relative_to(root_dir))
                        break
    return packages
