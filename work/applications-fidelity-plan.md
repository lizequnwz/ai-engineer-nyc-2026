# Fidelity institutional sales enablement: revised application plan

Start with a **trustworthy, discoverable analytical assistant for one sales workflow**, then add conversation and bounded planning. Current priorities are correctness and task understanding, followed by relevant context and latency. The target is advisor-sales enablement for Fidelity products, not retail-client financial planning.

## Confirmed current state and implications

The user describes an independent lightweight LLM intent router followed by one-shot text2SQL, including for complex questions. There is no conversation state, memory or agent behavior. A definition request such as “What's the meaning of live?” is rejected as not being a SQL question. Users need teaching because they do not know which data is available. SQL prompts include all tables/columns (about 20–30K tokens), with reported LLM latency of 30–45 seconds before execution. Salesforce/CRM integration exists, but its workflow benefit is unknown. Current “execution accuracy” uses generated-versus-target row counts and an LLM comparison of returned data.

These facts are user-reported; no internal code, schemas, telemetry or current evaluation examples have been inspected. **The meaning of “live” is unknown here and must come from an authoritative business glossary.** Do not invent a definition. Existing integration and any existing controls should be inspected before proposing replacement features.

## Prioritized changes mapped to the actual pain

| Priority | Current pain | Smallest useful change | Measure |
|---|---|---|---|
| **P0: redefine correctness** | Matching row counts can label a wrong result correct; the LLM judge is not independently validated. | Retire the row-count-based accuracy definition. Define task semantics and compare result values against expert-reviewed references on the same snapshot. Use deterministic checks where appropriate; calibrate any remaining judge against reviewed disagreements. | Result/semantic correctness; wrong-entity/period/grain failures; false passes and false failures of the judge; accepted task rate. |
| **P0: understand the user's task** | Router only accepts SQL requests, including rejecting a business-definition question. | Support grounded **definition, data discovery, analytical query and clarification** intents. Retrieve the exact glossary definition with scope/source/version; if missing or ambiguous, say what is unresolved and ask a focused clarification. | Correct routing; grounded definition accuracy; appropriate clarification; unsupported-definition rate; task completion. |
| **P1: retrieve a semantic slice** | Every prompt carries 20–30K tokens of schema; latency is 30–45 seconds and users do not know available data. | For one approved sales domain, select relevant business concepts, metrics and data objects within the user's role, then include required join paths, grain and other dependencies. Provide capability cards and answerable question examples using that same catalog. | Required-context recall; excess context; prompt tokens; routing/retrieval/LLM/database latency separately; final answer quality. |
| **P1: retain explicit conversation state** | Follow-up questions and definitions cannot carry forward; users must restate context. | Add a session-scoped state containing resolved entities, business definitions, filters, dates, grain, source snapshot, previous query/result reference and unresolved questions. Show material assumptions and confirm changes that alter meaning. | Follow-up correctness; stale-filter/entity carryover; clarification burden; corrections; complete-task time. |
| **P2: plan complex analysis narrowly** | Complex questions are sent to one-shot generation. | Detect a bounded set of complex tasks; produce a short inspectable plan, resolve missing semantics, execute permitted subqueries, reconcile results and compose the answer. Keep straightforward, well-specified tasks on the simple execution path. | Complete multi-step task success; step/query correctness; reconciliation failures; extra calls, latency and reviewer effort. |
| **P2: prove Salesforce workflow value** | Integration exists, but a connection is not demonstrated user benefit. | Observe the actual advisor-sales workflow and test whether grounded analysis improves an existing meeting-preparation packet. Reuse the integration. Separate advisor, firm and office scope, product/share-class material, facts and commercial hypotheses. | Accepted sales packets; entity/material defects; preparation plus review time; full cost; useful discovery/follow-up outcomes. |

### 1. Replace the accuracy definition before optimizing it

Two queries can each return one row while reporting different advisors, dates or values. Row-count agreement is not result equivalence. A query can also return the correct count after a duplicate join has inflated a sum. Different SQL strings can be semantically equivalent, so string matching is not the answer either.

Create an expert-reviewed evaluation contract for each task: intended entity and aggregation grain; metric definition; period and information cutoff; permitted data; expected values or properties; required clarification/abstention; and prohibited behavior. Run references and candidates against the same stable snapshot and access scope.

Compare schema/types and actual values with appropriate rules for nulls, dates, currency and numerical tolerances. Ignore order only when the task is unordered; preserve ranking and top-N semantics when order matters. Check grouping and duplicate-join effects explicitly. Use expert review for ambiguous business meaning and for reference errors. An LLM may assess explanation quality or propose a disagreement for review; it should not be the sole source of the correctness label. Record important false passes and false failures, not just overall judge agreement.

An initial 50–100-case set is a possible error-discovery starting point, conditional on reviewer/data access. Include definitions, discovery, straightforward queries, complex questions, follow-ups and severe failures, with a separate assessment portion. It is not sufficient statistical evidence that rare errors are absent.

### 2. Add definitions and discovery through an authoritative semantic catalog

For “What's the meaning of live?”, the desired behavior is:

1. Recognize a business-definition request.
2. Look up “live” in the authorized glossary, including its domain and version.
3. Return the definition and source **only if established**. If several meanings exist, ask which business context is intended; if none is available, acknowledge that gap.
4. If useful, show a verified example of how the definition affects a query. Do not manufacture a schema mapping from a label alone.

Data discovery should explain **which business questions can be answered**, with available date ranges, entity/grain and limitations, rather than exposing an undifferentiated list of columns. Capability cards can offer examples such as advisor activity, office aggregation or product comparisons only where the approved catalog actually supports them. The same catalog should drive both user teaching and query-context selection, reducing inconsistent descriptions.

### 3. Retrieve relevant meaning plus dependencies, not isolated table names

The context path should be: **user role/scope → business concept → approved metric and entity definitions → relevant data objects → required join/aggregation dependencies**. Start with a curated, owner-reviewed slice of one sales domain. The internal schema and supported joins must be inspected; none are assumed here.

The selected context needs canonical advisor/firm/office identities, effective-dated relationships where applicable, metric formulas, grain, allowable joins, date semantics and required filters. A small prompt that omits a necessary denominator, join constraint or definition can be worse than the large prompt. If required context is missing, clarify or decline that task; do not silently proceed with a plausible interpretation. Permission filtering must happen before context is exposed to the model.

### Latency experiment

Instrument the reported 30–45 seconds before setting a target: measure router, semantic retrieval/context assembly, LLM time to first token and completion, SQL execution, formatting and total user-task time. Record input/output tokens and query complexity. The reported range is not an observed p50/p95 distribution.

Compare **A: current full-schema prompt** with **B: role-filtered semantic slice plus dependency closure** on the same frozen cases, data, model and attempt policy. Repeat runs where stochastic variation matters. Review required-context recall and final result correctness before crediting latency improvement. Measure simple and complex questions separately; planning may add calls even when each prompt is shorter.

A candidate hypothesis is **at least 50% fewer input tokens and 30% lower median LLM completion latency**, with quality within an agreed tolerance and no unresolved critical semantic/control failure in the defined tests. These are proposed targets, not promises or Fidelity standards. Report upper-tail latency, full-task completion, clarification and retry costs as well. The current prompt is an experiment baseline, not a required fallback in the shipped design.

### 4. Add conversation as explicit state, then bounded planning

The state should describe the task, not be an unbounded chat transcript: resolved advisor/firm/office; definitions; product/share-class; filters; date/as-of rules; grain; sources; previous query/result reference; and unresolved questions. For “now show the office,” the system must explicitly change the aggregation scope instead of merely replacing a name. For “same period,” it should retain the stated period and expose that assumption. Reset context when the task changes; do not carry one advisor's facts into another's packet.

For a defined complex task such as “compare this advisor's activity with their office, explain which products contribute, and prepare meeting questions,” use a short plan: resolve identities and definitions → run authorized scoped analyses → reconcile aggregates and sources → compose supported facts → label possible commercial interpretations → request review. Missing data should remain a gap. Limit tools, steps and retries, and surface failed substeps. This does not require a general autonomous agent or persistent personal memory.

## Smallest next release

Choose **one existing advisor-sales analytical workflow** with a small approved semantic slice. Ship an end-to-end path that:

- Handles a glossary definition, supported-data discovery and a straightforward analytical question.
- Resolves advisor/firm/office and period explicitly.
- Supplies only role-permitted relevant semantics and required dependencies to SQL generation.
- Returns the result with its scope, query/source and information cutoff, or a useful clarification.
- Is assessed with result/semantic correctness and measured task latency.

This directly addresses the rejected-definition experience, data-discovery problem, oversized context and misleading accuracy metric. It does not depend on first building conversation, multi-agent orchestration or another CRM integration. Add follow-up state and complex planning as the next working layer once the narrow path passes its agreed checks.

## Worked advisor-sales example

**Synthetic teaching case: all names, identifiers, amounts and product labels are invented. P-A / SC-1 is a placeholder, not a real Fidelity fund or share class.**

Request: “Prepare for Maya Chen at Northstar Advisory's Boston office. Explain recent P-A activity and prepare the requested share-class discussion.”

Resolved identities: advisor **A17**, firm **F08**, office **O03**. Activity period: July 3–September 30, 2026 (90 calendar days). Data snapshot and packet preparation: October 14. Product material has its own validity at preparation/sharing; it is not governed solely by the activity-period cutoff.

| Item | Correct treatment |
|---|---|
| Advisor A17 purchases $0.8m; redemptions $1.0m | Net flow is **−$0.2m** for that advisor/product/period. Preserve query, grain, snapshot and arithmetic. |
| Firm F08 net flow +$5.0m | A separate firm aggregate. A one-row result containing +$5.0m is still wrong for an advisor-flow question. |
| Meeting record requests share-class and implementation discussion | Supported context for a discovery agenda; it does not establish end-client needs, eligibility or suitability. |
| Approved material M3 identifies P-A / SC-1 and supersedes M2 | Confirm exact product/share-class, approval/channel and validity before use. Do not substitute another share class's claims. |
| Proposed opportunity | “An approved share-class comparison may help this conversation because the advisor requested one.” Label as a **commercial hypothesis**, not proven purchase intent or predicted conversion. |
| Reviewer decision | Inspect facts, material and questions; accept, edit or reject the sales packet. Preparation acceptance does not automatically authorize outbound communication or a transaction. |

A useful adversarial case swaps the firm aggregate into the advisor answer while preserving the one-row count. A second duplicates activity through a join. A third attaches a superseded or wrong-share-class document. The upgraded evaluator should detect all three for different reasons. Conversation tests should then ask “show the office for the same period” and “what does live mean?”; the latter must use the real glossary or expose that its meaning is unresolved.

## 30/60/90-day sequence

These milestones are proposals, conditional on owners, access and baseline findings—not company commitments.

| Horizon | Working outcome | Gate and measures |
|---|---|---|
| **Days 1–30** | Audit current correctness/judge labels; create the task/result suite; inspect one semantic domain and permitted glossary; instrument latency; release definitions/discovery plus context-selected straightforward SQL for that slice. Observe how existing Salesforce integration fits actual sales preparation. | Definition/discovery completion, context recall, entity/metric correctness, judge false passes, tokens and p50/p95 stage latency. Repair critical semantic/access defects before broadening. |
| **Days 31–60** | Add explicit session state and a small set of inspectable complex-query plans. Build a specialist-authored meeting-preparation skill using the existing CRM path and approved product evidence. Run paired current-versus-assisted preparation tests. | Follow-up correctness, complex-task completion, aggregate reconciliation, stale-context leakage, reviewer corrections, total time and accepted packet quality. Extra model calls must earn their cost. |
| **Days 61–90** | Pilot a bounded advisor-sales task/user cohort. Monitor task/rubric slices, escaped failures, review effort and cost; test one source/skill/model change at a time. If quality holds, test one proactive meeting trigger. Produce a grow/revise/stop readout. | Stable accepted quality and critical boundaries, task latency, full cost and measurable workflow benefit. Define pause/rollback conditions before exposure. Product-sales impact remains a separate attribution question. |

For Salesforce discovery, observe the actual sequence before designing more integration: what triggers preparation; where users find advisor/firm/office context; which analytical questions they ask; where results go; what gets copied or corrected; and which review step determines acceptance. A read-only connection may be valuable or may add friction—the current evidence does not say. Test the packet within that real sequence instead of counting successful CRM calls.

## KPI contract

| Measure | Definition and interpretation |
|---|---|
| **Semantic/result correctness** | Analytical tasks meeting intended entity, grain, metric, period and result requirements / analytical tasks. Report failure categories; SQL execution and row count alone are not correctness. |
| **Definition/discovery success** | Requests answered from authorized, versioned glossary/capability evidence or appropriately clarified / eligible definition/discovery requests. Track invented definitions separately. |
| **Context completeness and efficiency** | Expert-required semantic objects/dependencies retrieved / required objects; excess context and prompt tokens alongside final correctness. This guards against making prompts smaller by omitting meaning. |
| **Judge validity** | Important false passes, false failures and disagreements against expert-reviewed labels. Record rubric/model/version and repeated-run stability. |
| **Conversation/complex completion** | Complete follow-up or planned tasks accepted / eligible assigned tasks. Include stale-state, wrong-entity carryover, substep and reconciliation failures. |
| **Packet acceptance and evidence** | Reviewed packets meeting agreed factual, product/share-class/material-validity and hypothesis-labeling requirements / eligible preparation tasks; retain rejected, abandoned and excluded tasks. |
| **Latency and human effort** | p50/p95 stage and complete-task latency; preparation + review + correction + exception time. Faster LLM generation must not hide more clarification or rework. |
| **Cost per accepted task** | Full model/data/tool/retry/review/rework/support cost / accepted tasks. Include failed attempts in costs and report accepted-task rate beside the metric. |
| **Critical failures** | Counts/rates of denied-data exposure, wrong-entity disclosure, forbidden action and other predeclared critical conditions in the defined tests/pilot. Zero observed is bounded evidence, not proof of absence. |
| **Commercial follow-through** | Useful discovery outcomes, approved follow-ups and later qualified opportunities under agreed definitions and windows. Product sales/flows require a separate credible comparison before causal revenue claims. |

Compare equivalent task populations and source snapshots, with the same acceptance rubric. Randomize task assignment or preparation order where feasible; account for learning/spillover. If comparisons are observational, say so. Agree quality tolerances and critical gates before interpreting time or cost improvements.

## Conference grounding

- **Bridgewater:** task-specific sources, time scoping and human/agent retrieval needs → glossary/capability context and relevant semantic selection. [Vault](https://ai.engineer/nyc/2026/schedule?session=a84ca3a8-cc2f-4b50-a635-fc380f6f04f6).
- **Kepler:** source, typed facts, computation and citation checks → entity/period/value equivalence, product/share-class lineage and supported packet claims. Exact verification coverage was not established. [Numerical evidence](https://ai.engineer/nyc/2026/schedule?session=2d29f925-f16b-41b3-8086-de0524829cbe).
- **Ramp:** define complete tasks and test skill/memory changes → evaluate routing, retrieval, conversation and planning on complete jobs with controlled comparisons. Reported configuration changes are not defaults. [End-to-end evals](https://ai.engineer/nyc/2026/schedule?session=4607dbbe-8f94-4b0e-91ce-257d1cfb5448).
- **Range:** specialist-authored required questions, reasons and limits → sales/product/analytics specialists author the sales-preparation method. Transfer the development method, not the retail-planning task or an unmeasured capacity claim. [Planner-authored skills](https://ai.engineer/nyc/2026/schedule?session=9b002687-09cf-42e2-9282-532ed9d0c184).
- **Two Sigma:** owners, declared access, active controls and evaluations → constrain session/task resources and action authority; assess denied cases. No measured control or classifier effectiveness was captured. [Agent boundaries](https://ai.engineer/nyc/2026/schedule?session=73badd10-6f8c-4c95-b5e7-55fc3d7bafc1).
- **Contour:** a counterfactual and cost per useful insight → measure accepted sales work against the current workflow. The notes do not establish causal ROI or a generally sufficient three-month window. [Value attribution](https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca).

**Immediate next action:** select one real sales question family and inspect its current failures, authoritative definitions, data dependencies and use inside the existing Salesforce workflow. Produce the task/evidence contract and latency baseline, then implement the smallest next release above. No internal implementation change or missing business definition has been assumed beyond the user-provided current-state facts.
