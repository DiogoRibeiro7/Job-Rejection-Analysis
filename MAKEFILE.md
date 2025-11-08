# Makefile Usage Guide

This project includes a comprehensive Makefile to streamline development tasks. Below is a guide to all available targets.

## Quick Start

```bash
# Show all available targets
make help

# Set up development environment
make dev-setup

# Run tests
make test

# Format and lint code
make format
make lint
```

## Installation Targets

| Target | Description |
|--------|-------------|
| `make install` | Install core dependencies only |
| `make install-dev` | Install development dependencies (recommended) |
| `make install-all` | Install all dependencies including optional ones |
| `make install-web` | Install with web interface dependencies |
| `make install-nlp` | Install with advanced NLP dependencies |

**Example:**
```bash
# For development
make install-dev

# For production with all features
make install-all
```

## Testing Targets

| Target | Description |
|--------|-------------|
| `make test` | Run all tests with standard output |
| `make test-verbose` | Run tests with verbose output |
| `make test-coverage` | Run tests with coverage report (generates htmlcov/) |
| `make test-fast` | Run only fast tests (skip slow tests) |

**Example:**
```bash
# Standard test run
make test

# With coverage report
make test-coverage
# Then open htmlcov/index.html in browser
```

## Code Quality Targets

| Target | Description |
|--------|-------------|
| `make lint` | Run flake8 linting (lenient) |
| `make lint-strict` | Run strict linting (fails on warnings) |
| `make type-check` | Run mypy type checking |
| `make format` | Format code with black and isort |
| `make format-check` | Check if code is properly formatted (for CI) |
| `make check` | Run linting and tests |
| `make check-all` | Run all checks (lint, type-check, tests with coverage) |

**Example:**
```bash
# Before committing
make format
make check

# Full quality check
make check-all
```

## Cleanup Targets

| Target | Description |
|--------|-------------|
| `make clean` | Remove generated files (__pycache__, *.pyc, coverage, etc.) |
| `make clean-all` | Deep clean including build artifacts |

**Example:**
```bash
# Standard cleanup
make clean

# Deep cleanup before building
make clean-all
```

## Build & Distribution Targets

| Target | Description |
|--------|-------------|
| `make build` | Build both wheel and source distributions |
| `make build-wheel` | Build wheel distribution only |
| `make build-sdist` | Build source distribution only |
| `make upload-test` | Upload to TestPyPI |
| `make upload` | Upload to PyPI (production) |

**Example:**
```bash
# Build package
make build

# Test on TestPyPI first
make upload-test

# Then upload to production PyPI
make upload
```

## Run Targets

| Target | Description |
|--------|-------------|
| `make run-cli` | Run the CLI tool (shows help) |
| `make run-dashboard` | Start the Streamlit dashboard |
| `make run-api` | Start the FastAPI server |
| `make jupyter` | Start Jupyter notebook server |

**Example:**
```bash
# Start the web dashboard
make run-dashboard

# Start the API server
make run-api
```

## Utility Targets

| Target | Description |
|--------|-------------|
| `make dev-setup` | Complete development environment setup |
| `make verify` | Verify package installation |
| `make info` | Show project information |
| `make init-data` | Initialize data directories |
| `make requirements` | Generate requirements.txt from setup.py |

**Example:**
```bash
# First time setup
make dev-setup
make init-data

# Verify everything works
make verify
```

## Common Workflows

### Daily Development
```bash
# 1. Pull latest changes
git pull

# 2. Install/update dependencies
make install-dev

# 3. Make your changes...

# 4. Format code
make format

# 5. Run checks
make check

# 6. Commit
git add .
git commit -m "Your message"
```

### Before Creating a Pull Request
```bash
# 1. Format code
make format

# 2. Run all checks
make check-all

# 3. Clean up
make clean

# 4. Verify build works
make build
```

### CI/CD Pipeline
```bash
# In CI environment
make install-dev
make format-check
make lint-strict
make test-coverage
```

### Release Process
```bash
# 1. Update version in setup.py

# 2. Run full checks
make clean-all
make check-all

# 3. Build distributions
make build

# 4. Test on TestPyPI
make upload-test

# 5. If all good, upload to PyPI
make upload
```

## Tips

1. **Always run `make format` before committing** to maintain consistent code style
2. **Use `make check` frequently** during development to catch issues early
3. **Run `make clean` if tests behave strangely** to remove cached files
4. **Use `make test-fast` during development** for quicker feedback
5. **Run `make check-all` before pushing** to ensure everything passes

## Troubleshooting

**Issue: `make` command not found**
- On Windows: Install GNU Make (via chocolatey: `choco install make` or use Git Bash)
- On Linux/Mac: Should be pre-installed, otherwise use package manager

**Issue: Tests failing after changes**
```bash
make clean
make install-dev
make test
```

**Issue: Import errors**
```bash
make clean
make install-dev
make verify
```

**Issue: Formatting conflicts**
```bash
make format
git add .
```

## Environment Variables

You can customize behavior with environment variables:

```bash
# Use different Python
PYTHON=python3.11 make install

# Use different pip
PIP=pip3 make install-dev
```

## Help

For a quick reference of all targets:
```bash
make help
```

For project information:
```bash
make info
```
