# Industry report source and attribution audit

Audited artifact: `outputs/ai-engineer-nyc-2026-industry-report.html`.

Method: read the generated HTML from the filesystem, extracted reader-facing text excluding scripts and styles, inspected source-link targets, and compared the institutional claims and maturity wording with `work/program.json`, `work/industry_themes.json`, and the builder's structured case records. No browser navigation or visual rendering was used.

## One material issue to fix

**P2 — A vendor-reported bank example is visibly mislabeled as a practitioner perspective.** In Theme 5, the example headed **“Unnamed top global bank, described by Langfuse”** carries the badge **“Practitioner perspective.”** The source is the Langfuse speaker's abstract for **Building Deployment Gates for AI Agents in Financial Services** (`f7cd2f57-654a-4bbc-874b-ffa66a8ab3ed`), not a named bank practitioner presentation. Its text and maturity caveat correctly acknowledge this limitation, but the prominent evidence badge contradicts that distinction.

Cause: `work/build_industry_report.py` identifies vendor cases only when the classification contains “vendor” and does not contain “practitioner.” This classification contains “not a named bank practitioner presentation,” so a negated occurrence causes the wrong badge.

Required correction: label this example **Vendor-reported customer pattern** or **Vendor / adjacent case**, using explicit classification rather than interpreting a negated word. Preserve the unnamed-bank caveat. This matters because the report promises visibly distinct practitioner and vendor evidence.

## Session source validation

- All **32 distinct session IDs** appearing in official-session link targets exist in `work/program.json`.
- Every referenced session is dated **Tuesday October 13 or Wednesday October 14, 2026**. No Monday workshop or other date enters the report's session evidence.
- The source catalog's titles and speaker/company strings are generated from the same session records. No unresolved or foreign session identifier was found.
- Official session links consistently use `https://ai.engineer/nyc/2026/schedule?session=SESSION_ID`.
- External wealth-management disclosures are separately labeled as external, historical, company-reported evidence rather than NYC sessions. Their factual wording is consistent with the stored `work/wealth_context.json`; live external-page verification was outside this filesystem-only audit.

## Requested institutional checks

| Item | Result |
|---|---|
| Optiver scope fix | **Pass.** Comparison row says reported broad internal use and explicitly limits inference to engineering. The value theme now says broad daily internal engineering use. No visible claim establishes autonomous trading or causal firm-wide savings. The capability theme's “broad daily agent use” is supported by the advertised daily internal scale and does not assert all employee roles use it. |
| Arca identity | **Pass.** Theme names the speaker-linked `arcawealth.ai`; the comparison row warns against conflating similarly named firms or inferring incumbent-scale adoption. Runtime implementation is separated from deployment scale and measured automation. |
| Compound AI versus LinqAlpha | **Pass.** Compound's analyst-workflow account links to **Towards Autonomous Analysts in Finance**, presented by Yijia Liang of Compound AI. LinqAlpha's benchmark/customer claims link to **Why Frontier Models Fail on Billion Dollar Portfolios** with the LinqAlpha and Google DeepMind speakers. They remain distinct vendor examples; neither becomes a named incumbent case. |
| Wells Fargo deployment | **Pass.** Describes transaction-model development, lifecycle and transition toward production, while explicitly saying the abstract does not identify which fraud/decisioning applications are live. It also distinguishes this model category from LLM assistants. |
| Upstart remediation | **Pass.** Production voice use and human-calibrated judging are separated from automated self-improvement/self-healing loops still under development. The short maturity label and detailed theme text agree. Coval's co-presentation is identified. |
| Apollo distinctions | **Pass.** Portfolio-operations case studies link to Adam Nahari's operating-margin session. The comparison row separately includes the sparse Rowspace/customer keynote and warns against treating both as one proven platform. No measured ROI or shared platform is invented from the sparse keynote. |

## Additional material checks

- **Bridgewater:** PAT is correctly presented as reported production; the next Researcher is described as enabled rather than broadly deployed. Retrieval permissions and usage claims remain attributed.
- **Citadel Securities:** Affiliation is preserved; the report does not turn this into a Citadel case or establish firm-wide deployment of the specific state-estimation system.
- **Wise:** A built framework/control architecture is described without claiming that an LLM is authorized to move customer funds or that control effectiveness has been measured.
- **GEICO:** Explicit experiment status and annualized-versus-realized-benefit caveats are retained.
- **Vanguard:** Production migration engineering is distinguished from the narrower advertised contribution of AI tools; the whole migration benefit is not attributed to AI.
- **JPMC:** Panel participation is not represented as Keycard/AAuth adoption.
- **Blackstone and Coatue:** Empty/sparse abstracts remain watchlist evidence, with no invented use case, architecture, vendor adoption, or outcome.
- **Kepler:** Source-constrained numerical analysis is labeled vendor positioning; absolute hallucination claims are challenged rather than adopted as verified facts.
- **Pre-event status:** Hero, executive evidence banner, theme learning labels and source/limits section consistently indicate draft analysis. The report does not claim attendance or independently verified outcomes.

Conclusion: the institutional content and source selection are otherwise consistent with the supplied official program. Correct the Langfuse evidence badge before delivery.
