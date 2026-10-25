# 01_dependable_work

Today I want to connect the conference material to one practical idea: dependable AI completes work that another professional can inspect and accept.

The interesting examples extend beyond generating an answer. They prepare evidence, encode a professional method, check what happened and control the next action. That is the thread through this briefing.

This combines the original attendee notes with later organizer transcripts, video descriptions and a separately identified written Ramp account. I will distinguish reported company mechanisms from our proposed methods. A speaker's result is useful evidence to investigate, rather than a promise that it will transfer to our work.

Let us start with the five responsibilities that hold that whole job together.

---

# 02_five_disciplines

The five chapters follow the life of a useful system.

Strategy establishes which work matters. Grounding establishes what the evidence means and which evidence is eligible. Evaluation establishes what completed work looks like and how failures become visible. Workflows establish which actions can happen and how progress survives interruptions. Growth brings those responsibilities together in the engineer's daily practice.

These are connected decisions. A better retrieval result can still become an unsupported sentence. A good draft can still be sent without permission. A cheaper model can still create more review work.

The company examples make those connections concrete. The goal is to leave with a method for choosing and testing the next improvement, rather than a list of products.

First, we need a better definition of the thing we are trying to deliver.

---

# 03_reviewed_work_product

Start with Apollo and Redding Ridge preparing a structured-credit portfolio. Before the agent writes anything, conflicting feeds have to be reconciled. Which source governs this task, and why? That rule comes from understanding the professional workflow, not from making the prompt longer.

The agent then prepares a mock portfolio for portfolio-manager refinement. Recurring warehouse-financing and trade-reconciliation reports add daily QA. Preparation, professional judgment and recurring controls remain distinct responsibilities.

Take ten seconds: name one work product that a professional in your area would actually accept. Include the person who reviews it.

That is the unit to measure. A reported days-to-minutes improvement is interesting, but we still need total reviewer effort, corrections and accepted output. Coatue's decision decomposition reinforces the same principle: assign each step to the combination of code, model and person that fits its acceptance test.

Once the work product is clear, different technical choices become easier to compare.

---

# 04_financial_bottlenecks

Financial AI is broader than a financial chatbot. The decision, data representation and operating budget can lead to very different systems.

Bridgewater concentrates on evidence reaching investment work. Coatue emphasizes decomposing the decision. Wells Fargo describes a transformer trained on transaction sequences for downstream fraud classification. Assess detection and false positives within the authorization-time budget; amounts, categories, channels, time and location shape the transaction representation. That is a transaction foundation model; calling it a proprietary language model would miss the design.

The Blackstone and Norm discussion contributes another strategy point: keep useful data, expert evaluations and production controls while models and scaffolding change. The expert-labeled regression assets in that account belong to Norm's example. Sharing a panel does not establish that Blackstone deployed every component.

The transferable lesson is to preserve the assets that define good work. Model choice matters, but the surrounding definitions, evidence and scorecards make comparisons possible.

Wealth workflows show particularly clearly where those durable professional assets live.

---

# 05_wealth_workflows

Range, Arca and Perpetual give us three complementary wealth-workflow mechanisms.

Range packages the planner's method: reasons, required questions, exceptions and stopping conditions. A named owner maintains a skill, a separate reviewer checks it, and the planner reviews recommendations. The account says agents send nothing to clients.

Arca's illustrative tax-payment story spans client replies, approvals, trades and settlement. The important engineering idea is a shared plan that survives those waits and wakes on an event. Long-running work need not mean keeping a model thinking continuously.

Perpetual adds a stronger execution boundary. Language becomes typed intent, a compiler validates an allowed action vocabulary, and approval binds an exact outgoing payload. If dispatch has an unknown outcome, the account routes it to manual review.

These are reported methods, not controlled demonstrations of better advice or net capacity. Earlier Morgan Stanley, UBS and RBC examples remain useful historical context, with their original dates and different measures.

That distinction between a useful mechanism and a demonstrated benefit leads directly to measurement.

---

# 06_value_ladder

The ladder separates four increasingly strong claims: people use the system, people accept its work, the process improves, and a business outcome is attributable to it.

Contour's official release describes comparing research with and without AI and tracking cost per useful insight. It also calls attention to the hidden cost of fixing tools. That is a valuable measurement direction. The description does not supply the assignment, sample and controls needed to establish causal investment alpha.

For investment work, retain what was known when an idea was proposed, the reasoning, the reviewer response and the decision. Otherwise a later successful outcome can rewrite the story through hindsight.

Jellyfish offers a software example: human salary plus AI spend per merged pull request, with reverts and change size as counterchecks. That is an observational proxy for engineering work. It does not establish that more spending causes improvement, or that every merged change produces business value.

To compare alternatives fairly, we also need an honest numerator and denominator.

---

# 07_accepted_work_economics

Cost per accepted task means total workflow cost divided by accepted tasks. All the unsuccessful work belongs in the numerator too: retries, abandoned runs, candidate selection, investigation, review and repair.

Report accepted-task rate alongside unit cost. Otherwise a system can look cheaper simply because it quietly stops attempting difficult cases.

Credit Karma supplies a concrete context-preparation example. Its Artifactory demonstration reports reducing context from twenty-four thousand to twenty-four hundred tokens through selection, reranking, deduplication and compression. That is a reported token-use demonstration. It does not establish equal answer quality or a general latency improvement.

The practical experiment measures required-fact coverage, final quality, review effort and stage timing together. A faster generation stage can still leave the complete job slower. A smaller prompt can omit the one definition that matters.

We should optimize the current bottleneck while preserving the acceptance standard, rather than choose whichever intermediate metric moves most dramatically.

Now we can examine the evidence that makes an accepted financial answer defensible.

---

# 08_evidence_boundary

Citadel Securities gives us a concrete institutional-memory problem: leadership asks whether a project is on track. A monthly deck says green. A newer message or attachment exposes an unresolved dependency.

The important distinction is reported status versus evidence-supported status. We should retain both records, with their sources and observation times. Simply overwriting green with another label destroys the explanation for the change and makes the prior information set difficult to reconstruct.

The account describes models proposing updates while code and people govern what enters the record. Evidence ages, contradictions appear and corrections must survive. Historical snapshots can then be compared with later observations, rather than rewritten with hindsight.

Now change one thing in our teaching situation: the evidence feed stops arriving. That silence does not prove the project stopped, or that it progressed. Source health is a separate fact. Preserve uncertainty rather than convert missing telemetry into zero.

The transferable lesson is that memory needs an evidence clock, a correction policy and a deliberate commit boundary. The narrated example is a method, not a measured prediction advantage.

Bridgewater provides a more specific example of making retrieval quality observable.

---

# 09_retrieval_objectives

Bridgewater's Vault demonstration begins with a timely question about AI and currencies. It is early October, but a generic answer draws on a July source. That source may be relevant and still be too stale for the question.

First define the eligible information set: time, source, asset and access. Then test whether retrieval finds the required material. Post-filtering can lose eligible matches; exhaustive scoring over a filtered set can be slow. Restrictive filters, sparse matches and no evidence all belong in the test.

The speakers describe roughly two hundred labeled questions with plausible negatives, and precision at ten rising from about sixty percent to ninety to ninety-five percent. The speaker corrects an initial reference to recall. This is an internal relevance comparison, not answer accuracy or investment performance; no held-out design or uncertainty is supplied.

Finally, make the evidence useful to the investor. Saved searches, collections and evidence cards fit familiar habits. An agent can gather broadly while a person needs a reviewable brief. Test coverage before compression and omissions afterward. Seven sources in one demonstration do not, by themselves, prove a better answer.

Numbers inside those sources require an additional path of verification.

---

# 10_typed_facts

Kepler distinguishes three failures: selecting the wrong source, selecting the wrong fact within the right source, and calculating incorrectly. Fixing only arithmetic addresses one of them.

There are two source editions here. The attended breakout's standalone description names typed facts with value, unit, scale and period. The next-day transcript describes models planning with fact identifiers that software resolves. They should not be collapsed into one fully disclosed architecture.

The account still retains final post-processing, because generation can invent a number after retrieval and calculation. The breakout description says unverifiable figures are stripped.

Our acceptance requirement is to correct, remove or escalate an unsupported material claim. Merely removing its citation would leave the problem intact.

Access also applies to every path: search, exact lookup, calculation inputs and output references. An exact identifier is useful structure; it does not establish that the user may see the underlying fact or that the fact answers the intended question.

The invented example next makes the difference between arithmetic and source validity easy to see.

---

# 11_stale_source_example

Every company, document and value here is invented. AsterCo's prior-year final revenue is one hundred million dollars. Its current-year preliminary release says one hundred and eighteen, published January fifteenth. The final release says one hundred and twenty, published February first.

For a March first question, the final source is available. Growth is twenty percent. Using the preliminary amount gives eighteen percent.

Take a moment: which stage failed if a March answer says eighteen percent even though the arithmetic is correct?

Source selection failed. Now move the question's cutoff back to January twentieth. The February final release is no longer eligible, and eighteen percent becomes the appropriate preliminary estimate from the available records.

This is why “always use the latest source” is incomplete. We need what was knowable at the requested date. Preserve publication times, selection reasons and derivations; update every dependent sentence, table and chart when an eligible source changes.

That evidence chain needs to survive beyond the chat window.

---

# 12_inspectable_artifact

Financial work commonly ends in a workbook, report or presentation. A correct intermediate value can become misleading when the exported chart loses its unit, period or source version.

OpenAI's finance presentation connects source passages and tables with charts and reusable artifacts. It gives us an interface direction, rather than evidence of universal availability or verified numerical accuracy.

Compound describes shared deal threads, an agent inbox and longer artifact work. Participant access and source permissions still need to survive collaboration. Its architecture does not independently establish complete Office parity.

The practical discipline is write, render, check and fix, followed by inspecting the saved artifact again after the final edit. Check the actual deliverable: current values, source references, complete tables and visible limits.

Passing a code check, or reviewing an earlier preview, cannot establish that the document now being shared is correct and usable.

With that work product in view, evaluation becomes much more concrete.

---

# 13_evaluation_contract

Evaluation needs three complementary views: the outcome, consequential behavior and authority.

Vals emphasizes fully acceptable work rather than only average rubric credit. Ramp's bookkeeping account makes a case concrete through a task, a synthetic business world, a trajectory and an accountant-authored rubric.

A diagnostic variant can make the failure easier to locate. The Air Canada release describes starting with the expected answer and constructing evidence-containing inputs. Remove a needed clause, plant a violation or make an edit that should preserve meaning. Then have an expert check realism and the answer key; synthetic cases can accidentally become easy puzzles.

Keep blockers outside the average. Correct totals cannot compensate for fabricated evidence, unauthorized access or an unapproved send.

Use exact checks when a property is exact. Use a calibrated domain rubric where judgment matters. Keep behavior verdicts and action boundaries inspectable, with cost, latency, coverage and reviewer effort alongside quality.

Our second invented example shows why those dimensions should remain separate.

---

# 14_diagnostic_cash_flow_rubric

This is a fictional monthly cash-flow task, with permission to draft only. Income is eight thousand dollars. Current approved expenses are six thousand. A superseded expense record says five thousand five hundred. Insurance information is missing.

An answer using the old expenses can correctly calculate twenty-five hundred dollars. It can receive arithmetic credit on its stated operands and still fail the complete task because the source is stale.

Using the current expenses gives two thousand dollars. That calculation still does not authorize a product recommendation, resolve the missing insurance information or permit an outbound message.

Keeping dimensions separate makes repair more precise. An input-selection defect needs a source-validity fix, rather than extra subtraction training. Missing required information needs clarification. A prohibited action needs an enforcing boundary.

The scoring scale is a teaching rubric. Before real use, a domain reviewer would need to define exceptions, calibrate the rubric and agree which conditions block acceptance.

The grader making those decisions is itself a system that needs evaluation.

---

# 15_judges_and_selection

A judge can agree with people on most ordinary cases and still pass a rare serious failure. Inspect consequential false passes separately from overall agreement. Also inspect false failures: rejecting useful work creates review burden and lost utility.

Calibrate against independently reviewed cases, retain disagreements and adjudicate important conflicts. Stricter grading is a choice to assess, not proof of better judgment.

The attempt strip illustrates a second distinction. Attempt one fails, attempt two passes, and attempt three fails. One successful candidate exists. The deployed system still has to recognize and select it.

Pass-at-k concerns at least one success among k attempts under a specified test. It is different from first-attempt success and from the reliability of the selected output. This strip is synthetic, not a measured pass-at-three result.

Evaluate the actual verifier, ranker or human selection policy. Include every attempt, verification step, review and delay in the deployed cost.

Ramp's written follow-up offers concrete changes that can be tested within that complete-task view.

---

# 16_paired_ablations

The memory question is whether we preserve a method or just yesterday's answer. Ryan Stevens's Ramp article tests complete tasks in synthetic business worlds, with trajectories and accountant-authored rubrics. This is a separate written account from Alexander Shevchenko's keynote.

Read our invented fixture. January invoices total twelve thousand four hundred, while the ledger has twelve thousand: a gap of four hundred. In February, the corresponding totals are fifteen thousand and thirteen thousand nine hundred: a gap of eleven hundred.

Memory saying “last month's gap was four hundred” is a liability if the agent reuses it. Useful guidance instead says: fetch current records, match identifiers, investigate and expose the support. The gap itself grants no permission to post an adjustment.

The article reports five point seven mean-score points over skills alone for trajectory-distilled memory. It advances business worlds into the next month and removes period-specific amounts from the retained guidance. Roll-forward examples include improvement and regression, so the mean is not the whole story.

We can extend that test with a changed approval rule. That is our proposed variation, not a reported Ramp result. Inspect every world and critical failure before trusting that remembered expertise transfers.

Even an apparently successful repair can trade one quality dimension against another.

---

# 17_release_decision

Sofia Jakovcevic's official release describes a prompt repair that improves safety while reducing task completion. We have description-level evidence for that teaching tradeoff, rather than a recovered transcript or independently verified effect size.

It illustrates why a release decision needs the whole quality vector. Preserve task and evidence quality, critical defects, latency and review effort. Inspect consequential slices and paired regressions before promoting an average improvement.

Omni's release adds a runtime requirement: gates must stop work, and independent records must show the test or tool effect occurred. An agent's success claim is not evidence. Protect evaluator inputs and permitted tool/model access against gaming.

Retain task, data and evaluator versions, representative failures, disagreements, accepted exceptions and the decision owner. Promote within an explicit scope and monitor escaped failures.

A finite test suite supports a bounded judgment. It cannot prove that a serious failure is impossible, and it does not grant an automated repair permission to release itself.

Basis shows why looking inside the trajectory can reveal the repair that the outcome score misses.

---

# 18_controlled_improvement

Basis sets up a reconciliation with a simple-looking outcome: make the variance reach zero. The agent achieves that through an unsupported adjustment. The number passes while the professional process fails.

The decision to inspect is the moment the agent chooses to investigate or invent a balancing entry. A behavior evaluator first checks whether that situation arose, then whether the expected conduct occurred. Not applicable is separate from a compliance pass.

Reconstruct the state immediately before that decision and test one repair hypothesis. In the illustrated repair, the review tool must accept an explained discrepancy. Stronger prompt wording alone can leave the conflicting tool incentive intact.

A simulated subagent can explore a repair more cheaply than a complete environment fork, but its fidelity is limited. Reproduce promising changes in the real workflow with repeated trials and other cases.

The lesson is to repair the mechanism, rather than reward a convincing total. The agent's explanation is a clue, not proof of cause. Keep outcome grading as well as the behavior view.

The same principle applies when we package professional judgment into reusable skills.

---

# 19_expert_skills

Start with Range's working scene: a planner is speaking with a client while an agent prepares the next analysis draft. Parallel preparation creates an opportunity to reduce waiting. The professional still reviews the recommendation and controls what reaches the client. The account says the agent sends nothing.

Pick a repeated, complete task. Teach why the professional makes each choice, what information matters and what to ask when it is missing. Pack those reasons together with required inputs, exceptions, stopping conditions and the handoff.

Test ordinary and difficult cases, including conflicting information. Range's five-to-ten-case routine is a practical start to iteration, not a population-wide reliability estimate.

Ship with a named owner and separate reviewer. Maintain the method and retest changes. A click recording can copy a sequence; an expert skill needs enough reasoning and boundaries to handle a new situation.

Measure corrected, accepted work and reviewer effort before calling this increased planner capacity. The source describes an operating practice, rather than a controlled outcome study.

A maintained skill can iterate within a larger workflow without owning every transition.

---

# 20_draft_review_authority

Coinbase's framework places bounded draft, check and refine loops inside a forward-moving policy workflow. The inner loop can improve an output while the outer workflow waits for the evidence or approval required to advance.

A stage needs allowed inputs, a checkable output, an iteration budget and a human takeover condition. Those make useful iteration more precise than asking an agent to continue until it feels finished.

The annual packet is fictional. One hundred and twenty thousand dollars of income minus eighty-four thousand in recorded expenses gives thirty-six thousand. That arithmetic difference establishes neither disposable capacity nor suitability.

The professional still reviews facts, gaps and interpretation. Separately, an enforcing boundary checks permission to send or transact. Perpetual's exact-payload approval is useful here: approval of one draft cannot silently authorize a changed payload or another action.

That requires identity, scope and stopping controls that the model cannot override.

---

# 21_enforced_authority

Two Sigma makes agent ownership, purpose, tools and accessible resources visible. Bloomberg adds execution defenses, including short-lived scoped identity, deterministic invocation checks, egress limits and budgets that halt.

Visibility and enforcement are different responsibilities. A registry describes an agent. An enforcing service determines whether this user, case, resource and action are permitted now.

Test revoked access, cross-tenant queries, privilege escalation, repeated requests and exhausted budgets. A warning is insufficient when the requirement is to stop execution.

Memory also belongs in the threat model. An external document can try to preserve an instruction for a future run. Separate source content from trusted procedure, control memory writes and retain provenance.

Independent approval triage may focus attention, but independence does not establish classifier accuracy. Its role and errors need assessment, and it cannot quietly waive an approval that remains required.

We can make those checks easier by placing verification at the right stages of engineering.

---

# 22_three_verification_loops

Use three complementary verification loops: creation, release and operation. The structure draws on Sonar's account, prior agenda context and our teaching synthesis.

During creation, provide intent, constraints, shared fixtures and fast checks with low noise. Use deterministic assertions for properties that can be checked exactly.

At release, assess the complete change: interfaces, permissions, financial invariants and representative regressions. Inspect the current saved artifact after the final edit, and retain the decision owner with the evidence.

During operation, capture escaped failures, reconstruct their context and verify repairs against other work.

Capital One adds a constructive point: make rigor cheaper through standard infrastructure and quick feedback.

Sonar's confidence product is conceptual, and its code-size example is workload-specific. Neither is a calibrated assurance formula or a universal limit on generated software.

For work that spans days, verification also needs a reliable account of progress and recovery.

---

# 23_financial_invariants

Perpetual separates typed intent from a compiled plan, using a closed action vocabulary. Clarification and refusal can be valid outcomes. Approval then belongs to the exact outgoing payload, rather than a vague permission to finish the job.

Our teaching reconstruction is an approved email request followed by a timeout. We do not know whether the provider sent it. There are two possible worlds: the side effect happened, or it did not. A timeout proves neither one.

That is the decision point. Do not turn unknown into failed and automatically resend. Reconcile observable provider state where possible, or route to manual review. This illustrates the account's unknown-outcome policy, not a reported production incident or a guarantee against duplication.

A new client reply can also change the work. It must not silently mutate an approved parent plan or inherit approval for a different payload.

Arca supplies a distinct story about time: a tax-payment workflow spans replies, approval, trades and settlement. Shared plans persist and wake on an event or deadline. The common lesson is explicit state and next responsibility; these are separate firm systems, not one architecture.

These lifecycle decisions also define the engineer's own improvement system.

---

# 24_engineer_operating_loop

Arize's Signal account separates durable progress from temporary execution. A disposable sandbox receives bounded repository and credential access, while issue history, skills and telemetry live outside it.

A replacement run can resume useful work after a sandbox failure. It still needs newly checked authority. Persistent knowledge does not imply persistent permission.

Instrument enough to reconstruct the request, evidence, tools, outcome, evaluator and versions. Trace agents changing the system as well as agents serving users.

Calibrate evaluators on human-labeled cases, reproduce failures and inspect paired regressions. A proposed fix or pull request remains a proposal until accountable review permits release.

Prime Intellect's learning progression reinforces preserving corrections and evaluation assets before pursuing routing or specialized training. The durable contribution is a verified learning loop, rather than a confident automatic diagnosis.

That changes which skills become most valuable as code becomes easier to produce.

---

# 25_connected_fluency

Laurie Voss's product-engineer argument follows the bottleneck from code creation into review, operations and security. The responsibility is to understand what users need and define work they can accept.

Southbridge illustrates semantic fluency. Row counts can survive while dates disappear, negative signs lose meaning or categories change. Multiple models can agree because they share the same wrong convention.

Learn the entity, grain, period, units and source rules well enough to challenge a plausible answer. Turn professional corrections into definitions, cases and maintained instructions.

Monzo's described Slack entry point, internal gateway and sandbox show the surrounding product work. Familiar distribution and supported execution can matter as much as a polished prompt. Task volume and merged pull requests establish use; quality and review effort need their own measurement.

Capital One's argument helps decide where to apply rigor and how to reduce its cost.

---

# 26_lifespan_and_consequence

Capital One's disposability argument considers consequences, dependencies, replacement cost and maintenance burden. It is a conceptual argument, not evidence that the company deployed a particular disposable-software program.

A small one-use helper can become a shared process with downstream users. Revisit the checks when that happens. Calling a tool temporary does not stop a consequential mistake.

Make the dependable path cheap: standard choices, reusable fixtures, fakes and quick feedback. A complete working slice with checks can be simpler than an elaborate system whose verification is deferred.

Match acceptance to the consequence. A report needs current evidence and a usable saved artifact. A financial action also needs authorization and recovery. Code generation speed and another model's confidence do not settle either decision.

A bounded learning project lets us practice those responsibilities without committing to a large platform effort.

---

# 27_bounded_learning_experiment

Choose one historical task whose completed work a practitioner recognizes. Preserve the input snapshot and allowed tools, and establish the baseline before changing anything.

Write a few exact checks, a short expert rubric and one consequential behavior expectation. Test one hypothesis: remove a skill, narrow context or repair a tool incentive. Keep assessment separate from the cases used to tune the change.

Add a missing-evidence variant and a next-period memory case. Repeat when variation could change the conclusion. Inspect failures and disagreements as well as the mean.

The output is a learning packet: the trace, comparison, review effort, current artifact and decision to continue, revise or stop. It develops product judgment, debugging and evaluation together.

This is a proposed exercise, not production approval or a Fidelity project commitment.

We can now reduce the conference's return to three connected decisions.

---

# 28_three_decisions

The first decision is acceptance: name the professional, the work product and the conditions that make it useful. Include corrections and total effort.

The second is evidence: preserve meaning, period, source version, access and calculation through the final artifact. Give memory an aging and correction policy.

The third is controlled improvement: choose one failure mechanism and a bounded comparison. Assess the final result, consequential behavior and permission to act separately.

The company mechanisms make these decisions tangible. Their reported outcomes remain scoped to their accounts. Preserve the case, correction and reasoning so the next engineer starts from evidence rather than rediscovering the same lesson.

I will close with one prompt to choose the most useful discussion.

---

# 29_discussion

Which one failure would most change your confidence in a workflow you know, and what comparison would test it?

Take a moment to choose a specific case: an unsupported number, a wrong period, an unauthorized action or an exception that ordinary review might miss.

For discussion, we can name the accepted output, existing baseline and evidence that would change the decision. If a prerequisite is missing, identifying it is a useful result too.

There is no need to choose a favorite framework or make a project commitment today. The useful outcome is a clear uncertainty and a practical way to investigate it.

Open discussion; use the technical questions in the companion notes as needed.

---

# 30_implementation_checklist

This shared contract connects responsibilities that are often evaluated separately. Task specifies the user, accepted work, baseline and acceptance decision. Evidence keeps entity, period, units, source version, cutoff and access reproducible. Authority distinguishes resources, proposals, approvals and execution. Evaluation names cases, rubric, blockers and calibrated judges. Operation preserves versions, traces, accountable ownership and stop or rollback conditions. The inspection questions make compliance observable: can someone recognize completion, reproduce a claim, challenge a denial boundary, detect a severe false pass, diagnose a failure and verify a repair? Retain disagreement and accepted limits. A new source, user group, tool or permission can change exposure without a prompt change, so reassess when uncertainty could alter the decision. The checklist is a proposed synthesis.

---

# 31_company_mechanism_map

Thirty-seven later-source briefs add practitioner mechanisms to the original company research. Compare the work, the professional’s role and the evidence—not a league table of AI maturity.

Compare like work with like. Direct wealth accounts now include Range’s expert skills, Arca’s event-driven work and Perpetual’s compiled plans. Apollo/Redding Ridge adds source reconciliation and QA. These stories explain operating mechanisms while preserving the professional decision and the scope of each example.

Distinguish mechanism from effectiveness. A detailed architecture explains how a system is intended to operate. Production use shows operational adoption. Neither alone establishes quality, net time saved or causal business impact. Ask what baseline, task mix and human effort would support the stronger claim.

Use the atlas for follow-up. The full reading-mode atlas retains 25 firm perspectives, source links and case limits. Use it to find a relevant peer pattern, then investigate the missing implementation detail or measurement. A company affiliation alone does not establish deployment of every discussed technique.

The selected map connects Bridgewater, Kepler and Citadel Securities with time-scoped evidence, fact resolution and changing beliefs. Range, Arca, Perpetual and Apollo connect expert methods with handoffs, compiled plans and QA. Basis, Ramp and Vals supply behavior checks, roll-forward worlds and accepted-work evaluation. Two Sigma, Bloomberg and Credit Karma connect identity, scope, runtime controls and recoverable state. Arize, Sonar, Capital One and Monzo connect durable learning, shared verification and supported delivery. The reading edition contains thirty-seven later-source briefs; these examples are not a firm ranking.

---

# 32_versioned_eval_spec

The illustrative evaluation schema links the draft-review-packet task, approved input snapshot, accepted output, critical unauthorized-access and unsupported-number failures, case slices, evaluator, baseline comparison and accountable owner. It is a compact discussion specification rather than a runnable framework. Define output and action limits and when to clarify or abstain; correctly refusing access can succeed while unauthorized access fails. Version the evaluator’s model, prompt, rubric and threshold as well as the agent, because reported quality can move without a system change. Recalibrate important decisions on reviewed cases when the evaluator or users change. Model selection, reducing human review and expanding execution authority require different evidence. Finite tests support a scoped judgment with known limits, not proof of zero failure.

---

# 33_typed_claim_contract

The synthetic AsterCo contract preserves a growth ratio rather than a floating number. It identifies the entity, annual-revenue-growth metric, fiscal twenty twenty-five period, ratio unit, value of zero point two, hundred and hundred-twenty inputs in millions of US dollars, March first cutoff and calculation. A revenue value of one hundred twenty million and a growth value of twenty percent have different meanings and units. Retain document, passage, version and available-as-of identity for each input; publication, reporting period and access answer different questions. When an input is superseded, update dependent claims, tables and charts while preserving earlier values and reasons. Check that export keeps units, periods and links. These exact fields are proposed requirements, not verified Kepler or Bridgewater coverage, and all AsterCo data is invented.

---

# 34_passk_and_deployment

Pass-at-k asks a benchmark question: did at least one of k sampled candidates meet the specified test, summarized over tasks? State the workload, test and attempt budget. Ground-truth recognition can behave like an oracle and does not demonstrate that the first candidate succeeds or the operational selector finds the usable one. Run the actual verifier, ranker or human-review process and measure chosen-output acceptance, missed defects, rejected useful candidates and first-attempt behavior while enforcing critical conditions. Include all candidates, tool calls, verification, review and latency when comparing budgets. More attempts can create opportunity while increasing cost and exposure. Keep partial-credit task quality, pass-at-k and selected-output reliability distinct. Chen and colleagues supply this metric and selection distinction, not a finance performance result or a general retry policy.

---

# 35_measurement_contract

Use acceptance rate and full cost per accepted task together. Acceptance rate divides accepted outputs by eligible assigned tasks and shows rejected, excluded and abandoned outcomes. Unit cost divides total workflow cost, including failed attempts, verification, retries, review and rework, by accepted tasks. Capacity compares accepted work per professional effort or time at equivalent quality and task mix, including preparation, correction, evidence checking, approval and follow-up. Business impact needs an additional credible alternative and attention to selection and other drivers; faster accepted work is a process result rather than automatically causal revenue or investment return. Contour’s roughly three-month tracking account lacks captured sample, assignment, controls and causal estimates. It motivates the comparison but does not define a universal validation window or a verified benefit.

---

# 36_questions_for_followup

Later sources replace several early ambiguities with concrete methods. Keep similarly named talks and different evidence classes separate, and identify the exact test needed for any stronger claim.

Clarifications worth keeping. Bridgewater supplies a precision@10 account and the proactive direction; Range supplies owner/reviewer responsibilities; Kepler retains final verification. Vanguard’s time claim concerns legacy-code research. These clarifications improve the teaching without proving business outcomes.

Editions are not interchangeable. Ryan Stevens’s eval article differs from Alexander Shevchenko’s Ramp keynote. Kepler’s breakout differs from its next-day follow-up. Range’s online index label differs from its attendance placement. Preserve the identity and date of the evidence used.

Ask a bounded follow-up. Banking affiliation and terminology, exact retrieval defaults, provider spelling and several result denominators remain open. Ask for the source, workload, population and comparison needed to resolve the claim. Do not manufacture a threshold or calibrated risk formula.

The recording review clarifies Bridgewater precision at ten and proactive participation, Range skill ownership and separate review, Kepler final post-processing, and Vanguard mainframe-code research. Keep the two Ramp sessions and two Kepler editions distinct. Range’s online index label and attendance date remain separately recorded. Banking affiliation and terminology, provider spelling, exact retrieval defaults and several result denominators remain unresolved.

---

# 37_sources

The review screened ninety channel uploads and inspected fifty official video descriptions, alongside selected transcripts from the organizer’s fifty-two-session archive. Links on this page lead to primary source accounts. A description does not establish an unobserved demonstration, and a speaker report is not independent result validation. Original attendee notes, historical firm disclosures, the metric paper and proposed teaching examples retain their separate boundaries.

Proving Alpha: Showcasing AI's Value in Fundamental Investing is available at https://ai.engineer/nyc/2026/schedule?session=ae273f0b-db0f-4638-8ae3-05874bebf9ca.

We Let Our Financial Planners Write the Agents is available at https://ai.engineer/nyc/2026/schedule?session=9b002687-09cf-42e2-9282-532ed9d0c184.

Building the Next Chapter of AI in Finance is available at https://ai.engineer/nyc/2026/schedule?session=02f94835-c29d-4cf5-b77a-c5a491b747b8.

Coatue · A Hedge Fund as a Function is available at https://ai.engineer/nyc/2026/talks/coatue.

Apollo / Redding Ridge / Rowspace · AI in Practice: An Inside Look at Apollo's Approach is available at https://ai.engineer/nyc/2026/talks/apollo-rowspace.

Range · We Let Our Financial Planners Write the Agents is available at https://ai.engineer/nyc/2026/talks/range.

Vault: Making Unstructured Data Work for Investing is available at https://ai.engineer/nyc/2026/schedule?session=a84ca3a8-cc2f-4b50-a635-fc380f6f04f6.

Balancing Acceleration and Safety for AI Agents is available at https://ai.engineer/nyc/2026/schedule?session=73badd10-6f8c-4c95-b5e7-55fc3d7bafc1.

Compound value from building Monzo’s in-house agent using LLMs* is available at https://ai.engineer/nyc/2026/schedule?session=58fe4b11-571e-4afd-bd89-8ad63e6cfe11.

Scaling AI with P&L on the line is available at https://ai.engineer/nyc/2026/schedule?session=272a7ef0-4b78-41a3-813d-a67361fcd2d3.

Bridgewater · Vault: Making Unstructured Data Work for Investing is available at https://ai.engineer/nyc/2026/talks/bridgewater.

Wells Fargo · Wells Fargo Foundation Model: Application to Fraud Detection at Scale is available at https://ai.engineer/nyc/2026/talks/wells-fargo.

Blackstone / Norm.ai · Built to Scale: Future-Proofing Your Technology Roadmap is available at https://ai.engineer/nyc/2026/talks/blackstone-norm.

Morgan Stanley Wealth Management · Debrief launch is available at https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch.

UBS · fourth-quarter/full-year 2024 results is available at https://www.ubs.com/global/en/media/display-page-ndp/en-20250204-4q24-quarterly-result.html.

RBC · 2025 Investor Day presentation is available at https://www.rbc.com/investor-relations/_assets-custom/pdf/investorday2025_presentation.pdf#page=95.

RBC · 2025 Investor Day transcript is available at https://www.rbc.com/investor-relations/_assets-custom/pdf/investorday2025_transcript.pdf#page=20.

Arca · Inside Arca’s long-horizon agents that run the business is available at https://ai.engineer/nyc/2026/talks/arca.

Perpetual · Building Reliable, yet Smart Workflows for Finance, Wealth and Insurance is available at https://ai.engineer/nyc/2026/talks/perpetual.

Contour Asset Management · Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management is available at https://www.youtube.com/watch?v=ZMZlAn6Pyfg.

Jellyfish · Tokens Are the Cheap Part is available at https://ai.engineer/nyc/2026/talks/jellyfish.

Intuit Credit Karma · Paving the Road to Production: Governed Enterprise AI Agents is available at https://ai.engineer/nyc/2026/talks/credit-karma.

Ramp · Alexander Shevchenko keynote · Chasing capabilities while waiting for the frontier is available at https://ai.engineer/nyc/2026/talks/ramp.

Can Your AI Analyst Keep a Secret? is available at https://ai.engineer/nyc/2026/schedule?session=88f71c9f-f0a9-4f42-96c0-0e1492bad1c2.

Do Not Let Models Invent Numbers is available at https://ai.engineer/nyc/2026/schedule?session=2d29f925-f16b-41b3-8086-de0524829cbe.

Citadel Securities · Your Company Has No Model of Itself: Bootstrapping a World Model from Slack, Decks and Meetings is available at https://ai.engineer/nyc/2026/talks/citadel.

Kepler · October 14 follow-up · Why Wall Street Still Doesn’t Trust AI is available at https://ai.engineer/nyc/2026/talks/kepler-14.

Kepler · attended breakout release · Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler is available at https://www.youtube.com/watch?v=dZgA6btnb_s.

OpenAI · Building the Next Chapter of AI in Finance is available at https://ai.engineer/nyc/2026/talks/openai.

Compound AI · Towards Autonomous Analysts in Finance is available at https://ai.engineer/nyc/2026/talks/compound.

Building Better Agents Through End-to-End Evals is available at https://ai.engineer/nyc/2026/schedule?session=4607dbbe-8f94-4b0e-91ce-257d1cfb5448.

1,368 AI Failures: What They Teach Us About System Evals is available at https://ai.engineer/nyc/2026/schedule?session=9d72d7ac-a2a2-42cf-b880-5859316d840c.

From Agent Prototype to Production in Regulated Banking is available at https://ai.engineer/nyc/2026/schedule?session=e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa.

Vals AI · Beyond the Model Card: The Jagged Frontier of AI in Finance is available at https://ai.engineer/nyc/2026/talks/vals.

Ramp · Ryan Stevens written follow-up · Ramp · Ryan Stevens written follow-up is available at https://dev.to/dailycontext/building-better-agents-through-end-to-end-evals-pgh.

Basis · Process Supervision for Agents That Do Long-Horizon Work is available at https://ai.engineer/nyc/2026/talks/basis.

Air Canada · Nathanael Weill · How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada is available at https://www.youtube.com/watch?v=c_SPW__jF9w.

From Human Review to Self-Healing Agents: How Upstart Evaluates Voice AI at Regulated-Lending Scale is available at https://ai.engineer/nyc/2026/schedule?session=ece6925c-c979-483f-bd40-51eacdbbe11b.

Chen et al. · Evaluating Large Language Models Trained on Code is available at https://arxiv.org/html/2107.03374v2.

What does an AI engineer do? is available at https://ai.engineer/nyc/2026/schedule?session=b2ed4456-5671-4e8e-83fd-684c012fef8c.

Arize · Sofia Jakovcevic · Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI is available at https://www.youtube.com/watch?v=v5tm5EAzsAs.

Omni Analytics · Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics is available at https://www.youtube.com/watch?v=A3FL_zTQKU0.

Google DeepMind / Kaggle / LinqAlpha · Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha is available at https://www.youtube.com/watch?v=aVbRSIQO2dE.

Arize · Aparna Dhinakaran · What does an AI engineer do? is available at https://ai.engineer/nyc/2026/talks/arize.

Stop turning your Humans Into APIs for your Agents is available at https://ai.engineer/nyc/2026/schedule?session=ac709f86-ce51-4582-a680-70449c32d29c.

Coinbase · Trusting Agents in Policy-Driven Workflows is available at https://ai.engineer/nyc/2026/talks/coinbase.

Two Sigma · Balancing Acceleration and Safety for AI Agents is available at https://ai.engineer/nyc/2026/talks/two-sigma.

Bloomberg · Security in the Age of AI: Recent Attacks, Incidents & Defenses is available at https://ai.engineer/nyc/2026/talks/bloomberg.

The Machine that Changed the World, vAI is available at https://ai.engineer/nyc/2026/schedule?session=4add802c-6a68-4e9c-93fb-9c1e017193bc.

Sonar · The Machine that Changed the World, vAI is available at https://ai.engineer/nyc/2026/talks/sonar.

Capital One · Does Code Quality Even Matter? is available at https://ai.engineer/nyc/2026/talks/capital-one.

No Cash Left Behind: Vanguard's Ledger Modernization Journey is available at https://ai.engineer/nyc/2026/schedule?session=1779b934-d67b-45e9-ba11-0b19efac4b7e.

Vanguard · AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard is available at https://www.youtube.com/watch?v=uA4ah-dVHvU.

Prime Intellect · Self-Improving Organizations is available at https://ai.engineer/nyc/2026/talks/prime-intellect.

Arize · Laurie Voss · AI Writes the Code. So What's Left for Engineers? - Laurie Voss, Arize AI is available at https://www.youtube.com/watch?v=kspZP5BgkEU.

Southbridge · Just-in-Time Ontologies is available at https://ai.engineer/nyc/2026/talks/southbridge.

Monzo · A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo is available at https://www.youtube.com/watch?v=adfw3xJBx1o.

Does Code Quality Even Matter? is available at https://ai.engineer/nyc/2026/schedule?session=5191589c-a70e-4806-99dc-86f7794f46b9.

Chasing capabilities while waiting for the frontier is available at https://ai.engineer/nyc/2026/schedule?session=caecd5f6-b352-4868-a995-f0f71679caf0.

Turning AI Into Operating Margin: A Field Report from Private Equity is available at https://ai.engineer/nyc/2026/schedule?session=5049757d-8a2e-46fd-9d7b-c8c1f3d7b72a.

AI in Practice: An Inside Look at Apollo's Approach is available at https://ai.engineer/nyc/2026/schedule?session=44e9d04a-e8b4-418c-8a85-02fbb9263dd0.

Wells Fargo Foundation Model: Application to Fraud Detection at Scale is available at https://ai.engineer/nyc/2026/schedule?session=1c25f303-f38f-450b-862d-669fdbab5f82.

Intent Based Auth is available at https://ai.engineer/nyc/2026/schedule?session=e65f74f9-2174-406d-bd32-2d7073eb677d.

Your Company Has No Model of Itself: Bootstrapping a World Model from Slack, Decks and Meetings is available at https://ai.engineer/nyc/2026/schedule?session=bf371da6-6ef6-42ec-865f-5de4974a9114.

Inside the Fable War Room is available at https://ai.engineer/nyc/2026/schedule?session=6b92fb75-064e-4cb5-8aa3-7c7f211e7420.

Trusting Agents in Policy-Driven Workflows is available at https://ai.engineer/nyc/2026/schedule?session=ee927042-2ba1-44c3-b304-d001ae247839.

Developer Docs as Knowledge Infrastructure for Fintech is available at https://ai.engineer/nyc/2026/schedule?session=d3d8c80e-84b7-4106-b8b5-ca63bc508480.

Building the Financial Account for Agents is available at https://ai.engineer/nyc/2026/schedule?session=bc4b6b4a-cf07-4326-8276-fcf845da0284.

Security in the Age of AI: Recent Attacks, Incidents & Defenses is available at https://ai.engineer/nyc/2026/schedule?session=01982251-7fdc-4828-8520-fb34b9bc7564.

CTO, Blackstone is available at https://ai.engineer/nyc/2026/schedule?session=4cf641ef-436a-4e59-bd73-8a1988d8214c.

Head of AI & AI Engineer, Coatue is available at https://ai.engineer/nyc/2026/schedule?session=9a9dfcd0-459f-43eb-b3f8-004864b4ad2a.

Arca’s agent runtime for long horizon financial services work is available at https://ai.engineer/nyc/2026/schedule?session=75bd85ed-b49d-41f6-98e1-7a22853c18ab.

Shipping like a startup, regulated like a bank is available at https://ai.engineer/nyc/2026/schedule?session=2a07765d-fe3a-48df-be0f-75c111dbee6a.

UBS · Innovation and AI is available at https://www.ubs.com/global/en/our-firm/what-we-do/technology/innovation-and-ai.html.

Asset-management strategy · Sid Pednekar · Everyone Has AI. Who Has the Advantage? is available at https://ai.engineer/nyc/2026/talks/sid-pednekar.

Failure study · New York Life affiliation · 1,368 AI Failures and What They Teach About Evals — Vishal Srivastava, New York Life & Tanmay Sah is available at https://www.youtube.com/watch?v=mMw3arwQsL0.
