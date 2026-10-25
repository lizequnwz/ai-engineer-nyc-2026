# Finance and wealth recording evidence ledger

Research cutoff: **October 25, 2026**. Original paraphrase of primary sources. This is an evidence update for the earlier conference reports, not a new industry survey.

## What was inspected

- Official [NYC 2026 talks index](https://ai.engineer/nyc/2026/talks): the fetched page has **52 reading/transcript sessions**, 25 labeled October 13 and 27 labeled October 14. These are livestream/online-track reading editions, **not the full set of conference breakouts**. A search-index result reporting 53 is not the fetched-page count.
- Official [transcript download](https://ai.engineer/reading/nyc-2026/transcripts.zip): text extracted locally; twelve finance/strategy transcripts below were read substantively in full. This agent did **not watch the videos**. Transcripts can contain recognition errors; source titles and firm identities are checked against the official page/index rather than blindly copied from spoken-word recognition.
- Official AI Engineer [videos](https://www.youtube.com/@aiDotEngineer/videos) and [playlists](https://www.youtube.com/@aiDotEngineer/playlists), including the first-party catalog snapshots shared in this workspace. The expanded channel capture contains 90 individual releases across three fetched catalog pages; the latest 30 individual uploads include additional breakouts absent from the 52-talk index. The [NYC playlist](https://www.youtube.com/playlist?list=PLLKkCXQeuCis) currently lists livestreams and conference bookends; the [online playlist](https://www.youtube.com/playlist?list=PLVanfCmVOgIg) lists 20 individual releases. A finite listing is not proof that another recording does not exist.
- Earlier Day 1/Day 2 notes, conference takeaway notes, and October 10 `program.json` were checked for evidence upgrades and discrepancies. Original outputs remain unchanged.

The date below is the **official event/recording label**, not a verified upload date. Exact individual-release dates recovered by the capture agent from public YouTube watch metadata are listed below. A relative catalog label such as “1d ago” is not used to invent a publication timestamp. Public caption endpoints returned no readable text, so descriptions remain description evidence.

## Highest-value additions and corrections

1. **Add direct wealth-firm cases, not only historical large-bank disclosures:** Range, Arca, and Perpetual now have substantive released accounts. They preserve professional review and operational authority while delegating preparation or bounded workflow steps.
2. **Upgrade sparse agenda placeholders:** Coatue and Blackstone/Norm now have real titles and operating principles; Apollo/Rowspace has specific credit workflows, data-source reconciliation, and human QA. These remain speaker reports, not audited results.
3. **Correct the grounding guarantee:** Kepler explicitly acknowledges that a model can still invent a number after pointer lookup, motivating post-processing. Typed facts and deterministic rendering are a useful design, not proof of universal numerical correctness.
4. **Use investment outcomes carefully:** Bridgewater retrieval precision, Apollo preparation-time examples, Citadel Securities backtests, and Contour-style idea attribution are different evidence types. None should silently become causal alpha or independently verified ROI.
5. **Preserve metadata disagreements:** Range’s published reading edition labels the online recording October 13; the attendee account and October 14 program place the attended session on Day 2. Do not silently rewrite attendance history. The original schedule UUID was also reused between snapshots.

## Transcript-backed cases

### 1. Bridgewater — evidence substrate plus proactive investor attention

**Title:** Vault: Making Unstructured Data Work for Investing. **Speakers:** Aaron Linsky and Sam Green. **Event:** October 13, main stage. **Evidence:** official full transcript read; no video watched.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/bridgewater) · [Livestream at 0:07:22](https://www.youtube.com/watch?v=akEqiXFo3GM&t=442s) · [Individual release: How Bridgewater Turned 100 Million Documents Into an Edge](https://www.youtube.com/watch?v=CLve4Nx_RwI)

**What the account adds:** Vault combines internal research with external sources and organizes material by market, country, concept, and discussed period. The speakers report more than 100 million documents and 135 external sources. Filter-aware retrieval, human relevance labels, and agentic search serve different information needs than a short human search. Adoption required moving existing subscription/email-folder habits into saved searches and collections. Their investor workbench proposes topics with inspectable evidence; research findings flow back into the corpus.

**Numbers and limits:** About 200 manually labeled questions underpin the reported precision@10 change from roughly 60% to 90–95% after several changes. The speaker briefly says “recall” before correcting to precision. No held-out design, uncertainty, answer-accuracy measure, or causal investment result was supplied. Public-chat versus Vault source counts are one demonstration, not a controlled benchmark. The reactive/proactive wording in the raw attendee note was reversed: the desired change is **reactive resource → proactive participant**.

**Operational lesson:** preserve entitlement and time filters, build a task-specific relevance set, and design the human evidence brief plus feedback capture—not just an index.

### 2. Range — professional methods become maintained skills

**Title:** We Let Our Financial Planners Write the Agents. **Speaker:** Matt Ragone; the YouTube title uses Matthew. **Event label:** October 13, online track; conflicts with Day 2 attendance/schedule metadata. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/range) · [Livestream at 3:00:11](https://www.youtube.com/watch?v=akEqiXFo3GM&t=10811s) · [Individual release](https://www.youtube.com/watch?v=gpmze-6ueGU)

**What the account adds:** A planner can serve one client while an agent drafts another client’s cash-flow or insurance analysis. The agent sends nothing; a planner reviews and adjusts each recommendation before a client sees it. Ragone’s five steps are to pick a repeated, easily judged workflow; teach it through previous cases and reasoning; pack questions, stopping conditions, and limits; test and repair; then ship with both an owner and a separate reviewer. The owner keeps rules and procedures current.

**Numbers and limits:** Ragone reports 24 company skills, 17 in planning, after six months. His suggestion to test 5–10 real cases is a practical starting routine, **not a statistically sufficient release criterion**. No measured accuracy, advisor-capacity improvement, revenue, or client outcome was reported. Owner/reviewer detail can now be attributed to the released transcript, rather than only the agenda.

**Operational lesson:** the reusable asset is the expert’s reasons, exceptions, and maintenance obligation, while professional authority remains explicit.

### 3. Arca — durable service work is event-driven and collaborative

**Title:** Inside Arca’s long-horizon agents that run the business. **Speaker:** Aman Singh. **Event:** October 13. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/arca) · [Livestream at 1:53:23](https://www.youtube.com/watch?v=akEqiXFo3GM&t=6803s) · [Individual release](https://www.youtube.com/watch?v=oP2WLFpMoDY)

**What the account adds:** Singh introduces Arca as a financial-services firm providing financial planning, tax planning, asset management, and investment advice. “Long horizon” means a workflow persists across days, people, client replies, custodial events, approvals, and settlement—not a model reasoning continuously. Agents share client and operational memory, keep plans in a collaborative workspace, register interest in events, and wake on a signal or deadline. People approve plans and client emails and complete required actions. Exceptions and practitioner reasoning become evaluation material.

**Limits:** The Jane tax-payment narrative is a presented example, not an established customer result. Its dollar amounts and the talk’s broad percentage-of-work remark should not become audited throughput or ROI. Proactive goal planning is an illustrated direction, not evidence of unconstrained financial autonomy. Do not conflate this Arca with another firm sharing the name.

**Operational lesson:** persist state and ownership; define which event resumes which task; involve the right person only when their action is ready.

### 4. Perpetual — constrain interpretation, execution, and uncertain side effects separately

**Title:** Building Reliable, yet Smart Workflows for Finance, Wealth and Insurance. **Speaker:** Karthic Rao, CTO. **Event:** October 13, online track. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/perpetual) · [Livestream at 4:23:48](https://www.youtube.com/watch?v=akEqiXFo3GM&t=15828s) · [Individual release](https://www.youtube.com/watch?v=8g0g1ncwzG0)

**What the account adds:** Rao describes Perpetual as a wealth-management roll-up acquiring traditional firms and reports production workflows. LLMs answer bounded interpretation questions; a compiler and state machine determine valid transitions, evidence requirements, and side effects. The illustrated flow turns a typed semantic graph into a validated execution plan, obtains human approval, binds approved email content to its payload, and handles client replies without silently rewriting the approved parent plan. An uncertain dispatch outcome goes to manual review rather than automatic retry.

**Limits:** Firm identity is used as introduced; it was not independently matched to a similarly named incumbent. The reported action counts, compiler stages, follow-up round limit, and waiting period are implementation choices. A 95% local-model goal is architectural ambition, not measured production parity or cost savings. Logging/evaluations are described as present; the training loop is next, not already operating.

**Operational lesson:** make language interpretation provisional, freeze approved plans, and distinguish failed execution from unknown execution to prevent duplicate consequential actions.

### 5. Sid Pednekar — concentrate judgment and preserve organizational learning

**Title:** Everyone Has AI. Who Has the Advantage? **Speaker:** Sid Pednekar, asset-management data/AI executive; employer not named. **Event:** October 13. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/sid-pednekar) · [Livestream at 6:02:04](https://www.youtube.com/watch?v=akEqiXFo3GM&t=21724s)

**What the account adds:** The three pillars are selecting the right problem, building shared capabilities, and compounding advantage. The research example contrasts faster summaries with continuously collecting evidence that supports or refutes an investment thesis. Shared datasets, semantic layers, failed approaches, and known gaps reduce repeated rebuilding. Feedback should preserve evidence and update the system’s reusable knowledge, not remain an individual’s lesson.

**Limits:** Companies A and B are **explicitly hypothetical**. The talk references enterprise studies but the transcript does not establish their underlying methodology; do not reproduce its survey percentages as verified conference findings. This resolves the likely attribution of the earlier notes’ unattributed closing strategy framework, but it does not identify a specific firm’s deployment or measured advantage.

**Operational lesson:** define where scarce professional judgment is worth spending and what the next team member should not need to rediscover.

### 6. Coatue — optimize an evaluated decision graph, not the amount of automation

**Title:** A Hedge Fund as a Function. **Speaker:** Frank Long. **Event:** October 13. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/coatue) · [Livestream at 6:47:46](https://www.youtube.com/watch?v=akEqiXFo3GM&t=24466s)

**What the account adds:** Long models investing as external plus internal context transformed into selection, size, and timing. Internal positions, risk/liquidity constraints, historical decisions, and research matter alongside public data. His Korean-news example decomposes collection, filtering, translation/extraction, cross-checking, and view updates. Each node can use deterministic code, statistics/classical ML, an LLM, a person, or a combination. Data formatting, control flow, model, harness, and skills are evaluated design choices.

**Limits:** This is a practitioner’s framework and illustrative workflow, not evidence of an autonomous fund or superior returns. His claim that agents may matter more in investing than coding is a thesis. The old agenda placeholder “Head of AI & AI Engineer, Coatue” can be replaced with the real recorded title. Nothing here establishes another vendor’s deployment at Coatue merely because its founder previously worked there.

**Operational lesson:** compartmentalize into observable inputs/outputs, assign the appropriate executor, and improve against quality criteria instead of maximizing LLM coverage.

### 7. Kepler — facts and calculations need a constrained path plus checks

**Title:** Why Wall Street Still Doesn’t Trust AI. **Speaker:** Vinoo Ganesh. **Event:** October 14. **Evidence:** official full keynote transcript read. The related individual release has a different title, duration, and chapter sequence; its equivalence to this recording was not established.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/kepler-14) · [Livestream at 5:49:35](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=20975s) · [Related individual release: Do Not Let Models Invent Numbers](https://www.youtube.com/watch?v=dZgA6btnb_s)

**What the account adds:** Ganesh separates the wrong document, wrong fact within a correct document, and arithmetic failure. His disclosed design preprocesses facts into structured storage with identifiers; the model plans while code retrieves facts and computes. Source chips expose how a claim was obtained. Search width, reranking, tenant scoping, direct-read permissions, freshness, and empty-index failure all matter before final verification.

**Critical qualification:** At 6:05:27–6:05:39, Ganesh explicitly acknowledges models can still make numbers up during inference and therefore need post-processing. Do not turn the pointer design into a universal correctness guarantee. A correct lookup cannot establish that preprocessing chose the correct entity, period, unit, definition, or version. The transcript includes production-data language but no independently reviewable rate or evaluation protocol. Approximate retrieval candidate counts are the reported configuration, not prescribed defaults.

**Operational lesson:** check financial meaning, source existence, arithmetic, authorization, and final output separately; missing support must change the output.

### 8. Kepler investing conversation — attention allocation remains the objective

**Title:** AI and the Future of Fundamental Investing. **Speakers:** Jack Woodruff and Vinoo Ganesh. **Event:** October 13. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/kepler-13) · [Livestream at 5:29:04](https://www.youtube.com/watch?v=akEqiXFo3GM&t=19744s)

**What the account adds:** Woodruff identifies himself as Candlestick’s founder/former CIO and a former Surveyor Capital portfolio manager. He argues the source of differentiated fundamental views remains, while routine preparation and analyst roles change. Faster preparation should free time for proprietary investigation and direct attention to promising names; analysts still need to internalize important information.

**Limits:** The five-minute versus six-to-eight-hour preparation comparison is a conversational possibility, not a measured firm-level study. Staffing, coverage, and 2030 scenarios are questions or forecasts. Surveyor’s Citadel history must not be conflated with Citadel Securities’ organizational-memory case. This is expert strategy opinion, not a disclosed Kepler investment outcome.

**Operational lesson:** evaluate where professional attention goes after time is saved, not only whether a summary was produced quickly.

### 9. Blackstone / Norm.ai — preserve data and evaluation assets while implementations change

**Title:** Built to Scale: Future-Proofing Your Technology Roadmap. **Speakers:** John Stecher and Scott Worland. **Event:** October 14. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/blackstone-norm) · [Livestream at 5:22:25](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=19345s)

**What the account adds:** Stecher prioritizes accessible proprietary/public data and straight-through processing, injecting intelligence where useful. Model, harness, and data changes all require repeatable evaluation. Worland reports tens of thousands of expert-labeled examples, originally regression assets for a highly structured regulatory workflow, that let Norm compare newer agentic approaches and reconsider scaffolding. They distinguish rapid proof-of-value creation from production deployment, which still requires enterprise infrastructure, security, traceability, and SRE integration.

**Limits:** Attribute Norm’s benchmark size and architecture change to **Norm**, not Blackstone. Their appearance together does not by itself prove a Blackstone customer deployment of every Norm component. Replacing internal applications or waiting for a better model are context-dependent roadmap decisions, not instructions to discard core security primitives. No quantified causal operating-margin gain is supplied.

**Operational lesson:** own the data, acceptance scorecards, and protected primitives; make implementation choices replaceable and judge them against the same work.

### 10. Apollo / Redding Ridge / Rowspace — reconciliation is a frontline investment enabler

**Title:** AI in Practice: An Inside Look at Apollo’s Approach. **Speakers:** Michael Manapat, Rowspace; Jack McDonald, Apollo principal and COO of Redding Ridge. **Event:** October 14. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/apollo-rowspace) · [Livestream at 7:50:03](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=28203s)

**What the account adds:** The concrete scope is Redding Ridge’s structured-credit/CLO operations. Engineers work beside portfolio and finance teams to resolve fragmented documents, source conflicts, and calculation definitions. McDonald describes preparation of mock credit portfolios, followed by PM refinement, and repeatable warehouse purchase/trade reconciliation reports, followed by daily team QA. The source-of-truth decision can require understanding why one of many feeds is authoritative.

**Numbers and limits:** McDonald reports portfolio preparation moving from two–three days to minutes and a recurring report produced in about a minute. These are customer speaker accounts without a study protocol, failure rate, full review cost, or causal P&L estimate. His 80–90% draft-completion phrase is not accuracy. Do not generalize the examples to all Apollo investment decisions or confuse them with Adam Nahari’s separate operating-margin session.

**Operational lesson:** domain-specific data reconciliation and hands-on workflow discovery can matter more than a general chatbot; retain QA and professional investment judgment.

### 11. Citadel Securities — institutional memory is a time-varying estimate, not a static answer

**Title:** Your Company Has No Model of Itself: Bootstrapping a World Model from Slack, Decks and Meetings. **Speaker:** Joao Wenzel. **Event:** October 14. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/citadel) · [Livestream at 6:38:33](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=23913s)

**What the account adds:** Wenzel reports a system at **Citadel Securities** that updates longitudinal project records from decks, messages, meetings, code, and opted-in agent traces. It distinguishes reported status from evidence, ages claims, observes contradictions, grades against later outcomes, and collects human corrections. Models propose; code and people decide record updates. Historical records are preserved rather than rewritten, supporting time-snapshot evaluation. Missing sensor data must not be treated as a real zero or evidence of inactivity.

**Numbers and limits:** He describes three years of records, more insightful updates after specialist workflows, and higher subsequent warning rates among flagged projects. Counts/ratios are speaker-reported observational results, not a controlled causal test or universal predictive accuracy. Client-franchise expansion and canonical entity resolution remain directions/open problems, not completed capability.

**Operational lesson:** retain claim time, origin, confidence, source health, correction history, and an as-of snapshot; evaluate whether warnings predict later observable changes without future leakage.

### 12. Compound AI — collaborative artifacts require permissions and verification loops

**Title:** Towards Autonomous Analysts in Finance. **Speaker:** Yijia Liang. **Event:** October 14. **Evidence:** official full transcript read.

[Reading edition and transcript](https://ai.engineer/nyc/2026/talks/compound) · [Livestream at 1:59:37](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=7177s)

**What the account adds:** Liang identifies Compound AI as a vendor building long-running buy-side analyst workflows. A shared deal-team thread and agent inbox need participant-level authorization, not only an email connector. Their claimed headless Office-like engines support parallel work and a write–render–check–fix loop. File breadth, workbook depth, source citations, and firm preferences are distinct context problems. Human deal judgment remains the desired focus.

**Limits:** Compound is not LinqAlpha. Liang’s former Coatue employment does not establish that Compound was deployed by Coatue. Full Office parity, speed, token/code counts, and autonomous-delegation prospects are vendor claims without a disclosed independent test here. The example of turning data-room work into investment-committee materials is a product use case/ambition, not measured investment success. General statements dismissing existing libraries should not be treated as independently validated library limitations.

**Operational lesson:** evaluate artifact correctness and visual fidelity alongside reasoning, and carry authorization across every collaborative participant and source.

## Additional individual releases: organizer descriptions read, not transcripts

The first-party descriptions were recovered by the capture agent and read here from `youtube-watch-evidence.json`. They support the bounded paraphrases below. No individual video was watched, and its advertised caption tracks returned no readable text. These recordings expand coverage beyond the 52 reading editions.

### Contour — measure useful research, including the cost of repair

[Proving Alpha: How a Hedge Fund Measures AI’s ROI — Hari Kumar](https://www.youtube.com/watch?v=ZMZlAn6Pyfg). **Published October 24, 2026; 18:24. Evidence: organizer description and chapter list, plus original attendee notes/agenda.**

The description identifies Contour as a fundamental long/short fund and says Kumar compares analyst research with and without AI, measures useful-insight cost, revisits older ideas when market conditions change, and applies the approach beyond research to trading, operations, and compliance. Useful navigation points are **2:25** for the advertised live A/B comparisons, **5:42** for process measurement, **10:04** for time and useful-insight cost, and **16:40** for fixing tools. This adds an economic completion boundary: a generated idea is not valuable merely because it was cheap to create. The description does **not** disclose randomization, control quality, confidence intervals, leakage controls, a causal alpha estimate, or a verified return amount. Preserve the earlier notes’ limited measurement evidence rather than upgrading “A/B” into an established randomized trial.

### Vanguard — the headline research speedup concerns legacy code

[AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder](https://www.youtube.com/watch?v=uA4ah-dVHvU). **Published October 21, 2026; 15:38. Evidence: organizer description/chapter list; original ledger-modernization agenda.**

The described task is **mainframe code research during cash-ledger modernization**, not investment analysis. Yoder exposes the legacy codebase through an MCP server while running data, producer, and consumer migrations in parallel. The description emphasizes making legacy code queryable, treating migration documentation as a product, redesigning rather than simply relocating, adopting AI incrementally, and preserving observability. Key navigation points are **2:32** for code research, **3:20/4:12/6:38** for migration tracks, and **13:12** for the five lessons. The seven-day to fifteen-minute comparison is an organizer-reported speaker claim with no disclosed task sample, end-to-end review boundary, controlled comparison, or net organizational saving. It must not become “Vanguard investment research is 672 times faster” or an accuracy guarantee.

### Monzo — adoption compounds through a shared runtime and familiar entry point

[A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso and Francesco Galletta](https://www.youtube.com/watch?v=adfw3xJBx1o). **Published October 20, 2026; 15:30. Evidence: organizer description/chapter list, corroborating advertised scope in the original agenda.**

The description says Monzo’s agent began as a Slack emoji interaction and grew on pre-existing platform capabilities: an MCP gateway for internal knowledge/tools, sandboxed orchestration, and a reusable agent building block. Examples extend to incidents, on-call data-quality work, and non-engineers requesting changes. The useful mechanism is the combination of distribution and governed platform reuse, not merely selecting a coding model. Navigation: **1:37** Slack adoption, **5:04** gateway, **5:59** sandboxing, **8:37** reusable building block, **10:07** incidents. The reported over-10% merged-PR share and more-than-1,800 daily tasks establish claimed activity, not defect reduction, safe autonomy, net engineering productivity, or causal savings. No transcript was recovered to inspect the qualification of those counts.

### Axim — convergence is a diagnostic, not a correctness label

[Can AI Understand a Distressed Credit? — Harneet Kaur](https://www.youtube.com/watch?v=WOszaC1WWbQ). **Published October 24, 2026; 14:14. Evidence: organizer description/chapter list and original agenda.**

The description reports a distressed-credit case concerning iHeartMedia: models given the same context initially disagree over bankruptcy versus negotiated restructuring. Breaking the analysis into extraction, derivation, judgment, and prediction makes them converge. This supplies a useful layered evaluation structure: check factual extraction and calculation before assessing assumptions and future scenarios. It also explicitly raises whether agreement means correctness. Navigate to **6:13** for the disagreement, **8:01** for layer-specific benchmarking, and **12:03** for convergence versus correctness. The description establishes neither a validated bankruptcy forecast nor an unbiased general benchmark result. Agreement may reflect shared assumptions or common errors. Kaur’s past Morgan Stanley employment is biographical context, not a Morgan Stanley deployment or endorsement.

### Google DeepMind / Kaggle / LinqAlpha — test the entire mandate-to-memo job

[Why Frontier Models Fail as Buy-Side Analysts — Janie Gu and Suyeol Yun](https://www.youtube.com/watch?v=aVbRSIQO2dE). **Published October 25, 2026; 18:31. Evidence: organizer description/chapter list only.**

The description introduces reproducibility and verifier-integrity problems in industry benchmarks, then MandateBench as a buy-side analyst task running from a fund’s mandate to an investment memo. It emphasizes grading reasoning as well as the final answer. Useful navigation is **5:25** for reproduced-benchmark issues, **11:44** for MandateBench, **13:31** for the complete analyst task, and **15:33** for reasoning grades. The transferable method is to preserve task constraints and protect the grader while evaluating intermediate analytical decisions and the completed work product. The description’s benchmark counts and score-variation figures are organizer-reported claims; task set, model settings, score uncertainty, holdouts, and released results were not inspected here. **LinqAlpha is separate from Compound AI**, whose full transcript is summarized above.

### Other verified leads for follow-up

- [Do Not Let Models Invent Numbers — Vinoo Ganesh, Kepler](https://www.youtube.com/watch?v=dZgA6btnb_s), **October 25; 20:58**, organizer description read. Chapters name fact fields (value, unit, scale, period) at **8:27**, tenant isolation at **11:30**, stripping unsupported figures at **14:42**, and guarantee limits at **19:46**. The description mentions a citation registry built from over 30 million SEC documents. These details belong to this individual release; do not silently attach them to the different Oct14 keynote transcript.
- [The Investor’s Edge Lives in Their Head — Anekha Sokhal, Moshi](https://www.youtube.com/watch?v=UHbODjuviAU), **October 20; 16:29**, organizer description read. It argues for separating data preparation from human investment decisions and eliciting the investor’s tacit context. This is a product thesis, not a demonstrated deployment or measured alpha.
- [I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](https://www.youtube.com/watch?v=dYh7TQkuYFE), online-playlist title verified; no transcript/description reviewed in this ledger.
- [What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad](https://www.youtube.com/watch?v=gDRCpTMCqEU), online-playlist title verified; no transcript reviewed here. The quoted percentage in a title is not an established outcome.

## Recorded boundaries and publication metadata

The following bounds come from the official reading-edition catalog; they identify the inspected transcript, not the full conference schedule. Small silence gaps may be excluded. Individual releases can be edited or be a different session; compare titles and chapter sequences before treating them as identical.

| Official reading edition | Event label | Livestream interval |
|---|---|---|
| Vault: Making Unstructured Data Work for Investing | 2026-10-13 | 0:07:22–0:23:43 |
| We Let Our Financial Planners Write the Agents | 2026-10-13 | 3:00:11–3:09:03 |
| Inside Arca’s long-horizon agents that run the business | 2026-10-13 | 1:53:23–2:06:38 |
| Building Reliable, yet Smart Workflows for Finance, Wealth and Insurance | 2026-10-13 | 4:23:48–4:38:59 |
| Everyone Has AI. Who Has the Advantage? | 2026-10-13 | 6:02:04–6:20:02 |
| A Hedge Fund as a Function | 2026-10-13 | 6:47:46–7:01:37 |
| Why Wall Street Still Doesn’t Trust AI | 2026-10-14 | 5:49:35–6:07:40 |
| AI and the Future of Fundamental Investing | 2026-10-13 | 5:29:04–5:35:06 |
| Built to Scale: Future-Proofing Your Technology Roadmap | 2026-10-14 | 5:22:25–5:42:55 |
| AI in Practice: An Inside Look at Apollo's Approach | 2026-10-14 | 7:50:03–8:08:48 |
| Your Company Has No Model of Itself: Bootstrapping a World Model from Slack, Decks and Meetings | 2026-10-14 | 6:38:33–6:57:11 |
| Towards Autonomous Analysts in Finance | 2026-10-14 | 1:59:37–2:15:23 |

Public watch metadata available for related individual releases (source: first-party YouTube embedded watch data recovered October 25):

| Release | publishDate / uploadDate as exposed |
|---|---|
| [How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater](https://www.youtube.com/watch?v=CLve4Nx_RwI) | 2026-10-24T08:00:38-07:00 |
| [Inside Arca's Long-Horizon Agents That Run the Business - Aman Singh, Arca](https://www.youtube.com/watch?v=oP2WLFpMoDY) | 2026-10-23T14:00:21-07:00 |
| [Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management](https://www.youtube.com/watch?v=ZMZlAn6Pyfg) | 2026-10-24T01:00:28-07:00 |
| [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](https://www.youtube.com/watch?v=uA4ah-dVHvU) | 2026-10-21T01:00:37-07:00 |
| [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](https://www.youtube.com/watch?v=adfw3xJBx1o) | 2026-10-20T12:00:34-07:00 |
| [Can AI Understand a Distressed Credit? - Harneet Kaur, Axim Intelligence](https://www.youtube.com/watch?v=WOszaC1WWbQ) | 2026-10-24T02:00:16-07:00 |
| [Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha](https://www.youtube.com/watch?v=aVbRSIQO2dE) | 2026-10-25T00:00:32-07:00 |
| [Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler](https://www.youtube.com/watch?v=dZgA6btnb_s) | 2026-10-25T01:00:12-07:00 |
| [We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](https://www.youtube.com/watch?v=gpmze-6ueGU) | 2026-10-12T05:00:24-07:00 |
| [Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual](https://www.youtube.com/watch?v=8g0g1ncwzG0) | 2026-10-12T10:00:05-07:00 |

The Range and Perpetual individual releases were published October 12, before their October 13 recording-index labels. The label therefore does not establish a live-stage appearance date; recorded content can precede the indexed event day. This is another reason to keep publication, recording-index, scheduled, and attended dates separate.

## Named-bank coverage and identity controls

- **Morgan Stanley / UBS / RBC:** no matching firm entry appears in the fetched 52-talk index, expanded 90-release individual catalog, or 20-item online catalog inspected here. This is a bounded coverage finding, not proof no video exists elsewhere. The earlier deck’s Morgan Stanley Debrief, UBS Red, and RBC Advisor Assist examples came from dated **external company disclosures**, not NYC conference talks. Keep that evidence class and date visible. Axim founder Harneet Kaur’s prior Morgan Stanley role does not transform her startup talk into a bank deployment.
- **NatWest / Comet / Cora:** no NatWest or Jonathan Osborne match appears in these fetched recording catalogs. The notes and October 10 program say Comet, while October 14 schedule says NatWest. This research does not resolve that discrepancy and does not assign the Cora example to a bank.
- **Citadel versus Citadel Securities:** Wenzel’s case is Citadel Securities, regardless of the short URL slug `citadel`. Ganesh’s previous role and Woodruff’s Surveyor history refer to Citadel and do not make their current Kepler session a present Citadel deployment.
- **Historical and future statements:** keep operating reports, product demonstrations, architectural designs, hypothetical companies, and future aims distinct. A polished reading edition is an organizer’s explanatory rendering; a transcript identifies what a speaker actually said, not independent validation of the underlying deployment or result.
