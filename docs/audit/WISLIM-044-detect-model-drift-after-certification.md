---
id: WISLIM-044
source_id: AS09
kind: red-team
title: "Detect model drift after certification"
severity: medium
workstream: security
labels: [audit, red-team, severity:medium, workstream:security]
source_lines: "n/a (red-team scenario)"
quote_line: 1493
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-019, WISLIM-065]
github_issue: 44
---

# WISLIM-044: Detect model drift after certification

> **Severity:** medium · **Kind:** red-team · **Source:** `AS09`  
> **GitHub issue:** [#44](https://github.com/docxology/WISLIM-audit/issues/44)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Changes to the framework must follow a formal amendment process with: - High consensus thresholds - Public deliberation requirements - Pilot testing before adoption - Periodic drift audits
>
> — `source/WISLIM-v2.0.1.txt:1493`

Certification is not bound to a model version or conditioned on re-testing after a weight change.

## Summary

Certification attaches to a model version, but vendors can deploy new weights silently. The FLVS can keep relying on an old certificate while decisions are made by an uncertified model.

## Evidence

- **Actor:** A vendor updates a model after certification.
- **Preconditions:** The FLVS certifies a model version but does not monitor updates.
- **Attack path:** The vendor deploys a new version with different behavior. The FLVS continues to rely on the old certification.
- **Impact:** Decisions are made by an uncertified model.
- **Detection:** Version pinning; hash verification; continuous monitoring.
- **Mitigation:** Require recertification for updates; publish model hashes; monitor behavior.
- **Residual risk:** Vendors may change models silently. Medium.

## Why it matters

Certification is a claim about a specific artifact. Without version binding and re-testing, it silently becomes a claim about whatever the vendor ships next.

## Required repair

1. Require recertification for updates
2. Publish model hashes
3. Monitor behavior.

## Acceptance criteria

- [ ] Certification is bound to a model digest and expires on any weight change; a silent model swap is detected and blocks approval.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-019`
- `WISLIM-065`

## Tracking

This record is mirrored to GitHub issue #44.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
