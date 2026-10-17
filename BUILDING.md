# Editing, rebuilding and verification

## Final files first

The final HTML, Markdown and PPTX files are ready to consume. The original final deliverables are preserved unchanged under `outputs/`. Rebuilding can overwrite those files, so work in a separate checkout or commit your edits first.

## HTML and daily-note sources

The builders use Python’s standard library. From the repository root, using Python 3.10 or later:

```sh
python3 work/build_report.py
python3 work/build_industry_report.py
python3 work/day1_report_content.py
python3 work/day2_report_content.py
python3 work/presentation/build_deck.py
python3 work/applications/build_brief.py
```

`work/build_report.py` creates the historical field guide. The industry builder consumes the integrated daily-note modules and source JSON. The presentation builder consumes the research/notes and its enrichment JSON. The application builder contains the dated review findings in its source; it does not open or re-inspect the separate personal repository.

Data JSON, research Markdown and schedule HTML are snapshots. These commands do not fetch a current conference schedule or refresh public company claims. Do not rerun `build_institution_cases.py` or `build_grounding_workflows.py` merely to build the final reports: they are earlier content-authoring helpers, retained for editing context.

## PowerPoint

Use either final `.pptx` file directly in PowerPoint for editing. Native text, diagrams, tables and notes are retained. Editable SVG sources, slide content, per-slide notes, design specifications and final validation receipts are in the two `work/ppt-master/` projects.

Native re-export from those projects depends on the separately installed `ppt-master` skill used for authoring. Its implementation and runtime are not included. The archive supplies editable sources, not a fully vendored PPTX exporter. Finalized SVGs are previews, not a replacement for the native PowerPoint files.

## Packaging checks

All six Python builders above were run in a disposable copy of this archive. The four HTML reports and two daily Markdown note files they regenerated matched the packaged final files byte-for-byte. All ten final artifacts match their original local files. Both PPTX archives passed ZIP integrity checks and their slide/note/table counts were verified. See `PACKAGING-VALIDATION.json`.

## Recorded checks

The existing PPTX export receipts report passed structural postflight checks: 37 slides/37 note pages for the conference deck and 28 slides/28 note pages for the application deck. Final SVG quality reports are included. These historical receipts preserve original authoring paths; the package contains stable output filenames rather than timestamped duplicate exports.

Historical HTML/content audits and QA results are retained as working evidence. They can include issues later resolved, blocked browser checks and source-specific assumptions. Read their status and date; their presence does not mean every browser interaction passed. QA scripts are development aids and can need path adjustments for a new environment. Optional JavaScript dependencies are pinned in `work/qa/package-lock.json`; installed dependencies are omitted. The lockfile’s jsdom dependency requires a compatible modern Node version.

No new browser-rendered or PowerPoint-rendered visual inspection was performed during packaging. The packaging validation report records integrity, archive structure, local artifact links and source-build checks actually performed.

## Integrity

On macOS, from the repository root:

```sh
shasum -a 256 -c SHA256SUMS.txt
```

`MANIFEST.json` hashes the archive content except itself and `SHA256SUMS.txt`. `SHA256SUMS.txt` also covers the manifest, excluding only itself. After intentional edits, those original checksums will no longer match.
