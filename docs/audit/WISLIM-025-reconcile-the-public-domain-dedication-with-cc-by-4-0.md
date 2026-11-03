---
id: WISLIM-025
source_id: C25
kind: claim
title: "Reconcile the public-domain dedication with CC-BY 4.0"
severity: medium
workstream: publication
labels: [audit, claim, severity:medium, workstream:publication]
source_lines: "13255"
quote_line: 13255
audit_modules: [evidence/provenance.md, LICENSE]
related: [WISLIM-026]
github_issue: 25
---

# WISLIM-025: Reconcile the public-domain dedication with CC-BY 4.0

> **Severity:** medium · **Kind:** claim · **Source:** `C25`  
> **GitHub issue:** [#25](https://github.com/docxology/WISLIM-audit/issues/25)  
> **Audit modules:** evidence/provenance.md, LICENSE  
> **Source lines:** 13255

## Quoted passage

> “I dedicate this work to the public domain.”
>
> — `source/WISLIM-v2.0.1.txt:13255`

PubPub displays CC-BY 4.0; the dedication is the only license statement in the PDF.

## Summary

The work is public domain. Verdict: `ambiguous`. The PubPub page uses CC-BY 4.0. The PDF says public domain. These are different legal instruments. The PDF has no license page. Reuse terms are unclear.

## Evidence

- **Claim:** The work is public domain.
- **Anchor:** "I dedicate this work to the public domain."
- **Source:** `source/WISLIM-v2.0.1.txt:13255`
- **Verdict:** `ambiguous`; severity `medium`.
- **Audit:** `evidence/provenance.md`

## Why it matters

The public-domain dedication conflicts with the CC-BY notice on PubPub. Users cannot tell what they may reuse.

## Steelman and reply

The reply is that the dedication and CC-BY are compatible because CC-BY is a license and public domain is a waiver. They are not compatible as stated: CC-BY requires attribution, and a public-domain dedication purports to waive it.

## Required repair

1. Clarify the license with the author and preserve attribution.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C25` or removes the claim from the thesis.
- [ ] The repair is documented in `evidence/provenance.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C25` is updated from `ambiguous` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-026`

## Tracking

This record is mirrored to GitHub issue #25.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
