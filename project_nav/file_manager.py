from yaml import load, Loader, dump

from pathlib import Path

from project_nav.data_models import Project, Aliases, Groups

NAV_DIR = Path.home() / ".nav"
if not NAV_DIR.exists():
    NAV_DIR.mkdir()


class ShellManager:
    file = NAV_DIR / "make_alias.sh"

    def save(self, data: str):
        with open(self.file, "w") as f:
            f.write(data)


class YAMLManager:
    """Class to interact with the YAML file.

    Example YAML file:
    ---
    projects:
        General:
            Desktop: $DESKTOP/Misc

        Group 1:
            project_1: $PROJECT_FOLDER/project_1
            project_2: $PROJECT_FOLDER/project_2

    aliases:
        DESKTOP: $HOME/Desktop
        PROJECT_FOLDER: $DESKTOP/projects

    The above file generates three different projects aliases. For navigation to:
        1. Desktop
        2. project_1
        3. project_2

    """

    file = NAV_DIR / "make_alias.yaml"
    min_key = "folders"

    def __init__(self):
        self.raw_data = self._load_file()

    def _load_file(self):
        """Return the dictionary form of the YAML file."""
        if not self.file.exists():
            return {self.min_key: dict()}

        with open(self.file, "r") as f:
            data = load(f, Loader)

        return data

    def parse_raw_data(self):
        """Split the file into projects and aliases."""
        self.aliases = self.raw_data.get("aliases", dict())
        aliases = Aliases.from_dictionary(self.aliases)

        try:
            self.folders = self.raw_data[self.min_key]
        except:
            raise KeyError(
                f'The navigation file must at a minimum have a "{self.min_key}" section. Edit the {self.file}.'
            )

        groups = Groups.from_dictionary(self.folders)
        groups.resolve_aliases(aliases)

        return aliases, groups

    def save(self):
        data = {self.min_key: self.folders, "aliases": self.aliases}

        with open(self.file, "w") as f:
            dump(data, f)

    def add_project_nav(self, project_alias: Project, group_name: str):
        if not group_name in self.folders:
            self.folders[group_name] = dict()

        self.folders[group_name][project_alias.alias_name] = project_alias.alias_value

        self.save()
