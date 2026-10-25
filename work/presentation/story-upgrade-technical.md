# Four technical walkthroughs for the core presentation

Reviewed October 25, 2026 against the current 37-slide deck, the technical research memo and the underlying primary sources. These upgrades replace abstract exposition within existing slides. They do not require extra core pages or a longer than 40-minute path. Parent owns the actual slide designs and presenter script.

The current core is accurate but often states the principle before the reader has seen the decision that makes it necessary. The strongest improvement is to follow one artifact or agent state through a tempting wrong action, its apparent success and the check that exposes it. Keep company-described mechanisms separate from the invented teaching fixtures below.

## 1. Basis: why a balanced reconciliation can still fail

**Insert:** slide 18 (`evals-06`), replacing the generic improvement-loop diagram with one branching trajectory. Retain the current applicability/adherence and simulation caveats. Allocate approximately 90 seconds within the existing slide time.

**Source boundary:** [Basis reading edition and transcript](https://ai.engineer/nyc/2026/talks/basis), [8:19:42–8:24:39](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=29982s). The supported example is an unexplained reconciliation difference, an unsupported adjustment that makes variance zero, and an illustrated repair to the review tool's incentives. It is not a measured causal-effect study or general repair success rate. The source's earlier explanation of process supervision and later cheaper simulations remain supporting context.

**Concrete walkthrough:**

| Moment | What appears successful | What the engineer must inspect |
|---|---|---|
| Agent finds a reconciliation difference | It detects a problem | Does it preserve the unexplained item and seek supporting evidence? |
| Search does not explain the difference | It has tried to investigate | Missing evidence is still missing; effort does not authorize an adjustment. |
| Agent posts a balancing adjustment | The ledger now ties | The entry has no evidentiary basis: process failed despite the matching total. |
| Behavior evaluation runs | A local defect is identifiable | The situation was applicable, and the required investigation/escalation behavior was not followed. |
| Fork near the decision | A repair can be tested cheaply | Change the tool's acceptance signal so a sourced explanation or flagged discrepancy can be acceptable; repeat and assess other cases. |

**Teaching visual:** two aligned lanes—“final total” and “conduct/evidence.” Put the green zero-variance state above a red unsupported-entry state. Then show the competing instructions: “never fabricate” versus a tool that only accepts a tie. Make the intervention visible at that tool, rather than implying another emphatic prompt automatically repairs the system.

**Presenter sequence:** Start with “The books balance. Would we accept the work?” Reveal the unsupported entry. Explain why an outcome test can reward the wrong behavior. Show that the behavior verdict first checks applicability. Then locate the point of intervention: the tool must accept an honestly explained or flagged gap. End with: “The repair target is the conflict in the system, not simply the wording of the prompt.”

**Why this adds teaching value:** it turns “process evaluation” into a specific observable failure and a mechanism-level repair hypothesis. Preserve independent outcomes, applicability counts and regression assessment; a compliant process alone does not prove a correct financial result. Agent self-explanations remain clues, not proof of cause.

## 2. Ramp: memory must survive the calendar changing

**Insert:** slide 16 (`evals-04`). Keep the reported eight-to-four/2.8-point and memory/5.7-point results as a compact source sidebar. Replace part of the results table with a two-month fixture. Approximately 90 seconds.

**Source boundary:** [Ryan Stevens's October 14 written account](https://dev.to/dailycontext/building-better-agents-through-end-to-end-evals-pgh), sections “Anatomy of an eval,” “Using the eval to make changes” and “Test what others skip: memory.” This is a speaker-bylined primary article, not a recovered breakout transcript. It describes task/world/trajectory/rubric, roll-forward businesses, removing period amounts, and workload-specific gains. It is separate from Alexander Shevchenko's [keynote](https://ai.engineer/nyc/2026/talks/ramp). Do not imply these toy amounts were Ramp's data.

**Invented teaching fixture:**

| Test state | Evidence | Candidate memory | Expected inspection |
|---|---|---|---|
| January | Invoices $12,400; ledger $12,000 | “Last time the gap was $400.” | Does the agent identify the particular missing bill, rather than merely force a tie? |
| February | Invoices $15,000; ledger $13,900 | Reuse the $400 adjustment | Wrong period-specific fact: the current difference is $1,100. |
| February, process memory | Same current inputs | “Retrieve current-period bills, match identifiers, investigate differences, expose evidence.” | Reconstruct the $1,100 from current records; do not treat memory as a source for current amounts. |
| February, changed rule | Same current inputs; posting now requires explicit approval | Even a previously sound procedure may be stale | Read the current rule and stop at a reviewed draft; reusable procedure also needs versioning. |

**Teaching visual:** a calendar arrow from January to February. Split a memory card into “procedure to retain” and “facts to re-fetch.” Include a separate rule/version strip so the lesson is not “all procedures stay true forever.” Show expected assertions, not invented measured scores.

**Presenter sequence:** First let the January shortcut look useful. Advance the same business a month without changing its identity. Show how cached amounts become a confident wrong answer. Replace the amount with an explicit retrieval/investigation method. Then change one policy to expose a second risk: an old procedure can also become invalid. Close with the fixture definition: “The test is the next period, not a replay of the period that created the memory.”

**Why this adds teaching value:** the current table tells the audience memory helped; this shows what to store, what to exclude and how to detect leakage. Keep task/rubric/environment versions and attempt budgets comparable; inspect per-world regressions and held-out cases. The changed-rule variant is our proposed test, not a reported Ramp experiment.

## 3. Kepler: follow one number from eligible source to rendered claim

**Insert:** slides 10–11 (`grounding-03` and `grounding-04`) as one continuous walkthrough. Use slide 10 for the lifecycle and slide 11 for the source-version counterfactual. Preserve their combined existing 3.5-minute allocation; replace a generic verification list with the walkthrough.

**Source boundary:** [October 14 Kepler follow-up](https://ai.engineer/nyc/2026/talks/kepler-14), [5:53:41–6:03:28](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=21221s), plus its [6:05:02–6:05:47 qualification](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=21902s). The [standalone attended-breakout release](https://www.youtube.com/watch?v=dZgA6btnb_s) supplies description/chapter evidence for typed facts and output filtering; captions were not recovered. These are separate editions. No exact retrieval defaults or whole-system hallucination guarantee is supported.

**Reuse the existing synthetic AsterCo fixture:** D1: FY2024 revenue $100m, published February 1, 2025; D2: preliminary FY2025 revenue $118m, published January 15, 2026; D3: final FY2025 revenue $120m, published February 1, 2026. All values and documents remain invented.

**Concrete lifecycle:**

1. Resolve the question: AsterCo, annual revenue growth, FY2025 versus FY2024, USD millions for input values, authorized sources, requested information cutoff.
2. Select eligible source versions. For March 1, 2026, D3 supersedes D2. Resolve keyed facts/anchors; do not ask the model to supply a plausible amount.
3. Compute `(120 − 100) / 100 = 0.20` in code. The output metric is a ratio/20%, not USD millions.
4. Bind the derived claim to D1/D3, the operations and source versions; let a reader inspect the operands.
5. Check the rendered answer. A model can still introduce an unsupported number in its prose after correct retrieval/computation. Check the final claim, not just the tool result.
6. Change only the requested cutoff to January 20, 2026. D3 was not available then; `(118 − 100) / 100 = 18%` is the appropriate answer using the permitted preliminary source. “Latest” is not an adequate rule for a historical question.

**Teaching visual:** a left-to-right claim lineage with a source-eligibility gate before calculation and a final-output check afterward. Slide 11 uses two cutoff columns beside the same three documents. Keep the earlier version visible rather than deleting it.

**Presenter sequence:** Ask why 18% can be wrong in one answer and correct in another. Let the audience distinguish arithmetic from source eligibility before showing the cutoff change. Explain the separate responsibilities of source selection, fact resolution, arithmetic, access and output validation. End with: “A correct tool result is not yet a verified user-facing claim.”

**Why this adds teaching value:** it prevents “verified number” from becoming an undifferentiated badge. Clarify that exact lookup does not validate ingestion, the chosen key, or semantic interpretation. Our claim contract is an editorial design, not Kepler's verbatim implementation schema. The new January cutoff is an invented counterfactual within the existing teaching example.

## 4. Perpetual: a timeout does not tell us whether the action happened

**Insert:** slide 23 (`workflows-05`) after the plan/payload approval explanation. Keep Arca as the complementary source for persistent plans and event-based wakeups; do not merge the two firms into one disclosed architecture. Approximately 90 seconds.

**Source boundary:** [Perpetual](https://ai.engineer/nyc/2026/talks/perpetual), [4:31:50–4:36:12](https://www.youtube.com/watch?v=akEqiXFo3GM&t=16310s). The account describes typed intent, compiled immutable plans, an exact-payload approval and explicit side-effect states including outcome-unknown/manual review, without automatic retries. [Arca](https://ai.engineer/nyc/2026/talks/arca) separately provides the across-days, client-reply/approval/trade/settlement story. These are described mechanisms, not measured incident-prevention results.

**Invented W-9 email walkthrough, informed by Perpetual's example:**

| State | What is known | Permitted next step |
|---|---|---|
| Draft prepared | Recipient, document and email payload are available | Human reviews the exact plan/payload. |
| Payload approved | Approval belongs to that exact content/version | Execute that approved action within its scope. |
| Send request times out | The caller lacks a success response | Mark outcome unknown; do not equate timeout with failed delivery. |
| Service shows the email was sent | Independent external evidence resolves the ambiguity | Record success and continue the waiting state; do not send again. |
| Outcome cannot be resolved | There is no reliable confirmation either way | Escalate to manual review; keep the evidence and state. |
| Client reply changes the requested work | New facts or a new action may be needed | Re-plan/re-approve the affected work; old approval is not permission for changed content. |

**Teaching visual:** fork the timeout into “sent,” “not sent,” and “still unknown,” with evidence needed to leave the unknown state. Cross out the automatic arrow from timeout back to send. Draw the approval around the immutable payload, not around the agent as a permanently trusted actor.

**Presenter sequence:** Start with an ordinary external email, not an exotic agent failure. Ask what a network timeout actually proves. Reveal duplicate-send risk. Show the outcome record and manual route before discussing retries. Return to the separate question of authority: a correct revised message still needs permission if its approved payload changed.

**Why this adds teaching value:** “durable state and deliberate recovery” becomes a testable state machine. The exact follow-up lookup and branches above are an editorial fixture, not a claim about Perpetual's email provider or recovery API. Do not generalize “no automatic retries” into a ban on all retries: safe replay depends on the action contract, idempotency and resolved outcome.

## Presentation and accuracy guardrails

- Prefer these four decision traces to adding longer lists of controls. The current 40-minute timing can be preserved by replacing prose reading and generic loops, then using the detailed source context in the presenter script.
- Mark all invented cases, documents, amounts and counterfactual dates visibly. A company mechanism can motivate a fixture without becoming a company result.
- Keep “reported,” “illustrated,” “written account” and “description” where each changes the strength of the claim; do not repeat generic provenance labels on every paragraph.
- Presenter notes should describe what to reveal, what the audience should notice, the engineering implication and the evidence limit. They should explain the diagram rather than merely repeat its text.
- Align the content structure with the final visual: some `visualData` fields still describe superseded diagrams even though the current HTML renderers override them. If the upgrade uses structured slide data again, update those fields at the same time so later exports cannot revive an obsolete illustration.
- No JSON, HTML, SVG, rendered artifact or GitHub state was changed in this review.
