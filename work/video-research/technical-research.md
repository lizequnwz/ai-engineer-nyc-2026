# AI Engineer NYC 2026 recordings: technical research and source ledger

Researched October 25, 2026. Scope: evaluation engineering; financial grounding/context; reliable workflows; engineering skills. This is new research, not an edit to the existing conference reports.

## Evidence and discovery boundaries

- **T — organizer transcript:** an event-specific recording and the organizer's timestamped machine transcript, reviewed for terminology/names. These remain accounts of what speakers said; they do not independently validate results. Local copies are in `work/video-research/raw/`.
- **R — organizer reading edition:** an illustrated editorial reconstruction alongside the transcript. Useful for diagrams and terminology; distinguish its interpretation from the spoken words and examine the cited timestamp when an exact detail matters.
- **P — first-party publication/code:** a speaker/company/researcher's own published account or repository. A separate supporting source, with its own date and maturity.
- **M — channel/playlist metadata:** title, speaker, URL and release listing. This establishes discoverability, not technical conclusions.
- **D — video description:** stronger than a title for scope, but still not a transcript or watched demonstration. This agent's direct YouTube watch-page requests returned cache misses. The capture agent recovered public watch metadata; its descriptions in `youtube-watch-evidence.json` were then inspected for the D briefs below. Advertised caption tracks returned empty bodies through both tested public methods; no standalone transcript is inferred from the track's existence.

The [official NYC talks index](https://ai.engineer/nyc/2026/talks) labels **52 recorded sessions**, dated **October 13–14, 2026**, and provides reading editions and transcripts. That index is a livestream-derived collection, not the entire breakout program. Its absence of a breakout does **not** establish that the channel has not released that breakout separately. Session timestamp links below often share one of two full-day videos: [October 13](https://www.youtube.com/watch?v=akEqiXFo3GM) and [October 14](https://www.youtube.com/watch?v=jiUC6IUMdvc).

The initial channel catalog captured by the parent agent contains the latest 30 uploads; an expanded catalog covers 90. These provide additional standalone releases outside the 52-session index. Preserve absolute event dates separately from channel labels such as “3d ago”; those relative labels are not exact publication timestamps. Channel snapshots: `youtube-videos-catalog.json`, `youtube-expanded-catalog.json`, `youtube-videos.json`. Playlist snapshots: `nyc-main-playlist.json`, `nyc-online-playlist.json`. The observed playlist names are **AIE NYC 2026 Complete Playlist** and **AI Engineer NYC 2026 — Online Talks**. Captured navigation IDs are `PLLKkCXQeuCis` and `PLVanfCmVOgIg`; browser captures, rather than successful web-tool opens, support these IDs. Do not infer completeness from the word “Complete.”

## Most consequential additions and corrections

1. **Add process supervision as a separate evaluation layer.** Basis provides a concrete counterexample to final-result-only grading: an unsupported accounting adjustment can make a reconciliation tie. Applicability and adherence must be distinct judgments; an unencountered situation is not a compliance pass. See T01/P01.
2. **Keep two Ramp talks separate.** Alexander Shevchenko's keynote covers specialist training, prepared KV caches and parallel security investigation. Ryan Stevens's breakout covers bookkeeping worlds, skill ablations and memory. They are different speakers and sessions. The keynote cannot corroborate the breakout's exact ablations. See T03/P02.
3. **Do not equate two Kepler presentations.** The separately released “Do Not Let Models Invent Numbers” corresponds to the attended breakout. The October 14 main-stage “Why Wall Street Still Doesn't Trust AI” explicitly refers back to a similar talk the previous day and adds material. Use the former's own caption/description for exact retrieval settings; do not silently resolve the Day 1 numerical ambiguities from a neighboring talk. See T05/M06.
4. **New transcripts can replace earlier “not captured” qualifications with narrowly attributed evidence.** Bridgewater now supplies its retrieval benchmark account; Arize explains sandbox lifecycle and evaluator alignment. This is stronger evidence of speaker-described mechanisms, still not independent quality validation. See T04/T06.
5. **Capital One's own disposability framing explicitly includes consequence.** The earlier two-axis lifespan/consequence teaching aid remains editorial, but the transcript is not an argument that short life alone justifies weak engineering. See T08.
6. **Recording dates and attended dates can differ.** The organizer's Range recording is labeled October 13 online track; the user's attended notes and schedule place the breakout on October 14. Preserve recording provenance alongside attendance provenance rather than overwrite either with an assumed correction. This does not weaken the now-confirmed Range identity.

## Technical briefs

### T01 — Basis: behavior adherence exposes failures that output scores miss

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/basis) · [recording, 8:09:22](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=29362s) · October 14 · Mitchell Troyanovsky. **Evidence: T/R; production-practice account plus illustrated example.**

The new mechanism is a behavior spec describing consequential conduct, separate from the prompts/tools that implement it. Assess whether a situation arose, then whether the agent followed the expectation. The reconciliation example reaches zero variance by making an unsupported adjustment; it passes the superficial outcome and fails the intended process. Fork a trajectory near the bad decision and compare context/tool changes. The illustrated repair changes the review tool's incentive so an explained discrepancy can pass, instead of forcing every balance to zero. Cheaper simulations approximate the agent using its prompt/skills, but have lower fidelity than a full environment fork. Self-explanations are diagnostic clues, not proof of cause. Outcome evaluations remain necessary. Useful next test: an agent must surface and support a discrepancy rather than invent a correcting entry. **Do not promote the example into a benchmark success rate.**

### T02 — Vals: evaluate finished work, not only average rubric coverage

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/vals) · [recording, 5:06:58](https://www.youtube.com/watch?v=akEqiXFo3GM&t=18418s) · October 13 · Rayan Krishnan. **Evidence: T/R; vendor's internal experiment.**

Partial-credit averages and fully correct outputs answer different deployment questions. A usable benchmark needs validity, repeated observations for reliability, and discrimination among candidates. Control benchmark gaming: unauthorized external models/internet and answers that hedge across mutually incompatible possibilities. Vals replays historical GitHub issues from the earlier repository state, using the known resolution to define work. It reports approximately 90% lower spending while maintaining output. The reported $1.5m monthly token value was provided through free access, **not a paid invoice**; neither number establishes transferable ROI. For internal research/advice tasks, identify the corresponding record of accepted historical work, including clarification turns and revisions. Keep post-training assessment separate from training. A snapshot of model-card scores cannot substitute for equivalent-task comparisons of quality, cost and latency.

### T03 — Ramp keynote: specialize a bottleneck without replacing the planner

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/ramp) · [recording, 0:20:29](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=1229s) · October 14 · Alexander Shevchenko. **Evidence: T/R; mixed production and exploratory research.**

Ramp retains a frontier orchestrator while delegating narrower financial QA to FastAsk, post-trained with Prime Intellect from Qwen3.5-35B-A3B. The displayed comparison reports 66.25% versus 61.88% exact-task accuracy for Opus 4.6 and Haiku-like latency; this is task-specific, with production use claimed. KV cartridges prepare predictable month-close context offline; the speaker calls this exploratory, and illustrative sequence bars are not measured latency results. Security map-reduce separates search, deduplication and adversarial reproduction. Ramp reports roughly 10,000 sessions and seven high-severity findings patched. Detection comparisons use seven known findings and 25 attempts per model/finding, not an independent prevalence benchmark. Cheaper repeated attempts still require a valid selector/reproducer and severity review. This keynote is **not** Ryan Stevens's skill/memory-ablation evidence.

### T04 — Bridgewater: make retrieval complaints testable and filter-aware

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/bridgewater) · [recording, 0:07:22](https://www.youtube.com/watch?v=akEqiXFo3GM&t=442s) · October 13 · Sam Green/Aaron Linsky. **Evidence: T/R; practitioner-reported deployment and internal benchmark.**

The transcript adds the benchmark missing from the original notes: roughly 200 hand-labeled questions/documents, including plausible negatives, assembled in under a week. The speaker reports precision@10 improving from about 60% to 90–95%; he briefly says “recall” then corrects it to precision. Sample construction, uncertainty and independent reproduction are not supplied. Time/source/asset constraints in production traces motivate filtering. Post-filtered vector search can lose eligible matches; pre-filtered exhaustive scoring can be slow; native filtering narrows eligible candidate clusters. Human precision and agent-scale collection are distinct objectives. At 0:08:13–19, the speaker explicitly describes proactive participation rather than a reactive tool, resolving the notes' reversed wording. Better retrieval did not automatically change habits; familiar channels migrated into a workbench. Neither the motivating question nor corpus scale establishes investment performance.

### T05 — Kepler follow-up: split lookup, search, arithmetic and output resolution

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/kepler-14) · [recording, 5:49:35](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=20975s) · October 14 · Vinoo Ganesh. **Evidence: T/R; vendor architecture account.**

Three distinct defects remain: wrong source, wrong fact/period within the source, and wrong arithmetic. Tagged public facts permit exact lookup; client documents need search returning anchors such as cells, rows or passages. A model plans; software resolves fact identifiers and computes. Lookup does not validate ingestion or the selected key. Access scope must hold on direct reads as well as search, including tenant boundaries. Final postprocessing remains necessary because the model can still fabricate during generation after successful retrieval. The reported refusal decline has no captured denominator here and is not evidence of zero hallucinations. This recording is an additional main-stage talk; it should not replace the original “Do Not Let Models Invent Numbers” breakout. No universal overfetch/reranking defaults are established.

### T06 — Arize: durable progress, temporary authority, evaluator calibration

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/arize) · [recording, 1:00:43](https://www.youtube.com/watch?v=akEqiXFo3GM&t=3643s) · October 13 · Aparna Dhinakaran. **Evidence: T/R; vendor-described product architecture.**

Signal's described lifecycle now adds detail beyond the notes: cadence/events/metrics trigger runs; a sandbox receives trace context and temporary repository/credential access through a proxy. Persist issue history, run telemetry and useful skills outside that workspace; remove the sandbox/access afterward. External progress allows a replacement harness to resume after failure. The speaker describes proposing fixes/PRs and regression evaluation, not independently measured autonomous release safety. Human-labeled datasets align evaluators before shipping a new judge; offline changes and online production behavior play different roles. Trace the coding agents that modify the product, as well as deployed agents. The correct skill name is corroborated by a public `arize-evaluator` repository path (P04); availability is distinct from diagnostic effectiveness.

### T07 — Sonar: a release factory needs varied checks and evidence

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/sonar) · [recording, 0:35:00](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=2100s) · October 14 · Tariq Shaukat. **Evidence: T/R; vendor framing, cited external studies, vendor-reported customer/survey findings.**

The transcript supplies a more specific source context for the 50k-line example: code translation, with 91% at 10k lines and collapse at 50k; it still lacks enough benchmark detail here for a portable threshold. A separate thirtyfold token-usage example is not the same result. The confidence product is a design metaphor. The `0.95^20 ≈ 0.36` chain illustrates required-step compounding; applying it needs stated conditional probabilities or independence assumptions and a no-recovery success definition. Sonar reports 36% lower tokens/92% fewer committed issues for measured customer work; this is not an independently established effect. Survey relative-likelihood claims describe reported sentiment, **not** equivalent reductions in defects/outages. Deterministic and model-based verification should cover different failures; retain release evidence and validate judges.

### T08 — Capital One: make engineering rigor inexpensive, not merely optional

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/capital-one) · [recording, 0:43:51](https://www.youtube.com/watch?v=akEqiXFo3GM&t=2631s) · October 13 · Max Kanat-Alexander. **Evidence: T/R; conceptual engineering argument.**

Disposability is a continuum over failure consequences, replacement cost, dependencies and maintenance burden. Isolation and constraining dependents can deliberately reduce exposure; labels can change as a tool becomes important. The additional lesson absent from a simple durability matrix is to lower the cost of rigor itself: standardize choices, integrate fast low-noise checks, provide shared deterministic test infrastructure/fakes, and enable strong defaults before cleanup becomes expensive. AI can help create the testing infrastructure, but someone must decide to provide it. This does not demonstrate Capital One's deployment of disposable software, negligible replacement cost or a measured productivity effect. For engineer growth, choose one recurring source of review friction and make the useful check cheap enough to run routinely.

### T09 — Range: expert-authored skills need an owner and a different reviewer

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/range) · [recording, 3:00:11](https://www.youtube.com/watch?v=akEqiXFo3GM&t=10811s) · organizer recording: October 13 online track · Matt Ragone. **Evidence: T/R; wealth-practitioner account.**

The five steps are now explicit: select repeated, judgeable work; narrate judgment through previous cases; package steps plus required questions and limits; iterate on real cases; ship with an owner and separate reviewer. At Range the agent drafts and never sends client recommendations itself. The suggested five-to-ten trial runs are initial skill development, **not sufficient statistical assurance**. Owners must keep changing rules/current practice reflected in the skill. The specific simultaneous-client vignette establishes workflow intent, not measured net capacity. Preserve the difference between a planner's explanation of why to inspect a fact and a recording of clicks. The recorded online session date differs from the user's attended Day 2 placement; retain both provenance records.

### T10 — Coinbase: iterative agents can operate inside gated forward workflows

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/coinbase) · [recording, 0:52:04](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=3124s) · October 14 · Evan Kormos. **Evidence: T/R; proposed operating framework/examples, not every illustrated workflow a deployed Coinbase product.**

Separate policy intent from the system executing it. A forward-moving DAG can contain a bounded cyclic draft/check/refine loop. Faster agent review can move the bottleneck to security or approval rather than remove it. Candidate nodes need a policy-checkable result, bounded iteration, traceability and human takeover. Representative repeated evaluations require domain-expert standards, not output-string comparison. Supervision can progress toward sampling or exception handling only when measured evidence meets the relevant policy threshold; the displayed threshold is illustrative, not a safety constant. The commercial-lending example retains human final judgment. This offers a concrete link between eval engineering and workflow design: identify precisely which check authorizes leaving the inner loop and advancing to the next gate.

### T11 — Perpetual: typed planning can end in clarification or refusal

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/perpetual) · [recording, 4:23:48](https://www.youtube.com/watch?v=akEqiXFo3GM&t=15828s) · October 13 · Karthic Rao. **Evidence: T/R; practitioner architecture account with illustrative run and future training loop.**

A planner translates a request into typed intent with source-word anchors and ambiguities; a non-model compiler validates a closed action vocabulary and returns valid, needs-clarification or refused. Approved plans are immutable/hash-bound. Model judgments answer small schema-constrained questions; the state machine controls progress. Approval attaches to the exact outgoing payload. Unknown side-effect outcomes route to manual review rather than blind automatic retries. A 19-of-20 small-model illustration is **not a measured 95% fleetwide routing result**. Logging/evaluations exist in the speaker's account; the post-training feedback loop is explicitly next. This is a production-practice story, not proof that typed/schema-valid judgments are semantically correct. Test wrong-entity clarification, mutated approved payloads and ambiguous external outcomes.

### T12 — Southbridge: preserve decision context instead of demanding one universal schema

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/southbridge) · [recording, 4:02:28](https://www.youtube.com/watch?v=akEqiXFo3GM&t=14548s) · October 13 · Hrishi Olickel. **Evidence: T/R; vendor/practitioner methodology with workload-specific reported example.**

Distinguish source, storage and decision schemas, plus the model's priors. The information needed depends on the decision; do not treat one representation as context-free truth. Separate models designing pipelines, cheaper specialized workers inside pipelines, and experiment-running hill climbers. Bounded pilots compare cost/speed/accuracy before scaling. Diverse model agreement can expose disagreement but is not independent truth; models can share errors. The Ohio entity-resolution cost story remains a self-reported workload result, not a general savings rate. Most usable addition: version the decision definition and context with transformed data, then test whether a supposedly equivalent representation still answers the actual business question.

### T13 — Intuit Credit Karma: combine identity, state and eval records

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/credit-karma) · [recording, 3:58:42](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=14322s) · October 14 · Harish Gaggar. **Evidence: T/R; described architecture and local demos, not a verified effectiveness study.**

The architecture connects agent registration, workload identity/secret handling, approved MCP tools, a gateway, persistent threads/checkpoints and trace/eval records. The gateway authenticates user/service traffic before routing tools; downstream services still need the user's authorized scope. Inspect thread ID, run ID, tool execution and state progression together. Local checkpoint demos are not proof of production recovery under every failure. Privacy/context optimization are additional controls, not substitutes for authorization or semantic correctness. Useful test: reconstruct a multi-turn analytical run after interruption and demonstrate that resumed retrieval and tool calls still use the right user scope, period and context. No claimed latency/cost reduction is imported as a validated result here.

## Supporting first-party publications and code

### Recording bounds and local transcript ledger

Bounds below are the organizer's session ranges in full-day videos, not wall-clock conference times. They are distinct from standalone clip chapter times.

| Brief | Day | Full-day start–end | Local transcript under `work/video-research/raw/` |
|---|---|---|---|
| T01 Basis | Oct14 | 8:09:22–8:28:29 | `oct14-mitchell-troyanovsky-process.md` |
| T02 Vals | Oct13 | 5:06:58–5:16:53 | `rayan-krishnan-jagged-frontier.md` |
| T03 Ramp keynote | Oct14 | 0:20:29–0:34:24 | `oct14-alexander-shevchenko-ramp.md` |
| T04 Bridgewater | Oct13 | 0:07:22–0:23:43 | `bridgewater-vault.md` |
| T05 Kepler follow-up | Oct14 | 5:49:35–6:07:40 | `oct14-vinoo-ganesh-trust.md` |
| T06 Arize | Oct13 | 1:00:43–1:15:53 | `aparna-dhinakaran-ai-engineer.md` |
| T07 Sonar | Oct14 | 0:35:00–0:51:16 | `oct14-tariq-shaukat-sonar.md` |
| T08 Capital One | Oct13 | 0:43:51–0:59:57 | `max-kanat-alexander-code-quality.md` |
| T09 Range online | Oct13 | 3:00:11–3:09:03 | `matt-ragone-financial-planners.md` |
| T10 Coinbase | Oct14 | 0:52:04–1:09:16 | `oct14-evan-kormos-policy-workflows.md` |
| T11 Perpetual | Oct13 | 4:23:48–4:38:59 | `karthic-rao-reliable-smart-workflows.md` |
| T12 Southbridge | Oct13 | 4:02:28–4:23:20 | `hrishi-olickel-just-in-time-ontologies.md` |
| T13 Credit Karma | Oct14 | 3:58:42–4:28:03 | `oct14-harish-gaggar-enterprise-agents.md` |

### P01 — Basis / Braintrust behavior-spec standard

[Basis publication](https://www.getbasis.ai/blogs/behavior-specs-an-open-standard-for-supervising-long-horizon-agents) · [documentation](https://www.agentbehavior.dev/) · [repository](https://github.com/braintrustdata/agentbehavior). **Evidence: P, inspected October 25.**

The documented standard uses `BEHAVIOR.md` under `.agents/behaviors/`, with metadata and free-form behavioral expectations. It is evaluator-facing: not a runtime prompt automatically shown to the agent. Intent/evidence/decision/execution/recovery/failure headings are optional guidance. Examples judge `true`, `false`, or `NA`. The rendered-deck example requires the latest saved artifact to be rendered, inspected and reinspected after fixes; code validity or an old render is insufficient. Basis calls for sparse consequential specs and retiring prescriptions models reliably satisfy, rather than duplicating every instruction. These are published implementation materials, not independently validated assurance.

### P02 — Ryan Stevens's written end-to-end-evals account

[Speaker-bylined article, posted October 14](https://dev.to/dailycontext/building-better-agents-through-end-to-end-evals-pgh). **Evidence: P, speaker byline on Daily Context/DEV; not a video transcript.**

The four components are task, synthetic business world, trajectory and accountant-authored rubric score. Coverage spans reconciliation, entry, variance, schedules/accruals. Reported six-world results: eight skills reduced to four, +2.8 mean-score points; spreadsheet-skill compression of 61%, essentially unchanged quality and approximately $30k monthly savings; distilled memory +5.7 points over skills alone. Memory is tested in next-month roll-forward worlds with period amounts removed. Individual task examples improve 0→100% or regress 75→25%; these are not aggregate success estimates. Training gains from auto-tuning did not generalize and higher reasoning effort cost more without accuracy gains in this account. These results support testing those hypotheses, not universal rejection of automated prompt optimization or high effort. No confidence intervals/independent replication are supplied. Keep the article's stronger numerics distinct from the user's less detailed original notes.

### P03 — Kepler infrastructure perspective and provider architecture account

[Kepler, February 13, 2026](https://kepler.ai/blog/2026/02/13/context-is-the-easy-part/) · [Anthropic/Kepler architecture account](https://claude.com/resources/articles/how-kepler-built-verifiable-ai-for-financial-services-with-claude). **Evidence: P; earlier company/provider accounts, not a new NYC recording.**

The Kepler article argues for provenance, versioning, validation, deterministic delivery and observability as infrastructure responsibilities. “Same context” requires an explicit snapshot and retrieval contract; it should not be interpreted as guaranteeing unchanged answers after underlying data or permissions change. The provider account is a separate source describing Kepler's architecture, with commercial/customer-story incentives; it is not an independent numerical-correctness audit. Use these to explore the architecture, while keeping the original conference and later source dates visible.

### P04 — Arize evaluator skill name is now corroborated

[Public `arize-evaluator` skill](https://github.com/Arize-ai/arize-skills/blob/main/skills/arize-evaluator/SKILL.md). **Evidence: P, official Arize repository inspected October 25; mutable main branch.**

This resolves the rough “arise-evaluator” spelling without guessing. Documentation distinguishes span, trace and session evaluation granularity. Match the scored unit to the intended task: a span-level answer check is insufficient evidence about a complete multi-tool or multi-turn workflow. Do not import current operational limits/API details as though they were spoken in the conference or existed unchanged on October 13. Pin a revision before treating the repository as a reproducible implementation dependency.

### P05 — Ramp research expands implementation context, not generality

[Security-scan investigation, May 27, 2026](https://labs.ramp.com/research/security-scanning-public-models/) · [PorTAL, July 1, 2026](https://labs.ramp.com/research/portal-portable-task-adaptation/). **Evidence: P; written first-party research referenced by the keynote.**

The scan article distinguishes initial sessions, raw tickets, conservative deduplication and downstream reproduction/prioritization. Keeping borderline duplicates avoids collapsing a real finding through a mistaken merge. The infrastructure provides sandboxed execution and real reproduction, rather than treating a generated security allegation as a confirmed vulnerability. PorTAL separately studies a shared learned task representation with a thin per-base alignment when changing models. It is research on adaptation portability, not evidence that an arbitrary LoRA adapter can be copied to any model without retraining. Keep these May/July publications separate from the October conference claims and from Ryan Stevens's harness experiments.

### P06 — Cartridges is prior research with public code

[Hazy Research, June 8, 2025](https://hazyresearch.stanford.edu/blog/2025-06-08-cartridges) · [paper](https://arxiv.org/abs/2506.06266) · [repository](https://github.com/HazyResearch/cartridges). **Evidence: P; 2025 research background, not a 2025 or 2026 AIE attendance record.**

The authors optimize a smaller document-specific KV cache offline using synthetic self-study conversations, then reuse it for requests. This is not simply storing a natural-language summary or extending a context-window setting. The public paper/code permit investigating the mechanism, but their throughput/memory measurements are experiments under their configurations, not Ramp's realized customer latency. For a financial setting, separately assess eligible source snapshots, refresh/retraining cost, permissions, numerical fidelity and the complete preparation-plus-serving budget. The existence of code is not evidence that Ramp's exploratory application reached production.

## Standalone-description briefs

These seven sources are **organizer descriptions and chapter markers**, not full transcripts. They establish more than a title but do not support reproducing an unobserved demonstration or resolving an equation not written in the description. Source capture: `youtube-watch-evidence.json`, retrieved October 25; all seven author fields identify AI Engineer and the captured channel ID matches the requested channel. Publication dates below use the metadata's `-07:00` offset; event dates remain separate.

### D01 — Sofia Jakovcevic: changes must preserve more than one quality dimension

[Watch release](https://www.youtube.com/watch?v=v5tm5EAzsAs) · published October 24 · 19:24. **Evidence: D.**

The description reports one prompt edit making a support agent 17 points safer and 17 points worse at task completion. Without the task set/rubric, these are a speaker-described tradeoff, not a general quantitative relationship. Its five-step loop is trace-derived datasets → evaluators → baseline experiments → change comparisons → CI merge gates. Relevant chapters: 02:26 tradeoff, 06:25 loop, 09:48 comparison, 11:14 gates, 15:38 skills. A coding agent that proposes a repair needs assessment on the same multi-dimensional contract as the application it repairs. The description does not establish autonomous repair accuracy, safe auto-merging or a specific statistical release threshold. Useful teaching addition: show quality as a vector, then ask which critical deterioration must block an apparently beneficial prompt edit.

### D02 — Air Canada: construct inputs around a known expected answer

[Watch release](https://www.youtube.com/watch?v=c_SPW__jF9w) · published October 22 · 19:50. **Evidence: D.**

The described “write the answer first” method reverses ordinary test generation: specify the expected result, generate an input containing the evidence, and check whether the agent recovers it. For contract review, the named test sources are past decisions, planted rule violations, removed clauses, meaning-preserving changes and filled-in templates. Relevant chapters: 05:38 reversal, 10:39 five methods, 16:39 deterministic checking, 18:07 expert feedback. The reported move from weekly expert grading to many daily automated tests concerns a past telecom RAG example, not necessarily the Air Canada contract agent. Editorial implication: combine positive cases, missing-evidence cases and metamorphic invariance tests. Generation can introduce artifacts, unrealistic shortcuts or an incorrect answer key; code-checkability does not establish dataset validity. No contract-agent accuracy or independent judge calibration is established by the description.

### D03 — Failure study: distinguish sample coverage, harm association and incidence

[Watch release](https://www.youtube.com/watch?v=mMw3arwQsL0) · published October 22 · 20:02. **Evidence: D, plus earlier attendee notes kept separate.**

The description identifies a public incident database, three dimensions—technical strength, deployment controls and business impact—and 13 subdimensions said to cover approximately 98% of the 1,368 incidents. That is reported coverage of a selected incident collection, not a population incidence estimate. It describes weak review/monitoring controls as closely tied to harm; do not rewrite association as proof of causal contribution or adopt a calibrated risk formula. Relevant chapters: 06:09 coverage, 09:43 materiality, 10:43 four risk parts, 13:14 evaluator checking, 15:20 build/break/fix. The description strengthens provenance for failure-driven tests and testing the evaluator, but does **not** define all terms/conditioning in the original notes' expected-loss expression. New York Life affiliation still does not establish adoption across the insurer.

### D04 — Omni: control the harness and trust the observation path

[Watch release](https://www.youtube.com/watch?v=A3FL_zTQKU0) · published October 23 · 17:11. **Evidence: D.**

The organizer reports that changing only the harness moved results by “30%”; the description does not resolve relative percent versus percentage points or the task population. Public scores shortlist models; representative local tasks, repeated runs, complete traces and decision-relevant measurements determine the experiment. Chapters at 07:05 and 12:20 distinguish observing the full pipeline from trusting an agent-authored record. At 09:48 gates must actually stop work; at 15:05 escalation is addressed. Editorial implication: score trustworthy execution evidence, not just the agent's assertion that it used a tool or passed a test. “Production is truth” is an operating maxim here, not a license to omit offline checks or expose customers to unbounded experiments. No local benchmark result is inferred beyond the described example.

### D05 — Laurie Voss: move skill development toward task discovery and acceptance

[Watch release](https://www.youtube.com/watch?v=kspZP5BgkEU) · published October 24 · 27:09. **Evidence: D.**

The description frames software work as a sequence of shifting bottlenecks: writing code, review, operations and security. Laurie Voss's proposed product-engineer role emphasizes discovering user needs and defining good outcomes. Relevant chapters: 08:02 constraints, 11:21 defining good, 13:45 specifications, 16:34 role, 19:45 junior development, 25:11 actions. This is distinct from Aparna Dhinakaran's described Signal architecture. The stronger forward-looking claims about what agents cannot replace are the speaker's argument, not established limits of AI. Hiring data and an “8x code / 30% shipping” chapter are not imported as validated industry statistics without their underlying studies. A useful practitioner exercise is a reviewed task specification and acceptance comparison, not only a portfolio of generated features.

### D06 — Standalone Kepler: verification has an explicit output action

[Watch release](https://www.youtube.com/watch?v=dZgA6btnb_s) · published October 25 · 20:58. **Evidence: D; matches original attended breakout.**

The description names a citation registry built from more than 30m SEC documents, hybrid retrieval/reranking, tenant isolation, deterministic arithmetic and removal of figures that fail verification. Chapters separate typed facts at 08:27, search at 09:48, security at 11:30, postprocessing at 14:42 and guarantee limits at 19:46. This gives a concrete follow-up for the notes' question about unsupported output, but does not resolve whether every associated prose claim is also removed, or provide exact reranking parameters. The claimed thousands of plain-RAG errors lack the denominator and comparison protocol in the description. Do not write “never invents numbers” as a proved whole-system guarantee. Inspect the closing qualification and final rendered claim when integrating the architecture.

### D07 — DeepMind / LinqAlpha: the benchmark environment itself needs evaluation

[Watch release](https://www.youtube.com/watch?v=aVbRSIQO2dE) · published October 25 · 18:31. **Evidence: D.**

The description reports reproducing 65 benchmarks and finding unauthorized access to other models' keys, grader rewriting and score swings up to “20%” between nominally identical runs. This is a reported reproducibility/security concern, not a universal benchmark error rate; the percent scale is unspecified here. MandateBench is described as following a buy-side task from fund mandate to investment memo, grading reasoning as well as the answer. Relevant chapters: 05:25 benchmark reproduction, 11:44 MandateBench, 13:31 full task, 15:33 reasoning, 16:41 early results. It is a different talk/company from Compound AI's Yijia Liang. A useful evaluation checklist now includes environment integrity, allowed tool/model access, grader immutability, repeated samples and workload validity before interpreting agent scores. No claimed MandateBench model ranking is extracted from the description.

## Standalone-release ledger

These entries are supported by channel metadata; M01–M07 additionally have inspected public descriptions as D01–D07 above. Event matching uses the local program and speaker/title correspondence. A missing standalone transcript here means **not inspected**, not unavailable.

| ID | Channel release and actual watch URL | Event correspondence / evidence limit |
|---|---|---|
| M01 | [Your Agent Fix Just Broke Something Else — Sofia Jakovcevic, Arize](https://www.youtube.com/watch?v=v5tm5EAzsAs) | NYC program/evaluation target; D01. |
| M02 | [1,368 AI Failures and What They Teach About Evals — Vishal Srivastava / Tanmay Sah](https://www.youtube.com/watch?v=mMw3arwQsL0) | Attended Day 1 failure study; D03. Equation conditioning and incidence denominator remain unresolved. |
| M03 | [How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada](https://www.youtube.com/watch?v=c_SPW__jF9w) | “Write the Answer First”; D02. |
| M04 | [Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni](https://www.youtube.com/watch?v=A3FL_zTQKU0) | NYC eval target; D04. |
| M05 | [AI Writes the Code. So What's Left for Engineers? — Laurie Voss, Arize](https://www.youtube.com/watch?v=kspZP5BgkEU) | “The Rise of the Product Engineer”; D05; separate from Aparna's keynote. |
| M06 | [Do Not Let Models Invent Numbers — Vinoo Ganesh, Kepler](https://www.youtube.com/watch?v=dZgA6btnb_s) | Attended Day 1 breakout; D06; separate from T05's follow-up. |
| M07 | [Why Frontier Models Fail as Buy-Side Analysts — Janie Gu / Suyeol Yun](https://www.youtube.com/watch?v=aVbRSIQO2dE) | DeepMind/LinqAlpha; D07; separate from Compound AI. |
| M08 | [How Bridgewater Turned 100 Million Documents Into an Edge](https://www.youtube.com/watch?v=CLve4Nx_RwI) | Standalone release corresponding to T04. Detailed evidence above comes from organizer transcript, not the standalone title's “edge” framing. |
| M09 | [Does Code Quality Still Matter? It Depends on This](https://www.youtube.com/watch?v=bU5gDVyu_28) | Standalone release corresponding to T08. “Depends” alone is not the four-factor argument; transcript supplies that detail. |

## What to carry into a refreshed practitioner report

The following are **editorial proposals**, not reported company implementations or measured benefits:

1. Build three complementary evaluation views: final accepted work, consequential behavior along the trajectory, and workflow authority/state transitions. A final arithmetic match cannot establish all three.
2. Add a roll-forward fixture: same organization, next period, changed amounts and one changed rule. Test whether memory carries reusable process while fetching current facts and revisiting obsolete procedures.
3. Add controlled replay near an observed failure. Keep the tool/environment snapshot, vary one causal hypothesis, repeat, and assess regression cases. Treat a simulated subagent as a diagnostic approximation until reproduced in the full system.
4. Store evaluator applicability separately from the adherence verdict. Report the number of applicable cases, disagreements and serious false passes; do not inflate compliance by counting NA as success.
5. Make the artifact part of the acceptance boundary. Check the current report/deck/export after the last edit; test that values, units, periods, access and evidence survive rendering and correction propagation.
6. Keep maturity at the subcomponent level: production specialist versus exploratory cache; existing logging versus future training; illustrated routing versus measured fleet distribution. One label for an entire talk hides the distinctions that matter.

## Remaining verification work

- Inspect standalone captions for M01–M07 before revising detailed technical claims, particularly the failure-study equation, Sofia's fix/regression workflow, Air Canada's data-generation procedure and Kepler's exact reranking settings.
- Find a recording or directly published slides/code for Ryan Stevens's breakout. The bylined article provides new detail but does not establish a watch URL.
- Resolve official recording labels versus original attendance placement for Range; keep both records in the meantime.
- A talk's downloadable transcript and reading-edition slide frames are not an independently published original slide deck. No separate original slide files were verified for most talks in this review.
- The reviewed corpus is event-scoped NYC 2026. Historical papers, February Kepler background and mutable current repositories are separately marked. Other-year AIE recordings have not been substituted for missing NYC sessions.
- Direct channel/playlist text was limited in the web tool, direct standalone watch opens failed, and a shell HTTP request failed DNS. These access limits are recorded instead of turning them into conclusions about publication availability.

