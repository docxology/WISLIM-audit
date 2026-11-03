---
id: WISLIM-010
source_id: C10
kind: claim
title: "Defend the missing normative premise"
severity: critical
workstream: argument
labels: [audit, claim, severity:critical, workstream:argument]
source_lines: "1282"
quote_line: 1278
audit_modules: [audit/04-necessity-to-priority.md, audit/12-steelman.md]
related: [WISLIM-009]
github_issue: 10
---

# WISLIM-010: Defend the missing normative premise

> **Severity:** critical · **Kind:** claim · **Source:** `C10`  
> **GitHub issue:** [#10](https://github.com/docxology/WISLIM-audit/issues/10)  
> **Audit modules:** audit/04-necessity-to-priority.md, audit/12-steelman.md  
> **Source lines:** 1282

## Quoted passage

> Because all values, truths, and meanings that matter require decision-making systems to exist and retain agency, the preservation and enhancement of that decision-making capacity (agency) is the highest-priority constraint for moral coordination and action.
>
> — `source/WISLIM-v2.0.1.txt:1278`

## Summary

Life protection is the highest-priority constraint for moral coordination and action. Verdict: `unsupported`. This is the central normative premise. It is asserted rather than argued. Counterexamples in which truth, justice, autonomy, equality, or consent outrank survival are not addressed, and no conflict-resolution rule is given.

## Evidence

- **Claim:** Life protection is the highest-priority constraint for moral coordination and action.
- **Anchor:** "highest-priority constraint for moral coordination and action"
- **Source:** `source/WISLIM-v2.0.1.txt:1282`
- **Verdict:** `unsupported`; severity `critical`.
- **Audit:** `audit/04-necessity-to-priority.md`

## Why it matters

A highest-priority constraint needs a decision rule for conflicts. The paper gives none, so the ranking cannot guide action when lives and agency collide.

## Steelman and reply

The reply is that the highest-priority constraint is a presumption, not an absolute, and can be outweighed. But the paper gives no weight, threshold, or procedure for outweighing it, so the presumption is either absolute or empty.

## Required repair

1. State the premise explicitly, defend it against counterexamples, and specify scope, thresholds, and exceptions.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C10` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/04-necessity-to-priority.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C10` is updated from `unsupported` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-009`

## Tracking

This record is mirrored to GitHub issue #10.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
