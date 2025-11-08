"""Validate job market data against the JSON schema."""
from __future__ import annotations
from pathlib import Path
import json
from typing import Any
from jsonschema import Draft7Validator
from ..schema_versioning import load_schema


def validate_record(record: dict[str, Any], version: str = "v1") -> None:
    """Validate a single record against the schema."""
    schema = load_schema(version)
    Draft7Validator(schema).validate(record)


def validate_file(path: Path | str, version: str = "v1") -> int:
    """Validate JSON data in ``path``.

    Returns the number of records validated.
    """
    schema = load_schema(version)
    validator = Draft7Validator(schema)
    data = json.loads(Path(path).read_text())
    if isinstance(data, list):
        for item in data:
            validator.validate(item)
        return len(data)
    elif isinstance(data, dict):
        validator.validate(data)
        return 1
    raise TypeError("JSON content must be an object or list of objects")
