---
id: WISLIM-036
source_id: AS01
kind: red-team
title: "Prevent CRS underreporting from bypassing review"
severity: critical
workstream: governance
labels: [audit, red-team, severity:critical, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_line: 2158
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-020, WISLIM-057]
github_issue: 36
---

# WISLIM-036: Prevent CRS underreporting from bypassing review

> **Severity:** critical · **Kind:** red-team · **Source:** `AS01`  
> **GitHub issue:** [#36](https://github.com/docxology/WISLIM-audit/issues/36)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Combined Risk Score (CRS): CRS = IS × II × log(ID) - Determines verification tier and latency budgets
>
> — `source/WISLIM-v2.0.1.txt:2158`

The three inputs are self-reported, and the paper provides no independent feed or audit.

## Summary

The hospital supplies the three CRS inputs that determine its review tier, and nothing independently checks them. An administrator can classify a risky cost-cutting decision as low-scope and short-duration, keep the score below the Layer 3 threshold, and obtain automated approval while the record shows compliance.

## Evidence

- **Actor:** A hospital administrator under financial pressure.
- **Preconditions:** The hospital self-reports `IS`, `II`, and `ID`; the CRS routes decisions to review layers; there is no independent audit of the inputs.
- **Attack path:** The administrator classifies a risky cost-cutting decision as low-scope and short-duration. The CRS falls below the Layer 3 threshold. The decision is approved by an automated check. Patients are harmed.
- **Impact:** Preventable injury or death; erosion of trust; the framework's records show compliance.
- **Detection:** Compare self-reported inputs with independent data (patient outcomes, staffing levels, incident reports). Audit a random sample.
- **Mitigation:** Independent data feeds; random audits; whistleblower protection; criminal liability for false reporting; publish aggregate CRS distributions.
- **Residual risk:** Sophisticated actors can manipulate the data in ways that are hard to detect. High.

## Why it matters

The score is only as good as its inputs. Self-reporting makes the review tier an honor system, and an honor system cannot carry decisions that may kill people.

## Required repair

1. Independent data feeds
2. Random audits
3. Whistleblower protection
4. Criminal liability for false reporting
5. Publish aggregate CRS distributions.

## Acceptance criteria

- [ ] An independent data feed or random audit detects a seeded 20% underreport of IS, II, or ID before the decision is approved.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-020`
- `WISLIM-057`

## Tracking

This record is mirrored to GitHub issue #36.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
