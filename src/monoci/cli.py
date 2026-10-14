import typer
from rich.console import Console
from .git_utils import get_changed_files
from .monorepo import discover_packages, get_affected_packages
from .runner import run_command_in_packages

app = typer.Typer(
    help="Zero-config Monorepo CI/CD CLI Tool", add_completion=False
)
console = Console()

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Zero-config Monorepo CI/CD CLI Tool"""
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())

@app.command()
def affected(
    base: str = typer.Option(
        "HEAD~1", help="Базовый коммит или ветка для сравнения"
    ),
    head: str = typer.Option("HEAD", help="Целевой коммит или ветка"),
):
    """Показать пакеты, затронутые изменениями."""
    console.print("[bold]🔍 Analyzing git changes...[/]")
    changed_files = get_changed_files(base, head)
    packages = discover_packages()
    affected_pkgs = get_affected_packages(changed_files, packages)
    console.print(f"\n[yellow]📄 Changed files ({len(changed_files)}):[/]")
    for f in changed_files[:15]:
        console.print(f"  - {f}")
    
    if len(changed_files) > 15:
        console.print(f"  ... и еще {len(changed_files) - 15} файлов")

    console.print(f"\n[green]📦 Affected packages ({len(affected_pkgs)}):[/]")
    for name, path in affected_pkgs.items():
        console.print(f"  - {name} ({path})")

if __name__ == "__main__":
    app()
