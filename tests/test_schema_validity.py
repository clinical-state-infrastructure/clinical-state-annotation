"""Verify the JSON Schema file is itself valid Draft 2020-12."""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "annotation_schema" / "schema.json"


def test_schema_is_valid_draft_2020_12():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)


def test_schema_has_required_metadata():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    assert "$id" in schema
    assert "title" in schema
    assert "$schema" in schema
    assert schema.get("additionalProperties") is False, "additionalProperties must be false to catch typos"


def test_schema_required_fields():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    required = set(schema.get("required", []))
    expected = {"ord", "hpo_id", "category", "presence", "tier", "review_status"}
    assert expected.issubset(required), f"missing required fields: {expected - required}"


def test_schema_excludes_dangerous_fields():
    """Schema must NOT allow surface/text/span/doi properties."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    properties = schema.get("properties", {})
    forbidden = {"surface_form", "surface", "text", "begin", "end", "doi", "pmid", "pmcid", "url", "paper_title"}
    overlap = forbidden & set(properties.keys())
    assert not overlap, f"Schema must not define forbidden fields: {overlap}"
