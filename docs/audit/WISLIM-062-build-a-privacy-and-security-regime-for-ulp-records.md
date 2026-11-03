---
id: WISLIM-062
source_id: WS07
kind: workstream
title: "Build a privacy and security regime for ULP records"
severity: high
workstream: security
labels: [audit, workstream, severity:high, workstream:security]
source_lines: "n/a (workstream)"
quote_line: 2226
audit_modules: [audit/09-governance-and-oversight.md, red-team/threat-model.md]
related: [WISLIM-019, WISLIM-038, WISLIM-043, WISLIM-048, WISLIM-053]
github_issue: 62
---

# WISLIM-062: Build a privacy and security regime for ULP records

> **Severity:** high · **Kind:** workstream · **Source:** `WS07`  
> **GitHub issue:** [#62](https://github.com/docxology/WISLIM-audit/issues/62)  
> **Audit modules:** audit/09-governance-and-oversight.md, red-team/threat-model.md  
> **Source lines:** n/a (workstream)

## Quoted passage

> High-impact decisions must include a standardized record:
>
> — `source/WISLIM-v2.0.1.txt:2226`

Privacy is listed as a threat, but the ULP specification gives no retention, access-control, or key-management design.

## Summary

ULP records contain sensitive data, are processed by LLMs, and rely on signatures. The framework has no privacy regime, key management, or injection defense.

## Evidence

- **Failure modes covered:** F24, F25, F27
- **Claims covered:** C19
- **Scenarios covered:** AS03, AS08, AS13, AS18
- **Audit modules:** audit/09-governance-and-oversight.md, red-team/threat-model.md

## Why it matters

A verification system that leaks, forges, or misreads records is worse than no system: it creates false assurance.

## Required repair

1. Minimize data and set retention limits.
2. Encrypt records and enforce access control.
3. Use key management and multi-party signatures.
4. Use structured fields and treat free text as untrusted.
5. Run penetration tests and incident-response exercises.

## Acceptance criteria

- [ ] A data protection impact assessment and threat model exist.
- [ ] Key rotation and signature audit are implemented.
- [ ] Prompt-injection tests are part of the release gate.
- [ ] An incident-response exercise is completed.

## Related issues

- `WISLIM-019`
- `WISLIM-038`
- `WISLIM-043`
- `WISLIM-048`
- `WISLIM-053`

## Tracking

This record is mirrored to GitHub issue #62.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
