"""Minimal FastAPI app serving sanitized rejection data."""
from pathlib import Path
import json
from fastapi import FastAPI

app = FastAPI(title="Job Market Data API")

DATA_FILE = Path(__file__).resolve().parent.parent.parent.parent / "data" / "samples" / "rejection_schema_example.json"

@app.get("/rejections")
def get_rejections() -> dict:
    """Return sample rejection records while preserving privacy."""
    if DATA_FILE.exists():
        with DATA_FILE.open() as fh:
            data = json.load(fh)
        # In a real system, PII would be removed or anonymised here
        return {"data": [data]}
    return {"data": []}
