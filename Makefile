default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: test
test: # Run tests and generate coverage report
	poetry run tox

.PHONY: docs
docs: # Build the documentation locally
	poetry run sphinx-build -M html docs public 

.PHONY: lint
lint: # Run linter
	poetry run ruff check

.PHONY: dev
dev: # Install project dependencies and create a dev shell
	poetry install
	poetry shell

