# Note capture, company readout, and logistics

Prepared October 10, 2026. These are recommendations for the confirmed use case: internal knowledge/research assistants and workflow agents. They are not statements about Fidelity's internal systems, controls, approval process, or targets.

## Practical logistics and source confidence

- Attend Tuesday October 13 and Wednesday October 14, 2026 at the **Sheraton New York Times Square Hotel**. The full conference runs October 12–14. **Workshops are on Monday October 12**, outside the requested days; the Tuesday/Wednesday plan should not invent workshop attendance. The NYC homepage describes workshops as an add-on. [Official NYC event](https://ai.engineer/nyc/2026), [detailed schedule](https://ai.engineer/nyc/2026/schedule).
- Treat the **detailed schedule, refreshed October 10**, as the planning source. It displays New York/ET times and says times, rooms, and speaker assignments are tentative. Its session times differ from the homepage's older block overview. Refresh it the evening before each day and at registration. [Detailed schedule](https://ai.engineer/nyc/2026/schedule).
- Ticket access is unresolved: the homepage lists Engineering tickets as available and Leadership as sold out/waitlist. The ticket checkout requires JavaScript and did not expose precise entitlements in the public text view. Do not assume a Principal title grants access to leadership sessions or the speaker/token-billionaire lounge. The organizer's general terms permit restrictions by credential tier, track, pre-registration and capacity. Build the main plan from open engineering content, mark leadership items conditional, and keep an accessible alternate. [NYC ticket page](https://ai.engineer/nyc/2026#tickets), [checkout](https://app.ai.engineer/e/u/checkout/ai-engineer-new-york-2026/tickets/order), [terms §3](https://ai.engineer/tos).
- **Recording and slide availability is unconfirmed for NYC 2026.** The organizer links its YouTube channel and hosts a public talks archive. That establishes a place to check later, not a promise that each NYC session, leadership session, or slide deck will be published. The general FAQ explicitly concerns World's Fair 2026 and should not be used to promise NYC recording coverage. Capture the speaker's offered slide/repository URL, or ask after the talk. Link to materials rather than attaching their entire deck to the company report. Check session rules before recording or photographing; the terms restrict content distribution. [Organizer YouTube](https://www.youtube.com/@aiDotEngineer), [talk archive](https://ai.engineer/talks), [archive data coverage](https://ai.engineer/data), [FAQ—World's Fair scope](https://ai.engineer/faq), [terms §6](https://ai.engineer/tos).

## Optional evening choices

These are suggestions for networking, not assumed inclusions in the conference ticket. Confirm registration/approval and final time/location; do not register on the user's behalf.

1. **Tuesday: Secure Software Factory Show and Tell**, organizer listing 5:30–8:30 p.m., Elsie Rooftop, 1412 Broadway. Best thematic match if agent identity, authorization and verification are priorities. Host page names Keycard, Braintrust and Socket and explicitly requires approval. Attend after the closing sessions and a short synthesis break rather than departing early simply to reach the opening. [Host registration and approval](https://luma.com/keycard-rg1c?utm_source=aie), [organizer event listing](https://ai.engineer/nyc/2026#events).
2. **Tuesday: Table Stakes**, organizer listing 5:30–8:30 p.m.; address supplied on RSVP, space limited. Best breadth of infrastructure contacts: the host group spans evaluations, orchestration, model infrastructure and cloud. Useful for finding practitioners to compare failure-handling and evaluation approaches. Treat it as networking, not a technical session with guaranteed content. [Organizer event listing and RSVP links](https://ai.engineer/nyc/2026#events).
3. **Tuesday: Optiver Social: Think Fast!**, organizer listing 6–10 p.m., M Social Hotel, 226 W 52nd St. Best financial-services peer networking; weaker for structured technical learning. Separate RSVP. [Official Optiver registration](https://optiver-8296840.hs-sites.com/aie-ny-2026), [organizer listing](https://ai.engineer/nyc/2026#events).

**Wednesday: Speaker VIP Happy Hour**, organizer listing 5:30–7:30 p.m. at Dear Irving on Broadway. The host page requires approval, describes it as welcoming speakers, and asks registrants to obtain the exact location. **Do not count on general-attendee access or treat this as the same event as the schedule's Leadership Reception sponsored by Primitive.** Only add it if invited/approved. Otherwise use 30–45 minutes to synthesize the conference and schedule later follow-ups. [Host approval page](https://luma.com/6dobkzfh?utm_source=aie), [organizer listing](https://ai.engineer/nyc/2026#events), [detailed schedule](https://ai.engineer/nyc/2026/schedule).

## Capture decisions, evidence, and a test—not a transcript

An 18-minute talk is too short for comprehensive transcription and careful thinking. Aim for **one reusable idea, one supporting example, one limitation, and one action**. The report-back unit is a decision your team can evaluate, not a list of products or slogans.

### Before Tuesday: 25-minute setup

1. Create one conference notebook in the company-approved note location. Pre-create a page for each primary talk: title, speaker/company, time/room, official session link and one question you want it to answer.
2. Create three experiment questions: (a) Can better evidence retrieval improve an assistant's usefulness? (b) Can we detect agent failure before a bad action? (c) Can we make the workflow auditable and economical?
3. Create an index with five tags: **retrieval/context; evaluation; agents/reliability; security/governance; adoption/economics**. Add a separate parking lot for vendors and tools, so product names do not become the conclusions.
4. Keep public conference notes distinct from confidential company-specific application notes. Use only approved storage and approved AI tools for any internal material. You can write public observations offline during talks and add company context later in the approved workspace.

### The 18-minute capture loop

| Moment | What to do | Maximum output |
|---|---|---|
| 1 minute before | Write the decision/question this talk could inform | One sentence |
| First 3 minutes | Identify the actual workload, users, constraints and maturity: demo, pilot or production | Two bullets |
| Middle 12 minutes | Capture mechanism/architecture, strongest evidence and failure modes; sketch a simple data/tool flow if useful | Three to five bullets + one sketch |
| Final 3 minutes | Write the transferable idea, what remains unproven, and one experiment/question | Three bullets |
| Transition/break | Finish a 30-second memory summary and tag it; do not consume the whole room-transfer buffer | Four lines |

The detailed schedule usually leaves several minutes between short talks. Room changes take precedence over polishing notes. Batch completion at lunch/coffee. For a longer panel, separate speakers' claims instead of treating the panel as one consensus position.

### Reusable talk-note template

```text
TALK / SPEAKER / COMPANY:
DATE / TIME / ROOM / OFFICIAL URL:
WHY I CHOSE THIS (decision to inform):

ONE-SENTENCE TAKEAWAY:
MECHANISM (data → retrieval/model → tools → checks → output):

STRONGEST EVIDENCE:
- Claim and source:
- Workload/sample + baseline + metric + time period:
- Maturity: demo / pilot / production / unclear
- Missing details or counterexamples:

FAILURE MODE / CONTROL / TRADEOFF:
WHAT COULD TRANSFER TO OUR WORK (hypothesis):
SMALLEST TEST + success measure:
OPEN QUESTION FOR SPEAKER:
SLIDES / REPOSITORY / RECORDING LINK (if offered):
FOLLOW-UP: person, reason, permission/channel, next action
TAGS:
```

### Evidence labels that prevent a misleading report

- **Speaker claim:** Something stated, including a numeric benefit with no enough method to assess. Attribute the speaker/company. A polished slide is still a claim.
- **Evidence shown:** Results with workload, sample/period, baseline and metric described. Record what was shown and the omissions; this is not independent verification.
- **Public artifact checked:** You inspected the linked paper, code or measurement method. Record the version/date and what it actually establishes.
- **Our hypothesis:** Your interpretation of possible Fidelity relevance. Keep it explicitly separate from a reported conference result.
- **Internally validated:** Only after your team reproduces a useful result under its own data, constraints and controls. No item starts in this category at the conference.

For every impressive percentage, ask: **Percentage of what? Compared with what? Over what period? What errors were excluded? What did humans still do?** Capture cost per *accepted successful task*, including human review/rework, rather than tokens alone. This is a proposed evaluation practice, not a claim about Fidelity's existing measures.

### Questions worth spending a hallway conversation on

- **Retrieval:** How did you detect missing/stale sources, preserve permissions, and evaluate citation support? What fraction of questions should abstain?
- **Evaluation:** What failed despite passing offline evals? Who labeled difficult examples, and how did you prevent the test set from shaping the solution?
- **Agents:** What happens after a timeout, partial tool failure, duplicate action or invalid state? Which steps require approval, and can execution be replayed?
- **Identity/security:** Is authorization bound to the user's intent and every tool call? What evidence demonstrated isolation across users/documents?
- **Economics:** What is the full cost per accepted task, what baseline did you beat, and which use cases did you stop?
- **Vendor/demo:** Which part can we reproduce with a small test? What capabilities require a different deployment or paid tier?

## Daily synthesis: turn attendance into work product

**At lunch: 10 minutes.** Finish the three most valuable notes; mark uncertain claims; select two questions for afternoon speakers. Review the afternoon path in case the morning changed your priorities.

**After the last session: 20 minutes before a social event.** Make a 3–2–1 digest: three useful patterns, two unresolved risks or competing claims, one experiment worth proposing. Link every pattern to specific talk notes. Fill gaps with “unknown,” not recollection presented as fact. Preserve useful failures and negative results, not just success stories.

**Wednesday wrap: 30–45 minutes.** Compare independent accounts of the same theme, choose the three strongest recommendations, and mark each Adopt / Test / Watch / Reject with reasons. Add a “what changed my mind” row. Build a source backlog for slides or recordings that have not been released; do not delay the initial readout waiting for them.

**Suggested deliverable standard:** a complete capture for every attended session, 5–8 carefully supported insights, 3 proposed experiments, 3–5 useful contacts with a defined follow-up, and an explicit list of open questions. These are proposed attendance goals, not company mandates.

## Report back in two layers

### Manager: one-page executive summary, within two business days

Suggested date: **Friday October 16, 2026**. Keep the summary decision-oriented.

1. **Purpose and scope:** Why attended; confirmed focus; which days/tracks covered.
2. **Three lessons:** Each has a plain-language statement, source talk, evidence quality and business implication.
3. **What this changes:** One thing to continue, one thing to test, one thing to avoid/pause—only if the evidence warrants it.
4. **Proposed next step:** Narrow pilot, owner to confirm, estimated effort/cost to scope, success measure and stop rule. Present any resource request for review rather than suggesting a purchase based on a talk.
5. **Uncertainty:** Vendor claims unvalidated internally, access/recording gaps, unanswered architecture or control questions.

Do not pre-write conference lessons as already learned. Before the event, this is a fill-in structure. After it, replace hypotheses with attributed observations.

### Technical peers: 30-minute readout within one week

Suggested date: **Wednesday October 21, 2026**. Agenda: 3 minutes goals/context, 12 minutes three mechanisms with diagrams and failure modes, 8 minutes evaluation/experiment designs, 5 minutes recommendations and tradeoffs, 2 minutes ownership/next steps. Put citations beside claims and include a reference appendix.

Supporting package: notes index; 3 architecture/sequence sketches; a small failure taxonomy; an experiment backlog ranked by impact/effort/evidence; links to public materials; unresolved questions. A reusable harness or test set is often a stronger return than a large slide deck.

### Copy-ready executive-summary scaffold

```text
AI Engineer NYC 2026 — attendance readout
Attended: Oct 13–14 | Focus: internal assistants and workflow agents

Most decision-relevant finding:
[Observation + talk/source + evidence strength]

Three takeaways and implications:
1. [Finding] → [Implication] → [Uncertainty]
2. [Finding] → [Implication] → [Uncertainty]
3. [Finding] → [Implication] → [Uncertainty]

Recommendation:
[One narrow experiment, baseline, proposed owner, expected effort to validate]

Decision/request:
[Specific approval or prioritization needed, if any]

Success and stop rules:
[Quality, risk, time, cost measures; threshold to agree before testing]

Next checkpoint / sources:
[Date and links to inspected evidence]
```

## Proposed 30/60/90-day experiments

These are options to discuss with your team. They do not presume approval, available datasets, a particular model/vendor, or existing Fidelity policy. Numeric goals below are **illustrative pilot acceptance targets to agree after baseline measurement**, not promised results or mandated controls. Evaluate quality and risk before interpreting speed improvements.

| Horizon | Narrow experiment | Design and measures | Deliverable and stop/grow decision |
|---|---|---|---|
| **By day 30: evidence-grounded assistant** | Test whether a permission-aware retrieval pipeline improves one bounded internal knowledge/research task | Use an approved representative or public/synthetic corpus. Assemble ~100 expert-reviewed questions spanning answerable, multi-source, stale/conflicting and unanswerable cases. Hold out a test portion; tune only on development cases. Compare current/manual search baseline with retrieval+citations under the same access. Measure answer correctness, citation support, abstention, retrieval recall, stale-source errors, permission leakage, p50/p95 latency, review time and cost per accepted answer. Example hypothesis: reduce median task time ≥20% with non-inferior expert quality and no observed leakage in the defined adversarial suite. | Reproducible benchmark, error taxonomy and decision memo. If quality regresses or access tests fail, repair before piloting. Zero observed failures in a finite suite does not prove absence of risk. |
| **By day 60: controlled workflow agent** | Add tool use to one repetitive, reversible research/reporting workflow once the baseline works | Compare agent-assisted execution with the same manual or scripted workflow on ~50–100 held-out tasks. Start read-only or sandboxed; add human confirmation at consequential steps. Inject timeouts, stale input, malformed results, denial of authorization and interrupted execution. Measure end-to-end accepted completion, harmful/duplicate tool actions, recovery, human interventions, trace completeness, latency and all-in cost including rework. Illustrative target: ≥20% less active human time at non-inferior quality; no unauthorized/duplicate action in defined tests; every run traceable to inputs, tools and approvals. | A working narrow end-to-end prototype, failure report and explicit permission model. Increase autonomy only if tested controls and recovery work; prefer a deterministic workflow if it performs as well with less complexity. |
| **By day 90: monitored pilot and governance package** | Determine whether the assistant/workflow remains useful with real variability | With approval, run a small time-bounded cohort; use shadow evaluation before consequential execution. Freeze versions, log redacted traces, define escalation/rollback, and review a stratified sample of real tasks. Compare accepted task quality/time/cost and incidents against baseline; report uncertainty and subgroup failures. Example target: sustained ≥20% median time reduction over two weeks with agreed quality, budget, security and reliability gates. | Pilot readout: grow, revise or stop; reusable evaluation suite; monitoring/rollback runbook; total-cost estimate and owners. Do not scale on usage or satisfaction alone. |

For small samples, show counts and uncertainty, not just percentages. Report critical failure categories separately; an average score can hide a serious authorization or unsupported-answer failure. Ask domain reviewers to assess output without knowing which system produced it where practical. Fix the success/stop criteria before the final comparison.

## Source register for integration into the HTML report

| Source | Supports | Caveat |
|---|---|---|
| https://ai.engineer/nyc/2026 | Dates, venue, Monday workshop add-on, ticket availability, event listing | Homepage block times differ from detailed schedule; avoid using it for exact session timing |
| https://ai.engineer/nyc/2026/schedule | Published exact sessions, rooms, ET, tentative status, Oct10 freshness; Leadership Reception | Public text does not settle credential entitlements |
| https://app.ai.engineer/e/u/checkout/ai-engineer-new-york-2026/tickets/order | Official checkout, dates and venue | Detailed entitlements not readable in non-JavaScript view |
| https://ai.engineer/tos | Tier/capacity access restrictions; content distribution terms; attendee support contact | General terms; this is not a legal opinion |
| https://luma.com/keycard-rg1c?utm_source=aie | Secure Software Factory host and approval requirement | Times/venue taken from organizer listing; host confirmation governs attendance |
| https://luma.com/6dobkzfh?utm_source=aie | Speaker VIP happy hour approval and speaker audience | Do not assume attendee eligibility; not the Primitive leadership reception |
| https://optiver-8296840.hs-sites.com/aie-ny-2026 | Official Optiver RSVP destination | Public text view exposes little form detail |
| https://www.youtube.com/@aiDotEngineer | Organizer recording channel | No verified NYC2026 per-session publishing promise |
| https://ai.engineer/talks | Official archive for later source checking | Archive includes past events; do not label them NYC2026 learnings |
| https://ai.engineer/data | Organizer's published talks/data coverage | Distinguishes scheduled sessions from published talks; transcripts automated |
| https://ai.engineer/faq | Establishes FAQ is World's Fair2026, not NYC | Do not transfer its recording or ticket guarantees to NYC |
