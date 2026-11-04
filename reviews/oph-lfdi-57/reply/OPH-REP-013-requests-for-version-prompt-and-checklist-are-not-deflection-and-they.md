---
id: OPH-REP-013
review: OPH-LFDI-57
kind: reply-topic
status: observation
claim_kind: provenance
reply_lines: [30]
github_issue: 
related: [OPH-REP-003, OPH-REP-006, OPH-REP-012]
---

# OPH-REP-013: Requests for version, prompt, and checklist are not deflection, and they remain open

> **Status: audit observation, not a required fix.** This is a tracked note on one
> claim in a reply. It is not a verdict on anyone's character, and the sender may
> decline the suggested step with reasons. Comments on the matching issue are welcome.

## The reply says

> By dismissing the invariant as an ungranted premise and deflecting to requests for prompt versions and manuscript hashes, it rests in Option C.
>
> — [`reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt:30`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt#L30)

## Summary

The response asked for three things: the OPH manuscript version audited, the prompt and model version, and the verification checklist. It did not ask for hashes. None of the three has been supplied.

## Assessment

The response said: 'We would welcome the exact OPH manuscript version audited, the prompt and model version used, and the verification checklist behind "verified as correct"'. The only SHA-256 in it describes this repository's copy of WISLIM. These are ordinary requests for a document titled an audit that says it was 'verified as correct', and the version matters: the flagship changes release often, and this exchange has already turned on a sentence that changed.

WISLIM's Observed Reception section lists 'deflection to side-issues (tone, wording, politics)' as a recurring response, and the Integrity Screen treats 'substitution of side-issues' as disqualifying. Classifying a provenance request as deflection uses that rule to set the request aside.

The reply adds new text attributed to 'the bot', again without a model or prompt. Disclosing the help is good practice. The open requests are listed in the reply register's index.

**Kind of claim:** `provenance`: turns on a source, version, or verification that has not been supplied.

## Evidence

**The response as sent**

- [`02-friedman-response-as-sent.txt:13`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/02-friedman-response-as-sent.txt#L13)
  > We would welcome the exact OPH manuscript version audited, the prompt and model version used, and the verification checklist behind "verified as correct"

**Elsewhere in the reply**

- [`03-wishengrad-reply.txt:34`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt#L34)
  > The bot doesn't seem to think that we are describing the exact same thing

**The one-page review**

- [`LFDI_Alignment_Audit-57.verified.txt:6`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.verified.txt#L6)
  > AI Gemini Pro latest was used to generate this correction, and this correction has been verified as correct by David Wishengrad.

**WISLIM v2.0.1**

- [`source/WISLIM-v2.0.1.txt:344`](https://github.com/docxology/WISLIM-audit/blob/main/source/WISLIM-v2.0.1.txt#L344)
  > deflection to side-issues (tone, wording, politics)
- [`source/WISLIM-v2.0.1.txt:376`](https://github.com/docxology/WISLIM-audit/blob/main/source/WISLIM-v2.0.1.txt#L376)
  > substitution of side-issues

**Related audit records**

- [`WISLIM-018`](https://github.com/docxology/WISLIM-audit/blob/main/docs/audit/WISLIM-018-publish-the-prompts-and-ratification-record-or-withdraw-the-claim.md)
- [`WISLIM-015`](https://github.com/docxology/WISLIM-audit/blob/main/docs/audit/WISLIM-015-remove-silence-and-deflection-as-evidence.md)

## What would move this forward

Supply the release or date audited, the prompts and model versions for both documents, and the checklist.

## Related

- `OPH-REP-003`
- `OPH-REP-006`
- `OPH-REP-012`

## Tracking

This record is generated. The canonical source is
`reviews/oph-lfdi-57/model/reply.json`; regenerate with `make reply`.
