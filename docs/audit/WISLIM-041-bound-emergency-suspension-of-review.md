---
id: WISLIM-041
source_id: AS06
kind: red-team
title: "Bound emergency suspension of review"
severity: critical
workstream: governance
labels: [audit, red-team, severity:critical, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_line: 1509
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-030, WISLIM-059]
github_issue: 41
---

# WISLIM-041: Bound emergency suspension of review

> **Severity:** critical · **Kind:** red-team · **Source:** `AS06`  
> **GitHub issue:** [#41](https://github.com/docxology/WISLIM-audit/issues/41)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> This is not philosophy. This is engineering. It is a complete specification for building life-protecting systems.
>
> — `source/WISLIM-v2.0.1.txt:1509`

The 'complete specification' contains no emergency-suspension clause, sunset, or independent trigger.

## Summary

The framework permits emergency suspension of verification, and nothing in the design limits its scope or duration. A government or coalition can rule by decree indefinitely while claiming emergency necessity.

## Evidence

- **Actor:** A state or international body facing a crisis.
- **Preconditions:** Layer M allows emergency exceptions; the exception can suspend Layer 4 review.
- **Attack path:** The body declares an emergency, suspends review, and makes irreversible decisions. The emergency is renewed indefinitely.
- **Impact:** Decisions escape oversight; capture is easiest when stakes are highest.
- **Detection:** Track emergency declarations; require automatic expiration; publish decisions after the emergency.
- **Mitigation:** Narrow emergency powers; sunset clauses; judicial review; legislative approval.
- **Residual risk:** Crises create pressure to bypass procedures. High.

## Why it matters

An emergency exception with no sunset, scope limit, or independent trigger is a permanent opt-out from the framework's safeguards.

## Required repair

1. Narrow emergency powers
2. Sunset clauses
3. Judicial review
4. Legislative approval.

## Acceptance criteria

- [ ] Emergency suspension requires a declared scope, an independent trigger, a sunset, and publication; a simulated renewal is denied.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-030`
- `WISLIM-059`

## Tracking

This record is mirrored to GitHub issue #41.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
