"""Minimal JSON Schema validator.

Usage:
    python scripts/validate_schema.py <json_file> [<json_file2> ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Install: pip install -r scripts/requirements.txt", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "annotation_schema" / "schema.json"


def validate(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    # If wrapper with annotations[], validate each
    if isinstance(data, dict) and "annotations" in data:
        for i, ann in enumerate(data["annotations"]):
            try:
                jsonschema.validate(instance=ann, schema=schema)
            except jsonschema.ValidationError as e:
                print(f"  ✗ {path.name} annotations[{i}]: {e.message}", file=sys.stderr)
                return False
        print(f"  ✓ {path.name}: {len(data['annotations'])} annotations validated")
        return True
    # Single annotation
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"  ✓ {path.name}: 1 annotation validated")
        return True
    except jsonschema.ValidationError as e:
        print(f"  ✗ {path.name}: {e.message}", file=sys.stderr)
        return False


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    ok = all(validate(Path(p)) for p in sys.argv[1:])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
