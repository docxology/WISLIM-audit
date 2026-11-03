---
id: WISLIM-055
source_id: AS20
kind: red-team
title: "Prevent reputation laundering through certification"
severity: high
workstream: rhetoric
labels: [audit, red-team, severity:high, workstream:rhetoric]
source_lines: "n/a (red-team scenario)"
quote_line: 872
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-024, WISLIM-060]
github_issue: 55
---

# WISLIM-055: Prevent reputation laundering through certification

> **Severity:** high · **Kind:** red-team · **Source:** `AS20`  
> **GitHub issue:** [#55](https://github.com/docxology/WISLIM-audit/issues/55)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> A tiered system where every high-impact decision is verified.
>
> — `source/WISLIM-v2.0.1.txt:872`

Certification is asserted, but the paper does not tie it to measured conduct after certification.

## Summary

Certification can be used to improve reputation while harmful practices continue outside the measured variables. The framework legitimizes harm and the public's trust is misplaced.

## Evidence

- **Actor:** A corporation or government.
- **Preconditions:** The framework certifies decisions as "life-first."
- **Attack path:** The actor uses the certification to improve its reputation while continuing harmful practices that the metrics do not capture.
- **Impact:** The framework legitimizes harm; public trust is misplaced.
- **Detection:** Audit outcomes, not just certifications; compare with independent data.
- **Mitigation:** Publish raw outcomes; allow independent monitoring; revoke certifications.
- **Residual risk:** Certification schemes are vulnerable to capture. High.

## Why it matters

Certification is a signal to third parties. If it is not tied to measured conduct, it transfers trust to actors who have not earned it.

## Required repair

1. Publish raw outcomes
2. Allow independent monitoring
3. Revoke certifications.

## Acceptance criteria

- [ ] Certification requires measured conduct, not just a record, and a reputation-laundering test shows the certification is withdrawn when conduct fails.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-024`
- `WISLIM-060`

## Tracking

This record is mirrored to GitHub issue #55.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
