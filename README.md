# Firefly Engine

Firefly is a modern game engine in python.

[![CI](https://github.com/ambye85/firefly/workflows/CI/badge.svg?branch=master)]()
[![codecov](https://codecov.io/gh/ambye85/firefly/branch/master/graph/badge.svg)](https://codecov.io/gh/ambye85/firefly)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Development - getting started

Clone the repo, then install all necessary dependencies:

```shell script
poetry install
```

We use various linting, typing and testing tools to help maintain a high quality codebase.
These tools are executed during CI to check that the code meets our minimum standards.
Developers should run these checks locally prior to pushing changes.

### Linting

We use [black](https://github.com/psf/black) to provide a consistent formatting for all source code files.
[Flake8](https://gitlab.com/pycqa/flake8) provides additional linting.

Linting is executed by the following commands:

```shell script
poetry run black .
poetry run flake8 src tests
```

### Testing

Firefly's test suite can be run using the following command:

```shell script
poetry run pytest -v
```

Test coverage reports can be generated for the project:

```shell script
poetry run coverage run -m pytest
poetry run coverage combine
poetry run coverage report
```

We configure coverage to run in parallel in [pyproject.toml](pyproject.toml), so we need to combine reports prior to viewing the results.
Coverage reports should not be committed but will be generated during CI and uploaded to [codecov](https://codecov.io/gh/ambye85/firefly).

### Typing

Python interface stubs are provided for all modules.
We use [mypy](https://github.com/python/mypy) to perform static analysis of Firefly's typing.
Static analysis is run with the following command:

```shell script
poetry run mypy src tests
```

## Documentation

Firefly's public API is [documented](https://ambye85.github.io/firefly/index.html).

To build documentation, run:

```shell script
pdoc --html --config show_source_code=False --output-dir docs firefly
mv docs/firefly/* docs
rmdir docs/firefly
```
