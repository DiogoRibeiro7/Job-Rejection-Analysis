import json
from pathlib import Path
import pytest
from validation import validate_record, validate_file

SAMPLE_PATH = Path("data/rejection_schema_example.json")
SAMPLE = json.loads(SAMPLE_PATH.read_text())


def test_validate_record_accepts_sample():
    validate_record(SAMPLE)


def test_validate_file_accepts_sample():
    assert validate_file(SAMPLE_PATH) == 1


def test_validate_record_rejects_missing_fields():
    bad = {"application": {"id": "123"}}
    with pytest.raises(Exception):
        validate_record(bad)
