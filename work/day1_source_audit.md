# Day 1 supplied-notes source audit

Reviewed the supplied `Pasted text.txt` against `work/program.json` for conference metadata and source boundaries. This audit uses the attendee's notes and the saved official program only; it does not independently verify speaker claims or add external facts.

## Metadata: all seven named sessions match

All seven official session links, titles, dates, times, rooms, and named speaker/company combinations match the saved official records. All are Tuesday, October 13, 2026. The first four are in Simons; system failures and Contour are in Turing; Kepler is in Shannon.

- Vault: Aaron Linsky and Sam Green — Bridgewater.
- Safety: John Feminella — Two Sigma.
- Code quality: Max Kanat-Alexander — Capital One.
- AI engineering: Aparna Dhinakaran — Arize AI.
- System evals: Vishal Srivastava — New York Life Insurance; Tanmay Sah's company is blank in the official record. Do not give both presenters the New York Life affiliation or present the research as an adopted New York Life control framework.
- Proving Alpha: Hari Kumar — Contour Asset Management.
- Numbers: Vinoo Ganesh — Kepler. This is a vendor account, not evidence of adoption by a named investment institution.

The ending “Everyone has AI: how to have advantage” block has **no title, speaker, company, time, or source link**. Keep it as unattributed attendee synthesis until its origin is identified; do not assign it to the preceding Kepler talk by proximity.

## Evidence and maturity boundaries

Every named note labels its strongest evidence **Speaker claim**. Preserve that status: attendance is evidence of what a speaker described, not independent verification of deployment quality or benefits. Template labels and prefilled questions are not extra observations.

- **Bridgewater:** both notes and official abstract support speaker-reported production of Vault/PAT. New activity-feed/investor-workbench/proactive features are described in the notes, but the notes do not establish their individual rollout scope, adoption, quality, or impact. Do not transfer PAT's established production label to every new feature.
- **Two Sigma:** the attendee labels the material production, and records an agent registry, risk scoring, access declarations/enforcement, common evaluations, and approval triage. The official abstract supports approaches used internally but does not independently establish coverage or maturity of each listed control. Safe wording: “Feminella described Two Sigma's control approach; the attendee recorded it as production use.” No measured safety improvement or negligible utility impact was captured. An independent classifier is not established as deterministic, perfectly calibrated, or a replacement for accountable human oversight.
- **Capital One:** principles/conceptual framing, maturity unclear. Do not attribute a disposable-software deployment or a company-wide policy to Capital One from this talk.
- **Arize:** vendor product/development-loop discussion, maturity unclear in notes. Do not turn trace analysis and suggested improvement opportunities into evidence of autonomous, production-proven remediation. The recorded skill name `arise-evaluator` may be a spelling error; keep it “as recorded / verify exact name” until slides or documentation are inspected. Do not publish an installation command from this note.
- **System evals:** research/framework, not evidence that New York Life deploys the formula or process. The official abstract names 1,368 documented failures, but the notes do not provide a study protocol or independent results.
- **Contour:** attendee maturity is unclear. The program separately reports daily-used research workflows and an implemented logging/attribution process, which may be cited as program context. The notes do not establish that the particular A/B pipeline, manual-idea workflow, or every metric listed is a fully deployed company-wide system.
- **Kepler:** attendee maturity is unclear; the program describes a built AI analyst. Detailed registry, repair, filtering, and retrieval mechanics are notes of the presentation. No production scale, acceptance rate, error rate, security result, latency, or comparative benefit was captured for this specific pipeline.

## Formal equation: retain as a recorded conceptual decomposition

The supplied note records:

`E(loss) = P(fail) × P(reach | fail) × P(miss | reach) × severity`

Label this **“conceptual risk decomposition, as recorded by the attendee; definitions and exact slide notation unverified.”** It is not yet an operational expected-loss estimator or an exact general probability identity.

Material limitations:

1. Define the unit of analysis and time/exposure horizon: one task, one incident, one user, or a deployed system over a period. Define “reach,” “miss,” and “severity,” including whether “miss” means failure of prevention, detection, or intervention.
2. The conditional chain may require `P(miss | reach, fail)` rather than `P(miss | reach)`, unless “reach” already entails the original failure. The notes do not establish that relationship. Do not silently “correct” the speaker's formula without the slide.
3. Multiplying by one severity assumes a fixed loss for the selected path. If loss varies across outcomes, an expected-loss calculation needs the appropriate conditional average loss and/or a sum over mutually exclusive paths. Consequences, recovery, and losses outside the selected missed-control path also need treatment.
4. The product does not authorize multiplying unrelated marginal rates or assuming independence. Estimating these conditional terms requires consistent denominators and evidence about controls and exposure.
5. No probabilities, currency amounts, calibration, uncertainty, or validation are supplied. Do not produce numerical expected losses, compare firms, or claim risk reduction from this schematic alone.

A useful report takeaway can still be stated qualitatively: evaluate how technical failure can propagate through exposure and failed controls into consequence, rather than measuring task completion alone. The official abstract supports that qualitative system perspective.

## Statistical and ROI claims that must remain unverified

- **“AI failures grow exponentially.”** No time series, observation window, growth model, exposure denominator, incident-selection process, or detection/reporting adjustment is recorded. Do not present exponential growth as an established finding. Safe alternative: “The attendee recorded a speaker warning about increasing failures; the quantitative trend was not captured.”
- **“System design fails the most”; human mediation/harm detection has the largest impact but lowest frequency.** The underlying chart, categories, denominators, sample construction, severity scale, uncertainty, and exact comparisons are absent. Keep these as qualitative observations from the presentation, explicitly requiring the study/slide, or omit the rankings. Documented incident counts are not population failure rates, and frequency is not causal importance.
- **1,368** is the official session title/sample claim, not a count independently checked by the attendee. The saved abstract's 92% figure is not in the supplied notes; if used, attribute it separately to the official abstract and retain methodology caveats.
- **Risk-based versus frequency-based evaluation** is a design recommendation, not proof that frequently occurring failures can be ignored. A careful synthesis considers both likelihood/exposure and consequence.
- **Contour “A/B testing.”** The notes capture a comparison over three months, but do not establish randomization, simultaneous controls, sample size, treatment assignment, crossover, blinding, power, or causal identification. Call it a “described with/without-AI measurement pipeline” unless its experimental design is verified. Do not claim demonstrated alpha, P&L uplift, or ROI.
- **Contour “tracking 3 months.”** Retain as a speaker's reported observation window, not a general minimum duration or sufficient validation period. Investment attribution also depends on selection, market conditions, timing, and other process changes.
- **“Studies show leading companies have fewer AI use cases and concentrate investment.”** The final block provides no study, definition of “leading,” comparison, or sample. Do not state this as research-backed. It may be labeled an unattributed hypothesis about focused investment, with the alleged study pending.
- **“Intelligence is becoming cheap; judgment is scarce.”** Treat as a strategic viewpoint, not a measured market-price or labor-market finding.
- No numeric effect size, baseline, quality gain, time saving, business benefit, or financial return was captured in these notes. The report should not manufacture one from the talk titles or examples.

## Numeric settings and mechanical details: preserve as recorded

Kepler retrieval notes capture **3× overfetch**, **100 per namespace**, **maximum 5 per document**, and **top 20 documents “for earning.”** These are reported implementation settings, not recommended defaults or established optimal parameters.

- “3×” lacks a clear reference quantity.
- “100 per namespace” lacks a clear unit and stage: documents, chunks, or candidates; per query or total.
- “max 5 per doc” lacks an explicit item type.
- “top 20 docs for earning” is ambiguous; it may refer to an earnings workload, but do not resolve the typo into a universal pipeline limit without evidence.
- No corpus/task comparison, parameter sweep, recall/precision, latency, or cost results support generalizing these values.
- Keep **three months** in Contour as a separate measurement-window observation, not a parameter for all ROI studies.

The registry/verification account supports a useful design pattern: retrieve evidence, compute using code, bind typed facts to source metadata, repair citation formatting where appropriate, and reject unsupported citations. However, the notes do not establish a fully ordered reference architecture: “preprocessing filter” and “post-processing citation filter” are both recorded. Describe components unless the exact sequence is confirmed.

“Deterministic model handles every facts” is ambiguous. Do not convert it into “all facts are deterministically verified” or a guarantee of no hallucinations. Matching a value or repairing a citation does not alone establish the correct entity, period, unit, currency, restatement, context, or entailment. Those properties appear in the note's **prefilled question**, with no recorded answer. Likewise, no recorded answer establishes how verification failure leads to abstention, repair, or escalation in every case.

## Other important ambiguities and report-writing treatment

- **Bridgewater direction conflict:** the first takeaway says reactive → proactive; “Latest capabilities” says proactive → reactive. The described feeds/“What am I missing?” surface suggests proactive attention steering, but do not silently attribute a corrected directional quote. Write “The notes describe activity feeds and evidence-backed summaries intended to steer attention,” and flag the direction for confirmation.
- **Human precision versus agent recall:** useful workload heuristic, not a universal law. Do not imply agents can ignore precision or humans never need broad recall. The notes have no measured retrieval tradeoff or quality improvement.
- **“Precision is bad; let's benchmark”** records a challenge/intention, not benchmark results. Ontology dimensions, filtering, and vector search are components mentioned, not evidence of solved precision.
- **Disposable software:** “replaceable in hours,” “depended on by a few,” and “maintenance unimportant” are the speaker's conceptual contrast. They do not establish zero management cost or license a lower bar for permissions, data handling, correctness, or consequential outcomes. The user placed “nearly zero” in the decision/question field; do not promote it into a proven economic result.
- **Contour “manual idea agent”** is unclear. Do not silently change it into an autonomous investment agent, a managed-agent product, or a particular tool name. The official abstract supports logged ideas, sources, utility, PM/position progression, and benchmarks; distinguish that program context from unclear live notes.
- Trading/order history/execution, operations/process reliability, and finance/query/reconciliation are listed examples in the Contour note. They do not establish separate deployed products or validated metrics in each domain.
- **RDs** is not expanded in the source. Do not guess the organizational role. The user's Socrates/text-to-SQL and meeting-prep questions are proposed applications, not evidence of either speaker or firm deployments.
- Empty decision, failure, hypothesis, and follow-up sections signal missing capture, not absence of risk or controls. Prefilled questions that remain unanswered must stay open questions.
- No slides, repository, published method, benchmark artifact, screenshot, or exact transcript was attached. Quotes and product/skill spellings are attendee recollections/as-recorded text, not source-verified quotations.

## Suggested evidence note for the final synthesis

“Based on attendee notes from seven Day 1 talks, cross-checked against the official program for session metadata. Technical details and company practices are speaker-reported unless explicitly stated otherwise. Numeric settings are examples as recorded; study, deployment, and ROI claims have not been independently validated. Open questions and personal applications are kept separate from observed content.”
