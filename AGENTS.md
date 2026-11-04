# WISLIM-audit — repository rules

This repository is a critical audit, not an endorsement. Keep the audit
source-bound and reproducible.

1. **The source is immutable.** Do not edit anything in `source/`. If a new
   edition is added, put it beside the old one and update `source/metadata.json`.
2. **Cite the source.** Every substantive claim about the paper must cite a
   section name or a line in `source/WISLIM-v2.0.1.txt` (for example,
   `source/WISLIM-v2.0.1.txt:778`). Do not launder an inference as a quote.
3. **Preserve claim and issue IDs.** `C01`–`C35` in `model/claims.json`,
   `ST001`–`ST210` in `model/stress-tests.json`, `WISLIM-001`–`WISLIM-066` in
   `model/issues.json`, `OPH-REV-001`–`OPH-REV-012` in
   `reviews/oph-lfdi-57/model/review.json`, and `OPH-REP-001`–`OPH-REP-016` and
   `OPH-AUD-001`–`OPH-AUD-011` in `reviews/oph-lfdi-57/model/reply.json` are stable.
   Add new IDs; never renumber or reuse one.
4. **Separate quotation from verdict.** Quoted source text may contain
   overclaiming language. The audit's own prose must not repeat it as fact.
   Every issue record carries one or more verbatim `quotes[]` entries, each with
   a `line`; every quotation must appear in the source at that line, and the
   validator checks it.
5. **Distinguish the author's intent from the argument's validity.** Criticize
   arguments, evidence, and institutions, not the author's character or motives.
6. **Keep the issue and review registers in sync.** Edit `docs/audit/*.md` only
   through `model/issues.json` and `make register`. Edit
   `reviews/oph-lfdi-57/topics/*.md`, `docs/reviews/oph-lfdi-57/topics/*.md`,
   and `docs/reviews.md` only through `reviews/oph-lfdi-57/model/review.json`
   and `make review`. Edit `reviews/oph-lfdi-57/reply/`,
   `reviews/oph-lfdi-57/corrections.md`, and the correspondence ledger only through
   `reviews/oph-lfdi-57/model/reply.json`, `correspondence/metadata.json`, and
   `make reply`, then `make reply-issues`. Then run `make issues` to refresh the 66 GitHub issues. Do
   not edit issue bodies on GitHub: the canonical record is the repository file,
   and comments are for discussion.
7. **Do not relicense the source paper.** The source license is ambiguous
   (CC-BY 4.0 on PubPub; a public-domain dedication in the PDF). Keep the source
   PDF and received review under their own terms without relicensing them.
8. **Validate before committing.** Run `make verify`. It runs the validator,
   the register check, and the test suite. Use `python3 -m pytest -q` only if
   pytest is installed; it is optional and not required by the repository.
9. **No new dependencies for the validator.** The audit must remain runnable
   with a stock Python 3.11+ interpreter. `gh` is required only for the
   GitHub mirror, not for local validation.
10. **High-risk topics need care.** The paper's suicide, medical-triage, and
    integrity-screen examples are not implementation guidance. Flag them as
    requiring clinical, legal, and ethical review.
11. **Keep the tone precise.** No ridicule, no ad hominem, no invented facts.
    Where the evidence is unavailable, say so.
12. **Cite what the source prints, at its current home.** Compare any OCR with the
    page image before citing it; keep raw OCR as a record and cite the verified
    transcription. Pin third-party evidence to the upstream repository, not a fork,
    and read each quotation in its passage before relying on it. `make verify-oph`
    checks the words; only reading checks the sense. A quotation mark means the
    words are verbatim; put paraphrase outside quotation marks.
13. **Keep private details out of public records.** Correspondence records carry no
    telephone numbers, email addresses, recipient lists, or mail-service identifiers.
    Quote what the exchange needs, say where something was removed, and let the
    validator's general check reject the class.
14. **Do not treat audit issues as fatal or mandatory.** Each issue carries
    `status: observation` and a note saying it may matter for impact, clarity,
    or risk. Severity is an impact estimate, not a fatality rating, and the
    author may decline a proposed response with reasons. Keep that framing in
    records and mirrors.
