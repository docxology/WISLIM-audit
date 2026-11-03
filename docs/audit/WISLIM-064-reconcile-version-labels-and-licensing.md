---
id: WISLIM-064
source_id: WS09
kind: workstream
title: "Reconcile version labels and licensing"
severity: high
workstream: publication
labels: [audit, workstream, severity:high, workstream:publication]
source_lines: "n/a (workstream)"
quote_line: 13249
audit_modules: [evidence/provenance.md, evidence/philpapers.md]
related: [WISLIM-025, WISLIM-026]
github_issue: 64
---

# WISLIM-064: Reconcile version labels and licensing

> **Severity:** high · **Kind:** workstream · **Source:** `WS09`  
> **GitHub issue:** [#64](https://github.com/docxology/WISLIM-audit/issues/64)  
> **Audit modules:** evidence/provenance.md, evidence/philpapers.md  
> **Source lines:** n/a (workstream)

## Quoted passage

> Date: September 1, 2025 (updated Febuary 4, 2026 to Version 2.0.1)
>
> — `source/WISLIM-v2.0.1.txt:13249`

The '8th edition' and 'Release #1' labels come from the PubPub record, not the PDF.

## Summary

The paper is labeled 8th edition, Version 2.0.1, and Release #1. PubPub says CC-BY 4.0; the PDF says public domain. Readers cannot tell what they are citing or what they may reuse.

## Evidence

- **Failure modes covered:** F36, F37, F40
- **Claims covered:** C25, C26
- **Scenarios covered:** none
- **Audit modules:** evidence/provenance.md, evidence/philpapers.md

## Why it matters

Version and license ambiguity undermines citability and reuse. It also creates legal risk for anyone who redistributes the work.

## Required repair

1. Publish one authoritative version with a changelog.
2. Reconcile the edition and release labels.
3. Clarify the license in writing.
4. Add a citation record and DOI metadata.
5. Submit to peer review or state that the work is not peer reviewed.

## Acceptance criteria

- [ ] One version record exists.
- [ ] The author provides a license statement.
- [ ] Citation and repository metadata are updated.
- [ ] Peer-review status is explicit.

## Related issues

- `WISLIM-025`
- `WISLIM-026`

## Tracking

This record is mirrored to GitHub issue #64.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
