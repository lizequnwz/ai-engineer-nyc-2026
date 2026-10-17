import json
from pathlib import Path
program=json.load(open('work/program.json'))
sessions=program['sessions']
by_title={s['title']:s for s in sessions}
cases=[]
def case(firm,segment,titles,reportedWork,maturity,evidenceLimits,transferableLearning,theme):
 ss=[by_title[t] for t in titles]
 dates=sorted(set(s['date'] for s in ss))
 cases.append(dict(firm=firm,segment=segment,sessionIds=[s['id'] for s in ss],sessionTitles=titles,sourceUrls=['https://ai.engineer/nyc/2026/schedule?session='+s['id'] for s in ss],reportedWork=reportedWork,maturity=maturity,evidenceLimits=evidenceLimits,transferableLearning=transferableLearning,attendanceDate=dates[0] if len(dates)==1 else dates,theme=theme))
case('Bridgewater','Investment management / macro research',
 ['Vault: Making Unstructured Data Work for Investing','Can Your AI Analyst Keep a Secret?'],
 'Reports building Vault as a centralized, high-quality repository of external research and internal unstructured knowledge. The abstract says Vault powers PAT, an analyst agent used daily by hundreds of investors, and is enabling a second-generation Researcher. A co-presentation with turbopuffer describes millions of documents and row-level permissions enforced at retrieval rather than only in application code.',
 'speaker-reported production',
 'Production use and scale are claims in the program. No independent quality, leakage, latency, ROI, or access-revocation results are published in the abstracts. Researcher is described as being enabled, not proven generally deployed.',
 'The distinctive investment appears to be the institution’s information foundation: source quality, connectors, and entitlement-aware access. A reusable analyst platform requires the same permissions as the human user, evaluated as part of retrieval quality rather than added after answer generation.',
 'Institutional knowledge and permission-aware evidence')
case('Wise','Cross-border payments',
 ['Stop turning your Humans Into APIs for your Agents'],
 'Describes LOOP, a Lifecycle Onboarding and Oversight framework, separating model reasoning from authority to act. Human decisions become automated, versioned policies enforced by the platform; repeatable decisions become preventative controls while people handle judgment. The talk promises architecture, trust boundaries, and enforcement locations.',
 'framework',
 'The abstract describes a system Wise says it built, but does not quantify rollout scope, action classes, error rates, or measured control effectiveness. Do not infer that an LLM autonomously moves customer money.',
 'Scale governance by making routine authority decisions explicit and executable. Separate a model’s proposal from the component allowed to execute it, and reserve human attention for genuine exceptions rather than every repeated approval.',
 'Authority, policy, and deterministic controls')
case('Monzo','Digital banking',
 ['Compound value from building Monzo’s in-house agent using LLMs*'],
 'Reports Agent Chip, a sandboxed internal agent, an MCP gateway, and an agent orchestration system. The abstract says it authors about 10% of merged pull requests and runs more than 1,800 tasks daily, with Slack distribution to technical and nontechnical staff and security/observability constraints.',
 'speaker-reported production',
 'Usage and contribution statistics are company-reported. The program does not provide defect-adjusted productivity, avoided review effort, independent security results, or an ROI baseline; merged-PR share is not itself a quality measure.',
 'Distribution inside existing work tools and a centrally controlled runtime can matter as much as model capability. Internal adoption should be read alongside review, quality, and control metrics rather than interpreted from task volume alone.',
 'Firm-wide rollout and engineering operating models')
case('Ramp','Finance operations / spend management',
 ['Chasing capabilities while waiting for the frontier','We gave our finance agent more context. It got worse.'],
 'Ramp Labs describes rapidly replicating research to close capability gaps that finance teams face today. Its production accounting-agent session describes end-to-end benchmarks across models, tools, skills, memory, and the harness; skill ablations identified harmful context, and one frequently loaded skill was shortened from 14,000 to 5,000 characters without sacrificing reported quality. The speaker emphasizes reusable process in memory rather than stale task facts.',
 'speaker-reported production',
 'The abstract does not release task definitions, holdout results, sample sizes, cost deltas, or independent reproduction. One successful context reduction should not be generalized into a rule that less context always wins.',
 'Treat context, memory, tools, and harness changes as empirical interventions. Removing unhelpful content can improve an agent; the useful target is end-to-end quality, reliability, latency, and cost, not maximal context or the latest model alone.',
 'Evaluation-driven harness improvement')
case('Optiver','Electronic market making / trading',
 ['Scaling AI with P&L on the line'],
 'Describes agent adoption in engineering with a supported golden path and an experimental funnel requiring telemetry and a graduation-or-sunset decision. Model choice is handled through task-specific exams, routing toward the cheapest certified model, multiple access channels, and self-hosted open weights. The abstract identifies long-context work as an important inference-cost driver at large internal scale.',
 'speaker-reported production',
 'The operational account is speaker-reported. The abstract does not publish exam validity, security findings, defect rates, causal productivity estimates, or cost savings; it does not establish AI control of trading decisions.',
 'A mature rollout can offer both a dependable standard path and bounded experimentation. Certification should be task-specific, cost should be measured on successful work, and model independence can be an operating policy rather than an ad hoc vendor switch.',
 'Firm-wide rollout and engineering operating models')
case('Upstart','Consumer lending',
 ['From Human Review to Self-Healing Agents: How Upstart Evaluates Voice AI at Regulated-Lending Scale'],
 'Reports voice agents handling hundreds of thousands of customer calls per month. The described evaluation path starts with human review of every call and advances to LLM judges only after they match human graders; a co-presenter from Coval discusses evaluation infrastructure and simulation. Automated self-improvement loops are described as work they are building toward.',
 'speaker-reported production',
 'Production voice use is reported, but judge-agreement metrics, error severity, approval thresholds, and outcome baselines are not supplied. The abstract distinguishes future automated loops from achieved capability; do not label the system fully self-healing today.',
 'The evaluator must earn trust before it can substitute for review. Establish agreement with qualified humans on consequential failures, then expand automation in stages rather than assuming a model judge is reliable because it is fluent.',
 'Evaluation-driven harness improvement')
case('Contour Asset Management','Long/short fundamental equity investing',
 ["Proving Alpha: Showcasing AI's Value in Fundamental Investing"],
 'Describes agent workflows integrated into idea generation, overnight news synthesis, and earnings previews, developed with investors and used daily. It logs each generated idea at creation with its source and reasoning, scores utility, tracks progression to PM consideration and positions, and compares positions with benchmarks. Softer signals are compared with the previous way of producing the same metric.',
 'speaker-reported production',
 'The abstract promises attribution methods but gives no realized return uplift, experiment design, controls for selection/market regime, or independently established alpha. Tracing a workflow into a position does not by itself demonstrate causal performance contribution.',
 'Record the lineage from generated output to human use to a business decision. Evaluate research tools on utility, workflow adoption, time, and signal quality while keeping operational attribution distinct from claims of causal investment alpha.',
 'Business value and investment-process measurement')
case('Apollo Global Management','Private equity / alternative asset management',
 ['Turning AI Into Operating Margin: A Field Report from Private Equity',"AI in Practice: An Inside Look at Apollo's Approach"],
 'The portfolio-operations session describes AI assessment in deal diligence and underwriting, deployment cases in air-cargo network decisions and AI-native education, central reusable capabilities versus partnerships, and linking work to operating margin. A separate Apollo/Rowspace keynote is labeled only as a Rowspace customer co-presentation.',
 'speaker-reported production',
 'Portfolio examples are described as shipping work, but no quantified margin improvement, deployment coverage, causal comparison, or detailed architecture is supplied. The Rowspace keynote has no substantive abstract, so it cannot support claims about a particular Apollo agent, platform, or use case.',
 'AI investment can be evaluated as an operating intervention with a financial outcome, not only a technology rollout. Distinguish reusable central capabilities from company-specific workflows, and demand a measurement path to the margin or decision the business actually cares about.',
 'Business value and investment-process measurement')
case('Vanguard','Asset management / cash infrastructure',
 ["No Cash Left Behind: Vanguard's Ledger Modernization Journey"],
 'Describes modernization of a cash ledger processing hundreds of thousands of daily transactions into active-active cloud-native microservices while the legacy system remained live. Producer migration, replicated gold-copy data, and consumer migration ran separately; CDC, GraphQL decoupling, and database-layer idempotency are highlighted. AI tools are said to have helped maintain both codebases during the migration.',
 'speaker-reported production',
 'The production claim concerns the ledger migration. The abstract does not detail the AI tooling, isolate its productivity impact, or describe a deployed investor/advisor agent. Do not turn this case into a claim of Vanguard autonomous financial decision-making.',
 'Reliable financial infrastructure still depends on explicit data consistency, decoupled change, and idempotency. AI assistance does not remove those system responsibilities; modernization evidence should distinguish the core architecture from the unspecified AI contribution.',
 'Reliable infrastructure and controlled modernization')
case('Wells Fargo','Banking / fraud and transaction modeling',
 ['Wells Fargo Foundation Model: Application to Fraud Detection at Scale'],
 'Reports developing transaction foundation models trained on billions of banking transactions. The session covers heterogeneous transaction representation, tokenization and sequence design, data curation, training/evaluation pipelines, and adaptive fine-tuning with multi-task learning for fraud detection and transaction decisioning.',
 'unknown',
 'The abstract uses production-grade language and promises lessons moving from experimentation to production, but does not clearly establish the deployment status or scope of any particular model. No performance, loss reduction, fairness, or operating-cost results are supplied.',
 'Institutional AI activity includes domain-specific predictive models as well as LLM assistants. Data representation and validation are central design investments; evaluate this approach against task baselines before assuming a foundation model is preferable.',
 'Domain models and financial data foundations')
case('Two Sigma','Quantitative investment management',
 ['Balancing Acceleration and Safety for AI Agents'],
 'John Feminella describes technical approaches Two Sigma says it uses to balance safe agentic AI with innovative research and engineering in a regulated firm. The abstract frames utility, cost, and risk as joint design concerns.',
 'framework',
 'The program does not name the controls, deployment scope, use cases, metrics, or evaluation results. The claim that safety need not trade off against innovation is an argument to examine, not demonstrated evidence that all such tradeoffs disappear.',
 'Treat safety and utility as co-designed system properties. A useful industry comparison requires the actual control mechanism and its measured effect, not a general assertion of safe innovation.',
 'Authority, policy, and deterministic controls')
case('JPMC','Banking / security architecture',
 ['Intent Based Auth'],
 'Global Chief Security Architect Michael Davis participates with Keycard and AAuth in a panel about authorizing an agent’s mission and resource scope beyond individual tool calls. The abstract introduces AAuth as a new protocol and discusses intent enforcement.',
 'framework',
 'Panel participation does not establish JPMC adoption of AAuth, Keycard, or a production intent-auth system. No JPMC deployment case or measured effectiveness appears in the abstract.',
 'A valid credential and an allowed tool are insufficient descriptions of delegated authority. Evaluate whether policy binds the human, agent, resource, and intended task, and where a runtime can enforce those bounds.',
 'Authority, policy, and deterministic controls')
case('Citadel Securities','Market making / enterprise operations',
 ['Your Company Has No Model of Itself: Bootstrapping a World Model from Slack, Decks and Meetings'],
 'Joao Wenzel, listed as COO at Citadel Securities, describes bootstrapping an enterprise state estimator from messages, screenshots/PDFs, decks, meetings, and voice notes. The proposed model tracks beliefs about entities over time, freshness, noisy observations, missing sources, and predictions, distinguishing current-state estimation from retrieval of past statements. His speaker bio says he is responsible for firm-wide agentic AI deployment.',
 'pilot or experiment',
 'The abstract describes a usable model but does not establish production rollout, prediction accuracy, business impact, permission controls, or firm-wide adoption of this specific system. Citadel Securities is the explicit affiliation; it must not be shortened to or conflated with Citadel, the separate firm referenced in other speakers’ past roles.',
 'Some enterprise questions require maintained estimates of changing state, not only document search. The architecture claim is interesting but needs fresh-data, uncertainty, access-control, and out-of-sample prediction evidence before its superiority can be accepted.',
 'Institutional knowledge and permission-aware evidence')
case('GEICO','Insurance / enterprise engineering',
 ['Inside the Fable War Room'],
 'Describes an enterprise experiment with Anthropic on distributed legacy systems. A cross-functional team and on-call experts provided a modernization strategy, tools, context, rules, skills, system knowledge, validation tips, and structured routes back to humans. The abstract describes packaging this as a plugin methodology and claims a first-day outcome equivalent to $275,000 per year.',
 'pilot or experiment',
 'The abstract explicitly calls this an experiment. The annualized savings claim has no methodology, baseline, realized-period evidence, or attribution details; do not report it as audited savings or evidence of company-wide autonomous modernization.',
 'For difficult legacy work, domain access and a coordinated team can be part of the agent system. A reusable method should include how uncertainties are routed to experts and how changes are validated, not just the model or prompt.',
 'Reliable infrastructure and controlled modernization')
case('Capital One','Banking / software engineering',
 ['Does Code Quality Even Matter?'],
 'Principal Software Engineer Max Kanat-Alexander proposes principles for deciding how to evaluate code quality and review practices as AI writes more software.',
 'framework',
 'This is a principles talk, not an abstract describing a named Capital One deployment, rollout policy, measured outcome, or eliminated review process.',
 'Software review needs an explicit decision standard. Before accepting a faster AI delivery process, identify what correctness evidence remains necessary and which review responsibilities are being transferred or retained.',
 'Firm-wide rollout and engineering operating models')
case('Coinbase','Digital assets / financial developer infrastructure',
 ['Trusting Agents in Policy-Driven Workflows','Developer Docs as Knowledge Infrastructure for Fintech','Building the Financial Account for Agents'],
 'Describes auditable workflows with bounded agent loops and human control; rebuilding Coinbase Developer Platform documentation for agents; and designing financial accounts with human-defined controls, stablecoin payments, and machine-scale transactions. The docs session claims agents account for 59% of traffic, more than 30,000 MCP tool calls, and 145 AI tools. The account session cites x402 ecosystem payment activity.',
 'speaker-reported production',
 'Production evidence is strongest for developer documentation/tool consumption. Traffic and protocol volumes are speaker-reported and are not measures of correctness, unique agent users, or Coinbase-specific autonomous-account deployment. The proposed account/control design and workflow framework should not be treated as a mature universally deployed product.',
 'Agents can become consumers of documentation, APIs, and financial rails, so infrastructure must expose machine-usable knowledge and bounded authority. Adoption volume and transaction success must be supplemented by correctness, fraud, policy, and delivered-value measures.',
 'Machine-facing financial infrastructure')
case('Bloomberg','Financial data and technology',
 ['Security in the Age of AI: Recent Attacks, Incidents & Defenses'],
 'Head of Architecture and Emerging Technologies Andrey Rybka discusses recent incidents, prompt injection, data leakage, agentic AI, supply-chain risk, and defense patterns. His official bio describes leading architecture for Bloomberg’s open-source, AI-cloud, MCP/agentic-AI adoption, and AI-security initiatives.',
 'framework',
 'The session abstract and bio establish the speaker’s institutional remit, not a specific Bloomberg production architecture, security outcome, or failure-free deployment. Incident details and defense effectiveness remain to be inspected.',
 'AI adoption broadens both internal attack surfaces and attacker capabilities. Security architecture should connect model and agent risks to existing identity, software supply-chain, data, and runtime controls, then test the combined system.',
 'Authority, policy, and deterministic controls')
case('Jump Trading','Trading / compute markets',
 ['The Dark Pools of Compute'],
 'Compute-trading leaders discuss GPU/compute supply, power and data-center economics, financing/depreciation, shifts in buyer contracts and hardware generations, policy, sovereign demand, and possible market maturation. The speaker bio describes a compute division trading, financing, and structuring compute/inference transactions.',
 'framework',
 'This is a market-structure perspective, not evidence of an AI agent deployment or a realized investment return. Policy and market forecasts in the abstract are not independently verified and should not be presented as settled developments.',
 'AI economics extend beyond token pricing to capacity, contract duration, financing, and hardware generation risk. A mature cost comparison should distinguish model/application efficiency from the procurement and capital structure of compute.',
 'Machine-facing financial infrastructure')
case('Blackstone','Alternative asset management',
 ['CTO, Blackstone'],
 'CTO John Stecher is scheduled in conversation with Norm.ai CTO Scott Worland.',
 'unknown',
 'Role-placeholder title and empty abstract. The program does not support a claim that Blackstone deployed Norm.ai, a particular compliance agent, or a particular architecture; shared stage appearance alone is insufficient.',
 'Treat this as a potential practitioner interview to learn from after the event, not as an existing case study in a report based only on abstracts.',
 'Evidence gap / practitioner to follow')
case('Coatue','Investment management',
 ['Head of AI & AI Engineer, Coatue'],
 'Head of AI Frank Long is scheduled for a keynote.',
 'unknown',
 'Role-placeholder title and empty abstract. No specific Coatue product, deployment, investment workflow, measured outcome, or architecture is supported by this record.',
 'Keep institutional presence separate from evidence of institutional practice. Add a case only when the talk or released materials provide a substantive mechanism and scope.',
 'Evidence gap / practitioner to follow')
case('Arca','Financial-services workflow automation (as described in abstract)',
 ['Arca’s agent runtime for long horizon financial services work'],
 'Describes an agent runtime for work spanning weeks, multiple agents and humans, and external systems. The promised architecture includes orchestration, tools, context, a sandbox, signals, and human involvement when work cannot progress; it is framed as managing clients’ financial lives and operational work.',
 'unknown',
 'The company name alone does not establish which similarly named entity or business segment is meant. The abstract claims broad automation but gives no rollout counts, task success, loss/risk metrics, or production maturity sufficient to classify this as proven full automation.',
 'Financial work is often long-horizon rather than a single uninterrupted agent run. Durable state, explicit handoffs, external events, and bounded human involvement are distinct design needs that a fluent model loop does not resolve by itself.',
 'Reliable infrastructure and controlled modernization')
case('New York Life Insurance (speaker affiliation)','Insurance / AI evaluation research',
 ['1,368 AI Failures: What They Teach Us About System Evals'],
 'Vishal Srivastava and Tanmay Sah describe research on 1,368 documented failures across sectors and Risk-Based Evaluability Design. The proposed unit of evaluation is the deployed system—evidence, tools, state, authority, human intervention, exposure, and impact—rather than task completion alone.',
 'framework',
 'The speaker affiliation does not establish adoption of this framework at New York Life. Incident counts and the reported 92% multi-weakness result need sampling/labeling methodology; this is not a prevalence estimate of all AI systems or a New York Life incident dataset.',
 'Evaluate consequential failure paths through the full system and design the evidence needed to reconstruct them. A correct answer can coexist with unsupported evidence or an unauthorized action; insufficient evidence can be the appropriate evaluation result.',
 'Evaluation-driven harness improvement')
out=dict(source='https://ai.engineer/nyc/2026/schedule',sourceGeneratedAt=program['generatedAt'],preparedDate='2026-10-10',status='Pre-conference example intelligence based on program descriptions, not an attendance readout or independently verified deployment survey.',cases=cases,
 attributionCautions=[
  dict(topic='Citadel vs Citadel Securities',detail='Joao Wenzel is listed at Citadel Securities and his bio repeats that affiliation. Kepler speakers mention former Citadel roles; these do not establish current Citadel sponsorship or deployment of Kepler. Keep the organizations and current/former roles distinct.',sessionIds=['bf371da6-6ef6-42ec-865f-5de4974a9114','a244839c-239c-4789-b621-32a3568a218e']),
  dict(topic='SoFi vs Salesforce affiliation mismatch',detail='Ishween Kaur’s company field says SoFi and role says Agentic Platform Agentforce; her bio says senior software engineer on Salesforce AgentForce. The payment-attack talk is a local simulation/testnet demonstration, not evidence of a SoFi deployment. Attribute it to the speaker unless the conflict is resolved.',sessionIds=['eaa39362-c0ec-4849-a90d-841f4825a5b3']),
  dict(topic='Goldman Sachs title is not a Goldman case',detail='Can AI run Goldman Sachs? is presented by Epsilab founders, with no Goldman Sachs speaker or deployment asserted. Do not label its experiments as Goldman Sachs practice.',sessionIds=['471890b7-1779-41e1-8411-b499dd38c346']),
  dict(topic='Named wealth-manager evidence is limited',detail='The concrete wealth-concierge workshop is delivered by OpenAI engineers on Monday October12. It demonstrates building with plugins, client information, skills, client questions, and advisor briefs; it does not name a wealth-management institution using the system in production and is outside the attendee’s Tuesday/Wednesday scope.',sessionIds=['b4d58021-e1c3-4703-b294-0f7cacaa5f68']),
  dict(topic='Sponsor and trusted-by logos are not case studies',detail='Homepage logos for Morgan Stanley, BlackRock, Goldman Sachs, and others do not by themselves establish the use cases, architectures, adoption, or results of those firms. Do not fill gaps in the schedule from logos.',sessionIds=[]),
  dict(topic='Unnamed client banks remain unnamed',detail='Cisco’s five-bank deployment description, Comet’s regulated-bank account, and Langfuse’s top-global-bank pattern do not identify client institutions. They can be vendor-reported patterns, not institution-attributed cases.',sessionIds=['71008b4d-f354-4f66-85dc-9052435c2955','d75067e0-d840-47ad-93ee-9465ab3ae891'] if False else ['71008b4d-f354-4f66-85dc-9052435c2955'])
 ],
 suggestedThemes=[
  dict(title='Institutional knowledge is becoming an AI platform asset',caseFirms=['Bridgewater','Citadel Securities'],takeaway='Permission-aware, high-quality source access and maintained organizational context are recurring investments; retrieval and current-state estimation answer different questions.'),
  dict(title='Governance is moving into executable runtime controls',caseFirms=['Wise','JPMC','Two Sigma','Bloomberg'],takeaway='Reasoning should not automatically confer authority. Identify policy enforcement, trust boundaries, revocation, and evidence rather than equating governance with a review committee.'),
  dict(title='Evaluation is an operating loop, including evaluation of the evaluator',caseFirms=['Ramp','Upstart','New York Life Insurance (speaker affiliation)'],takeaway='Institutional speakers emphasize ablations, human-calibrated judges, multi-metric evaluation, and system failure paths rather than relying on model leaderboards.'),
  dict(title='Firm-wide adoption needs both a standard path and bounded experimentation',caseFirms=['Optiver','Monzo','Capital One'],takeaway='Platforms, approved runtimes, existing collaboration channels, task-specific model certification, and clear quality standards make adoption manageable.'),
  dict(title='Value is being tied to the investment or operating process',caseFirms=['Contour Asset Management','Apollo Global Management'],takeaway='Capture lineage from generated output to use and decision, and compare outcomes with a baseline. Usage and annualized claims are not causal ROI or alpha.'),
  dict(title='Legacy and long-horizon work keep reliability fundamentals central',caseFirms=['Vanguard','GEICO','Arca'],takeaway='Durable state, data consistency, idempotency, expert handoffs, and verified changes remain essential even when agents accelerate part of the work.'),
  dict(title='Financial AI includes domain models and machine-facing infrastructure',caseFirms=['Wells Fargo','Coinbase','Jump Trading'],takeaway='Beyond chat interfaces, the agenda includes transaction models, agent-readable documentation and payment rails, and compute economics; maturity varies materially across these accounts.')])
# Every referenced institution case must map to an existing source session.
ids={s['id'] for s in sessions}
for c in cases:
 assert all(i in ids for i in c['sessionIds'])
Path('work/institution_cases.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('Saved',len(cases),'institution/practitioner cases,',len(out['suggestedThemes']),'themes,',len(out['attributionCautions']),'attribution cautions.')
