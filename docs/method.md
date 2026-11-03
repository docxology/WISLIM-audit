# Method

## Questions

The audit asks five questions:

1. **Form:** What proposition, if any, does the paper actually assert? Is it the
   same proposition it claims to prove?
2. **Definitions:** Are the central terms ("life," "agency," "importance,"
   "harm," "needless") defined consistently and independently?
3. **Inference:** Do the arguments validly connect the premises to the stated
   conclusions? Where are the normative premises?
4. **Evidence:** What evidence is offered, and does it meet the standards the
   paper claims (proof, universality, irrefutability, consensus)?
5. **Consequences:** If implemented, what could the framework do — including to
   people who dissent, to institutions, and to the paper's own stated values?

## Standards

- **Source-bound.** Every claim about the paper cites a section or a line in
  `source/WISLIM-v2.0.1.txt`. Line numbers are 1-based and newline-delimited
  (`wc -l`, `grep -n`), not Python `splitlines()` numbering; see
  `evidence/provenance.md`.
- **Charity first.** Each major objection is tested against the strongest
  reconstruction in `audit/12-steelman.md`.
- **No motive attribution.** The audit critiques arguments and institutions,
  not the author's character.
- **Explicit uncertainty.** Where the evidence is unavailable (for example, the
  raw AI prompts), the audit says so rather than inferring.
- **Falsifiability.** The audit states what would count as evidence against its
  own verdict.
- **Reproducibility.** The source checksums, line anchors, claim registry, and
  stress-test catalog are machine-checkable.

## What this is not

- Not a peer-reviewed verdict.
- Not a metaethical treatise; it does not settle whether value is
  valuer-dependent.
- Not a legal, medical, clinical, or safety certification.
- Not a forensic audit of the AI letters' prompts or model weights.

## Issue register

Every finding is decomposed into a stable issue in `model/issues.json` and one
record in `docs/audit/`. There are three kinds:

- **Claim issues** (`WISLIM-001`–`035`) attack a registered claim (`C01`–`C35`).
  Each carries the claim's verdict, one or more verbatim primary quotations, and
  a steelman reply that states the strongest defense and why it does not hold.
- **Red-team issues** (`WISLIM-036`–`055`) attack a control or design element
  (`AS01`–`AS20`). Each carries the actor, preconditions, attack path, impact,
  detection, mitigation, residual risk, and suggested checks for reviewers.
- **Workstream issues** (`WISLIM-056`–`066`) group remediation options
  (`WS01`–`WS11`). Each names the claims, scenarios, and modules it covers.

## External review register (`OPH-LFDI-57`)

External critiques received in connection with the audited framework are
decomposed using the same source-bound rules:

- **Source preservation and OCR provenance** (`reviews/oph-lfdi-57/source/`):
  the received PDF and normalized OCR text are checksummed in
  `reviews/oph-lfdi-57/source/metadata.json`.
- **Topic decomposition** (`OPH-REV-001`–`OPH-REV-012` in
  `reviews/oph-lfdi-57/model/review.json`): each distinct claim is anchored to a
  verbatim quote and line number in `LFDI_Alignment_Audit-57.txt`, graded
  intrinsically (`valid`, `partly-valid`, `unsupported`, `question-begging`,
  `out-of-scope`, `unverifiable`), and graded extrinsically against OPH
  (`addressed`, `refuted`, `not-addressed`, `unverifiable`) and against the
  WISLIM audit (`WISLIM-001`–`WISLIM-066`).
- **Modular outputs**: `scripts/build_review_register.py` (`make review`)
  renders each topic to `reviews/oph-lfdi-57/topics/` and
  `docs/reviews/oph-lfdi-57/topics/`, plus the summary indexes in
  `reviews/oph-lfdi-57/README.md`, `docs/reviews/oph-lfdi-57/README.md`, and
  `docs/reviews.md`.

Every issue opens with a publication reference built from
`source/metadata.json`: title, author, version, date, page count, DOI,
PhilPapers record, source-of-record digests, and the audit-status disclaimer. It
then carries at least one `quotes` entry, rendered as a block quotation with a
line citation. The validator checks that each normalized quotation is a
substring of the source text within the cited line's window. This is deliberate:
a finding that cannot be anchored to the paper is not part of the register.
Remediation is written as options for the author, not as instructions or
deployment gates. Each issue carries `status: observation` and a status note
saying it is an audit observation, not a required fix; an author may decline a
proposed response with reasons. Issue titles name a concern and a possible
response, so they should be read as suggestions rather than commands.

## Evidence classes

| Class | Meaning |
|---|---|
| `quoted` | Direct text from the source, with a line anchor. |
| `logical` | A validity or inference defect that can be checked formally. |
| `definitional` | A term is ambiguous, circular, or used inconsistently. |
| `empirical` | A factual claim that would require data to support. |
| `bibliographic` | A claim about the publication record or citations. |
| `red-team` | A plausible misuse or failure scenario, not a prediction. |

## Severity

Severity is an impact estimate, not a fatality rating. It says how much a
concern could matter if it applies; it does not say the work is invalid, nor
does it make a response mandatory.

| Severity | Meaning |
|---|---|
| Critical | Could materially undermine a central claim or create a serious harm pathway if the framework were implemented as written. |
| High | Could materially weaken the argument or a major implementation claim. |
| Medium | Localized impact; worth considering but not central. |
| Low | Clarity, style, or minor bibliographic note. |
