# Annotation Schema

JSON Schema (Draft 2020-12) for clinical state annotations.

## Files

| File | Purpose |
|---|---|
| `schema.json` | Per-annotation record schema (Level 0: no surface, no span) |
| `example_synthetic.json` | A small, completely fictional example demonstrating the schema |

## Validation

```bash
pip install -r ../scripts/requirements.txt
python ../scripts/validate_schema.py example_synthetic.json
```

## Versioning

Schema versioning is tied to repository semantic versioning. Breaking
schema changes will appear in a major version bump and be documented in
`CHANGELOG.md`.

## Fields not in this schema (intentional)

The following are deliberately **not** part of the Level 0 schema:

- `surface_form` / `text`
- `begin` / `end` span offsets
- `case_id` (any value that would identify the underlying source)
- `doi`, `pmid`, `pmcid`, `paper_title`

These may appear at Level 1 (with `doc_hash`) or Level 2+ (with controlled
access), per `RELEASE_POLICY.md`.

## Notes on `is_synthetic`

Any example committed to this public repository **must** carry
`is_synthetic: true` at both the document level and the annotation level.
This is enforced by `tests/test_synthetic_validates.py`.
