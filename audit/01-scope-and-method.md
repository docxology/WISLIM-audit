# Scope, source, and method

## The object

The audit covers the user-supplied PDF, **Version 2.0.1**, dated 4 February
2026. It is 289 pages. The extracted text is 13,255 lines and 40,538 words.

- PDF: `source/WISLIM-v2.0.1.pdf`
- Text: `source/WISLIM-v2.0.1.txt`
- Checksums and metadata: `source/metadata.json`
- Public record: PhilPapers `WISLIM`; DOI `10.21428/4831231e.8c4c6c8f`

The PhilPapers record labels the work an "8th edition." The PDF calls itself
Version 2.0.1. The PubPub release is Release #1. These labels are not reconciled
in the source. The audit treats the PDF as the object and records the
bibliographic inconsistency rather than guessing which label is authoritative.

## What the audit covers

1. The logical form of the central sentence and the paper's reinterpretation of
   it.
2. The definition of "life" and the related terms "agency," "harm," "needless,"
   and "important."
3. The inference from necessity to priority, including the T1/T2/T3 arguments.
4. The `E∞` formula and the "Life-First Necessity Theorem."
5. The AI-consensus evidence and the seven letters in Appendix B.
6. The 210 stress tests in Appendix D.
7. The implementation blueprint (LFDI, FLVS, ULP, CRS, Layer M).
8. The rhetoric, integrity screen, and governance implications.
9. The citations and publication record.

## What the audit does not cover

- **Raw AI transcripts.** The audit does not have the prompts, model versions,
  sampling parameters, or full workspace logs. The consensus critique is
  therefore methodological, not forensic. It shows that the published process
  cannot support the published claim; it does not reconstruct what each model
  was told.
- **The author's intentions.** The audit critiques the argument and its likely
  effects, not the author's character or motives.
- **The truth of the paper's metaethical premises.** The audit does not settle
  whether value is valuer-dependent. It shows that the paper does not settle it
  either.
- **Clinical, legal, or safety certification.** The paper's suicide, triage, and
  integrity-screen examples are discussed as risk cases, not as guidance.
- **The 8th edition.** If the 8th edition differs materially from Version 2.0.1,
  the line citations may not transfer. The audit would need the new PDF.

## Method

### 1. Source-bound claim extraction

The audit identifies the paper's load-bearing claims and assigns stable IDs
(`C01`–`C35`). Each claim records a short paraphrase, an exact anchor quote, a
section, and the first line of the anchor in the extracted text. The registry is
`model/claims.json`.

### 2. Charitable reconstruction

Before criticizing a claim, the audit states the strongest version it can. The
steelman is in `audit/12-steelman.md`. The purpose is to avoid attacking a
weaker claim than the paper needs.

### 3. Logical and definitional checks

The audit checks:

- whether the conclusion follows from the premises;
- whether the terms are used consistently;
- whether the definitions are circular, overinclusive, or underinclusive;
- whether a necessity claim is being confused with a priority claim;
- whether a descriptive premise is being used to support a normative
  conclusion.

### 4. Evidence audit

For empirical and consensus claims, the audit asks:

- What is the sample?
- Who was asked, and under what conditions?
- Was the elicitation independent and blinded?
- Were the prompts and coding rules fixed in advance?
- Is there a control or comparison?
- Are negative or dissenting results reported?
- Can the claim be falsified?

### 5. Formal audit

For the `E∞` formula and the 210 stress tests, the audit checks whether the
formal result is correctly stated and whether it actually bears on the moral
conclusion. A formal result can be valid and still be irrelevant.

### 6. Red-team scenarios

The red-team section constructs plausible misuse, capture, and failure
scenarios. These are not predictions; they are stress tests for the framework's
institutions and rhetoric.

### 7. Reproducibility

`tools/validate.py` checks the source checksums, claim anchors, line bounds, the
210-test catalog, and internal links. `tests/test_repository.py` wraps the
validator for pytest. The audit uses only the Python standard library.

## Evidence standards

The paper claims **proof**, **universality**, **irrefutability**, and **100%
consensus**. Those are strong standards. The audit holds the paper to them. A
rhetorical analogy, a self-referential argument, or a shared-context model
convergence does not meet them.

## How to read the rest

- Start with `00-verdict.md`.
- Read `02`–`11` for the argument-by-argument audit.
- Read `12` for the strongest version of the paper.
- Read `13` for failure modes and `red-team/` for misuse scenarios.
- Read `14` for a prioritized repair plan.

Line citations use the form `source/WISLIM-v2.0.1.txt:778`. The text is an
extraction; page layout and typography are not authoritative. Section names are
given when a line citation alone would be ambiguous.
