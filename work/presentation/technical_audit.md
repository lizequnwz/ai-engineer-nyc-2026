# Presentation technical audit

Reviewed `outputs/ai-engineer-nyc-2026-presentation.html`, its reader-facing HTML text, `work/presentation/deck-data.json`, and the rendering logic. Scope included slide visuals, reader notes, and speaker notes. Filesystem/DOM inspection only; no browser navigation.

## Two teaching corrections

1. **P2 — Arithmetic rubric partly conflates calculation with source selection.** Slide `evals-02` correctly teaches that `$8,000 − $5,500 = $2,500` can be valid arithmetic on a superseded input. Its full reader rubric nevertheless calls arithmetic score 0 a “wrong result” and score 2 “correct operands, calculation, and result.” Readers could reasonably grade the stale-source answer as an arithmetic failure, undermining the dimension separation. Define this row as calculation correctness/inspectability **given the stated operands**, and leave current/approved operand selection to source validity. Final task acceptance should still require the correct current inputs and output. Alternatively, rename the row “Numerical answer correctness” and adjust the speaker explanation; the first option preserves the intended lesson better.

2. **P2 — `denied_access` is ambiguous in the critical-failure contract.** Appendix `appendix-eval-spec` shows `critical: [denied_access, unsupported_number]`, while its reader notes describe critical failures. Refusing an unauthorized request should normally be a passing control outcome. Rename the failure to `unauthorized_access` or explicitly distinguish a denied-access **test case** from an access-control **failure**. The core release-gate slide already uses the correct unauthorized-action concept.

## Checks passed

- Synthetic cash-flow arithmetic is correct: current `$8,000 − $6,000 = $2,000`; superseded `$5,500` yields `$2,500`. All values, rubric conditions, and outputs are explicitly synthetic, without company-performance attribution.
- The grounding example is internally consistent: invented final FY2025 revenue 120 versus FY2024 revenue 100 yields 20%; superseded 118 yields 18%. Source publication dates precede the stated March 1, 2026 cutoff. No real company result is implied.
- Judge matrix orientation is correct: rows are judge pass/fail; columns are human accept/reject; top-right is false pass and bottom-left false failure. Reader notes appropriately avoid treating human labels or blanket fail-leaning behavior as infallible.
- Standard `pass@k` is correctly distinguished from first-attempt reliability and deployed answer selection. The three-attempt strip is explicitly a synthetic single-case illustration, not an empirical rate. Retry, verification, selection, latency, and review costs remain separate.
- Paired ablations hold cases, snapshots, rubric/evaluator, and attempt policy fixed where feasible. Notes call for repeated assessment of stochastic behavior and separate tuning cases from final assessment. No fake uplift, significance, or optimal skill count is asserted.
- Critical release conditions are outside compensating averages. Staged rollout, accountable judgment, finite-suite limitations, and monitoring/rollback remain explicit. The gate is an editorial proposal, not an invented bank policy.
- Independent verification is described as a designed check/evidence responsibility. It is not equated with another model agreeing, a human signing off, or independently validated company outcomes. Sonar's conceptual four-factor framing is not presented as a calibrated probability or confidence metric.
- Company metrics and maturity are appropriately bounded. Ramp's eight-to-four count remains an unverified experiment detail without invented effect size. Upstart is clearly program context and its self-improvement loops remain under development. Comet/NatWest uncertainty is preserved; Cora's deployment is not assigned to either firm. No fabricated company accuracy, ROI, throughput, or safety metric was found.
- Improvement-loop diagrams require adjudication, assessment, and scoped release; they do not imply proven autonomous self-healing.

Overall: technically sound after the two terminology/rubric clarifications above. No further material correctness or provenance issue found in this scope.
