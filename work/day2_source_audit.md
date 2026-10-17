# Day 2 supplied-notes source audit

Reviewed the new attachment `a45dfe6d-9d15-4ffb-b6b5-b8152ec8f7bc/Pasted text.txt`, specifically the content after `----Day2`, against the saved official program in `work/program.json`. No browsing or external identity matching was used. This is an audit of supplied notes and saved metadata, not independent verification of speaker claims.

## Scope and source reconciliation

The attachment repeats the existing Day 1 notes before the marker. Treat that content as repeated input, not additional attendance, independent corroboration, or new Day 2 learning. Existing Day 1 caveats still apply.

After the marker there are **five note blocks: four identified sessions and one unattributed RIA/financial-planner example**. The four session IDs resolve to the expected saved official records:

| Supplied block | Saved official identity | Saved time and room | Audit result |
|---|---|---|---|
| The Machine that Changed the World, vAI | Tariq Shaukat, CEO, Sonar; `4add802c-6a68-4e9c-93fb-9c1e017193bc` | Oct 14, 9:18–9:36 AM EDT; Simons | Recorded title, name, company, time, and room match. |
| Building the Next Chapter of AI in Finance | Joseph Kim, Head of ChatGPT for Financial Services, OpenAI; `02f94835-c29d-4cf5-b77a-c5a491b747b8` | Oct 14, 9:54–10:12 AM EDT; Simons | Recorded metadata matches. |
| Building Better Agents Through End-to-End Evals | Saved title: **We gave our finance agent more context. It got worse.**; Ryan Stevens, Director of Applied Science, Ramp; `4607dbbe-8f94-4b0e-91ce-257d1cfb5448` | Oct 14, 11:05–11:23 AM EDT; Shannon | URL establishes the source identity in the saved program. Preserve the supplied heading as the recorded heading; do not imply it was necessarily wrong or that the talk could not have been retitled on site. Label the other name “title in saved official program.” Speaker/time/room are program context, not newly captured in this freeform block. |
| RIA is building agent by business | No speaker, named institution, session ID, time, or source link supplied | Unknown | Keep explicitly unattributed. Do not match to an agenda session or infer a wealth manager from adjacent content. |
| From Agent Prototype to Production in Regulated Banking | Jonathan Osborne, Comet; `e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa` | Oct 14, 2:05–2:23 PM EDT; McCarthy | Recorded metadata matches. Official speaker role is blank; do not add a job title. |

**Official schedule facts and notes are different evidence sources.** Adding a missing time, role, or official abstract can improve metadata, but must not make unrecorded technical details appear to have been observed during the talk. The saved snapshot does not independently establish the exact live title or room if a last-minute change occurred.

## Sonar: conceptual assurance model, not a calibrated formula

The note records:

`Code confidence = Intent × guardrails × verification × evidence`

The parentheses define useful categories: stated goals/standards; guidance and governance; independent/thorough verification; auditable/repeatable evidence. Treat this as **the speaker's conceptual assurance framework, as recorded**, not a numerical confidence model, probability, risk score, or demonstrated predictor of defects.

- No numeric scales, units, functional relationships, calibration, weights, or validation are supplied. A product of unlike categories cannot be used to compute a meaningful confidence percentage without additional definitions and evidence.
- Do not infer statistical independence, an experimentally validated interaction, or a mathematical guarantee that satisfying the four labels yields safe software. An illustrative multiplication sign does not establish a formal theorem.
- **“More than 50k lines of code, accuracy collapsed”** is an as-recorded claim with no model, repository, task distribution, evaluation rubric, baseline, sample size, context/tool configuration, or observed values. It must not become a universal 50,000-line boundary or a sizing rule for all coding agents. Safe synthesis: “The speaker warned about difficulty on large, complex codebases; the notes record a 50k-line example whose setup was not captured.”
- **“Cognitive surrender” / humans tend to agree with AI more** lacks a study citation, comparator, population, or measurement. Report as a caution about over-reliance, not an established effect size or proof that human oversight never works.
- **“Human in the loop does not scale”** is a speaker's operational argument, not proof that human review is unnecessary or universally infeasible. Distinguish repeated low-value approvals from expert judgment and independent verification.
- **Compounding errors** and **inconsistent LLM judges** are qualitative failure mechanisms here. No stepwise probabilities, repeatability rate, run count, or measured end-to-end reliability were captured. Do not add an independence-based compounded-success calculation.
- **“Prevention comes first”** is a design recommendation. It does not establish that detection, maintenance, incident response, or humans are obsolete.
- The official abstract separately describes agentic, CI-verification, and maintenance loops. If included, attribute those to **program context**; they were not explicitly captured in the supplied technical notes.
- Maturity is explicitly **Unclear** and evidence **Speaker claim**. Do not infer a named customer production rollout or measured Sonar outcome from this keynote.

## OpenAI: product presentation, with unresolved provider and availability details

The notes describe a financial-services product direction using financial data, finance-oriented interfaces, source passages/tables/charts, firm formats, artifacts, and citations. The official abstract confirms a product/direction keynote but does not independently enumerate these integrations or their availability.

- Keep the provider string **“crunchable”** unresolved/as recorded, or omit it pending materials. Do not silently replace it with a guessed company or product name.
- “Bulletin premium data” and “firms format” are ambiguous. Do not convert them into a specific data feed, entitlement model, brand-compliance feature, output template guarantee, or established deployment.
- The notes list LSEG, OpenAI/SEC filings, Fiscal.ai, FMP, and Quartr. Treat these as **names recorded during the presentation**, not independent confirmation of a signed partnership, customer entitlement, complete coverage, deployment availability, premium-data redistribution rights, or data provenance guarantees. Do not expand abbreviations into an unrecorded specific service.
- **“OpenAI (SEC filings)”** does not establish that OpenAI is the original publisher of SEC filings, nor does it clarify connector ownership or source-update mechanics. Preserve the recorded association without inventing the integration architecture.
- “Source citations (MCP Apps” has an unfinished parenthesis and does not fully specify the mechanism. Do not claim that a UI citation guarantees correct entailment, numerical accuracy, licensing, or source freshness.
- Artifact generation and interactive charts are reported capabilities, not proof that all financial calculations are correct or that output is ready for regulated/client use.
- No available-now versus roadmap distinction, ticket/license/tier, rollout region, enterprise permission model, deployment constraints, performance, or customer results were captured. Keep **maturity unclear** and product details **speaker-reported**. If the report merely synthesizes notes, it should not add present-day product claims without a separate verification step.

## Ramp: benchmark choices and ablations, not production-reliability guarantees

The supplied notes describe mapping a job to tasks and success criteria, partial-credit accuracy, `pass@k`, skill ablation (eight skills to a four-skill bundle), trajectory-distilled memory, and Excel-skill reduction.

- **`pass@k` must be explained carefully.** In its usual benchmark sense, it concerns whether at least one of k attempts succeeds under a defined acceptance criterion. It is not the probability that one production run succeeds, nor proof that a user can recognize the successful candidate, nor the reliability of a deployed retry/selection system. The notes do not record k, number of sampled attempts, estimator, independence assumptions, selection mechanism, budget, time, or failure consequences.
- Do not infer an implementation or estimator from the shorthand alone. **Partial credit** is a separate scoring choice; the note does not define how partial credit was combined with pass/fail acceptance or `pass@k`. Keep them as two recorded evaluation ideas, with the missing rubric open.
- A repeated-attempt metric can improve simply because more attempts are allowed. A fair comparison needs the same attempt, compute, tool, cost, and time budgets and a defined method for accepting a candidate. No result magnitude or uncertainty was captured.
- **Eight skills → four-skill bundle** is a reported experiment, not a recommendation to use exactly four skills, and not evidence that a 50% count reduction necessarily improved every task. Skill size, content, task distribution, comparator, and quality/latency/cost deltas are missing.
- **Trajectory-distilled memory** is a named technique in the notes, not a complete reproducible method. No source trajectories, distillation objective, privacy/filtering, holdout separation, write/retention policy, or stale-memory results were captured.
- **Excel skill shrinkage** has no size or measured delta in these Day 2 notes. The official abstract separately reports shrinking a frequently loaded skill from 14k to 5k characters without sacrificing quality. Do not automatically equate that skill with the Excel skill or present the abstract's numbers as attendee-captured details. If included, explicitly identify program context.
- The saved abstract explicitly discusses a **production accounting agent** and end-to-end benchmarking. This supports **speaker-reported production context**, but does not establish that every intervention in the notes was shipped, the improvement was independently reproduced, or all production workloads benefited.
- Suitable synthesis: evaluate the whole task/harness and use ablations to discover harmful context. Unsuitable conclusion: fewer skills, distilled memory, or higher pass@k universally makes an agent reliable.

## Unattributed RIA example: preserve human-reviewed workflow and unknown provenance

The block describes a planner handling one client call while an agent drafts cash-flow or insurance analysis for another, followed by human review/editing. It proposes selecting a frequent judgeable workflow, teaching why, packaging required questions/limits, testing, and shipping.

- Identity, firm size, speaker, conference session, relationship to another block, product, and deployment maturity are unknown. Do not infer the RIA's name or attach it to Ramp, OpenAI, Comet, or a known wealth-management institution.
- The supplied wording suggests an example or described practice, but gives no rollout count, client count, control evidence, performance results, cost, or business impact. Do not label it proven production, a firm-wide transformation, or representative of the wealth-management industry.
- Human **review, editing, and adjustment** are explicit; do not convert it into autonomous financial advice, autonomous recommendations, suitability determination, or agent action on client accounts.
- Standardized processes and knowledge of client data are reported design ideas, not evidence of lawful/appropriate access, valid analysis, compliant recommendations, or reliable safeguards.
- The five steps are an **as-recorded practice sequence**, not a validated industry standard or a guarantee that a skill is ready for deployment.
- No time-saving, capacity, AUM, revenue, accuracy, or ROI figure is supplied. Parallel drafting is a possible workflow mechanism, not a quantified productivity result.
- This remains a useful but explicitly **unattributed, human-reviewed financial-planning illustration**. Do not count it as an additional named institution in the report.

## Comet / Cora: multidimensional evaluation and unknown customer identity

The notes record quality as a vector, safety/task/experience dimensions, a stricter judge, a configurable judge, and a contextual filtering/classification/rephrasing/intent pipeline. They also record “Cora” at “100K conversations a day.”

- **Do not identify the bank behind Cora.** Neither the supplied notes nor the saved abstract identifies it. Familiarity with an assistant name is insufficient evidence, and Comet is the listed presenter company, not established as the bank or owner of the assistant.
- **100K conversations/day** is a speaker-reported scale claim, not a measured fact independently checked here. No observation period, definition of conversation, channel mix, unique-user count, task completion, escalation, or error rate is supplied. Do not convert it to customers, successful interactions, revenue, or annualized volume.
- **“Safety: roundedness”** is ambiguous/as recorded. Do not silently change it to groundedness, robustness, or another metric. State “one safety term was unclear in the notes” or omit the term pending slides; bias is separately recorded.
- “Quality is a vector” is a useful multidimensional framing, not evidence of an actual numeric vector, weights, complete metric set, aggregate formula, or validated scoring model.
- **Stricter fail/pass judging** needs a calibrated rubric and sensitivity/specificity tradeoff. A preference for failing uncertain outputs does not by itself validate a judge or guarantee safety; it can raise false alarms and review burden. No thresholds, agreement rates, calibration examples, or outcome measurements were captured.
- **Judge as configuration** supports versioning/control as a design idea. It does not establish which configuration fields were used, whether changes were governed, or whether judge drift was controlled in production.
- The routing steps are notes of components and an approximate order, not a complete architecture. Do not invent models, exact branching logic, authority boundaries, storage, retry behavior, or customer data movement.
- The prefilled question asks about approval evidence, judge validation, rollback, and renewed review, but no specific answer was captured. Do not present these mechanisms as observed simply because the official abstract mentions continuous scoring, gates, observability, and staged rollout.
- Maturity in the note remains **Unclear**. Cora's reported scale may indicate an operating service, but it does not establish production use or scope of every described Comet evaluator/routing component. Safe wording: “Osborne described a high-volume assistant case; institution, detailed deployment scope, and effectiveness measures were not captured.”

## Cross-cutting report guidance

1. Describe **four identified Day 2 sessions plus one unattributed example**; do not present five fully sourced, named institutional cases.
2. Maintain distinct labels for **attendee note**, **speaker-reported claim**, **saved program context**, and **editorial takeaway**. No new block contains a checked public artifact or independently reproduced result.
3. Quantitative settings and scale claims—50k LOC, eight → four skills, pass@k, 100K/day—must retain their source limits. Do not turn them into universal thresholds, causal effects, or ROI.
4. No Day 2 material supplies a controlled business-benefit result, a deployed failure-rate estimate, or a validated statistical confidence level. Do not manufacture these from the recorded formula, usage scale, or benchmark shorthand.
5. Empty evidence/failure/follow-up sections and unanswered prefilled questions should remain visible gaps; absence of captured detail is not absence of a control or proof of a control.
6. No slides, transcript, benchmark dataset, repository, provider-integration document, or customer-verifiable study accompanies the notes. Exact quotations, ambiguous spellings, and unrecorded implementation details remain unverified.

## Addendum: user confirmation and refreshed official metadata, October 14

This addendum supersedes the earlier **identity/title uncertainty only** where stated. It does not turn notes into independently validated outcomes. Sources: direct user confirmation supplied to the parent agent and refreshed official raw schedule saved in `work/schedule-2026-10-14-data.json` (`props.pageProps.sessions`). The earlier audit used the October 10 snapshot.

- **RIA is now identified as Range.** The user confirmed the company. The refreshed official schedule lists Matt Ragone, Financial Planner, Range, “We Let Our Financial Planners Write the Agents,” October 14, 11:30–11:48 AM, Turing, session `9b002687-09cf-42e2-9282-532ed9d0c184`. Its abstract directly matches the notes' parallel client-work drafting and skill-building sequence. It explicitly says planners write/maintain skills used daily, with an owner, reviewer, and peer review. Therefore the case can now be attributed to Range, with **speaker-reported daily operational use**; no measured correctness, time saving, ROI, or autonomous advice result is established. The abstract reports six months, 24 skills (17 in planning), and tests on five to ten real cases—these are **fresh agenda claims**, not numbers captured in the attendee's notes. None is a universal rollout/testing prescription.
- **Source-ID reuse: treat metadata as versioned.** In the October 10 snapshot, `9b002687-09cf-42e2-9282-532ed9d0c184` referred to NVIDIA's reranker session; in the October 14 official snapshot it refers to Range. A UUID alone is therefore not a stable identity across these snapshots. Do not attach NVIDIA's old title, speaker, company, abstract, or the old recommendation to Range's new content. Preserve snapshot date and the title/company alongside each cited ID. The live session link may now resolve to the replaced record.
- **Ramp title discrepancy resolved in the fresh official record.** Session `4607dbbe-8f94-4b0e-91ce-257d1cfb5448` is now officially titled “Building Better Agents Through End-to-End Evals,” matching the notes. Ryan Stevens/Ramp, October 14, 11:05–11:23 AM, Shannon, are unchanged. Keep the old “more context” title only as a historical snapshot title if necessary. The technical and metric caveats in the original audit still apply.
- **Comet / NatWest company discrepancy must be preserved.** The refreshed official record for `e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa` lists Jonathan Osborne's company as **NatWest**; the supplied notes and October 10 record list **Comet**. The talk title, date/time, room, and abstract remain the same. A source-transparent label is “Jonathan Osborne — Comet in attendee notes / October 10 program; NatWest in October 14 official program.” Do not silently choose one affiliation or rewrite the note as having recorded NatWest. The refreshed affiliation **does not explicitly identify the institution behind Cora in the abstract**, so do not infer Cora's bank from name recognition or speaker company. Its volume, routing, maturity, and judge-calibration caveats remain unchanged.
