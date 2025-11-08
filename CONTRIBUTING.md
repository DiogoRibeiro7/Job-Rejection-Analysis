# Contributing to Job Rejection Analysis

Thank you for your interest in contributing!

## Development Setup

1. Fork the repository
2. Clone your fork:
```bash
   git clone https://github.com/YOUR_USERNAME/job-rejection-analysis.git
   cd job-rejection-analysis
```

3. Install dependencies:
```bash
   poetry install
```

4. Create a branch for your feature:
```bash
   git checkout -b feature/your-feature-name
```

## Running Tests
```bash
poetry run pytest
```

## Code Style

We use:
- Black for code formatting
- isort for import sorting
- flake8 for linting

Run all formatters:
```bash
poetry run black src/ tests/
poetry run isort src/ tests/
```

## Submitting Changes

1. Ensure all tests pass
2. Update documentation as needed
3. Submit a pull request

## Reporting Issues

Use the GitHub issue tracker to report bugs or suggest features.
