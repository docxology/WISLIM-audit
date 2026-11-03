---
id: WISLIM-053
source_id: AS18
kind: red-team
title: "Prevent privacy leaks from ULP records"
severity: high
workstream: security
labels: [audit, red-team, severity:high, workstream:security]
source_lines: "n/a (red-team scenario)"
quote_line: 2190
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-019, WISLIM-062]
github_issue: 53
---

# WISLIM-053: Prevent privacy leaks from ULP records

> **Severity:** high · **Kind:** red-team · **Source:** `AS18`  
> **GitHub issue:** [#53](https://github.com/docxology/WISLIM-audit/issues/53)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Privacy attacks: Forcing disclosure via audit requirements
>
> — `source/WISLIM-v2.0.1.txt:2190`

Privacy is listed as an attack to guard against, but no retention or access-control design follows.

## Summary

ULP records hold sensitive personal and organizational data, are processed by third-party models, and have no specified access-control or retention regime. Exfiltration or weak access controls can publish or sell the data, producing privacy harm, discrimination, and chilling effects.

## Evidence

- **Actor:** An attacker or insider.
- **Preconditions:** ULP records contain personal data about affected people.
- **Attack path:** The attacker exfiltrates records or exploits weak access controls. Sensitive information is published or sold.
- **Impact:** Privacy harm; discrimination; chilling effects.
- **Detection:** Access logs; anomaly detection; penetration testing.
- **Mitigation:** Data minimization; encryption; retention limits; privacy impact assessment.
- **Residual risk:** Any centralized record system is a target. High.

## Why it matters

The framework creates a central store of sensitive records and supplies no privacy or security design. A breach would harm the people the framework claims to protect.

## Required repair

1. Data minimization
2. Encryption
3. Retention limits
4. Privacy impact assessment.

## Acceptance criteria

- [ ] A privacy impact assessment and access-control test show that ULP records cannot be exfiltrated or repurposed, and retention is bounded.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-019`
- `WISLIM-062`

## Tracking

This record is mirrored to GitHub issue #53.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
