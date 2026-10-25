# Conference takeaways — editable slide sources

Final PowerPoint: [open/download](../../../outputs/ai-engineer-nyc-2026-conference-takeaways.pptx).

- `svg_output/`: canonical editable slide drawings used for native PPTX export.
- `svg_final/`: generated, self-contained SVG previews; these differ from the source drawings.
- `notes/`: per-slide Markdown notes plus the combined notes file.
- `sources/`: normalized content, deck data and conversion provenance.
- `design_spec.md` and `spec_lock.md`: design decisions, content and layout contracts.
- `validation/`: final SVG checks, text calibration, content-carrier review and PPTX postflight receipts from the authoring run.

The PPTX itself is editable in PowerPoint. Exporting these SVG sources back to native PowerPoint requires a separately installed compatible `ppt-master` skill and its Python dependencies. This archive does not vendor that skill or promise an independent PPTX build environment. Font assumptions: Arial, Cambria and Consolas. No external image files were required by the recorded exports.

Validation receipts retain their original authoring paths and hashes as historical provenance. Omitted backup/export paths in those receipts refer to excluded duplicate intermediates. See the package manifest for the files present here.

## Recording revision · October 25, 2026

The current37-slide deck incorporates the released-source review. Sources include37curatedbriefs, with source classes and limitations in notes. The final native export has37slides,37notes and9editabletables. The current export postflight and final SVG report passed with zero warnings. Actual PowerPoint rendering was not performed.
