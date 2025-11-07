"""Utilities for loading versioned job market data schemas."""
from __future__ import annotations
from pathlib import Path
import json
from typing import List

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"
LATEST_VERSION = "v1"


def available_versions() -> List[str]:
    """Return available schema versions."""
    return sorted(p.name for p in SCHEMA_DIR.iterdir() if p.is_dir())


def get_schema_path(version: str = LATEST_VERSION) -> Path:
    """Return path to the schema file for ``version``."""
    path = SCHEMA_DIR / version / "job_market_data.schema.json"
    if not path.exists():
        raise FileNotFoundError(f"Schema for version {version} not found")
    return path


def load_schema(version: str = LATEST_VERSION) -> dict:
    """Load and return the JSON schema for ``version``."""
    return json.loads(get_schema_path(version).read_text())
