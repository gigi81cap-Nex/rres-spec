#!/usr/bin/env python3
"""
RRES Validator v2
Deterministic PASS/FAIL validator for RRES v0.1 records.

Usage:
  python validator_v2.py record.json
  python validator_v2.py record.json --explain
"""

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("Missing dependency: jsonschema")
    print("Install with: pip install jsonschema")
    sys.exit(2)


SCHEMA_FILE = "rres-v0.1.schema.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    if len(sys.argv) < 2:
        print("Usage: python validator_v2.py <record.json> [--explain]")
        sys.exit(1)

    record_path = sys.argv[1]
    explain = "--explain" in sys.argv

    if not Path(SCHEMA_FILE).exists():
        print(f"Schema not found: {SCHEMA_FILE}")
        sys.exit(2)

    try:
        schema = load_json(SCHEMA_FILE)
    except Exception as e:
        print(f"Failed to load schema: {e}")
        sys.exit(2)

    try:
        record = load_json(record_path)
    except Exception as e:
        print(f"Failed to load record: {e}")
        sys.exit(2)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(record), key=lambda e: e.path)

    if not errors:
        print("PASS")
        sys.exit(0)

    print("FAIL")

    if explain:
        print("\nValidation errors:")
        for err in errors:
            location = ".".join(str(p) for p in err.path) or "<root>"
            print(f"- {location}: {err.message}")

    sys.exit(3)


if __name__ == "__main__":
    main()
