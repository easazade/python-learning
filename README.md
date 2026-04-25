# Python Notes

This repo is about learning python
Install python using brew:
`brew install python`
export it in path in `.zshrc`:
`export PATH="/opt/homebrew/bin:$PATH"`

`which python` should show the homebrew installation not the one from `/usr/bin/python3`. that is system's installation of python.

## Commands

- Create a python virtual environment using venv: `python3 -m venv .venv`
- Activate venv environment: `source .venv/bin/activate`
- Deactivate environment: `deactivate`
- To make sure python version being used is from environment: `which python3`
- Upgrade pip inside environment: `python -m pip install --upgrade pip`
- Install package: `python -m pip install [package]`
- Uninstall package: `python -m pip uninstall [package]`
- Uninstall package: `python -m pip uninstall [package]`
- Save installed packages to file: `python -m pip freeze > requirements.txt`
- Install dependencies from requirements.txt: `python -m pip install -r requirements.txt`
- List installed packages: `python -m pip list`

## VSCode extensions and settings:

Install these VS Code extensions

- Python by Microsoft
- Pylance by Microsoft
- Python Environments by Microsoft
- Ruff extension
- Even better toml by tamasfe

Update vscode settings:

```json
{
  "python.analysis.autoImportCompletions": true,
  "python.analysis.typeCheckingMode": "strict",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit",
    "source.fixAll": "explicit"
  }
}
```

`defaultInterpreterPath` points VS Code at your project venv.
`autoImportCompletions` enables auto-import suggestions.
`typeCheckingMode` can be `off`, `basic`, or `strict`.

If you're not using `uv` to manage project put this in the `.vscode/settings.json`
`"python.defaultInterpreterPath": "${workspaceFolder}/.venv",`

## Notes:

### pyproject.toml file

Handles these 3 things:

- dependencies
- build system (setuptools, poetry, etc.)
- tool configs (ruff, black, mypy…)

`pyproject.toml` in python is the equivalent of `package.json` in JS or (`pubspec.yaml`+`analysis_options.yaml`+`build.yaml`) in Dart

> **uv** is the project management tool which initializes the project `pyproject.toml` file and `venv` config

Here is how it can look like:

```toml
[project]
name = "fastapi-utils-pro"
version = "0.3.2"
description = "Utilities and helpers for FastAPI projects"
readme = "README.md"
requires-python = ">=3.10"
authors = [
  { name = "Ali Dev", email = "ali@example.com" }
]
license = { text = "MIT" }

dependencies = [
  "fastapi>=0.110",
  "pydantic>=2.0",
  "httpx>=0.25"
]

[project.optional-dependencies]
dev = [
  "pytest",
  "pytest-cov",
  "ruff",
  "mypy"
]

# -----------------------------------

[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

# -----------------------------------

[tool.ruff]
line-length = 100
target-version = "py310"
select = ["E", "F", "I"]  # errors, flakes, import sorting

[tool.ruff.format]
quote-style = "double"

# -----------------------------------

[tool.mypy]
python_version = "3.10"
strict = true
ignore_missing_imports = true

# -----------------------------------

[tool.pytest.ini_options]
addopts = "-ra -q --cov=fastapi_utils_pro"
testpaths = ["tests"]

# -----------------------------------

[tool.coverage.run]
branch = true
source = ["fastapi_utils_pro"]

[tool.coverage.report]
show_missing = true
```

# project management

**uv** is the tool for project management. It's similar to `npm`

Here are some of its most used commands:

- Create a new Python project in the current directory: `uv init `
- Create a new Python project at the specified path: `uv init project`
- Add a new dependency to the project: `uv add package`
- Remove a dependency from the project: `uv remove package`
- Run a script or a command in the project's environment: `uv run path/to/script.py|command`
- Update a project's environment from `pyproject.toml`: `uv sync`
- Create a lock file for the project's dependencies: `uv lock`
- Build the project into source and binary distributions: `uv build`

## How to install uv and init a project:

- Install uv using curl `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Create a new project `uv init my_project && cd my_project`

Now you'll have a project with a pyproject.toml ready to manage

- run `uv sync`. It is same as `flutter pub get` or `npm install`.
  With uv you don't need to call `source .venv/bin/activate`. uv manages that.
- All uv sub-command calls use python from virtual environment that it creates and manages.
- to call python commands or scripts call: `uv run path/to/script.py|command`

Now you can run a python script using `uv`
`uv run python --version`

If you're using vscode. First make sure `.venv` file is created by `uv` then hit `Cmd+Shift+P` to open command prompt and search for `Python:Select Interpreter` make sure the python path that is selected is from workspace `.venv/bin/python`. This will make vscode to use the python from `.venv` or virtual environment managed by **uv** which should be automatically recognized and chosen by vscode itself.

**NOTE:** If for any reason you need to force the python version on vscode you can do so by
putting this in the `.vscode/settings.json`

```json
"python.defaultInterpreterPath": "${workspaceFolder}/.venv",
```

## Lint & Format

This is done by **Ruff**

> Need to have uv installed first. And need to have the vscode extension of it installed and add the recommended vs-code global config to your IDE. checkout above

- run `uv add --dev ruff`

Add ruff config to `pyproject.toml`

```toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I"]
fixable = ["ALL"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

This gives you:

- E = style/pycodestyle-type checks
- F = common correctness checks like undefined names
- I = import sorting
- formatting rules for consistent code layout

Now you can run ruff:

- `uv run ruff check .`
- `uv run ruff check . --fix`
- `uv run ruff format .`


## Type lints (pyright)
Ruff has a few rules (like flagging missing annotations with ANN rules), but it does not do actual type inference or type checking at compile time.
For that we need to use pylance.

> **NOTE:** First make sure you have pylance plugin installed on vscode

- Install pyright
`uv add --dev pyright`
- Add its configuration to pyproject.toml
```toml
# pyproject.toml
[tool.pyright]
include        = ["src"]
exclude        = [".venv", "**/__pycache__"]
venvPath       = "."
venv           = ".venv"
typeCheckingMode = "standard"
```

Now you can run pyright:
`uv run pyright`

