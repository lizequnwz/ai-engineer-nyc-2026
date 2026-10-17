<!-- ppt-master-schema: design-spec/v1 -->
# AI Engineer Application Demo - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | ai-engineer-application-demo |
| Canvas Format | ppt169 — 1280 × 720 |
| Page Count | 28 — 24 core and 4 reference pages |
| Primary Language | en-US |
| Target Audience | Data scientists, AI engineers and technical leads; presenter is a Principal Data Scientist at Fidelity Investments |
| Communication Intent | Explain conference mechanisms, apply them to the two application tracks, teach the important correctness distinctions, and align on measurable next-release decisions |
| Desired Audience Outcome | Peers can explain why each improvement matters, recognize the failure examples and select a bounded next increment with an acceptance test |
| Core Message / Ask / Action | Fidelity should become a conversational sales-data assistant around the existing SQL engine; the personal agent should extend its evidence guarantees and deliver one workspace-to-checked-result journey |
| Delivery Context | Technical presenter-led briefing of 40 minutes plus discussion, with independent close reading equally supported by visible explanations |
| Artifact Afterlife | Editable PowerPoint for team review, knowledge sharing, implementation planning and later reference |
| Reading Mode | text |
| Content Strategy | Balanced adaptation of the application-roadmap report; preserve all material claims, proposed status, source limits and synthetic labels while reorganizing for a presentation |
| Design Style | Evidence to Action — editorial consulting with disciplined alignment and practical technical diagrams |
| AI Image Acquisition Path | not applicable — no prepared images |
| Generation Mode | continuous |
| Spec Refinement | disabled — optional full-spec review offered; no opt-in requested |
| Speaker Notes | enabled — workflow default, retained earlier present-and-review requirement |
| Custom Animations | disabled — final delegated design policy; static figures convey the complete state |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-10-17 |

Theme choice is delegated by the user’s request to choose appropriate themes. The communication audience, English, 40-minute format and self-contained learning depth are retained from the earlier explicit confirmations. No UI receipts are fabricated. Three complete direction intents were considered: Evidence to Action (conclusion-led, light editorial, Cambria/Arial contrast), Operating Blueprint (instruction-led, dark schematic, Segoe UI concord with code annotations), and Decision Notebook (case-led narrative, warm editorial, Georgia/Arial). Evidence to Action is selected because its close-reading hierarchy best fits the user's explicit preference for substantive consulting-style slides. All use no prepared images; their unused rendering candidates are respectively minimalist-swiss, blueprint and editorial.

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 48 px left/right and 40 px top/bottom; footer is kept separate from body |
| Content Area | x=48..1232, y=40..680 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: pyramid, instructional
- **Mode Behavior**: State each recommendation as an assertion, support it with the actual baseline or mechanism, teach a worked example where necessary, and close each track with an observable next decision. Keep definitions and failure distinctions explicit for independent reading.
- **Visual style**: custom
- **Visual Style References**: swiss-minimal, editorial
- **Visual Style Behavior**: Use rigorous alignment and purposeful large fields to organize the argument, combined with editorial title/lead/body hierarchy and restrained rules. Dense prose, evidence tables, contrasts and diagrams carry the content; Cambria headlines contrast with neutral Arial explanation. Use navy fields for real structural anchors and teal for meaningful emphasis; vary page-level geometry according to the content.
- **Theme**: Evidence to Action. A restrained evidence rail can connect an observed fact to an application and its acceptance test; its recurrence expresses traceability rather than decoration.
- **Tone**: analytical, practical, specific and candid about what is proposed or demonstrated.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFDF7 | Warm-white reading field |
| Secondary background | #E7F0EA | Quiet evidence and comparison surfaces |
| Primary | #102E3A | Structural anchors and dark panels |
| Accent | #075E52 | Key assertions and selected paths |
| Secondary accent | #D5EF8C | Emphasis on dark structural pages |
| Body text | #132F3B | Main reading text |
| Secondary text | #50616A | Captions and footnotes |
| Divider | #CBD4D1 | Structural rules |
| Surface | #F1F4EE | Table and note backing |
| Grid | #DEE5DE | Light internal cell rules |
| Positive | #075E52 | Accepted or supported behavior |
| Warning | #8B411C | Missing evidence and required clarification |
| Negative | #9B3025 | Deliberately wrong synthetic results and critical defects |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Editorial serif, decisive assertion | Cambria | | serif |
| Body | Neutral readable sans | Arial | | sans-serif |
| Code | Exact implementation and state identifiers | Consolas | | monospace |

- **Title stack**: Cambria
- **Body stack**: Arial
- **Code stack**: Consolas
- **Role rationale**: Code is a recurring distinct family for implementation anchors and explicit identifiers; it never replaces explanatory prose.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 20 |
| Title | 36 |
| Subtitle | 24 |
| Lead | 22 |
| Annotation | 18 |
| Footnote | 12 |
| Display | 64 |
| Kicker | 16 |
| Code | 16 |

All text is editable and names PowerPoint-safe faces; the target is standard Microsoft PowerPoint. Body is read-close, consistent with the user's request for fuller explanations rather than an illustration-only deck.

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: Assertion first, short explanatory lead next, then the page-specific evidence or mechanism and its practical implication.
- **Composition tendency**: Let a comparison, sequence, ownership boundary or work artifact define the page; use columns where they help comparison and prose where reasoning needs continuity.
- **Cross-page continuity**: Repeat an understated evidence-to-decision rail where it strengthens traceability; section anchors reset the reader between Fidelity and personal-project work.
- **Spacing posture**: Information-rich, varying density by page job; the cover and conclusion have genuine lower-density orientation roles.
- **Spacing anchors**: page_margin=48; block_gap=20; column_gutter=32; corner_radius=0; body_leading=28

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P08 | table | comparison_matrix | Compare the page’s stated rows and columns; native editable grid |
| P09 | table | record_table | Compare the page’s stated rows and columns; native editable grid |
| P10 | table | comparison_matrix | Compare the page’s stated rows and columns; native editable grid |
| P11 | table | comparison_matrix | Compare the page’s stated rows and columns; native editable grid |
| P17 | table | comparison_matrix | Compare the page’s stated rows and columns; native editable grid |
| P22 | table | comparison_matrix | Compare the page’s stated rows and columns; native editable grid |
| P25 | table | comparison_matrix | Compare the page’s stated rows and columns; native editable grid |
| P26 | table | record_table | Compare the page’s stated rows and columns; native editable grid |
| P27 | table | record_table | Compare the page’s stated rows and columns; native editable grid |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

The complete roster review selected no prepared-image job: the subject is a proposed operating model, bounded analytical examples and implementation decisions. Company names are source attributions, not documentary subjects needing likeness. Diagrams, tables, quantitative labels and explanatory text carry the required information as editable page content; no factual CRM screenshot is invented.

## IX. Content Outline

### Part 1: Recommendation and transfer

#### Slide 01 - From queries to accepted work

- **Audience move**: Understand the shared goal → recognize two distinct application tracks.
- **Relationships**: membership: Fidelity sales-data work and personal analytical work share accepted completion as the governing outcome.
- **Composition**: One dominant promise with a two-track route beneath it.
- **Title**: From queries to accepted work
- **Core message**: Adopt two focused release paths: a conversational sales-data assistant for Fidelity and stronger evidence guarantees for the personal analytics agent.
- **Content**:
  - Cover hook: From queries to accepted work. Full subtitle: Conference lessons applied to Fidelity institutional sales and a personal analytics workspace.
  - For data scientists, AI engineers and technical leads; 40-minute technical briefing plus discussion.
  - Carry enough explanation on pages for independent reading; notes add delivery context.
- **Cover impact**: Binding hook: From queries to accepted work. Reference: make the shared outcome dominant and the two application tracks easy to distinguish.

#### Slide 02 - Two release paths turn the conference into practical decisions

- **Audience move**: Broad AI ambition → two concrete next-release choices.
- **Relationships**: contrast: the one-shot Fidelity system and the existing multi-step personal agent need different next investments.
- **Composition**: Two asymmetric workstreams with an explicit shared acceptance test.
- **Title**: Two release paths turn the conference into practical decisions
- **Core message**: Start Fidelity with discovery, relevant semantics and stronger evaluation; extend the personal agent through precise correctness and evidence contracts.
- **Content**:
  - Fidelity: grounded definitions and data navigation; question-scoped semantics; conversation; bounded complex questions; a measured CRM preparation journey.
  - Personal agent: count/forecast correctness; bound narrative numbers; preserved metric/grain meaning; outcome oracles; one workspace-to-checked-result journey.
  - Every release compares accepted work, total human effort, full known cost and consequential failure modes against the existing process.

#### Slide 03 - Six company mechanisms translate into reusable engineering practices

- **Audience move**: Recall talks → connect mechanisms to application decisions.
- **Relationships**: membership: Bridgewater, Kepler, Range, Ramp, Two Sigma/Wise and Contour illustrate complementary practices.
- **Composition**: A shared accepted-work focal point surrounded by six specific engineering contributions.
- **Title**: Six company mechanisms translate into reusable engineering practices
- **Core message**: Use company stories to choose a mechanism and an experiment; reported implementations alone do not establish local benefits.
- **Content**:
  - Bridgewater: task-specific knowledge and time scoping → relevant evidence packages and concise human briefs.
  - Kepler: typed facts, code-based arithmetic and citation checks → meaning and lineage attached to each material number.
  - Range: expert-authored skills → sales/domain specialists encode reasons, questions and exceptions.
  - Ramp: end-to-end tasks and ablations → compare one context, skill, memory or model change at a time.
  - Two Sigma/Wise: ownership and authority → scoped tools and explicit permission to act.
  - Contour: useful work and the credible alternative → acceptance, review effort and full cost; no measured ROI is inferred.

### Part 2: Fidelity applications

#### Slide 04 - The current Fidelity bottleneck spans usability, context and evaluation

- **Audience move**: View latency as the only issue → see the complete product baseline.
- **Relationships**: membership: generation, semantic context, evaluation and CRM workflow are four current constraints.
- **Composition**: Two reported figures as a focal band with four explanatory baseline blocks.
- **Title**: The current Fidelity bottleneck spans usability, context and evaluation
- **Core message**: The reported baseline is a one-shot SQL system with large semantic input and an incomplete understanding of workflow value.
- **Content**:
  - Current architecture: a lightweight LLM intent classifier plus a text-to-SQL generation model; complex questions are also one shot; no conversation or memory.
  - 20–30K tokens of table/column semantics supplied each time; roughly 30–45 seconds of SQL-model latency before additional intent/data execution time. These are user-reported figures, not measured p50/p95.
  - Current evaluation: generated/reference row-count comparison plus an LLM comparison of returned data.
  - Salesforce integration is underway; its effect on sales preparation and daily workflow is not yet established. Fidelity code/data were not inspected.

#### Slide 05 - A shared semantic coordinator can support the complete business question

- **Audience move**: Think in two independent models → understand shared definitions and task routing.
- **Relationships**: order: question and CRM context feed scoped semantic discovery, then explanation/clarification/query/investigation, then checked output.
- **Composition**: An explicit current-to-proposed system contrast with one shared semantic foundation.
- **Title**: A shared semantic coordinator can support the complete business question
- **Core message**: Evolve the intent front door while retaining the current SQL generator as a bounded analytical tool.
- **Content**:
  - Input: user question, authorized CRM entity context and compact session state.
  - Coordinator capabilities: explain a definition; reveal supported data; clarify ambiguity; request a simple query; plan a bounded investigation.
  - Shared reviewed semantics carry entity meaning, metrics, dates, grain, required joins and catalog version. Filter metadata by authorized role/resource before context assembly; recheck permissions at execution.
  - Return the result with its source scope and useful next step. This is a proposed architecture, not the current implementation.

#### Slide 06 - Definitions and data discovery are useful tasks in their own right

- **Audience move**: See a rejected definition request → recognize the helpful metadata path.
- **Relationships**: order: a term question leads to reviewed matches, ambiguity resolution and a sourced explanation; supported examples enable a next question.
- **Composition**: An illustrative conversation paired with the required discovery behavior.
- **Title**: Definitions and data discovery are useful tasks in their own right
- **Core message**: A business-data assistant should help users learn what it can answer before requiring a fully formed SQL question.
- **Content**:
  - Example user question: What is the meaning of live? Its actual business definition is unknown in this review.
  - Look up the authoritative glossary/catalog. Explain matching definitions or ask which meaning applies; never invent the meaning.
  - Offer What can I ask?, topic browsing, supported example questions and explanations of unavailable data.
  - Definition-only questions need metadata rather than source SQL. Measure correctness, helpful discovery, useful next questions and time to a useful response.

#### Slide 07 - Select definitions by business role, then close their dependencies

- **Audience move**: Assume retrieval means top-k columns → recognize dependency-complete context.
- **Relationships**: order: authorized metadata boundary precedes role candidates; selected measures narrow dates/dimensions; required relationships complete the package.
- **Composition**: A role-based retrieval and dependency diagram with an authorized-scope boundary.
- **Title**: Select definitions by business role, then close their dependencies
- **Core message**: A semantic package must include what makes the requested measure valid, rather than only similar column names.
- **Content**:
  - Retrieve candidate measure, dimension, filter, entity and time roles.
  - For chosen measures, include reviewed definitions, denominators, physical mappings, date rules, keys, cardinality and required join routes.
  - Preserve ambiguity and missing definitions. A near match does not establish question coverage.
  - Reuse versioned catalog metadata while refreshing source data independently. Validate required-definition/join coverage and final result correctness as context is reduced.

#### Slide 08 - Test semantic context reduction before attributing a latency gain

- **Audience move**: Assume fewer tokens means better performance → design a quality-qualified comparison.
- **Relationships**: contrast: full and selected semantics differ only in context selection; the same model, cases, settings and frozen inputs are held fixed.
- **Composition**: A comparison matrix above a stage-by-stage latency measurement strip.
- **Title**: Test semantic context reduction before attributing a latency gain
- **Core message**: Use one sales domain and an isolated comparison to determine whether a smaller package improves the full task.
- **Content**:
  - Baseline: current full semantics, reported 20–30K tokens. Candidate: role-selected, dependency-complete semantics; token size and latency are measured, not promised.
  - Hold model, behavior, question set, source snapshot and evaluation contract fixed.
  - Measure retrieval, routing, model generation, validation/database and total p50/p95 time, alongside context coverage and result correctness.
  - Run one-shot versus bounded repair as a separate later comparison. Input tokens may contribute to latency; inspect the stage timings before assigning causality.
- **Visualization**: table/comparison_matrix; keyed independent table objects: context-study.
- **Native-ready**: context-study=yes

#### Slide 09 - Equal row counts can conceal the wrong advisor result

- **Audience move**: Trust cardinality → detect a same-cardinality semantic failure.
- **Relationships**: contrast: the reference advisor result and a deliberately wrong candidate both contain one record, while their net-flow values have different entity meaning.
- **Composition**: Two small result tables with a decisive scope explanation.
- **Title**: Equal row counts can conceal the wrong advisor result
- **Core message**: Full typed-result and business-scope checks must distinguish a correct advisor number from a mislabeled firm aggregate.
- **Content**:
  - Synthetic case: A17, product P-A; purchases $0.8m and redemptions $1.0m produce advisor net flow −$0.2m.
  - Firm net flow is +$5.0m for a different aggregation scope. Illustrative bad candidate: label the firm figure as advisor A17 while retaining one row.
  - Row-count agreement alone passes the cardinality check; keyed values, measure definition and entity/grain checks expose the defect.
  - All identifiers, values and product labels are invented. Negative advisor flow does not establish dissatisfaction or competitor displacement.
- **Visualization**: table/record_table; keyed independent table objects: reference-result, candidate-result.
- **Native-ready**: reference-result=yes; candidate-result=yes
- **Data class**: scenario — all A17, P-A, $0.8m, $1.0m, −$0.2m and +$5.0m values, labels and wrong-candidate examples are invented teaching data.

#### Slide 10 - A layered evaluation contract separates execution from accepted work

- **Audience move**: Use one accuracy label → distinguish five acceptance dimensions.
- **Relationships**: order: execution, typed result, business meaning, conversation and useful sales work provide separate evidence toward acceptance.
- **Composition**: A five-layer comparison matrix plus a reference/judge calibration conclusion.
- **Title**: A layered evaluation contract separates execution from accepted work
- **Core message**: Keep result, interpretation, conversation and workflow judgments independently inspectable.
- **Content**:
  - Execution: valid SQL within source permissions and limits.
  - Result: compare complete keyed rows or multisets; preserve duplicates and NULLs; define ordering, top-k ties and column-specific tolerances in advance.
  - Business meaning: entity, measure, grain, denominator, date role, period, units and coverage.
  - Conversation: definitions, discovery, clarification, state updates and refresh. Workflow: factual support, useful omissions/questions, approved material and rep effort.
  - Freeze data/as-of and independently review reference SQL; permit alternative correct implementations. Calibrate LLM semantic judgments against adjudicated expert cases.
- **Visualization**: table/comparison_matrix; keyed independent table objects: evaluation-layers.
- **Native-ready**: evaluation-layers=yes

#### Slide 11 - Conversation state should preserve scope while making changes explicit

- **Audience move**: Treat memory as chat accumulation → use explicit, correctable task state.
- **Relationships**: contrast: a last-quarter follow-up changes the period while preserving the intended entity, measure and filters; conversation state, reviewed knowledge and saved data have distinct roles.
- **Composition**: A before/follow-up state table with three memory responsibilities beneath it.
- **Title**: Conversation state should preserve scope while making changes explicit
- **Core message**: A follow-up changes the requested part of the task; saved history does not make stale data current.
- **Content**:
  - Persist resolved advisor/office/firm IDs, metric, grouping, filters, time window, information cutoff, semantic version, saved result IDs and unresolved questions.
  - Example: What about last quarter? Change the period and preserve the other intended scope. A new advisor or measure requires explicit state updates.
  - Separate session context, reviewed business knowledge and saved data; show active scope and permit correction/reset.
  - Measure multi-turn completion, scope carryover, clarification, freshness and cross-advisor leakage.
- **Visualization**: table/comparison_matrix; keyed independent table objects: session-state.
- **Native-ready**: session-state=yes

#### Slide 12 - Bounded investigation can make complex questions inspectable

- **Audience move**: Expect one large query → understand controlled multi-step analysis.
- **Relationships**: order: resolve comparison, retrieve advisor change, calculate product contributions, reconcile and explain; validation feedback may lead to a bounded repair.
- **Composition**: A five-step analytical path with a clearly limited feedback loop.
- **Title**: Bounded investigation can make complex questions inspectable
- **Core message**: Give a difficult task an explicit decomposition, reconciliation and time/attempt budget.
- **Content**:
  - Question: Which advisors’ net flows fell, and which product families contributed?
  - Resolve measure and window; retrieve advisor-level change; calculate contributions at compatible grain; reconcile to the total; explain supported findings and uncertainty.
  - Use actual schema/execution/validation feedback for repair. Define attempts and total time in advance; keep all attempts; finish with an unresolved/clarification outcome when needed.
  - Held-out reference answers never become runtime hints. Check permissions and scope every step. Arithmetic contribution does not establish a causal driver.

#### Slide 13 - Meeting prep should produce a rep-reviewed advisor-sales packet

- **Audience move**: Think of a generated summary → define an accepted sales work product.
- **Relationships**: order: meeting objective and evidence inform observed changes, commercial hypotheses, discovery questions and material selection; the rep reviews the packet.
- **Composition**: Four question-led zones with a common evidence and review foundation.
- **Title**: Meeting prep should produce a rep-reviewed advisor-sales packet
- **Core message**: The useful output helps the salesperson decide why to meet, what changed, what to ask and which material to bring.
- **Content**:
  - End user: a Fidelity institutional salesperson serving advisors as distribution partners.
  - Why meet? Objective, resolved advisor identity and prior commitments. What changed? Relevant activity since the last interaction.
  - What to ask? Labeled commercial hypotheses and questions to validate them. What to bring? Correct current product/share-class material and unresolved requirements.
  - Numbers preserve entity, metric, period, units, snapshot and calculation. Historical scope uses effective-dated relationships; Fidelity activity does not imply the advisor’s whole wallet.

#### Slide 14 - The synthetic A17 brief separates facts from commercial interpretation

- **Audience move**: Read a sales claim as a fact → inspect facts, hypotheses and reviewer decisions.
- **Relationships**: order: scoped activity and a meeting request support a commercial hypothesis and discovery questions; reviewer acceptance closes preparation.
- **Composition**: A realistic schematic brief with a facts spine and a separate decision area.
- **Title**: The synthetic A17 brief separates facts from commercial interpretation
- **Core message**: Preserve the advisor/firm distinction and turn plausible interpretations into questions the rep can validate.
- **Content**:
  - Entirely synthetic: advisor A17 / product P-A; purchases $0.8m, redemptions $1.0m, net flow −$0.2m. Firm aggregate: +$5.0m.
  - A prior meeting record asks for share-class and implementation discussion.
  - Fact: advisor activity and the documented request. Hypothesis: a focused approved comparison may advance this conversation.
  - Ask which implementation constraints matter; confirm exact product/share-class, document version, approval context and valid time. Rep reviews and adjusts before use; draft acceptance does not grant authority for an outbound action.
- **Data class**: scenario — all A17, P-A, $0.8m, $1.0m, −$0.2m and +$5.0m values, labels and wrong-candidate examples are invented teaching data.

#### Slide 15 - Sales specialists can encode the preparation method as a maintained skill

- **Audience move**: Treat instructions as a prompt → recognize a reviewed professional method.
- **Relationships**: order: Pick, Teach, Pack, Test and Ship form the skill-development sequence; ownership and review maintain it.
- **Composition**: A five-stage method with concrete sales activities under each stage.
- **Title**: Sales specialists can encode the preparation method as a maintained skill
- **Core message**: Transfer Range’s expert-authored process into the sales domain, including reasons and exceptions.
- **Content**:
  - Pick one repeated preparation workflow with recognizable acceptance. Teach why a salesperson/product specialist takes each step.
  - Pack required facts, definitions, authorized sources, clarification questions and action limits. Missing information changes the workflow.
  - Test ordinary, ambiguous and consequential failure cases. Ship with an owner, reviewer and change history; retest revisions.
  - Range’s planning use case provides the method; the sales workflow is a proposed adaptation. No net capacity gain is inferred.

#### Slide 16 - Measure the complete Salesforce job before expanding the experience

- **Audience move**: Equate integration with value → identify an observable job and baseline.
- **Relationships**: order: observe existing work, select a job, deliver a scoped packet, compare preparation/review and follow-through; later business effects require separate attribution.
- **Composition**: A rep journey above a paired pilot evidence panel.
- **Title**: Measure the complete Salesforce job before expanding the experience
- **Core message**: Workflow observation reveals where preparation, checking and follow-through can improve.
- **Content**:
  - Observe where reps start, copy information, consult colleagues, verify claims and act after meetings.
  - Select one job such as preparing for an identified advisor meeting; make the brief available in that record’s context.
  - Compare similar existing/assisted cases and counterbalance preparation order where feasible to reduce learning effects.
  - Measure time to accepted brief, preparation/review/rework, useful questions, relevant omissions, return use and completed follow-through. Qualified opportunities and sales effects are separate outcome questions.

#### Slide 17 - Three increments keep the Fidelity roadmap measurable

- **Audience move**: See a feature backlog → understand release dependencies and decision gates.
- **Relationships**: order: baseline/first slice precedes the next working release and controlled expansion; workflow observation starts in the first increment.
- **Composition**: A three-increment matrix with a decision gate for each.
- **Title**: Three increments keep the Fidelity roadmap measurable
- **Core message**: Ship discovery/context first, then correct follow-ups, then one controlled complex-question and preparation journey.
- **Content**:
  - First slice: observe CRM tasks, strengthen result grading, select one sales domain and definition/discovery examples.
  - Next working release: glossary/data navigation and selected semantics; then explicit session state and follow-up checks. Isolate their effects.
  - Controlled expansion: one bounded complex-question workflow and one rep-reviewed meeting packet; pilot the complete journey.
  - These are release increments, not fixed 30/60/90-day promises. Continue when quality, scope and total effort support the next step.
- **Visualization**: table/comparison_matrix; keyed independent table objects: release-increments.
- **Native-ready**: release-increments=yes

### Part 3: Personal analytics agent

#### Slide 18 - The personal analytics agent already has a strong operating foundation

- **Audience move**: Expect a greenfield agent → see the implemented foundation and planned workspace frontier.
- **Relationships**: membership: coordinator, SQL and Python specialists own distinct work; saved evidence connects analysis, charts and reports; workspace tools are planned.
- **Composition**: A system map that marks existing capabilities and the next workspace boundary.
- **Title**: The personal analytics agent already has a strong operating foundation
- **Core message**: Extend the existing ownership, evidence and evaluation paths instead of creating a duplicate framework.
- **Content**:
  - Oct 15 read-only repository review: semantic discovery; SQL-owned warehouse access; Python over named saved data; immutable scope and report revisions.
  - Existing strengths: typed complete datasets, lineage, deterministic comparisons, persistent artifacts, Stop/Resume, retry and portable replay.
  - Paired evaluation already freezes receipts/fingerprints and protects boundary and first-attempt outcomes.
  - Broader project reading/search/authoring remains the selected planned direction. This deck does not report a new implementation or fresh model evaluation.

#### Slide 19 - Make counted populations and completed analyses explicit contracts

- **Audience move**: Accept execution success → require the evidence appropriate to the task.
- **Relationships**: membership: count grain, forecast completion and typed empty results are three code-backed boundary opportunities.
- **Composition**: Three engineering issue-and-acceptance units tied to exact implementation anchors.
- **Title**: Make counted populations and completed analyses explicit contracts
- **Core message**: Close small correctness boundaries before using stronger claims about analytical completion.
- **Content**:
  - Counts: canonical metric selection is optional and the general fanout guard iterates SUM/AVG. Require counted population/measure meaning for KPIs; test counts, distinct counts, denominators and many-side joins.
  - Forecasts: completed analysis requires successful execution, while the forecast descriptor is optional. Require saved predictions and the existing evaluation contract, or a supported partial outcome.
  - Empty/all-null Snowflake results: preserve declared types rather than inferring only from values. Keep valid custom extracts available.
  - Acceptance is demonstrated with targeted fixtures; these are code-review opportunities, not reproduced production incidents.

#### Slide 20 - Bind quantitative narrative to the same saved facts as metric cards

- **Audience move**: Trust a rendered report → inspect every material quantitative appearance.
- **Relationships**: link: a typed saved fact supplies metric card, lead and callout; declared units and checked transformations travel with it.
- **Composition**: A central bound fact feeding several editable report elements with a consistency check.
- **Title**: Bind quantitative narrative to the same saved facts as metric cards
- **Core message**: A correct table and an inconsistent sentence can coexist unless the report contract resolves both from evidence.
- **Content**:
  - Current report cards resolve stored values; narrative/callout bodies and infographic values remain strings. Ordinary cards also accept free-form prefix/suffix units.
  - Extend the declarative report contract with typed numeric spans in headlines, leads, callouts and infographic values. Reuse saved-cell/comparison resolvers and declared units.
  - Illustrative reuse of the A17 scenario: a bound net-flow value of −$0.2m must remain the same in the card and quantitative sentence; +$5.0m belongs to the firm scope.
  - Acceptance: changing evidence updates bound appearances; wrong/out-of-scope bindings and unsupported currency/percentage labels fail before saving.
- **Data class**: scenario — all A17, P-A, $0.8m, $1.0m, −$0.2m and +$5.0m values, labels and wrong-candidate examples are invented teaching data.

#### Slide 21 - Meaning must survive saved-data transformations and refresh

- **Audience move**: Assume same columns means same data → verify identity and grain.
- **Relationships**: order: source meaning passes through transparent projection or calculation and then refresh; each boundary preserves identity only when justified.
- **Composition**: A data path with separate transformation and refresh gates.
- **Title**: Meaning must survive saved-data transformations and refresh
- **Core message**: Preserved lineage and matching schemas need complementary checks on metric identity and row meaning.
- **Content**:
  - Current source SQL retains canonical metric bindings; saved-SQL reshapes omit that binding. Carry identity through unambiguous projections/renames, not scaled values or changed aggregates.
  - Refresh compares column names/types before copying the old grain description. Validate declared keys, time bucket, aggregation/measure and scope; check full-result key uniqueness.
  - Reject or clarify same-schema daily-to-monthly, duplicate-key or changed-measure refreshes; permit legitimate new values and typed empty results.
  - Keep source completeness unknown when undeclared; snapshot save time and the last transaction do not establish completeness.

#### Slide 22 - Outcome oracles should strengthen the existing paired evaluation harness

- **Audience move**: Treat method words as proof → evaluate the stored outcome.
- **Relationships**: contrast: keyword-based live smoke checks and numerical outcome oracles answer different questions; current paired controls remain valuable.
- **Composition**: An outcome-check matrix with retained harness strengths beneath it.
- **Title**: Outcome oracles should strengthen the existing paired evaluation harness
- **Core message**: Check saved numerical artifacts and final report agreement before trusting correct-sounding methodology.
- **Content**:
  - Broad live analytical checks use words such as holdout and MAE as proxies; the existing harness already freezes receipts, fingerprints and human review.
  - Reuse named Parquet bindings and forecast evaluation for actual predictions, windows, totals, counts and report agreement.
  - Separate development/regression from final assessment by family and exposure record. Add reviewer/rubric identity and an adjudicated defect pack.
  - Extend existing token/active-time diagnostics with reviewer effort and known/estimated cost. Unknown cost remains unknown; measure all attempts per accepted task.
  - Turn accepted failures into regression cases and reviewed skill/definition updates; never automatically promote user corrections to business truth.
- **Visualization**: table/comparison_matrix; keyed independent table objects: outcome-oracles.
- **Native-ready**: outcome-oracles=yes

#### Slide 23 - One workspace journey can join project understanding to checked analysis

- **Audience move**: See broad workspace ambition → identify one complete product slice.
- **Relationships**: order: understand definition, inspect calculation, propose repair, check approved evidence and explain the result; tool permissions constrain each assignment.
- **Composition**: A workspace-to-result journey with current capability boundaries visible.
- **Title**: One workspace journey can join project understanding to checked analysis
- **Core message**: Deliver the selected project-to-result task using the existing stack and explicit source scope.
- **Content**:
  - Example task: find the retention definition, inspect SQL, identify a denominator mistake, propose a patch and reconcile against approved saved evidence.
  - Begin with bounded project reading/search and explicit assignment-level source scope; then add controlled authoring and checks.
  - Keep coordinator, SQL specialist, Python specialist and evidence stores. Workspace text is context; accepted definitions and execution authority remain explicit.
  - The local subprocess has time/output limits but is not an isolation sandbox. Broader shell work requires an execution-isolation design. This is the existing HANDOFF direction, not a delivered capability.
  - Later artifact-quality checks should use a real browser to verify chart execution, disclosures, keyboard behavior, narrow layouts and print output; this is a future validation recommendation, not a claim of performed browser testing.

#### Slide 24 - Choose the next accepted work product and the test that earns expansion

- **Audience move**: Understand opportunities → select immediate actions and decision criteria.
- **Relationships**: membership: Fidelity and personal-project actions share a define/build/check/decide discipline; each track has its own next step.
- **Composition**: A genuine close with two concrete commitments-to-discuss and one shared decision rule.
- **Title**: Choose the next accepted work product and the test that earns expansion
- **Core message**: Make one bounded comparison per track and preserve the evidence behind the next decision.
- **Content**:
  - Fidelity next session: bring representative questions; choose one sales domain; agree entity/metric/date definitions and trusted reference results; instrument stage latency; observe rep preparation.
  - Personal next increments: one targeted count/forecast correctness fixture; one bound quantitative lead/callout; one numerical outcome oracle; then one workspace task.
  - Compare accepted quality, consequential failures, total human effort and full known cost. Record continue, revise or stop with uncertainty visible.
  - Closing takeaway: accepted work is the unit of progress. Owners, timing and thresholds are to be agreed, not assigned by this presentation.
- **Closing impact**: Binding takeaway: accepted work is the unit of progress. Reference: two practical next-step routes converge on a clear decision rule.

### Part 4: Reference material

#### Slide 25 - A compact defect suite tests more than fluent SQL

- **Audience move**: See generic accuracy → select diagnostic negative and positive cases.
- **Relationships**: membership: each named case has an expected behavior and a distinct failure it tests.
- **Composition**: A reference table of cases, expected behavior and failure class.
- **Title**: A compact defect suite tests more than fluent SQL
- **Core message**: Use cases that expose plausible same-cardinality, scope, state and authority failures.
- **Content**:
  - Include same-row-count wrong values; join duplication; wrong advisor hierarchy; wrong date role; ambiguous live; unavailable measure; changed follow-up scope; stale evidence; denied access.
  - Define expected clarification, supported result or refusal per case. A correctly denied action is a control success.
  - Keep reference answers unavailable to runtime repair; independently review references and keep assessment families distinct from tuning.
- **Visualization**: table/comparison_matrix; keyed independent table objects: defect-cases.
- **Native-ready**: defect-cases=yes

#### Slide 26 - An accepted-work scorecard connects quality, time and cost

- **Audience move**: Collect isolated telemetry → report decision-relevant denominators.
- **Relationships**: membership: task acceptance, critical defects, latency, human effort and cost each answer a different operational question.
- **Composition**: A definition table with no fabricated results or targets.
- **Title**: An accepted-work scorecard connects quality, time and cost
- **Core message**: Agree population, acceptance, exclusions and measurement windows before comparing systems.
- **Content**:
  - Acceptance: accepted work over eligible assigned tasks, with rejected/abandoned/excluded outcomes shown.
  - Quality: result equivalence and business-scope correctness; critical failures separate from compensating averages.
  - Time: p50/p95 stage and end-to-end latency; first-correct time for bounded work; active review/rework distinct from waiting.
  - Cost: all known or explicitly estimated attempt/tool/data/review/support costs over accepted tasks. Preserve unknown cost and measure later business effects separately.
- **Visualization**: table/record_table; keyed independent table objects: work-scorecard.
- **Native-ready**: work-scorecard=yes

#### Slide 27 - Implementation anchors make the personal roadmap reviewable

- **Audience move**: Read recommendations → locate the owning implementation boundary.
- **Relationships**: membership: each improvement maps to a specific file and inspected behavior.
- **Composition**: A compact code-reference table organized by improvement.
- **Title**: Implementation anchors make the personal roadmap reviewable
- **Core message**: Use these code paths as the starting points for focused increments; the observations are from the Oct 15 read-only review.
- **Content**:
  - Count grain: semantic_sql.py:312 and agents/text_to_sql/tools.py:93.
  - Forecast completion: agents/data_analysis/tools.py:122. Empty types: backends/snowflake.py:129.
  - Narrative binding and units: reporting/schemas.py:95; reporting/renderer.py:188,260; reporting/comparisons.py:113.
  - Reshape/refresh: agents/text_to_sql/tools.py:223; presentation.py:186,204. Outcome evaluation: tests/test_live_evaluations.py:140; scripts/grade_documented_examples.py:36.
  - Workspace direction and current scope: HANDOFF.md:27,42,56; coordinator.py:137. Repository: data-analytics-agent under the user-supplied path; no implementation or provider study was performed.
- **Visualization**: table/record_table; keyed independent table objects: implementation-anchors.
- **Native-ready**: implementation-anchors=yes

#### Slide 28 - Primary references support the mechanisms and their limits

- **Audience move**: Recognize the argument → locate durable supporting sources.
- **Relationships**: membership: conference sessions, primary technical references and the dated local review support different parts of the deck.
- **Composition**: Two editorial reference columns with native hyperlinks and short usage notes.
- **Title**: Primary references support the mechanisms and their limits
- **Core message**: Follow the company sessions and primary product/evaluation guidance; distinguish source mechanisms from proposed local designs.
- **Content**:
  - Conference: Bridgewater Vault; Kepler Do Not Let Models Invent Numbers; Range financial-planner skills; Ramp end-to-end evals; Contour useful-insight comparisons; full agenda for Two Sigma/Wise context.
  - Primary guidance: Snowflake VQR; Databricks Genie quality tuning; Anthropic agent evals; Snowflake CoCo overview.
  - Fidelity baseline is user-reported; personal implementation claims use the Oct 15 read-only review. Recommendations and all synthetic examples remain labeled; no ROI or speedup is asserted.
- **Hyperlinks**: Bridgewater Vault → https://ai.engineer/nyc/2026/schedule?session=a84ca3a8-cc2f-4b50-a635-fc380f6f04f6; Kepler numbers → https://ai.engineer/nyc/2026/schedule?session=2d29f925-f16b-41b3-8086-de0524829cbe; Range skills → https://ai.engineer/nyc/2026/schedule?session=9b002687-09cf-42e2-9282-532ed9d0c184; Ramp evals → https://ai.engineer/nyc/2026/schedule?session=4607dbbe-8f94-4b0e-91ce-257d1cfb5448; Contour value → https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca; Conference agenda → https://ai.engineer/nyc/2026/schedule; Snowflake VQR → https://docs.snowflake.com/en/user-guide/views-semantic/verified-query-repository; Databricks Genie → https://docs.databricks.com/aws/en/genie-agents/tune-quality; Anthropic evals → https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents; Snowflake CoCo → https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under notes/
- **Content**: Ground the explanation in the final visible page. Add transitions, implementation context and optional discussion prompts without moving required learning off the page. Preserve user-reported baseline status, proposed status and synthetic labels. Reference exact sources and the Oct 15 code review where appropriate.
- **Total duration**: 40 minutes for 24 core slides plus discussion; four reference slides are untimed.
- **Notes style**: Conclusion-led, explanatory and practical, with a patient register for worked examples.
- **Presentation purpose**: Explain conference mechanisms, apply them to the two tracks, teach correctness distinctions and align on measurable next-release decisions.
