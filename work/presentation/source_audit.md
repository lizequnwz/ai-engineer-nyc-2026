# Presentation evidence and source audit

Audited `outputs/ai-engineer-nyc-2026-presentation.html`, its embedded JSON and static DOM, `work/presentation/deck-data.json`, attendee-note records/raw attachments, both official program snapshots, and `work/wealth_context.json`. No browser navigation, external expansion, or output edits were performed.

## Result

**The principal evidence boundaries are correct.** All 12 identified note-session UUIDs are registered and referenced in the core presentation; their titles match the intended October 10 or October 14 snapshot. The HTML's embedded slides/sources exactly match `deck-data.json`. All 37 page records have static HTML articles and all declared source references have visible links. The 29-slide core sums to 40 minutes; eight appendices are outside the timed path.

Three small corrections would improve the final evidence trail; none requires new substantive research.

## Findings

1. **UBS atlas row cites only the dated Red source for a broader claim.** In the reading-mode `appendix-atlas` table, the UBS row says “Institutional knowledge access and personalized advisor meeting intelligence” and “dated and undated sources,” but its only linked source is E02, the February 4, 2025 results release/landing page. `wealth_context.json` attributes personalized STAAT advisor meeting intelligence to the separate **undated** corporate “Innovation and AI at UBS” webpage, inspected October 10, 2026. Either add that specific URL with an undated/observed-date label to the UBS atlas record/catalog, or narrow the atlas row to Red's institutional knowledge access and dated rollout. The core wealth slide is already narrower and correctly dated. Do not use October 10, 2026 as the publication date of the undated webpage.

2. **Range's strategy-map visual makes capacity sound established.** The static HTML for `strategy-02` uses the row wording “Expert capacity expands through drafting.” The notes support parallel drafting and subsequent planner review; no accepted-output capacity, correction burden, or measured productivity change was captured. The reading notes correctly state this limitation, but the live visual would be more precise as “Parallel drafting alongside planner work” or “Planner capacity bottleneck; impact to measure.” This avoids a benefit assertion stronger than the evidence.

3. **A few local source lists omit a named motivating source.** All sources exist elsewhere in the presentation, so these are page-level citation gaps, not missing research. `growth-02` names “Two Sigma / Sonar” in its visual example but does not include Sonar/S16 among its local source keys. `appendix-unknowns` discusses the OpenAI “crunchable” term and Bridgewater's reactive/proactive reversal but does not include OpenAI/S03 or Bridgewater/S04 in that page's local source keys. Add these references if the page is intended to stand alone when printed or shared.

## Required attribution checks passed

- **Notes versus program:** visible tags distinguish attendee accounts, program context, firm disclosure, synthetic illustration, and proposed method. Reader notes explicitly state when added detail comes from the program rather than the live capture. Program-only Monzo, Optiver, Upstart, Wise, Vanguard and other retained atlas cases are not claimed as attended sessions or independently checked implementations.
- **Range:** `workflows-01` explicitly says the five steps are captured in notes, while owner/reviewer and peer review are fresh agenda context. The visible page includes a Program context tag. The current Matt Ragone/Range title is correct. Reader notes preserve the crucial UUID reuse: the same ID described an NVIDIA reranker in the October 10 snapshot. No NVIDIA content is attached to the Range case.
- **Ramp:** S10 uses the fresh October 14 title “Building Better Agents Through End-to-End Evals,” consistent with the supplied note heading. Its eight-to-four skill count is treated as an as-recorded intervention, not an optimal bundle size or a proven universal improvement. The deck does not silently identify the program's 14k-to-5k skill reduction as the Excel skill.
- **Kepler:** `grounding-03` and the typed-claim appendix label the entity/period/unit/version fields and contract as a proposed design, not verified Kepler coverage. Reader notes state that these questions were not answered in the capture and reject a guarantee that every fact is deterministically correct. Ambiguous retrieval parameters remain examples rather than defaults.
- **Synthetic examples:** AsterCo's 100/118/120 revenues, 20%/18% calculations, the fictional client 120,000/84,000/36,000 arithmetic, the monthly 8,000/6,000/2,000 rubric, its 0–2 scores, and the three-attempt strip are explicitly labeled synthetic/illustrative. Arithmetic is consistent. No invented value is attributed to a firm result, actual client, Fidelity benchmark, or advice. The hypothetical approval/authority path is not labeled Range's deployed architecture.
- **Sonar:** `workflows-04` explicitly assigns its three-loop structure to the official abstract and its four assurance factors to attendee notes. It labels the confidence product conceptual and uncalibrated. The 50k-line example remains conditional and unverified, with no universal codebase threshold.
- **Two Sigma and Wise:** Two Sigma control components come from attendee notes; classifier type, effectiveness, and enforcement powers remain unspecified. Wise's reasoning/authority separation is agenda-only. Their combined diagram is explicitly proposed synthesis rather than either firm's full disclosed architecture.
- **Comet/NatWest:** S12 and the relevant reading notes preserve the discrepancy: attendee/October 10 says Comet, October 14 metadata says NatWest. No page assigns Cora to a bank based on its name or the changed speaker affiliation. The 100K/day scale and “roundedness” ambiguity are not transformed into measured reliability or an invented safety metric. The release gate remains editorial, and the unanswered reviewer/rollback question is not presented as observed policy.
- **pass@k:** the deck distinguishes at-least-one-success across attempts from first-attempt and selected-output reliability. The three-attempt strip is one synthetic case, not an empirical pass@3 estimate. The primary method reference is separate from the conference note, and no code-benchmark numerical result is transferred to financial workflows.
- **Risk/ROI:** the incident-count title is not converted into population failure rates. The incomplete expected-loss product, exponential-growth assertion, and incident rankings remain follow-up gaps. Contour's three-month/A/B account is not presented as randomized or causally established alpha/ROI. Adoption, accepted work, process effects, full cost, and attributable outcomes are explicitly distinguished.
- **External dates:** Morgan Stanley June 26, 2024; UBS February 4, 2025; and RBC March 27, 2025 agree with `wealth_context.json`. These are labeled historical firm disclosures, not NYC sessions or latest-state claims. RBC survey adoption/satisfaction and US-pilot conversion remain distinct. The separate 2021 method paper is labeled a primary method source. The only external-source coverage gap is the broader UBS atlas wording described above.
- **Company identities:** Citadel Securities stays distinct from Citadel; JPMC's panel participation is not deployment; Arca carries similarly named-firm caution; role-only Blackstone/Coatue records remain insufficient-detail cases. No sponsor logo is used as deployment evidence.

## Twelve note-session coverage

| Source | Intended snapshot / identity | Core reference examples |
|---|---|---|
| `a84ca3a8-cc2f-4b50-a635-fc380f6f04f6` | Oct 10 metadata · Bridgewater Vault | strategy-02; grounding-01/02 |
| `73badd10-6f8c-4c95-b5e7-55fc3d7bafc1` | Oct 10 metadata · Two Sigma safety | strategy-02; workflows-03 |
| `5191589c-a70e-4806-99dc-86f7794f46b9` | Oct 10 metadata · Capital One code quality | growth-03 |
| `b2ed4456-5671-4e8e-83fd-684c012fef8c` | Oct 10 metadata · Arize AI engineer | evals-06; growth-01 |
| `9d72d7ac-a2a2-42cf-b880-5859316d840c` | Oct 10 metadata · System failures / New York Life speaker + Tanmay Sah | evals-01/02/04/05/06 |
| `ae273f0b-db0f-4638-8ae3-05874bebf9ca` | Oct 10 metadata · Contour Proving Alpha | strategy-01/04/05 |
| `2d29f925-f16b-41b3-8086-de0524829cbe` | Oct 10 metadata · Kepler numbers | grounding-03/04/05 |
| `4add802c-6a68-4e9c-93fb-9c1e017193bc` | Oct 14 metadata · Sonar | workflows-04; growth-03 |
| `02f94835-c29d-4cf5-b77a-c5a491b747b8` | Oct 14 metadata · OpenAI finance | strategy-01; grounding-05 |
| `4607dbbe-8f94-4b0e-91ce-257d1cfb5448` | Oct 14 renamed title · Ramp | evals-01/02/03/04/06 |
| `9b002687-09cf-42e2-9282-532ed9d0c184` | Oct 14 replaced record · Range, not old NVIDIA title | strategy-01/02/03; workflows-01/02 |
| `e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa` | Oct 14 metadata · banking talk; Comet/NatWest discrepancy retained | evals-01/03/05 |

No blocking factual attribution or maturity issue was found in the core presentation. Address the UBS source breadth and the Range visual wording to make the printed/slide evidence as precise as the reading notes.
