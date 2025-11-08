.PHONY: help install install-dev install-all test test-verbose lint format clean clean-all check build docs

# Default target
.DEFAULT_GOAL := help

# Project variables
PYTHON := python
PIP := pip
PROJECT_NAME := job-rejection-analysis
SRC_DIR := src
TEST_DIR := tests
DATA_DIR := data

# Color output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Available targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}'

install: ## Install core dependencies only
	@echo "$(BLUE)Installing core dependencies...$(NC)"
	$(PIP) install -e .
	@echo "$(GREEN)Core dependencies installed successfully!$(NC)"

install-dev: ## Install development dependencies
	@echo "$(BLUE)Installing development dependencies...$(NC)"
	$(PIP) install -e ".[dev,test]"
	@echo "$(GREEN)Development dependencies installed successfully!$(NC)"

install-all: ## Install all dependencies (including optional)
	@echo "$(BLUE)Installing all dependencies...$(NC)"
	$(PIP) install -e ".[all]"
	@echo "$(GREEN)All dependencies installed successfully!$(NC)"

install-web: ## Install with web dependencies
	@echo "$(BLUE)Installing with web dependencies...$(NC)"
	$(PIP) install -e ".[web]"
	@echo "$(GREEN)Web dependencies installed successfully!$(NC)"

install-nlp: ## Install with NLP dependencies
	@echo "$(BLUE)Installing with NLP dependencies...$(NC)"
	$(PIP) install -e ".[nlp]"
	@echo "$(GREEN)NLP dependencies installed successfully!$(NC)"

test: ## Run all tests
	@echo "$(BLUE)Running tests...$(NC)"
	$(PYTHON) -m pytest $(TEST_DIR) -v --tb=short

test-verbose: ## Run tests with verbose output
	@echo "$(BLUE)Running tests (verbose)...$(NC)"
	$(PYTHON) -m pytest $(TEST_DIR) -vv

test-coverage: ## Run tests with coverage report
	@echo "$(BLUE)Running tests with coverage...$(NC)"
	$(PYTHON) -m pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=html --cov-report=term-missing
	@echo "$(GREEN)Coverage report generated in htmlcov/index.html$(NC)"

test-fast: ## Run tests without slow tests
	@echo "$(BLUE)Running fast tests...$(NC)"
	$(PYTHON) -m pytest $(TEST_DIR) -v -m "not slow"

lint: ## Run linting tools (flake8)
	@echo "$(BLUE)Running linting checks...$(NC)"
	@echo "$(YELLOW)Checking code style with flake8...$(NC)"
	-$(PYTHON) -m flake8 $(SRC_DIR) $(TEST_DIR) --count --select=E9,F63,F7,F82 --show-source --statistics
	-$(PYTHON) -m flake8 $(SRC_DIR) $(TEST_DIR) --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics
	@echo "$(GREEN)Linting complete!$(NC)"

lint-strict: ## Run strict linting (will fail on warnings)
	@echo "$(BLUE)Running strict linting checks...$(NC)"
	$(PYTHON) -m flake8 $(SRC_DIR) $(TEST_DIR) --max-line-length=100

type-check: ## Run type checking with mypy
	@echo "$(BLUE)Running type checks...$(NC)"
	-$(PYTHON) -m mypy $(SRC_DIR) --ignore-missing-imports
	@echo "$(GREEN)Type checking complete!$(NC)"

format: ## Format code with black and isort
	@echo "$(BLUE)Formatting code...$(NC)"
	@echo "$(YELLOW)Running black...$(NC)"
	$(PYTHON) -m black $(SRC_DIR) $(TEST_DIR)
	@echo "$(YELLOW)Running isort...$(NC)"
	$(PYTHON) -m isort $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)Code formatted successfully!$(NC)"

format-check: ## Check if code is formatted (for CI)
	@echo "$(BLUE)Checking code formatting...$(NC)"
	$(PYTHON) -m black --check $(SRC_DIR) $(TEST_DIR)
	$(PYTHON) -m isort --check-only $(SRC_DIR) $(TEST_DIR)

check: lint test ## Run linting and tests

check-all: lint type-check test-coverage ## Run all checks (lint, type-check, tests with coverage)

clean: ## Clean up generated files
	@echo "$(BLUE)Cleaning up generated files...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -f *.png *.html 2>/dev/null || true
	@echo "$(GREEN)Cleanup complete!$(NC)"

clean-all: clean ## Clean everything including build artifacts
	@echo "$(BLUE)Deep cleaning...$(NC)"
	rm -rf build/ dist/ .eggs/
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)Deep cleanup complete!$(NC)"

build: clean ## Build distribution packages
	@echo "$(BLUE)Building distribution packages...$(NC)"
	$(PYTHON) -m build
	@echo "$(GREEN)Build complete! Check dist/ directory$(NC)"

build-wheel: clean ## Build wheel distribution
	@echo "$(BLUE)Building wheel package...$(NC)"
	$(PYTHON) setup.py bdist_wheel
	@echo "$(GREEN)Wheel built successfully!$(NC)"

build-sdist: clean ## Build source distribution
	@echo "$(BLUE)Building source distribution...$(NC)"
	$(PYTHON) setup.py sdist
	@echo "$(GREEN)Source distribution built successfully!$(NC)"

upload-test: build ## Upload to TestPyPI
	@echo "$(BLUE)Uploading to TestPyPI...$(NC)"
	$(PYTHON) -m twine upload --repository testpypi dist/*

upload: build ## Upload to PyPI
	@echo "$(RED)Uploading to PyPI...$(NC)"
	$(PYTHON) -m twine upload dist/*

dev-setup: install-dev ## Set up development environment
	@echo "$(BLUE)Setting up development environment...$(NC)"
	@echo "$(GREEN)Development environment ready!$(NC)"
	@echo "$(YELLOW)Recommended: Run 'make check' to verify setup$(NC)"

run-cli: ## Run the CLI tool (example)
	@echo "$(BLUE)Running CLI tool...$(NC)"
	$(PYTHON) -m cli.main --help

run-dashboard: ## Run the Streamlit dashboard
	@echo "$(BLUE)Starting dashboard...$(NC)"
	streamlit run $(SRC_DIR)/web/dashboard.py

run-api: ## Run the FastAPI server
	@echo "$(BLUE)Starting API server...$(NC)"
	uvicorn web.api.main:app --reload

jupyter: ## Start Jupyter notebook server
	@echo "$(BLUE)Starting Jupyter notebook...$(NC)"
	jupyter notebook

requirements: ## Generate requirements.txt from setup.py
	@echo "$(BLUE)Generating requirements.txt...$(NC)"
	$(PIP) install pip-tools
	pip-compile --output-file=requirements.txt setup.py
	@echo "$(GREEN)requirements.txt generated!$(NC)"

init-data: ## Initialize data directories
	@echo "$(BLUE)Initializing data directories...$(NC)"
	mkdir -p $(DATA_DIR)/raw $(DATA_DIR)/processed $(DATA_DIR)/samples
	@echo "$(GREEN)Data directories created!$(NC)"

verify: ## Verify package installation
	@echo "$(BLUE)Verifying package installation...$(NC)"
	$(PYTHON) -c "import sys; sys.path.insert(0, '$(SRC_DIR)'); import nlp; print('✓ NLP module loaded')"
	$(PYTHON) -c "import sys; sys.path.insert(0, '$(SRC_DIR)'); import visualization; print('✓ Visualization module loaded')"
	$(PYTHON) -c "import sys; sys.path.insert(0, '$(SRC_DIR)'); import cli; print('✓ CLI module loaded')"
	@echo "$(GREEN)Package verification complete!$(NC)"

info: ## Show project information
	@echo "$(BLUE)Project Information:$(NC)"
	@echo "  Name: $(PROJECT_NAME)"
	@echo "  Python: $$($(PYTHON) --version)"
	@echo "  Pip: $$($(PIP) --version)"
	@echo "  Source: $(SRC_DIR)/"
	@echo "  Tests: $(TEST_DIR)/"
	@echo "  Data: $(DATA_DIR)/"
