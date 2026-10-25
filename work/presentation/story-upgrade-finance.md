# Finance story upgrades for the live presentation

Reviewed October 25: the current 29-slide core in `deck-data.json` and the rendered HTML, against existing official transcripts and the finance evidence ledger. No new browsing and no deck edits. Core timings currently add to **40.0 minutes**. That is a timing allocation, not evidence that a rehearsed delivery fits; several pages combine three firms in 75–90 seconds. The enrichment explains mechanisms, but much of the main visual path still presents taxonomies and rules before the listener has encountered a specific problem.

**Recommendation:** replace selected overview material with five short case walkthroughs inside the existing live path. Each should have a visible protagonist/task, obstruction, intervention, retained human decision and one transferable lesson. Do not append all five as extra slides. The suggested spoken bridges below are original paraphrases for a presenter, not speaker quotations.

## 1. Bridgewater: “The answer was fluent, but the evidence was three months old”

**Best live location:** `grounding-02` (slide 9, currently 1.25 minutes). Replace the human-versus-agent comparison table as the dominant visual; keep its useful distinction as one annotation. This is the strongest grounding opening because the question, bad answer and repair are all concrete.

- **Setup:** Sam Green asks how AI infrastructure investment is affecting the Korean won and whether market participants expect that effect to continue. It is an early-October investment question requiring contemporary perspectives, not general background.
- **Mechanism:** The open-web example finds 15 plausible sources but uses only one or two; one important source is from July. With Vault attached, the agent scopes October 1–8, finds 52 candidate documents and uses seven. The important change is the eligible information set and time scope, not simply a larger prompt.
- **Failure/tradeoff:** A source can be topically relevant but too stale for the decision. Later in the same account, the enormous corpus still receives “search is bad” complaints; the team builds roughly 200 manually labeled questions with deceptive negatives and uses precision@10 to guide improvements.
- **Learning:** Define the required perspective and cutoff before measuring retrieval. Count relevant eligible evidence and inspect the human brief; candidate counts alone are not quality.

**Visible story structure:** one question across the top; two evidence trays below (“open web: July note / insufficient consensus” and “Vault: October 1–8 / broader source support”); a bottom transition from a user complaint to an adjudicated relevance set. Show the reported source counts only if their small label says **one demonstration, not a controlled benchmark**. The 60%→90–95% precision@10 result, if retained, needs its own measurement label; it is neither answer accuracy nor investment performance.

**Suggested spoken bridge (about 20 seconds):** “The issue here was not a model failing to write a plausible answer. It was answering an October market question from evidence that included July. Vault changed what the agent could know and how it selected the relevant period. Then Bridgewater still had to measure whether search actually returned useful documents.”

**Evidence:** official transcript, speaker-reported product and internal evaluation account. [Reading edition](https://ai.engineer/nyc/2026/talks/bridgewater); [question and stale-source demonstration, 0:11:28–0:13:51](https://www.youtube.com/watch?v=akEqiXFo3GM&t=688s); [benchmark, 0:15:36–0:16:45](https://www.youtube.com/watch?v=akEqiXFo3GM&t=936s). No independently reviewed holdout or causal alpha result was provided.

## 2. Apollo / Redding Ridge: “The hard part was deciding which source to believe”

**Best live location:** `strategy-01` (slide 3, currently 1.25 minutes), replacing the three generic output cards with one credit-operations story. Use Coatue’s code/ML/model/person decomposition on the next strategy page or in one concluding sentence rather than narrating three firms here.

- **Setup:** Redding Ridge, an Apollo credit unit, constructs CLO portfolios using legal documents, trade/compliance systems and current pricing. Data is fragmented and calculations are domain-specific. This is a front-office decision problem with substantial preparation work.
- **Mechanism:** Rowspace engineers sit alongside portfolio and finance practitioners to reconcile information, learn calculations, and determine the authoritative source. The system prepares a mock portfolio; the portfolio manager refines it. A second concrete example turns recurring financing/trade reconciliation into a repeatable report that the team still checks daily.
- **Failure/tradeoff:** Joining twenty feeds is not equivalent to resolving which one governs a particular fact. Faster generation does not remove source adjudication or professional QA. A portfolio described as 80–90% complete is a draft, **not an 80–90% accuracy result**.
- **Learning:** Define the accepted artifact and the reviewer’s remaining decisions. Evaluate source precedence and reconciliation, not only document extraction or fluent answers.

**Visible story structure:** legal constraints + current system feeds → practitioner-resolved source precedence → prepared portfolio/report → explicit PM refinement or daily QA. Put “What must the professional still decide?” beside the final artifact. Optionally include **speaker-reported: two–three days to minutes**, with a concise qualification that the study protocol and full review cost were not supplied. Do not calculate an implied firmwide ROI.

**Suggested spoken bridge:** “The visible output is a portfolio or report, but the real engineering work is behind it: learning why one source is authoritative when many systems disagree. Apollo’s account is useful because the human role is still visible. The PM refines the portfolio, and the team checks the recurring report.”

**Evidence:** customer/vendor joint transcript, specific to Redding Ridge’s account; not the separate Adam Nahari operating-margin session. [Reading edition](https://ai.engineer/nyc/2026/talks/apollo-rowspace); [two workflows, 7:53:53–7:56:36](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=28433s); [source precedence and embedded engineers, 7:57:42–7:59:09](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=28662s). Timing and completion claims are attributed reports, without controlled ROI evidence.

## 3. Citadel Securities: “The deck says green; newer evidence says otherwise”

**Best live location:** `grounding-01` (slide 8, currently 1.5 minutes). Its current Request→Evidence→Meaning→Context→Answer visual is a useful generic contract, but the Citadel Securities story would make time, contradictions and memory concrete before returning to that contract. Alternatively use it immediately after Bridgewater if root changes the order.

- **Setup:** Leadership asks whether a project is on track. A clean status deck says green, but a later thread exposes an unresolved dependency. Projects can also change names, making longitudinal continuity difficult.
- **Mechanism:** A monthly record retains what was reported, what the evidence supports, and why. An update/age/observe/grade/correct loop combines decks, messages and other opted-in signals. Models propose changes; code and people decide record updates. Historical records remain intact.
- **Failure/tradeoff:** Static retrieval can select individually relevant statements while missing the evolving state. Quiet or unavailable telemetry must remain unknown, not become a false zero. Human correction needs to capture reusable rules as well as fix a single fact.
- **Learning:** Store claims with time, provenance, source health and correction history. Freeze an as-of snapshot and assess it against later observations without letting future information leak into the earlier record.

**Visible story structure:** two lanes (“reported status” and “evidence-supported status”) over an earlier/later timeline. End at a proposed update with an explicit human/code commit gate, then a separate backtest arrow to a future observation. Label this a reconstruction of the narrated example, not a copied production screen. No invented dates, outcomes, confidence scores or accuracy percentages are needed.

**Suggested spoken bridge:** “RAG can retrieve both the green slide and the worrying message and still miss the real question: what do we believe now, and why? Citadel Securities treats that as a state-estimation problem. The record changes as evidence arrives, while the old record stays intact so we can later test what the system knew.”

**Evidence:** official practitioner transcript; Citadel **Securities**, not Citadel. [Reading edition](https://ai.engineer/nyc/2026/talks/citadel); [contradiction and update, 6:43:43–6:47:34](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=24223s); [as-of evaluation, 6:49:34–6:50:28](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=24574s); [missing sensor versus zero, 6:53:00–6:53:43](https://www.youtube.com/watch?v=jiUC6IUMdvc&t=24780s). Reported associations are observational; client-franchise expansion remains a direction, not established completed capability.

## 4. Range: “One planner is on a call; the next analysis is being drafted”

**Best live location:** `workflows-01` (slide 19, currently 1.5 minutes). Keep the five-step method, but precede it on the face with a two-lane work scene. The current five boxes tell the audience what to do without first showing why capturing judgment changes the work.

- **Setup:** A financial planner is serving one client while another client needs cash-flow or insurance analysis. General chat assistance does not automatically know Range’s planning method or when to stop for more information.
- **Mechanism:** The practitioner narrates previous cases, including why a document matters and what questions must be asked. Those reasons become a skill with required facts, exceptions and limits. An agent drafts while the planner is busy; the planner reviews and adjusts before a client sees any recommendation.
- **Failure/tradeoff:** Teaching clicks without reasons misses the professional method. Testing reveals missing questions and confident mistakes. A skill becomes stale if no owner maintains changing rules; an author’s confidence is insufficient independent review.
- **Learning:** Pick/Teach/Pack/Test/Ship is a maintenance workflow, not just prompt creation. A separate owner and reviewer govern the method; the professional governs the recommendation; the agent sends nothing.

**Visible story structure:** planner/client-call lane above agent/draft lane; merge at professional review; place the five method steps below as the reusable recipe. Mark the client-delivery line as human controlled. Keep skill counts out unless they help explain diffusion; they are adoption, not effectiveness.

**Suggested spoken bridge:** “The interesting part is not that a planner can ask an LLM for an answer. It is that Range captured how its own planners reason, including the question that must be asked before proceeding. The agent can prepare the work in parallel, but the planner still reviews the recommendation and controls what reaches the client.”

**Evidence:** official released transcript, now confirming owner plus separate reviewer; no measured accepted-capacity or advice-quality result. [Reading edition](https://ai.engineer/nyc/2026/talks/range); [parallel preparation and review, livestream from 3:00:11](https://www.youtube.com/watch?v=akEqiXFo3GM&t=10811s); [standalone release, method begins around 3:16](https://www.youtube.com/watch?v=gpmze-6ueGU&t=196s). Testing five–ten cases is the speaker’s starting routine, not sufficient statistical release assurance. The online release publication/index/attended dates differ; do not convert the indexed October 13 label into a filming date.

## 5. Arca + Perpetual: “The client changes the plan while the workflow is waiting”

**Best live location:** `workflows-05` (slide 23, currently 1.5 minutes). The rendered HTML now has an appropriate Interpret→Validate & approve→Wait & resume→Resolve outcome diagram. Retain that mechanism, but replace abstract node descriptions with two **clearly separated** short case lanes. Avoid claiming the two firms use one combined architecture.

- **Setup:** Arca’s narrated tax-payment example spans days: a client request, an approved plan, trades, settlement and transfer. A later client reply changes the amount needed. Real long-horizon work spends time waiting for events and people.
- **Mechanism:** Arca persists shared context and plans, resumes on a client/custodian signal or deadline, and pulls in the required person. Separately, Perpetual explains how a typed request becomes a compiled, approved immutable plan; external communication has an approval gate tied to its exact payload.
- **Failure/tradeoff:** A new reply must not silently inherit permission for a changed action. A timeout after dispatch does not establish failure: automatic retry can duplicate a consequential action. Perpetual routes an unknown outcome to manual review. That safeguard is not a measured guarantee about all external actions.
- **Learning:** Keep an explicit plan version, owner, next event and approval boundary. Model continuity and execution authority have different lifetimes. Unknown execution needs reconciliation before repetition.

**Visible story structure:** Arca lane: request→approved plan→wait→client change→human replanning; Perpetual lane: compile→approve exact payload→dispatch→known result or manual review. A shared bottom takeaway can synthesize durable state plus authority, with a caption stating the synthesis combines two separate reported accounts. Do not invent a real incident, transfer amount or production loss.

**Suggested spoken bridge:** “A ten-day workflow is not ten days of continuous model thought. It is short runs connected by persistent state, signals and people. Arca makes the waiting and replanning visible. Perpetual adds another boundary: if an external action may have happened but we lost the response, retrying is not a harmless default.”

**Evidence:** [Arca transcript](https://ai.engineer/nyc/2026/talks/arca), presented scenario rather than established customer outcome; [start at 1:53:23](https://www.youtube.com/watch?v=akEqiXFo3GM&t=6803s). [Perpetual transcript](https://ai.engineer/nyc/2026/talks/perpetual), wealth roll-up as introduced by Rao; [standalone side-effect discussion around 11:45](https://www.youtube.com/watch?v=8g0g1ncwzG0&t=705s). Do not identify Perpetual with a similarly named incumbent without separate evidence. Its small-model routing example is illustrative and the training loop remains future work.

## What should change in the live delivery

- Give each chosen story **one dominant visual and one question**. A company logo beside an abstract method is not yet a walkthrough.
- Use only one or two numbers per story, and immediately name their unit and evidence scope. Prefer a short qualitative story to an unexplained performance figure.
- Preserve the distinction between the actual narrated company example and our reconstructed diagram/acceptance test. Any extra scenario or values must say synthetic.
- Reuse the case rather than reintroducing firms: Bridgewater can motivate retrieval and later measurement; Range can motivate skills and later authority. This supplies continuity without lengthening the roster.
- The presenter script should cue **scene → problem → engineering choice → retained risk → takeaway → transition**, with explicit stage actions. Current speaker-note paragraphs largely repeat the reading prose and are not yet a timed, spoken script.
- For 40 minutes, replace rather than append. A practical starting allocation is Apollo 90s, Bridgewater 105s, Citadel Securities 90s, Range 90s, and Arca/Perpetual 90s, balanced by shortening repeated overview material. Rehearsal must validate the revised total; the JSON sum alone cannot.
