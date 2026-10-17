# Conference applications: evaluation review of the personal analytics agent

Reviewed `/Users/charlie/Repos/deepagents-agents/data-analytics-agent` read-only, including its AGENTS.md, execution fingerprints, runner/grader/comparator, evaluation docs, synthetic fixture generation, live tests, and focused deterministic tests. No repository changes, provider/model calls, benchmark runs, source queries, credentials, or private business data were used.

## Existing strengths to preserve

This project already implements much of the conference's evaluation advice. Do not add a second evaluation service or duplicate these paths:

- The serving execution fingerprint binds code, instructions, dependencies, settings and local source snapshots; remote contents explicitly remain unfrozen: [evaluation.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/data_analytics_agent/evaluation.py:131).
- The runner retains failed/partial outcomes and complete typed results, reports and report specifications before grading: [evaluate_documented_examples.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/evaluate_documented_examples.py:69).
- Seven independently reviewed correctness criteria already exist, with unknown evidence distinct from failure: [grade_documented_examples.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/grade_documented_examples.py:16).
- Scalar expectations can already be checked against exact Parquet result bindings; complete SQL snapshots and semantic roles are independently reviewed: [grade_documented_examples.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/grade_documented_examples.py:36), [evaluation.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/data_analytics_agent/evaluation.py:72).
- Paired trials already require fresh runs/conversations, stable inputs and versions, declared changes, boundary/first-attempt reviews, repetitions, and conversation-level bootstrap. Failures/regressions retain the baseline and missing evidence stays inconclusive: [compare_ablation.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:90), [compare_ablation.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:243), [compare_ablation.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:323).
- Temporal holdout validation and independently recomputed forecast scores already have meaningful deterministic coverage: [test_forecast_evaluation.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_forecast_evaluation.py:77), [test_forecast_evaluation.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_forecast_evaluation.py:126).

The following are incremental opportunities, ranked by practical value. Proposed success measures are acceptance ideas, not findings or guarantees.

## 1. Connect live analytical evaluations to numeric and artifact oracles

**Conference connection:** Ramp's complete-job evaluation; Kepler's separation of correct arithmetic from correct inputs; the system-evals warning that successful execution can conceal incorrect work.

**What exists:** Synthetic live capability tests invoke the complete application and retain inspectable answers. Semantic cases already support exact scalar result bindings. Forecast scoring is independently recomputed by the product and tested.

**Concrete gap:** The broad live analytical test passes forecasting/prediction/seasonality by finding words such as “baseline,” “holdout,” “mae,” or “12” in analysis descriptions and counting executions. Those words do not establish chronological separation, correct saved predictions, an actually computed baseline, or correct error values. Its descriptive test finds the expected total anywhere among numeric result cells, without checking the requested observation count or a named binding. Evidence: [test_live_evaluations.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_live_evaluations.py:140), [test_live_evaluations.py](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_live_evaluations.py:164).

**Smallest useful action:** Extend the existing live harness to check named saved-result fields and independently recomputed forecast/predictive outputs, reusing the forecast evaluator and typed Parquet binding pattern. Require total **and** count for the descriptive fixture. Check training/holdout windows, candidate/baseline scores, predictions and interval metadata from saved artifacts; separately assess whether the final report agrees. Retain keyword checks only as smoke diagnostics, not a correctness pass. Start with descriptive and forecast cases rather than adding a new generic grading framework.

**Success measure:** Seed a completed synthetic receipt with (a) correct “holdout/baseline” prose but overlapping windows, (b) a wrong metric value, and (c) a report disagreeing with the saved result. Each must fail the appropriate dimension; a valid artifact set must pass. Record numeric correctness separately from source/version selection. A finite seeded suite demonstrates detection of those defects, not general analytical reliability.

**Implementation anchors:** [check_expected_values](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/grade_documented_examples.py:36); [existing forecast score assertions](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_forecast_evaluation.py:77); [existing overlapping-window rejection](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_forecast_evaluation.py:126).

## 2. Make held-out evaluation a deliberate final assessment stage

**Conference connection:** Ramp's ablation method and the judge/system-evals cautions about overfitting to known failures and interpreting a narrow benchmark as product reliability.

**What exists:** There is a separate four-case `held_out_examples.json` corpus documented for the existing runner, plus held-out paraphrase flags inside the 40-case ablation corpus. The comparator freezes whole corpora and groups follow-up/repetition dependence correctly. Evidence: [testing.md](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/doc/development/testing.md:106), [ablation held-out case](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/fixtures/ablation_cases.json:35), [fixture coverage test](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_ablation.py:318).

**Concrete gap:** `held_out` is fixture metadata, not an enforced role in the runner/grader/comparator. The runner accepts one corpus and freezes all its cases; the comparator aggregates that corpus without separate development-versus-final slices. A separate file also cannot remain statistically held out after repeatedly inspecting it to choose prompt/skill changes. This is a benchmark-exposure gap, not a missing forecasting holdout feature. Evidence: [runner selection and manifest](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/evaluate_documented_examples.py:274), [comparator corpus pairing](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:149), [comparator case loop](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:209).

**Smallest useful action:** Use the current `--corpus` interface to separate development/regression and final-assessment manifests. Predeclare case/conversation families, fixture version and an exposure record before iteration. Keep related paraphrases/follow-ups together so one variant is not effectively rehearsing its final test. Tune on the development set; run the locked assessment only after choosing the candidate. Replace exposed final cases when beginning a new decision. Introduce additional synthetic task/data families only where the current deterministic seasonal source fails to represent the intended analytical work.

**Success measure:** A study can show which case families influenced development and which were first evaluated after candidate selection. Final results, critical failures and uncertainty are reported separately from tuned regressions; no result is called held out solely because its JSON flag is true. Preserve the existing frozen receipts and paired repetition checks.

## 3. Calibrate the human grading process before adding automated judges

**Conference connection:** Upstart's human-calibrated judges, the banking quality-vector discussion, and Sonar's warning about inconsistent grading. This project currently relies on human review; there is no need to introduce an LLM judge merely because the conference discussed one.

**What exists:** Reviews are bound to exact run/manifest/receipt hashes. The seven rubric criteria, semantic-role checks, hard-boundary checks and first-attempt checks already separate important failure modes. The comparator tests enforce unknown-evidence and regression handling. Evidence: [grade criteria](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/grade_documented_examples.py:96), [review binding](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/grade_documented_examples.py:140), [missing-review gate test](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_ablation.py:258).

**Concrete gap:** A criterion is accepted when it contains an allowed status plus any nonempty evidence string. This is appropriate for transporting human judgments but does not establish that reviewers apply the same threshold, recognize seeded critical defects, or use `not_applicable` consistently. The existing grader captures no explicit reviewer identity, independent second rating, disagreement/adjudication, or versioned descriptive anchors for pass/fail/NA. Hashing the review establishes integrity, not reviewer validity. Evidence: [grade](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/grade_documented_examples.py:62), [review checksum](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/grade_documented_examples.py:220).

**Smallest useful action:** Define concise rubric anchors and permitted NA conditions for each criterion. Make a small offline calibration pack from synthetic saved outputs containing known defects: correct arithmetic on a wrong population, fabricated units, report/result disagreement, analysis before required clarification, and a requested source-scope expansion executed without approval. Double-review a sample blind to candidate identity; retain both judgments and adjudicate disagreements. Add reviewer/rubric versions to review records, reusing current evidence/hashes. If automated judging is later useful, evaluate it against this adjudicated pack first.

**Success measure:** Report serious false passes, false failures, agreement and adjudication burden by failure class; all seeded blocker examples in the calibration pack must be caught. Keep an expected denied action distinct from an actual unauthorized action. Do not claim universal calibration or zero risk from a small pack. Hard-boundary outcomes continue to block adoption independently of speed.

**Existing boundaries to preserve:** [metadata/clarification data-access checks](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/grade_documented_examples.py:68), [candidate hard-boundary failure gate](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:243), [cross-source artifact resolution test](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/tests/test_artifact_handoff.py:384), [untrusted file-cell policy](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/AGENTS.md:7).

## 4. Measure accepted-work cost alongside tokens and latency

**Conference connection:** Contour's cost-per-useful-insight and counterfactual questions; Optiver's task-qualified routing and inference economics. A faster or lower-token result can still require more review, repairs, or rejected attempts.

**What exists:** Diagnostics already collect model/tool calls, input/output/cached/reasoning tokens, active and elapsed time, approval waits and agent breakdowns. Missing usage is deliberately unknown, and the comparator suppresses performance on incomplete or unreviewed outcome pairs. Evidence: [TokenUsage](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/data_analytics_agent/schemas.py:259), [RunDiagnostics](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/data_analytics_agent/schemas.py:280), [missing-usage validation](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:28).

**Concrete gap:** The comparator explicitly returns `paid_cost: None` and `warehouse_query_count: None`; its target metrics are latency/tokens/calls rather than full accepted-task cost. Approval waiting time is not active reviewer labor. The saved outcome report does not measure the effort to review, repair and accept a result. Evidence: [supported metrics](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:17), [explicit unknown costs](/Users/charlie/Repos/deepagents-agents/data-analytics-agent/scripts/compare_ablation.py:371).

**Smallest useful action:** Add a dated, offline cost calculation to the existing comparison artifacts using recorded per-model token categories and known rates, or import provider-reported charges when available. Label estimates and reconcile them separately from paid cost. Capture active review/rework time in the review file. Summarize all attempts—including failed/rejected work—over accepted tasks at the same quality, without including failed trials in the speed estimator. Leave missing charges/tool/warehouse costs unknown; do not replace them with zero or alter production routing as part of measurement.

**Success measure:** A comparison reports quality-qualified task acceptance, total known/estimated provider cost, reviewer minutes, retry/rework burden and unknown-cost share. Two variants are compared on the same work and acceptance rules. Any cost-reduction claim reconciles its numerator and denominator and cannot hide rejected attempts. No model-price recommendation or current cost estimate is implied by this review.

## Recommended first increment

Start with **one live-output correctness oracle** using the existing descriptive/forecast fixture, then establish the grading calibration pack. These improve confidence in every future ablation before spending on a larger study. Keep the existing runner, immutable receipts, paired comparator, explicit hard-boundary gates and conservative inconclusive decisions. Freeze final-assessment practice and cost accounting as the next layers; no new provider runs are authorized by this review.

## Separate transfer note: Fidelity's current SQL evaluation

This section responds to the user's description of a **different system**. It is not a claim about the personal repository reviewed above. The user reports a one-shot SQL agent with row-count comparison plus an LLM judge over returned data; definitions are rejected, conversation is unsupported, and roughly 20–30K tokens of semantic context contribute to reported 30–45-second model latency. These are user-reported baselines, not independently measured findings.

### Replace row-count agreement with precise result-equivalence grading

A wrong filter, join, measure or group can preserve the row count. Keep row-count agreement as one diagnostic, then deterministically compare the full generated-query and independently reviewed reference outputs on the **same frozen data/as-of snapshot**:

- Predeclare expected columns, business measure, population/filter/time scope, units and grain. Compare named business keys where the result has stable keys; explicitly check key uniqueness and group coverage.
- Compare ordered rows only when ordering is part of the task. Otherwise compare keyed rows or row multisets. Preserve duplicate multiplicities; converting to a set can hide fan-out and duplicate-row defects. For top-k work, define ordering and tie treatment in the task contract.
- Use null-aware comparison: NULL is not zero, empty string or a missing row. Normalize permitted representation differences such as declared decimal/date types without erasing substantive differences. Handle timezone/as-of boundaries explicitly.
- Use agreed column-specific absolute/relative numerical tolerances and exact comparison for keys/categories/counts where appropriate. Monetary precision, rounded percentages and approximate aggregates may need different rules; do not choose tolerance after seeing the candidate error.
- Keep **execution success**, **result equivalence**, **scope/grain validity**, and **critical policy conditions** as separate outputs. A reference SQL string is not the only valid implementation, and a matching result on one snapshot does not prove semantic equivalence for every possible dataset.
- Validate the gold query/output itself independently and add synthetic contrast cases where plausible wrong joins, filters or dates yield a different answer. A single reference can also contain a mistake.

Use an LLM judge for the remaining semantic rubric—whether the chosen interpretation, assumptions, explanation and limitations match the business task—not as the primary grader of full numerical results. Calibrate it against human-adjudicated cases, inspect serious false passes and judge variability, preserve disagreements, and version the rubric/judge. Deterministic grading should inspect complete results outside the model; do not ask a sampled table preview to establish full-result equality.

**Suggested success measure:** known synthetic wrong-scope/wrong-grain/same-row-count/duplicate/NULL/date-boundary cases fail the appropriate dimension, while valid reordered or aliased equivalent results pass under the contract. Report equivalence by task slice and preserve human-adjudicated exceptions. Do not advertise zero risk from the finite suite.

### Evaluate bounded SQL repair before claiming a benefit

A bounded repair experiment can preserve the one-request experience: generate → validate/execute read-only → inspect actual error or contract violation → repair within a declared attempt/time/token budget → finish or return an explicit failure/clarification outcome. Feedback must come from real execution/validation evidence, **not from the held-out gold answer**. Preserve scope and permission boundaries across every attempt; the loop is not authority to expand access.

Compare the current one-shot baseline with the bounded loop on paired, frozen cases and fresh repetitions. Measure:

- First-attempt result-equivalence rate and within-budget accepted completion.
- First correct result, actual repair count, and unresolved/clarification rate; repairs that merely execute are not automatically correct.
- End-to-end p50/p95 latency, separating semantic retrieval, model time, SQL validation/database time, retries and user waiting.
- Full tokens/cost across all attempts per accepted result, plus any review burden.
- Unauthorized access/action attempts, scope changes, incomplete-source use, and new regressions as independent blocking conditions.

The reported long semantic context also suggests testing task-scoped context selection or role-based batching as an **isolated comparison**, with required-entity/definition coverage and result equivalence as guards. Do not reduce context and add a repair loop in the same first experiment; that would obscure which change caused the outcome. No percentage speedup or accuracy gain is established without those comparisons.
