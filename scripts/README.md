# scripts/

Minimal scripts shipped with this Level 0 release.

- `validate_schema.py` — JSON Schema validation
- `summarize_annotations.py` — Trivial aggregate counts (HPO, category, tier, presence, review_status)
- `requirements.txt` — `jsonschema`, `pytest`

These scripts intentionally do **not** include:

- The annotation pipeline (RLM iteration, chunking, extend chain, complement strategy)
- Statistical summarization of real corpora
- Format converters (Phenopackets / PubAnnotation / Brat)
- Document-hash utilities (not needed in Level 0)

These will appear in later releases or in the methodology paper's
accompanying repository.
