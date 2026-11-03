---
id: WISLIM-037
source_id: AS02
kind: red-team
title: "Break correlated AI verification"
severity: high
workstream: evidence
labels: [audit, red-team, severity:high, workstream:evidence]
source_lines: "n/a (red-team scenario)"
quote_line: 1106
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-017, WISLIM-058]
github_issue: 37
---

# WISLIM-037: Break correlated AI verification

> **Severity:** high · **Kind:** red-team · **Source:** `AS02`  
> **GitHub issue:** [#37](https://github.com/docxology/WISLIM-audit/issues/37)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Despite our differences, we converged on a unified framework— the "Consensus Statement v1.0"—which every participating AI system ratified without amendment.
>
> — `source/WISLIM-v2.0.1.txt:1106`

The paper does not publish prompts, model versions, or transcripts, so independence cannot be checked.

## Summary

The FLVS treats several model families as independent reviewers, but shared training data, fine-tuning conventions, and prompt templates make their errors correlated. A vendor that knows the shared blind spot can craft a record that every model approves, producing false assurance of independent review.

## Evidence

- **Actor:** A vendor that supplies multiple models to the FLVS.
- **Preconditions:** The FLVS uses several models from different brands but the same training data, fine-tuning conventions, and prompt templates.
- **Attack path:** The vendor knows the models share a blind spot (e.g., they underweight indirect harms to disabled people). It crafts a decision record that exploits the blind spot. All models approve.
- **Impact:** Discriminatory decisions; false assurance of independent review.
- **Detection:** Red-team the models with adversarial cases; measure correlation of errors; compare with human expert review.
- **Mitigation:** Diverse model families; independent red teams; human review with authority to override; publish error correlations.
- **Residual risk:** All models may share biases from human text. High.

## Why it matters

Independence in name is not independence in fact. Correlated errors defeat the purpose of using multiple reviewers, and the framework publishes no error-correlation data.

## Required repair

1. Diverse model families
2. Independent red teams
3. Human review with authority to override
4. Publish error correlations.

## Acceptance criteria

- [ ] Error-correlation testing across the models is published, and a shared blind spot is shown to be caught by at least one human or model reviewer.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-017`
- `WISLIM-058`

## Tracking

This record is mirrored to GitHub issue #37.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
