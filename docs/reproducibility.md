# Reproducibility

## Requirements

- Python 3.11 or newer, standard library only.
- `pdftotext` (Poppler) to re-extract the text.
- `shasum` or `sha256sum` to verify hashes.
- `gh` (GitHub CLI, authenticated) only for the GitHub issue mirror.
- `pytest` is optional; the validator runs without it.

The repository intentionally avoids third-party Python dependencies. The
validator and tests use only the standard library.

## Verify the source

```sh
shasum -a 256 source/WISLIM-v2.0.1.pdf source/WISLIM-v2.0.1.txt
```

Expected:

```
7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd  source/WISLIM-v2.0.1.pdf
aab7d298543fdf39c636706458c74118a663f8ae33c5fd2d71bca2b6f02d59f1  source/WISLIM-v2.0.1.txt
```

Check the PDF metadata:

```sh
pdfinfo source/WISLIM-v2.0.1.pdf
```

Expected: 289 pages, 348,857 bytes, PDF version 1.4.

Check the text statistics:

```sh
wc -lw source/WISLIM-v2.0.1.txt
```

Expected: 13,255 lines, 40,538 words.

## Re-extract the text

```sh
pdftotext -layout source/WISLIM-v2.0.1.pdf /tmp/WISLIM-v2.0.1.txt
shasum -a 256 /tmp/WISLIM-v2.0.1.txt
```

The hash should match the text hash. If it does not, the Poppler version or
options differ. The audit's line numbers depend on the extracted text, so a
different extraction may shift them.

## Run the validator

```sh
python3 tools/validate.py
```

The validator checks:

- source PDF and text hashes;
- source line, word, and byte counts;
- claim IDs, required fields, line bounds, and anchor text;
- the 210 stress tests and summary counts;
- the 66-issue register: stable IDs, C01–C35/AS01–AS20/WS01–WS11 coverage,
  generated records, and the GitHub issue map;
- every issue carries a publication reference and at least one primary
  quotation, and every quotation is a verbatim substring of the source at its
  `line`;
- every issue carries `status: observation` and the non-fatal status note;
- explicit source-line citations are within bounds;
- required files exist;
- relative Markdown links resolve;
- the README, AGENTS, and provenance contain the required notes.

## Run the tests

```sh
python3 -m unittest discover -s tests -v
```

If `pytest` is installed, the same tests also run under pytest:

```sh
python3 -m pytest -q
```

The tests exercise the validator, the source hashes, the claim and stress-test
registries, and the 66-issue register. They use only the standard library, so
the repository remains runnable without pytest.

## Issue register and GitHub mirror

The canonical register is `model/issues.json`. It holds 35 claim issues
(`C01`–`C35`), 20 red-team issues (`AS01`–`AS20`), and 11 workstream issues
(`WS01`–`WS11`). Each issue has one generated record under `docs/audit/`.

```sh
make register                  # regenerate docs/audit/ records and index
make issues                    # create missing issues and refresh bodies
make issues-check              # read-only comparison with GitHub
```

`model/issue-map.json` records the GitHub number, URL, title, and state for each
issue. `scripts/sync_issues.py` never creates a duplicate: it matches the
`WISLIM-NNN:` title prefix, adopts any existing issue, and updates bodies in
place. The `make verify` target is offline and does not contact GitHub;
`make issues-check` is the networked check and requires an authenticated `gh`.

The issue bodies are derived from the records, not independently edited. To
change an issue, edit `model/issues.json`, run `make register`, then
`make issues`. GitHub comments are not mirrored back into the repository.

## OPH/LFDI review register

The external review `reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.pdf` is
an image-only one-page PDF. Its raw OCR text is stored at
`reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.txt` and its provenance at
`reviews/oph-lfdi-57/source/metadata.json`.

Verify the review hashes:

```sh
shasum -a 256 reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.pdf reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.txt
```

Expected:

```
2f5c91b5e500c22560eee137a960ab39b6ed8c230899d24c9491393f265823a5  reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.pdf
ba92b8a91ae5c6fe7b23b7270d44c5175129411a8cdd863d903c9c2583ec65ab  reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.txt
```

The OCR text misreads the page's symbols and is kept as a record. The citation base
is `reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.verified.txt`, a transcription
compared with the page image. The validator derives it from the OCR text by the
literal substitution list in `metadata.json`, so nothing else can differ:

```
92416993bad7fd4c0dd981b675f8f125d793079ce9c1cdfb9bb1645354a9f300  reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.verified.txt
```

Regenerate and verify the 12-topic review register (`OPH-REV-001`–`OPH-REV-012`):

```sh
make review                    # regenerate reviews/oph-lfdi-57/ and docs/reviews/
make review-check              # verify generated review records without writing
```

The reply of 2026-11-03 has its own canonical model and generated records:

```sh
make reply                     # regenerate the reply register, corrections, and ledger
make reply-check               # verify them without writing
make reply-issues              # create missing GitHub issues and refresh bodies (needs gh)
make reply-issues-check        # read-only comparison with GitHub (needs gh)
```

`make reply-check` also rejects any email address or telephone number in the
correspondence, reply, and correction records.

Check every OPH quotation at the pinned upstream commit. This needs `git` and a clone
that contains the commit; continuous integration runs it on every push:

```sh
make verify-oph OPH_REPO=/path/to/observer-patch-holography
```

## Rebuild the stress-test catalog

```sh
python3 tools/build_stress_catalog.py
```

This reads the source text, extracts the 210 Appendix D titles, applies the
curated verdict map, and writes `model/stress-tests.json`. The script is
idempotent. It uses only the standard library.

## Line numbering

Citations use 1-based newline-delimited line numbers. The source contains 289
form-feed page breaks. Python's `str.splitlines()` counts each form feed as an
extra line and reports 13,544 lines. The validator uses `text.count("\n")` and
`text.split("\n")`, not `splitlines()`.

This is a common source of off-by-page citation errors. If you add citations,
verify them with `grep -n` or `Read` (which use newline numbering), not with a
Python `splitlines()` index.

## What is not reproducible

- The raw AI prompts and transcripts are not available.
- The model versions and sampling parameters are not available.
- The "Observed Reception" data is not available.
- The other editions (including the "8th edition") are not available.
- The PubPub Markdown copy was not downloaded; the PDF text is the object of
  record.

These gaps are recorded in `evidence/provenance.md` and
`evidence/ai-letter-audit.md`.
