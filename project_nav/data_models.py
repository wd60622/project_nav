from __future__ import annotations

import os

from typing import Optional

from pathlib import Path


class NotResolvedError(Exception):
    """Alias still contains a references to another."""


def resolve_aliases(aliases, others):
    while any(alias.has_reference for alias in aliases):
        for alias in aliases:
            for other in others:
                alias.replace_reference(other)


class Alias:
    def __init__(self, alias_name: str, alias_value: Optional[str] = None):
        self.alias_name = alias_name
        self.alias_value = alias_value or str(Path.cwd())

    def __repr__(self) -> str:
        return f"{self.alias_name} {self.alias_value}"

    def exists(self):
        if self.has_reference:
            raise NotResolvedError("This Alias has not been resolved yet.")

        return Path(self.alias_value).exists()

    def resolve(self, aliases: Aliases):
        for alias in aliases:
            self.replace_reference(alias)

    @property
    def has_reference(self) -> bool:
        return "$" in self.alias_value

    @property
    def alias_key(self):
        return "~" if self.alias_name == "~" else f"${self.alias_name}"

    def replace_reference(self, other):
        self.alias_value = self.alias_value.replace(other.alias_key, other.alias_value)


def resolve_aliases(aliases, others):
    while any(alias.has_reference for alias in aliases):
        for alias in aliases:
            for other in others:
                alias.replace_reference(other)


class Aliases:
    def __init__(self, aliases: list[Alias]):
        self.aliases = aliases

        self.resolve_aliases()

    def __iter__(self):
        return iter(self.aliases)

    @classmethod
    def from_dictionary(cls, values: dict):
        aliases = [Alias(key, value) for key, value in values.items()]
        aliases += [
            Alias("HOME", os.environ["HOME"]),
            Alias("~", os.environ["HOME"]),
        ]

        return cls(aliases)

    def resolve_aliases(self):
        resolve_aliases(self.aliases, self.aliases)


class Project(Alias):
    def create_sh_alias(self) -> str:
        return f"alias {self.alias_name}='cd {self.alias_value}'"

    def valid_location(self) -> bool:
        return Path(self.alias_value).exists()


class Group:
    def __init__(self, group_name: str, projects: list[Project]):
        self.group_name = group_name
        self.projects = projects

    def __repr__(self) -> str:
        s = f"{self.group_name}\n"
        for project in self.projects:
            s += f"    {project}\n"

        return s.strip()

    def shell(self):
        s = f"# {self.group_name}\n"
        for project in self.projects:
            s += f"{project.create_sh_alias()}\n"

        return s.strip()


class Groups:
    def __init__(self, groups: list[Group]):
        self.groups = groups

    def __repr__(self) -> str:
        return "\n".join(f"{group}\n" for group in self.groups).strip()

    def __iter__(self):
        return iter(self.groups)

    def __contains__(self, value: str):
        return value in self.list_groups()

    def shell(self):
        return "\n".join(group.shell() for group in self.groups)

    def list_groups(self):
        return [group.group_name for group in self.groups]

    def filter(self, groups: list[str]):
        """Filter based on group name."""
        return Groups(group for group in self.groups if group.group_name in groups)

    def add_project(self, project: Project, group_name: str):
        for group in self:
            if group.group_name == group_name:
                group.projects.append(project)
                return

        self.groups.append(Group(group_name=group_name, projects=[project]))

    @classmethod
    def from_dictionary(cls, groups: dict):
        groups = [
            Group(
                group_name=group_name,
                projects=[
                    Project(alias_name=alias_name, alias_value=alias_value)
                    for alias_name, alias_value in projects.items()
                ],
            )
            for group_name, projects in groups.items()
        ]

        return cls(groups)

    def resolve_aliases(self, aliases: Aliases):
        [resolve_aliases(group.projects, aliases.aliases) for group in self.groups]
