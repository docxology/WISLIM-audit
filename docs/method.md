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
