[Skip to recommendations](#main)

AI ENGINEER NYC 2026 · APPLICATION BRIEF · OCTOBER 15, 2026

# From conference lessons to the next useful release.

A practical roadmap for Fidelity’s advisor-sales applications and your personal data analytics agent.

FIDELITY

## Make the data assistant conversational, discoverable and faster.

Give users useful definitions and data guidance, retrieve the right semantics, then support bounded investigation inside their sales workflow.

PERSONAL PROJECT

## Extend the evidence guarantees through the final answer.

Build on the working agent: close specific correctness gaps, strengthen outcome evaluation, and deliver one complete workspace-to-analysis journey.

[Fidelity first release](#fidelity)[Evaluation](#quality)[Complex work & meeting prep](#agent-work)[Personal agent](#personal)[Next increments](#sequence)[Evidence](#sources)Print / PDF

01 / THE STARTING POINT

## Your new context changes the Fidelity priorities

The main problem is broader than SQL generation. Users need help understanding the available business data, expressing a question, refining it and turning the answer into work they can use.

**One shot**

Complex questions receive the same generation pattern as simple questions. Conversation and memory are absent.

**20–30K tokens**

Large table/column semantics are supplied each time. You report roughly 30–45 seconds of model latency before intent and data execution time.

**Row counts + judge**

Current evaluation compares generated/reference row counts and uses an LLM to compare returned data.

**Workflow unknown**

The tool is being integrated with Salesforce, while its effect on sales preparation and daily work remains unclear.

Fidelity’s baseline above comes from your description. The personal-project findings below come from read-only inspection of the current repository. Internal Fidelity code and data were not inspected.

**Recommended product goal**

A salesperson can discover what the system knows, ask a business question, clarify it, inspect the evidence and prepare a relevant advisor conversation within a predictable time budget.

02 / FIDELITY: FIRST RELEASE

## Give the assistant a useful front door and a smaller evidence context

Evolve the intent layer into a capability-aware coordinator. Keep the current SQL generator as an owned tool, and give both components access to the same reviewed business definitions.

**Understand**Question + CRM record + compact session state

**Ground**Definitions, entities, measures, dates and join dependencies

**Choose the work**Explain · discover · clarify · query · investigate

**Return accepted work**Checked result + source scope + useful next action

01

### Answer definitions and expose the available data

“What’s the meaning of live?” is a valid business-data question. Look up the actual catalog definition; if several definitions match, explain the choices and ask which one applies. Its meaning is currently unknown to this review and should not be invented.

Add “What can I ask?”, topic browsing, examples drawn from supported data, and explanations of why a question is unavailable. Offer definitions alongside query results. These metadata questions should finish without running SQL or loading the full warehouse schema.

**Measure:** grounded definition correctness, helpful discovery, successful next question, unnecessary SQL calls and time to a useful answer.

02

### Retrieve a semantic package for the question

Limit catalog discovery and metadata retrieval to the user’s authorized role/resource scope before building model context; validate source permissions again at execution. Select candidate measures, dimensions, filters, entities and date roles, then include the required definitions, physical mappings, keys and join routes. Metric dependencies should narrow the search. A top-k list of similar columns is insufficient if it drops a required denominator, date rule or relationship.

Start with one sales domain and keep the model and other behavior fixed. Compare today’s full context against the selected package on the same frozen cases. Preserve ambiguity: a near match is a reason to clarify, not proof that the requested measure exists. Reuse versioned catalog metadata; refresh data independently.

**Measure:** context tokens; required-definition and join coverage; result correctness; p50/p95 retrieval, model, database and total latency. Add retries or another retrieval technology only after the isolated comparison identifies the next bottleneck.

03

### Support follow-ups through explicit session state

Store the resolved advisor/firm/office IDs, measure, grouping, filters, time period, information cutoff, semantic version, saved results and unresolved questions. A follow-up such as “What about last quarter?” changes the period while preserving the other intended scope. Changing the advisor or measure must update the relevant state explicitly.

Separate conversation state, reviewed business knowledge and saved data. Chat history can preserve the question; it cannot make an old snapshot current or establish a new business definition. Show the active scope to users, and let them reset or correct it.

**Measure:** multi-turn task completion, correct scope carryover, appropriate clarification, stale-data reuse and cross-advisor leakage. Preserve previous evidence when creating a new result.

Relevant established patterns: [Snowflake’s reviewed question/SQL repository](https://docs.snowflake.com/en/user-guide/views-semantic/verified-query-repository) and [Databricks’ localized semantics and query examples](https://docs.databricks.com/aws/en/genie-agents/tune-quality) show how reusable definitions and organization-specific examples can support generation. This is an architectural pattern to adapt, rather than a platform decision.

03 / EVALUATION

## Keep row-count agreement as a diagnostic; grade the business result

Two queries can return ten rows while identifying different advisors or reporting different flows. Retain your current checks, but make full result comparison and business-scope correctness separate, explicit outcomes.

| Evaluation layer | What to check | Example defect it catches |
| --- | --- | --- |
| Execution | SQL parses, runs within limits and respects source permissions. | A syntactically invalid or prohibited query. |
| Result equivalence | Compare complete typed outputs outside the LLM: keyed rows or row multisets, values, NULLs and duplicate multiplicities. Ignore order only when it is irrelevant; define top-k ties and per-column tolerances in advance. | Same row count, different advisors; duplicate join rows; zero substituted for missing data. |
| Business meaning | Measure, entity, grain, denominator, date role, period, units and source coverage. | Firm totals described as advisor totals, or assets treated as net flows. |
| Conversation | Definitions, discovery, clarification, state updates, source refresh and follow-up completion. | A valid glossary question rejected, or last quarter applied to the wrong advisor. |
| Useful sales work | Correct facts, relevant omissions, useful questions, approved material and total rep review effort. | A factually correct brief that adds no useful meeting preparation. |

### Make the reference trustworthy

Freeze the data and information cutoff for comparison, independently review the reference SQL, and permit alternative correct SQL implementations. Add contrast fixtures where plausible wrong filters, joins or date roles produce a different answer. One matching snapshot does not prove equivalence on every dataset.

### Calibrate the current judge

Use deterministic checks for complete numeric results. Use the LLM judge for interpretation, explanation and other semantic rubric items; compare its decisions with adjudicated expert examples, especially serious false passes. Keep judge/rubric versions and disagreements.

The combination of outcome checks, model rubrics and human calibration is consistent with [Anthropic’s agent-evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). The specific grading contract here is proposed for your business tasks.

**First diagnostic suite**

Include a same-row-count/wrong-value case, duplicate-join case, wrong advisor hierarchy, wrong date role, ambiguous “live” definition, missing measure, follow-up scope change and denied access. A correctly denied request is successful control behavior; actual unauthorized access is the defect.

04 / FIDELITY: COMPLEX QUESTIONS & MEETING PREP

## Add bounded investigation where the question needs several steps

Agent capability should make difficult work clearer and more correct. Common definitions and simple queries should retain a fast path; a complex investigation can earn additional steps through an explicit plan and budget.

### A complex question becomes inspectable work

For “Which advisors’ net flows fell, and which product families contributed?”, resolve the metric and comparison window; obtain the advisor-level change; calculate product contributions at compatible grain; reconcile contributions to the total; and explain the supported result. Ask when the requested comparison is ambiguous. Arithmetic contribution is distinct from a causal explanation of behavior.

Allow a bounded validation/execution repair using actual schema or execution feedback. Define attempts and total time in advance, preserve all attempts and finish with an explicit unresolved outcome when necessary. Held-out reference SQL and expected answers must never become runtime repair hints.

### Evaluate the extra steps

Compare the one-shot baseline and the bounded workflow separately from the schema-selection experiment. Track first-attempt correctness, accepted completion within budget, first-correct time, repair rate, p50/p95 total latency and all-attempt cost per accepted result. Check permissions and scope on every step.

Use the existing SQL engine through the coordinator. Start with the recurring question class that currently needs the most manual decomposition; the number of agents is not a success measure.

### Turn meeting prep into a sales decision packet

The user is a Fidelity salesperson serving advisors as distribution partners. The packet should help that person decide why to meet, what changed, what to ask and which approved material to bring. Range’s expert-authored method is transferable; its retail financial-planning task is different.

**Why meet?**Meeting objective, advisor identity and prior commitments

**What changed?**Relevant activity and developments since the last interaction

**What to ask?**Commercial hypotheses and questions to validate them

**What to bring?**Correct product/share-class material and unresolved requirements

Use text2SQL as the fact provider for meeting prep. Each material number should retain entity, measure, period, unit, source snapshot and calculation. Use effective-dated advisor/office/firm relationships for historical questions; today’s affiliation does not establish last quarter’s population. Product statements should identify the exact product/share class, document version, approval context and valid time. Distinguish known facts, commercial interpretations and discovery questions; available Fidelity activity is not automatically an advisor’s entire wallet.

SYNTHETIC EXAMPLE · INVENTED ENTITIES, VALUES AND PRODUCT LABELS

### A useful brief preserves the difference between advisor and firm

**Request:** Prepare for advisor A17’s meeting. For the stated period, purchases of placeholder product P-A are $0.8m and redemptions are $1.0m, giving net flow of −$0.2m. The advisor’s firm has +$5.0m net flow for that product. A prior meeting record requests a share-class and implementation discussion.

#### Observed fact

A17’s net flow was −$0.2m. The +$5.0m figure belongs to the firm. The prior record contains a request for comparison material.

#### Commercial hypothesis

A focused approved share-class comparison may advance the conversation. Negative flow alone does not establish dissatisfaction or competitor displacement.

#### Discovery & review

Ask which implementation constraints matter. Confirm the correct current product/share-class material and channel context. The rep accepts or edits the packet before use.

### Find the Salesforce workflow before expanding the feature set

Observe a few reps performing real preparation and analytical tasks: where they begin, what they copy between screens, what they ask colleagues, what they verify and what they do after the meeting. Choose one job such as “prepare for this advisor meeting” and make the brief available at that record. Compare the complete existing and assisted workflows on similar cases; counterbalance order where feasible to reduce learning effects.

**Initial value measures:** time to an accepted brief, total preparation/review/rework, useful discovery questions, relevant omissions, return use and whether the rep completed the intended follow-through. Track later qualified opportunities separately. CRM placement and adoption do not by themselves establish sales lift.

05 / YOUR PERSONAL ANALYTICS AGENT

## The foundation is already substantial; extend the guarantees at specific boundaries

The repository already has SQL/Python ownership, semantic discovery, complete saved datasets, lineage, immutable revisions, numerical comparison checks, recovery, portable replay and a paired evaluation harness. The next investment should make those pieces support stronger end-to-end claims.

P0

### Close the count-grain and completed-analysis contract gaps

**Code finding:** canonical metric selection remains optional, and the general fanout guard iterates SUM/AVG rather than ordinary COUNT. A successful execution also permits completed analysis without requiring the optional forecast-evaluation descriptor.

**Next increment:** require explicit counted population/measure meaning for KPI queries; test counts, distinct counts, denominators and many-side joins. Make forecast completion require saved predictions and the existing evaluation contract, or return a supported partial outcome. Preserve declared Snowflake types for empty/all-null results as a small adapter repair.

**Acceptance:** wrong-grain counts fail or request clarification; valid custom extracts remain possible; incomplete forecast evidence cannot be called complete; empty refresh retains declared types.

Inspected implementation**Canonical metrics are optional at the tool boundary**`data_analytics_agent/agents/text_to_sql/tools.py:93`**General multiplicity check covers SUM/AVG**`data_analytics_agent/semantic_sql.py:312`**Forecast descriptor is optional; completion checks successful execution**`data_analytics_agent/agents/data_analysis/tools.py:122`**Value-inferred batches and string-typed empty results**`data_analytics_agent/backends/snowflake.py:129`

P0

### Bind narrative numbers and units to saved evidence

**Code finding:** metric-card values are resolved from saved data, while narrative/callout bodies and infographic values remain strings. Ordinary cards also accept free-form prefix/suffix units. A correct table can therefore coexist with an inconsistent quantitative sentence or undeclared currency label.

**Next increment:** extend the existing declarative report contract with typed numeric spans for headlines, leads, callouts and infographic values. Reuse the saved-cell/comparison resolver, declared units and checked percentage scaling. Keep explanatory prose flexible; another general-purpose “critic” is not required to format a known value correctly.

**Acceptance:** changing one stored metric updates every bound occurrence; wrong/out-of-scope bindings and invented unit labels are rejected. Test negatives, rounding, zero baselines and report/card disagreement.

Inspected implementation**Bound metric values and string narrative blocks**`data_analytics_agent/reporting/schemas.py:95`**Narrative rendering does not resolve quantitative claims**`data_analytics_agent/reporting/renderer.py:188`**Existing metric resolver to extend**`data_analytics_agent/reporting/renderer.py:260`**Existing declared-unit rule**`data_analytics_agent/reporting/comparisons.py:113`

P1

### Preserve business meaning through reshaping and refresh

**Code finding:** source SQL persists canonical metric bindings, but saved-SQL reshaping does not carry them forward. Refresh checks field names and physical types before copying the old grain description; the same schema does not establish the same business grain.

**Next increment:** propagate identity through unambiguous projections/renames, while withholding the old identity for changed calculations. Add selected-input keys, time bucket, aggregation/measure and scope contracts; verify them during refresh. Preserve unknown source completeness rather than inferring it from save time or the latest transaction.

**Acceptance:** transparent reshapes retain identity; scaled or changed measures do not. Same-schema daily-to-monthly, duplicate-key and changed-measure refreshes are rejected or clarified; legitimate new values and typed empty results remain supported.

Inspected implementation**Saved-result SQL stores lineage without metric\_columns**`data_analytics_agent/agents/text_to_sql/tools.py:223`**Refresh schema checks**`data_analytics_agent/presentation.py:186`**Prior grain is copied**`data_analytics_agent/presentation.py:204`**Current selected-input grain contract**`data_analytics_agent/analytical_scope.py:49`

P1

### Strengthen the current evaluation harness with output oracles

**Code finding:** the broad live analytical tests use method words such as “holdout” and “MAE” as proxies. The paired harness is much stronger: it already freezes receipts and fingerprints, checks human reviews and protects boundary/first-attempt outcomes.

**Next increment:** reuse named Parquet bindings and the forecast evaluator to grade actual predictions, windows, totals, counts and report agreement. Separate development/regression from final assessment by case family and exposure record. Add reviewer/rubric identity and a small adjudicated defect pack. Extend existing tokens/active-time diagnostics with reviewer effort and known/estimated cost; unknown cost stays unknown.

**Acceptance:** correct-sounding prose with wrong outputs fails. A new ablation identifies untouched assessment families, reviewer disagreements, critical failures and all-attempt cost per accepted task.

Inspected implementation**Keyword-based analytical proxies**`tests/test_live_evaluations.py:140`**Existing exact saved-value checks**`scripts/grade_documented_examples.py:36`**Existing hard-boundary adoption gate**`scripts/compare_ablation.py:243`**Paid cost and warehouse count are explicitly unknown**`scripts/compare_ablation.py:371`**Existing time, call and token diagnostics**`data_analytics_agent/stores.py:546`

P1

### Deliver the workspace journey already selected in your handoff

**Current direction:** understand project files and business definitions, find approved data, draft or repair a calculation, check it and explain the supported result. The current coordinator’s filesystem permission is limited to AGENTS.md and skills; broader workspace tools remain planned.

**Next increment:** support one complete task: “Find the retention definition, inspect the SQL, identify a denominator mistake, propose a patch and reconcile it against approved saved evidence.” Begin with bounded project reading/search and explicit task-level source scope, then add controlled authoring/checks. Use the existing coordinator, SQL specialist, Python specialist and evidence stores.

**Acceptance:** a reviewed definition is found, the wrong calculation is identified, the proposed repair matches a checked result and the final artifact explains scope and limitations. Workspace text remains context; accepted definitions and execution permissions remain explicit.

Inspected implementation**Selected end-to-end product journey**`HANDOFF.md:27`**Planned workspace and discovery capabilities**`HANDOFF.md:42`**Current filesystem scope**`data_analytics_agent/coordinator.py:137`**Execution isolation must be revisited for broader shell work**`HANDOFF.md:56`

Your chosen workspace direction is consistent with the project/file/SQL/skill workflow described in [Snowflake’s CoCo overview](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code). Adapt the workflow through the current stack. The existing local subprocess has time/output limits; broader execution would require an explicit isolation design.

### Let observed failures produce reviewed skills

Start with change explanation, reconciliation and query debugging. Capture the task, required inputs, reasoning checks, output evidence and exceptions in a skill owned by you. Turn a real failure into a regression case, then propose a reviewed skill or definition update. Compare one skill/context change at a time with the current harness. Persistent history is already useful; automatically adopting every correction as business truth would bypass the review that makes the knowledge trustworthy.

**Later artifact check:** add a small real-browser test suite for synthetic HTML reports—rendered numbers, chart execution, source disclosures, keyboard controls, narrow screens and print. Schema/string tests establish useful properties, but do not establish that the delivered artifact renders correctly.

06 / DELIVERY SEQUENCE

## Make each increment answer a measurable question

| Increment | Fidelity | Personal agent | Decision evidence |
| --- | --- | --- | --- |
| Baseline and first slice | Observe real Salesforce tasks; improve reference/result grading; select one sales domain and build definition/discovery examples. | Add a numerical outcome oracle and close a directly relevant count/forecast/report claim gap. | Can the grader catch plausible wrong work, and can a user recognize accepted completion? |
| Next working release | Grounded glossary + data navigation + selected semantics; then session state and follow-up scope checks. Keep retrieval and conversation changes separately measurable. | Extend bindings through narrative, reshapes and refresh; deliver bounded workspace reading/search for one calculation question. | Does context shrink without losing necessary definitions or result correctness? Do follow-ups and refreshed artifacts preserve meaning? |
| Controlled expansion | One bounded complex-question workflow; one rep-reviewed meeting packet; pilot the complete CRM preparation journey. | Complete workspace-to-repaired-calculation-to-checked-report; compare reviewed skills with independent assessment and full effort. | Does accepted completion improve at agreed quality and total effort? What failure would stop or change the release? |

### The next Fidelity team session

1. Bring recent user questions, including definitions, ambiguous terms, follow-ups and slow complex requests.
2. Choose one sales domain; agree entities, measures, dates and a trusted reference result.
3. Instrument latency by stage and compare full versus task-scoped semantics.
4. Observe a rep’s existing meeting-prep workflow and define the accepted packet.

### The next personal-project increments

1. Turn one known wrong count or incomplete forecast into a deterministic failing case.
2. Bind one quantitative lead/callout to the existing result/comparison resolver.
3. Strengthen one live output oracle, then use it to assess a complete workspace task.
4. Record reviewed reusable lessons and the evidence behind each engineering decision.

**Shared principle**

Measure accepted work: the right question, evidence, calculation, artifact and human decision. Tokens, SQL execution, generated drafts and tool counts explain the process; they are not substitutes for its outcome.

07 / EVIDENCE & REUSE

## Where the recommendations come from

| Conference mechanism | Application | Source |
| --- | --- | --- |
| Bridgewater: task-specific knowledge and time scoping | Question-specific semantics and source cutoffs; separate evidence coverage from the rep’s short brief. | [Vault session](https://ai.engineer/nyc/2026/schedule?session=a84ca3a8-cc2f-4b50-a635-fc380f6f04f6) |
| Kepler: retrieval, typed facts, arithmetic and citations | Result contracts, narrative bindings and exact product/source identities. | [Do Not Let Models Invent Numbers](https://ai.engineer/nyc/2026/schedule?session=2d29f925-f16b-41b3-8086-de0524829cbe) |
| Range: expert-authored skills | Sales-authored meeting methods; reusable analytical skills with reasons, questions and exceptions. | [Financial planners write the agents](https://ai.engineer/nyc/2026/schedule?session=9b002687-09cf-42e2-9282-532ed9d0c184) |
| Ramp: end-to-end tasks and ablations | Separate context, conversation, repair and skill changes; grade complete outputs. | [End-to-End Evals](https://ai.engineer/nyc/2026/schedule?session=4607dbbe-8f94-4b0e-91ce-257d1cfb5448) |
| Two Sigma / Wise: ownership and authority | Scoped SQL/tools and explicit review/execute boundaries across every step. | Individual session links in the [conference presentation](../../../../outputs/ai-engineer-nyc-2026-presentation.html). |
| Contour: useful work, full cost and the credible alternative | Measure preparation and review against existing Salesforce work; keep sales attribution separate. | [Proving Alpha](https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca) |

Company stories supply mechanisms and questions; the recommendations are an application of those lessons to your described workflows and inspected code. The notes do not establish verified ROI for these proposals. Synthetic examples contain no real advisor, Fidelity product or client data.

Repository reviewed: `/Users/charlie/Repos/deepagents-agents/data-analytics-agent`. Source paths above are relative to that root. This was a read-only review: no application code changed, no tests or model/provider studies ran, and no warehouse data was queried. The repo’s existing handoff remains the active product direction.

This brief contains no external runtime assets or network requests. Its source links and companion presentation link are optional references. The document is fully readable without JavaScript.

Prepared October 15, 2026 · Proposals for prioritization and testing; no application implementation or deployment was performed.
