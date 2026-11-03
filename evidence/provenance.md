# Provenance

## The object

The audit covers the user-supplied PDF:

- Title: *Life is Most Important in Life is The Most Important Truth in Life: A
  Foundational Proof for Alignment, Identity, and the Cure of Needless
  Suffering*
- Author: David Wishengrad
- Version: 2.0.1
- Date on cover: February 04, 2026
- Pages: 289
- Bytes: 348,857
- PDF producer: PDF-XChange Lite (7.0 build 328.2)
- PDF creation: 2026-02-04 13:20:57 PST
- PDF modification: 2026-02-04 13:21:04 PST

The original attachment was found at:

`/Users/4d/Downloads/218C14D4-374E-11F1-9441-E324A0E63B03.pdf`

It was copied unchanged to:

`source/WISLIM-v2.0.1.pdf`

## Hashes

| File | SHA-256 |
|---|---|
| `source/WISLIM-v2.0.1.pdf` | `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd` |
| `source/WISLIM-v2.0.1.txt` | `aab7d298543fdf39c636706458c74118a663f8ae33c5fd2d71bca2b6f02d59f1` |

## Text extraction

The text was extracted with:

```sh
pdftotext -layout source/WISLIM-v2.0.1.pdf source/WISLIM-v2.0.1.txt
```

Text statistics:

- 13,255 newline-delimited lines
- 40,538 words
- 343,221 bytes

## Line numbering

Citations use **1-based newline-delimited line numbers**, the same numbering
reported by `wc -l`, `grep -n`, and most text editors.

The file contains 289 form-feed characters (`\f`), one per page break. Python's
`str.splitlines()` treats each form feed as an additional line break, so it
reports 13,544 lines instead of 13,255. Do not use `splitlines()` for citation
numbers. Use `split("\n")` or a line-numbering tool that counts only `\n`.

This matters because a citation to line 13,505 in the `splitlines()` numbering
does not exist in the newline-delimited text (which ends at 13,255). The audit
normalized all claim anchors to newline numbering and added a validator check.

## Immutability

`source/` is immutable. The audit does not edit the PDF or the extracted text.
If a new edition is added, it goes beside the old one and the metadata is
updated.

## Version labels

The public record uses inconsistent labels:

| Source | Label |
|---|---|
| PhilPapers | "8th edition" |
| PDF cover | Version 2.0.1 |
| PubPub | Release #1 |
| PubPub page | Published Feb 04, 2026 |
| PubPub release metadata | Release #1, Mar 11, 2026 2:57 PM |

The audit treats the PDF as the object and records the inconsistency rather
than guessing which label is authoritative. The "8th edition" may refer to an
earlier or later revision; the audit cannot verify without the other editions.

## License

The license is ambiguous:

- PubPub displays a Creative Commons Attribution 4.0 International License
  (CC-BY 4.0).
- The PDF closes with: "I dedicate this work to the public domain."
  (`source/WISLIM-v2.0.1.txt:13255`).
- The author's PubPub comment says the paper is "dedicated to the public
  domain and freely shared for the public good."

CC-BY 4.0 requires attribution. A public-domain dedication does not. The two
statements are not the same. Until the author clarifies, the audit treats the
license as unresolved.

Consequences:

- The audit preserves full attribution (satisfying CC-BY 4.0) while recording the public-domain dedication.
- The audit does not relicense the source.
- Quotations are used for criticism and review.

## Public record

- PhilPapers: `https://philpapers.org/rec/WISLIM`
- DOI: `10.21428/4831231e.8c4c6c8f`
- PubPub: `https://life-is-most-important-in-life.pubpub.org/pub/n81ngqkw/release/1`
- PhilPapers added: 2025-09-02
- PhilPapers downloads: 1,843 as of 2026-11-03
- PhilPapers citations of this work: none found as of 2026-11-03

The download count is a PhilPapers metric, not a measure of scholarly uptake.
The "no citations found" result is PhilPapers' record, not proof that no one has
cited the work elsewhere.

## Missing materials

The audit does not have:

- the raw prompts used to elicit the AI letters;
- the full transcripts of the AI workspace;
- model version identifiers, API receipts, or sampling parameters;
- the coding protocol for the "100% consensus";
- the raw data for the "Observed Reception" claim;
- the other editions (including the "8th edition");
- a PubPub Markdown copy (a direct download attempt returned HTTP 403 earlier;
  the PDF text is sufficient for this audit).

These absences are material. The consensus critique is methodological, not
forensic. It shows that the published process cannot support the published
claim; it does not reconstruct what each model was told.

## Verification

To verify the source:

```sh
shasum -a 256 source/WISLIM-v2.0.1.pdf source/WISLIM-v2.0.1.txt
pdfinfo source/WISLIM-v2.0.1.pdf
wc -lw source/WISLIM-v2.0.1.txt
python3 tools/validate.py
```

The validator checks the hashes, line bounds, claim anchors, stress-test
catalog, and internal links.

## Provenance of the audit

The audit was produced in `docxology/WISLIM-audit` with
AI assistance. It is a first complete critical pass, not a peer-reviewed
publication. The audit's claims are only as good as the evidence cited. Where
the evidence is unavailable, the audit says so.
