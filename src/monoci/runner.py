import shlex
import subprocess
from pathlib import Path
from typing import Dict
from rich.console import Console

console = Console()

def run_command_in_packages(
    packages: Dict[str, str], command: str, root_dir: str = "."
):
    """Выполняет команду в каждом из указанных пакетов."""
    success = True
    for pkg_name, pkg_path in packages.items():
        console.print(
            f"\n[bold blue]▶ Running '{command}' in [{pkg_name}]...[/]"
        )
        full_path = Path(root_dir) / pkg_path
        try:
            cmd_parts = shlex.split(command)
            subprocess.run(
                cmd_parts, cwd=full_path, check=True, capture_output=False
            )
            console.print(f"[green]✔ Success in {pkg_name}[/]")
        except subprocess.CalledProcessError:
            console.print(f"[red bold]✖ Failed in {pkg_name}[/]")
            success = False
    return success
