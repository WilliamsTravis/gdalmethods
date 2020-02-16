# pygds
A module containing a series of helpful python utilities for GDS work.
[Docs](https://github.nrel.gov/pages/GDS/pygds/index.html)

# Install/Update

Install: `pip install git+https://github.nrel.gov/GDS/pygds.git` 

Update: `pip install --upgrade git+https://github.nrel.gov/GDS/pygds.git`

# Contributing

## Pre-commit
This repository uses [pre-commit](https://pre-commit.com/) hooks to manage code style and quality standards.

## Installation
First install the pre-commit package

    pip install pre-commit

The following files need to be present in the repo to install the actual pre-commit hooks:

1. .pre-commit-config.yaml
2. .pylintrc
3. .flake8

Next install the pre-commit hooks defined in .pre-commit-config.yaml

    pre-commit install

## Test hooks
To test your files before committing, stage them

    git add file or git add .
    pre-commit run --all-files

## Generating Docs

Once code is pushed to master, run `generate_docs.sh` to generate and upload updated docs.

Updated docs should be available [here](https://github.nrel.gov/pages/GDS/pygds)

