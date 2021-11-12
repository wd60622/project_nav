
# Project Navigation

This project helps navigate between projects in the command line.

## Setup

The `setup.sh` script covers all the setup. Clone the repo and run the following commands.

```zsh
git clone https://github.com/wdeanHPA/project_nav.git
cd project_nav
source setup.sh
```

This will add a sourcing command to your start-up script and create the `nav` command.

This project requires `zsh` shell as well as `python` and `pip`.

## How To Use

Type `nav` to see the whole list of commands available.

### Creating Project Aliases

The `nav create` command will create an alias for a project from the command line. It can be used in a few ways.

#### 1. Create an alias for the current directory
The command `nav create <alias>` creates an alias to navigate to the *current working directory* with the given alias.

That is, after reloading the terminal, typing `<alias>` in the terminal will `cd` into the previous working directory.

#### 2. Create an alias for specific directory

The `destination` option will specify where the alias will `cd`. Here is an example to create a Desktop alias.

```shell
nav create --destination $HOME/Desktop <desktop-alias>
```

**NOTE:** The `$HOME` keyword can be used in the destination. By default, `$HOME` and `~` are replaced with the environment variable `$HOME`.

### Grouping the Aliases

Each project has a group name which has a default name `General`. If some other group name is desired, the `group-name` option can be specified.

Below is example of creating a project alias under a `Projects` group from within that projects root folder.

```shell
nav create --group-name Projects <project-alias>
```

### Viewing Aliases

The `nav list` command will display all defined shortcuts.

They are stored in the hidden folder `~/.nav` in the yaml file `make_alias.yaml`. To view the file, use the command `nav open`. This file can be alternative way to create and modifying project shortcuts.


### The Alias File

The `make_alias.yaml` file contains two sections: `folders` and `aliases`.

The `folders` sections contains each group and all the aliases created and the `aliases` section defines additional shortcuts to be used in the shortcuts.

Below is an example of that file.

```
aliases:
    DESKTOP: $HOME/Desktop
    PROJECTS: $DESKTOP/Markets

folders:
    General:
        Desktop: $DESKTOP
        Misc: $DESKTOP/Misc
        Downloads: $HOME/Downloads

    Projects:
        first_project: $PROJECTS/first_project
        second_project: $PROJECTS/second_project
```

In this example file, the `DESKTOP` and `PROJECTS` aliases are defined. These are not shortcuts but can be used like the `$HOME` and `~` variables. Any abbreviations of folders can be defined in `aliases` section of the file.

This file also defines shortcuts for the Desktop, Misc, and Downloads folders in the `General` group as well as two project folders in the `Projects` group.
