# Engineering reliable and useful financial AI

This is the revised, analytical team briefing based on the five selected talks.
The cases remain the evidence, while each slide states a conclusion, provides
engineering analysis, and explains an application implication.

## Deliverables

- `../../outputs/ai-engineer-2026-five-stories.html`: 22 fully visible analytical
  slides, with a reading edition and further source/technical detail.
- `../../outputs/ai-engineer-2026-five-stories-presenter-guide.html`: aligned
  speaking notes, timing, discussion focus, source briefs, and printing.

Open the presentation in a modern browser. Arrows or Space move directly between
slides. Contents and the section labels provide navigation. Read shows the whole
briefing with supplementary explanation. The presenter guide belongs on a second
screen. Print includes all slides and restores the delivery state afterward.

The target remains 35 minutes presenting plus 10 minutes discussing. The briefing
opens with an executive summary and ends with consolidated takeaways and team
reflection. No roadmap, experiment selection, or owner assignment is required.

## Editorial and design contract

- Conclusion-led headlines and visible engineering detail on every slide.
- Case evidence, mechanisms, validation criteria, tradeoffs, and implications.
- Case openers explain the users, business problem, and application before the
  engineering lessons. Each case footer retains the full talk title and presenter
  alongside a short description of the source application or workflow. Max’s
  contribution is identified as an engineering perspective rather than a product.
- Restrained white surfaces, navy typography, teal emphasis, and flat analytical
  tables/process exhibits. System fonts and no external runtime assets.
- Main-slide content is complete when the slide appears. The theatrical opening,
  oversized typography, decorative mockups, dark scenes, and reveal engine were
  removed rather than retained behind a configuration switch.
- Research accounts, our applications, and fictional examples remain distinct.

The verified main-slide word counts range from 160 to 239. The full speaking
notes and deeper qualifications remain available in the guide and reading edition.

## Build and verify

From the repository root:

```sh
python3 work/story-session/build.py
node work/story-session/qa.cjs
```

`briefing.json` owns headlines, supporting statements, application implications,
speaker notes, source bindings, and timing. `visuals.py` owns analytical exhibits.
`deck.css` and `deck.js` own styling and direct slide navigation. `build.py`
assembles both self-contained HTML files and the readable source briefs.

The build uses Python’s standard library. DOM verification uses the existing
`work/qa` dependency lock. Restore absent dependencies with `npm ci` in that
directory. The deliverables themselves need no installation or runtime server.

## Evidence and validation

`research/sources.json` records the acquisition method and checksums of five
complete original-release English auto-generated transcript exports. The local
working copies are under `research/transcripts/` and ignored by Git. Original
captions are preserved without silent edits. Official metadata and organizer
readings inform corrections to names and terminology in the paraphrased analysis.

`research/briefs.json` contains the case briefs and application context;
`source-briefs.md` is its
generated readable form. Shareable HTML contains original paraphrases and links,
not full caption copies. No audiovisual viewing or independent validation of
company outcomes is claimed.

`validation/qa-report.json` records content, table structure, DOM interactions,
printing state, source checksums, synthetic calculations, offline independence,
and static contrast checks. The earlier browser URL-policy rejection prevents a
local-file visual preview workaround. Actual rendered geometry, physical
readability, and print pagination remain unverified.

`validation/timing-review.json` is an editorial word-count estimate, not a spoken
rehearsal. Rehearse the delivery in the presenter’s own voice.

The root manifest/checksums retain the older archive snapshot. This briefing has
its own build and validation records. Existing unrelated deleted files were not
restored or changed.
