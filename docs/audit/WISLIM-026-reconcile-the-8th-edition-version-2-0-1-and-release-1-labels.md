---
id: WISLIM-026
source_id: C26
kind: claim
title: "Reconcile the 8th edition, Version 2.0.1, and Release #1 labels"
severity: medium
workstream: publication
labels: [audit, claim, severity:medium, workstream:publication]
source_lines: "25"
quote_line: 25
audit_modules: [evidence/provenance.md, evidence/philpapers.md]
related: [WISLIM-025]
github_issue: 26
---

# WISLIM-026: Reconcile the 8th edition, Version 2.0.1, and Release #1 labels

> **Severity:** medium · **Kind:** claim · **Source:** `C26`  
> **GitHub issue:** [#26](https://github.com/docxology/WISLIM-audit/issues/26)  
> **Audit modules:** evidence/provenance.md, evidence/philpapers.md  
> **Source lines:** 25

## Quoted passage

> February 04, 2026, Version 2.0.1
>
> — `source/WISLIM-v2.0.1.txt:25`

The '8th edition' and 'Release #1' labels come from the PubPub record, not the PDF; see evidence/philpapers.md.

## Summary

The paper is an 8th edition published by Knowledge Futures Group / PubPub. Verdict: `inconsistent`. PhilPapers says '8th edition'; the PDF says Version 2.0.1; PubPub says Release #1. The labels are not reconciled. PubPub is a publishing platform, not a peer-reviewed journal.

## Evidence

- **Claim:** The paper is an 8th edition published by Knowledge Futures Group / PubPub.
- **Anchor:** "February 04, 2026, Version 2.0.1"
- **Source:** `source/WISLIM-v2.0.1.txt:25`
- **Verdict:** `inconsistent`; severity `medium`.
- **Audit:** `evidence/provenance.md`

## Why it matters

Three different labels (8th edition, Version 2.0.1, Release #1) circulate for one document. Citation and version control are therefore unreliable.

## Steelman and reply

The reply is that 8th edition, Version 2.0.1, and Release #1 describe different things. They are used interchangeably for the same document, and no mapping is given, so a citation cannot identify its object.

## Required repair

1. Add a version history and a clear publication-status statement.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C26` or removes the claim from the thesis.
- [ ] The repair is documented in `evidence/provenance.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C26` is updated from `inconsistent` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-025`

## Tracking

This record is mirrored to GitHub issue #26.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
