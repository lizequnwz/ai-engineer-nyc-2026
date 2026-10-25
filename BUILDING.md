# Editing and rebuilding the archive

The 13 final HTML, Markdown and PPTX files are ready to consume. Current conference deliverables include the October 25 recording revision, eight re-authored core walkthroughs and a presenter guide. Application companions and the pre-conference field guide retain their original scope. Rebuilding overwrites generated outputs; use a disposable copy or commit edits first.

## HTML and Markdown

From the repository root with Python 3.10 or later (standard library only):

```sh
python3 work/build_report.py
python3 work/recording_content.py
python3 work/day1_report_content.py
python3 work/day2_report_content.py
python3 work/build_industry_report.py
python3 work/presentation/build_deck.py
python3 work/presentation/build_presenter_guide.py
python3 work/applications/build_brief.py
```

The presentation builder writes the HTML and its generated `work/presentation/deck-data.json`. Edit the owning story/grounding/eval JSONs, four enrichment JSONs and `work/presentation/core_cases.py`, plus the body renderers when a diagram changes. The latest core walkthroughs are pages 03, 08, 09, 11, 16, 18, 19 and 23.

`work/presentation/presenter-script.json` is the shared spoken script for the 29 core slides. Run `build_deck.py` before `build_presenter_guide.py` so the guide consumes the current slide content. The guide builder writes both HTML and Markdown presenter guides, including cues, transitions, three discussion prompts, eight Q&A answers, a roughly 25-minute route and print support. Keep script changes aligned with the current visuals and core PowerPoint notes; the eight appendix notes retain reference narration. The 40-minute core is a target that needs rehearsal.

`work/recording_evidence.json` holds the 37 later-source briefs; `work/recording_content.py` renders the recording supplement, daily follow-ups and report digest.

These commands do not fetch a current schedule, video or company disclosure. Preserve source dates and classes when authoring. Earlier content-authoring helpers such as `build_grounding_workflows.py` are not required rebuild steps; rerunning them can replace editorial content.

## PowerPoint

Final decks contain editable native text, diagrams, tables and speaker notes. The two authoring projects under `work/ppt-master/` include canonical `svg_output/`, preview `svg_final/`, notes, normalized content and design specifications. The conference deck has 37 slides, nine native tables and 37 note pages: 29 core spoken notes aligned with the shared presenter script, plus eight appendix notes. Its 29-slide core targets 40 minutes plus discussion; eight appendix pages are optional. The application deck has 28 slides and 28 note pages.

HTML rebuilding does not regenerate PowerPoint automatically. Revise the canonical SVG and its plan/notes together, carry the shared core presenter script into the combined and per-slide notes, then use the external `ppt-master` skill/runtime to validate, split notes, finalize and export. The skill and installed dependencies are not bundled. The current conference export receipt is `work/ppt-master/ai-engineer-conference-takeaways_20261017/validation/ai-engineer-conference-takeaways_20261025_141637_native_charts_tables.report.json`; match any future receipt to the output revision being reviewed.

## Validation

After building the presentation and guide, install the optional JavaScript QA dependencies from the lockfile and run both checks from the repository root with a compatible modern Node version:

```sh
npm ci --prefix work/qa
node work/presentation/qa_deck.cjs
node work/presentation/qa_presenter.cjs
```

The presentation check covers the core/appendix structure, DOM/navigation behavior and related controls. The presenter check covers the guide and shared-script consistency; its recorded results are in `work/presentation/presenter-validation.json`. `work/presentation/core-story-validation.json` records the latest story revision audit; `work/presentation/recording-refresh-validation.json` retains the historical recording/source audit. `PACKAGING-VALIDATION.json` records actual package checks. The latest disposable rebuild ran eight builders and reproduced nine HTML/Markdown outputs; the two PowerPoint notes companions are maintained by the notes pipeline above. Export and script checks confirmed 37 slides, 37 note pages and nine native tables. The timed core script has 4,448 words, plus 114 discussion words; rehearse rather than treating word count as a timing guarantee. DOM and structural checks do not establish browser-layout or PowerPoint-render quality; earlier browser restrictions and historical audit limitations remain documented.

Run rebuild verification in a disposable copy and compare regenerated outputs with the package before updating its validation receipts. Source links remain external and require internet. Historical audits retain their dates and can describe issues later resolved; they are not current validation receipts. JavaScript QA dependencies are pinned in `work/qa/package-lock.json`, but installed packages are omitted.

## Package integrity

`MANIFEST.json` hashes every file except itself and `SHA256SUMS.txt`. The checksum list also covers the manifest and excludes only itself. Regenerate both after intentional changes. The package omits Git metadata, installed dependencies, caches, duplicate exports, SVG backups, raw third-party transcripts/watch pages and browser annotations. Re-export browser-added notes separately if needed.
