---
id: WISLIM-042
source_id: AS07
kind: red-team
title: "Prevent vendor capture of the FLVS"
severity: high
workstream: governance
labels: [audit, red-team, severity:high, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_line: 2188
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-030, WISLIM-059]
github_issue: 42
---

# WISLIM-042: Prevent vendor capture of the FLVS

> **Severity:** high · **Kind:** red-team · **Source:** `AS07`  
> **GitHub issue:** [#42](https://github.com/docxology/WISLIM-audit/issues/42)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Verifier capture: Bribery, coercion, collusion, regulatory capture
>
> — `source/WISLIM-v2.0.1.txt:2188`

The paper lists verifier capture as a threat but does not separate the certifier from the vendors it regulates.

## Summary

Certification depends on a body whose staff, standards, and tests can be shaped by the vendors it regulates. A vendor can place former employees in verification roles and set standards that its own models meet more easily, turning the FLVS into a barrier to entry.

## Evidence

- **Actor:** A large AI vendor.
- **Preconditions:** The vendor supplies models, funds research, and rotates staff into the FLVS.
- **Attack path:** The vendor places former employees in key verification roles. The FLVS adopts standards that favor the vendor's models. Competing models are slower or more expensive to certify.
- **Impact:** Regulatory capture; barriers to entry; the framework becomes a moat.
- **Detection:** Track revolving doors; disclose funding; require cooling-off periods.
- **Mitigation:** Independent funding; conflict-of-interest rules; transparent standards; multiple vendors.
- **Residual risk:** Capture is gradual and hard to detect. High.

## Why it matters

A certifier that depends on the regulated vendors for staff, revenue, and standards has an incentive to certify the incumbents and exclude entrants.

## Required repair

1. Independent funding
2. Conflict-of-interest rules
3. Transparent standards
4. Multiple vendors.

## Acceptance criteria

- [ ] The certifier's staff, funding, and standards are independent of vendors, and a blinded certification test shows no incumbent advantage.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-030`
- `WISLIM-059`

## Tracking

This record is mirrored to GitHub issue #42.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
