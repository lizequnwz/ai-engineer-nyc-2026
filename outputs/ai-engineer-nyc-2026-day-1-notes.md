# AI Engineer NYC 2026 — Day 1 synthesis

**Date:** Tuesday, October 13, 2026  
**For:** Principal Data Scientist, Fidelity Investments  
**Basis:** Seven session-note sets supplied by the attendee, plus an unattributed closing reflection.

## Executive synthesis

Day 1’s strongest message is that useful financial-services AI depends on the surrounding system: information organized for the task, controls that govern action, an evaluation loop that looks for consequential failures, and measurement tied to useful work. This synthesis is based on seven sets of attendee notes, rather than an independently verified assessment of the firms.

Bridgewater described a shared knowledge foundation serving humans and agents with different retrieval needs, together with an investor workbench intended to direct attention toward missing information. Two Sigma described agent registration, risk scoring, declared resource access, active controls, shared evaluation, and selective human approval. Together, these accounts connect usefulness to information access and explicit operating boundaries.

The evaluation sessions broadened the unit of improvement from a feature to a system. Arize’s talk emphasized a build–evaluate–inspect–improve loop, including agent-readable traces. The AI-failures session emphasized seeking disproof and prioritizing risk, while Kepler described a pipeline that separates language-model planning from source retrieval, computation, and citation checks.

Contour framed value measurement around a counterfactual: what would the research process have concluded without AI? Capital One’s durability discussion added a second question: how long must a piece of software live, and who depends on it? Neither a usage metric nor cheaper code generation answers those questions by itself.

The practical takeaway for the team is to connect each AI workflow to an evidence trail: what information it used, what it was allowed to do, how failures were tested, what people accepted or corrected, and what improvement remains against a credible baseline. Day 2 topics and other industry cases remain agenda-based context wherever attendee notes are absent.

## Evidence and reading conventions

All seven named sessions were marked “Speaker claim” in the supplied notes. Vault and Two Sigma were marked production, speaker-reported; the other five were marked unclear. No result is upgraded to independently checked or internally validated evidence.

Session descriptions below distinguish what the notes record from editorial takeaways, proposed tests, and unanswered questions. Blank or prefilled questions in the raw notes are not treated as answered. Official schedule links identify sessions; they do not verify the details captured in attendance.

## Seven cross-session learnings

### 1. Information access and delivery should match the work

The Vault notes distinguish human search, which needs a small high-signal result set, from agent retrieval, which may need broader recall at larger scale. The same notes emphasize drawing on familiar information channels and supplying time, market, country and concept context. This suggests designing both the information foundation and its route into the user's work rather than expecting a repository alone to change habits.

**Practical tips:**

- Define the user decision and relevant time window before choosing a retrieval approach.

- Measure retrieval recall for the agent and precision/usefulness of the final human-facing brief separately.

- Compare a focused brief or feed with on-demand search; count important omissions, irrelevant items and review time.

**Evidence limit:** The notes do not provide benchmark results, evidence that habits changed, or proof of better predictions. The direction of the reactive/proactive transition is inconsistent in the source.

**Sessions:** [D1-01 · Bridgewater](https://ai.engineer/nyc/2026/schedule?session=a84ca3a8-cc2f-4b50-a635-fc380f6f04f6)

### 2. Govern agents as owned systems with enforced access

The Two Sigma notes describe an agent registry, ownership, declared tools/endpoints/resources, risk-factor scoring, active controls and a shared evaluation framework. They also record an independent classifier for determining when human approval is required. The useful principle is to make ownership, access and oversight explicit; the classifier is a mechanism to investigate rather than an established substitute for review.

**Practical tips:**

- Record the owner, purpose, data/resources, tools and evaluation evidence for each workflow.

- Check denied access and tool calls as well as successful ones.

- If triaging approvals automatically, measure missed high-risk cases and unnecessary escalations separately.

**Evidence limit:** Production maturity is speaker-reported. The notes do not document the scoring rubric, enforcement architecture, classifier performance or measured effect on approval fatigue.

**Sessions:** [D1-02 · Two Sigma](https://ai.engineer/nyc/2026/schedule?session=73badd10-6f8c-4c95-b5e7-55fc3d7bafc1)

### 3. Use risk-based system evaluation to seek failures

The failure-analysis notes argue for evaluating the complete path from a failure through its reaching a consequential situation, escaping detection and causing harm. They favor seeking disproof and retesting a repair over accumulating confirming examples. This complements the Two Sigma shared-evaluation idea and the Arize build/evaluate/improve loop.

**Practical tips:**

- Include rare but consequential errors rather than sampling only common requests.

- Separate the chance of an error from the effectiveness of containment, detection and human intervention.

- Turn a found failure into a regression case, then verify the fix against that case and a separate assessment set.

**Evidence limit:** The notes do not establish the incident dataset's representativeness or validate the risk formula numerically. Claims about exponential growth and which categories dominate should remain attributed and provisional.

**Sessions:** [D1-05 · New York Life Insurance / Tanmay Sah](https://ai.engineer/nyc/2026/schedule?session=9d72d7ac-a2a2-42cf-b880-5859316d840c), [D1-02 · Two Sigma](https://ai.engineer/nyc/2026/schedule?session=73badd10-6f8c-4c95-b5e7-55fc3d7bafc1), [D1-04 · Arize AI](https://ai.engineer/nyc/2026/schedule?session=b2ed4456-5671-4e8e-83fd-684c012fef8c)

### 4. Financial numbers need a verifiable evidence path

The Kepler notes distinguish wrong-source, wrong-number and arithmetic errors. They describe a plan/retrieval/code path, typed facts and a citation registry/filter with attempted repair before rejection. The transferable idea is to bind a quantitative claim to its source and transformation, then define what happens when verification fails.

**Practical tips:**

- Retain the source, entity, period, unit/currency and calculation path for each important number.

- Compute arithmetic with an inspectable tool and verify the operands and intended formula.

- When a quantitative claim cannot be supported, expose the unresolved claim or abstain; deleting the citation alone would not validate the sentence.

**Evidence limit:** This is a vendor-described mechanism. The notes do not show error rates, refusal rates, adversarial results or a guarantee that deterministic processing verifies every fact. The exact retrieval settings may be task-specific or incompletely transcribed.

**Sessions:** [D1-07 · Kepler](https://ai.engineer/nyc/2026/schedule?session=2d29f925-f16b-41b3-8086-de0524829cbe)

### 5. Measure useful work against a credible alternative

The Contour notes describe tracking workflows, sources, conclusions and outcomes with and without AI over a three-month period. Cost per useful insight and adoption/utilization are recorded as measures. The central question is what changed relative to the work that would otherwise have been done, and when any benefit becomes observable.

**Practical tips:**

- Define 'useful' through accepted outputs and quality criteria before reporting cost per insight.

- Keep adoption, time saved, work quality and financial outcomes as separate measures.

- Include review and rework in effort/cost comparisons, and preserve the inputs available at the time of a decision.

**Evidence limit:** The notes call the method A/B testing but do not specify randomization, comparison groups, sample size or controls. They do not establish causal ROI or investment alpha; three months is a reported observation window, not a generally sufficient validation period.

**Sessions:** [D1-06 · Contour Asset Management](https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca)

### 6. Match engineering rigor to consequence, dependency and lifespan

The Capital One notes distinguish disposable software used by a few people and replaceable in hours from durable software maintained for years with many dependents. A useful interpretation is to allocate maintainability effort deliberately. In financial workflows, short expected lifespan alone does not make incorrect outputs, sensitive access or consequential actions harmless.

**Practical tips:**

- Ask who depends on the tool, how easily it can be removed, and what an error or outage would affect.

- Separate maintainability needs from the controls required by data sensitivity and consequence.

- Give a short-lived experiment an owner, an explicit expiry/retirement decision and clear limits on use.

**Evidence limit:** This is a conceptual argument in the notes, with maturity marked unclear. It is not evidence that maintenance or replacement costs are actually zero, or that financial-system controls can be skipped.

**Sessions:** [D1-03 · Capital One](https://ai.engineer/nyc/2026/schedule?session=5191589c-a70e-4806-99dc-86f7794f46b9)

### 7. Build an improvement loop around interpretable traces

The Arize notes frame AI engineering as running a build/evaluate/improve loop, with traces informing issue discovery and agents potentially consuming telemetry. They also mention explicit triggers such as messages, schedules, metrics and events. The transferable responsibility is to connect observed behavior to reviewable diagnosis and verified improvement.

**Practical tips:**

- Capture enough structured context to connect the request, retrieved evidence, tools, result and evaluation outcome.

- Define when a review or improvement process is triggered and who owns the proposed change.

- Treat an automated diagnosis as a hypothesis; verify it on concrete traces and rerun relevant tests before accepting a change.

**Evidence limit:** The Arize account is a vendor perspective, and the notes contain no measured results. Product/skill spellings and the exact capabilities of 'Signal' and 'arise-evaluator' need verification before using them as named instructions.

**Sessions:** [D1-04 · Arize AI](https://ai.engineer/nyc/2026/schedule?session=b2ed4456-5671-4e8e-83fd-684c012fef8c), [D1-05 · New York Life Insurance / Tanmay Sah](https://ai.engineer/nyc/2026/schedule?session=9d72d7ac-a2a2-42cf-b880-5859316d840c)

## Coherent session notes

### D1-01 · Vault: Making Unstructured Data Work for Investing

**Speaker/company:** Aaron Linsky and Sam Green · Bridgewater  
**Time:** October 13, 2026 · 9:00–9:18 a.m. EDT  
**Room:** Simons Room (Metropolitan East)  
**Evidence:** Speaker claim  
**Maturity:** Production, speaker-reported in the notes  
**Official session:** [Vault: Making Unstructured Data Work for Investing](https://ai.engineer/nyc/2026/schedule?session=a84ca3a8-cc2f-4b50-a635-fc380f6f04f6)

**Central idea:** A shared information foundation can serve humans and agents while recognizing that their retrieval needs differ. Its usefulness also depends on fitting existing information habits and helping investors decide where to direct attention.

#### What the notes record

- Vault brings external news, research, and transcripts together with internal unstructured information. The notes describe an internal ontology organized around market, country, concept, and time.

- The speaker contrasted human search—precision, high signal-to-noise, and a small result set—with agent search—large-scale consumption and stronger sensitivity to recall. This is a design emphasis, not a claim that agents do not need precision.

- Time scoping was highlighted as an early step in answering an investment question. Filtering, vector search, and benchmarking retrieval precision were also discussed; no benchmark results were captured.

- The notes emphasize bringing existing information channels, including email and subscribed lists, into the knowledge foundation instead of expecting a new tool alone to change working habits.

- An investor workbench was described with activity feeds, question-focused summaries, evidence, and a ‘What am I missing?’ orientation.

#### Takeaway

Treat retrieval as task-specific information access. Preserve a common evidence foundation, but distinguish human browsing from agent collection and synthesis. Proactive feeds should be evaluated on whether they direct attention to useful, timely evidence.

#### Practical tips

- Scope the relevant time period before retrieving or synthesizing investment evidence.

- Measure recall and precision for the consumer and task; do not optimize only for a human-sized answer list.

- Compare the usefulness of an attention feed with current information habits, including noise, missed signals, and actionability.

#### Limits and unresolved details

The notes reverse ‘reactive’ and ‘proactive’ once. The workbench examples suggest a move toward proactive attention guidance; confirm the direction and terminology against slides. No quality, adoption-change, investment-return, or predictive-accuracy result was captured.

#### Questions to pursue

- Which information events trigger a feed, and how are timeliness, novelty, relevance, and evidence quality evaluated?

- How are conflicting sources, time validity, and permissions handled?

- For the RDs mentioned in the notes, what decision should a feed improve? The role abbreviation and the intended workflow need confirmation.

- What evidence would distinguish surfacing timely signals from predicting future outcomes?

### D1-02 · Balancing Acceleration and Safety for AI Agents

**Speaker/company:** John Feminella · Two Sigma  
**Time:** October 13, 2026 · 9:36–9:54 a.m. EDT  
**Room:** Simons Room (Metropolitan East)  
**Evidence:** Speaker claim  
**Maturity:** Production, speaker-reported in the notes  
**Official session:** [Balancing Acceleration and Safety for AI Agents](https://ai.engineer/nyc/2026/schedule?session=73badd10-6f8c-4c95-b5e7-55fc3d7bafc1)

**Central idea:** Agent governance can be expressed through concrete platform services and active boundaries, with human attention directed toward decisions that need it.

#### What the notes record

- An agent registry records owners, associated products, tools, and evaluations.

- Registered agents receive risk-factor scoring informed by access, tools, endpoints, controls, and related characteristics.

- Owners declare the endpoints, tools, and resources an agent needs; active controls enforce the declared access boundaries.

- A shared evaluation framework provides a common operating capability across agents.

- Approval fatigue was discussed. An independent classifier was described as deciding when human approval is needed.

#### Takeaway

Make ownership, access, risk, evaluation, and escalation explicit parts of the operating model. A registry provides visibility; enforcement and tested escalation determine how much protection that visibility delivers.

#### Practical tips

- Record the owner and intended products, tools, endpoints, and resources for each agent.

- Test allowed and denied actions, rather than treating declared access as proof that access is constrained.

- Evaluate an approval classifier for missed consequential cases and unnecessary interruptions before relying on it to reduce review.

#### Limits and unresolved details

No measured safety improvement, task-utility impact, classifier error rate, or approval-volume reduction was captured. Independence of the classifier does not by itself establish reliability.

#### Questions to pursue

- Which controls were preventive, and where were they enforced?

- How are risk scores calibrated, updated, and connected to required controls?

- What can override the approval classifier, and how are false negatives detected?

### D1-03 · Does Code Quality Even Matter?

**Speaker/company:** Max Kanat-Alexander · Capital One  
**Time:** October 13, 2026 · 9:54–10:12 a.m. EDT  
**Room:** Simons Room (Metropolitan East)  
**Evidence:** Speaker claim  
**Maturity:** Unclear in the notes; conceptual engineering discussion  
**Official session:** [Does Code Quality Even Matter?](https://ai.engineer/nyc/2026/schedule?session=5191589c-a70e-4806-99dc-86f7794f46b9)

**Central idea:** Expected durability and the number of dependents should influence the engineering investment a piece of software receives.

#### What the notes record

- The talk contrasted durable software—living for years, relied on by many people, and requiring maintenance—with a proposed category of disposable software.

- Disposable software was characterized as replaceable in hours, relied on by relatively few people, and having less need for long-term maintenance.

- The recorded argument was to scale engineering rigor with the software’s durability and dependency footprint.

#### Takeaway

Distinguish the need for long-term maintainability from immediate correctness and operational risk. Cheap replacement may change a maintenance decision; it does not establish that a wrong result or unsafe action is inexpensive.

#### Practical tips

- Ask who depends on the software, how long it must live, and what replacement actually requires.

- Use a lighter maintenance investment only when the scope and dependency footprint justify it.

- Retain appropriate checks for sensitive data, financial calculations, and consequential actions even in short-lived tools.

#### Limits and unresolved details

Near-zero management or replacement cost is a proposition in the notes, not a demonstrated outcome. The notes do not establish Capital One’s deployment of a disposable-software operating model.

#### Questions to pursue

- What criteria determine when software is truly disposable?

- What happens when a short-lived tool acquires downstream users, data dependencies, or a longer life?

- Which correctness and security requirements remain regardless of intended lifespan?

### D1-04 · What does an AI engineer do?

**Speaker/company:** Aparna Dhinakaran · Arize AI  
**Time:** October 13, 2026 · 10:12–10:30 a.m. EDT  
**Room:** Simons Room (Metropolitan East)  
**Evidence:** Speaker claim  
**Maturity:** Unclear in the notes; practitioner/vendor operating-loop discussion  
**Official session:** [What does an AI engineer do?](https://ai.engineer/nyc/2026/schedule?session=b2ed4456-5671-4e8e-83fd-684c012fef8c)

**Central idea:** AI engineering includes building and operating the improvement loop around a feature: evaluation, trace inspection, issue identification, and iteration.

#### What the notes record

- The notes contrast working on an individual feature with building the system that repeatedly improves it.

- The loop was recorded as build, evaluate, read traces, identify issues or improvement opportunities, and improve.

- Arize’s ‘Signal’ was mentioned as reading agent traces to identify issues. The exact product scope and performance were not captured.

- Telemetry should be usable by agents as well as people. The notes also raise how agents are triggered: messages, schedules, metrics, and events.

- An evaluator skill was recorded as ‘arise-evaluator’; its exact spelling and availability were not verified.

#### Takeaway

Design observability as an input to diagnosis and controlled improvement, rather than only as a store of logs. Discovering an issue, proposing a fix, validating it, and authorizing a release are distinct responsibilities.

#### Practical tips

- Retain task context, intermediate actions, outcomes, evaluator results, and relevant versions in a trace.

- Define which event starts a diagnostic agent and which decisions still require a person.

- Require a reproducible evaluation of a proposed fix before treating automated diagnosis as a release decision.

#### Limits and unresolved details

The notes do not establish autonomous remediation, validated diagnosis accuracy, or any financial firm’s adoption of the named tool or skill. Treat the vendor names as recorded references to verify.

#### Questions to pursue

- Which trace structure makes issue diagnosis reliable and useful?

- How are spurious diagnoses, repeated triggers, and regression-causing fixes handled?

- What is the correct name and public source for the evaluator skill mentioned?

### D1-05 · 1,368 AI Failures: What They Teach Us About System Evals

**Speaker/company:** Vishal Srivastava · New York Life Insurance / Tanmay Sah  
**Time:** October 13, 2026 · 12:20–12:38 p.m. EDT  
**Room:** Turing Room (Riverside Ballroom)  
**Evidence:** Speaker claim  
**Maturity:** Unclear in the notes; failure-study and evaluation framework  
**Official session:** [1,368 AI Failures: What They Teach Us About System Evals](https://ai.engineer/nyc/2026/schedule?session=9d72d7ac-a2a2-42cf-b880-5859316d840c)

**Central idea:** Evaluate how an AI system fails and allows harm to materialize, with priority determined by risk rather than incident frequency alone.

#### What the notes record

- The notes describe failure analysis across development phase and material business impact, including financial, legal, and scale dimensions.

- The speaker’s framework was captured as: E(loss) = P(fail) × P(reach | fail) × P(miss | reach) × severity.

- The notes report that system-design failures were common, while failures of human mediation and harm detection could be less frequent but high impact. Counts, rankings, and definitions were not captured.

- Evaluation was framed as failure-driven: seek disconfirming evidence, find the failure, and then verify the fix rather than confirm a preferred result.

- The notes include a claim of exponential growth in AI failures, without a dataset, time period, denominator, or fitting method.

#### Takeaway

Evaluate the complete failure path: an error can arise, pass through controls, escape detection or intervention, and cause consequential harm. Rare but severe cases deserve deliberate coverage alongside common quality failures.

#### Practical tips

- Construct tests to disprove a claim of reliability, then preserve failures as regression cases.

- Prioritize tests by credible severity and control gaps, alongside frequency.

- Evaluate detection and human intervention as parts of the system, not as assumed rescue mechanisms.

#### Limits and unresolved details

The equation is retained as a recorded heuristic. ‘Reach’ and ‘miss’ were not defined, conditional relationships were not established, and probabilities or severity units were not supplied. Do not use it as a calibrated expected-loss estimate. The 1,368-case study is not an industry incidence rate, and speaker affiliation does not establish New York Life’s adoption of the framework.

#### Questions to pursue

- How were the incidents sampled and labeled, and what is the exposure denominator?

- What do ‘reach’ and ‘miss’ mean, and what conditioning does the full framework require?

- Which tests would have detected the important failures before harm occurred?

### D1-06 · Proving Alpha: Showcasing AI’s Value in Fundamental Investing

**Speaker/company:** Hari Kumar · Contour Asset Management  
**Time:** October 13, 2026 · 1:40–1:58 p.m. EDT  
**Room:** Turing Room (Riverside Ballroom)  
**Evidence:** Speaker claim  
**Maturity:** Unclear in the attendee notes; the earlier program separately reports daily workflow use  
**Official session:** [Proving Alpha: Showcasing AI’s Value in Fundamental Investing](https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca)

**Central idea:** Value measurement needs a counterfactual: would the research process have reached the same conclusion without AI, at the same cost and time?

#### What the notes record

- The notes describe an ‘A/B testing’ pipeline and roughly three months of tracking, documenting workflows with and without AI, sources, conclusions, and subsequent outcomes.

- Idea tracking was described as assessing ideas against the market and considering timing and other dimensions, rather than only generating ideas. The exact division between manual tracking and agent automation is unclear.

- Cost per useful insight and adoption/utilization were recorded as measures. The notes emphasize that observing ROI takes time.

- Examples of value dimensions included execution timing and order history in trading; repetitive work and process reliability in operations; and querying and reconciliation in finance/analytics.

#### Takeaway

Build measurement into the workflow before benefits are claimed. Record inputs, AI involvement, decisions, timing, human effort, and subsequent outcomes. Distinguish activity, accepted insights, process change, and financial return.

#### Practical tips

- Define a useful insight and record who accepted it, how much review it required, and whether it changed a decision.

- Use a credible comparison and document assignment, selection effects, and contamination between AI and non-AI workflows.

- Include review, rework, tool, and inference costs when estimating cost per useful insight.

#### Limits and unresolved details

The phrase ‘A/B testing’ does not establish random assignment, comparable groups, sample size, or controlled causal attribution. No return estimate, verified alpha, or generalizable three-month ROI horizon was captured.

#### Questions to pursue

- What was randomized or matched, and how were AI-influenced and non-AI workflows kept comparable?

- How was ‘useful insight’ defined before observing the outcome?

- How did the analysis handle market movement, selection effects, delayed outcomes, and full operating costs?

### D1-07 · Do Not Let Models Invent Numbers

**Speaker/company:** Vinoo Ganesh · Kepler  
**Time:** October 13, 2026 · 2:30–2:48 p.m. EDT  
**Room:** Shannon Room (NY Ballroom E)  
**Evidence:** Speaker claim  
**Maturity:** Unclear in the attendee notes; vendor-described implementation  
**Official session:** [Do Not Let Models Invent Numbers](https://ai.engineer/nyc/2026/schedule?session=2d29f925-f16b-41b3-8086-de0524829cbe)

**Central idea:** Separate language-model planning and narration from source retrieval, computation, and checking whether a citation supports the financial claim.

#### What the notes record

- Three numerical failure modes were recorded: citing the wrong source, extracting the wrong number from the right source, and performing arithmetic incorrectly.

- The described components include SEC-corpus preprocessing, language-model planning, tool-based source retrieval, code-based arithmetic, a citation registry holding metadata and typed facts, and postprocessing citation checks or filters. The notes do not fully establish their order or boundaries.

- Unverifiable citations were described as refused. Repair attempts were recorded before removing citations: exact matching, equivalent value formatting, and paraphrased quotations.

- Retrieval settings are preserved as recorded: “3× overfetch”; “100 per namespace” (item type/stage unclear); “max 5 per doc” in the reranking discussion; and “top 20 docs for earning” (workload wording unclear). These are incomplete implementation notes, not validated general recommendations.

- The phrase ‘deterministic model handles every fact’ was recorded; the exact scope of deterministic verification needs clarification.

#### Takeaway

A financial answer needs claim-level evidence and a reproducible calculation path. Verification should bind the entity, period, units, currency, source version, and transformation, and should specify what happens to an unsupported claim.

#### Practical tips

- Retain typed facts and the calculation inputs and operations, rather than allowing free-form arithmetic to carry the result.

- Test wrong-entity, wrong-period, unit, sign, currency, restatement, and conflicting-source cases.

- Confirm whether failed verification removes the unsupported statement, triggers abstention, or only strips its citation; those behaviors have different consequences.

#### Limits and unresolved details

No error rate, test set, latency/cost tradeoff, or proof of universal factual correctness was captured. A cited source can still be misinterpreted. The recorded retrieval settings require workload-specific evaluation, and paraphrase repair must not change what the source supports.

#### Questions to pursue

- Which facts and transformations are actually checked deterministically?

- What is the precise order of the retrieval and reranking settings recorded in the notes?

- What happens to a financial claim when citation repair and verification fail?

## Unattributed closing reflection: Business problem selection and shared capabilities

**Attribution:** Unattributed closing reflection in the supplied notes; may combine a speaker’s remarks and the attendee’s own synthesis

- As model intelligence becomes easier to access, judgment about what matters and what to build becomes more important.

- Start with a valuable business problem, such as material signals arriving too late, rather than beginning with where to add an AI tool.

- Consider whether work should become more proactive, rather than simply automating its current reactive form.

- Concentrate shared investment in reusable capabilities; standardize common foundations while allowing workflow-specific adaptation.

**Evidence limit:** The notes mention studies suggesting that leading companies concentrate investment in fewer, higher-value use cases, but supply no citation or methodology. Treat concentration as a strategy hypothesis, not a verified research finding.

## Tensions worth retaining in the team report

- **Recall versus attention:** broader agent retrieval may help coverage, while human-facing feeds still need precision, timeliness, and limited noise.

- **Automation versus oversight:** an approval classifier may reduce interruption burden and can also miss consequential cases. Evaluate both sides.

- **Disposable software versus durable consequence:** a short-lived tool can still expose data or produce a consequential wrong answer. Maintenance needs and immediate risk require separate judgments.

- **Citation support versus correctness:** deterministic arithmetic and a valid citation do not by themselves establish that the entity, period, definition, or interpretation is correct.

- **Adoption versus value:** usage, useful outputs, process efficiency, and attributable financial impact require different measures.

## Optional application hypotheses from your notes

These respond to the questions you raised about Socrates and sales meeting preparation. They are proposals for discussion, not commitments or claims about your current systems.

### Socrates text2SQL

**Hypothesis:** Correctly executing SQL and correctly answering a business question are different outcomes. A traceable query/result path and risk-weighted review could help evaluate the whole task.

**Smallest useful comparison:** Compare a small representative set of questions with authoritative expected results against the current query workflow on the same data snapshot. Include ambiguous definitions, wrong periods, duplicate joins, wrong grain, missing data, and access-denied cases. Keep assessment cases separate from tuning.

**Measures:** Business-meaning and result correctness; important numerical errors; appropriate clarification or abstention; accepted completion; review/rework time; cost per accepted task.

**Limit:** This is a proposed test, not a description of Socrates’ current architecture or a finding that it lacks any capability.

### Sales meeting-preparation agent

**Hypothesis:** A focused, evidence-grounded brief delivered at the right time may help preparation, while proactive delivery can also increase noise.

**Smallest useful comparison:** Compare current preparation with an agent brief on the same approved historical or synthetic cases and an explicit information cutoff. Review factual support, relevant omissions, and usefulness. Test delivery timing separately from content quality.

**Measures:** Accepted brief quality; wrong-client or unsupported claims; important missed developments; freshness; relevance/noise; preparation plus review time; cost per accepted brief.

**Limit:** Preparation benefits do not establish better forecasts or incremental sales. The current implementation, intended user group, and performance are not assumed.

## Priority follow-ups

- Bridgewater: confirm the reactive/proactive wording; obtain retrieval task definitions, benchmark results, and evidence on feed usefulness.

- Two Sigma: clarify the risk-scoring rubric, enforcement points, and approval-classifier false negatives and interruption burden.

- Failure study: obtain incident selection/labeling methods, denominators, and the exact definitions and conditioning of the loss heuristic.

- Contour: clarify assignment or matching, the definition of useful insight, the three-month observation window, and full cost accounting.

- Kepler: clarify deterministic verification scope, citation-repair failure behavior, and the exact meaning/order of the retrieval settings.

- Arize: verify the product and evaluator-skill names and ask how diagnostic accuracy and proposed fixes are evaluated.

- Closing reflection: identify the source and the unnamed study before presenting either as an attributed empirical finding.

## Suggested team readout

1. Lead with three findings: task-specific information access, risk-based operating controls/evaluation, and counterfactual value measurement.

2. Explain the Bridgewater, Two Sigma, and Contour mechanisms, then use Kepler to make numerical trust concrete.

3. Discuss the durability and oversight tradeoffs rather than presenting every technique as universally beneficial.

4. Close with proposed evaluation questions and the evidence still missing. Day 2 can strengthen, qualify, or revise the argument.

## Source and editorial notes

Primary source: the attendee’s pasted Day 1 notes, supplied October 13, 2026. The wording has been corrected for spelling and organized for coherence. Ambiguous details remain explicit. No slides, recordings, datasets, product documentation, or independent results were inspected for this synthesis. Session metadata matches the previously saved official program; the schedule has not been newly verified.

The raw notes remain the underlying record. In particular, the reactive/proactive reversal, the undefined expected-loss terms, the unspecified A/B design, the recorded retrieval settings, and the unverified product/skill names have not been silently resolved.
## Recording follow-up · October 25, 2026

The original attendee observations above are preserved. The following later-source findings clarify them or add related sessions; this is not a claim of additional attendance. The [complete recording supplement](ai-engineer-nyc-2026-recording-supplement.md) contains the wider thematic synthesis and source limits.

### Bridgewater

Vault joins time- and source-aware retrieval with an investor workbench and feedback into the research corpus. The transcript adds a roughly 200-question labeled relevance set and a reported precision@10 improvement from about 60% to 90–95%.

**Practical implication:** Test eligible-source coverage separately from human-facing relevance; include plausible negatives and restrictive filters. Preserve information cutoff and access scope before synthesis.

**Source and scope:** Organizer transcript. Internal retrieval results, without a disclosed held-out design or investment-performance estimate. The speaker corrects 'recall' to precision; the intended product direction is reactive resource to proactive participant.

[Read / watch source](https://ai.engineer/nyc/2026/talks/bridgewater) · [Recording at the session start](https://www.youtube.com/watch?v=akEqiXFo3GM&t=442s)

### Two Sigma

An agent registry makes ownership, purpose, tools, resources and risk visible. Scoped access and a separate approval path constrain execution; approval triage is a different responsibility from enforcement.

**Practical implication:** Test a requested action at the enforcing boundary, including revocation, cross-user access and duplicate requests. Record which component can actually deny it.

**Source and scope:** Organizer transcript. A described control framework is not a measured protection rate or proof that a triage classifier can waive required approval.

[Read / watch source](https://ai.engineer/nyc/2026/talks/two-sigma) · [Recording at the session start](https://www.youtube.com/watch?v=akEqiXFo3GM&t=1435s)

### Kepler · attended breakout release

The standalone release describes a citation registry, deterministic calculation, hybrid retrieval, tenant isolation and typed facts with value, unit, scale and period. Chapters separate retrieval, verification and the limits of guarantees.

**Practical implication:** Use the source's exact fact structure to organize review, then test semantic selection and final output independently.

**Source and scope:** Official video description and chapters. Description/chapter evidence only for this edition. Its 20:58 duration and contents differ from the October 14 main-stage follow-up; exact retrieval settings are not adopted as defaults.

[Read / watch source](https://www.youtube.com/watch?v=dZgA6btnb_s)

### Contour Asset Management

The release describes live research comparisons, cost per useful insight, timing agents that revisit older ideas and the hidden cost of fixing tools. Chapter markers locate those topics for review.

**Practical implication:** Predefine useful insight and track decision timing, human effort and repairs, rather than relying on an attractive ROI title.

**Source and scope:** Official video description and chapters. No usable caption text was recovered. Randomization, controls, sample size and causal alpha remain unverified; description supplements the original attendee notes.

[Read / watch source](https://www.youtube.com/watch?v=ZMZlAn6Pyfg)

### Failure study · New York Life affiliation

The description organizes selected public incidents around technical strength, deployment controls and business impact, and motivates failure-driven tests plus evaluation of the evaluators themselves.

**Practical implication:** Use incident mechanisms to build adversarial and regression cases. Separate materiality from frequency, and inspect false passes in the grader.

**Source and scope:** Official video description and chapters. Coverage of a selected incident database is not population incidence or proof of causation. The original expected-loss equation and insurer-wide deployment remain unverified.

[Read / watch source](https://www.youtube.com/watch?v=mMw3arwQsL0)

### Arize · Aparna Dhinakaran

A disposable sandbox receives temporary repository/credential access; issue history, useful skills and run telemetry persist outside it. Replacement runs can resume from durable progress. Human-labeled data calibrates evaluators before use.

**Practical implication:** Separate the lifetime of task state from the lifetime of execution authority. Trace the agents modifying the system as well as those serving users.

**Source and scope:** Organizer transcript. Proposed fixes/PRs and regression evaluation do not establish safe autonomous production release or measured diagnostic accuracy.

[Read / watch source](https://ai.engineer/nyc/2026/talks/arize) · [Recording at the session start](https://www.youtube.com/watch?v=akEqiXFo3GM&t=3643s)

### Clarifications that remain open

The Comet/NatWest affiliation discrepancy and the banking notes' “roundedness” label remain unresolved. OpenAI's uncertain provider spelling is not guessed. The failure-study expression is not adopted as a calibrated expected-loss formula. Ryan Stevens's written account is separate from Alexander Shevchenko's recorded keynote. Range's online recording is labeled October 13; its attended notes remain in Day 2.
