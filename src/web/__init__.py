"""Web interface module for job rejection analysis.

This module includes:
- dashboard: Interactive Streamlit dashboard
- api: FastAPI REST API for accessing rejection data
"""

from . import api
from .dashboard import main as run_dashboard

__all__ = [
    "api",
    "run_dashboard",
]
