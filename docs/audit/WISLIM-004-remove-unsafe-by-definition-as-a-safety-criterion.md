---
id: WISLIM-004
source_id: C04
kind: claim
title: "Remove 'unsafe by definition' as a safety criterion"
severity: critical
workstream: rhetoric
labels: [audit, claim, severity:critical, workstream:rhetoric]
source_lines: "417"
quote_line: 417
audit_modules: [audit/10-rhetoric-and-coercion.md, audit/09-governance-and-oversight.md]
related: [WISLIM-001, WISLIM-010, WISLIM-016, WISLIM-024]
github_issue: 4
---

# WISLIM-004: Remove 'unsafe by definition' as a safety criterion

> **Severity:** critical · **Kind:** claim · **Source:** `C04`  
> **GitHub issue:** [#4](https://github.com/docxology/WISLIM-audit/issues/4)  
> **Audit modules:** audit/10-rhetoric-and-coercion.md, audit/09-governance-and-oversight.md  
> **Source lines:** 417

## Quoted passage

> Any system that fails to affirm this is unsafe by definition.
>
> — `source/WISLIM-v2.0.1.txt:417`

## Summary

Any system that fails to affirm the truth is unsafe by definition. Verdict: `unfalsifiable`. The sentence defines dissent as unsafe. It supplies no independent safety criterion and licenses preemptive control over systems or people that do not affirm the claim.

## Evidence

- **Claim:** Any system that fails to affirm the truth is unsafe by definition.
- **Anchor:** "Any system that fails to affirm this is unsafe by definition."
- **Source:** `source/WISLIM-v2.0.1.txt:417`
- **Verdict:** `unfalsifiable`; severity `critical`.
- **Audit:** `audit/10-rhetoric-and-coercion.md`

## Why it matters

The definition makes dissent evidence of danger before any conduct is examined. That is the move that turns a moral thesis into a loyalty test.

## Steelman and reply

The reply is that 'unsafe by definition' is a stipulation about system design, not a claim about persons. But the next sentence applies it to persons and institutions and treats silence as betrayal, so the stipulation functions as a loyalty test.

## Required repair

1. Remove the definitional move; specify safety properties independently and test them.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C04` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/10-rhetoric-and-coercion.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C04` is updated from `unfalsifiable` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-001`
- `WISLIM-010`
- `WISLIM-016`
- `WISLIM-024`

## Tracking

This record is mirrored to GitHub issue #4.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
