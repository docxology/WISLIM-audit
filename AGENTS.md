# WISLIM-audit — repository rules

This repository is a critical audit, not an endorsement. Keep the audit
source-bound and reproducible.

1. **The source is immutable.** Do not edit anything in `source/`. If a new
   edition is added, put it beside the old one and update `source/metadata.json`.
2. **Cite the source.** Every substantive claim about the paper must cite a
   section name or a line in `source/WISLIM-v2.0.1.txt` (for example,
   `source/WISLIM-v2.0.1.txt:778`). Do not launder an inference as a quote.
3. **Preserve claim IDs.** `C01`–`C35` in `model/claims.json` and `ST001`–`ST210`
   in `model/stress-tests.json` are stable. Add new IDs; never renumber.
4. **Separate quotation from verdict.** Quoted source text may contain
   overclaiming language. The audit's own prose must not repeat it as fact.
5. **Distinguish the author's intent from the argument's validity.** Critique
   arguments, definitions, evidence, and institutions, not the author's
   character or motives.
6. **Do not publish the source paper.** This repository is private. The source
   license is ambiguous (CC-BY 4.0 on PubPub; a public-domain dedication in the
   PDF). Do not relicense or redistribute the PDF without clarification.
7. **Validate before committing.** Run `python3 tools/validate.py` and
   `python3 -m pytest -q`. Fix failures rather than suppressing them.
8. **No new dependencies for the validator.** The audit must remain runnable
   with a stock Python 3.11+ interpreter.
9. **High-risk topics need care.** The paper's suicide, medical-triage, and
   integrity-screen examples are not implementation guidance. Flag them as
   requiring clinical, legal, and ethical review.
10. **Keep the tone precise.** No ridicule, no ad hominem, no invented facts.
    Where the evidence is unavailable, say so.
