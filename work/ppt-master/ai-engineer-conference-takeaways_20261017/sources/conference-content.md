# 01 opening-cover
AI ENGINEER NYC 2026 / LEARNING BRIEFING

From AI capability to dependable work. Financial-services AI, explained through company stories, practical methods, and evidence worth questioning. AI Engineer NYC 2026 Research + attendee notes · October 13–14 For practitioners Data scientists · AI engineers · technical leads 40 minutes + discussion Five chapters · one operating story FIELD NOTES → METHODS → DECISIONS

Reader explanation:
This presentation consolidates pre-conference research and twelve identified attendee-note sets from AI Engineer NYC 2026. It is organized around methods and decisions, with company stories serving as evidence and questions rather than as a ranking.
The live path is planned for 40 minutes plus discussion. Reading mode adds detailed explanations, sources, and an evidence atlas. All material is local to this file; source links lead to the original websites.

Speaker notes:
Open with the central question: what must surround a model for it to complete useful financial work that a professional can accept? State that the talk combines attendee accounts, program context, historical firm disclosures, and our own proposed methods.

Source keys: 


# 02 opening-map
FIELD NOTES / NYC 2026 Dependable financial AI combines valuable work, grounded evidence and controlled improvement Five themes connect the company stories into one operating model: define useful work, preserve financial meaning, evaluate the whole task, enforce authority and improve through evidence.

01 Strategy Valuable work and credible economics 02 Grounding Evidence, meaning, time, access 03 Evaluation Cases, rubrics, judges, release 04 Workflows Skills, authority, verification 05 Growth Own the improvement loop Start with the business bottleneck Bridgewater targets access to relevant investment information; Range packages expert planning methods; wealth firms support advisor preparation and follow-through. These are distinct workflows. Specify the accepted work product and scarce resource before selecting a model, agent framework or platform. Make the entire path inspectable Grounding includes access, definitions, time, source versions and calculations. Reliability also depends on what the system may do and how errors are discovered. Evaluate the delivered artifact and action trajectory together, including the corrections and judgments people must still supply. Improve through a bounded comparison Ramp’s ablations and Arize’s trace loop point toward a practical discipline: reproduce the task, change one component, assess quality and full effort, then make a scoped release decision. The engineer’s contribution is a defensible improvement, supported by observable evidence.

Reader explanation:
The argument starts with valuable work, then follows the evidence and control requirements through evaluation, reliable execution, and professional growth. These responsibilities reinforce one another; no single model choice or benchmark resolves them all.

Speaker notes:
Preview the five chapters. Tell listeners that examples and source detail are preserved in reading mode, so they can focus on the argument during the talk.

Source keys: 


# 03 strategy-01
01 / FINANCE STRATEGY & VALUE The valuable unit is a reviewed financial work product Design around the analysis, brief or decision packet a professional can accept. Generation becomes useful when evidence, corrections, constraints and the next decision are included in completion.

Investment research Accepted research insight Contour: compare workflows with and without AI Wealth planning Reviewed analysis Range: draft in parallel, then review and adjust Financial communication Inspectable brief or artifact OpenAI: sources, tables, charts and artifacts Define the acceptance decision Contour described comparing research workflows with and without AI, including sources, conclusions and subsequent outcomes. Define which insight a reviewer would accept before measuring productivity; a generated idea is not automatically useful, and a useful idea does not establish investment alpha. Include review in completion Range described an agent drafting an analysis while a planner serves another client, followed by review and adjustment. Treat corrections, missing facts and professional judgment as workflow steps. Parallel drafting creates a capacity hypothesis; the notes contain no measured net gain. Make the artifact inspectable The OpenAI finance presentation connected source passages, tables, charts and reusable artifacts. A technical acceptance test should follow a material claim through its source and calculation into the final document. Polished formatting cannot establish that the underlying financial interpretation is correct.

Reader explanation:
A generated response is one component of a larger financial workflow. The useful end state may be a research insight an analyst accepts, a planning analysis a professional reviews, or a brief whose claims can be inspected. Acceptance needs a definition that includes quality and required controls, not merely user preference.
Evidence: Contour's comparison approach, Range's parallel drafting with planner review, and the OpenAI finance-interface discussion come from attendee notes. The notes do not establish causal ROI, measured advisor capacity or verified product accuracy. This slide proposes a common unit for discussing those cases.

Speaker notes:
Open with one question for the audience: what completed piece of work would matter to its user? Keep the examples concrete. For an analysis, a fluent answer is insufficient if the reviewer cannot resolve its sources or assumptions.
Explain that the deck combines 12 session-note sets with explicitly marked program and historical context. Speaker accounts are inputs to engineering decisions, not verified performance results.

Source keys: S01, S02, S03


# 04 strategy-02
01 / FINANCE STRATEGY & VALUE Different financial bottlenecks require different success criteria Compare the scarce resource each system addresses: timely evidence, professional attention, permitted execution or accepted engineering output. The same adoption metric cannot describe value across all four contexts.

Company story Bottleneck addressed Mechanism Bridgewater Information reaches a decision Time-scoped retrieval and evidence-backed summaries Range Planner work is prepared in parallel Expert-authored methods and professional review Two Sigma Useful agents operate within boundaries Registry, declared access and active controls Monzo / Optiver Engineering scales through a supported path Shared runtime, task certification and routing Information and attention differ Bridgewater described a shared repository with different human and agent retrieval needs; Range described parallel preparation with planner review. Evaluate evidence coverage and final brief relevance for the first pattern, and accepted analysis plus total professional effort for the second. Utility depends on boundaries Two Sigma described registration, declared resources, active controls and approval triage. The engineering question is which useful tasks remain possible within those boundaries. Test both permitted and denied actions, then inspect missed consequential cases rather than equating registration with effective protection. Platforms must earn support Monzo's program describes a shared runtime and Slack distribution; Optiver's describes task certification, routing and an experiment funnel. These patterns suggest evaluating discovery, access, review and support alongside model quality. Their program descriptions do not establish causal firmwide engineering savings.

Reader explanation:
A financial-services AI landscape is easier to compare when the workflow and bottleneck are explicit. An investment information foundation, a financial-planning skill and an internal engineering agent have different success criteria, risk exposures and operating constraints. This map is a selected set of cases, not a representative survey or firm ranking.
Evidence: Bridgewater, Range and Two Sigma are recorded attendee accounts. Monzo's shared agent runtime and Optiver's certification/routing approach remain descriptions from the earlier official program. Those engineering cases do not establish autonomous trading, banking or causal firmwide savings.

Speaker notes:
Use this map to establish breadth without turning the presentation into a company catalog. Ask which resource is scarce in each case: evidence, professional attention, safe execution or accepted engineering output.
Mention that mechanisms can transfer across firms while success measures often cannot. The next chapters will examine what each workflow needs from its data, evaluation and runtime.

Source keys: S04, S02, S05, S06, S07


# 05 strategy-03
01 / FINANCE STRATEGY & VALUE Wealth AI connects preparation, institutional knowledge and professional review The concrete wealth examples augment recognizable advisor work. Compare their mechanisms while preserving dates, review responsibilities and the distinction between reported deployment, useful outputs and demonstrated client outcomes.

Range Expert-authored planning Parallel drafts; planner reviews and adjusts. October 2026 Morgan Stanley Meeting to follow-up Consent-based notes, action items and draft follow-up. June 2024 UBS Institutional knowledge Advisor access to products, research and CIO reports. February 2025 RBC Client-context preparation Meeting preparation using relevant client information. March 2025 Encode the planning method Range's planners package what client information exists, how to obtain it and how their firm prepares recommendations. Agents draft cash-flow or insurance analyses; planners review and adjust them. Measure accepted planning capacity after correction effort before claiming improved advice or throughput. Connect meetings to follow-through Morgan Stanley's June 26, 2024 release describes consent-based Debrief notes, action items, advisor-edited follow-up and CRM capture. Its separate Assistant adoption claim does not demonstrate Debrief productivity. Assess the complete meeting-to-follow-up process, including consent, accuracy, corrections and the advisor's final decision. Preserve historical evidence boundaries UBS's February 4, 2025 release describes advisor knowledge access through Red. RBC's March 27, 2025 materials describe client-context preparation alongside survey and pilot measures. These historical disclosures illustrate different workflows; neither rollout scope nor pilot conversion establishes universal deployment or causal revenue.

Reader explanation:
The common wealth-management pattern is augmentation of a professional workflow. Range's recorded example drafts another client's analysis while a planner is on a call, then leaves review and adjustment with the planner. Morgan Stanley's historical release describes consent-based meeting capture and advisor-edited follow-up. UBS and RBC provide public examples of advisor knowledge access and preparation.
Evidence: Range's identity was confirmed by the attendee and matched to Matt Ragone's official session. Its notes omit explicit evidence/maturity labels and contain no measured benefit. The other three cases are dated company disclosures; they are not independent evaluations or NYC attendance evidence. The RBC presentation's conversion measure is US-pilot based, and its adoption/satisfaction measures are separately labeled survey results.

Speaker notes:
Use the four cards to show a pattern, then make the boundary clear: generating a draft is different from authorizing advice or demonstrating better client outcomes. The professional's review is an observable part of the workflow and must be included in any productivity measure.
Keep the historical dates visible. Do not introduce the cases as the latest industry state, or compare their adoption percentages as if the denominators and tools were the same.

Source keys: S02, E01, E02, E03, E04


# 06 strategy-04
01 / FINANCE STRATEGY & VALUE Business value requires evidence beyond adoption and accepted output Track a chain from use to accepted work, process improvement and attributable outcomes. Each step changes the claim being made and therefore requires a different comparison and evidence.

01 Adoption Usage by task and cohort 02 Accepted work Quality, critical failures, reviewer effort 03 Process change Time, throughput, capacity, reliability 04 Attributable value Comparable baseline, full costs, uncertainty Separate use from usefulness Count who uses a system, for which tasks, and what outputs reviewers accept, correct or reject. Define usefulness before examining downstream outcomes. Adoption can coexist with heavy rework, and an accepted answer may still leave the underlying business process unchanged. Establish the credible alternative Contour's notes describe AI and non-AI workflow tracking over roughly three months. The relevant question is what would have happened otherwise, at what quality, effort and timing. The notes do not specify randomization or controls, so the comparison cannot establish causal alpha. Preserve decisions through time For investment research, retain the information available when an idea was generated, its reasoning, reviewer response and subsequent decision. This prevents successful outcomes from being reconstructed with hindsight. Report process improvements separately from returns influenced by markets, selection and other drivers.

Reader explanation:
Contour's notes ask whether the research process would have reached the same conclusion without AI and describe a comparison/tracking approach over roughly three months. This gives an actionable measurement question, but the notes do not specify random assignment, comparable groups, contamination control or a causal return estimate. Three months is a reported window, not a universal ROI-validation period.
The ladder keeps different claims from collapsing into one success story. A widely used assistant can still require substantial corrections; accepted work can improve a process without a financial effect being attributable to AI. For research, preserve point-in-time inputs and decision lineage to avoid reconstructing success with hindsight.

Speaker notes:
Walk upward one step at a time. Ask what extra evidence would justify the next claim. Use Contour's cost-per-useful-insight idea to make the denominator concrete: useful must be defined before the outcome is known.
Emphasize that a good conference report can bring back a measurement method without claiming verified alpha. The same distinction applies to advisor adoption, conversation volume and merged pull requests.

Source keys: S01, S06


# 07 strategy-05
01 / FINANCE STRATEGY & VALUE Count every attempt and human intervention in accepted-task economics A lower inference bill can conceal greater review, retry or maintenance work. Compare equivalent tasks at agreed quality, using all workflow costs and reporting accepted completion alongside cost.

Proposed measurement Total workflow cost ÷ accepted tasks Attempts + tools + review + rework + operation Same task Baseline and candidate face equivalent work. Same standard Acceptance criteria and critical limits are agreed. Full effort Count the work that people still perform. Include downstream operating work Record inference, data, tools, retries, selection, human review, rework and support costs. If several candidates are generated before one is accepted, all attempts belong in the numerator. A cheaper draft is not cheaper completed work when correction effort rises. Qualify before optimizing cost Optiver's program describes routing to models certified for particular tasks. The transferable idea is a task-specific quality requirement before price optimization. A qualification must cover consequential failures and operating conditions; certification on one workload does not establish readiness for another. Keep the denominator honest Define eligible tasks, accepted completion and exclusions before comparing workflows. Include failed and abandoned attempts in total costs, then report accepted-task rate beside cost per accepted task. Otherwise narrowing the task population can make an unchanged system appear economically better.

Reader explanation:
A cheap model response can create expensive downstream work. A fair comparison records the cost of all attempts, the work needed to select or repair an output, and the services needed to operate the workflow. Compare equivalent workloads and accepted quality; otherwise the denominator changes while the metric appears to improve.
Evidence: Contour's attendee notes provide the value/cost-per-useful-insight framing. Optiver's task certification and routing to qualifying models remain program background. The all-in-cost stack is an editorial measurement proposal. Neither source establishes avoided headcount, causal firmwide savings or a generally optimal model-routing policy.

Speaker notes:
Use a failure example rather than made-up numbers: a retry that requires another review belongs in the cost, even if the final artifact is accepted. Ask whether a faster draft actually frees professional time after corrections.
Hand off to grounding: now that the unit of value is clear, the next question is which facts, sources and calculations make that work defensible.

Source keys: S01, S07


# 08 grounding-01
02 / GROUNDED AGENTS Time, meaning, and access define the financial question an agent can answer Bridgewater’s Vault discussion connects institutional knowledge to time, business meaning, and access. These boundaries should shape retrieval before the model assembles a persuasive answer.

01 Request Entity · task · as-of date 02 Evidence boundary Allowed sources · entitlement · effective time 03 Meaning Ontology · metric definitions · versions 04 Context Relevant evidence · explicit gaps 05 Answer Supported claims · uncertainty Scope before retrieving evidence Bridgewater describes combining external research, news, and transcripts with internal information, organized around market, country, concept, and time. Translate the request into an explicit entity, decision, and information cutoff before selecting sources; a broad corpus alone does not define relevance. Enforce access during retrieval The Bridgewater and turbopuffer permissions case describes enforcing user-level permissions in retrieval. Test whether the current user may see each returned source, including after access changes. Application checks or a valid tool credential alone do not establish correct resource access. Carry definitions into context A model can retrieve the right document while answering with the wrong business definition. Include the intended metric, reporting period, entity scope, and source version in the context contract. Surface conflicting definitions or missing evidence instead of silently selecting one.

Reader explanation:
Bridgewater’s Vault presentation, captured in the attendee notes, describes external and internal unstructured information with an ontology organized around market, country, concept, and time. The notes emphasize restricting the relevant time period and serving both people and agents. The official program reports production use of Vault/PAT; this is a speaker-reported deployment claim rather than an independent quality result.
The separate Bridgewater/turbopuffer permissions session is agenda-only background here: its abstract describes user-level permissions enforced at retrieval. It was not one of the supplied attended-note blocks. The diagram is our proposed method combining these ideas with Kepler’s source-verification discussion; it does not claim to reproduce either company’s implementation.

Speaker notes:
Start with the boundary of the answer. A model cannot repair an omitted source, a definition that means different things to two desks, or permission that was never enforced. Ask the audience to identify where their own system checks time, identity, and meaning.
Keep the company evidence precise: Vault’s production status is reported, while the effect of a particular ontology or filter was not measured in these notes.

Source keys: S04, S08, S09


# 09 grounding-02
02 / GROUNDED AGENTS Human attention and agent coverage require different retrieval objectives Bridgewater contrasts compact, high-signal human search with broader agent retrieval. Evaluate evidence collection and the final human-facing brief separately, while preserving shared checks on relevance, access, and freshness.

Design question Human-facing search Agent-facing retrieval Observed emphasis Precision and signal-to-noise Recall and scale Consumption Small, reviewable result set Fast processing of more evidence Shared checks Permissions • meaning • freshness Permissions • meaning • freshness Protect scarce human attention The Vault notes emphasize precision and signal-to-noise for people consuming a small result set. A brief should make the important development easy to inspect without burying it in irrelevant material. Human review effort belongs in the evaluation alongside answer quality. Test coverage before compression An agent may need broader retrieval to avoid missing decisive evidence, but irrelevant context can still distract it. Measure whether required sources are found, then whether synthesis preserves their meaning. Do not assume a larger context window or result count improves the answer. Evaluate the delivered feed Bridgewater’s investor-workbench examples include activity feeds and evidence-backed summaries around what an investor might be missing. Compare relevance, important omissions, timeliness, and review time against the existing information flow. The examples do not establish changed habits, predictive accuracy, or investment returns.

Reader explanation:
The attendee recorded a contrast between human search needs—precision, high signal-to-noise, and small scale—and agent needs—broad recall, scale, and fast consumption. This is useful for choosing an evaluation workload, but agents cannot ignore precision and people sometimes need exhaustive recall. No benchmark result or optimal retrieval setting was captured.
The notes also describe activity feeds, “What am I missing?” surfaces, and evidence-backed summaries intended to steer investor attention. They contain contradictory reactive-to-proactive wording, so this slide avoids attributing an exact directional claim. New-feature deployment scope and measured impact are not established.

Speaker notes:
Use the matrix to ask what failure each consumer tolerates. For a human, irrelevant results can consume scarce attention; for an agent, missing the decisive source can make a polished answer wrong. The shared contract is evidence quality.
If discussing feeds, describe attention steering as reported functionality. Do not promise that a feed changes habits, predicts markets, or improves returns.

Source keys: S04


# 10 grounding-03
02 / GROUNDED AGENTS Every reported number needs meaning, source history, and calculation lineage Kepler describes retrieval, code-based arithmetic, typed facts, and citation checks. The engineering implication is an inspectable evidence contract, not a guarantee that a citation makes a financial conclusion correct.

01 Retrieve evidence 02 Compute deterministically 03 Register typed facts 04 Validate rendered claims Entity Metric Period Unit / currency Value Source version / passage Separate retrieval from arithmetic Kepler’s account distinguishes finding source material from calculating a result. Code can make arithmetic reproducible, but it cannot establish that the selected input represents the intended entity, period, or definition. Evaluate input selection and calculation correctness as separate failure classes. Register meaning with values A useful typed-fact contract carries entity, metric, period, unit, currency, source version, and passage alongside the value. These extended checks are proposed requirements, not verified Kepler coverage. Retain calculation inputs and transformations so another reviewer can reconstruct the reported figure. Make failed support visible Citation repair may recover an exact value or formatting variant without resolving a semantic mismatch. Test what happens when support still fails: remove the claim, abstain, or escalate. Stripping a citation while retaining the unsupported sentence would not make the answer trustworthy.

Reader explanation:
Kepler’s presentation notes describe an LLM-generated plan, source retrieval, code-based calculation, a citation registry carrying metadata and typed facts, and citation repair/filtering. The key transferable idea is to make the path from a figure to its source and calculation inspectable. The notes do not establish a complete ordered architecture or prove that every generated fact is deterministically correct.
The entity/period/unit/currency/restatement checks shown here are proposed requirements. They appeared in a prefilled question without a recorded answer, so they must not be presented as verified Kepler coverage. Exact-match or formatting repair can recover a citation while still leaving a semantic mismatch. The recorded 3× overfetch, 100 per namespace, maximum 5 per document, and top-20 wording are ambiguous implementation examples, not recommended defaults.

Speaker notes:
Point to the typed fact, not only the citation icon. A cited value can still belong to the wrong period or unit. Code arithmetic solves one failure class; it does not select the right input by itself.
Explain that abstention and repair behavior need testing. “Verified citation” is not a blanket guarantee of a correct financial conclusion.

Source keys: S09


# 11 grounding-04
02 / GROUNDED AGENTS Correct arithmetic can produce the wrong answer when the source is stale This synthetic AsterCo example separates calculation correctness from source validity: preliminary revenue produces 18% growth, while the final source available at the requested cutoff produces 20%.

Illustrative example AsterCo: FY2025 revenue growth as of March 1, 2026? Invented document USD m Treatment FY2024 final 100 Prior-year input FY2025 preliminary 118 Superseded FY2025 final 120 Current-year input Synthetic calculation (120 − 100) / 100 = 20% Using 118 gives 18%: correct arithmetic on the wrong source version. Apply the information cutoff All company data and documents here are invented. The March 1 cutoff permits the February 1 final report, which supersedes the preliminary version. Source eligibility depends on what was available then; selecting today’s latest document would not answer every historical question. Recompute the dependent claim Using preliminary revenue of 118 against prior-year revenue of 100 gives 18%; using final revenue of 120 gives 20%. Both calculations are arithmetically valid. A source correction must update the derived figure and any narrative or chart that depends on it. Preserve the rejected version Retain the chosen inputs, publication dates, calculation, and reason the preliminary source was superseded. That record explains why the answer changed and supports later reproduction. Extend the test to missing, conflicting, restated, and unauthorized sources before claiming dependable financial analysis.

Reader explanation:
All company names, documents, publication dates, amounts, and results in this example are invented for teaching. The exercise is not a result achieved by Kepler, Bridgewater, Fidelity, or any real company, and is not investment advice. It illustrates a source-version failure that deterministic arithmetic alone cannot prevent.
The chosen as-of date permits D3, while the earlier D2 is superseded. A complete evidence record retains the entity, definition, period, units, source choice, and calculation. A different as-of date could require a different source or an explicit uncertainty statement. This proposed contract should be evaluated on stale, conflicting, absent, and unauthorized evidence before claiming production reliability.

Speaker notes:
Ask for the answer before revealing the treatment column. Eighteen percent is mathematically valid for the preliminary inputs; twenty percent follows from the final inputs. That difference is the point.
Close by asking what a citation registry must retain for another person to reproduce the answer later. Remind the audience that these are fictional values, not a market example.

Source keys: S09


# 12 grounding-05
02 / GROUNDED AGENTS Inspectability must survive the journey from source passage to exported artifact OpenAI’s finance presentation described source passages, tables, charts, and generated documents. Connect these interfaces to an evidence contract that remains usable in the artifact people review and share.

01 Source passage Inspect the relevant excerpt and version 02 Typed table Values, units, periods, and source references 03 Chart Visible inputs and transformations 04 Reusable artifact Preserved provenance and unresolved limits Connect claims to passages The OpenAI discussion links financial data access with interfaces for inspecting passages and tables. Keep the relevant evidence near consequential claims rather than providing a generic source list. Product availability, provider entitlements, and the exact citation implementation still require confirmation. Carry provenance through transformations A correct intermediate value can become misleading when an exported chart drops its unit, period, or source version. Preserve typed fields and calculation lineage through tables, charts, and documents. Test the delivered artifact, including formatting changes, rather than only the model response. Evaluate the reviewer’s task Inspectability makes review possible; it does not prove that a reviewer finds an error or that the source supports the claim. Measure whether someone can locate evidence, understand transformations, detect planted mistakes, and correct the final artifact without reconstructing the entire workflow.

Reader explanation:
The OpenAI keynote notes describe finance-oriented interfaces, source passages, tables, interactive charts, and document/presentation artifacts. These are speaker-reported capabilities, with maturity and available-now versus roadmap distinctions unclear in the capture. This slide intentionally avoids naming uncertain data providers or asserting partnership, entitlement, licensing, or current rollout availability.
The proposed output stack connects the interface discussion to the provenance problem. Inspectability makes review possible; it does not establish source entailment, numerical correctness, or an effective reviewer. The evidence contract must survive export into the table, chart, or document the user actually consumes.

Speaker notes:
Use the stack to show how evidence can get lost after generation. A correct intermediate value is less useful if the exported chart omits its unit, period, or source.
Keep vendor discussion at the level actually captured. Attractive citations and interactive charts still need end-to-end checks.

Source keys: S03, S09


# 13 evals-01
03 / BUILDING EVALUATIONS Evaluate the complete job against an explicit acceptance contract A useful evaluation states the decision, permitted behavior, and accepted work product before scoring. Task quality, evidence, safety, experience, and operating effort then become separate tests.

01 Specify Job, permitted inputs, acceptance 02 Build cases Common, difficult, missing, denied 03 Score Task, evidence, safety, experience 04 Decide Versioned evidence + accountable review Write the task contract Specify the request, input snapshot, allowed sources and tools, required output, clarification conditions, and prohibited actions. Ramp’s task mapping starts here: judge the result against the complete job the user needed, including evidence and the next permitted decision. Cover consequential failure paths Build cases for ordinary work, ambiguity, missing evidence, denied actions, and known regressions. The system-failure discussion emphasizes that a correct output can conceal an unacceptable trajectory. Record which failure each case tests and how a reviewer recognizes it. Separate diagnostics from acceptance Score usefulness, source support, experience, latency, cost, and review effort individually. Predeclare which failures block acceptance regardless of other scores. Version cases and rubrics, preserve expert disagreement, and reserve assessment examples that were not used to tune the system.

Reader explanation:
A useful evaluation begins with a decision: selecting a system, approving a change, reducing review, or extending authority. Describe what a completed job means, which sources and tools may be used, what must be clarified, and which failures are unacceptable. Then select the measurements needed for that decision. A single average can conceal a serious safety or evidence failure.
Build cases from the intended workload and consequential failure paths. Each case should contain its input/context snapshot, allowed actions, required evidence, expected output properties, and severity tags. A reference answer can help, but open-ended work may admit several acceptable answers. Keep development examples separate from the final assessment set; do not assume a small case set proves population reliability.
Provenance: Ramp's job/task-success framing, the Day 1 system-failure discussion, and the banking session's quality-vector framing are attendee-reported speaker accounts, not independently verified results. The banking speaker is Jonathan Osborne; the notes/October 10 metadata say Comet, while October 14 metadata say NatWest. This slide does not assign a production architecture or outcome to either institution.

Speaker notes:
Start with the work a user accepts, rather than a benchmark score. Ask the audience to imagine an agent with excellent prose and incorrect permissions: an average quality score would give the wrong release signal. Separate diagnostic scores from conditions that must hold.
Walk quickly through the five case slices. The practical starting artifact is a case record plus rubric, not an elaborate evaluation platform. We will make that concrete on the next slide.

Source keys: S10, S11, S12


# 14 evals-02
03 / BUILDING EVALUATIONS Score arithmetic and source validity independently to locate the actual defect The synthetic cash-flow example separates correct computation from correct evidence selection. An answer can earn arithmetic credit while failing the complete task because its input is superseded.

Illustrative example Draft a monthly cash-flow snapshot. Use current approved records. Do not recommend or send. Synthetic input Value Income $8,000 / month Current expenses $6,000 / month Superseded expenses $5,500 / month Insurance details Missing Rubric dimension Scoring / acceptance Arithmetic 0: wrong · 1: correct but derivation incomplete · 2: correct and reconstructable Source validity Use current $8,000 and $6,000 inputs; a superseded input fails this dimension Uncertainty State missing insurance facts and the needed clarification Action boundary BLOCK recommendation or send; scores cannot offset it Grade calculation and inputs Check arithmetic on the operands the answer actually states, then assess whether those operands answer the requested question. Give source validity its own rubric covering period, version, permissions, and provenance. This keeps an input-selection failure from being misdiagnosed as faulty subtraction. Diagnose the stale-input example In this invented case, $8,000 minus superseded expenses of $5,500 correctly produces $2,500, but fails current-source validity. Approved expenses of $6,000 produce $2,000. Both calculations can be arithmetically sound; only the latter uses the current input required by the task. Block explicitly forbidden behavior For this draft-only teaching task, a product recommendation or outbound message blocks acceptance even if diagnostic scores are high. Missing insurance facts must remain explicit. The diagnostic rubric needs domain review and calibration before use on real work.

Reader explanation:
Every value, case, score guide, and output on this slide is synthetic and was authored for this presentation. The example is a draft financial-information task, not financial advice, a Fidelity test, or a benchmark used by any conference speaker. The general lessons connect Ramp's task-success framing with the notes on numerical evidence and risk-based evaluation.
The worked failure shows why dimensions should remain visible. Subtracting a stale expense value can yield flawless arithmetic and an incorrect answer to the current-period question. A separate action-boundary gate prevents diagnostic scores from compensating for prohibited behavior. The 0–2 scales are illustrative; a real rubric needs domain review, explicit exceptions, and calibration on representative cases.
Acceptance here requires the expected properties and respected boundary. The rubric is intended to make disagreements diagnosable: was the error in input selection, computation, missing-information handling, or action control? It does not imply that passing one example demonstrates advice quality, broad safety, or production readiness.
Rubric clarification: arithmetic is checked on the operands the answer actually states. A $2,500 calculation can earn arithmetic credit if it correctly subtracts $5,500 from $8,000, while failing source validity and the complete task because the $5,500 expense record is superseded. Do not double-count source selection as an arithmetic defect.

Speaker notes:
Ask: Is $2,500 an arithmetic failure? The subtraction is correct for the old record, which is exactly why one accuracy label is too coarse. The real failure is selecting the wrong version. Walk through the acceptable draft and its explicit limit on insurance information.
Then point to the action gate. The proposal is to keep a forbidden action outside a weighted average. These are invented teaching numbers and conditions; the point is the structure, not a recommended universal threshold.

Source keys: S10, S09, S11


# 15 evals-03
03 / BUILDING EVALUATIONS Calibrate the judge and evaluate how the system selects a usable answer Reliable evaluation requires both a trustworthy grader and a tested candidate-selection policy. A passing attempt, a selected acceptable output, and consistent first-attempt success describe different system behaviors.

Illustrative example Human accepts Human rejects Judge passes Agreement False pass Missed consequential failure Judge fails False failure Lost utility / review burden Agreement Synthetic attempt illustration 1 · fail 2 · pass 3 · fail One success among three attempts Who recognizes the usable answer? What are retry, verification, latency, and review costs? Calibrate against reviewed cases Compare judge decisions with independently reviewed examples and adjudicate important disagreements. Inspect serious false passes separately from overall agreement. Upstart’s announced account describes judges earning trust against human graders; stricter grading alone can also increase false failures and review burden. Separate attempts from selection pass@k concerns at least one successful candidate among k attempts under a defined test. In the synthetic three-attempt strip, the second candidate passes. That establishes neither the system’s ability to choose it nor reliable first-attempt completion of the deployed task. Price the deployed retry policy Report the acceptance test, k, single-attempt results, selection success, and total retry cost together. Evaluate the actual selection or verification mechanism under the same attempt budget. Include latency and human review; a benchmark’s successful candidate may remain unrecognized in operation.

Reader explanation:
Treat the judge as another evaluated system. Use independently reviewed examples, retain expert disagreement, and adjudicate important conflicts rather than treating one person's label as infallible. Check high-consequence false passes separately from overall agreement. A fail-leaning judge can also reject useful work and increase human burden; stricter grading is a hypothesis to test, not proof of reliability.
In standard pass@k evaluation, a task counts as solved when at least one of k sampled candidates meets the specified test, then results are summarized across tasks. It measures a multi-attempt success opportunity, not the reliability of the first answer or the deployed system's ability to choose a correct candidate. The primary HumanEval paper explicitly separates oracle-like selection from practical candidate selection. No numerical result from that paper or from a company is claimed here.
Provenance: Ramp's Day 2 notes mention pass@k without k, scoring rules, or results. The banking session records a fail-leaning configurable judge, with Comet/NatWest affiliation unresolved. Upstart's advertised abstract describes human calibration for voice-agent judges; it is agenda evidence, not an attendee observation. Its automated self-improvement loops are described as under development, not achieved self-healing.

Speaker notes:
Spend the first half on the dangerous top-right cell: the judge passes an unacceptable output. Ask whether a system could have excellent average agreement while missing rare severe defects. Then acknowledge the opposite cost: a judge that fails everything is not useful.
Use the attempt strip to prevent a common metric misunderstanding. There is one successful candidate, but someone must recognize it. The end-to-end retry and selection policy must be evaluated and costed. The illustration is one synthetic case, not an empirical pass@3 estimate.

Source keys: S10, S12, S13, E05


# 16 evals-04
03 / BUILDING EVALUATIONS Hold the workload fixed while testing one system change at a time Ablations make context, skills, memory, and model changes accountable to the complete job. Paired comparisons reveal improvements and regressions that disappear when task mix or grader behavior changes.

Variant Task + evidence Critical defects Human effort Cost / latency Baseline Measure Inspect Measure Measure Skill bundle Paired change New regression? Paired change Paired change Memory policy Paired change Stale facts? Paired change Paired change Model Paired change New regression? Paired change Paired change Control the comparison conditions Replay baseline and candidate on matched tasks with the same source snapshots, permissions, rubric, evaluator version, and attempt policy. Change one component where feasible. Repeat stochastic assessments to inspect variation and paired failures; one aggregate run can conceal an unstable advantage. Use ablations to challenge intuition Ramp described reducing an eight-skill bundle to four, shrinking an Excel skill, and what it called trajectory-distilled memory: memory derived from prior agent runs. The notes do not capture its construction or measured effect. Test each component’s contribution instead of assuming that more memory or fewer skills always helps. Protect an independent assessment set Turn discovered failures into regression cases, while retaining a separate assessment set covering ordinary and difficult work. Compare evidence quality, critical defects, review effort, latency, and full cost. A fix earns its place only within explicitly agreed quality and operating tradeoffs.

Reader explanation:
Compare changes on matched cases so that task mix, source freshness, or grader changes do not masquerade as an improvement. Where feasible, vary one component at a time. For stochastic systems, use repeated assessments sufficient to examine uncertainty; compare distributions and important failure examples rather than only a single run's aggregate.
Ramp's Day 2 notes record experiments described as working: reducing an eight-skill bundle to four, trajectory-distilled memory, and shrinking an Excel skill. No effect sizes, controlled assessment details, or repeated-run results were captured. The method motivates an ablation design; the recorded counts are neither recommended defaults nor proof that reducing context always helps.
The proposed matrix adds explicit review and full attempt cost to the quality vector. Retest a discovered failure, but retain an assessment set not selected solely because it contains known failures. Otherwise an iteration can overfit the observed incidents while harming ordinary work. This is editorial methodology, not a claim that Ramp followed this exact protocol.

Speaker notes:
The point is not to build this entire matrix before starting. Choose the next decision, hold the case set fixed, and compare one candidate against a working baseline. Show that even a seemingly obvious improvement—another skill, more memory—must earn its place.
Ask what would change our mind: better average scores with a new high-severity failure should trigger investigation, not an automatic win. Separate the cases used to fix a problem from those used to assess the final change.

Source keys: S10, S11, S14


# 17 evals-05
03 / BUILDING EVALUATIONS Release decisions need explicit blockers, accountable judgment, and bounded exposure A release gate combines critical conditions with useful-work evidence and an accountable decision. Passing a finite suite supports a scoped judgment; it cannot establish that consequential failures are impossible.

Blocking conditions Unauthorized action · unsupported consequential number · omitted required approval Quality & economics Task acceptance · paired regressions · judge validity · uncertainty · review cost 01 Evidence packet Cases, versions, traces 02 Accountable decision Investigate or promote within scope 03 Staged operation Monitor, stop, roll back Declare blockers before scoring Specify prohibited access or actions, unsupported consequential claims, and omitted approvals before reviewing candidate results. Keep these conditions outside a compensating average. The banking session’s quality-vector discussion motivates multidimensional review, but supplied no captured release threshold or implemented rollback policy. Assemble a reviewable evidence packet Retain intended scope, task and evaluator versions, results by important slice, representative traces, material regressions, expert disagreements, and known limits. Name the accountable decision owner and record accepted exceptions. Inadequate evidence is a reason to investigate before expanding exposure. Limit promotion and monitor outcomes Promote only within agreed scope, with operational monitoring and explicit pause, rollback, or renewed-review conditions. A clean finite assessment does not prove zero risk. Broaden or repeat testing when unresolved uncertainty could change the decision, and retain authority outside automated diagnosis.

Reader explanation:
Define the release decision's standard before seeing the candidate's results. Critical conditions may include unauthorized access, unsupported consequential claims, or missing required approval; which conditions block a release is a domain decision. Keep those conditions separate from graded usefulness. A finite assessment can support a bounded decision, but a clean test run is not a proof of zero risk.
Retain a reviewable evidence packet: intended use and scope, case/evaluator/system versions, results by important slice, material disagreement, representative traces, known limitations, exception decisions, and operational stop conditions. Repeat or broaden assessment when uncertainty could change the decision. Do not invent a universal pass threshold or regard a single combined accuracy score as sufficient.
The banking notes record multidimensional quality and a configurable fail-leaning judge, but no actual reviewer approval package, release threshold, or rollback trigger. Its current NatWest versus earlier Comet attribution remains unresolved. The gate shown here is an editorial proposal informed by that discussion and the Day 1 system-failure perspective; it is not attributed as an implemented bank policy.

Speaker notes:
Return to the synthetic rubric: excellent arithmetic cannot compensate for an unauthorized send. The gate preserves that logic at release level. Ask the team to name a blocker and the evidence needed to test it, rather than choose a convenient overall percentage.
Emphasize bounded scope and accountable judgment. Tests inform a release decision; monitoring and rollback address what the suite did not foresee. We are not claiming that any speaker supplied this exact evidence packet.

Source keys: S12, S11, S05


# 18 evals-06
03 / BUILDING EVALUATIONS Convert production failures into reviewed tests before changing agent behavior A controlled improvement loop connects observations to reproducible cases, assessed changes, and authorized releases. Trace analysis can suggest a repair; evidence and accountable judgment determine whether that repair should operate.

01 Observe Traces + corrections 02 Adjudicate Find the failure mechanism 03 Test a repair Regression + assessment cases 04 Release in scope Monitor; pause or roll back Capture enough context to reproduce Record the request, permitted sources and actions, tool interactions, output, human correction, and relevant versions. Triage whether the defect concerns evidence, reasoning, runtime behavior, or the evaluator itself. Handle traces under existing access rules; observability does not authorize exposing sensitive content. Turn diagnosis into an experiment Arize described using agent traces to identify issues and improvement opportunities. Reproduce a suspected failure, add a versioned case, and propose a specific change. Assess it against regressions and separate cases before accepting the diagnosis; automated suggestions are still hypotheses requiring verification. Keep release authority explicit Require accountable review before a proposed repair changes production behavior, then monitor escaped defects, corrections, drift, and full operating cost. Upstart’s announced self-improvement loops remained under development. Use these accounts to design a controlled process without assuming autonomous remediation has been demonstrated.

Reader explanation:
Connect monitoring to decisions and experiments, not merely dashboards. Capture enough context to reproduce important behavior: request, available sources and permissions, tool interactions, output, reviewer correction, relevant versions, and evaluation results. Authorized handling of traces and sensitive data remains a prerequisite; collecting more telemetry is not permission to expose private content.
Arize's Day 1 notes describe a build/evaluate/trace-inspection/improvement loop and agents consuming telemetry. The product and skill names were recorded uncertainly, and no diagnostic accuracy or autonomous remediation result was captured. The controlled loop shown here adds explicit adjudication, assessment separation, and release authority as editorial recommendations.
Upstart's advertised session describes moving from human call review toward human-calibrated judges, with automated self-improvement loops still being built. That is agenda-based, speaker-reported context rather than an attended-case result. Use it to ask what evidence permits reduced review; do not present it as proof that a self-healing production system was achieved.

Speaker notes:
Close the chapter by tracing a failure around the loop. The failure becomes a test; a proposed change must prove it helps without causing an unacceptable regression. An agent can assist with diagnosis or propose a skill edit, while approval to change production remains explicit.
Give the team a manageable next step: one workflow, a small reviewable case set, a rubric, and a baseline. Add infrastructure when the working loop requires it. Invite discussion about which failure class deserves the first dedicated test.

Source keys: S14, S11, S10, S13


# 19 workflows-01
04 / RELIABLE WORKFLOWS & SKILLS Reusable skills must encode expert reasons, required questions, and limits Range’s planners describe turning their own methods into agent skills. Pick–Teach–Pack–Test–Ship makes judgment explicit, while ownership and peer review keep the instructions maintainable as practice changes.

01 Pick Repeatable work • recognizable success 02 Teach Narrate why in a representative case 03 Pack Inputs • questions • boundaries 04 Test Ordinary cases • edge cases • review 05 Ship Owner • reviewer • change history Teach the firm’s method Range distinguishes general planning knowledge from how its professionals deliver recommendations. Start with a repeated workflow whose result an expert can judge, then narrate a representative case and the reasons behind decisions. Capture judgment rather than asking the agent to imitate a polished answer. Package questions and limits A skill needs required client inputs, ways to obtain authorized information, clarification questions, and boundaries it must respect. Missing facts should change the workflow, not invite invented assumptions. Make exceptions and handoff conditions explicit enough to test on difficult cases. Maintain an accountable instruction Range’s current abstract describes planners maintaining skills and peer-reviewing them like plans. Assign an owner and reviewer, retain change history, and retest revisions. Include incomplete facts and conflicting instructions to check when the skill clarifies, hands off or refuses an unsupported conclusion.

Reader explanation:
The user confirmed that the financial-planner example was Range. The refreshed official schedule identifies Matt Ragone and “We Let Our Financial Planners Write the Agents.” The attendee notes capture the five-step skill-building method and human-reviewed drafting while a planner works with another client. The fresh abstract says planners write and maintain skills used daily and peer-review them like plans; this supports speaker-reported operational use, not independently verified outcomes.
Owner/reviewer requirements are fresh agenda context rather than a detail captured in the freeform notes. The abstract’s six-month/24-skill/17-planning-skill figures and five-to-ten-case testing example are not universal targets and are intentionally omitted from the visible method. Source identity must be versioned: this UUID referred to an NVIDIA reranker session in the October 10 snapshot and to Range in the October 14 snapshot.

Speaker notes:
Emphasize the difference between general financial knowledge and how a firm performs a particular workflow. Domain experts can make required questions and limits explicit, while technical teams help make the behavior inspectable and testable.
A skill is a maintained work instruction with ownership. The five steps organize the work; they do not guarantee appropriate advice or safe deployment.

Source keys: S02


# 20 workflows-02
04 / RELIABLE WORKFLOWS & SKILLS Drafting useful work does not grant permission to recommend or act The synthetic review packet separates authorized facts, agent preparation, professional judgment, and execution. Its USD 36,000 arithmetic difference supports inspection, not an affordability conclusion or a product recommendation.

Illustrative example SYNTHETIC REVIEW PACKET · FICTIONAL CLIENT A 01 Authorized facts Income $120k · recorded expenses $84k 02 Agent draft Arithmetic difference: $36k 03 Planner review Inspect facts, assumptions, gaps 04 Separate authority No action without permission Separate facts from judgment The fictional inputs show annual income of USD 120,000 and recorded expenses of USD 84,000. Their USD 36,000 difference is arithmetic, not disposable capacity or an insurance need. The agent should expose missing facts and assumptions rather than infer suitability from this subtraction. Make review a decision Range’s vignette has an agent draft another client’s analysis while a planner serves someone else, followed by review and adjustment. A useful review packet exposes inputs, calculations, gaps, and proposed conclusions. Evaluate accepted work after corrections, rather than counting drafts as completed professional service. Keep execution authority separate Wise’s framework description separates model proposals from authority to act. In this proposed workflow, reviewing a draft does not automatically authorize sending it or executing a transaction. A separate service should enforce the permitted action and retain who approved it, for which case.

Reader explanation:
This fictional workflow illustrates the Range note’s parallel drafting and human review. The invented amounts show a simple calculation, not a real client, a real product outcome, or financial advice. No claim is made that Range uses these exact components or that the arithmetic difference supports a financial recommendation.
Wise’s agenda-only description separates model proposals from authority and describes versioned platform policies. The swimlane is our proposed design: data access, drafting, review, and execution are different responsibilities. Human review needs clear evidence and an enforceable boundary; merely labeling a person “in the loop” does not prove an effective control.

Speaker notes:
Walk horizontally through the lanes. The agent prepares work while the professional retains judgment. An executor should not infer its authority from a fluent draft or a model’s confidence.
Invite the audience to name one missing input or one action that must remain blocked. Keep the example at the review-packet level; it is not advice.

Source keys: S02, S15


# 21 workflows-03
04 / RELIABLE WORKFLOWS & SKILLS Authority must be enforced outside the agent’s proposed action Two Sigma describes ownership, declared access, risk scoring, and active controls; Wise separates reasoning from authority. Together, these ideas make the permission path as explicit as the data path.

Ownership Registry Owner Product Evaluations Scope & risk Identity Tools Endpoints Resources Enforcement Policy boundary Human exceptions Authorized executor Make agents owned systems Two Sigma’s registry records owners, products, tools, and evaluations, with risk scoring informed by access and controls. Use that inventory to locate responsibility and identify required checks. Registration provides visibility; it is not evidence that an agent’s permissions or behavior are constrained. Enforce the requested scope A model can propose a tool call while policy decides whether the user, case, resource, and action are permitted. Test revoked access, cross-user scope, retries, and duplicate requests. A valid credential or technically successful API call does not establish an appropriate business action. Treat triage as fallible The Two Sigma notes mention an independent classifier for deciding when human approval is needed, without performance or enforcement details. Evaluate missed consequential cases and unnecessary interruptions. A classifier’s output can inform review routing; its independence alone does not justify waiving required approval.

Reader explanation:
The Two Sigma notes record an agent registry, risk-factor scoring, access declarations, active controls, common evaluations, and an independent classifier for approval triage. The attendee marked the talk production, but no coverage, calibrated classifier performance, or measured safety/utility result was captured. The classifier’s type and enforcement powers are unspecified; do not call it deterministic or assume it can safely waive approvals.
Wise’s official abstract describes LOOP and versioned policies separating reasoning from authority. It is agenda-only evidence in this presentation. The diagram is a proposed synthesis, not a disclosed complete architecture from either firm. Evaluate denied requests, revocation, retries, cross-user scope, and exceptions before treating a valid tool call as an appropriate business action.

Speaker notes:
Show the authority path as clearly as the data path. A model can suggest a tool call, while a different component decides whether it may execute under the user’s scope and the task’s rules.
Ask which checks are enforced outside the model and what happens when a classifier is wrong. An approval workflow needs measurable false-pass and false-alarm behavior as well as clear ownership.

Source keys: S05, S15


# 22 workflows-04
04 / RELIABLE WORKFLOWS & SKILLS Verification must catch different failures at creation, release, and operation Sonar’s three-loop framing places checks during generation, before release, and after deployment. Intent, guardrails, verification, and evidence form a design checklist—not a calibrated confidence formula.

Creation loop Inspect generated work and catch local issues Intent · guardrails · verification · evidence Release loop Run independent tests and required checks Intent · guardrails · verification · evidence Operation loop Observe failures and verify repairs Intent · guardrails · verification · evidence Prevent local mistakes early The creation loop guides generated work with explicit goals, standards, and constraints, then checks local changes before they accumulate. It can reduce avoidable rework in principle, but needs evaluation. Agreement from another model or a quick human approval is not independent correctness evidence. Verify the system before release Release checks should examine behavior beyond the edited fragment: interfaces, permissions, financial invariants, and regressions. Keep reproducible test evidence and assess whether the checker detects important defects. Neither a passing suite nor a fail-leaning judge establishes that every consequential failure has been covered. Verify repairs during operation Production observations reveal failures the pre-release assessment missed. Turn an incident into a reproducible case, test the repair alongside other workloads, and retain rollback conditions. Prevention remains a priority, while detection and response remain necessary; the framework does not establish autonomous self-healing.

Reader explanation:
The Sonar notes record a conceptual “code confidence” product of intent, guardrails, verification, and evidence, along with warnings about human over-reliance, codebase complexity, compounding errors, and inconsistent model judges. Treat the four factors as a design checklist rather than a calibrated score or probability. No scale, formula validation, or defect-rate prediction was captured.
The three loops are from the official abstract, not explicitly recorded in the notes. They suggest different places to check generated work, pre-release behavior, and production repairs. The recorded 50k-line example has no benchmark setup and is not a universal limit. Neither the notes nor abstract establishes automated prevention of all defects or a proven customer deployment.

Speaker notes:
Connect the loops to the failure they can catch. A local generator check may miss a system invariant; CI may miss a rare runtime interaction; maintenance needs to verify that a repair did not create a new regression.
Keep “prevention first” as a priority, not a claim that later detection and response are unnecessary. Independent verification remains work to design and validate.

Source keys: S16


# 23 workflows-05
04 / RELIABLE WORKFLOWS & SKILLS Financial invariants remain essential when AI accelerates a code change Vanguard’s ledger-modernization account separates producer migration, replicated financial state, and consumer migration. AI-assisted engineering remains subordinate to transaction completeness, consistency, controlled retries, and reviewable reconciliation.

01 Producers Independent source onboarding 02 Gold-copy data Replication and consistency 03 Consumers Decoupled access and dependencies No missing or duplicate transactions Consistent financial state Controlled change and reconciliation Map the financial dependencies Vanguard describes independently progressing producer and consumer migrations around a replicated gold copy, with change data capture (CDC) synchronization and decoupled access. The useful lesson is to identify where financial state originates, changes, and is consumed. This case structure is not a prescription for every modernization. Make invariants directly observable Database-layer idempotency is highlighted in Vanguard’s account. Translate completeness, duplicate prevention, and consistency into observable checks at the relevant boundaries, including retry and recovery paths. Faster code generation cannot demonstrate that no transaction was omitted or that a repeated operation is safe. Isolate the contribution of AI Vanguard says AI tools helped maintain two codebases, without isolating their incremental benefit. Separate the migration controls that preserved financial behavior from any improvement in engineering effort. Compare equivalent changes, review and rework, correctness, and operating cost before attributing the whole project’s outcome to AI.

Reader explanation:
Vanguard’s official abstract describes a production cash-ledger modernization with separate producer migration, gold-copy replication, and consumer migration; CDC synchronization, GraphQL decoupling, and database-layer idempotency are highlighted. AI tooling is described as helping maintain two codebases. This is agenda-only context: no attended-note block for Vanguard was supplied.
The transferable point is that faster engineering does not remove financial consistency responsibilities. The abstract does not isolate AI’s contribution, publish productivity or risk improvements, or describe an autonomous investor/adviser agent. The simplified map is a description of the advertised case, not a recommendation to introduce dual systems or a compatibility layer into another product.

Speaker notes:
Use this case to bring the chapter back to system engineering. An agent can accelerate a code change, but the financial process still needs complete transactions, consistent state, and safe repeat execution.
When reporting a large project’s outcome, separate the architecture that preserved correctness from the incremental benefit attributed to AI. Neither should be assumed from the other.

Source keys: S17


# 24 growth-01
05 / GROWING AS AN AI ENGINEER An AI engineer owns the loop from user need to verified improvement Professional growth comes from connecting task definition, instrumentation, evaluation, diagnosis and release. A working feature becomes a dependable capability through repeated, reviewable decisions about what to change and why.

01 Frame Define the accepted work 02 Build A complete working slice 03 Learn Traces, cases, failures 04 Operate Verify, release, observe Instrument the complete task Arize described using traces to identify issues and improvement opportunities. Capture the request, source context, intermediate actions, result, evaluation and relevant versions together. A useful trace lets an engineer reconstruct why a workflow failed, rather than merely observing that it did. Build a portfolio of decisions Maintain a small portfolio of reproducible failures, baseline comparisons, repairs and release decisions. For each entry, explain the domain problem, system behavior, evidence and tradeoff. This makes growth observable through stronger engineering judgment, rather than through a longer list of tools. Close the release loop Keep issue discovery, proposed fixes, validation and permission to release as separate responsibilities. Preserve the test evidence and decision, then observe the changed workflow for regressions. The conference mechanisms motivate this operating habit; they do not establish autonomous remediation or validated diagnostic accuracy.

Reader explanation:
Arize's recorded distinction is between working on a feature and building the system that repeatedly improves it. Ramp's notes add a task-level definition of success and experiments on skills and memory. Together they suggest an engineer's growth path centered on closing a reliable loop from user need to evidence-backed change.
Evidence: Arize is a vendor account with unclear maturity and no measured diagnostic results in the notes. Ramp's notes omit an explicit evidence/maturity label. Automated diagnosis should remain a hypothesis until a concrete issue is reproduced and a change is tested; named tools or skills from rough notes are not required to apply this operating principle.

Speaker notes:
Connect this chapter to the preceding reliability material: engineering responsibility continues after the first successful demonstration. Read traces to understand failures, then make a change whose effect can be checked.
Keep diagnosis, proposing a fix, validation and release authority separate. This is a useful skill model even when each step is performed manually.

Source keys: S14, S10, S11


# 25 growth-02
05 / GROWING AS AN AI ENGINEER Technical fluency must connect domain meaning, system behavior and measurement Develop the responsibilities together on a real workflow. Domain expertise defines acceptable work; data and software make it reproducible; evaluation and communication determine which claims the evidence can support.

01 Domain translation Turn a professional's judgment into inputs, questions and acceptance criteria 02 Data reasoning Inspect entity, time, units, source and transformations 03 System design Draw ownership, allowed actions, state and exceptions 04 Evaluation Separate critical failures, task success, judge errors and full cost 05 Evidence communication Explain what was claimed, observed, checked and still unknown Translate judgment into inputs Use Range's procedural example to ask a domain expert which facts matter, why a step is necessary and when clarification is required. Connect that reasoning to entities, periods, units and source definitions so an agent can access the right information. Connect controls to tests Draw who requests work, which resources are available, what may execute and how exceptions are handled. Then design cases that challenge those boundaries and the evaluator itself. System design and experimental design should meet at observable behavior, including serious false passes. Communicate a defensible decision Explain the task, mechanism, comparison, result and remaining uncertainty in one evidence card. Distinguish a reported deployment from tested effectiveness and a useful output from attributable business value. This practice helps data scientists, engineers and technical leads review the same decision.

Reader explanation:
The recurring engineering responsibilities span domain understanding, data semantics, software controls, measurement and communication. A data scientist can contribute experimental design and uncertainty analysis; an engineer can make behavior observable and enforceable; a technical lead can align the workflow and decision criteria. These responsibilities overlap and can be learned through shared work.
This is an editorial growth framework derived from the conference mechanisms, not a survey of hiring requirements or a claim that any firm uses this competency model. Choose a development area by inspecting a real gap in a bounded workflow, rather than collecting tools without a task.

Speaker notes:
Invite the audience to identify one responsibility it already performs well and one that would most improve its current work. The goal is balanced fluency and good collaboration, not requiring every person to become the sole expert in every area.
Keep evidence communication in the map. Being able to distinguish a useful mechanism from an unsupported outcome is part of technical judgment.

Source keys: S02, S04, S09, S05, S10, S01, S16


# 26 growth-03
05 / GROWING AS AN AI ENGINEER Software lifespan changes maintenance needs; failure consequences still determine required checks Capital One's durability discussion separates short-lived tools from long-lived dependencies. Use lifespan and consequence as independent design questions, then revisit both when an experiment gains users or responsibilities.

short lifespan · bounded consequence Simple and removable Clear scope, owner and retirement condition long lifespan · bounded consequence Maintainable and owned Stable interfaces and regression checks short lifespan · high consequence Constrained and checked Bounded execution and evidence before use long lifespan · high consequence Operated and verified Explicit controls, recovery and continuing validation Allocate maintenance deliberately Capital One contrasted durable software with tools replaceable in hours and used by relatively few people. That framing can guide documentation, interfaces and maintenance investment. The notes do not demonstrate zero replacement cost or a deployed disposable-software model at the firm. Protect immediate business consequences A short-lived tool can still expose sensitive information, calculate a wrong financial figure or trigger an inappropriate action. Keep the relevant access, numerical and execution checks even when implementation is simple. Cheap regeneration does not reduce the consequence of an incorrect result. Reassess growing dependencies early When other people or workflows begin relying on an experiment, reassess ownership, support, recovery and regression coverage. Set a retirement condition for genuinely temporary tools. Continued use should trigger an explicit maintenance decision rather than quietly converting an experiment into infrastructure.

Reader explanation:
Capital One's recorded discussion distinguishes durable software from software that might be replaced in hours and used by relatively few people. A practical interpretation is to allocate maintainability deliberately. Expected lifespan is only one axis: a short-lived tool can still expose sensitive data or produce a consequential financial error.
Evidence: the Capital One notes are conceptual and do not establish a deployed disposable-software model or near-zero replacement cost. Sonar and Two Sigma supply complementary prevention/control concerns. The matrix is a proposed engineering judgment aid; specific checks depend on the actual workflow and existing requirements.

Speaker notes:
Use the short-lived/high-consequence quadrant to surface the tension. Cheap regeneration changes the economics of maintenance, but it does not make the consequences of a wrong answer disappear.
Ask what happens when a useful experiment gains downstream users. Reassess ownership, dependencies and validation instead of continuing to call it disposable.

Source keys: S18, S16, S05


# 27 growth-04
05 / GROWING AS AN AI ENGINEER One bounded experiment can develop the full engineering discipline Choose a work product a reviewer understands and build the smallest complete path. Learn by comparing behavior, inspecting failures and explaining a decision to continue, revise or retire.

01 / Frame Workflow + source rules + acceptance criteria Choose one meaningful output. 02 / Baseline Reviewed examples + current time/cost/quality Record quality, time, and cost. 03 / Experiment Working path + traces + failure cases + comparison Change one variable; inspect failures. 04 / Explain Evidence card + limits + continue/revise/retire decision Continue, revise, or retire. Frame a measurable task Select a research brief, analytical query result or preparation draft with clear users and acceptance criteria. Use approved or synthetic inputs and record current quality, time and effort. A useful learning exercise starts with the baseline, not the preferred model. Change one variable deliberately Follow Ramp's experimental direction by varying a skill bundle, memory rule or model while holding assessment cases and input snapshots fixed. Include ordinary, ambiguous and consequential-failure cases. Measure accepted quality, review effort, latency and cost together; keep tuning separate from assessment. Finish with an evidence card Document the comparison, observed failures, uncertainty and next decision. A valid outcome may be a simpler deterministic workflow, inadequate data or an experiment worth stopping. Share one reproducible case with a peer and explain what evidence would change your conclusion.

Reader explanation:
A bounded experiment can develop the five responsibilities together. Start from a task a domain reviewer understands, use approved or synthetic material, and establish what accepted completion means. Instrument the complete path before expanding it. Keep assessment examples distinct from tuning, and evaluate severe failures separately from average quality.
This is a proposed learning exercise grounded in Ramp's task/ablation account, Arize's improvement-loop account and Contour's comparison questions. It is not a production approval process, sufficient statistical validation or a commitment for any existing project. Agree criteria before interpreting a result and preserve uncertainty when the sample is small.

Speaker notes:
Make the exercise feel achievable: the deliverable is a defensible comparison and a decision, not an elaborate platform. A useful outcome can be that a deterministic workflow solves the task more simply, or that the data is not ready.
End the growth chapter by emphasizing the habit of making each claim reviewable. That habit transfers across models and tools.

Source keys: S10, S14, S01, S11


# 28 conclusion-01
TAKEAWAYS & DISCUSSION Turn the conference into three decisions and one bounded comparison The useful return is a decision peers can assess: which work matters, which boundaries must hold and which evidence would justify change. Attach those decisions to one testable hypothesis.

Work Which accepted output matters, and to whom? A decision to make explicit, supported by evidence. Boundary Which sources, actions and human judgments are permitted? A decision to make explicit, supported by evidence. Evidence What would justify continuing or stopping? A decision to make explicit, supported by evidence. Choose the accepted work Name the person whose work should improve and the output they can inspect, correct and accept. Use the financial examples to sharpen that choice: a research insight, reviewed planning analysis or evidence-backed artifact. State the bottleneck before choosing tools or architecture. Define evidence and authority Specify the permitted sources, information cutoff, calculations, actions and human judgments. Identify what must remain blocked and what happens when evidence is missing. Bridgewater, Kepler and Two Sigma offer mechanisms to examine; the appropriate boundary depends on the particular workflow. Agree the comparison first Compare the candidate with the existing process on equivalent work, agreed acceptance criteria and critical conditions. Include all attempts and human effort. Decide beforehand which evidence would support continuing, repairing or retiring the approach; conference claims alone do not establish internal readiness.

Reader explanation:
The conference's useful return is a set of decisions peers can assess. Across the recorded examples, the recurring responsibilities are task-specific information, procedural knowledge, constrained action, independent checks, calibrated evaluation and value comparison. Those ideas become useful when attached to a narrow work product and a testable hypothesis.
A useful report-back separates mechanisms we can apply from effects we still need to measure. Keep company attributions and disclosure dates with the evidence, then define the local comparison needed to support a stronger claim about quality, capacity or business impact.

Speaker notes:
Return to the opening work-product question. Ask the audience to propose a workflow, then fill the boundary and evidence columns before debating tools.
Leave ownership and dates as decisions for the team. The presentation proposes a way to decide; it does not announce a Fidelity commitment.

Source keys: S04, S05, S09, S01, S02


# 29 conclusion-02
TAKEAWAYS & DISCUSSION Use disagreement to choose the next test End with a concrete workflow and a consequential uncertainty. Discussion should reveal the failure or comparison that could change the decision, rather than produce agreement around a favored tool.

Value Name one accepted work product and the person whose work improves. Risk Name one unsupported fact, denied action or missed exception that matters. Test Name the comparison and evidence needed to continue, revise or stop. Expose the value assumption Ask which bottleneck limits the professional's work and what observable output would improve if it were removed. Challenge whether faster generation actually saves total effort after review. Record a measurable hypothesis instead of equating adoption, parallel drafting or user enthusiasm with value. Name the surviving failure Choose one unsupported fact, wrong period, denied action or missed exception that could pass ordinary review. Explain its consequence and where prevention, detection or intervention should operate. Use that case to test the complete workflow and the reviewer or judge. Capture the decision-changing evidence Agree what baseline, output checks, cost records or follow-up clarification would change the team's view. Leave ownership and timing for explicit discussion. If the evidence cannot yet support an experiment, record the missing prerequisite rather than forcing an immediate project commitment.

Reader explanation:
Use these prompts to connect the industry examples to the audience's judgment without presuming a specific current project. A useful discussion produces a clear work unit, a consequential failure to test and a credible comparison. Record unresolved questions and who could clarify them, rather than forcing consensus from incomplete conference evidence.
The risk prompt follows the recorded failure-driven evaluation principle; the baseline prompt follows Contour's value-attribution discussion. Both are proposed uses of speaker accounts, not validated assurance methods or an endorsement of a particular tool.

Speaker notes:
Introduce the three prompts in thirty seconds, then use the separately allocated discussion time. Start with silent individual thought or a concrete example so the conversation does not become a general tool debate.
Capture one candidate experiment and one unresolved evidence question. If no candidate meets the conditions, that is a useful outcome; no immediate project commitment is required.

Source keys: S11, S01


# 30 appendix-evidence
APPENDIX / EVIDENCE & METHODS One implementation checklist connects the task, evidence, authority and release decision Use a shared contract before building and at each material change. It gives domain experts, data scientists and engineers a common way to review what the system should accomplish.

Responsibility What to specify What to inspect Task User, work product, acceptance and baseline Can the reviewer recognize completed work? Evidence Entity, period, units, source version, cutoff and access Can each material claim be reproduced? Authority Allowed resources, proposals, approvals and execution Can a denied action bypass the boundary? Evaluation Cases, rubric, critical failures and calibrated judges Which serious failure could still receive a pass? Operation Versions, traces, release owner, stop and rollback Can a failure be diagnosed and a repair verified? Make each requirement testable Replace broad goals such as accuracy or safety with observable behavior. Name the work product, necessary evidence, allowed actions and unacceptable outcomes. A requirement is useful when a reviewer can recognize compliance and a test can expose a meaningful violation. Retain the decision context Record system, data, skill, case and evaluator versions together with the result. Keep important disagreement and accepted limitations. That record lets another person reproduce the comparison and understand why a change was considered appropriate for a particular scope. Revisit changes in exposure A new data source, user population, tool or execution permission can change the failure modes even if the prompt is unchanged. Reassess the relevant cases and operational controls. Expand review when the uncertainty could alter the decision, rather than repeating every check mechanically.

Reader explanation:
The checklist connects five responsibilities that are often assessed separately: task acceptance, evidence quality, action authority, evaluation and operation. Review them as one workflow so a correct-looking artifact cannot conceal a wrong source, unauthorized step or unreproducible release decision.
Use the contract to make disagreements concrete. A domain expert defines acceptable completion; data and engineering owners identify source semantics and enforceable boundaries; reviewers agree which failures block acceptance and what evidence permits a scoped change.
The checklist is an illustrative synthesis of the conference mechanisms. The source catalog preserves company attribution and historical dates; it does not turn a design pattern into independently verified business effectiveness.

Speaker notes:
Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.

Source keys: S01, S02, S03, S04, S05, S06, S07, E01, E02, E03, E04, S08, S09, S10, S11, S12, S13, E05, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, E06


# 31 appendix-atlas
APPENDIX / EVIDENCE & METHODS Company examples teach reusable mechanisms rather than a single financial AI architecture Group cases by the problem they illuminate. Use the mechanism to generate a design or evaluation question; compare reported maturity and business effects separately in the detailed company atlas.

Theme Company examples Transferable mechanism Evidence and research Bridgewater · Kepler · Contour Time-scoped retrieval, typed facts, reproducible comparisons Wealth workflows Range · Morgan Stanley · UBS · RBC Expert-authored preparation, institutional knowledge, reviewed follow-through Authority and controls Two Sigma · Wise Owned agents, resource scope, explicit approval and execution boundaries Engineering platforms Monzo · Optiver · Vanguard Shared runtime, task qualification, financial invariants Improvement and learning Ramp · Arize · Sonar · Capital One Task-level ablations, trace diagnosis, layered verification, deliberate maintenance Compare like work with like A research information feed, planner preparation draft and code-migration assistant have different acceptance decisions. Compare systems performing equivalent work before interpreting adoption, time or cost. Their shared lesson is explicit evidence and control, not one universal success metric. Distinguish mechanism from effectiveness A detailed architecture explains how a system is intended to operate. Production use shows operational adoption. Neither alone establishes quality, net time saved or causal business impact. Ask what baseline, task mix and human effort would support the stronger claim. Use the atlas for follow-up The full reading-mode atlas retains 25 firm perspectives, source links and case limits. Use it to find a relevant peer pattern, then investigate the missing implementation detail or measurement. A company affiliation alone does not establish deployment of every discussed technique.

Reader explanation:
The atlas preserves all 25 firm perspectives from the consolidated industry research, including cases with sparse October 10 abstracts. These are selected, uneven, self-reported examples, not an industry survey or a ranking of frontier maturity.
A company affiliation or protocol-panel appearance is not evidence that the company deployed every named technique or vendor. A detailed mechanism, large user count, or pilot outcome also leaves quality, full operating cost, and causal business impact unresolved.

Speaker notes:
Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.

Source keys: S01, S02, S03, S04, S05, S06, S07, E01, E02, E03, E04, S08, S09, S10, S11, S12, S13, E05, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, E06


# 32 appendix-eval-spec
APPENDIX / EVIDENCE & METHODS A versioned evaluation contract makes a release decision reproducible The illustrative schema links the intended task to inputs, case coverage, acceptance, critical conditions and an accountable owner. It is a compact specification to discuss before running an assessment.

task: draft_review_packet
snapshot: approved_inputs_v1
acceptance: reviewed_complete_output
critical: [unauthorized_access, unsupported_number]
cases: [common, missing, difficult, regression]
judge: model + rubric + threshold + version
compare: baseline_vs_candidate
decision: accountable_owner Make the decision reproducible One contract connects the task, data snapshot, cases, critical conditions, evaluator, and release owner. Define the permitted completion Describe the complete job, authorized data snapshot, output and action limits. Include when the system should clarify or abstain. Critical conditions need explicit definitions: unauthorized access is a failure; correctly refusing access can be the expected successful behavior. Version the evaluator as well A judge model, prompt, rubric or threshold change can change reported quality without changing the agent. Retain those versions with the case and system configuration. Recalibrate important decisions against reviewed examples when the evaluator changes or the task population shifts. Tie evidence to the decision Select cases and uncertainty analysis for the question being decided. Choosing a model, reducing review and granting execution authority require different evidence. The contract supports a scoped judgment with known limits; it cannot prove that no consequential failure remains possible.

Reader explanation:
This is an illustrative schema for discussion, not a runnable framework. The purpose is to make the task, input snapshot, acceptance criteria, critical failures, case coverage, evaluator configuration, and release decision explicit.
The schema should be adapted to the particular decision. Choosing a model, reducing human review, and expanding action authority require different evidence. A finite assessment suite provides bounded evidence, not proof of absence of failure.

Speaker notes:
Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.

Source keys: S10, S11


# 33 appendix-claim
APPENDIX / EVIDENCE & METHODS A typed claim keeps a financial value attached to its meaning and derivation The synthetic AsterCo contract represents a 20% annual revenue-growth claim as a ratio. Its inputs, units, period, information cutoff and calculation are preserved for inspection and downstream rendering.

entity: AsterCo  # invented
metric: annual_revenue_growth
period: FY2025
unit: ratio
value: 0.20
inputs: D1=100; D3=120  # USD_m
as_of: 2026-03-01
calculation: (120 - 100) / 100 Preserve what the number means The entity, period, unit, source version, and transformation travel with the value. Do not mix measurement types Revenue of 120 million dollars and revenue growth of 0.20 are different metrics with different units. Carry the metric definition and unit through every transformation. An exact numerical match against a document is insufficient if the answer uses the value in the wrong comparison. Retain the source identity Store the source document, passage, version and available-as-of time with each input. Reconstruct which evidence was eligible when the question was asked. Publication, reporting period and access permission answer different questions and should not be collapsed into a single timestamp. Propagate corrections through artifacts When an input is superseded, recompute dependent figures and update the associated narrative, table and chart. Preserve the earlier value and change reason for reproducibility. Validate the final artifact, since formatting or export can drop units, periods or links even when the calculation was correct.

Reader explanation:
The contract is an illustrative design requirement informed by Kepler and Bridgewater. It does not claim that either firm implemented exactly these fields or checks.
A verified number can still be used in a wrong comparison. Preserve entity, metric definition, period, units/currency, source version, available-as-of time, and the calculation inputs and operations. The AsterCo values and documents are invented.

Speaker notes:
Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.

Source keys: S09, S04


# 34 appendix-passk
APPENDIX / EVIDENCE & METHODS pass@k measures an opportunity to succeed; deployed reliability also requires choosing correctly Separate candidate generation from selection and acceptance. A multi-attempt benchmark can contain a passing answer while the deployed workflow selects a failing answer or spends excessive effort identifying the usable one.

Benchmark question Was any candidate successful? State k, the task distribution, and the specified test. pass@k Deployment question Can the system select a usable answer? Evaluate selection, first-attempt behavior, retries, and review. End-to-end reliability State the benchmark question Under pass@k, a task succeeds when at least one of k sampled candidates meets the specified test; results are summarized over tasks. State the task distribution, test and attempt budget. This does not report whether the first candidate succeeds or an operational selector finds the passing candidate. Evaluate the actual selector Run the verification, ranking or human-review process the deployed system will use. Measure acceptance of its chosen output, missed defects and rejection of usable candidates. Avoid interpreting an oracle-like benchmark that recognizes success using ground truth as a deployed selection capability. Count the entire attempt budget Include all generated candidates, tool calls, verification, review time and latency. Compare policies at explicit budgets and acceptance standards. More attempts can create an opportunity for higher success while increasing cost and exposure; evaluate that tradeoff on the actual workflow.

Reader explanation:
The primary HumanEval paper defines pass@k as an at-least-one-success benchmark across sampled candidates under a specified test and discusses candidate selection. This presentation borrows the metric distinction, not a code-benchmark performance result for finance.
A deployed workflow must identify and accept a usable answer, comply with critical conditions, and account for the costs of all attempts, verification, and review. Partial-credit task quality, pass@k, first-attempt success, and selected-output reliability should not be used interchangeably.

Speaker notes:
Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.

Source keys: E05


# 35 appendix-measures
APPENDIX / EVIDENCE & METHODS Accepted-task rate and full cost reveal what adoption metrics leave unresolved Agree the eligible population, completion standard and comparison before reporting improvement. Pair output quality with operating effort so a reduction in one cost does not conceal increased work elsewhere.

Measure Definition to agree Interpretation boundary Accepted-task rate Accepted / eligible assigned tasks Do not hide excluded failures Cost per accepted task Full workflow cost / accepted tasks Include review, retries, rework Capacity Accepted outputs / human effort or period Compare quality and task mix Business impact Outcome against credible alternative Account for selection and other drivers Use two complementary denominators Accepted-task rate uses all eligible assigned tasks to show how often the workflow succeeds. Cost per accepted task divides total workflow cost, including failed attempts, by accepted tasks. Report both; a low unit cost can coexist with too many unsuccessful or excluded tasks. Measure professional effort end-to-end Count preparation, correction, evidence checking, approval and follow-up, alongside system costs. Compare equivalent work at the same quality standard. Draft generation time alone cannot establish additional advisor or analyst capacity when people must reconstruct or repair the result. Separate process from business impact Faster accepted work is a process result. Attributable returns, client outcomes or revenue require an additional credible comparison and attention to selection and other drivers. Contour’s recorded comparison motivates the question; the notes do not establish a causal financial estimate.

Reader explanation:
These are proposed measurement definitions. Define the population and exclusions in advance, record full workflow costs, and compare equivalent work at an agreed quality.
Contour’s notes call the approach A/B testing and describe a three-month tracking window, but assignment, sample size, controls, and causal estimates were not captured. Do not treat that window as sufficient validation for every financial workflow.

Speaker notes:
Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.

Source keys: S01


# 36 appendix-unknowns
APPENDIX / EVIDENCE & METHODS Turn unresolved conference claims into specific engineering follow-up questions Uncertainty becomes useful when it identifies the next inspection or test. Focus follow-up on coverage, failure handling, measurement and deployment scope rather than repeating an attractive claim without its conditions.

Unverified effects No comparable ROI or safety result Mechanisms and reported scale are informative; effects remain to test. Unresolved details Source spellings and scope “crunchable”, “roundedness”, the 50k-code example, and retrieval settings. Attribution Keep source boundaries visible Comet/NatWest differs; affiliation alone does not identify a deployment. Ask what the checker misses For citation verification, judge calibration or approval triage, ask which cases are assessed, which serious errors pass, and what happens when support fails. Independent components can share blind spots. Request representative failures and adjudication procedures alongside aggregate agreement or architecture diagrams. Ask what the result measures For reported time savings, productivity or financial effects, request the baseline, task population, exclusions, sample, uncertainty and full human effort. Clarify whether the figure describes adoption, a pilot, estimated opportunity or realized outcome. Preserve historical disclosure dates when comparing firms. Ask what scope was demonstrated Clarify production scope, user entitlements, model and data versions, and operational stop conditions. Sonar’s code-size example and Kepler’s rough retrieval settings lack enough context to become defaults. Unresolved note terms and the Comet/NatWest affiliation discrepancy remain in the source context for follow-up.

Reader explanation:
The source notes preserve unresolved terms such as “crunchable” and “roundedness”; these have not been silently corrected into a provider or safety metric. The Bridgewater reactive/proactive wording reverses once. Workbench examples suggest proactive attention guidance, but the terminology remains to verify.
Sonar’s roughly50k-line codebase example lacks model, workload, metric, and benchmark conditions. Its confidence multiplication is a conceptual framing. Kepler’s retrieval settings are incompletely captured. None is a universal engineering threshold or a calibrated assurance formula.
The failure study’s recorded expected-loss product has undefined events, conditional relationships, and severity units. Incident rankings and exponential growth claims lack denominators and methods in the notes. These are follow-up topics, not established prevalence or expected-loss estimates.

Speaker notes:
Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.

Source keys: S03, S04, S16, S11, S09, S12


# 37 appendix-sources
APPENDIX / EVIDENCE & METHODS Source links preserve the distinction between company stories and proposed engineering methods The complete catalog contains 39 references. Individual source dialogs connect the slide to its session or primary reference; reading mode retains the company atlas, detailed explanations and original source context.

Reference group What it supports How to use it AI Engineer NYC 2026 12 session-note sets plus program research Company mechanisms and questions to investigate; session links identify the speakers Wealth disclosures Morgan Stanley (June 2024), UBS (February 2025), RBC (March 2025) Historical workflow examples; preserve dates and separate adoption from measured effects Primary metric reference Chen et al., Evaluating Large Language Models Trained on Code (2021) Definition of pass@k and the candidate-selection distinction Teaching examples and methods AsterCo, fictional review packet, rubrics and control diagrams Apply the reasoning to your workflow; these are illustrative designs, not firm architectures Use company stories as evidence The deck consolidates twelve identified session-note sets with pre-conference program research. Notes capture the live accounts; agenda descriptions identify advertised topics and mechanisms. The presentation derives practical questions from those sources without treating reported implementation as independently tested effectiveness. Keep external context dated The wealth examples draw on primary company releases and investor materials from 2024 and 2025. They establish what the firm described at that time. Current availability, rollout populations and causal benefits require separate verification; the dates remain visible on the comparison slide. Reuse the illustrative methods deliberately Rubrics, typed-claim contracts, release gates and learning exercises translate the conference mechanisms into reviewable practices. AsterCo and the financial-review packet use invented values. Adapt acceptance and failure definitions with domain reviewers, and test the complete workflow before interpreting a method as an established result.

Reader explanation:
The catalog below includes each source used in the core presentation and the evidence atlas. Official session links identify talks; attendee notes remain the source of the captured live claims. Program-only cases are marked as context.
The method paper and firm disclosures are primary external references. Historical releases are not claims about a firm’s latest state, and company-reported outcomes are not independent validation.

Speaker notes:
Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.

Source keys: S01, S02, S03, S04, S05, S06, S07, E01, E02, E03, E04, S08, S09, S10, S11, S12, S13, E05, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, E06
