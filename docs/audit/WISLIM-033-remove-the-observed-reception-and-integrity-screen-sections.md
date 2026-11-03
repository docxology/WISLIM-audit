---
id: WISLIM-033
source_id: C33
kind: claim
title: "Remove the observed-reception and integrity-screen sections"
severity: critical
workstream: rhetoric
labels: [audit, claim, severity:critical, workstream:rhetoric]
source_lines: "364"
quote_line: 364
audit_modules: [audit/10-rhetoric-and-coercion.md]
related: [WISLIM-015, WISLIM-016, WISLIM-024]
github_issue: 33
---

# WISLIM-033: Remove the observed-reception and integrity-screen sections

> **Severity:** critical · **Kind:** claim · **Source:** `C33`  
> **GitHub issue:** [#33](https://github.com/docxology/WISLIM-audit/issues/33)  
> **Audit modules:** audit/10-rhetoric-and-coercion.md  
> **Source lines:** 364

## Quoted passage

> Because life is treated here as the supreme decision constraint, a person or organization’s trustworthiness in life-affecting roles can be screened by how they respond when asked to affirm (or rebut) that constraint.
>
> — `source/WISLIM-v2.0.1.txt:364`

The paper presents the screen as a practical application and the reception section as evidence; neither is examined ethically.

## Summary

The observed-reception and integrity-screen sections are ethically appropriate. Verdict: `harmful`. The sections pathologize non-response and propose a loyalty test for life-affecting roles. This can discriminate against dissenters, vulnerable people, and people with disabilities, and it violates autonomy and epistemic humility.

## Evidence

- **Claim:** The observed-reception and integrity-screen sections are ethically appropriate.
- **Anchor:** "Integrity Screen for Trust in Life-Affecting Roles"
- **Source:** `source/WISLIM-v2.0.1.txt:364`
- **Verdict:** `harmful`; severity `critical`.
- **Audit:** `audit/10-rhetoric-and-coercion.md`

## Why it matters

The integrity screen is presented as an ethical practice. If it is coercive and unfalsifiable, it contradicts the framework's own no-coercion rule.

## Steelman and reply

The reply is that the screen protects vulnerable people from those who would harm them. A screen that cannot distinguish dissent from evasion, and that punishes both, does not protect the vulnerable; it protects the framework.

## Required repair

1. Remove; replace with a voluntary, confidential survey and independent ethics review.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C33` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/10-rhetoric-and-coercion.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C33` is updated from `harmful` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-015`
- `WISLIM-016`
- `WISLIM-024`

## Tracking

This record is mirrored to GitHub issue #33.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
