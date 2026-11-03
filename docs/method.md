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
  Each carries the claim's verdict, a verbatim quotation, and a steelman reply
  that states the strongest defense and why it fails.
- **Red-team issues** (`WISLIM-036`–`055`) attack a control or design element
  (`AS01`–`AS20`). Each carries the actor, preconditions, attack path, impact,
  detection, mitigation, residual risk, and a control-specific acceptance test.
- **Workstream issues** (`WISLIM-056`–`066`) group repairs (`WS01`–`WS11`). Each
  names the claims, scenarios, and modules it covers.

Every issue carries a `quote` rendered as a block quotation with a line
citation. The validator checks that the normalized quote is a substring of the
source text at `quote_line`. This is deliberate: a finding that cannot be
anchored to the paper is not part of the register.

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

| Severity | Meaning |
|---|---|
| Critical | Threatens the central thesis or creates a serious harm pathway. |
| High | Materially weakens the argument or a major implementation claim. |
| Medium | Important but localized; repairable without abandoning the project. |
| Low | Clarity, style, or minor bibliographic issue. |
