"""Setup configuration for job-rejection-analysis package."""

from pathlib import Path
from setuptools import setup, find_packages

# Read the README for the long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Core dependencies
install_requires = [
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "nltk>=3.8.0",
    "scikit-learn>=1.3.0",
    "matplotlib>=3.7.0",
    "requests>=2.31.0",
    "beautifulsoup4>=4.12.0",
    "jsonschema>=4.17.0",
]

# Optional dependencies
extras_require = {
    # Web interface components
    "web": [
        "streamlit>=1.28.0",
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
    ],
    # Advanced NLP features
    "nlp": [
        "transformers>=4.35.0",
        "torch>=2.1.0",
        "textstat>=0.7.3",
    ],
    # Visualization tools
    "viz": [
        "wordcloud>=1.9.0",
        "seaborn>=0.12.0",
    ],
    # Testing dependencies
    "test": [
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
        "httpx>=0.25.0",  # For FastAPI testing
    ],
    # Development dependencies
    "dev": [
        "black>=23.0.0",
        "flake8>=6.0.0",
        "mypy>=1.5.0",
        "isort>=5.12.0",
    ],
}

# Add 'all' extras that includes everything
extras_require["all"] = list(set(sum(extras_require.values(), [])))

setup(
    name="job-rejection-analysis",
    version="0.1.0",
    author="Job Rejection Analysis Contributors",
    description="Exploratory data analysis of job rejection emails with NLP showcase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/job-rejection-analysis",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "job-rejection=cli.main:main",
            "job-rejection-dashboard=web.dashboard:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="nlp, data-analysis, sentiment-analysis, job-search, text-mining",
    include_package_data=True,
    package_data={
        "": ["schemas/**/*.json"],
    },
    zip_safe=False,
)
