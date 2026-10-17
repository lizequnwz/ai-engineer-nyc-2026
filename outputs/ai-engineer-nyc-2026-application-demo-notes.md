# 01_from_queries_to_accepted_work

The practical lesson I want to bring back from AI Engineer is to judge progress by accepted work. A generated query, a tool call and a polished page are intermediate outputs. The question is whether a person can use the resulting work product with a defensible amount of checking. This briefing applies that idea to two different starting points: Fidelity’s institutional sales-data and meeting-preparation applications, and my personal analytics agent. For Fidelity, the opportunity is to help users discover, clarify, investigate and prepare within reviewed definitions. For the personal agent, the opportunity is to connect project understanding to a checked analytical result and a consistent report. These pages contain the reasoning and examples for independent review; the discussion should help us choose the next bounded release rather than agree to a broad agent platform.

---

# 02_two_release_paths

The two applications should not receive the same backlog. Fidelity’s current interaction is predominantly one shot, so the first investments are grounded definitions, data navigation and relevant semantic context. Conversation, bounded investigation and one measured Salesforce preparation journey can then build on that working product. The personal agent already has multi-step specialists and evidence stores; its next investments are more precise count and forecast contracts, quantitative narrative bindings, preservation of metric and grain meaning, and numerical outcome checks. Both tracks should compare the new work product with the existing process on accepted quality, total human effort, full known cost and consequential failure modes. A release can generate more sophisticated behavior while making the user’s total job harder, which is why those dimensions belong together.

---

# 03_company_mechanisms

I have grouped the conference stories by the mechanism we can transfer. Bridgewater’s Vault points toward task-specific knowledge, temporal scoping and concise human briefs. Kepler connects material numbers to typed facts, calculation and citation checks. Range makes the professional method explicit through expert-authored skills, including reasons and exceptions. Ramp’s end-to-end evaluation approach suggests testing one context, skill, memory or model change at a time. The ownership and authority lessons from Two Sigma and Wise support scoped tools and explicit permission to act. Contour brings the analysis back to useful work against a credible alternative, including review effort and cost. This grouping is our synthesis, and a reported company implementation does not establish a speedup or return on investment in our setting. Each mechanism should lead to a local experiment with an observable acceptance test.

---

# 04_fidelity_baseline

The Fidelity baseline comes from the reported experience, not an inspection of application code or production data. There is a lightweight LLM intent classifier and a SQL-generation model, and complex questions also receive a one-shot treatment. Conversation and memory are not supported, and users need help understanding what the data surface contains. Each request supplies roughly twenty to thirty thousand tokens of table and column semantics. The reported thirty to forty-five seconds refers to SQL-model latency; intent handling and data execution add further time, and these figures are not measured median or tail latency. The current accuracy process compares returned row counts and uses an LLM to judge the returned data. Salesforce integration is underway, but the effect on preparation and daily work has not yet been established. That baseline motivates a combined usability, correctness and workflow agenda.

---

# 05_shared_semantic_coordinator

The proposed coordinator expands the task around the existing SQL generator. A user’s question, authorized CRM entity context and compact session state first establish the task. A shared reviewed catalog supplies entity meaning, metrics, dates, grain, join routes and version information. The coordinator can explain a term, reveal supported data, clarify ambiguity, request a simple query or run a bounded investigation. The SQL engine stays a useful analytical tool with a specific responsibility. The result should include its source scope and a useful next step rather than only a returned table. Authorization applies twice: filter metadata before it enters model context, then recheck permissions when executing against the source. This diagram describes a proposed architecture, not the current implementation.

---

# 06_definitions_and_discovery

The question about the meaning of “live” exposes a useful product boundary. We do not know its actual business definition in this review, so the assistant should search the authoritative glossary or catalog rather than guess. If several reviewed definitions match, it should ask which meaning applies; otherwise it can explain the supported definition with its source and offer a relevant example. Definition-only work can often use metadata without querying source data. The same experience can expose topic browsing, supported questions and explanations of unavailable data. That helps users learn what the product can do at the moment they need it. Evaluate definition correctness, useful discovery, the next question users can successfully ask, and time to a useful response. These tasks deserve a first-class route through the application.

---

# 07_dependency_complete_context

Semantic retrieval should start with business roles, not merely similar column names. After restricting metadata to the authorized scope, retrieve candidate measures, dimensions, filters, entities and time roles. Once the requested measure is selected, close its dependencies: the reviewed definition, denominator, physical mapping, date rules, keys, cardinality and required join routes. Those dependencies make the measure valid. A near match does not prove question coverage, and missing definitions or unresolved ambiguity should remain visible. Versioned catalog metadata can be reused while source data refreshes independently. The experiment is to reduce context while preserving required-definition coverage, join coverage and final result correctness. The smallest useful package is the one that retains enough meaning to answer correctly, not simply the one with the fewest tokens.

---

# 08_context_latency_experiment

This should be a controlled comparison in one sales domain. The baseline uses the current full semantic context, reported at twenty to thirty thousand tokens. The candidate uses role-selected definitions with complete metric and join dependencies. Hold the model, behavior, settings, questions, source snapshot and evaluation contract fixed so that context selection is the change being tested. Record coverage and correct results together with tokens and stage timing. Separate retrieval, routing, generation, validation and database execution from the full task duration, and report both median and tail latency. Fewer input tokens may help, but the measured stages determine whether that explains a gain. One-shot versus bounded repair is a later, separate comparison; combining the two changes would make attribution difficult. We are proposing the experiment, not promising a particular context size or speedup.

---

# 09_same_row_count_failure

Every identifier and number in this example is invented teaching data. For advisor A17 and product P-A, purchases of eight hundred thousand dollars and redemptions of one million dollars produce negative two hundred thousand dollars of net flow. The firm’s positive five million dollars is a separate aggregation scope. The deliberately wrong candidate labels that firm figure as A17’s result while still returning exactly one row. Row-count agreement therefore passes, but the business answer is wrong. Comparing keyed values, the definition of net flow and the entity and grain exposes the error. An LLM judgment can add semantic coverage, but it needs calibration against adjudicated expert cases. Even the correct negative advisor result does not establish dissatisfaction or competitor displacement. That commercial interpretation requires additional evidence and discovery.

---

# 10_layered_evaluation

The evaluation contract should leave five dimensions independently inspectable. Execution checks valid SQL, source permissions and query limits. Typed-result checks compare complete keyed rows or multisets while preserving duplicates and nulls; ordering, top-k ties and column-specific tolerances must be specified before grading. Business meaning checks entity, metric, grain, denominator, date role, period, units and coverage. Conversation checks definitions, discovery, clarification, state updates and freshness. Useful sales work checks factual support, useful questions, disclosed material gaps, approved material and rep effort. Freeze the source data and as-of conditions, and review reference SQL independently. Alternative SQL implementations can be correct, so the reference should define the accepted result rather than force a single syntax. Calibrate LLM semantic judgments on expert-adjudicated cases and keep critical defects visible instead of hiding them inside a single average accuracy score.

---

# 11_explicit_conversation_state

Conversation memory should be explicit task state that the user can inspect and correct. Persist resolved advisor, office and firm identifiers, the metric, grouping, filters, period, information cutoff, semantic version, saved result identifiers and unresolved questions. In the last-quarter follow-up, the period changes while the intended entity, metric, grouping and filters carry forward. Changing the advisor or measure requires a deliberate state update. Session context, reviewed business knowledge and saved evidence have different responsibilities: the first holds the active task, the second holds definitions, and the third holds data snapshots. Show active scope and allow correction or reset. Reusing a conversation does not make old evidence current. Multi-turn evaluation should test completion, scope carryover, clarification, freshness and cross-advisor leakage, including cases where preserving prior state would be wrong.

---

# 12_bounded_investigation

For a question about falling advisor flows and contributing product families, make the decomposition visible. Resolve the measure, comparison window and advisor scope; retrieve advisor-level change; calculate product-family contributions at a compatible grain; reconcile the components to the requested total; then explain the supported findings and uncertainty. This provides intermediate evidence that a one-shot answer often lacks. Actual schema, execution or validation feedback may justify repair, but attempts and total time need a predefined budget. Retain every attempt and permit an unresolved or clarification outcome. Recheck permissions and scope at each step. Held-out reference answers must not enter the runtime repair path, because that would invalidate assessment. Product contributions are arithmetic decompositions; they do not by themselves identify causal drivers of a sales change.

---

# 13_sales_meeting_packet

The intended user is a Fidelity institutional salesperson serving advisors as distribution partners. A useful preparation packet answers four business questions. Why meet covers the objective, resolved advisor identity and prior commitments. What changed selects relevant activity since the last interaction while preserving period and coverage. What to ask separates commercial hypotheses from observed facts and turns them into questions the rep can validate. What to bring identifies current approved product and share-class material and flags unresolved requirements. Every material number should carry entity, metric, period, units, snapshot and calculation. Historical analysis needs effective-dated relationships so that today’s hierarchy is not silently projected into the past. Fidelity activity is only the observed scope; it does not establish an advisor’s entire wallet. The rep’s review completes preparation.

---

# 14_synthetic_sales_brief

The schematic brief uses entirely invented advisor, product, record and numerical data. A17’s purchases are eight hundred thousand dollars, redemptions are one million, and net flow is negative two hundred thousand. The positive five million firm aggregate stays explicitly separate. A prior meeting record requests a share-class and implementation discussion. Those are the facts available in this scenario. The idea that a focused approved comparison may move the conversation forward is a commercial hypothesis, not an observed outcome. Ask which implementation constraints matter and confirm the exact product and share class, document version, approval context and valid time. The rep reviews and adjusts the preparation before use. Accepting a draft does not authorize an outbound action, and negative flow alone does not prove dissatisfaction or displacement.

---

# 15_expert_authored_skills

Range’s financial-planning method offers a practical way to author a professional skill. Pick one repeated workflow with recognizable acceptance. Teach why the salesperson or product specialist performs each step, including exceptions. Pack the facts, definitions, authorized sources, clarification questions and action limits that make the method executable. Test ordinary cases, ambiguous cases and consequential failures; missing information should change the workflow rather than be smoothed over. Ship with an owner, reviewer, change history and regression checks for revisions. Domain experts contribute the method and its reasons alongside the steps. Applying that process to advisor-sales preparation is our proposed transfer from Range’s planning use case. Adoption alone establishes neither a capacity gain nor business value; those require evaluation in the local workflow.

---

# 16_measure_salesforce_job

Salesforce integration makes the assistant available in a useful context, but availability does not establish workflow value. Observe where reps begin, what information they copy, which colleagues they consult, which claims they verify and how they act after meetings. Choose one identifiable job, such as preparing for a meeting with a resolved advisor, and place the scoped packet in that record’s context. Compare similar existing and assisted cases, counterbalancing preparation order where feasible to reduce learning effects. Include preparation, checking, rework and post-meeting action in the baseline. Measure time to an accepted brief, active review and rework, useful questions, material omissions, return use and completed follow-through. Qualified opportunities and sales effects are separate outcome questions with their own attribution problems. They should not be inferred from a shorter preparation session.

---

# 17_fidelity_release_increments

The roadmap is a sequence of working releases with evidence gates. The first slice observes CRM tasks, strengthens result grading, selects one domain and establishes definition and discovery examples. That produces trusted references, visible failure classes and a workflow baseline. The next working release adds glossary and data navigation with selected semantics, followed by explicit session state and follow-up checks; isolate their effects rather than changing everything together. Controlled expansion adds one bounded complex-question workflow and one rep-reviewed meeting packet, then pilots the complete journey. The evidence should include correct results, coverage, stage timing, scope carryover, consequential failures and total human effort. These are not fixed thirty-, sixty- or ninety-day promises. Owners, thresholds and timing remain to be agreed, and quality and effort determine whether expansion is justified.

---

# 18_personal_agent_foundation

The personal project begins from a different point. The October fifteenth read-only review found semantic discovery, SQL-owned warehouse access, Python analysis over named saved data, typed complete datasets, lineage, immutable scope and report revisions. Deterministic comparisons, persistent artifacts, Stop and Resume, retries and portable replay are valuable existing capabilities. The paired evaluation harness already freezes receipts and fingerprints and protects boundary and first-attempt outcomes. Preserve those ownership and evidence paths rather than introducing another framework. The planned frontier is broader workspace reading and search followed by controlled authoring and checks connected to accepted evidence. This presentation does not report a new implementation or a fresh model or provider evaluation. The recommendations are focused extensions to the inspected foundation.

---

# 19_analytical_correctness_contracts

Three small boundaries deserve focused fixtures. First, canonical metric selection is optional at the tool boundary, and the general fanout guard iterates sum and average rather than ordinary count. KPI work should declare the counted population and measure meaning, with cases for counts, distinct counts, denominators and many-side joins; valid custom extracts should remain possible. Second, successful execution is required for completion, but the forecast descriptor is optional. A completed forecast should require saved predictions and the existing evaluation contract, or return a supported partial outcome. Third, empty or all-null Snowflake data should retain declared types rather than relying only on observed values. A successful script and a well-formed batch are useful checks, but neither establishes the full analytical claim. These are code-review opportunities identified in the dated review, not reproduced production incidents.

---

# 20_bound_quantitative_narrative

The existing report cards already resolve stored evidence, while narrative and callout bodies and infographic values remain strings. Ordinary cards also allow free-form prefix and suffix units. This creates a boundary where a correct table can coexist with a wrong quantitative sentence or an unsupported currency label. Extend the declarative report contract with typed numeric spans and reuse the saved-cell and comparison resolvers. In the invented A17 example, the advisor’s negative two hundred thousand dollars must be the same in the card, sentence and callout; the firm’s positive five million belongs to a different scope. The binding should carry entity, period, units, snapshot and calculation, not just a formatted value. Acceptance means that changed evidence updates every bound appearance and that wrong-scope bindings and unsupported unit labels fail before saving.

---

# 21_preserve_meaning_on_refresh

Lineage and matching columns need complementary checks on meaning. The reviewed source SQL path retains canonical metric bindings, while saved-SQL reshaping omits that binding. Preserve identity through unambiguous projections and renames, but require a new justified meaning when a calculation scales a value or changes its aggregation. Refresh currently checks column names and types before copying the prior grain description. Add validation of declared keys, time bucket, aggregation or measure, scope and full-result key uniqueness. A daily-to-monthly refresh can retain the same physical schema while changing row meaning; duplicate keys or a changed measure can do the same. Reject or clarify those changes while permitting legitimate new values and typed empty results. Keep source completeness unknown when undeclared: save time and the last observed transaction are not evidence of a complete source.

---

# 22_outcome_oracles

The useful extension to evaluation is to inspect the stored outcome. For counts and totals, recompute from named Parquet bindings and check denominators. For forecasts, inspect saved predictions and windows and recompute error using the existing forecast contract; the words holdout and MAE do not prove those operations happened. For reports, compare values, scope and units with accepted saved evidence. Retain the paired harness’s receipts, fingerprints and human review. Add reviewer and rubric identity, an adjudicated defect pack and separation of development, regression and final assessment by task family and exposure record. Turn failures into regression cases, then reviewed skill or definition updates; a user correction should not automatically become business truth. Extend token and active-time diagnostics with reviewer effort and known or estimated cost across all attempts per accepted task, keeping unknown costs explicit.

---

# 23_workspace_to_checked_result

The selected workspace direction becomes concrete through one assignment: find the retention definition, inspect the SQL, identify a denominator mistake, propose a patch and reconcile against approved saved evidence. Begin with bounded project reading and search within assignment-level source scope. Then add controlled authoring and checks with explicit tool permissions, keeping the existing coordinator, SQL and Python specialists and evidence stores. Workspace text is context; it does not by itself establish an accepted business definition or grant execution authority. The current subprocess has time and output bounds, which are not an isolation sandbox; broader shell work requires an execution-isolation design. This remains planned HANDOFF work rather than a delivered capability. Later artifact validation should exercise charts in a real browser and check disclosures, keyboard access, narrow layouts and print behavior. This presentation does not claim those browser checks were performed.

---

# 24_next_accepted_work_product

The next decision is a bounded work product and the test that earns expansion. For Fidelity, bring representative questions, choose one sales domain, agree entity, metric and date definitions, and establish trusted reference results. Instrument stage latency and observe how reps prepare for an advisor meeting. For the personal agent, begin with one count or forecast correctness fixture, one bound quantitative lead or callout and one numerical outcome oracle, then connect one workspace assignment to a checked result. In both tracks, compare quality, consequential failures, total human effort and full known cost. Record whether to continue, revise or stop, including what remains uncertain. Accepted work is the unit of progress. The discussion should agree owners, thresholds and timing rather than treat this presentation as an assigned delivery commitment.

---

# 25_diagnostic_defect_suite

This reference suite makes the accuracy contract diagnostic. Same-cardinality wrong values test false accuracy; duplicated joins test population and aggregation; advisor hierarchy and date-role cases test business scope. The ambiguous live question should retrieve definitions or clarify, while an unavailable measure should disclose the limit rather than invent coverage. Follow-up questions test deliberate state changes, stale evidence tests freshness, and denied-access cases test authority. A correctly denied action is a control success. Each case needs an expected clarification, supported result or refusal, not merely a fluency score. Keep reference answers outside runtime repair, review them independently and separate assessment families from tuning. These are proposed cases for a defect pack, not measured incident rates.

---

# 26_accepted_work_scorecard

Agree populations and denominators before comparing systems. Task acceptance is accepted work over eligible assigned tasks in an agreed window, with rejected, abandoned and excluded outcomes visible. Quality combines typed-result equivalence and business-scope correctness, with critical defects reported separately. Latency includes median and tail times by stage and end to end, plus first-correct time for bounded work, attempts and timeouts. Human effort includes active preparation, review and rework, distinguished from waiting and accompanied by reviewer role and case mix. Cost includes known or explicitly estimated attempt, tool, data, review and support costs over accepted tasks; unknown components and assumptions must remain explicit. Measure later business effects separately. This is a measurement definition table, with no fabricated results, targets or return on investment.

---

# 27_implementation_anchors

The code-reference table makes the personal roadmap reviewable at its owning boundary. Start count-grain work in semantic SQL and the text-to-SQL tool contract, forecast completion in the analysis tools, and empty-result typing in the Snowflake adapter. Narrative and unit binding span reporting schemas, renderer and comparison logic. Reshape and refresh live in text-to-SQL tools and presentation handling; outcome checks begin in the live evaluation tests and documented-example grader. HANDOFF and the coordinator explain the planned workspace direction and current scope. The application paths are relative to the data analytics agent package, while tests, scripts and HANDOFF are at repository root. These anchors are from the October fifteenth read-only review and identify starting points, not delivered changes or a provider study.

---

# 28_primary_references

The links provide a route back to the evidence behind the mechanisms. Conference sources cover Bridgewater’s task knowledge and temporal scope, Kepler’s checked numbers, Range’s expert-authored methods, Ramp’s complete-task comparisons, Contour’s credible alternative, and the broader ownership and authority context from Two Sigma and Wise. The technical references include Snowflake’s Verified Query Repository for reviewed examples, Databricks Genie quality guidance for curated semantics, Anthropic’s evaluation guidance for agent outcomes and Snowflake Cortex Code for workspace-oriented analytical engineering. Those sources support patterns; our local architecture and release choices remain recommendations. Fidelity’s baseline is user-reported, personal implementation claims come from the October fifteenth read-only review, and synthetic examples are labeled. No measured return on investment or speedup is asserted.
