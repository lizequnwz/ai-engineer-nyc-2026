# Day 1 Markdown audit

Artifact audited: `outputs/ai-engineer-nyc-2026-day-1-notes.md`.

Primary source: `/Users/charlie/.codex/attachments/0a2b5573-7b18-4c57-8baf-2a2ad8c8f5dd/Pasted text.txt`.

Also checked the supplied-notes source audit in `work/day1_source_audit.md`. This review is a filesystem-only comparison; it does not independently verify what the speakers said.

## Material findings — resolved during review

The parent regenerated the Markdown while this audit was in progress. The two initial Kepler findings below are now **resolved** in the current artifact: line 434 lists components and explicitly leaves order/boundaries unresolved; line 438 preserves the numeric settings as recorded with transcription caveats. Their initial findings are retained for the audit trail.

### P2 — Kepler retrieval settings silently resolve ambiguous units and workload

In D1-07's **What the notes record**, the output says:

> Retrieval settings recorded in the notes were 3× overfetch, 100 candidates per namespace, at most five candidates per document after reranking, and the top 20 documents for an earnings use case.

The raw record is:

> Retrieval they do 3*overfetch. 100 per name space, rerank candidates max 5 per doc, top 20 docs for earning.

The output supplies an item type for “100,” fixes a precise reranking-stage interpretation, and resolves “for earning” into an earnings use case. These are plausible readings but were not captured unambiguously. The existing caveat about workload-specific evaluation does not disclose that the transcription itself is unresolved; the final source note then incorrectly says these settings have not been silently resolved.

**Correction:** Retain the values explicitly as recorded, such as **3× overfetch; “100 per namespace”; “max 5 per doc” around the reranking step; “top 20 docs for earning” [wording unclear]**. State that the reference quantity, item types, stage ordering, and workload require confirmation. Do not represent the interpreted values as observations until clarified.

### P2 — Kepler pipeline ordering is more definite than the raw record supports

The adjacent **What the notes record** bullet presents preprocessing, language-model planning, retrieval, computation, registry, and postprocessing as one described pipeline. The raw notes separately mention “retrieval finds the source → code does the math → preprocessing filter” and “Question → LLM writes plan → tools retrieve sources … citation registry … post processing citation filter.”

Those notes support the components and some local relationships but do not establish a complete execution order or where every filter operates. Presenting the combined list as a coherent ordered pipeline hides that uncertainty.

**Correction:** Use **“Recorded components include …”**, retain supported local relationships such as model planning/tool retrieval and code-based arithmetic, and explicitly leave preprocessing/filter placement and full stage ordering unresolved.

## Coherence correction

The executive synthesis says **“Day 2 and the broader industry cases below remain agenda-based context wherever attendee notes are absent.”** This standalone Markdown contains neither Day 2 cases nor the broader industry case comparison below. Remove “below” and refer to the separate industry report, or remove the sentence here if it is needed only in a combined HTML document. This is a document-navigation inconsistency rather than an evidence upgrade.

## Checks that passed

- All seven session-note sets are represented; the closing reflection remains unattributed.
- Evidence remains **Speaker claim** throughout. Vault and Two Sigma preserve the attendee's production label; the other five remain unclear, with Contour's separate program context explicitly identified.
- Blank fields and prefilled decision questions are not treated as answered. Proposed source metadata, abstention behavior, tests, applications, and risk controls are presented as takeaways, practical tips, hypotheses, or questions rather than claimed live observations.
- The Bridgewater reactive/proactive reversal remains explicit and is not silently replaced by a definitive quote. Retrieval-precision concerns are not transformed into benchmark results or proven habit changes.
- Two Sigma's approval classifier is not declared deterministic, validated, error-free, or a measured substitute for human oversight. No measured safety/utility benefit is invented.
- Capital One's disposable-software framing is not turned into a deployed corporate policy or proven zero-cost maintenance result.
- Arize's product and skill names remain as recorded and unverified. No installation instructions or established autonomous remediation are invented.
- The expected-loss expression is kept as a recorded heuristic, with undefined terms and missing calibration disclosed. Incident growth/category claims remain attributed rather than established empirical results.
- New York Life affiliation is attached to Vishal Srivastava rather than both presenters; framework adoption at the insurer is not inferred.
- Contour's A/B language and three-month tracking window are preserved with explicit uncertainty about randomization, comparability, and causal attribution. No alpha, P&L uplift, or verified ROI is claimed.
- The “manual idea agent” ambiguity is handled cautiously; the report does not invent a named tool or autonomous investment product.
- The Socrates and sales meeting-preparation sections are explicit optional application hypotheses prompted by the user's questions, without inventing current architecture or results.
- No fabricated numeric effect size, deployment scale, accuracy rate, return estimate, or attendee-checked artifact was found.

Conclusion: the synthesis is faithful and appropriately separates editorial recommendations from captured claims. Both material Kepler ambiguity issues have been corrected and rechecked. Only the standalone “below” reference remains as a minor coherence correction.
