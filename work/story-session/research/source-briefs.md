# Source briefs: Engineering reliable and useful financial AI

Reviewed October 27, 2026. Five complete original-release English auto-generated transcripts were extracted and reviewed. No audiovisual viewing or independent validation of company results is claimed.

## Kepler: Do Not Let Models Invent Numbers

Vinoo Ganesh · [Original recording](https://www.youtube.com/watch?v=dZgA6btnb_s)

**Source application: Kepler financial-research assistant.** Retrieval-augmented financial answers and reports with inspectable sources and calculations.

**Case context.** A retrieved filing contains 17. Without unit, scale, period, and location, it could mean millions of yen, dollars, an older reporting year, or the page number. Attaching a source after generation does not settle the financial meaning.

**Mechanism.** Ganesh describes language-model planning, source retrieval, typed facts with registered anchors, predetermined human-written calculation code, and a post-processing citation filter. The filter resolves numerical claims against registered evidence and strips unsupported output. Some cases attempt citation repair, whose complete method is not disclosed. The model can still hallucinate; the architectural claim concerns what reaches the user.

**Evidence limits.** This is Kepler’s account of its architecture. No universal correctness guarantee was independently tested. The talk reports 10,981 rejected citations and about 3,810 wrong numbers without a denominator or sufficiently specified evaluation protocol. These cannot become a comparative RAG error rate. Garbled caption counts and retrieval settings are omitted. The generalizing aside about banking/sales accuracy is not adopted.

**Our application.** Our inference: preserve entity, metric definition, period, unit, actual query result, and derivation through final narration. A verified number does not validate the surrounding commercial interpretation. Our A17 example is invented, not a Kepler implementation or production incident.

- [03:12 · The ambiguous 17](https://www.youtube.com/watch?v=dZgA6btnb_s&t=192s)
- [04:02 · Planning, retrieval, human-written calculation, filtering](https://www.youtube.com/watch?v=dZgA6btnb_s&t=242s)
- [06:03 · Adjusted EBITDA and the context of a fact](https://www.youtube.com/watch?v=dZgA6btnb_s&t=363s)
- [08:31 · Typed facts](https://www.youtube.com/watch?v=dZgA6btnb_s&t=511s)
- [14:39 · Citation registry and final-output filtering](https://www.youtube.com/watch?v=dZgA6btnb_s&t=879s)
- [18:15 · The model can still hallucinate](https://www.youtube.com/watch?v=dZgA6btnb_s&t=1095s)
- [18:44 · Inspect source and calculation](https://www.youtube.com/watch?v=dZgA6btnb_s&t=1124s)

Local caption: `transcripts/kepler.txt`. Acquisition method and checksum: `sources.json`.

## Bridgewater: How Bridgewater Turned 100 Million Documents Into an Edge

Sam Green and Aaron Linsky · [Original recording](https://www.youtube.com/watch?v=CLve4Nx_RwI)

**Source application: Bridgewater Vault.** Shared unstructured-research corpus and search platform for both human researchers and agents.

**Case context.** In an October demonstration about AI investment and the Korean won, a public chat response includes older July research. Vault supplies explicitly time-scoped evidence. Later, an improved search engine still does not make researchers visit every morning. Their working routine remains email subscriptions and folders.

**Mechanism.** Bridgewater distinguishes high-signal human search from broader agent retrieval. The team describes time/source/asset filtering, authorized information, a roughly 200-question manually labeled relevance set, and reported precision@10 improvements from about 60% to 90–95%. They bring familiar subscriptions into saved searches and folders into collections, then introduce cross-corpus questions, feeds, and agent work. A research workbench and returning findings to the shared corpus are further described directions.

**Evidence limits.** The Korean-won comparison is a demonstration, not a controlled accuracy study. More sources do not prove correctness. Precision@10 is document relevance among the top ten, not answer accuracy or ROI. No held-out protocol is disclosed. The habit change is the speakers’ explanation of product fit, without a measured adoption uplift. Avoid saying nobody used Vault. The title’s corpus scale does not establish retrieval quality.

**Our application.** Our inference: current to what date, relevant to which question, and available in whose actual working routine? For meeting prep, combine temporal evidence with an entry point in the salesperson’s existing workflow. For text-to-SQL, select task-relevant semantics while preserving required definitions and joins. Our mock inbox and brief are original explanatory reconstructions.

- [04:14 · Korean-won evidence comparison](https://www.youtube.com/watch?v=CLve4Nx_RwI&t=254s)
- [07:15 · Human and agent readers](https://www.youtube.com/watch?v=CLve4Nx_RwI&t=435s)
- [08:19 · Labeled search benchmark and precision@10](https://www.youtube.com/watch?v=CLve4Nx_RwI&t=499s)
- [11:35 · The inbox and the adoption turn](https://www.youtube.com/watch?v=CLve4Nx_RwI&t=695s)
- [14:05 · Proactive workbench](https://www.youtube.com/watch?v=CLve4Nx_RwI&t=845s)
- [15:44 · Findings return to the corpus](https://www.youtube.com/watch?v=CLve4Nx_RwI&t=944s)

Local caption: `transcripts/vault.txt`. Acquisition method and checksum: `sources.json`.

## Contour Asset Management: Proving Alpha: How a Hedge Fund Measures AI’s ROI

Hari Kumar · [Original recording](https://www.youtube.com/watch?v=ZMZlAn6Pyfg)

**Source workflow: Contour’s AI-assisted investment research.** Analyst research and synthesis workflows, with value measurement and an emerging direction for revisiting prior ideas.

**Case context.** An analyst spends a day or two on an idea. Another priority takes precedence. The idea disappears for months and a useful price window can be missed. Kumar discusses agents revisiting old notes against changing markets, rather than only generating more new ideas.

**Mechanism.** Contour documents workflows with and without AI, including sources, conclusions, and time. One comparison follows a company from earnings to earnings, about three months. Kumar discusses different agent/human divisions of work around expert calls, tracks analyst time by company and eventual outcomes, and names cost per useful insight. Operating effort includes broken connectors, model-call failures, and repairs.

**Evidence limits.** Kumar explicitly says P&L impact is still to come at 1:34–1:37. No alpha uplift, ROI figure, productivity percentage, or adoption rate is disclosed. Although he uses the phrase live A/B tests, the talk does not specify randomized assignment. The neglected-idea passage describes a problem and a direction they are thinking about, not a named trade with a proven return. No exact formula for cost per useful insight is supplied.

**Our application.** Our inference: a prior client concern can become useful again before an upcoming meeting. Surface it with date and evidence, then let the rep validate relevance. Compare the complete preparation and review job, including corrections and repairs. Later sales outcomes cannot be causally assigned to assistance from chronology alone.

- [01:34 · P&L impact is still to come](https://www.youtube.com/watch?v=ZMZlAn6Pyfg&t=94s)
- [02:25 · With/without-AI workflow comparisons](https://www.youtube.com/watch?v=ZMZlAn6Pyfg&t=145s)
- [04:38 · Different divisions of expert-call work](https://www.youtube.com/watch?v=ZMZlAn6Pyfg&t=278s)
- [07:35 · The neglected investment idea](https://www.youtube.com/watch?v=ZMZlAn6Pyfg&t=455s)
- [10:05 · Analyst time and cost per useful insight](https://www.youtube.com/watch?v=ZMZlAn6Pyfg&t=605s)
- [16:40 · Broken connectors and operating effort](https://www.youtube.com/watch?v=ZMZlAn6Pyfg&t=1000s)

Local caption: `transcripts/contour.txt`. Acquisition method and checksum: `sources.json`.

## Arize AI: What Does an AI Engineer Do Now?

Aparna Dhinakaran · [Original recording](https://www.youtube.com/watch?v=ImnZ7s68jw8)

**Source application: Arize Signal.** An investigation agent that reads traces, retains issue history, and proposes fixes for AI engineering teams.

**Case context.** Signal provides a concrete example of the engineer’s improvement loop: traces expose recurring problems, investigations retain history, and an agent proposes changes that need evaluation. A run can end without erasing what it learned.

**Mechanism.** Dhinakaran describes agent-consumable telemetry, triggers, context, temporary workspaces, scoped access, proxies, and tracing. Outputs and progress persist as temporary access and environments disappear. She emphasizes comparing evaluators with human-adjudicated examples before shipping a new evaluator.

**Evidence limits.** This is vendor-described architecture, not a measured diagnosis result, proof of autonomous-release safety, or an actual incident reconstructed here. A late self-correction indicates that multi-model support is future-facing; the presentation makes no current-capability claim about it. Persistent investigation evidence does not imply unrestricted user memory or permanent authorization.

**Our application.** Our inference: preserve business questions, snapshots, corrected meanings, and reviewed evaluation cases when a SQL or meeting-prep failure recurs. Judge agreement itself needs examination. The wrong-scope false pass shown in the deck is invented and carries no empirical rate.

- [02:33 · The engineer’s improvement loop](https://www.youtube.com/watch?v=ImnZ7s68jw8&t=153s)
- [03:31 · Signal investigations and issue history](https://www.youtube.com/watch?v=ImnZ7s68jw8&t=211s)
- [06:01 · Workspace, context, proxy, tracing](https://www.youtube.com/watch?v=ImnZ7s68jw8&t=361s)
- [07:11 · Persistent outputs and temporary access](https://www.youtube.com/watch?v=ImnZ7s68jw8&t=431s)
- [11:43 · Trusting and evaluating the evaluator](https://www.youtube.com/watch?v=ImnZ7s68jw8&t=703s)

Local caption: `transcripts/arize.txt`. Acquisition method and checksum: `sources.json`.

## Capital One: Does Code Quality Still Matter? It Depends on This

Max Kanat-Alexander · [Original recording](https://www.youtube.com/watch?v=bU5gDVyu_28)

**Engineering perspective: Max’s software-quality framework.** Choosing rigor by consequences, dependencies, replacement cost, and maintenance; making that rigor easier to apply.

**Case context.** Max moves from tiny changes to Chromium, then from a one-party planning tool to systems people depend on. The real question is what makes software disposable or durable. He then shifts attention to reducing the effort needed to apply rigor.

**Mechanism.** Four factors determine the degree of disposability: consequences of failure, dependencies, replacement cost, and maintenance cost. He advises assuming more durability than expected. Teams can reduce exposure through isolation, limited scope, and independence, and reduce the cost of rigor with standards, checks inside the workflow, deterministic tests, and realistic shared service fakes.

**Evidence limits.** This is a conceptual engineering argument, not a Capital One deployment case study or quantified productivity result. Durability is a spectrum, not a binary or a function of lifetime alone. Short-lived software can still have consequential failures. The presentation invents no numerical risk score.

**Our application.** Our inference: a shared SQL or meeting-prep tool creates dependencies even if its initial code was easy to generate. Reusable checks and reviewed cases can lower the effort required for later changes. These are discussion connections, not an approved team backlog.

- [02:49 · Chromium and comprehensible changes](https://www.youtube.com/watch?v=bU5gDVyu_28&t=169s)
- [07:17 · Disposable-software conditions](https://www.youtube.com/watch?v=bU5gDVyu_28&t=437s)
- [08:58 · A children’s party planner](https://www.youtube.com/watch?v=bU5gDVyu_28&t=538s)
- [09:31 · Four factors and assume durability](https://www.youtube.com/watch?v=bU5gDVyu_28&t=571s)
- [12:05 · Reduce the cost of rigor](https://www.youtube.com/watch?v=bU5gDVyu_28&t=725s)
- [14:19 · Fast deterministic tests and service fakes](https://www.youtube.com/watch?v=bU5gDVyu_28&t=859s)

Local caption: `transcripts/quality.txt`. Acquisition method and checksum: `sources.json`.
