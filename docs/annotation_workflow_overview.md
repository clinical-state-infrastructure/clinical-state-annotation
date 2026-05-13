# Annotation Workflow Overview (high-level)

This document provides a **high-level description** of the recursive-LLM
(RLM) annotation workflow used to populate the clinical state annotation
schema. **Implementation source code is held privately** pending peer-reviewed
publication of the methodology.

## Overall flow

```
[Clinical case description, private]
        │
        ▼
[Structural chunking by clinical section]
        │
        ▼
[Initial LLM extraction per chunk]   ← produces candidate annotations
        │
        ▼
[Recursive refinement: K iterations]
   each iter:
     - chunk strategy rotation
     - complement extraction in uncovered regions
     - merge with deduplication
     - convergence check
        │
        ▼
[Ontology post-validation]            ← HPO ID lookup, normalization
        │
        ▼
[Schema-conformant annotation output]
```

## Key design ideas

1. **Structural chunking**: clinical narratives have a typical section
   structure (chief complaint, history of present illness, etc.). Chunking
   along section boundaries preserves semantic context.

2. **Rotation of chunk strategy**: iterating with rotated chunk boundaries
   exposes "seam" regions to extraction that may have been missed when those
   regions sat on a previous boundary.

3. **Complement extraction**: rather than re-extracting from scratch at each
   iteration, the LLM is asked to find annotations the prior pass missed.
   This is biased toward gap regions and reduces redundant output.

4. **Three-tier convergence**: iteration stops when a target coverage is
   reached, when consecutive iterations no longer add new annotations
   (stagnation), or when the maximum iteration count is reached.

5. **Post-hoc ontology validation**: extracted concept labels are matched to
   HPO identifiers post-hoc, decoupling label production from ontology
   lookup, which yields better fidelity for ambiguous Japanese terms.

## What is NOT in this repository

- Specific prompt templates
- Chunking parameters (sizes, strides, overlap, rotation formulas)
- Iteration scheduler logic
- Complement-extraction prompt and merging rules
- Convergence threshold tuning
- Model selection and inference configuration

These are integral to the methodology and will be released alongside the
forthcoming paper.

## Compatibility for third-party annotators

Third-party annotators can produce output that conforms to the schema
(`annotation_schema/schema.json`). They do not need to use any specific
extraction methodology. The schema is the interface; the workflow above is
one possible implementation.
