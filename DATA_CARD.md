# Data Card

Following the structure of *Datasheets for Datasets* [Gebru et al., 2021],
adapted for an **infrastructure-only Level 0 release**.

## 1. Motivation

### Why was this resource created?

To provide a **schema and validation infrastructure** for converting clinical
case descriptions into ontology-linked clinical state representations, with
the longer-term aim of supporting early diagnosis of undiagnosed and atypical
clinical presentations.

This Level 0 release **does not redistribute any source texts, surface forms,
spans, or paper identifiers**. It contains only schema, synthetic examples,
and validation tooling.

### Who created this?

Developers and clinical collaborators planning to apply this infrastructure
to undiagnosed and atypical case analysis. Funded in part by, and prepared
for application to, Japanese national research support programs.

## 2. Composition

### What is in this release?

| Item | Description | Count |
|---|---|---:|
| Schema files | JSON Schema definitions | 1 |
| Synthetic examples | Completely fictional case-style examples | 3 (≥3, all fictional) |
| Validation code | JSON Schema validator | minimal |
| Aggregate statistics | None in v0.1.0; planned for v0.2.0+ | 0 |
| Real source data | **Not redistributed in any version of this repository** | 0 |

### What is the data?

This repository **does not contain a corpus of real annotations**.
Synthetic examples in `annotation_schema/example_synthetic.json` are entirely
fictional and do not derive from any real publication or patient.

### What is each instance?

A synthetic example is a JSON document containing annotations of a fictional
clinical narrative. Each annotation has fields described by the schema:
HPO_ID, hpo_label, category, presence, tier, iteration, review_status, etc.

## 3. Collection Process

Synthetic examples were authored manually to demonstrate the schema.
No collection from real sources is performed for this release.

Future releases may include aggregate statistics derived from machine
annotations of real case reports, but those statistics will NOT include
source-identifying information.

## 4. Preprocessing

Not applicable for v0.1.0 (synthetic only).

## 5. Uses

### Recommended uses

- Implementing schema-compatible annotators for clinical narratives
- Validating annotator outputs against the schema
- Understanding annotation field semantics before requesting Level 1+ access

### Discouraged / not-yet-supported uses

- Clinical decision support (this is NOT clinically validated)
- Training data — there is no training data in this release
- Citing as a corpus — there is no corpus in this release

## 6. Distribution

### How is this distributed?

Public GitHub repository under MIT (code) + CC-BY 4.0 (data) dual licensing.

### How is the source corpus distributed?

It is **not distributed** in this repository at any level. Original case
reports are held privately and are subject to publisher / academic society
copyright.

## 7. Maintenance

- Schema versioning is tied to semantic versioning of this repository
- Updates happen as schema stabilizes and as Levels are added
- Issues / questions: GitHub Issues
- Contact: [`CONTACT.md`](./CONTACT.md)

## 8. Known limitations

- Schema is preliminary; will evolve through v1.0.0
- No real annotated data is yet released; users cannot evaluate quality
  empirically until Level 1+
- HPO is the primary ontology in v0.1.0; expansion to other ontologies is planned
- Synthetic examples represent narrow clinical scenarios

## 9. Re-identification considerations

Even with this restricted release, we have taken care that:

- No surface text from real publications appears anywhere
- No DOI, PMID, PMCID, or paper title is included
- No combination of fields could enable reverse lookup
- Synthetic examples are clearly marked as fictional

## 10. Methodology source code

The annotation pipeline source code (RLM iteration logic, structural chunking,
extend chain, complement strategy, etc.) is **not included**. It will be
released alongside the methodology paper. Until then, only high-level
description is publicly available
([`docs/annotation_workflow_overview.md`](./docs/annotation_workflow_overview.md)).
