from pathlib import Path
import json
from jsonschema import validate
from schema_versioning import load_schema

SCHEMA = load_schema()
SAMPLE = json.loads(Path("data/rejection_schema_example.json").read_text())

def test_sample_conforms_to_schema():
    validate(instance=SAMPLE, schema=SCHEMA)
