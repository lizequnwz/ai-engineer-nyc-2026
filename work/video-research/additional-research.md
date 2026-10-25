# Additional primary-transcript findings · October 25, 2026

These are original paraphrases of the organizer's timestamped transcripts, not independent verification of company results. URLs point to the recorded session and its reading edition. Full transcripts are research inputs, not redistribution artifacts.

## Citadel Securities — institutional memory has a lifecycle

Joao Wenzel describes combining executive collateral with operational evidence, preserving a longitudinal record and distinguishing reported status from inferred status. His loop updates beliefs, ages them, observes new signals, grades prior predictions, and incorporates corrections. Historical records remain unchanged so a February snapshot can be tested against later outcomes. Missing telemetry must remain an unavailable signal rather than becoming a zero or a negative observation. Models propose record updates; code and people decide what is committed. Feedback can repair a fact or teach a reusable interpretation rule. Source access, evidence age, contradictions and sensor health therefore belong in a memory design, beyond retrieval relevance. The talk reports encouraging retrospective associations; these are not independently assessed predictive accuracy or causal business effects.

Source: https://ai.engineer/nyc/2026/talks/citadel · recording https://www.youtube.com/watch?v=jiUC6IUMdvc&t=23913s · especially 06:44:34–06:53:48.

## Credit Karma — governance and context preparation are infrastructure

Harish Gaggar walks through agent registration/deployment, workload identity, a gateway authenticating and routing tool calls, persisted execution checkpoints, and records for run summaries plus ordered trajectories. His context optimizer selects/prunes, reranks, deduplicates and compresses a payload before model submission. An Artifactory demonstration changes a reported context from 24,000 to 2,400 tokens. This illustrates a reduction in a particular demo; the transcript does not establish equivalent answer quality or a general latency improvement. Treat compression as a candidate to evaluate on required-fact coverage, final task quality, time and total review effort. Redaction is described before model calls and persistence, extending privacy controls to traces and memory.

Source: https://ai.engineer/nyc/2026/talks/credit-karma · recording https://www.youtube.com/watch?v=jiUC6IUMdvc&t=14322s · context sequence 04:23:06–04:25:56.

## Southbridge — semantic correctness needs checks that row counts miss

Hrishi Olickel separates schemas imposed by observation, storage, the decision and model assumptions. A customer has different meanings for billing, support and compliance. His examples preserve row counts or totals while losing transaction dates, misclassifying contribution categories, or removing meaningful negative signs. Multiple models can agree on the same wrong convention. The design lesson is to make decision-specific definitions explicit and check typed intermediate results, nulls, signs, categories and dates. He also separates pipeline designers, repeated workers and bounded optimization agents. These are a speaker's design argument and task examples, not proof that one ontology strategy or model ensemble is universally superior. The memorable counterexample is the date parser: agreement on row counts cannot establish that the date field survived transformation.

Source: https://ai.engineer/nyc/2026/talks/southbridge · recording https://www.youtube.com/watch?v=akEqiXFo3GM&t=14548s · especially 04:16:26–04:19:03.

## Wells Fargo — a financial foundation model need not be a language model

Freddy Lecue describes pretraining a transformer from scratch on transaction sequences, using representations for a downstream fraud classifier. The central engineering problem is encoding heterogeneous amounts, categories, channels, time and location into a manageable vocabulary. The task has an authorization-time latency constraint, a different operating regime from a minutes-long analyst workflow. The talk compares against a production XGBoost approach and reports better detection and fewer false positives; the available transcript does not expose enough dataset, slice, uncertainty or result-table detail to reproduce the comparison. The transferable lesson is to select the data representation, objective and operating budget around the actual decision. It is not a general recommendation to train a proprietary language model.

Source: https://ai.engineer/nyc/2026/talks/wells-fargo · recording https://www.youtube.com/watch?v=akEqiXFo3GM&t=5321s.

## Bloomberg — authority and memory need controls outside the model

Andrey Rybka organizes agent defenses around identity, untrusted inputs, tools, isolation, data and observability. He recommends short-lived scoped credentials, deterministic checking of tool invocations, tenant checks on queries, default-deny egress including DNS, and budgets that stop execution. Persistent memory can retain injected instructions, extending an attack beyond the original document. An agent's agreement to avoid production changes is not an enforcing control. Incident vignettes motivate the controls but are not treated here as independently verified incident reports, prevalence statistics or proof that a named defense prevents every attack. A useful team test is to try a denied tool call and verify that the executor blocks it, even if the model requests it.

Source: https://ai.engineer/nyc/2026/talks/bloomberg · recording https://www.youtube.com/watch?v=jiUC6IUMdvc&t=5361s.

## Jellyfish — delivery economics include people and quality

Steve Jamison combines salary and AI spend per merged pull request rather than judging token spending in isolation. The reported observational results include a 26% year-over-year decline in cost per merged PR despite a large rise in AI spend. Reverts and change size are inspected as counterweights to raw throughput. A merged PR is an engineering proxy, not a complete measure of customer value, correctness or maintenance burden; the talk does not establish that spending more causes better outcomes. For financial analysis, the analogous proposed denominator is an accepted, reviewable work product with agreed quality. Include review, rework, unsuccessful attempts and operating costs.

Source: https://ai.engineer/nyc/2026/talks/jellyfish · recording https://www.youtube.com/watch?v=jiUC6IUMdvc&t=17029s.

## Prime Intellect — make corrections an owned learning asset

Will Brown argues that internal corrections and repeated workflows can become evaluation and, later, training assets. He proposes a progression from workflow discovery and skills to evaluations, routing and eventually specialized training. Comparing a smaller model with a stronger model on real tasks can inform routing, but the comparison needs an acceptance standard; agreement with the larger model is not sufficient ground truth. The organization-wide continuous-learning scenario is forward-looking. The immediate transferable practice is to retain versioned tasks, feedback and adjudicated failures so future optimization can be measured rather than guessed.

Source: https://ai.engineer/nyc/2026/talks/prime-intellect · recording https://www.youtube.com/watch?v=jiUC6IUMdvc&t=25528s.
