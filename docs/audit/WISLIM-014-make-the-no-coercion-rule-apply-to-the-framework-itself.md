---
id: WISLIM-014
source_id: C14
kind: claim
title: "Make the no-coercion rule apply to the framework itself"
severity: high
workstream: rhetoric
labels: [audit, claim, severity:high, workstream:rhetoric]
source_lines: "238"
quote_line: 238
audit_modules: [audit/10-rhetoric-and-coercion.md, audit/06-agency-and-life.md]
related: [WISLIM-010, WISLIM-016, WISLIM-024]
github_issue: 14
---

# WISLIM-014: Make the no-coercion rule apply to the framework itself

> **Severity:** high · **Kind:** claim · **Source:** `C14`  
> **GitHub issue:** [#14](https://github.com/docxology/WISLIM-audit/issues/14)  
> **Audit modules:** audit/10-rhetoric-and-coercion.md, audit/06-agency-and-life.md  
> **Source lines:** 238

## Quoted passage

> Actions that affect life must maintain epistemic transparency — no manipulation or misrepresentation.
>
> — `source/WISLIM-v2.0.1.txt:238`

## Summary

Actions affecting life must maintain epistemic transparency and avoid coercion. Verdict: `self-undermining`. The paper's own rhetoric — 'silence equals betrayal,' the integrity screen, 'unsafe by definition' — is coercive. The rule is also too broad: privacy, confidentiality, and justified non-disclosure are normal in medicine and security.

## Evidence

- **Claim:** Actions affecting life must maintain epistemic transparency and avoid coercion.
- **Anchor:** "Actions that affect life must maintain epistemic transparency"
- **Source:** `source/WISLIM-v2.0.1.txt:238`
- **Verdict:** `self-undermining`; severity `high`.
- **Audit:** `audit/10-rhetoric-and-coercion.md`

## Why it matters

Transparency and non-coercion are the framework's own conditions. Applying them only to agents and not to the framework is a consistency failure.

## Steelman and reply

The reply is that the framework is a theory, so transparency applies only to actions it governs. A theory that tells agents to avoid coercion while using coercive rhetoric and a loyalty screen has not applied its own condition.

## Required repair

1. Specify minimal, proportionate, rights-respecting communication and exceptions for privacy and security.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C14` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/10-rhetoric-and-coercion.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C14` is updated from `self-undermining` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-010`
- `WISLIM-016`
- `WISLIM-024`

## Tracking

This record is mirrored to GitHub issue #14.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
