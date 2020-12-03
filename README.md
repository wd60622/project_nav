
# Project Navigation

This project helps navigate between projects in the command line.

## How to Use

### `add_project` Function

There are two ways to add a new project. Both rely on the function `add_project`.

#### Specify Destination

```zsh
add_project <alias> <location>
```

When specifying a location relative to the home directory, the alias name becomes a command to navigate to that directory.

#### Current Directory

```zsh
add_project <alias>
```

Running `add_project` with just an alias creates a shortcut to the current directory.

### Navigation

Simply type one of the project aliases that were added in the terminal.

For instance, after running `add_project Desktop Desktop`, the alias `Desktop` changes to the Desktop.

### `projects` Function

List current projects that are aliased. This can be useful when navigating to old projects.

```zsh
projects
# Desktop:location/to/Desktop
```


## Setup

The `setup.sh` script covers all the setup before use. Clone the repo and run the following commands.

```zsh
git clone <repo_name>
cd project_nav
source setup.sh
```
