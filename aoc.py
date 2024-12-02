import importlib
from pathlib import Path
from typing import Annotated
import typer
from rich.console import Console

err_console = Console(stderr=True)


def cli(year: int, day: int, part: Annotated[int, typer.Argument()] = 1):
    year_dir = Path("src", str(year))
    if not year_dir.exists():
        err_console.print(f"Year {year} does not exist")
        return
    day_file = Path(year_dir, f"day{day}.py")
    if not day_file.exists():
        err_console.print(f"Day {day} does not exist")
        return
    if part not in [1, 2]:
        err_console.print(f"Part {part} does not exist")
        return
    module = importlib.import_module(f"src.{year}.day{day}")
    func_name = "solve"
    if part == 2:
        func_name += "2"
    func = getattr(module, func_name)

    print(f"Running Advent of Code solution from year {year}, day {day}; part {part}")
    func()


if __name__ == "__main__":
    typer.run(cli)
