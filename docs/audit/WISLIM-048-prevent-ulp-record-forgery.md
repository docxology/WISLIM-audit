---
id: WISLIM-048
source_id: AS13
kind: red-team
title: "Prevent ULP record forgery"
severity: high
workstream: security
labels: [audit, red-team, severity:high, workstream:security]
source_lines: "n/a (red-team scenario)"
quote_line: 2204
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-019, WISLIM-062]
github_issue: 48
---

# WISLIM-048: Prevent ULP record forgery

> **Severity:** high · **Kind:** red-team · **Source:** `AS13`  
> **GitHub issue:** [#48](https://github.com/docxology/WISLIM-audit/issues/48)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Tamper-evident audit logs (append-only, signed artifacts)
>
> — `source/WISLIM-v2.0.1.txt:2204`

Signatures attest integrity, not the truth of the underlying verification.

## Summary

ULP records rely on signatures to establish that verification occurred. An actor who steals a signing key or exploits a weak scheme can forge a compliant record for a harmful decision, and accountability collapses.

## Evidence

- **Actor:** A decision-maker or insider.
- **Preconditions:** ULP records are signed with keys; key management is weak.
- **Attack path:** The actor steals a signing key or exploits a weak signature scheme. They create a record showing proper verification for a harmful decision.
- **Impact:** False assurance; accountability is undermined.
- **Detection:** Key rotation; hardware security modules; anomaly detection.
- **Mitigation:** Strong key management; multi-party signatures; transparency logs.
- **Residual risk:** Insider threats are hard to eliminate. High.

## Why it matters

Signatures establish integrity, not truth. If the key or the scheme fails, the record system certifies a decision that never happened as required.

## Required repair

1. Strong key management
2. Multi-party signatures
3. Transparency logs.

## Acceptance criteria

- [ ] A key-compromise and weak-signature test cannot produce a record that passes verification, and signing keys have rotation and revocation.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-019`
- `WISLIM-062`

## Tracking

This record is mirrored to GitHub issue #48.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
