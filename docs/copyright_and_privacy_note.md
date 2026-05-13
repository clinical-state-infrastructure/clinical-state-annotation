# Copyright and Privacy Note

## Why we do not redistribute source texts

Clinical case reports are typically published in academic journals owned by
medical societies or commercial publishers. Reproducing or redistributing the
**full text**, **sentence text**, or **surface forms** of such reports without
explicit publisher / society permission would risk copyright infringement.

This repository therefore **does not** include:

- Source-text content from any real publication
- Sentence text
- Surface forms (annotated word strings)
- Original article titles, DOIs, PMIDs, PMCIDs, URLs
- Any identifier through which a third party could locate the original source

These restrictions are deliberate and apply to **all current and planned
versions of this repository at Level 0**. Later levels may relax some
restrictions only after explicit publisher / society approval and
appropriate ethics review.

## Why we do not include patient-identifying information

Even when individual case reports are deidentified at publication, combinations
of fields (age, sex, location, rare disease, presentation timeline) can in
principle enable patient re-identification. For this reason we do not include
in any form:

- Patient demographics tied to a specific case
- Geographic information
- Date-of-event information at fine granularity
- Rare-disease combinations specific to an individual

Where aggregate statistics are released in future versions, we will:

- Apply **k-anonymity-like aggregation** thresholds (e.g., minimum n = 5 per cell)
- Use **document hashing** (`doc_hash` = SHA-256 of source ID with a private salt)
  so that cross-version linkage is possible without revealing source identity
- Avoid releasing high-density continuous span information that could enable
  text reconstruction

## High-density continuous spans

A particular risk is releasing many overlapping span offsets together with HPO
coverage statistics. In principle, an attacker who possesses a copy of the
source text could verify candidate alignments and reconstruct surface form.

To mitigate:

- Spans will only appear from Level 2 onward, under controlled access
- Continuous-span density will be controlled and partitioned
- Where appropriate, only **sentence-level references** will be released

## Synthetic data

All synthetic examples in this repository are **entirely fictional**. They do
not derive from any real publication or patient. They exist solely to
demonstrate the schema. They are released under CC-BY 4.0.

## Methodology source code

Implementation of the annotation pipeline (RLM iteration, chunking strategy,
extend chain, complement strategy) is held privately pending peer-reviewed
publication. This is to avoid premature disclosure of novel methodological
contributions. High-level description appears in
`docs/annotation_workflow_overview.md`.

## If you find a privacy / copyright concern

Please contact us via [`CONTACT.md`](../CONTACT.md). We take such reports
seriously and will respond promptly. If a concern is verified, we will
remove or revise affected content as quickly as possible.
