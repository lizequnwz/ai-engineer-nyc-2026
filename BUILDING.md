# Editing and rebuilding the archive

The final HTML, Markdown and PPTX files are ready to consume. Current conference deliverables include the October 25 recording revision. Application companions and the pre-conference field guide retain their original scope. Rebuilding overwrites generated outputs; commit edits first.

## HTML and Markdown

From the repository root with Python 3.10 or later (standard library only):

```sh
python3 work/build_report.py
python3 work/recording_content.py
python3 work/day1_report_content.py
python3 work/day2_report_content.py
python3 work/build_industry_report.py
python3 work/presentation/build_deck.py
python3 work/applications/build_brief.py
```

The presentation builder writes the HTML and its generated `work/presentation/deck-data.json`. Edit the owning story/grounding/eval JSONs and four enrichment JSONs, plus the body renderers when a diagram changes. `work/recording_evidence.json` holds the 37 later-source briefs; `work/recording_content.py` renders the recording supplement, daily follow-ups and report digest.

These commands do not fetch a current schedule, video or company disclosure. Preserve source dates and classes when authoring. Earlier content-authoring helpers such as `build_grounding_workflows.py` are not required rebuild steps; rerunning them can replace editorial content.

## PowerPoint

Final decks contain editable native text, diagrams, tables and speaker notes. The two authoring projects under `work/ppt-master/` include canonical `svg_output/`, preview `svg_final/`, notes, normalized content and design specifications. The conference deck has 37 slides, 37 note pages and nine native tables. The application deck has 28 slides and 28 note pages.

HTML rebuilding does not regenerate PowerPoint automatically. Revise the canonical SVG and its plan/notes together, then use the external `ppt-master` skill/runtime to validate, split notes, finalize and export. The skill and installed dependencies are not bundled. The October 25 conference export receipt is `validation/ai-engineer-conference-takeaways_20261025_065805_native_charts_tables.report.json` inside its project.

## Validation

`PACKAGING-VALIDATION.json` records actual package checks. `work/presentation/recording-refresh-validation.json` records the current content/source/structure audit. The conference SVG gate passed all 37 pages with zero errors and warnings; the PPTX postflight passed. HTML DOM/navigation checks passed, including source dialogs, keyboard controls, print-state restoration, self-contained assets and contrast. These are not browser-layout or PowerPoint-render inspections; the prior local-browser restriction prevented those checks.

Seven source builders were run in a disposable copy. Their regenerated outputs were compared byte-for-byte with the package. Source links remain external and require internet. Historical audits retain their dates and can describe issues later resolved; they are not current validation receipts. JavaScript QA dependencies are pinned in `work/qa/package-lock.json`, but installed packages are omitted.

## Package integrity

`MANIFEST.json` hashes every file except itself and `SHA256SUMS.txt`. The checksum list also covers the manifest and excludes only itself. Regenerate both after intentional changes. The package omits Git metadata, installed dependencies, caches, duplicate exports, SVG backups, raw third-party transcripts/watch pages and browser annotations. Re-export browser-added notes separately if needed.
