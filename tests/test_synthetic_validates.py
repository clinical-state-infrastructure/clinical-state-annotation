"""Verify example_synthetic.json validates against the schema and is marked synthetic."""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "annotation_schema" / "schema.json"
SYNTH_PATH = REPO / "annotation_schema" / "example_synthetic.json"


def test_synthetic_validates():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    data = json.loads(SYNTH_PATH.read_text(encoding="utf-8"))
    assert data.get("is_synthetic") is True, "Document-level is_synthetic must be true"
    for i, ann in enumerate(data["annotations"]):
        jsonschema.validate(instance=ann, schema=schema)


def test_synthetic_all_anns_marked_synthetic():
    data = json.loads(SYNTH_PATH.read_text(encoding="utf-8"))
    for i, ann in enumerate(data["annotations"]):
        assert ann.get("is_synthetic") is True, f"annotation[{i}] missing is_synthetic"


def test_synthetic_no_real_identifiers():
    """Synthetic example must not contain any real-looking DOI / PMID etc."""
    text = SYNTH_PATH.read_text(encoding="utf-8").lower()
    forbidden = ["10.", "pmid", "pmcid", "doi:", "pubmed.ncbi"]
    for bad in forbidden:
        assert bad not in text, f"synthetic example contains real-ID-like substring '{bad}'"
