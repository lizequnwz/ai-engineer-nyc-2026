# Industry themes factual audit

Reviewed all eight themes, every top-level/firm-example session ID, the source abstracts, and relevant speaker records in `work/program.json`. All referenced IDs exist and map to the intended sessions. No edits made to `industry_themes.json`.

## Material findings

1. **Known attribution conflict: replace SoFi example as planned.** In `authority-and-controls.firmExamples[2]`, the company field says SoFi, but Ishween Kaur's biography says Salesforce AgentForce. The abstract supports a local/testnet payment-attack demonstration, not a SoFi production case. Substituting Bloomberg's security practitioner session avoids the conflict. Bloomberg's source supports an institutional security remit and threat/defense discussion, not a specific proven production architecture or measured defense effectiveness.

2. **Narrow Optiver's “firm-wide daily usage.”** In `value-attribution.firmExamples[2].maturity`, “Firm-wide daily usage” is broader than the abstract establishes. The source says “agents in every engineer's workflow” and discusses a few thousand people using agents daily; it does not establish daily usage by all employees or across every business function. Use “broad daily internal engineering use” or “daily agent use at internal scale.” The other Optiver passages describing the golden path, experiment funnel, telemetry, task certification, model routing, multiple channels, and self-hosted weights are supported.

## Identity checks passed

- **Compound AI is correct for `d49d49e1-90cb-4b8d-beb6-84d6560aaf04`.** Its official speaker is Yijia Liang, company **Compound AI**; his bio says Co-Founder at Compound and the website is `https://getcompound.ai/`. It is not LinqAlpha. His past Coatue role must not be converted into a Coatue deployment claim. The current theme correctly identifies it as a vendor with unnamed production-finance experience.
- **LinqAlpha is correct for `e8e53365-3c1f-4c28-bdd0-44c305a05d57`.** The source lists three LinqAlpha speakers and Google DeepMind/Kaggle Benchmarks' Janie Gu. The abstract explicitly says LinqAlpha built the benchmark with that team. Current attribution and vendor/client-evidence limitations are appropriate.
- **Citadel Securities is correct**, supported by both Joao Wenzel's company field and bio. Current wording avoids conflating it with Citadel. The theme correctly refrains from claiming quantified effectiveness or established firm-wide production of the specific state-estimation system.
- **Arca website disambiguation is supported.** Aman Singh's source record has company `Arca` and website `arcawealth.ai`. Keeping the site in the label and warning against similarly named firms is appropriate. The abstract does not establish client scale, full operational automation, or fiduciary/advice outcomes; current caveats reflect that.
- **JPMC participation is not adoption.** Current theme correctly limits this to a practitioner panel with Keycard/AAuth and disclaims bank protocol adoption/endorsement.
- **Basis is an accounting-agent vendor**, not a named wealth-manager deployment. The intermediate-behavior, tax-source, trajectory-judge, and behavior-spec claims are supported. Current deployment/outcome caveats are appropriately cautious.
- **Neo4j/Blitzy are vendor cases with unnamed financial clients.** Current theme keeps customer identities and acceleration claims conditional rather than assigning the work to a named institution.

## Maturity and inference assessment

No additional material maturity overstatements found. Bridgewater/PAT, Ramp's accounting agent, Monzo, and Upstart explicitly describe production or current use. The theme correctly separates Upstart's future self-improvement ambition from current operations; Wells Fargo's development/production transition from unspecified live applications; GEICO's experiment from established scale; Vanguard's production ledger migration from the unspecified incremental contribution of AI; and Contour's attribution process from causal alpha. Apollo's portfolio case is correctly distinguished from a uniform adviser workflow.

The learning/tips are clearly editorial synthesis and the theses consistently disclose their pre-event basis. Keep the planned separate wealth-management disclosures: these eight themes are strongest for investment firms, banks, fintechs, and adjacent financial operations, with limited direct evidence of a named established wealth manager's production deployment. The existing warning against universally autonomous advice is useful but does not by itself establish such a named case.
