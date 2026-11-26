# Build the WISLIM audit manuscript

Use Git, uv, Pandoc 3.14 with pandoc-crossref 0.3.26b, and XeLaTeX with the
[required TeX packages](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/usage/output-formats.md).
The audit’s [local checks](reproducibility.md) use the Python standard
library. The renderer has a separate locked environment.

From a clean WISLIM-audit checkout:

```sh
set -e
project_root="$(pwd -P)"
renderer="$(mktemp -d)/template"
git clone https://github.com/docxology/template.git "$renderer"
git -C "$renderer" checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
mkdir -p "$renderer/projects/working"
project_copy="$renderer/projects/working/WISLIM-audit"
git clone --no-hardlinks "$project_root" "$project_copy"
git -C "$project_copy" checkout --detach "$(git -C "$project_root" rev-parse HEAD)"
make -C "$project_copy" verify

cd "$renderer"
uv sync --locked --no-dev
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/WISLIM-audit
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/WISLIM-audit
```

Find the combined PDF in `output/pdf/`, HTML at `output/web/index.html`,
and validation and provenance reports under `output/reports/` in the
disposable copy. The [manuscript](manuscript/README.md) contains six ordered
sections, a classification table, and bibliographic references. It renders
from authored Markdown. Archival PDFs, correspondence, and scenario records
are separate evidence and are outside the manuscript’s input set.
