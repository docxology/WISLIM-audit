---
id: WISLIM-018
source_id: C18
kind: claim
title: "Publish the prompts and ratification record, or withdraw the claim"
severity: high
workstream: evidence
labels: [audit, claim, severity:high, workstream:evidence]
source_lines: "1108"
quote_line: 1106
audit_modules: [audit/07-consensus-and-evidence.md, evidence/ai-letter-audit.md]
related: [WISLIM-017]
github_issue: 18
---

# WISLIM-018: Publish the prompts and ratification record, or withdraw the claim

> **Severity:** high · **Kind:** claim · **Source:** `C18`  
> **GitHub issue:** [#18](https://github.com/docxology/WISLIM-audit/issues/18)  
> **Audit modules:** audit/07-consensus-and-evidence.md, evidence/ai-letter-audit.md  
> **Source lines:** 1108

## Quoted passage

> Despite our differences, we converged on a unified framework— the "Consensus Statement v1.0"—which every participating AI system ratified without amendment.
>
> — `source/WISLIM-v2.0.1.txt:1106`

## Summary

Every participating AI ratified Consensus Statement v1.0 without amendment. Verdict: `unverifiable`. No signatures, prompts, transcripts, model versions, or independent verification are provided. The letters are prose, not ratifications. The claim of unanimity is asserted by the same process it describes.

## Evidence

- **Claim:** Every participating AI ratified Consensus Statement v1.0 without amendment.
- **Anchor:** "which every participating AI system ratified without"
- **Source:** `source/WISLIM-v2.0.1.txt:1108`
- **Verdict:** `unverifiable`; severity `high`.
- **Audit:** `audit/07-consensus-and-evidence.md`

## Why it matters

The ratification claim is the specific evidentiary basis for C17. Without prompts, transcripts, or an amendment record, it cannot be checked.

## Steelman and reply

The reply is that the ratification is documented in Appendix B. Appendix B contains letters, not a ratification record, and the paper does not publish the prompts or the amendment process.

## Required repair

1. Publish raw prompts and transcripts, or drop the ratification claim.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C18` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/07-consensus-and-evidence.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C18` is updated from `unverifiable` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-017`

## Tracking

This record is mirrored to GitHub issue #18.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
