# Presentation narrative audit

Reviewed the actual slide-card text and reading content of `outputs/ai-engineer-nyc-2026-presentation.html`, plus the corresponding `work/presentation/deck-data.json`. Used filesystem/HTML parsing only. No source or output edited.

## Material finding

**[P2] Bound the Range capacity claim on `slide-strategy-02`.** The projected company table says **“Expert capacity expands through drafting.”** The notes establish the described mechanism—agent drafting in parallel with a planner's client work, followed by review and adjustment—but contain no measured net capacity improvement. Review and correction effort could offset some or all of the benefit. Replace the cell with **“Planner work is prepared in parallel”** or **“Professional capacity is the bottleneck.”** The reading notes already preserve the correct evidence limit; bring the projection wording into line with them.

## Requirements checked

- **English / technical audience:** English throughout, with substantive concepts for data scientists, AI engineers and technical leads. Typed evidence, rubrics, judge validation, paired experiments, authority boundaries and operational invariants give the audience concrete engineering material.
- **Narrative and chapter structure:** The five requested chapters are explicit: finance strategy/value; grounding; evaluation; reliable workflows/skills; and engineer growth. The argument follows decisions and dependencies rather than conference chronology. Opening, conclusion and appendix support that structure.
- **Timing:** Twenty-nine core slides total **40.0 minutes** in the structured timing data. The last discussion slide is assigned zero timed minutes, and the cover/readers describe discussion as additional. Eight appendix slides are outside the timed path.
- **Company stories and evidence:** The core includes substantive Bridgewater, Contour, Range, Two Sigma, Kepler, Ramp, Sonar and Arize stories, plus marked program context and dated Morgan Stanley/UBS/RBC disclosures. Evidence labels and source boundaries remain visible. The source catalog contains the 38 session/disclosure/method records used by the deck and atlas.
- **Practitioner methods and worked examples:** The deck explains workflow acceptance, the value ladder, all-in cost, grounding contracts, ablations, judge validation, release gates, skills and authority. Worked revenue-growth, cash-flow-rubric and review-packet examples are prominently synthetic; arithmetic and narrative boundaries are internally consistent. No invented example is attributed to a firm.
- **Engineer growth:** Four substantive slides connect the improvement loop, five responsibilities, lifespan/consequence tradeoffs and a bounded learning exercise. These are proposed development practices, not a surveyed industry skill ranking or Fidelity commitment.
- **Reading and speaker notes:** Every core slide has useful explanatory reader notes and speaker notes, including provenance, limits, transitions and discussion prompts. Reading mode expands technical examples and the evidence atlas rather than merely repeating slide bullets.
- **Projection density:** Actual core slide cards contain about 57–116 words including headers, evidence labels and footers. The densest worked examples have about 100–116 words, organized into tables/panels; no material content-density issue was found from text inspection. Physical readability/overflow still requires the separate visual QA.
- **Source caution:** Range confirmation and the current session match are preserved; the historical UUID/title change is explained in reading notes. Comet/NatWest remains an unresolved affiliation discrepancy, not an inferred Cora-bank attribution. Ambiguous product terms and thresholds are not silently repaired into validated claims.
- **Separate deliverable:** The presentation uses its own HTML path and structure, distinct from the existing industry report.

Scope: narrative, requirements, attribution and text-density review. Speaker claims, implementations, current product specifications and outcomes were not independently validated by this audit; no browser rendering or interaction checks performed.
