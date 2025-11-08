# Job Rejection Analysis

> Exploratory data analysis of job rejection emails with comprehensive NLP showcase

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Introduction

Nobody likes getting that rejection email after applying for a job, but it happens. The question remains: what do we do when it happens?

This project analyzes over 80 job rejection emails scraped from my inbox, diving into questions regarding:
- When rejection emails are sent (time and day patterns)
- The content and sentiment of rejection messages
- Common patterns and themes across rejections
- Readability and grammatical structure
- Named entities (companies, organizations)

The dataset continues to grow for stronger statistical insights.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Development](#development)
- [Open Data Standard](#open-data-standard)
- [Contributing](#contributing)
- [Roadmap](#roadmap)

## Project Structure

```
Job-Rejection-Analysis/
├── src/                          # Source code (package root)
│   ├── __init__.py
│   ├── nlp/                      # NLP analysis modules
│   │   ├── __init__.py
│   │   ├── nlp_utils.py          # Core NLP utilities
│   │   ├── nlp_showcase.py       # Demonstration script
│   │   ├── advanced_sentiment.py # Transformer-based sentiment
│   │   ├── topic_modeling.py     # LDA topic modeling
│   │   ├── topic_modeling_lsa.py # LSA topic modeling
│   │   ├── extract_named_entities.py
│   │   ├── summarize_emails.py
│   │   └── readability_metrics.py
│   ├── visualization/            # Data visualization
│   │   ├── __init__.py
│   │   ├── generate_wordcloud.py
│   │   ├── visualize_sentiment.py
│   │   ├── visualize_clusters.py
│   │   ├── visualize_timings.py
│   │   ├── visualize_trends.py
│   │   ├── visualize_lengths.py
│   │   ├── visualize_bigrams.py
│   │   └── visualize_pos_tags.py
│   ├── web/                      # Web interfaces
│   │   ├── __init__.py
│   │   ├── dashboard.py          # Streamlit dashboard
│   │   └── api/                  # FastAPI REST API
│   │       ├── __init__.py
│   │       └── main.py
│   ├── cli/                      # Command-line interface
│   │   ├── __init__.py
│   │   └── main.py
│   ├── data_processing/          # Data utilities
│   │   ├── __init__.py
│   │   ├── email_scraper/        # Email template scraper
│   │   ├── validation/           # Schema validation
│   │   ├── schema_versioning/    # Version management
│   │   └── tenant_management/    # Multi-tenant support
│   └── models/                   # ML models (placeholder)
├── tests/                        # Test suite (mirrors src/)
│   ├── nlp/
│   ├── visualization/
│   ├── web/
│   ├── cli/
│   └── data_processing/
├── data/                         # Data files
│   ├── raw/                      # Original data
│   │   └── rejections.csv
│   ├── processed/                # Processed datasets
│   └── samples/                  # Example files
│       └── rejection_schema_example.json
├── schemas/                      # JSON schemas
│   └── v1/
│       └── job_market_data.schema.json
├── notebooks/                    # Jupyter notebooks
├── .github/                      # GitHub templates
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── setup.py                      # Package configuration
├── Makefile                      # Development automation
├── CONTRIBUTING.md               # Contribution guidelines
├── ROADMAP.md                    # Future plans
└── README.md                     # This file
```

## Features

### 📊 NLP Analysis
- **Sentiment Analysis**: VADER and transformer-based sentiment classification
- **Topic Modeling**: LDA and LSA for discovering themes
- **Named Entity Recognition**: Extract companies and organizations
- **Text Summarization**: Condense emails using TF-IDF
- **Readability Metrics**: Flesch reading ease and grade level
- **Bigram Analysis**: Common two-word phrases

### 📈 Visualizations
- Sentiment distribution histograms
- t-SNE cluster visualizations
- Word clouds
- Timing analysis (by day/hour)
- Trend analysis over time
- Length distribution
- POS tag analysis
- Bigram frequency plots

### 🌐 Web Interfaces
- **Interactive Dashboard**: Streamlit-based exploration tool
- **REST API**: FastAPI service for programmatic access

### 🔧 Data Processing
- Email template scraper
- JSON schema validation
- Schema versioning support
- Multi-tenant data isolation

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Basic Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Job-Rejection-Analysis.git
cd Job-Rejection-Analysis

# Install core dependencies
pip install -e .
```

### Installation with Optional Features

```bash
# Install with web interface support
pip install -e ".[web]"

# Install with advanced NLP features
pip install -e ".[nlp]"

# Install with visualization tools
pip install -e ".[viz]"

# Install everything (recommended for full features)
pip install -e ".[all]"
```

### Using Makefile (Recommended for Development)

```bash
# Install development dependencies
make install-dev

# Or install everything
make install-all

# Initialize data directories
make init-data
```

See [MAKEFILE.md](MAKEFILE.md) for all available targets.

## Quick Start

### Using the CLI Tool

After installation, you can use the `job-rejection` command:

```bash
# Analyze sentiment
job-rejection sentiment --csv data/raw/rejections.csv

# Find top words
job-rejection top-words --csv data/raw/rejections.csv --top 20

# Cluster emails
job-rejection cluster --csv data/raw/rejections.csv --clusters 3
```

### Running the Web Dashboard

```bash
# Using the command
job-rejection-dashboard

# Or using make
make run-dashboard

# Or directly with streamlit
streamlit run src/web/dashboard.py
```

### Starting the API Server

```bash
# Using make
make run-api

# Or directly with uvicorn
uvicorn web.api.main:app --reload
```

The API will be available at http://localhost:8000 with automatic documentation at http://localhost:8000/docs

## Usage

### NLP Analysis Scripts

All scripts support `--help` for detailed options.

#### Sentiment Analysis

```bash
# Basic VADER sentiment
python -m nlp.nlp_showcase --csv data/raw/rejections.csv

# Advanced transformer-based sentiment
python -m nlp.advanced_sentiment --csv data/raw/rejections.csv --model distilbert-base-uncased-finetuned-sst-2-english
```

#### Topic Modeling

```bash
# LDA topic modeling
python -m nlp.topic_modeling --csv data/raw/rejections.csv --topics 5 --top-words 10

# LSA topic modeling
python -m nlp.topic_modeling_lsa --csv data/raw/rejections.csv --topics 5 --top-words 10
```

#### Text Analysis

```bash
# Extract named entities
python -m nlp.extract_named_entities --csv data/raw/rejections.csv --top 10

# Summarize emails
python -m nlp.summarize_emails --csv data/raw/rejections.csv --words 150

# Readability metrics
python -m nlp.readability_metrics --csv data/raw/rejections.csv
```

### Visualization Scripts

```bash
# Generate word cloud
python -m visualization.generate_wordcloud --csv data/raw/rejections.csv --output wordcloud.png

# Sentiment distribution
python -m visualization.visualize_sentiment --csv data/raw/rejections.csv --bins 20

# Cluster visualization (t-SNE)
python -m visualization.visualize_clusters --csv data/raw/rejections.csv --clusters 5

# Timing analysis
python -m visualization.visualize_timings --csv data/raw/rejections.csv

# Trends over time
python -m visualization.visualize_trends

# Length distribution
python -m visualization.visualize_lengths --csv data/raw/rejections.csv

# Bigram analysis
python -m visualization.visualize_bigrams --csv data/raw/rejections.csv --top 15

# POS tag distribution
python -m visualization.visualize_pos_tags --csv data/raw/rejections.csv
```

### Python API

```python
from nlp import load_data, sentiment_scores, common_words, cluster_texts

# Load data
df = load_data("data/raw/rejections.csv")

# Sentiment analysis
scores = sentiment_scores(df["full_text"])
print(f"Average sentiment: {sum(scores) / len(scores):.3f}")

# Common words
words = common_words(df["full_text"], n=10)
for word, count in words:
    print(f"{word}: {count}")

# Clustering
labels, clusters = cluster_texts(df["full_text"], n_clusters=3)
for idx, terms in clusters.items():
    print(f"Cluster {idx}: {', '.join(terms)}")
```

## Development

### Setting Up Development Environment

```bash
# Clone and install
git clone https://github.com/yourusername/Job-Rejection-Analysis.git
cd Job-Rejection-Analysis

# Set up development environment
make dev-setup

# Initialize data directories
make init-data
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-coverage

# Run fast tests only
make test-fast
```

### Code Quality

```bash
# Format code
make format

# Run linting
make lint

# Type checking
make type-check

# Run all checks
make check-all
```

### Development Workflow

```bash
# 1. Make your changes
# 2. Format code
make format

# 3. Run checks
make check

# 4. Commit
git add .
git commit -m "Your message"
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## Open Data Standard

### JSON Schema

This project defines a **v1 JSON schema** for job market data:

- **Schema**: `schemas/v1/job_market_data.schema.json`
- **Example**: `data/samples/rejection_schema_example.json`

### Validation

```python
from data_processing.validation import validate_record, validate_file

# Validate a record
validate_record(record_dict)

# Validate a file
count = validate_file("data/samples/rejection_schema_example.json")
print(f"Validated {count} records")
```

### Schema Versioning

```python
from data_processing.schema_versioning import load_schema

schema = load_schema(version="v1")
```

### Multi-Tenant Support

```python
from data_processing.tenant_management import TenantManager, Tenant

manager = TenantManager()
tenant = Tenant(tenant_id="demo", name="Demo Corp")
manager.add_tenant(tenant)

# List all tenants
for t in manager.list_tenants():
    print(t.name)
```

## Testing

The project includes a comprehensive test suite:

```bash
# Run all tests
pytest tests/

# Run specific test modules
pytest tests/nlp/
pytest tests/web/

# With coverage
pytest tests/ --cov=src --cov-report=html
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned enhancements and future directions.

Key upcoming features:
- Machine learning models for rejection prediction
- Email parsing improvements
- Enhanced multi-tenant features
- API authentication
- More visualization types
- Export functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NLTK for NLP utilities
- scikit-learn for machine learning algorithms
- Transformers for advanced sentiment analysis
- Streamlit for the interactive dashboard
- FastAPI for the REST API

## Citation

If you use this project in your research, please cite:

```bibtex
@misc{job-rejection-analysis,
  author = {Job Rejection Analysis Contributors},
  title = {Job Rejection Analysis: Exploratory NLP Analysis of Job Rejection Emails},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/yourusername/Job-Rejection-Analysis}
}
```

## Contact

For questions, issues, or suggestions, please [open an issue](https://github.com/yourusername/Job-Rejection-Analysis/issues).

---

**Note**: This project analyzes rejection emails for educational and research purposes. All data should be anonymized and handled according to privacy best practices.
