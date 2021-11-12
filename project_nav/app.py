import typer

import os

from rich import print

from typing import Optional

from project_nav.file_manager import YAMLManager, ShellManager
from project_nav.data_models import Project

app = typer.Typer()

yaml = YAMLManager()
shell = ShellManager()
aliases, parsed_groups = yaml.parse_raw_data()

shell.save(parsed_groups.shell())


@app.command()
def groups():
    """List all the groups."""
    typer.clear()
    for group in parsed_groups.list_groups():
        print(group)


@app.command()
def list(group_name: Optional[str] = None):
    """List the navigation destinations."""
    typer.clear()
    if group_name is not None:
        print(parsed_groups.filter([group_name]))
    else:
        print(parsed_groups)


@app.command()
def create(
    alias: str, destination: Optional[str] = None, group_name: Optional[str] = None
):
    """Create a new navigation destination."""
    project = Project(alias, destination)
    project.resolve(aliases)

    if not project.exists():
        print("This destination doesn't exist!")
        raise typer.Exit()

    if group_name is None:
        group_name = "General"

    yaml.add_project_nav(project, group_name)
    parsed_groups.add_project(project, group_name)

    shell.save(parsed_groups.shell())

    print(f"Creating alias {alias}.")


@app.command()
def check():
    """Check that all the projects exist."""
    errors = False
    for group in parsed_groups:
        for project in group.projects:
            if not project.exists():
                print(project.alias_name, "has an error with", project.alias_value)
                errors = True

    if not errors:
        print("All the projects exist!")


@app.command()
def open():
    """Open navigation yaml file."""
    os.system(f"vim {yaml.file}")
