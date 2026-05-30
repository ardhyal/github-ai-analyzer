# GitHub Analyzer

A small CLI application that fetches GitHub user profile details with a clean architecture design.

## Features

- Dependency injection for the GitHub API client
- Clear separation between domain, use cases, infrastructure, and presentation
- Error handling for invalid input, missing users, network errors, and timeouts
- Structured logging for operational visibility

## Usage

Run the tool from the repository root:

```bash
env PYTHONPATH=. python main.py
```

Or install locally and run via the script entrypoint:

```bash
python -m pip install -e .
github-analyzer
```

## Architecture

- `github_analyzer/clients.py` contains the GitHub API adapter and timeout handling
- `github_analyzer/usecases.py` contains the application business logic
- `github_analyzer/adapters.py` contains the presentation adapter for console output
- `github_analyzer/cli.py` composes dependencies and handles runtime errors
- `github_analyzer/exceptions.py` defines explicit domain errors
- `main.py` is a small entrypoint that delegates to the CLI layer
