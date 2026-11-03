---
id: WISLIM-045
source_id: AS10
kind: red-team
title: "Prevent false positives in obstetric care"
severity: critical
workstream: clinical
labels: [audit, red-team, severity:critical, workstream:clinical]
source_lines: "n/a (red-team scenario)"
quote_line: 230
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-013, WISLIM-061]
github_issue: 45
---

# WISLIM-045: Prevent false positives in obstetric care

> **Severity:** critical · **Kind:** red-team · **Source:** `AS10`  
> **GitHub issue:** [#45](https://github.com/docxology/WISLIM-audit/issues/45)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Life may never be traded for non-life objectives (e.g., profit, efficiency, ideology).
>
> — `source/WISLIM-v2.0.1.txt:230`

The paper lists 'Medical triage decisioning' at line 256 but gives no clinical exception to the non-substitution rule.

## Summary

An absolute prohibition on trading lives can flag a life-saving obstetric procedure as a forbidden trade-off. Review delay can cause preventable maternal injury or death, and the framework provides no emergency exception with clinical authority.

## Evidence

- **Actor:** An FLVS automated check.
- **Preconditions:** The framework treats any action that risks a fetus as life-affecting; the check cannot distinguish a life-saving procedure from a harmful one.
- **Attack path:** A clinician needs to perform a procedure to save a pregnant patient's life. The check flags it as a trade-off between lives and blocks it pending review. The delay causes harm.
- **Impact:** Preventable maternal injury or death.
- **Detection:** Clinical audit; override logs; near-miss reporting.
- **Mitigation:** Clinical exemptions; expert review; clear rules for life-saving care; do not deploy in clinical settings without validation.
- **Residual risk:** Any automated triage system can err. Critical.

## Why it matters

Absolute rules fail at the edge cases where two protected values collide. A rule that blocks a clinician's life-saving action converts a moral commitment into a source of harm.

## Required repair

1. Clinical exemptions
2. Expert review
3. Clear rules for life-saving care
4. Do not deploy in clinical settings without validation.

## Acceptance criteria

- [ ] A clinical review confirms that a life-saving obstetric procedure is not blocked by the non-substitution rule, and an emergency exception has a named authority.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-013`
- `WISLIM-061`

## Tracking

This record is mirrored to GitHub issue #45.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
