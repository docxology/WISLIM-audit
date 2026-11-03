# Source

This directory contains the immutable object of the audit.

| File | Description |
|---|---|
| `WISLIM-v2.0.1.pdf` | User-supplied PDF, 289 pages, 348,857 bytes. |
| `WISLIM-v2.0.1.txt` | Text extraction produced with `pdftotext -layout`. 13,255 lines, 40,538 words. |
| `metadata.json` | Checksums, bibliographic record, extraction command, license notes. |

All line citations in `audit/`, `red-team/`, `model/`, and `evidence/` refer to
`WISLIM-v2.0.1.txt`. The text is an extraction, not a critical edition; page
breaks and layout are approximate. Where a citation is decisive, the audit also
names the section.

Line numbers are **1-based and newline-delimited**, matching `wc -l` and
`grep -n`. The file contains 289 form-feed page breaks; Python's
`str.splitlines()` counts those as extra lines and reports 13,544 lines. Do not
use `splitlines()` for citations. See `../evidence/provenance.md`.

## Extraction

```sh
pdftotext -layout source/WISLIM-v2.0.1.pdf source/WISLIM-v2.0.1.txt
```

## Public record

The paper is listed on PhilPapers as `WISLIM`, with DOI
`10.21428/4831231e.8c4c6c8f`. The PubPub release page is dated 4 February 2026
and describes the work as CC-BY 4.0. The PDF itself says "I dedicate this work to
the public domain." The audit records both statements and does not resolve them.

## Versioning

The attached PDF is Version 2.0.1. PhilPapers labels the record an "8th edition."
The PubPub page is Release #1. These labels are not reconciled in the source.
See `../evidence/provenance.md`.
