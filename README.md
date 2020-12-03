
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

For instance, after running `add_project Desktop Desktop`, the command `Desktop` changes to the Desktop in the terminal.

#### Current Directory

```zsh
add_project <alias>
```

Running `add_project` with just an alias creates a shortcut to the current directory.

If I am currently in the directory `~/Desktop/CodeReview/` and would like make an alias `code_review`, the command `add_project code_review` will create the alias.

### `projects` Function

There is the functionality to list all the projects that have aliases. This can be useful when navigating to old projects.

```zsh
projects
# Desktop:location/to/Desktop
# code_review:location/to/Desktop/CodeReview
```

### `make_alias.sh` File

Any alias that is created is stored in the file `make_alias.sh`. This file is run upon terminal start up.

Any projects added will automatically get appended to this file.


## Setup

The `setup.sh` script covers all the setup before use. Clone the repo and run the following commands.

```zsh
git clone <repo_name>
cd project_nav
source setup.sh
```
