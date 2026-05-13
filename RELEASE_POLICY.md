# Release Policy

## Principles

This repository follows a **staged release policy** for clinical state
annotation data and tooling. Staged release is intended to balance:

1. **Reproducibility / openness** of the schema and methodology
2. **Copyright compliance** with academic societies / publishers that own
   the source case reports
3. **Re-identification risk** mitigation for patient privacy
4. **Pre-publication intellectual property** of novel methodology

## Versioning

We use semantic versioning. Each version corresponds to a Level (data exposure)
and a Quality state.

| Version | Data exposure (Level) | Quality state | Typical timing |
|---|---|---|---|
| **v0.1.0** | Level 0 — schema + synthetic + tools only | Machine-only (no human review) | **Initial release (now)** |
| v0.2.0 | Level 0 — adds aggregate stats (no source-data) | Partial human review (single reviewer) | Pending review tooling |
| v0.3.0 | Level 0 — adds full aggregate stats, schema v1 | Full single-reviewer review | Pending full review |
| v1.0.0 | Level 0 — final schema, full IAA | Multi-reviewer + IAA validated | Pending multi-reviewer process |
| Level 1.x | Adds per-ann ontology metadata, hashed doc IDs | (Controlled access) | After conference presentation / paper submission |
| Level 2.x | Adds span positions (controlled, on request) | (Controlled access) | After publisher/society approval |
| Level 3.x | Adds surface forms + DOI links (open corpus) | (Open) | After full copyright clearance |

## What is in each Level

### Level 0 (this release)

✅ Included:
- Annotation schema (JSON Schema)
- Synthetic examples (3 completely fictional cases)
- Validation code
- Summary tool (minimal aggregation of synthetic data)
- Policy and documentation
- Aggregate statistics that DO NOT contain surface or source IDs (added in v0.2.0+)

❌ Not included:
- Source-text data
- Surface forms / sentence text
- Spans (begin/end offsets)
- DOIs / PMIDs / PMCIDs
- Paper titles / URLs
- Original case IDs
- Salts, credentials, `.env`
- Patient-identifying information
- High-density continuous spans (would enable text reconstruction)

### Level 1 (planned)

Adds:
- Per-annotation ontology metadata (HPO_ID, category, presence, etc.)
- Sentence-index references (not actual text)
- Document hash (`doc_hash`) for de-anonymized cross-version linkage
  (salt remains private)

Distribution: **Controlled access** via formal request + IRB confirmation.

### Level 2 (planned)

Adds:
- Span position references (begin/end character offsets within a privately-held
  text corpus)

Distribution: **Controlled access** for verified collaborators with executed
data-use agreement.

### Level 3 (planned)

Adds:
- Surface forms
- DOI links to original sources

Distribution: **Open** corpus release, on Zenodo or equivalent, after full
copyright clearance.

## How quality state and data exposure interact

Quality state (machine-only / single-reviewer / multi-reviewer + IAA) is
**orthogonal** to data exposure level. For instance, a Level 1 release with
v0.2.0 quality means: ontology metadata accessible under controlled access,
based on partially-human-reviewed annotations.

## When the next release will appear

We do not commit to specific dates. Releases happen when:

- Schema becomes stable and validated against synthetic and (privately) real data
- Review tooling (annotation-editor) reaches usable maturity
- Reviewer time becomes available
- Publisher/society negotiations complete (for Level 2+)
- Paper publication is in process (for methodology source code release)

## Access requests

For Level 1+ access, please contact us via [`CONTACT.md`](./CONTACT.md) with:

1. Affiliation and project description
2. Intended use
3. IRB approval (where applicable)
4. Confirmation of data-use restrictions

We will respond as soon as feasible.

## License

- Code: MIT
- Schema / docs / synthetic data: CC-BY 4.0

See [`LICENSE`](./LICENSE) and [`DATA_LICENSE.md`](./DATA_LICENSE.md).
