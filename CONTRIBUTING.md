# Contributing

## Development Workflow

Pewter is a cli, which is handled by Click and Poetry. In order to get the `pewter` cli on your
path, start with:

* `poetry install`

Then, depending on your setup, you can invoke `pewter` directly using either:

* `poetry run pewter`

or (if you've got direnv and poetry set up together) simply

* `pewter`

## Pushing and Merging a branch

When a branch is pushed or merged, CI will compile the project, check formatting, and run tests
and static analysis.

## Follow Patterns

When adding something, first look for other implementations in the repository, and mirror those.
