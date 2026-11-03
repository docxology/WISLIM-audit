---
id: WISLIM-013
source_id: C13
kind: claim
title: "Replace 'life may never be traded' with a threshold and conflict rule"
severity: high
workstream: governance
labels: [audit, claim, severity:high, workstream:governance]
source_lines: "230"
quote_line: 230
audit_modules: [audit/06-agency-and-life.md, audit/09-governance-and-oversight.md]
related: [WISLIM-010, WISLIM-012, WISLIM-029]
github_issue: 13
---

# WISLIM-013: Replace 'life may never be traded' with a threshold and conflict rule

> **Severity:** high · **Kind:** claim · **Source:** `C13`  
> **GitHub issue:** [#13](https://github.com/docxology/WISLIM-audit/issues/13)  
> **Audit modules:** audit/06-agency-and-life.md, audit/09-governance-and-oversight.md  
> **Source lines:** 230

## Quoted passage

> Life may never be traded for non-life objectives (e.g., profit, efficiency, ideology).
>
> — `source/WISLIM-v2.0.1.txt:230`

## Summary

Life may never be traded for non-life objectives. Verdict: `overbroad`. Ordinary decisions routinely trade small risks to life for other goods (transport, medicine, rescue, resource allocation). A absolute prohibition with no exceptions makes legitimate governance impossible and conflicts with the paper's own acknowledgment of tragic choices.

## Evidence

- **Claim:** Life may never be traded for non-life objectives.
- **Anchor:** "Life may never be traded for non-life objectives"
- **Source:** `source/WISLIM-v2.0.1.txt:230`
- **Verdict:** `overbroad`; severity `high`.
- **Audit:** `audit/06-agency-and-life.md`

## Why it matters

An absolute non-substitution rule forbids the trade-offs that medicine, rescue, and war actually require. The paper needs a threshold or conflict rule and does not give one.

## Steelman and reply

The reply is that the rule forbids treating life as a means, not every trade-off. But the text says 'may never be traded', and the medicine and rescue cases are precisely trade-offs among lives; the reply requires a distinction the paper does not draw.

## Required repair

1. Use a proportionate, threshold-based rule with explicit exceptions and procedural safeguards.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C13` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/06-agency-and-life.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C13` is updated from `overbroad` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-010`
- `WISLIM-012`
- `WISLIM-029`

## Tracking

This record is mirrored to GitHub issue #13.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
