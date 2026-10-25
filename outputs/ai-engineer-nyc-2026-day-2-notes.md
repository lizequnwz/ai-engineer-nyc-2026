# AI Engineer NYC 2026 — Day 2 synthesis

**Date:** Wednesday, October 14, 2026  
**For:** Principal Data Scientist, Fidelity Investments  
**Scope:** New Day 2 material only; the attachment’s repeated Day 1 notes are not counted again.

## Executive synthesis

Day 2 made the operating ideas from Day 1 more concrete: prevent errors before they propagate, evaluate complete jobs, package domain judgment into reusable skills, and assess quality across several dimensions. These are interpretations of the supplied notes, not independently reproduced results.

Sonar emphasized explicit intent, guardrails, independent verification, and repeatable evidence. Ramp connected evaluation to the tasks that make a job successful, using skill ablations and procedural memory as examples of system changes to test. The banking evaluation session added that safety, task completion, and user experience should remain separate dimensions, and that automated judges need their own validation.

Range supplied the clearest wealth-workflow example in the Day 2 notes: financial planners encode their methods into skills, let an agent draft analyses while they serve another client, then review and adjust the output. The five-step method—Pick, Teach, Pack, Test, Ship—turns practitioner knowledge into an explicit, testable workflow.

The OpenAI presentation connected financial data access to inspectable sources, tables, charts, firm-specific formats, and reusable artifact-generation tools. The practical connection across the day is to treat the whole deliverable—from authorized inputs through reviewed output—as the unit of design and evaluation.

## Evidence and attribution

Five Day 2 session-note sets are identified. Sonar, OpenAI, and the banking session explicitly record Speaker claim and unclear maturity. Ramp and Range have no explicit evidence/maturity fields in the raw notes; they remain unverified attendee-reported speaker accounts. Range was identified through your company clarification and the current official program. No implementation or result is upgraded to independently checked evidence.

Session links identify the talks. The October14 official schedule was checked for the five Day2 records; it confirms Range and the updated Ramp title. The banking speaker affiliation differs: the notes and October10 snapshot say Comet, while the October14 program says NatWest. The discrepancy remains unresolved and is not used to assign the Cora example to a bank.

## Coherent session notes

### D2-01 · The Machine that Changed the World, vAI

**Speaker/company:** Tariq Shaukat · Sonar  
**Time:** October 14, 2026 · 9:18–9:36 a.m. EDT  
**Room:** Simons Room (Metropolitan East)  
**Evidence:** Speaker claim, explicitly recorded  
**Maturity:** Unclear in the attendee notes  
**Official session:** [The Machine that Changed the World, vAI](https://ai.engineer/nyc/2026/schedule?session=4add802c-6a68-4e9c-93fb-9c1e017193bc)

**Central idea:** Prevent defects through explicit intent and deterministic controls, then support release decisions with independent verification and repeatable evidence.

#### What the notes record

- The recorded conceptual formula was: Code confidence = Intent × guardrails × verification × evidence. Intent includes specified goals and standards; verification is independent and thorough; evidence is auditable and repeatable.

- The talk was recorded as arguing that human review alone does not scale, with ‘cognitive surrender’ describing the risk that people too readily agree with AI.

- The notes report a codebase example in which accuracy collapsed above roughly 50k lines and much of the token budget went into understanding the codebase. Model, task, dataset, metric, and test conditions were not captured.

- Compounding errors in long-running tasks and inconsistent answers from LLM judges were recorded as limitations. The conclusion in the notes was that prevention should come first.

#### Takeaway · editorial synthesis

Use prevention, verification, and human judgment as distinct layers. A reviewer needs usable evidence and a defined responsibility; a human approval step alone does not demonstrate that the underlying failure was detected.

#### Practical tips · proposed practices

- Specify the intended outcome, standards, allowed actions, and required evidence before execution.

- Test preventive constraints and independent checks on consequential failures, rather than relying only on the final review.

- Treat judge disagreement as a signal to inspect, not a reason to select whichever judgment is favorable.

#### Evidence limits

The multiplication is a conceptual mnemonic, not a calibrated confidence metric. The 50k-line example is not a universal size limit or a quantified result that transfers across codebases. No measured prevention benefit or judge variance was captured.

#### Questions to pursue

- What failure classes does each preventive or verification layer catch?

- What were the model, workload, accuracy definition, and context conditions behind the codebase example?

- How were independent verification and judge consistency measured?

### D2-02 · Building the Next Chapter of AI in Finance

**Speaker/company:** Joseph Kim · OpenAI  
**Time:** October 14, 2026 · 9:54–10:12 a.m. EDT  
**Room:** Simons Room (Metropolitan East)  
**Evidence:** Speaker claim, explicitly recorded; product/provider perspective  
**Maturity:** Unclear in the attendee notes; availability and deployment scope not established  
**Official session:** [Building the Next Chapter of AI in Finance](https://ai.engineer/nyc/2026/schedule?session=02f94835-c29d-4cf5-b77a-c5a491b747b8)

**Central idea:** A financial AI product combines data access, source inspection, financial interfaces, and useful work products in firm-specific formats.

#### What the notes record

- The notes describe financial data and premium data, with interfaces for inspecting source passages and tables, interactive charts, and firm-specific formats.

- Names recorded in the data discussion include LSEG, Fiscal.ai, FMP, and Quartr, with SEC filings also mentioned. The term ‘crunchable’ is preserved as an unresolved provider or term; it has not been silently corrected.

- Artifact generation included presentation and document outputs, skills, shared artifact tools, and interactive charts.

- Source citations and ‘MCP Apps’ appear together in the notes. Their exact implementation relationship was not captured.

#### Takeaway · editorial synthesis

Evaluate the path from authorized data to inspectable evidence to a usable artifact. The ability to generate a polished report or chart does not establish that its financial claims are current, correctly interpreted, or suitable for the user’s decision.

#### Practical tips · proposed practices

- Assess source identity, dates, tables, transformations, and final artifact accuracy together.

- Check how firm conventions and formatting are represented and reviewed.

- Verify data coverage, entitlements, product availability, and missing-source behavior before treating a presentation as an implementation specification.

#### Evidence limits

The notes do not establish general availability, licensing, supported integrations, complete data coverage, or customer outcomes. Data-provider names and UI descriptions are recorded speaker references, not verified product specifications.

#### Questions to pursue

- Which capabilities were available, demonstrated, or described as future direction?

- How are source passages, quantitative claims, and generated artifacts kept consistent?

- What does ‘crunchable’ refer to, and what role do MCP Apps play in the citation workflow?

### D2-03 · Building Better Agents Through End-to-End Evals

**Speaker/company:** Ryan Stevens · Ramp  
**Time:** October 14, 2026 · 11:05–11:23 a.m. EDT · from the official program  
**Room:** Shannon Room (NY Ballroom E) · from the official program  
**Evidence:** Attendee-reported speaker account; evidence level not explicitly recorded  
**Maturity:** Not captured in the Day2 notes; the program separately describes a production accounting agent  
**Official session:** [Building Better Agents Through End-to-End Evals](https://ai.engineer/nyc/2026/schedule?session=4607dbbe-8f94-4b0e-91ce-257d1cfb5448)

**Central idea:** Define the tasks that complete a job and what success looks like, then evaluate model, skills, memory, and runtime changes on that complete workload.

#### What the notes record

- The notes start with mapping a job into tasks and defining success, including accuracy with partial credit.

- The metric pass@k was recorded as an agent-evaluation measure, without a value for k, scoring rules, sample size, or results.

- Experiments described as working included skill ablation from eight skills to a four-skill bundle, trajectory-distilled memory, and shrinking an Excel skill. The effect sizes and assessment design were not captured.

- The recorded title matches the October14 official program. The same session ID had a different title in the October10 snapshot, ‘We gave our finance agent more context. It got worse.’ Speaker, time, and room here come from program metadata.

#### Takeaway · editorial synthesis

Treat context, skills, and memory as experimental variables. A smaller skill bundle can be a hypothesis worth testing; the result depends on the workload and does not imply that fewer skills always work better.

#### Practical tips · proposed practices

- Define both graded task progress and a clear accepted-completion condition before tuning.

- Compare skill bundles on the same assessment tasks, including critical failures, review effort, latency, and cost.

- For pass@k, state the attempt budget and how a successful attempt is identified; report single-attempt behavior and selection/review cost separately.

#### Evidence limits

pass@k concerns success within a budget of attempts under a specified success test; it does not establish one-attempt production reliability or that the deployed system can identify the successful attempt. The eight-to-four reduction is a reported experiment, not a recommended default. The notes do not equate the Excel-skill change with the program’s separate character-count example.

#### Questions to pursue

- What was the full task distribution and how were partial credit and critical errors handled?

- What were k, repeated-run variance, assessment separation, and selection costs?

- What information is retained or excluded from trajectory-distilled memory, and how is stale case data prevented from transferring?

### D2-04 · We Let Our Financial Planners Write the Agents

**Speaker/company:** Matt Ragone · Range  
**Time:** October 14, 2026 · 11:30–11:48 a.m. EDT · from the official program  
**Room:** Turing Room (Riverside Ballroom) · from the official program  
**Evidence:** Attendee-reported speaker account; company clarified by the attendee; session matched to the current official program  
**Maturity:** Not captured explicitly in the attendee notes; workflow use described  
**Official session:** [We Let Our Financial Planners Write the Agents](https://ai.engineer/nyc/2026/schedule?session=9b002687-09cf-42e2-9282-532ed9d0c184)

**Central idea:** Financial planners can encode their own repeatable planning methods into skills, use agents to draft parallel work, and retain review and adjustment of recommendations.

#### What the notes record

- The notes describe a planner serving one client while an agent drafts cash-flow or insurance analysis for another. The planner then reviews, edits, and adjusts the analysis.

- The recorded bottleneck was the planner’s limited ability to be in several places at once, rather than typing speed.

- A skill needs to know what client data exists and how to obtain it, as well as how the firm performs and delivers planning recommendations.

- The five recorded steps are Pick a repeated workflow that can be judged; Teach by explaining why; Pack the required questions and limits; Test; and Ship.

- The attendee clarified that the company is Range. The current official agenda identifies Matt Ragone and the matching session; the notes originally had no speaker, company, time, or link.

#### Takeaway · editorial synthesis

Codify the firm’s actual judgment process, required inputs, questions, and boundaries in a skill. Evaluate whether parallel drafting increases accepted planning capacity after review and correction effort, while keeping responsibility for the recommendation explicit.

#### Practical tips · proposed practices

- Select a repeatable workflow whose outputs a practitioner can judge.

- Capture the reasons behind choices, required client facts, clarification questions, and limits.

- Test representative and difficult cases before shipping, and keep ownership and review of the skill explicit. Ownership/review practices here are proposed implications, not separately measured results in the notes.

#### Evidence limits

No measured capacity increase, recommendation-quality result, or ROI was captured. Parallel drafting is not autonomous financial advice. The five steps are a process to investigate, not evidence that a skill is correct merely because it follows that process.

#### Questions to pursue

- How are nuanced planning judgments, exceptions, and missing client facts represented and reviewed?

- Who maintains a skill as practice and data change?

- What measures show increased accepted capacity without worse advice quality or greater review burden?

### D2-05 · From Agent Prototype to Production in Regulated Banking

**Speaker/company:** Jonathan Osborne · affiliation discrepancy: Comet in notes; NatWest in the October14 official agenda  
**Time:** October 14, 2026 · 2:05–2:23 p.m. EDT  
**Room:** McCarthy Room (Riverside Suite)  
**Evidence:** Speaker claim, explicitly recorded; affiliation to confirm  
**Maturity:** Unclear in the attendee notes; reported assistant scale does not establish evaluated rollout scope  
**Official session:** [From Agent Prototype to Production in Regulated Banking](https://ai.engineer/nyc/2026/schedule?session=e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa)

**Central idea:** Assess quality as separate safety, task, and experience dimensions, and treat the automated judge as a configured component that must itself be validated.

#### What the notes record

- Quality was recorded as a vector. Listed task dimensions include completion, topic hit rate, and conversation completeness; experience dimensions include user satisfaction and knowledge retention.

- The safety notes contain ‘roundedness, bias’. ‘Roundedness’ is ambiguous and has not been silently changed to ‘groundedness’ or used as a defined metric.

- The speaker was recorded as favoring a judge that tends toward fail rather than pass and making the judge model part of configuration.

- The notes describe ‘Cora’ at 100K conversations a day and a routing funnel involving contextual filters, preclassification, relevancy/rephrasing, and intent classification. The definition, observation period, exact ordering, and results were not captured.

- The notes and October10 program list Comet; the October14 official program lists NatWest for Jonathan Osborne. This discrepancy is preserved instead of silently assigning the speaker or the Cora deployment to an institution.

#### Takeaway · editorial synthesis

Keep a quality scorecard whose dimensions cannot hide one another. Version the judge’s model and rubric, then assess missed important failures, false rejections, stability, and review burden before using scores to change rollout or human review.

#### Practical tips · proposed practices

- Separate critical safety conditions from graded task and experience measures.

- Calibrate a stricter judge against independent human decisions; measure unnecessary failures as well as missed defects.

- Record the judge model, rubric, thresholds, and relevant system versions for comparable evaluations.

#### Evidence limits

The 100K/day figure is a recorded scale claim, not a verified quality, safety, ROI, or current-volume measure. A fail-leaning judge is not automatically better. No approval evidence package, rollback trigger, reviewer agreement, or error-rate result was captured; the prefilled question remains unanswered.

#### Questions to pursue

- Which safety metric was intended by ‘roundedness’, and how are all dimensions scored?

- What are judge false-pass/false-fail rates, human disagreement, and repeated-run variance?

- How does quality evidence govern release, rollback, and renewed review, and which speaker affiliation is correct?

## How Day 2 develops the Day 1 learnings

### 1. Specify the job, workflow and acceptable completion before building skills

Day 1's business-value questions and Day 2's end-to-end-evals notes both start with what work must succeed. The Range financial-planning vignette adds a procedural dimension: a skill needs to know which client information is available, how to obtain it and how recommendations are prepared. Its Pick–Teach–Pack–Test–Ship sequence includes why the work is done, questions the agent must ask and limits it must respect.

**Practical implications:**

- Choose a repeatable workflow whose output a domain expert can judge.

- Record required inputs, why each step matters, mandatory questions, limits, handoff and acceptance criteria.

- Judge the completed work product and correction effort, not only whether an agent produced an answer.

**Limit:** Range attribution is confirmed, but the notes supply no measured result. The five steps are a recorded workflow idea, not a verified industry standard or evidence of suitability for autonomous advice.

**Sessions:** [Vault: Making Unstructured Data Work for Investing](https://ai.engineer/nyc/2026/schedule?session=a84ca3a8-cc2f-4b50-a635-fc380f6f04f6), [Proving Alpha: Showcasing AI’s Value in Fundamental Investing](https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca), [Building Better Agents Through End-to-End Evals](https://ai.engineer/nyc/2026/schedule?session=4607dbbe-8f94-4b0e-91ce-257d1cfb5448), [We Let Our Financial Planners Write the Agents](https://ai.engineer/nyc/2026/schedule?session=9b002687-09cf-42e2-9282-532ed9d0c184)

### 2. Evaluate the model, context, skills and memory as one task system

Bridgewater distinguishes information needs by consumer and task. The Day 2 eval notes then describe experiments with skill ablation, reducing an eight-skill bundle to four, trajectory-distilled memory and a smaller spreadsheet skill. Together, they suggest that more context or more skills should earn their place through a controlled end-to-end comparison.

**Practical implications:**

- Hold the representative task set and grading rubric constant while varying one component where feasible.

- Measure task acceptance, consequential errors, latency, cost and reviewer effort together.

- Distinguish partial-credit task quality from binary success and repeated-attempt measures such as pass@k.

**Limit:** The notes say the experiments worked but give no effect sizes, task set, model versions, costs or statistical uncertainty. Eight-to-four is a reported configuration change, not a recommended bundle size.

**Sessions:** [Vault: Making Unstructured Data Work for Investing](https://ai.engineer/nyc/2026/schedule?session=a84ca3a8-cc2f-4b50-a635-fc380f6f04f6), [What does an AI engineer do?](https://ai.engineer/nyc/2026/schedule?session=b2ed4456-5671-4e8e-83fd-684c012fef8c), [Building Better Agents Through End-to-End Evals](https://ai.engineer/nyc/2026/schedule?session=4607dbbe-8f94-4b0e-91ce-257d1cfb5448)

### 3. Use prevention and independent verification together

Day 1's registered access boundaries and numerical-evidence checks align with Sonar's confidence framing: explicit intent, guardrails, independent verification and repeatable evidence. Prevention reduces defined invalid behavior; verification checks what actually happened. Neither eliminates the need for accountable judgment on unresolved cases.

**Practical implications:**

- State the allowed resources, actions, output requirements and escalation conditions before execution.

- Choose checks that fail differently from the generator; verify inputs and transformations as well as presentation.

- Retain enough versioned evidence to repeat a check and understand an exception.

**Limit:** Sonar's multiplication is a conceptual framework, not a calibrated confidence probability. The notes do not establish how independent any particular verification implementation was or what failure coverage it achieved.

**Sessions:** [Balancing Acceleration and Safety for AI Agents](https://ai.engineer/nyc/2026/schedule?session=73badd10-6f8c-4c95-b5e7-55fc3d7bafc1), [Do Not Let Models Invent Numbers](https://ai.engineer/nyc/2026/schedule?session=2d29f925-f16b-41b3-8086-de0524829cbe), [The Machine that Changed the World, vAI](https://ai.engineer/nyc/2026/schedule?session=4add802c-6a68-4e9c-93fb-9c1e017193bc)

### 4. Keep safety, task success and user experience visible as separate dimensions

The Day 1 failure study argues that frequency alone misses consequential harm. The banking-session Day 2 notes call quality a vector and distinguish safety, task and experience measures. This provides a way to expose tradeoffs rather than allowing a high overall score to hide a critical failure or poor user experience.

**Practical implications:**

- Keep separate measures for prohibited behavior, task completion, coverage/completeness and experience.

- Define critical-failure conditions explicitly instead of averaging them into a satisfaction score.

- Review quality by task and failure category; high volume can conceal important rare cases.

**Limit:** The notes contain an ambiguous safety term ('roundedness') and no operational definitions for satisfaction or knowledge retention. They do not specify thresholds, measured quality or bank identity.

**Sessions:** [1,368 AI Failures: What They Teach Us About System Evals](https://ai.engineer/nyc/2026/schedule?session=9d72d7ac-a2a2-42cf-b880-5859316d840c), [Proving Alpha: Showcasing AI’s Value in Fundamental Investing](https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca), [From Agent Prototype to Production in Regulated Banking](https://ai.engineer/nyc/2026/schedule?session=e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa)

### 5. Treat automated judges and human review as fallible parts of the system

Two Sigma's selective-approval classifier and the Day 1 harm-detection discussion become more concrete in Day 2: Sonar raises variable judge answers and cognitive surrender, while the banking session suggests a judge that tends toward failing and is part of configuration. The synthesis is to calibrate oversight, rather than assuming either a human or a stricter model is automatically reliable.

**Practical implications:**

- Compare judge decisions with independently adjudicated examples, including severe false passes and unnecessary false failures.

- Version judge model, prompt, rubric and threshold with the evaluated system.

- Use repeat assessments to inspect variability and examine whether reviewers meaningfully challenge unsupported outputs.

**Limit:** Fail-leaning grading is a speaker proposal, not a demonstrated optimum. It can increase false rejections and review burden. The notes do not quantify cognitive surrender or establish that all human review fails to scale.

**Sessions:** [Balancing Acceleration and Safety for AI Agents](https://ai.engineer/nyc/2026/schedule?session=73badd10-6f8c-4c95-b5e7-55fc3d7bafc1), [1,368 AI Failures: What They Teach Us About System Evals](https://ai.engineer/nyc/2026/schedule?session=9d72d7ac-a2a2-42cf-b880-5859316d840c), [The Machine that Changed the World, vAI](https://ai.engineer/nyc/2026/schedule?session=4add802c-6a68-4e9c-93fb-9c1e017193bc), [From Agent Prototype to Production in Regulated Banking](https://ai.engineer/nyc/2026/schedule?session=e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa)

### 6. Make financial work products inspectable at the point of use

Kepler's claim-level numerical evidence connects to the OpenAI session's finance-oriented interface, source passages/tables/charts and document/artifact generation. The Range vignette places a professional's review, editing and adjustment at the end of an analysis workflow. This suggests treating the final brief, spreadsheet or presentation as a decision surface with accessible evidence, not merely a formatted answer.

**Practical implications:**

- Keep source passages, tables, calculation lineage and relevant dates accessible beside consequential claims.

- Distinguish sourced data, computed figures, assumptions and professional judgment in a final artifact.

- Evaluate whether a reviewer can find and correct an error efficiently, including after an artifact is exported.

**Limit:** These are described capabilities and proposed design implications. The notes do not establish feature availability, firm-specific entitlements, provider integrations, data coverage, citation correctness or artifact accuracy. Do not infer provider identities from uncertain spellings.

**Sessions:** [Do Not Let Models Invent Numbers](https://ai.engineer/nyc/2026/schedule?session=2d29f925-f16b-41b3-8086-de0524829cbe), [Building the Next Chapter of AI in Finance](https://ai.engineer/nyc/2026/schedule?session=02f94835-c29d-4cf5-b77a-c5a491b747b8), [We Let Our Financial Planners Write the Agents](https://ai.engineer/nyc/2026/schedule?session=9b002687-09cf-42e2-9282-532ed9d0c184)

### 7. Measure capacity and value after review costs and consequences are included

The Range vignette describes parallel preparation—an agent drafts another client's analysis while a planner is on a call—followed by human review. Contour's counterfactual/value questions and Capital One's lifespan/dependency discussion help assess that proposition: generating work cheaply matters only when the output is useful, reviewable and worth maintaining or safely retiring.

**Practical implications:**

- Measure accepted analyses or prepared meetings per professional, total human time and output quality against the existing process.

- Include retries, review, corrections, exception handling and operating costs when estimating capacity gains.

- Separate professional capacity from client outcomes, sales, financial return and autonomous decision authority.

**Limit:** The Range vignette is an unverified speaker account, not proof of higher advisor throughput, better advice or incremental revenue. Sonar’s claims about compounding errors and long-running work motivate testing, not a universal task-length limit.

**Sessions:** [Does Code Quality Even Matter?](https://ai.engineer/nyc/2026/schedule?session=5191589c-a70e-4806-99dc-86f7794f46b9), [Proving Alpha: Showcasing AI’s Value in Fundamental Investing](https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca), [We Let Our Financial Planners Write the Agents](https://ai.engineer/nyc/2026/schedule?session=9b002687-09cf-42e2-9282-532ed9d0c184), [The Machine that Changed the World, vAI](https://ai.engineer/nyc/2026/schedule?session=4add802c-6a68-4e9c-93fb-9c1e017193bc)

## Three messages for the team report

### 1. Build around a complete, reviewable workflow rather than an impressive answer

Institutional information, procedural knowledge and the final work product belong together. Bridgewater's task-specific information foundation, the finance-interface discussion and the Range skills vignette point toward workflows such as a prepared meeting or a draft analysis that a professional can inspect and accept. The useful success definition includes the evidence, necessary questions, limits, edits and handoff—not just fluent generation.

**Evidence boundary:** This is cross-session synthesis. Range is now identified through the user’s confirmation and official metadata, but the supplied notes provide no measured comparison showing higher advisor capacity or better client outcomes.

### 2. Confidence needs preventive boundaries, independent checks and an evidence trail

Two Sigma's declared access and active controls, Kepler's source/calculation/citation path and Sonar's intent–guardrails–verification–evidence framework reinforce one operating principle: a person or another model agreeing with an answer is insufficient assurance. Make permitted behavior explicit, prevent defined invalid actions, and retain reviewable evidence of the checks performed.

**Evidence boundary:** The frameworks and mechanisms are speaker-described. No control effectiveness, universal code-size threshold or calibrated confidence formula is established by the notes.

### 3. Evaluate complete work across quality dimensions, then measure accepted value against a baseline

The end-to-end-evals notes, the banking session’s quality-vector framing, Sonar's judge-variability concern and Day 1's risk/value discussions argue for separate task, safety and experience measures. Inspect evaluator errors, preserve severe-failure gates, and include human review and repeated-attempt cost before interpreting productivity or business value.

**Evidence boundary:** Neither average quality, pass@k, conversation volume nor adoption proves safe single-attempt completion, causal financial value or a successful rollout.

## Priority follow-ups

- Sonar: obtain definitions and evidence behind the code-confidence framing, codebase-size example, and judge inconsistency claims.

- OpenAI: distinguish demonstrated, available, and planned capabilities; verify data entitlements, provider names, and the role of MCP Apps.

- Ramp: inspect task coverage, partial-credit rules, k and selection costs, repeated-run reliability, and the skill/memory ablation design.

- Range: inspect skill review, difficult-case testing, maintenance, and whether accepted planner capacity improved after corrections and review.

- Banking evaluation: confirm affiliation, the ambiguous safety term, conversation-count definition, judge calibration, and release/rollback evidence.

## Editorial and source notes

Primary content source: your pasted Day2 notes, supplied October14, 2026, and your subsequent clarification that the financial-planning company was Range. Session metadata was matched to the official conference schedule refreshed October14. Speaker claims, official program facts, our interpretations, and proposed tests are kept distinct.

The raw notes’ uncertain terms—“crunchable” and “roundedness”—remain unresolved. The 50k-line code example, eight-to-four skill bundle, and 100K/day conversation volume are preserved as contextual claims, not universal thresholds or verified outcomes. Prefilled questions about approval evidence, release/rollback, and judge validation remain unanswered.

No slide deck, recording, benchmark dataset, product specification, deployment, or financial outcome was independently verified.

Official schedule: [AI Engineer NYC 2026](https://ai.engineer/nyc/2026/schedule).
## Recording follow-up · October 25, 2026

The original attendee observations above are preserved. The following later-source findings clarify them or add related sessions; this is not a claim of additional attendance. The [complete recording supplement](ai-engineer-nyc-2026-recording-supplement.md) contains the wider thematic synthesis and source limits.

### Range

Planners encode repeated work through Pick → Teach → Pack → Test → Ship. Skills retain reasons, clarification questions and stopping conditions. Each has an owner and a separate reviewer; agents send nothing to clients and professionals review recommendations.

**Practical implication:** Start with a recognizable work product and previous cases. Test incomplete and conflicting inputs, then maintain the method as rules change.

**Source and scope:** Organizer transcript. Five to ten cases is the speaker's practical starting suggestion, not statistical release assurance. Online recording is labeled October 13; attended notes place the session on October 14.

[Read / watch source](https://ai.engineer/nyc/2026/talks/range) · [Recording at the session start](https://www.youtube.com/watch?v=akEqiXFo3GM&t=10811s)

### Ramp · Ryan Stevens written follow-up

Each case combines task, synthetic business world, trajectory and accountant-authored rubric. The account reports eight-to-four skill ablation (+2.8 mean-score points across six worlds), 61% spreadsheet-skill compression with essentially unchanged quality, and trajectory-distilled memory (+5.7 points over skills alone).

**Practical implication:** Advance the same business one period, remove prior-period amounts from memory and evaluate next-period work. Compare per-world regressions as well as the average.

**Source and scope:** Speaker-bylined article · October 14. Written primary account, not a located breakout recording or independently reproduced benchmark. Point gains are not relative percentages or a forecast for another team.

[Read / watch source](https://dev.to/dailycontext/building-better-agents-through-end-to-end-evals-pgh)

### Sonar

The transcript emphasizes intent, preventive constraints, independent verification and repeatable release evidence. The creation/release/operation three-loop teaching structure also draws on the prior agenda and our synthesis.

**Practical implication:** Provide low-noise checks at generation time, broader release tests and reproduction of escaped failures. Maintain an accountable promotion/rollback decision.

**Source and scope:** Organizer transcript + agenda-informed synthesis. The confidence product is conceptual. The 50k-line code-translation example is not a universal limit; survey sentiment and vendor results are not independently verified defect reductions.

[Read / watch source](https://ai.engineer/nyc/2026/talks/sonar) · [Recording at the session start](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=2100s)

### OpenAI

The finance product discussion links data access, inspectable source passages/tables, charts and reusable work artifacts. A useful answer must fit the professional's existing output and review process.

**Practical implication:** Test the exported document as well as the chat response: values, periods, units, provenance and corrections must survive into the artifact.

**Source and scope:** Organizer transcript. Product description and forward-looking agent capabilities do not establish universal availability, entitlements or measured financial accuracy. Uncertain provider spelling in the attendee notes is not guessed.

[Read / watch source](https://ai.engineer/nyc/2026/talks/openai) · [Recording at the session start](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=4203s)

### Basis

A reconciliation can reach zero variance through an unsupported adjustment and still be wrong. Behavior specs first ask whether a situation occurred, then whether the agent acted appropriately. Forks isolate a decision; cheaper simulations test repair hypotheses.

**Practical implication:** Record applicable / not applicable separately from pass / fail. Allow an explained discrepancy rather than rewarding a fabricated balancing entry. Reproduce promising simulated repairs in the real environment.

**Source and scope:** Organizer transcript. Agent explanations are clues, not proven causes. The fork is an illustrated repair, not a measured general success rate; outcome evaluations remain necessary.

[Read / watch source](https://ai.engineer/nyc/2026/talks/basis) · [Recording at the session start](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=29362s)

### Coinbase

A forward-moving policy workflow can contain bounded draft/check/refine loops. A policy-checkable result authorizes leaving a node; human review and escalation remain explicit.

**Practical implication:** Define entry, acceptance, iteration budget and takeover conditions for each stage. Reduce supervision only when representative evidence supports the change.

**Source and scope:** Organizer transcript. Framework and examples, not evidence that every illustrated process runs autonomously at Coinbase. Thresholds shown are not portable safety constants.

[Read / watch source](https://ai.engineer/nyc/2026/talks/coinbase) · [Recording at the session start](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=3124s)

### Perpetual

Language interpretation produces typed intent. A compiler validates a closed action vocabulary and can request clarification or refuse. Approved plans are immutable; approval binds the exact outgoing payload. An unknown side-effect outcome goes to manual review rather than blind retry.

**Practical implication:** Distinguish failed, succeeded and outcome-unknown actions. Test changed payloads after approval and interruptions around external writes.

**Source and scope:** Organizer transcript. Typed validity does not establish semantic correctness. Local-model routing examples are not measured fleetwide parity; the training feedback loop is described as future work.

[Read / watch source](https://ai.engineer/nyc/2026/talks/perpetual) · [Recording at the session start](https://www.youtube.com/watch?v=akEqiXFo3GM&t=15828s)

### Citadel Securities

Institutional memory updates and ages beliefs, observes contradictions, grades past predictions and accepts corrections. Reported status and evidence-based status remain separate; historical snapshots are preserved. Models propose updates, while code and people commit them.

**Practical implication:** Store evidence time, origin, source health and correction history. Missing telemetry is unknown, not zero. Backtest as-of snapshots against later observations without rewriting history.

**Source and scope:** Organizer transcript. The reported associations are observational. Client-franchise expansion is a direction, not an established completed capability.

[Read / watch source](https://ai.engineer/nyc/2026/talks/citadel) · [Recording at the session start](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=23913s)

### Clarifications that remain open

The Comet/NatWest affiliation discrepancy and the banking notes' “roundedness” label remain unresolved. OpenAI's uncertain provider spelling is not guessed. The failure-study expression is not adopted as a calibrated expected-loss formula. Ryan Stevens's written account is separate from Alexander Shevchenko's recorded keynote. Range's online recording is labeled October 13; its attended notes remain in Day 2.
