import typer
from rich.console import Console
from .git_utils import get_changed_files
from .monorepo import discover_packages
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
    console.print(f"Discovered packages: {list(packages.keys())}")
    console.print(f"Changed files: {changed_files}")

if __name__ == "__main__":
    app()
