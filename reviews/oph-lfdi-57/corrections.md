# Corrections to the OPH/LFDI tracker

Errors found in this tracker, what changed, and whether the email of 2026-11-03
carried them. The IDs are stable. The email stays as sent; see
[`response-email.md`](response-email.md).

| ID | Issue | Correction | In the sent email |
|---|---|---|---|
| [OPH-AUD-001](#oph-aud-001-ocr-errors-were-read-as-the-review-s-text) | [#83](https://github.com/docxology/WISLIM-audit/issues/83) | OCR errors were read as the review's text | yes |
| [OPH-AUD-002](#oph-aud-002-oph-evidence-was-pinned-to-a-stale-fork-not-upstream) | [#84](https://github.com/docxology/WISLIM-audit/issues/84) | OPH evidence was pinned to a stale fork, not upstream | yes |
| [OPH-AUD-003](#oph-aud-003-explicitly-separates-physics-from-ethics-overstated-oph) | [#85](https://github.com/docxology/WISLIM-audit/issues/85) | 'Explicitly separates physics from ethics' overstated OPH | yes |
| [OPH-AUD-004](#oph-aud-004-the-status-label-refuted-overclaimed) | [#86](https://github.com/docxology/WISLIM-audit/issues/86) | The status label 'refuted' overclaimed | no |
| [OPH-AUD-005](#oph-aud-005-symbols-and-tiers-wislim-glosses-were-called-undefined) | [#87](https://github.com/docxology/WISLIM-audit/issues/87) | Symbols and tiers WISLIM glosses were called undefined | no |
| [OPH-AUD-006](#oph-aud-006-paraphrase-and-altered-words-stood-inside-quotation-marks) | [#88](https://github.com/docxology/WISLIM-audit/issues/88) | Paraphrase and altered words stood inside quotation marks | no |
| [OPH-AUD-007](#oph-aud-007-the-tracker-still-said-no-response-had-been-sent) | [#89](https://github.com/docxology/WISLIM-audit/issues/89) | The tracker still said no response had been sent | no |
| [OPH-AUD-008](#oph-aud-008-the-reply-of-2026-11-03-was-not-tracked) | [#90](https://github.com/docxology/WISLIM-audit/issues/90) | The reply of 2026-11-03 was not tracked | no |
| [OPH-AUD-009](#oph-aud-009-the-oph-quotation-check-was-a-one-off-not-a-repeatable-test) | [#91](https://github.com/docxology/WISLIM-audit/issues/91) | The OPH quotation check was a one-off, not a repeatable test | no |
| [OPH-AUD-010](#oph-aud-010-correspondence-records-needed-a-privacy-rule) | [#92](https://github.com/docxology/WISLIM-audit/issues/92) | Correspondence records needed a privacy rule | no |
| [OPH-AUD-011](#oph-aud-011-the-audit-missed-the-formal-and-engineering-versions-of-wislim-s-formula) | [#93](https://github.com/docxology/WISLIM-audit/issues/93) | The audit missed the formal and engineering versions of WISLIM's formula | no |
| [OPH-AUD-012](#oph-aud-012-the-pin-fell-behind-upstream-s-release-r2061) | [#94](https://github.com/docxology/WISLIM-audit/issues/94) | The pin fell behind upstream's release r2061 | no |
| [OPH-AUD-013](#oph-aud-013-a-receipt-and-several-records-overstated-or-assumed-details) | [#95](https://github.com/docxology/WISLIM-audit/issues/95) | A receipt and several records overstated or assumed details | no |

## OPH-AUD-001: OCR errors were read as the review's text

**Affects the email sent 2026-11-03:** Yes.

**What was wrong.** The review PDF is one page image, and the tracker cited Tesseract OCR. OCR turned `$D$` into `SDS`, `$U$` into `SUS`, `$L_1$` into `SL_1$`, `E∞` into `Eoo`, `×` into `x`, and `AI` into `Al`. The audit then treated those errors as the review's own: F4 called the equation malformed, F6 charged a shifting acronym, and OPH-REV-007, OPH-REV-009, and OPH-REV-010 listed 'SL1', 'SDS', and 'SUS' as undefined. The sent email quoted 'Decision Entropy (SDS)' and called the tracker's quotations verified. The receipt reproduced the OCR and never compared it with the page.

**What changed.** Added `LFDI_Alignment_Audit-57.verified.txt`, compared line by line with the page image, and kept the OCR file unchanged. A test derives the verified text from the OCR by a literal substitution list, so no other difference can enter. Every review quotation now cites the verified text, and the findings are rewritten. One finding survives on better ground: the symbol $D$ really does shift, from 'delay, distortion, or destruction' to 'ethical entropy', 'severe epistemic distortion', and 'Decision Entropy'.

**Files.** `reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.verified.txt`, `reviews/oph-lfdi-57/source/metadata.json`, `reviews/oph-lfdi-57/intrinsic-audit.md`, `reviews/oph-lfdi-57/verification.md`

**Fixed in.** `701b463`

## OPH-AUD-002: OPH evidence was pinned to a stale fork, not upstream

**Affects the email sent 2026-11-03:** Yes.

**What was wrong.** The tracker pinned `docxology/observer-patch-holography` at `1c5a908`, a fork 7 commits ahead of and 1,593 behind upstream `main`. Of its 15 distinct OPH quotations, 11 no longer appear verbatim at upstream. Three errors followed. OPH-REV-001 said the review's title was not the flagship's; at upstream, at release r2060, it was exactly the flagship's title. The sent email quoted 'a condition on one structure that holds or fails with nothing running it', which upstream had rewritten on 2026-10-11. The intrinsic audit said the review 'cites no OPH passage' and does not mention fixed points, though it quotes the abstract accurately and does mention them.

**What changed.** Re-pinned all evidence to `FloatingPragma/observer-patch-holography` at `fcc2dd1` (paper release r2060) and re-read every passage. OPH-REV-001 and the intrinsic grade now credit the review's accurate citation and quotations: its title was the flagship's title at that release. OPH-REV-006 moved from contradicted to addressed, because OPH's fixed point does contain its observers; the counts are now 4 addressed, 3 contradicted, 5 not addressed.

**Files.** `reviews/oph-lfdi-57/model/review.json`, `reviews/oph-lfdi-57/extrinsic-audit.md`, `reviews/oph-lfdi-57/intrinsic-audit.md`, `reviews/oph-lfdi-57/source/metadata.json`

**Fixed in.** `701b463`

## OPH-AUD-003: 'Explicitly separates physics from ethics' overstated OPH

**Affects the email sent 2026-11-03:** Yes.

**What was wrong.** OPH-REV-008 said OPH 'explicitly separates physics from ethics', and E4 said it separates the physical reconstruction 'from any ethical layer'. The sent email said OPH 'keeps its physics separable from ethics'. All three quoted 'the physics can be taken alone and nothing above it breaks' and dropped its neighbors: 'They share a quantity' and 'Accepting the repair law is accepting both'. The words were verified. Their sense was not.

**What changed.** OPH-REV-008 and E4 now quote the whole passage and say what it says: a reader can take the physics without the ethics, and the two are not unrelated. AGENTS.md now requires reading each quotation in its passage, because a substring check cannot catch this.

**Files.** `reviews/oph-lfdi-57/model/review.json`, `reviews/oph-lfdi-57/extrinsic-audit.md`, `AGENTS.md`

**Fixed in.** `701b463`

## OPH-AUD-004: The status label 'refuted' overclaimed

**Affects the email sent 2026-11-03:** No.

**What was wrong.** Four topics carried `refuted`, and the indexes read 'Refuted by OPH'. The label's own definition was 'OPH's stated position contradicts the review's claim'. A sentence in OPH that contradicts a claim does not refute it. The sent email already used the accurate word, 'contradicted'; the repository did not.

**What changed.** Renamed the status to `contradicted` in the model, the builder, the validator, the indexes, and the audits, and its definition now says a contradiction is not by itself a refutation.

**Files.** `scripts/build_review_register.py`, `reviews/oph-lfdi-57/model/review.json`, `tools/validate.py`, `docs/method.md`

**Fixed in.** `701b463`

## OPH-AUD-005: Symbols and tiers WISLIM glosses were called undefined

**Affects the email sent 2026-11-03:** No.

**What was wrong.** The intrinsic grade said 'LFDI variables, Tier 2/3' are undefined, and OPH-REV-007 said the variables and formula are undefined. WISLIM v2.0.1 glosses $L_1$, $U$, and $D$, describes three tiers, and specifies the LFDI. The sent email's narrower wording, that the review does not define or defend them, remains accurate of the review.

**What changed.** The findings now say what is accurate: the review does not define them; WISLIM glosses them in words with no units or estimator; and the review and reply use them differently from WISLIM (table at F4 of the intrinsic audit). They also record the terms that do not occur in WISLIM v2.0.1 at all: 'Engineering Proof', 'Airtight', 'Epistemic Invariant', 'No Truth Outside', 'Decision Entropy', and 'Performative'.

**Files.** `reviews/oph-lfdi-57/intrinsic-audit.md`, `reviews/oph-lfdi-57/model/review.json`, `reviews/oph-lfdi-57/verification.md`

**Fixed in.** `701b463`

## OPH-AUD-006: Paraphrase and altered words stood inside quotation marks

**Affects the email sent 2026-11-03:** No.

**What was wrong.** F5 put 'OPH must immediately integrate the LFDI protocol' in quotation marks with a line citation; the page has no such sentence. E3 quoted 'fundamentally require', and the page says 'requires'. E2 quoted WISLIM as 'any system capable of making decisions', and the source says 'Any system that makes decisions'. A tracker that objects to unquoted attributions has to meet the same standard.

**What changed.** Corrected each case. The validator now requires every double-quoted string of four or more words in the two audits and the receipt to occur verbatim in the sources, the correspondence, or the recorded evidence.

**Files.** `reviews/oph-lfdi-57/intrinsic-audit.md`, `reviews/oph-lfdi-57/extrinsic-audit.md`, `tools/validate.py`

**Fixed in.** `701b463`

## OPH-AUD-007: The tracker still said no response had been sent

**Affects the email sent 2026-11-03:** No.

**What was wrong.** `review.json` said 'no response sent', the indexes said 'Not sent', and `response-email.md` said 'draft only'. The response went out on 2026-11-03. OPH-REV-011 also said there was 'no response from them'. The draft differed from what was sent.

**What changed.** Added a correspondence ledger and the as-sent text. `response-email.md` now records the sent email unchanged and lists what has since been corrected. The status fields and OPH-REV-011 are updated.

**Files.** `reviews/oph-lfdi-57/correspondence/README.md`, `reviews/oph-lfdi-57/correspondence/02-friedman-response-as-sent.txt`, `reviews/oph-lfdi-57/response-email.md`

**Fixed in.** `701b463`

## OPH-AUD-008: The reply of 2026-11-03 was not tracked

**Affects the email sent 2026-11-03:** No.

**What was wrong.** The response said 'we will record any response in the tracker'. The tracker had no place for a reply, no stable IDs for its claims, and no way to discuss them claim by claim.

**What changed.** Added the reply text, a canonical model, and one record and one GitHub issue per claim (`OPH-REP-001`–`OPH-REP-016`). The validator checks each quotation against its source. The index also records where the reply moves the exchange forward.

**Files.** `reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt`, `reviews/oph-lfdi-57/model/reply.json`, `reviews/oph-lfdi-57/reply/README.md`, `scripts/build_reply_register.py`, `scripts/sync_reply_issues.py`

**Fixed in.** `701b463`

## OPH-AUD-009: The OPH quotation check was a one-off, not a repeatable test

**Affects the email sent 2026-11-03:** No.

**What was wrong.** The receipt reported a quotation check that no script in the repository could rerun, so nothing would notice when a pin or an anchor went bad.

**What changed.** Added `scripts/verify_oph_quotes.py` and `make verify-oph`, and a continuous-integration job that checks every OPH quotation at the pinned upstream commit. The validator confirms that the receipt's count and the job's commit match the model.

**Files.** `scripts/verify_oph_quotes.py`, `Makefile`, `.github/workflows/verify.yml`, `tools/validate.py`, `reviews/oph-lfdi-57/verification.md`

**Fixed in.** `701b463`

## OPH-AUD-010: Correspondence records needed a privacy rule

**Affects the email sent 2026-11-03:** No.

**What was wrong.** This repository is public, and the thread carries a telephone number, email addresses, and a recipient list. Nothing kept those out of the records.

**What changed.** The recorded texts leave out contact details and recipient lists and say where they were removed. The validator rejects any email address or telephone number in the correspondence, reply, and correction records, and AGENTS.md states the rule.

**Files.** `reviews/oph-lfdi-57/correspondence/README.md`, `tools/validate.py`, `AGENTS.md`

**Fixed in.** `701b463`

## OPH-AUD-011: The audit missed the formal and engineering versions of WISLIM's formula

**Affects the email sent 2026-11-03:** No.

**What was wrong.** WISLIM's Appendix A gives its proof 'in three fashions'. Version 2 says 'L = 0 ⇔ no such system exists'. Version 3 says the formula 'is not meant to compute a number'. `audit/05-formula-e-infinity.md` and WISLIM-011 called the variables 'undefined' without weighing either, and this tracker missed both when it assessed the review's $L_1 = 0$. An independent pre-publication read caught it.

**What changed.** `audit/05-formula-e-infinity.md`, claim C11, and WISLIM-011 now say what is accurate: verbal glosses that differ across the versions, with no units or estimator. OPH-REV-007, F4 of the intrinsic audit, and OPH-REP-010 apply the formal definition to the review's step, where it is the strongest point against that step.

**Files.** `audit/05-formula-e-infinity.md`, `model/claims.json`, `model/issues.json`, `reviews/oph-lfdi-57/intrinsic-audit.md`, `reviews/oph-lfdi-57/model/review.json`

**Fixed in.** `701b463`

## OPH-AUD-012: The pin fell behind upstream's release r2061

**Affects the email sent 2026-11-03:** No.

**What was wrong.** The tracker pinned release r2060 and described that commit as upstream `main`. On 2026-11-04 upstream released r2061 with a new subtitle, a rewritten abstract, and a shorter flagship body. Against the new text, 50 of the 66 OPH quotations held at their lines, 4 had moved, and 12 no longer occurred in the flagship. Records said 'the flagship's title' and 'the abstract' without saying which release, one of them said 'incomplete' of wording r2061 no longer uses, and nothing reported the drift.

**What changed.** Re-pinned to `f50e4da` (release r2061) and re-read every flagship passage. Evidence about what the review read stays at `fcc2dd1` (release r2060) and is labeled; evidence about OPH's position cites r2061, in the passages that now carry the point. OPH-REV-001 says the review's title was exact on the day it was sent and that the subtitle changed the next day. OPH-REP-002's commit counts and OPH-REP-010's evidence now cite r2061. `make oph-drift` lists the quotations that have moved or vanished at any upstream ref. No disposition changed: the counts remain 4 addressed, 3 contradicted, 5 not addressed.

**Files.** `reviews/oph-lfdi-57/model/review.json`, `reviews/oph-lfdi-57/model/reply.json`, `reviews/oph-lfdi-57/source/metadata.json`, `reviews/oph-lfdi-57/extrinsic-audit.md`, `reviews/oph-lfdi-57/intrinsic-audit.md`, `reviews/oph-lfdi-57/verification.md`, `scripts/verify_oph_quotes.py`, `Makefile`, `.github/workflows/verify.yml`, `README.md`, `AGENTS.md`, `docs/method.md`, `docs/reproducibility.md`

**Fixed in.** `1dfcda5`

## OPH-AUD-013: A receipt and several records overstated or assumed details

**Affects the email sent 2026-11-03:** No.

**What was wrong.** The receipt said the word search for LFDI, WISLIM, and Wishengrad had 'no matches anywhere in the pinned tree'. As written, the command also reports two compressed binary data files, at both releases. OPH-REV-003 said 'living' does not occur in the flagship source; it occurs once, in the journal title 'Living Reviews in Relativity'. OPH-REP-004 stated its word search over the whole commit, and OPH-REP-007's phrase search covered only Markdown and TeX and did not allow for line wraps. OPH-REP-009 said 'You are running it' lands close to OPH's hypothesis, though the same passage says a run makes a model of the rule. OPH-REP-004 treated a quotation about the relational setting as stating a pluralism too. Three records called the sender 'his', though the sender's pronouns are not stated.

**What changed.** The receipt's command now skips binary files with `-I`, and the receipt says what the plain command returns and why. OPH-REV-003 names the journal title. OPH-REP-004 says 'text files'. OPH-REP-007's search covers every text file and allows for line wraps, and its result is unchanged. OPH-REP-009 separates a run of the model from the running of the world, and says what remains in dispute. OPH-REP-004 ties the quotation to the setting. The three records now say 'the sender'.

**Files.** `reviews/oph-lfdi-57/verification.md`, `reviews/oph-lfdi-57/model/review.json`, `reviews/oph-lfdi-57/model/reply.json`, `reviews/oph-lfdi-57/correspondence/metadata.json`, `reviews/oph-lfdi-57/response-email.md`

**Fixed in.** `1dfcda5`

`reviews/oph-lfdi-57/model/reply.json` is canonical; regenerate this file with `make reply`.
