---
id: WISLIM-032
source_id: C32
kind: claim
title: "Replace decorative citations with engaged literature"
severity: medium
workstream: evidence
labels: [audit, claim, severity:medium, workstream:evidence]
source_lines: "392"
quote_line: 392
audit_modules: [audit/11-citations-and-scholarship.md, evidence/citation-audit.md]
related: [WISLIM-027, WISLIM-028]
github_issue: 32
---

# WISLIM-032: Replace decorative citations with engaged literature

> **Severity:** medium · **Kind:** claim · **Source:** `C32`  
> **GitHub issue:** [#32](https://github.com/docxology/WISLIM-audit/issues/32)  
> **Audit modules:** audit/11-citations-and-scholarship.md, evidence/citation-audit.md  
> **Source lines:** 392

## Quoted passage

> See Appendix C for full references to Bostrom, Christiano, Friston, Hadfield-Menell, Leike, Ord, O'Keefe, Russell, Yudkowsky, and others.
>
> — `source/WISLIM-v2.0.1.txt:392`

The appendix lists names; it does not engage their arguments.

## Summary

The paper's citations support its claims. Verdict: `decorative`. The citations are name-drops. Friston is irrelevant to the argument. The paper does not engage the is-ought gap, moral pluralism, or the technical AI-safety literature. Some bibliographic details are inconsistent.

## Evidence

- **Claim:** The paper's citations support its claims.
- **Anchor:** "Appendix C"
- **Source:** `source/WISLIM-v2.0.1.txt:392`
- **Verdict:** `decorative`; severity `medium`.
- **Audit:** `audit/11-citations-and-scholarship.md`

## Why it matters

The citations are the paper's claim to scholarship. If they are name-drops rather than engaged arguments, the paper has not tested its thesis against the literature.

## Steelman and reply

The reply is that the bibliography is a map of relevant literature. A map is not an engagement; none of the cited positions is reconstructed, criticized, or shown to be compatible with the thesis.

## Required repair

1. Add a real literature review with claim-by-claim citation and engagement.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C32` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/11-citations-and-scholarship.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C32` is updated from `decorative` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-027`
- `WISLIM-028`

## Tracking

This record is mirrored to GitHub issue #32.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
