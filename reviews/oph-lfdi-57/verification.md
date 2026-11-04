# Verification receipt for the OPH/LFDI review tracker

All checks below were run on 2026-11-03 against the pinned OPH commit
`fcc2dd173d4f48763cd0bf7cc1739751eca3b96d` of
`FloatingPragma/observer-patch-holography` (paper release r2060, dated
2 November 2026). That commit was upstream `main` when checked. Commands and
results are recorded so any reader can repeat them.

## 1. OPH evidence quotes (66/66 verified)

Command: `make verify-oph OPH_REPO=<clone of the OPH repository>`, which runs
`scripts/verify_oph_quotes.py`. For every `oph_evidence` entry in the model files
under `reviews/oph-lfdi-57/model/`, the script reads the file with
`git show <commit>:<path>` and checks the normalized quotation as a substring of
the normalized window around its recorded line (3 lines before, 2 after). The same
check runs in continuous integration on every push.

A quotation check proves the words are there. It does not prove the record read
them in context; `OPH-AUD-003` is the case that taught this. Each OPH quotation was
also read in its surrounding passage for this receipt.

## 2. LFDI/WISLIM absence in the OPH tree

Command: `git grep -c -w -i -e LFDI -e WISLIM -e Wishengrad <commit>`.

Result: no matches anywhere in the pinned tree. The `-w` matters: without a word
boundary, a case-insensitive search matches letter runs inside unrelated words.
This backs the intrinsic audit's observation (F10) that OPH does not use the LFDI
framework at the pinned commit.

## 3. Review transcription

The PDF is one page image. `pdfimages -j -p` extracts it; `tesseract` output,
whitespace-normalized, reproduces the stored
`source/LFDI_Alignment_Audit-57.txt` exactly.

Reproducing the OCR does not show the OCR is right, and it is not. A line-by-line
comparison with the page image found seven misreadings of what the page prints:
`$L_1$` read as `SL_1$`, `$L_1 = 0$` as `SL_1 = 0$`, `$D$` as `SDS`, `$U$` as `SUS`,
`E∞` as `Eoo`, `×` as `x`, and `AI` as `Al`. The OCR file is kept unchanged.
`source/LFDI_Alignment_Audit-57.verified.txt` is the citation base, and the validator
derives it from the OCR text by the literal substitution list in
`source/metadata.json`, so no other difference can enter unnoticed.

Limit: capital I and lower-case l are close in the italic footer's face. "AI" is
the reading of the glyph and the plain sense of the sentence.

## 4. PhilPapers MUEFOC (target record), retrieved 2026-11-03

- Title and thirteen authors as listed in `source/metadata.json`. The flagship
  source at the pinned commit lists fourteen authors, adding David Matscheko.
- The abstract states "Measured by the four conditions, the program is incomplete",
  "Its testable form is the executable-model hypothesis", and "federated twelve-port
  icosahedral carrier". The same sentences are in the flagship source at the pinned
  commit (`flagship/from_observer_consensus_to_standard_physics.tex:96`).
- Record status: manuscript with a PhilArchive copy; 1,062 downloads; added
  2026-09-03.
- PhilPapers refused automated requests when this receipt was revised, so these
  values stand as retrieved earlier on 2026-11-03.

## 5. WISLIM source anchors (23/23 verified)

Every `source/WISLIM-v2.0.1.txt` line number cited in `extrinsic-audit.md` and
`intrinsic-audit.md` (62, 132, 198, 204, 212, 431, 435, 437, 441, 481, 626, 644, 687,
778, 788, 824, 1108, 1282, 1853, 2158, 2625, 3262, 8198) was read at that line and matches the
content cited. The validator independently re-checks all register quotations against
the source on every run.

## 6. WISLIM PhilPapers record, retrieved 2026-11-03

`https://philpapers.org/rec/WISLIM` matches `evidence/philpapers.md`: 1,843
downloads, no citations found, "(8th edition)" title, DOI
`10.21428/4831231e.8c4c6c8f`, added 2025-09-02.

## 7. The retired pin

The first version of this tracker pinned
`docxology/observer-patch-holography` at
`1c5a908ed3441c5d09628183af18c362dbc58bea`, a fork. Measured against upstream `main`
at the current pin with `git rev-list --left-right --count`, that commit is 7 ahead
and 1,593 behind, and `git merge-base` places the fork point on 2026-09-22.

Of the 15 distinct OPH quotations recorded at that pin, 11 no longer appear verbatim
at upstream `main`. The sentence "a condition on one structure that holds or fails
with nothing running it" was rewritten upstream by commit `083afa285` on 2026-10-11,
with the subject `Clarify history, clocks and emergence across OPH materials`. Every
quotation in this tracker now cites upstream. See `OPH-AUD-002`.

## 8. Term search in WISLIM v2.0.1

`rg -c -i` over `source/WISLIM-v2.0.1.txt` returns no hits for "Engineering Proof",
"Airtight", "Epistemic Invariant", "No Truth Outside", "Decision Entropy",
"Performative", or "truthful interest". "Substrate-neutral" and "LFDI" do occur
(`source/WISLIM-v2.0.1.txt:1195`, `source/WISLIM-v2.0.1.txt:208`). The nearest passage
to "Engineering Proof" is the paper's engineering version at
`source/WISLIM-v2.0.1.txt:667`, and the nearest to "Decision Entropy" is "ethical entropy
(D)" at `source/WISLIM-v2.0.1.txt:481`.

## Epistemic status

Verified above: quote anchoring in OPH and WISLIM, the transcription against the page
image, the absence claim over the OPH tree, and the term search. Taken from the
earlier retrieval on the same day: the PhilPapers fields. Not verified: the internal
correctness of OPH's formal results (not contested by this tracker), the review
sender's verification procedure, and which OPH release the sender audited, which the
sender has not stated.
