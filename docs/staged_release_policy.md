# Staged Release Policy (Detail)

This document complements [`RELEASE_POLICY.md`](../RELEASE_POLICY.md) and
provides operational detail of how each Level is structured.

## Levels at a glance

| Level | Data exposure | Access model | Typical release name |
|---|---|---|---|
| 0 | schema + synthetic + tools + (later) aggregate stats | Open / public GitHub | v0.x.x |
| 1 | + per-ann ontology metadata (HPO, category, presence, etc.) with `doc_hash` linkage | Controlled access (request) | Level-1 release |
| 2 | + span positions (begin/end offsets relative to a privately-held text) | Controlled access (DUA required) | Level-2 release |
| 3 | + surface forms + DOI links | Open release (Zenodo / NBDC) | Level-3 release |

## Level 0 (this release)

### What you can do at Level 0

- Read the annotation schema
- Implement schema-compatible annotators in your own pipeline
- Validate your annotator outputs using `scripts/validate_schema.py`
- Use synthetic examples to test integration

### What you cannot do at Level 0

- Re-create the corpus (no real-source data is present)
- Compute precision/recall against a held-out test set (no test set is present)
- Re-link to original publications (no DOI / PMID / title)

### Statistical content (planned)

Future Level 0 versions (v0.2.0+) may include aggregate statistics:

- HPO ID frequency distributions
- Category distributions
- Coverage statistics (clinical_coverage estimates)

These statistics will be derived from machine annotation of a private corpus,
**but the corpus itself will not be released**, and statistics will:

- Use `doc_hash` (salt private) instead of any real identifier
- Apply aggregation thresholds where re-identification risk exists
- Avoid releasing any per-document content that could reveal source identity

## Level 1 (planned)

### What we expect to add

- Per-annotation ontology metadata in a structured format:
  - HPO_ID, hpo_label
  - category, subcategory
  - presence (+ / - / ? / u)
  - tier (AUTO-OK / REVIEW / FLAG)
  - confidence
  - iteration (RLM iter origin)
  - review_status, reviewer_role
  - `doc_hash` (16-char SHA-256 prefix with a private salt)

### What we will not add at Level 1

- Surface form
- Span position
- Sentence text
- DOI / PMID / paper title

### Access model

Controlled access via request + simple agreement to:

- Not attempt re-identification
- Use only for stated research purpose
- Not redistribute

## Level 2 (planned)

### What we expect to add

- Span position references (begin / end character offsets in a privately-held
  text corpus)
- Sentence-level positional references

### Access model

Formal data-use agreement (DUA) required. Verified institutional affiliation
required. IRB approval where applicable.

## Level 3 (planned)

### What we expect to add

- Surface forms
- DOI / PMID links to original publications

### Access model

Open release on Zenodo or NBDC after full publisher / academic society
approval is documented.

## Cross-cutting considerations

### Document hashing (`doc_hash`)

A document hash is `SHA-256(doc_id || salt)[:16]`, where `salt` is a private
32+ character secret kept in `.env` (not committed). The same `doc_id` produces
the same `doc_hash` across releases, enabling longitudinal linkage of
annotations across versions **without** revealing the original `doc_id`.

If the salt is compromised, an attacker who possesses a candidate list of
`doc_id` values can compute matching `doc_hash` values. We therefore guard the
salt as an operational secret.

### Aggregate statistics privacy

When publishing aggregate statistics (HPO frequencies, category distributions),
we apply thresholds:

- Cells with `n < 5` cases may be merged into "other" or "rare combination"
- Outlier cases that uniquely identify a publication-style narrative may be
  excluded from per-case granularity

### Forward compatibility

Schema changes between major versions (e.g., v0.x → v1.0) may require migration.
We will document migration paths in `CHANGELOG.md`.
