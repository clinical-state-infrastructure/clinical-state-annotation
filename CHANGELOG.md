# Changelog

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Planned: aggregate statistics (without surface or source IDs) — v0.2.0

## [0.1.0] — 2026-05-13

### Added (Initial release — Level 0)

- Annotation **schema** (`annotation_schema/schema.json`) — Draft 2020-12
- **Synthetic** example (`annotation_schema/example_synthetic.json`, completely fictional)
- Minimal **validation** code (`scripts/validate_schema.py`)
- Minimal **summarizer** code (`scripts/summarize_annotations.py`)
- **Policy documents**:
  - `README.md` (bilingual EN + JA)
  - `RELEASE_POLICY.md`
  - `DATA_LICENSE.md`
  - `DATA_CARD.md`
  - `docs/copyright_and_privacy_note.md`
  - `docs/staged_release_policy.md`
  - `docs/annotation_workflow_overview.md`
- **Test suite** (`tests/`)
- LICENSE (MIT + CC-BY-4.0 dual)
- CITATION.cff

### Not included (deferred)

- Source-text data (deferred to Level 3, requires copyright clearance)
- Spans / begin-end offsets (Level 2)
- DOIs / PMIDs / PMCIDs / paper titles (Level 2+)
- Original case identifiers (Level 1+)
- Real annotation corpus or aggregate statistics from real corpus (Level 0, v0.2.0+)
- Methodology source code (deferred to paper publication)
