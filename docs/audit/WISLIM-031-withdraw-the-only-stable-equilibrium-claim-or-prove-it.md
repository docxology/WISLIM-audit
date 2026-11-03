---
id: WISLIM-031
source_id: C31
kind: claim
title: "Withdraw the 'only stable equilibrium' claim or prove it"
severity: high
workstream: formal
labels: [audit, claim, severity:high, workstream:formal]
source_lines: "12721"
quote_line: 12721
audit_modules: [audit/08-formal-and-scientific-claims.md]
related: [WISLIM-023]
github_issue: 31
---

# WISLIM-031: Withdraw the 'only stable equilibrium' claim or prove it

> **Severity:** high · **Kind:** claim · **Source:** `C31`  
> **GitHub issue:** [#31](https://github.com/docxology/WISLIM-audit/issues/31)  
> **Audit modules:** audit/08-formal-and-scientific-claims.md  
> **Source lines:** 12721

## Quoted passage

> Result: Life-first is the only evolutionary Nash equilibrium across generations.
>
> — `source/WISLIM-v2.0.1.txt:12721`

## Summary

Life-first is the only stable equilibrium or evolutionarily stable strategy. Verdict: `false`. Game theory does not show this. Equilibria depend on payoffs, institutions, information, and the strategy space. Anti-life strategies can persist, and life-preserving strategies can be exploited.

## Evidence

- **Claim:** Life-first is the only stable equilibrium or evolutionarily stable strategy.
- **Anchor:** "Life-first is the only evolutionary Nash equilibrium"
- **Source:** `source/WISLIM-v2.0.1.txt:12721`
- **Verdict:** `false`; severity `high`.
- **Audit:** `audit/08-formal-and-scientific-claims.md`

## Why it matters

The equilibrium claim turns a moral proposal into a purported fact of evolution. No model, population, or stability analysis is given.

## Steelman and reply

The reply is that the equilibrium claim is a prediction, not a proof. No model, population, or fitness function is specified, and moral advocacy is not an evolutionary stability analysis.

## Required repair

1. Model explicit games and test the claim; do not assert a general equilibrium result.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C31` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/08-formal-and-scientific-claims.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C31` is updated from `false` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-023`

## Tracking

This record is mirrored to GitHub issue #31.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
