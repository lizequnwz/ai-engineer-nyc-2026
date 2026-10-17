# Wednesday research — AI Engineer NYC 2026

Verified October 10, 2026 from the official detailed agenda: https://ai.engineer/nyc/2026/schedule and the official event page: https://ai.engineer/nyc/2026. The parent extracted official session data including abstracts and speaker biographies into `work/program.json`. Each session's direct source is `https://ai.engineer/nyc/2026/schedule?session=SESSION_ID`.

The agenda states New York/ET times, Sessionboard refresh on Oct 10, and that times, rooms, and speaker assignments may change. The detailed session agenda is more current and precise than the marketing page's broad block structure; use the detailed agenda for attendance times.

`work/wednesday_rankings.json` contains 11 concurrent slots × 3 ranked choices with role-specific reasons, a capture question, tradeoff, and theme. Those rankings and proposed Fidelity applications are analysis, not organizer claims or statements about Fidelity's actual architecture.

## Recommended primary path

| Time ET | First choice | Why this advances the approved brief |
|---|---|---|
| 10:40–10:58 | Towards Autonomous Analysts in Finance | Multi-person finance workflow, Office outputs, firm memory and context at scale |
| 11:05–11:23 | We gave our finance agent more context. It got worse. | Production ablations, context/memory choices, quality/cost/reliability loop |
| 11:30–11:48 | Your Reranker Improved Retrieval. Did It Improve the Answer? | Direct test of retrieval improvements against end-to-end answer quality |
| 11:55–12:13 | When AI Fails: Designing Evaluation Systems for High Stakes Applications | Severity-weighted failures, red teaming and human review |
| 12:20–12:38 | A/B Testing AI Products Is Weird | Offline scores to business/user outcomes; experimentation discipline |
| 12:38–13:30 | Protected lunch + 10-minute synthesis + one targeted conversation | Do not sacrifice all the break to vendor demos |
| 13:40–13:58 | Artificial Analysis — Optimizing the Cost of Intelligence | Model selection with own benchmark and successful-task economics |
| 14:05–14:23 | Stop turning your Humans Into APIs for your Agents | Wise's separation of reasoning and authority; versioned preventive policies |
| 14:30–14:48 | Your Agent Wants Your Data: Securing MCP Database Access from the Ground Up | End-user identity, least privilege, data-tier enforcement and vectors |
| 14:55–15:13 | Building Deployment Gates for AI Agents in Financial Services | Golden cases, domain evaluators, release thresholds, reviewable evidence |
| 15:20–15:38 | Building an Evidence Layer for Financial Agents | Specialized retrieval, source/version checks, compact evidence for reasoning |
| 15:45–16:03 | Code Mode: your agent should write code | Compare sandbox composition with tool-calling on workflow tasks |
| 16:03–16:20 | Expo closeout + follow-up scheduling | Expo closes at 16:30; keynotes resume at 16:25 |
| 16:25–17:30 | Featured keynotes + close | Especially 16:48 process supervision |

All first-choice recommendations avoid the agenda's Leadership Track label. The user did not disclose ticket type; recommendation of a Leadership Track alternative must be conditional on access. The official page says workshops are add-ons, but workshops are Monday Oct 12; none are scheduled Tuesday/Wednesday. Do not imply an 18-minute Wednesday talk is a hands-on workshop even when its imported abstract uses that word.

## Morning plenaries: attend full block, prioritize these captures

All morning plenaries are in **Simons Room (Metropolitan East)**. Welcome remarks 08:55–09:00; arrive/check badge earlier.

1. **09:00–09:18, Chasing capabilities while waiting for the frontier — Alexander Shevchenko, Ramp.** Official abstract: Ramp Labs closes current finance capability gaps by rapidly replicating research while expecting future model improvements. Inference for Fidelity: decide which assistant gaps merit building now and which may be commoditized by frontier progress. Capture a build/hold criterion. Direct source: https://ai.engineer/nyc/2026/schedule?session=caecd5f6-b352-4868-a995-f0f71679caf0
2. **09:18–09:36, The Machine that Changed the World, vAI — Tariq Shaukat, Sonar.** Abstract describes agentic, CI-verification, and production-maintenance loops. Inference: reusable engineering controls for AI-assisted delivery of your own systems; capture how each loop catches a different defect class. Source: https://ai.engineer/nyc/2026/schedule?session=4add802c-6a68-4e9c-93fb-9c1e017193bc
3. **09:36–09:54, Trusting Agents in Policy-Driven Workflows — Evan Kormos, Coinbase. HIGH PRIORITY.** Abstract covers auditable process graphs, bounded agent loops, human control, and measured quality guiding autonomy. Inference: particularly useful for designing the authority map of a Fidelity workflow assistant. Capture boundary decisions, accountability, and thresholds for autonomy. Source: https://ai.engineer/nyc/2026/schedule?session=ee927042-2ba1-44c3-b304-d001ae247839
4. **09:54–10:12, Building the Next Chapter of AI in Finance — Joseph Kim, OpenAI.** Abstract discusses ChatGPT for Financial Services product/research direction. Inference: strategic market context for build/buy conversations; do not treat product direction as procurement-ready evidence. Capture capabilities, constraints, and specific unanswered enterprise requirements. Source: https://ai.engineer/nyc/2026/schedule?session=02f94835-c29d-4cf5-b77a-c5a491b747b8
5. **10:12–10:30, Security in the Age of AI: Recent Attacks, Incidents & Defenses — Andrey Rybka, Bloomberg. HIGH PRIORITY.** Abstract includes incidents, prompt injection, leakage, agentic threats and supply-chain risk. Inference: inputs to an assistant threat model and tests. Capture one concrete attack path, where the defense acts, and what residual failure remains. Source: https://ai.engineer/nyc/2026/schedule?session=01982251-7fdc-4828-8520-fb34b9bc7564

## Evening plenaries

All in **Simons Room (Metropolitan East)**. Welcome back 16:25–16:30; closing remarks 17:25–17:30.

1. **16:30–16:48, AI in Practice: An Inside Look at Apollo's Approach — Michael Manapat, Rowspace; Jack McDonald, Apollo Global Management.** Only a sparse abstract identifying a Rowspace customer co-presentation is available. Attend for institutional perspective, but do not promise detailed architecture or measured results in the report. Capture the use case, baseline, evidence, operating model and conditions behind any claimed benefit. Source: https://ai.engineer/nyc/2026/schedule?session=44e9d04a-e8b4-418c-8a85-02fbb9263dd0
2. **16:48–17:06, Process Supervision for Agents That Do Long-Horizon Work — Mitchell Troyanovsky, Basis. VERY HIGH PRIORITY.** Abstract explicitly distinguishes final-answer correctness from dependable intermediate research decisions, then introduces behavior specs and trajectory judging. This closely matches the internal-research assistant requirement. Capture a minimal behavior spec, how a judge detects applicability, and how evidence links behavior failures to prompt/tool/runtime changes. Ask how judge validation, critical behaviors and spec growth are controlled. Source: https://ai.engineer/nyc/2026/schedule?session=1cbc625f-7f07-49bb-9c5c-57c95f07ba77
3. **17:06–17:24, Everything will be Simulated — Cristóbal Valenzuela, Runway.** Abstract is about physical-world models, motion, robotics and simulation. Interesting horizon-scanning, lower direct fit than evaluation/retrieval/security. Attend if energy permits; use for one bounded horizon insight rather than a near-term Fidelity recommendation. Source: https://ai.engineer/nyc/2026/schedule?session=af8422e8-d5f8-4dbd-a918-6360f5bfba80

## Overlooked conflicts and caveats

- Lunch is listed as 12:00–14:00 and networking 12:15–14:05, overlapping 12:20 and 13:40 talks. They are concurrent opportunities, not uninterrupted breaks. Protect a real break between the short sessions.
- All breakout choices reviewed at the 11 ranked Wednesday start times end 18 minutes later, leaving 7 minutes to switch rooms, but physical walking time/room capacity is unverified. Arrive at the first-choice room early where feasible; use a top-three backup if full.
- The imported AlixPartners abstract calls its session a workshop; timed agenda says 11:05–11:23 Wednesday, a breakout. The timed agenda controls attendance planning.
- The 13:40 'Evals in 5 minutes' session is an intro/vendor booth description in an 18-minute slot; lower marginal value for a Principal Data Scientist than cost/custom benchmark discussion.
- At 14:05 Blackstone/Norm.ai has no abstract; brand/company relevance alone is insufficient to rank it ahead of clear technical fits.
- At 15:20 four strong sessions collide. Evidence Layer wins direct role fit; subjective-evaluation methodology and Citadel's enterprise-state model are close alternatives. Graph Engineering remains a good reserve for governed, portable memory/context.
- The Wednesday official Speaker VIP Happy Hour is 17:30–19:30 at Dear Irving on Broadway, https://luma.com/6dobkzfh?utm_source=aie . Treat as invitation/RSVP-dependent, not an assured general-attendee event.
- The main site also lists a Langfuse community 5km run 07:30–09:00, meeting at the venue; it overlaps the 08:55 welcome and has low priority if it would compromise the morning plenaries. https://ai.engineer/nyc/2026#side-events
- Promotional abstracts contain numerical claims and broad model-performance assertions. Attribute these as speaker claims until the talk provides methods, baselines, uncertainty, and transfer conditions. Avoid turning advertised outcomes into verified conference learnings before attendance.

## High-value Wednesday report-back experiments (proposals, not Fidelity facts)

1. **Context ablation:** compare a minimal assistant, added retrieved context, process-only memory, and broader memory on a fixed approved task set; measure answer support, critical errors, reviewer effort, latency and cost.
2. **Evidence-layer A/B:** baseline retrieval versus retrieval+reranker versus specialist evidence retrieval, keeping the generator and tasks constant; score final answers, source/version fidelity and coverage.
3. **Deployment evidence:** build a minimal release record with golden cases, domain rubric, calibrated judge, critical-failure checks, traces and rollback criteria.
4. **Authority map:** enumerate proposed tools/actions, user entitlements, policy enforcement points, approval requirements, and fail-closed behavior.
5. **Process supervision:** choose a small set of mandatory research behaviors, such as checking a primary filing before reporting a number; evaluate trajectories in addition to outcomes.
