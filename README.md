# clinical-state-annotation

[![Version: v0.1.0](https://img.shields.io/badge/version-0.1.0-orange)](./CHANGELOG.md)
[![License: MIT + CC-BY-4.0](https://img.shields.io/badge/license-MIT_+_CC--BY--4.0-blue)](./LICENSE)
[![Release Policy](https://img.shields.io/badge/release-Level_0-yellow)](./RELEASE_POLICY.md)

> Infrastructure for converting clinical case descriptions into ontology-linked
> **clinical state representations**, supporting early diagnosis of undiagnosed
> and atypical presentations. Schema + validation tooling only;
> **source texts and surface forms are not redistributed**.

---

## 🇺🇸 English (concise)

### What this repository is

This repository provides the **schema, validation, and policy infrastructure**
for a forthcoming clinical state annotation framework. We are building a
recursive-LLM (RLM) semi-automated annotation workflow that extracts symptoms,
findings, temporal information, and HPO / ontology identifiers from case-style
clinical descriptions, with the aim of supporting a **clinical state space**
for undiagnosed and atypical conditions.

This is **v0.1.0 (Level 0 release)**: it contains only the public-safe
components — annotation **schema**, **synthetic examples**, **validation
code**, **data card**, and **release policy**.

### What this is NOT

This repository does **not** contain, and will not contain in Level 0:

- Source case-report texts
- Sentence text or surface forms
- DOIs, PMIDs, PMCIDs, paper titles, URLs
- Any identifier that links to a specific original article
- Salts, environment files, credentials
- Patient-identifying information
- High-density continuous spans that could reconstruct original text

These constraints are deliberate. See
[`docs/copyright_and_privacy_note.md`](./docs/copyright_and_privacy_note.md)
and [`RELEASE_POLICY.md`](./RELEASE_POLICY.md).

### Why machine-only metadata?

Annotation outputs are produced by a local LLM workflow; **no human
reviewer-level corpus is redistributed in Level 0**. We describe the
annotation schema and provide synthetic examples so that third parties can
implement compatible annotators, but we do not release annotations derived
from real source texts in this initial release.

### Purpose

1. Publish schema and validation code without redistributing source articles.
2. Provide a foundation for linking undiagnosed / atypical clinical narratives
   to HPO and other ontologies.
3. Provide a foundation that future projects (blood-EV quality passport,
   preserved-plasma EV quality control, SPARK-seq / aptamer probe development,
   clinical AI diagnostic infrastructure, etc.) can connect to.

### Status

| Component | Status |
|---|---|
| Schema definition | ✅ public (v0.1.0) |
| Synthetic example | ✅ public (v0.1.0) |
| Validation code | ✅ public (v0.1.0) |
| Real annotation corpus | ❌ not redistributed |
| Source texts / surface | ❌ not redistributed |
| Methodology source code | 🔒 private, planned release with paper |

### Usage

```bash
pip install -r scripts/requirements.txt
python scripts/validate_schema.py annotation_schema/example_synthetic.json
python scripts/summarize_annotations.py annotation_schema/example_synthetic.json
pytest tests/
```

### Citation

See [`CITATION.cff`](./CITATION.cff).

### Contact

See [`CONTACT.md`](./CONTACT.md).

### Acknowledgements
- This work was supported by JSPS KAKENHI Grant Number JP22K12253.

---

## 🇯🇵 日本語 (詳細)

### 本リポジトリの目的

本リポジトリは、症例報告等の臨床記述を、HPO 等のオントロジーに紐付けた
**「臨床状態表現 (clinical state representation)」** に変換するための
**スキーマと検証基盤**を公開します。

将来的には、RLM (Recursive Language Model) を用いた半自動アノテーション
ワークフローによって、症状・所見・時間情報・HPO/ontology ID 等を抽出し、
**未診断・非典型例の早期診断**に向けた **臨床状態空間 (clinical state space)**
を構築することを目指します。

本リポジトリは **v0.1.0 (Level 0 公開)** であり、公開しても問題のない要素
(スキーマ、合成例、検証コード、データカード、公開ポリシー) のみを
含みます。

### 公開しないもの

著作権・学会許諾・再識別リスクに配慮し、本リポジトリには以下を **含めません**:

- 症例報告本文 / sentence text / surface form
- DOI / PMID / PMCID / 論文タイトル / URL
- 元文献と直接対応可能な ID
- salt / `.env` 等の secrets
- 患者識別につながる情報
- 原文を復元可能な高密度連続 span 情報

詳細は [`docs/copyright_and_privacy_note.md`](./docs/copyright_and_privacy_note.md)
および [`RELEASE_POLICY.md`](./RELEASE_POLICY.md) を参照してください。

### Machine-only metadata 方針

アノテーション出力はローカル LLM ワークフローで生成されます。**Level 0 時点では、
人手レビュー済の corpus は再配布しません**。スキーマと合成例のみ公開することで、
第三者が互換性のあるアノテーターを実装できる形にしつつ、実テキストに由来する
アノテーションは含めません。

### このリポジトリで提供するもの

| 要素 | 内容 |
|---|---|
| `annotation_schema/schema.json` | アノテーション形式の JSON Schema |
| `annotation_schema/example_synthetic.json` | 完全に架空の症例例 (動作確認用) |
| `scripts/validate_schema.py` | JSON Schema による検証ツール (最小限) |
| `scripts/summarize_annotations.py` | 合成例の集計デモ (最小限) |
| `DATA_CARD.md` | Datasheets for Datasets 形式の説明 |
| `RELEASE_POLICY.md` | Level 0 → Level 3 の段階公開計画 |
| `DATA_LICENSE.md` | データライセンス詳細 |
| `docs/copyright_and_privacy_note.md` | 著作権・プライバシー注意事項 |
| `docs/staged_release_policy.md` | 段階公開の運用詳細 |
| `docs/annotation_workflow_overview.md` | RLM ワークフローの概要 (high-level のみ) |

### 段階公開計画 (概要)

| Level | 内容 | 時期 |
|---|---|---|
| **Level 0 (v0.1.0)** | schema + synthetic + validation + policy | **2026-05-13 ← 本リリース** |
| Level 1 | + per-annotation ontology metadata (controlled access、doc_hash 化) | 学会発表後 |
| Level 2 | + span 情報 (共同研究者向け、IRB 確認) | 学会・出版社許諾後 |
| Level 3 | + surface + DOI (open corpus) | 全許諾完了後 |

詳細は [`RELEASE_POLICY.md`](./RELEASE_POLICY.md)。

### 接続計画

将来的に、血液 EV 品質パスポート、保存血漿 EV 品質制御、SPARK-seq / aptamer
probe 開発、臨床 AI 診断基盤など、関連する臨床基盤プロジェクトと接続する
ことを想定しています。

### Methodology source code

RLM annotation pipeline の core source は本リポジトリには含めません。
論文公開時に別途リリース予定です。本リポジトリでは high-level な概要のみ
[`docs/annotation_workflow_overview.md`](./docs/annotation_workflow_overview.md)
に記載しています。

### ライセンス

- Code: MIT
- Schema / docs / synthetic: CC-BY 4.0

詳細は [`LICENSE`](./LICENSE) と [`DATA_LICENSE.md`](./DATA_LICENSE.md)。

### 引用

[`CITATION.cff`](./CITATION.cff) を参照。

### 連絡先

[`CONTACT.md`](./CONTACT.md) を参照。

### 謝辞

- 創発的研究支援事業 (JST FOREST) 申請に関連した基盤整備として開始
- HPO project, Examining-HPO-by-organ, ogishima/HPO-japanese
- 本研究はJSPS科研費 JP22K12253 の助成を受けたものです
