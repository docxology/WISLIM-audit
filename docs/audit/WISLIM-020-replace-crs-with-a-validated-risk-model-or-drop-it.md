---
id: WISLIM-020
source_id: C20
kind: claim
title: "Replace CRS with a validated risk model or drop it"
severity: high
workstream: formal
labels: [audit, claim, severity:high, workstream:formal]
source_lines: "2158"
quote_line: 2158
audit_modules: [audit/09-governance-and-oversight.md, audit/08-formal-and-scientific-claims.md]
related: [WISLIM-019, WISLIM-012]
github_issue: 20
---

# WISLIM-020: Replace CRS with a validated risk model or drop it

> **Severity:** high · **Kind:** claim · **Source:** `C20`  
> **GitHub issue:** [#20](https://github.com/docxology/WISLIM-audit/issues/20)  
> **Audit modules:** audit/09-governance-and-oversight.md, audit/08-formal-and-scientific-claims.md  
> **Source lines:** 2158

## Quoted passage

> Combined Risk Score (CRS): CRS = IS × II × log(ID)
>
> — `source/WISLIM-v2.0.1.txt:2158`

## Summary

CRS = IS x II x log(ID) is a valid risk score. Verdict: `invalid`. The units are unspecified. log(ID) is negative for durations below one unit and zero at one unit. The formula ignores probability, severity distribution, consent, and uncertainty. It is arbitrary, unvalidated, and easy to game.

## Evidence

- **Claim:** CRS = IS x II x log(ID) is a valid risk score.
- **Anchor:** "Combined Risk Score (CRS): CRS = IS × II × log(ID)"
- **Source:** `source/WISLIM-v2.0.1.txt:2158`
- **Verdict:** `invalid`; severity `high`.
- **Audit:** `audit/09-governance-and-oversight.md`

## Why it matters

The CRS determines which decisions get review. If the score is a product of self-reported inputs, an actor can choose its own tier.

## Steelman and reply

The reply is that the CRS is a triage heuristic, not a measurement. A triage heuristic that selects its own inputs and thresholds is a gatekeeping device, and the paper gives no calibration or validation.

## Required repair

1. Use a validated risk model with explicit assumptions, calibration, and adversarial testing.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C20` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/09-governance-and-oversight.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C20` is updated from `invalid` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-019`
- `WISLIM-012`

## Tracking

This record is mirrored to GitHub issue #20.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
