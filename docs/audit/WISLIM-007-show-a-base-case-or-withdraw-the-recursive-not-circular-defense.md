---
id: WISLIM-007
source_id: C07
kind: claim
title: "Show a base case or withdraw the 'recursive, not circular' defense"
severity: critical
workstream: argument
labels: [audit, claim, severity:critical, workstream:argument]
source_lines: "2625"
quote_line: 2625
audit_modules: [audit/03-definition-of-life.md]
related: [WISLIM-006]
github_issue: 7
---

# WISLIM-007: Show a base case or withdraw the 'recursive, not circular' defense

> **Severity:** critical · **Kind:** claim · **Source:** `C07`  
> **GitHub issue:** [#7](https://github.com/docxology/WISLIM-audit/issues/7)  
> **Audit modules:** audit/03-definition-of-life.md  
> **Source lines:** 2625

## Quoted passage

> Response: The definition is recursive, not circular. There is a crucial difference.
>
> — `source/WISLIM-v2.0.1.txt:2625`

## Summary

The definition is recursive, not circular, with observable base cases. Verdict: `false`. No base case, recursion clause, or closure rule is given. 'Recursive' is asserted, not demonstrated. The definition is a mutually recursive relation with no independent grounding, so it does not pick out a determinate class.

## Evidence

- **Claim:** The definition is recursive, not circular, with observable base cases.
- **Anchor:** "The definition is recursive, not circular."
- **Source:** `source/WISLIM-v2.0.1.txt:2625`
- **Verdict:** `false`; severity `critical`.
- **Audit:** `audit/03-definition-of-life.md`

## Why it matters

The recursive defense is the only answer to the circularity objection. If it has no base case, the definition is circular and the central term is undefined.

## Steelman and reply

The reply is that observation statements are the base case. But 'we observe systems making decisions' already uses the contested term, and no decision-independent criterion is given for what counts as a decision or a system.

## Required repair

1. Give a formal inductive definition with base cases and show that it is well-founded.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C07` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/03-definition-of-life.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C07` is updated from `false` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-006`

## Tracking

This record is mirrored to GitHub issue #7.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
