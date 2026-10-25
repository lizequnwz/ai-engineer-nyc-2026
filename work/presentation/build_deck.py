from pathlib import Path
import json,html,re
from urllib.parse import urlparse,parse_qs
from core_cases import render_case
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'work';P=W/'presentation';O=ROOT/'outputs'
H=lambda s:html.escape(str(s),quote=True)
notes1=json.loads((W/'day1_notes_data.json').read_text())['sessions'];notes2=json.loads((W/'day2_notes_data.json').read_text())['sessions']
NOTE_IDS={s['id'] for s in notes1+notes2};DAY2_IDS={s['id'] for s in notes2}
program={s['id']:s for s in json.loads((W/'program.json').read_text())['sessions']};program.update(json.loads((W/'day2_metadata.json').read_text())['sessions'])
industry=json.loads((W/'industry-report-data.json').read_text());wealth=json.loads((W/'wealth_context.json').read_text())['cases']
RECORDING=json.loads((W/'recording_evidence.json').read_text())
RECS={r['id']:r for r in RECORDING['records']}
SC='https://ai.engineer/nyc/2026/schedule?session='
CHAPTERS={
 'opening':('FIELD NOTES / NYC 2026','#075e52'),
 'strategy':('01 / FINANCE STRATEGY & VALUE','#075e52'),
 'grounding':('02 / GROUNDED AGENTS','#245b91'),
 'evals':('03 / BUILDING EVALUATIONS','#65428c'),
 'workflows':('04 / RELIABLE WORKFLOWS & SKILLS','#874c1b'),
 'growth':('05 / GROWING AS AN AI ENGINEER','#285d67'),
 'closing':('TAKEAWAYS & DISCUSSION','#075e52'),
 'appendix':('APPENDIX / EVIDENCE & METHODS','#50616a')}
def paras(xs):return ''.join('<p>'+H(x)+'</p>' for x in xs)
def table(headers,rows,cls='data-table'):
 return '<table class="'+cls+'"><thead><tr>'+''.join('<th scope="col">'+H(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+H(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
def cards(items,cols=3):
 return f'<div class="grid{cols}">'+''.join(f'<article class="visual-card"><div class="label">{H(a)}</div><h3>{H(b)}</h3><p>{H(c)}</p>'+('' if not d else f'<div class="company">{H(d)}</div>')+'</article>' for a,b,c,d in items)+'</div>'
def flow(items):
 return f'<div class="flow" style="--cols:{len(items)}">'+''.join(f'<div class="flow-step"><span class="n">{i:02}</span><b>{H(a)}</b><p>{H(b)}</p></div>' for i,(a,b) in enumerate(items,1))+'</div>'
def takeaway(t):return '<div class="takehome">'+H(t)+'</div>'
def small(t):return '<p class="small-note">'+H(t)+'</p>'
def body(s):
 v=s['visualData'];lid=s['layout'];sid=s['id']
 scene=render_case(sid,table,flow,small)
 if scene is not None:return scene
 if lid=='cover':
  return '<div><h2 class="cover-title slide-title" id="title-opening-cover" tabindex="-1">From AI capability<br>to <em>dependable work.</em></h2><p class="cover-intro">Financial-services AI, explained through company stories, practical methods, and reconstructable examples.</p><div class="cover-meta"><span><b>AI Engineer NYC 2026</b>October 13–14 · recordings reviewed October 25</span><span><b>For practitioners</b>Data scientists · AI engineers · technical leads</span><span><b>40 minutes + discussion</b>Five chapters · detailed reading edition</span></div></div><span class="cover-rail" aria-hidden="true">EVIDENCE → METHODS → ACCEPTED WORK</span>'
 if lid=='roadmap':
  return '<div class="chapter-map">'+''.join(f'<div><span>{i:02}</span><b>{H(a)}</b><small>{H(b)}</small></div>' for i,(a,b) in enumerate([('Strategy','Valuable work and credible economics'),('Grounding','Evidence, meaning, time, access'),('Evaluation','Cases, rubrics, judges, release'),('Workflows','Skills, authority, verification'),('Growth','Own the improvement loop')],1))+'</div>'+takeaway('The unit of progress is accepted work with evidence, controls, and a credible baseline.')
 if lid=='qualitative-case-map':
  rows=[['Bridgewater / Coatue','Investment attention','Eligible evidence; evaluated decision steps'],['Range / Apollo–Redding Ridge','Professional preparation','Expert method; reconciliation; reviewed drafts'],['Wells Fargo','Fraud decision at transaction speed','Transaction representation; detection vs false positives'],['Blackstone / Norm.ai','Adapt as models improve','Accessible data; durable acceptance assets; production controls']]
  return table(['Company story','Bottleneck addressed','Mechanism'],rows)
 if lid=='four-case-comparison':
  return cards([('Range','Planner-owned skills','Reasons, questions, owner + reviewer; no client send.','Recorded workflow'),('Arca','Service across days','Shared plans wake on replies, approvals and settlement.','Illustrative tax-payment story'),('Perpetual','Approved execution','Typed intent, compiled plan, exact-payload approval.','Reported production method'),('Wealth incumbents','Preparation + knowledge','Morgan Stanley Debrief; UBS Red; RBC Advisor Assist.','Historical disclosures · 2024–25')],4)
 if lid=='measurement-ladder':
  return flow([(x['name'],x['evidence']) for x in v['stages']])+takeaway('Contour’s comparison question: what would the workflow have concluded without AI?')
 if lid=='cost-equation-with-baseline':
  return '<div class="split"><div class="calculation"><div class="label-note" style="color:var(--lime)">Proposed measurement</div><div class="formula">Total workflow cost<br>÷ accepted tasks</div><p>Attempts + tools + review + rework + operation</p></div><div>'+''.join(f'<div class="case-strip"><b>{H(a)}</b><p>{H(b)}</p></div>' for a,b in [('Jellyfish','Human salary + AI spend per merged PR; inspect quality too.'),('Credit Karma demo','24,000 → 2,400 context tokens; quality still needs evaluation.'),('Local comparison','Same tasks, input snapshots, acceptance and review standard.')])+'</div></div>'+small('Reported engineering observations and a token-use demonstration motivate the measure; neither establishes causal savings for another workflow.')
 if lid=='fact-contract':
  return flow([('Select evidence','Eligible source + exact anchor'),('Resolve fact','Model chooses a fact identifier'),('Compute','Code preserves inputs and operations'),('Verify output','Check final number and supporting claim')])+'<div class="claim-facts">'+''.join('<span>'+H(x)+'</span>' for x in ['Value · unit · scale · period','Entity · metric · source version','As-of cutoff · access · derivation'])+'</div>'+takeaway('Kepler still checks generation after retrieval: pointer lookup does not prove every final claim correct.')
 if lid=='inspectable-output':
  return flow([(x['label'],x['detail']) for x in v['layers']])+takeaway('OpenAI’s product presentation and Kepler’s verification story meet at the point where a user inspects a claim.')
 if lid=='workflow-and-quality-vector':
  return flow([('Outcome','Is the complete work acceptable?'),('Behavior','Were consequential decisions sound?'),('Authority','Were actions and transitions permitted?'),('Operation','What did time, retries and review cost?')])+takeaway('Combine exact checks, expert rubrics and trajectory evidence; no single average or final-answer match covers the whole job.')
 if lid=='synthetic-worked-rubric':
  return '<p class="worked-question">Draft a monthly cash-flow snapshot. Use current approved records. Do not recommend or send.</p><div class="split"><div>'+table(['Synthetic input','Value'],[['Income','$8,000 / month'],['Current expenses','$6,000 / month'],['Superseded expenses','$5,500 / month'],['Insurance details','Missing']])+'</div><div>'+table(['Rubric dimension','Scoring / acceptance'],[['Arithmetic','0: wrong · 1: correct but derivation incomplete · 2: correct and reconstructable'],['Source validity','Use current $8,000 and $6,000 inputs; a superseded input fails this dimension'],['Uncertainty','State missing insurance facts and the needed clarification'],['Action boundary','BLOCK recommendation or send; scores cannot offset it']])+'</div></div>'
 if lid=='judge-calibration-and-passk':
  return '<div class="split"><div><div class="matrix"><div class="matrix-head"></div><div class="matrix-head">Human accepts</div><div class="matrix-head">Human rejects</div><div class="matrix-head">Judge passes</div><div>Agreement</div><div class="bad"><b>False pass</b><small>Missed consequential failure</small></div><div class="matrix-head">Judge fails</div><div class="bad"><b>False failure</b><small>Lost utility / review burden</small></div><div>Agreement</div></div></div><div><div class="label-note">Synthetic attempt illustration</div><div class="attempt-strip"><span>1 · fail</span><span class="pass">2 · pass</span><span>3 · fail</span></div><h3>One success among three attempts</h3><p>Who recognizes the usable answer? What are retry, verification, latency, and review costs?</p></div></div>'+small('pass@k measures an at-least-one-success opportunity under a defined test, not first-attempt reliability. No empirical rate is shown.')
 if lid=='release-decision-gate':
  return '<div class="decision-banner hard"><b>Blocking conditions</b><p>Unauthorized action · unsupported consequential number · omitted required approval</p></div><div class="decision-banner"><b>Quality & economics</b><p>Task acceptance · paired regressions · judge validity · uncertainty · review cost</p></div>'+flow([('Evidence packet','Cases, versions, traces'),('Accountable decision','Investigate or promote within scope'),('Staged operation','Monitor, stop, roll back')])+small('Illustrative release logic. Passing a finite suite does not prove that a critical failure is impossible.')
 if lid=='worked-workflow':
  return '<div class="boundary"><div class="boundary-title">SYNTHETIC REVIEW PACKET · FICTIONAL CLIENT A</div>'+flow([('Authorized facts','Income $120k · recorded expenses $84k'),('Agent draft','Arithmetic difference: $36k'),('Planner review','Inspect facts, assumptions, gaps'),('Separate authority','No action without permission')])+'</div>'+small('Illustrative workflow, not a firm architecture or advice. The arithmetic difference does not establish affordability, suitability, or an insurance need.')
 if lid=='control-path':
  return '<div>'+''.join('<div class="control-layer"><strong>'+H(a)+'</strong><div class="nodes">'+''.join('<span>'+H(x)+'</span>' for x in xs)+'</div></div>' for a,xs in [('Ownership',['Registry','Owner','Product','Evaluations']),('Scope & risk',['Identity','Tools','Endpoints','Resources']),('Enforcement',['Policy boundary','Human exceptions','Authorized executor'])])+'</div>'+takeaway('Two Sigma describes the components; Wise’s program case separates model reasoning from authority. Test the boundary under failure.')
 if lid=='three-loops':
  return cards([(x['label'],x['detail'],'Intent · guardrails · verification · evidence','') for x in v['loops']])
 if lid=='operating-loop':
  return '<div class="cycle">'+''.join(f'<div><span class="index">{i:02}</span><b>{a}</b><span>{b}</span></div>' for i,(a,b) in enumerate([('Frame','Define the accepted work'),('Build','A complete working slice'),('Learn','Traces, cases, failures'),('Operate','Verify, release, observe')],1))+'</div>'+takeaway('Grow from producing a feature to owning the evidence and decisions that improve it.')
 if lid=='competency-map':
  return '<div>'+''.join(f'<div class="role-row"><span class="index">{i:02}</span><b>{H(x["responsibility"])}</b><p>{H(x["practice"])}</p></div>' for i,x in enumerate(v['cards'],1))+'</div>'
 if lid=='qualitative-decision-matrix':
  return '<div class="grid2">'+''.join(f'<article class="visual-card {"warm" if x["y"]=="high" else ""}"><div class="label">{H(x["x"])} lifespan · {H(x["y"])} consequence</div><h3>{H(x["label"])}</h3><p>{H(x["detail"])}</p></article>' for x in v['cells'])+'</div>'+small('Editorial decision aid informed by Capital One’s talk. Short-lived software can still have consequential failures.')
 if lid=='learning-lab':
  return '<div class="plan-stack">'+''.join(f'<div class="plan-week"><span class="week">{i:02} / {H(x["step"])}</span><b>{H(x["deliverable"])}</b><p>{H(t)}</p></div>' for i,(x,t) in enumerate(zip(v['stages'],['Choose one meaningful output.','Record quality, time, and cost.','Change one variable; inspect failures.','Continue, revise, or retire.']),1))+'</div>'+small('Optional learning exercise. No Fidelity project, deadline, or resource commitment is implied.')
 if lid=='decision-board':
  return cards([(x['name'],x['prompt'],'A decision to make explicit, supported by evidence.','') for x in v['decisions']])+takeaway('One bounded comparison: same work, agreed quality, critical limits, full human effort, full cost.')
 if lid=='discussion-prompts':
  return cards([(x['label'],x['prompt'],'','') for x in v['cards']])+takeaway(v['closingLine'])
 if lid=='appendix-evidence':
  return table(['Responsibility','What to specify','What to inspect'],[['Task','User, work product, acceptance and baseline','Can the reviewer recognize completed work?'],['Evidence','Entity, period, units, source version, cutoff and access','Can each material claim be reproduced?'],['Authority','Allowed resources, proposals, approvals and execution','Can a denied action bypass the boundary?'],['Evaluation','Cases, rubric, critical failures and calibrated judges','Which serious failure could still receive a pass?'],['Operation','Versions, traces, release owner, stop and rollback','Can a failure be diagnosed and a repair verified?']])+takeaway('Use the same contract to align domain experts, data scientists, engineers and release owners.')
 if lid=='appendix-atlas':
  return table(['Theme','Company examples','Transferable mechanism'],[['Evidence and research','Bridgewater · Kepler · Contour','Time-scoped retrieval, typed facts, reproducible comparisons'],['Wealth workflows','Range · Morgan Stanley · UBS · RBC','Expert-authored preparation, institutional knowledge, reviewed follow-through'],['Authority and controls','Two Sigma · Wise','Owned agents, resource scope, explicit approval and execution boundaries'],['Engineering platforms','Monzo · Optiver · Vanguard','Shared runtime, task qualification, financial invariants'],['Improvement and learning','Ramp · Arize · Sonar · Capital One','Task-level ablations, trace diagnosis, layered verification, deliberate maintenance']])+small('The complete 25-firm table and individual source context are in Read & learn.')
 if lid=='appendix-eval-spec':
  return '<div class="split"><pre class="code-block">'+H(v['code'])+'</pre><div><h3>Make the decision reproducible</h3><p>One contract connects the task, data snapshot, cases, critical conditions, evaluator, and release owner.</p><p class="small-note">Illustrative schema, not an executable framework or company policy.</p></div></div>'
 if lid=='appendix-claim':
  return '<div class="split"><pre class="code-block">'+H(v['code'])+'</pre><div><h3>Preserve what the number means</h3><p>The entity, period, unit, source version, and transformation travel with the value.</p><p class="small-note">An inspectable calculation still requires correct source selection and interpretation.</p></div></div>'
 if lid=='appendix-passk':
  return cards([('Benchmark question','Was any candidate successful?','State k, the task distribution, and the specified test.','pass@k'),('Deployment question','Can the system select a usable answer?','Evaluate selection, first-attempt behavior, retries, and review.','End-to-end reliability')],2)+small('Primary method reference: Chen et al., Evaluating Large Language Models Trained on Code (2021).')
 if lid=='appendix-measures':
  return table(['Measure','Definition to agree','Interpretation boundary'],[['Accepted-task rate','Accepted / eligible assigned tasks','Do not hide excluded failures'],['Cost per accepted task','Full workflow cost / accepted tasks','Include review, retries, rework'],['Capacity','Accepted outputs / human effort or period','Compare quality and task mix'],['Business impact','Outcome against credible alternative','Account for selection and other drivers']])+small('Proposed measurement definitions. The notes contain no causal financial result for these workflows.')
 if lid=='appendix-unknowns':
  return cards([('Clarified','Mechanisms now have detail','Bridgewater precision@10; Range ownership/review; Kepler final checks; Vanguard code-research scope.',''),('Separate editions','Avoid a plausible false match','Ramp keynote vs eval breakout; Kepler breakout vs next-day follow-up; Range recording vs attendance date.',''),('Still open','Do not manufacture precision','Banking affiliation/“roundedness”; exact retrieval defaults; several result denominators; provider spelling.','')])+small('Sources distinguish transcript evidence, written follow-up and video-description scope. Reported outcomes are not independently validated effects.')
 if lid=='appendix-sources':
  return table(['Reference group','What was inspected','How to use it'],[['Released NYC material','90 uploads screened; 50 official descriptions; selected transcripts from the 52-session archive','Use timestamped sources; descriptions do not establish unobserved demo details'],['Original notes + written follow-up','12 attendee-note sets; Ryan Stevens’s October 14 article','Preserve attendance history; distinguish the two Ramp sessions'],['Historical disclosures + metric paper','Morgan Stanley 2024; UBS/RBC 2025; Chen et al. 2021','Retain dates, populations and the metric definition'],['Teaching examples','AsterCo, cash-flow rubric, release gates and combined diagrams','Invented examples and proposed methods are labeled']])+takeaway('Open Sources on any page. Read & learn adds company deep dives and the full linked catalog.')
 raise ValueError('Unhandled layout: '+lid)

def reader_extra(s):
 v=s['visualData'];lid=s['layout']
 if lid=='four-case-comparison':return '<h4>Original wealth disclosures and attendee context</h4><div class="table-scroll">'+table(['Firm / source date','Reported mechanism','Evidence boundary'],[[x['firm']+' · '+x['date'],x['mechanism'],x['boundary']] for x in v['cards']],'reader-appendix-table')+'</div>'
 if lid=='worked-example':return '<h4>Full synthetic source history</h4><div class="table-scroll">'+table(v['table']['columns'],v['table']['rows'],'reader-appendix-table')+'</div>'
 if lid=='synthetic-worked-rubric':return '<h4>Full illustrative rubric</h4>'+table(['Dimension','Diagnostic score / condition'],[[r['dimension'],r['scoreGuide']] for r in v['rubric']],'reader-appendix-table')+'<p>'+H(v['workedAcceptableOutput'])+'</p>'
 if lid=='paired-ablation-matrix':return '<h4>Variables to hold fixed</h4><ul>'+''.join('<li>'+H(x)+'</li>' for x in v['invariants'])+'</ul>'
 if lid=='worked-workflow':return '<h4>Illustrative responsibility boundaries</h4>'+table(['Actor','Responsibility'],[[x['actor'],' → '.join(x['steps'])] for x in v['lanes']],'reader-appendix-table')
 if lid=='appendix-atlas':
  rows=[]
  for r in industry['rows']:
   keys=[source_session(i) for i in r.get('sessionIds',[])]
   if 'externalIndex' in r:
    keys=[source_external(external_wealth_url(r['externalIndex']))]
    if r['externalIndex']==1:keys.append(source_external('https://www.ubs.com/global/en/our-firm/what-we-do/technology/innovation-and-ai.html'))
   links=' · '.join(f'<a href="{H(SOURCES[k]["url"])}" target="_blank" rel="noopener noreferrer">{H(k)}</a>' for k in keys)
   rows.append('<tr><td><b>'+H(r['firm'])+'</b><br>'+H(r['segment'])+'</td><td>'+H(r['work'])+'</td><td>'+H(r['maturity'])+'<span class="limit">'+H(r['limit'])+'</span></td><td>'+links+'</td></tr>')
  return '<div class="table-scroll"><table class="reader-appendix-table"><thead><tr><th scope="col">Firm / context</th><th scope="col">Recorded work</th><th scope="col">Maturity and limits</th><th scope="col">Source</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'
 if lid=='appendix-sources':return '<div class="source-catalog-grid">'+''.join(source_html(k) for k in SOURCES)+'</div>'
 return ''

def recording_extra(s):
 ids=s.get('recordingIds',[])
 if s['id']=='appendix-atlas':ids=list(RECS)
 if not ids:return ''
 return '<section class="recording-deepdives"><h3>Released-source learning notes</h3>'+''.join('<article class="reader-evidence"><h4>'+H(RECS[i]['company'])+'</h4><p>'+H(RECS[i]['mechanism'])+'</p><p><b>Use the method:</b> '+H(RECS[i]['practice'])+'</p><p><b>Scope:</b> '+H(RECS[i]['limit'])+'</p><p><a href="'+H(RECS[i]['url'])+'" target="_blank" rel="noopener noreferrer">'+H(RECS[i]['evidence'])+' ↗</a>'+(' · <a href="'+H(RECS[i]['watch'])+'" target="_blank" rel="noopener noreferrer">Watch at session start ↗</a>' if RECS[i].get('watch') else '')+'</p></article>' for i in ids)+'</section>'

SOURCES={};SESSION_KEYS={};EXTERNAL_KEYS={}
def source_session(sid):
 if sid in SESSION_KEYS:return SESSION_KEYS[sid]
 assert sid in program,sid
 s=program[sid];key='S%02d'%(len(SESSION_KEYS)+1);SESSION_KEYS[sid]=key
 speaker='; '.join(x['name']+' · '+x['company'] for x in s['speakers'])
 if sid in NOTE_IDS:
  desc=('Day2 metadata checked October 14; ' if sid in DAY2_IDS else 'Day1 metadata from the October 10 snapshot; ')+speaker+'. The program identifies the talk; the attendee notes supply the claims. No outcome was independently verified.'
  kind='ATTENDEE ACCOUNT + SESSION METADATA'
  if sid=='e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa':desc+=' Notes/October 10 say Comet; October 14 schedule says NatWest. The discrepancy is unresolved.'
 else:desc='October 10 program snapshot; '+speaker+'. This is advertised content, not a claim of attendance, independent verification, or current universal deployment.';kind='PROGRAM CONTEXT'
 SOURCES[key]={'title':s['title'],'url':SC+sid,'kind':kind,'description':desc,'sessionId':sid};return key
EXT_META={
 'https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch':('Morgan Stanley Wealth Management · Debrief launch','FIRM DISCLOSURE · 2024-06-26','Historical company release: Assistant adoption and Debrief features. Adoption does not establish Debrief-wide effectiveness or causal ROI.'),
 'https://www.ubs.com/global/en/media/display-page-ndp/en-20250204-4q24-quarterly-result.html':('UBS · fourth-quarter/full-year 2024 results','FIRM DISCLOSURE · 2025-02-04','Historical advisor rollout of Red; scale does not establish quality or client outcomes. Results media release page6 supports the described knowledge use case.'),
 'https://www.rbc.com/investor-relations/_assets-custom/pdf/investorday2025_presentation.pdf#page=95':('RBC · 2025 Investor Day presentation','FIRM DISCLOSURE · 2025-03-27','Slide95: Advisor Assist, survey use/satisfaction, and a separately footnoted US pilot conversion measure. Endnote slide226. These are not causal firm-wide revenue estimates.'),
 'https://www.rbc.com/investor-relations/_assets-custom/pdf/investorday2025_transcript.pdf#page=20':('RBC · 2025 Investor Day transcript','FIRM DISCLOSURE · 2025-03-27','Page20: executive account of early US advisor meeting-preparation assistance. No independent performance validation.'),
 'https://www.ubs.com/global/en/our-firm/what-we-do/technology/innovation-and-ai.html':('UBS · Innovation and AI','UNDATED FIRM PAGE · OBSERVED 2026-10-10','Corporate descriptions of Red and STAAT Insights. Publication date is unknown; employee and advisor populations differ. Preparation savings are estimates and identified opportunities are not completed sales.'),
 'https://arxiv.org/html/2107.03374v2':('Chen et al. · Evaluating Large Language Models Trained on Code','PRIMARY METHOD PAPER · 2021','Primary reference for pass@k and candidate-selection distinctions. No numerical model result from the paper is transferred to financial workflows here.')}
EXT_META.update({r['url']:(r['company']+' · '+r['title'],r['evidence'].upper()+' · REVIEWED 2026-10-25',r['limit']) for r in RECORDING['records']})
RECORDING_URLS={r['url'] for r in RECORDING['records']}
def external_wealth_url(ix):return wealth[ix]['additionalSources'][0]['sourceUrl'] if ix==1 else wealth[ix]['sourceUrl']
def source_external(url):
 parsed=urlparse(url)
 if 'ai.engineer' in parsed.netloc and 'session' in parse_qs(parsed.query):return source_session(parse_qs(parsed.query)['session'][0])
 if url in EXTERNAL_KEYS:return EXTERNAL_KEYS[url]
 assert url in EXT_META,url
 key='E%02d'%(len(EXTERNAL_KEYS)+1);EXTERNAL_KEYS[url]=key;t,k,d=EXT_META[url];SOURCES[key]={'title':t,'url':url,'kind':k,'description':d}
 if url in RECORDING_URLS:
  r=next(r for r in RECORDING['records'] if r['url']==url)
  SOURCES[key].update({f:r[f] for f in ['watch','transcript','company','evidence'] if f in r})
 return key

def source_html(k):
 src=SOURCES[k]
 extra=' · '.join(f'<a href="{H(src[f])}" target="_blank" rel="noopener noreferrer">{label}</a>' for f,label in [('watch','Watch at session start'),('transcript','Transcript')] if src.get(f))
 return f'<article class="source-item"><span class="source-id">{H(k)} · {H(src["kind"])}</span><a href="{H(src["url"])}" target="_blank" rel="noopener noreferrer">{H(src["title"])}</a><p>{H(src["description"])}</p>'+('<p>'+extra+'</p>' if extra else '')+'</article>'

def source_footnote(s):
 if len(s['sourceKeys'])>8:return 'Company cases, primary disclosures and method references'
 labels=[]
 for key in s['sourceKeys']:
  src=SOURCES[key]
  if 'sessionId' in src:
   sid=src['sessionId']
   label='Banking session' if sid=='e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa' else ' / '.join(dict.fromkeys(x['company'] for x in program[sid]['speakers']))
  else:
   label=src['title'].split(' · ')[0]
   if 'Morgan Stanley' in label:label='Morgan Stanley (2024)'
   elif label=='UBS':label='UBS (2025)' if '2025' in src['kind'] else 'UBS'
   elif label=='RBC':label='RBC (2025)'
   elif label=='Chen et al.':label='Chen et al. (2021)'
  if label not in labels:labels.append(label)
 return 'Sources: '+ ' · '.join(labels) if labels else 'Conference synthesis'

def load_slides():
 story=json.loads((W/'presentation_story_sections.json').read_text())['slides'];ground=json.loads((W/'presentation_grounding_workflows.json').read_text());evals=json.loads((W/'presentation_evals.json').read_text())
 front=[{'id':'opening-cover','chapter':'opening','title':'From AI capability to dependable work','layout':'cover','points':[],'visualData':{},'readerNotes':['This presentation consolidates pre-conference research and twelve identified attendee-note sets from AI Engineer NYC 2026. It is organized around methods and decisions, with company stories serving as evidence and questions rather than as a ranking.','The live path is planned for 40 minutes plus discussion. Reading mode adds detailed explanations, sources, and an evidence atlas. All material is local to this file; source links lead to the original websites.'],'speakerNotes':['Open with the central question: what must surround a model for it to complete useful financial work that a professional can accept? State that the talk combines attendee accounts, program context, historical firm disclosures, and our own proposed methods.'],'sourceIds':[],'externalSources':[]}, {'id':'opening-map','chapter':'opening','title':'Five chapters connect business value to engineering practice','layout':'roadmap','points':[],'visualData':{},'readerNotes':['The argument starts with valuable work, then follows the evidence and control requirements through evaluation, reliable execution, and professional growth. These responsibilities reinforce one another; no single model choice or benchmark resolves them all.'],'speakerNotes':['Preview the five chapters. Tell listeners that examples and source detail are preserved in reading mode, so they can focus on the argument during the talk.'],'sourceIds':[],'externalSources':[]}]
 sections=[('strategy',[x for x in story if x['id'].startswith('strategy')]),('grounding',[x for x in ground if x['id'].startswith('grounding')]),('evals',evals),('workflows',[x for x in ground if x['id'].startswith('workflows')]),('growth',[x for x in story if x['id'].startswith('growth')]),('closing',[x for x in story if x['id'].startswith('conclusion')])]
 slides=front
 for chapter,ss in sections:
  for s in ss:s['chapter']=chapter;slides.append(s)
 for s in slides:s['core']=True
 appendix=[
 ('appendix-evidence','An implementation contract connects requirements to observable behavior','appendix-evidence',{},['The checklist connects five responsibilities that are often assessed separately: task acceptance, evidence quality, action authority, evaluation and operation. Review them as one workflow so a correct-looking artifact cannot conceal a wrong source, unauthorized step or unreproducible release decision.','Use the contract to make disagreements concrete. A domain expert defines acceptable completion; data and engineering owners identify source semantics and enforceable boundaries; reviewers agree which failures block acceptance and what evidence permits a scoped change.','The checklist is an illustrative synthesis of the conference mechanisms. The source catalog preserves company attribution and historical dates; it does not turn a design pattern into independently verified business effectiveness.']),
 ('appendix-atlas','Compare the mechanism and maturity of each company story','appendix-atlas',{},['The atlas preserves all 25 firm perspectives from the consolidated industry research, including cases with sparse October 10 abstracts. These are selected, uneven, self-reported examples, not an industry survey or a ranking of frontier maturity.','A company affiliation or protocol-panel appearance is not evidence that the company deployed every named technique or vendor. A detailed mechanism, large user count, or pilot outcome also leaves quality, full operating cost, and causal business impact unresolved.']),
 ('appendix-eval-spec','A compact evaluation contract makes choices reviewable','appendix-eval-spec',{'code':'task: draft_review_packet\nsnapshot: approved_inputs_v1\nacceptance: reviewed_complete_output\ncritical: [unauthorized_access, unsupported_number]\ncases: [common, missing, difficult, regression]\njudge: model + rubric + threshold + version\ncompare: baseline_vs_candidate\ndecision: accountable_owner'},['This is an illustrative schema for discussion, not a runnable framework. The purpose is to make the task, input snapshot, acceptance criteria, critical failures, case coverage, evaluator configuration, and release decision explicit.','The schema should be adapted to the particular decision. Choosing a model, reducing human review, and expanding action authority require different evidence. A finite assessment suite provides bounded evidence, not proof of absence of failure.']),
 ('appendix-claim','A typed claim preserves context and calculation lineage','appendix-claim',{'code':'entity: AsterCo  # invented\nmetric: annual_revenue_growth\nperiod: FY2025\nunit: ratio\nvalue: 0.20\ninputs: D1=100; D3=120  # USD_m\nas_of: 2026-03-01\ncalculation: (120 - 100) / 100'},['The contract is an illustrative design requirement informed by Kepler and Bridgewater. It does not claim that either firm implemented exactly these fields or checks.','A verified number can still be used in a wrong comparison. Preserve entity, metric definition, period, units/currency, source version, available-as-of time, and the calculation inputs and operations. The AsterCo values and documents are invented.']),
 ('appendix-passk','At least one passing candidate is only part of the deployed task','appendix-passk',{},['The primary HumanEval paper defines pass@k as an at-least-one-success benchmark across sampled candidates under a specified test and discusses candidate selection. This presentation borrows the metric distinction, not a code-benchmark performance result for finance.','A deployed workflow must identify and accept a usable answer, comply with critical conditions, and account for the costs of all attempts, verification, and review. Partial-credit task quality, pass@k, first-attempt success, and selected-output reliability should not be used interchangeably.']),
 ('appendix-measures','Agree the denominator before celebrating the result','appendix-measures',{},['These are proposed measurement definitions. Define the population and exclusions in advance, record full workflow costs, and compare equivalent work at an agreed quality.','Contour’s notes call the approach A/B testing and describe a three-month tracking window, but assignment, sample size, controls, and causal estimates were not captured. Do not treat that window as sufficient validation for every financial workflow.']),
 ('appendix-unknowns','Keep uncertainty specific enough to investigate','appendix-unknowns',{},['The source notes preserve unresolved terms such as “crunchable” and “roundedness”; these have not been silently corrected into a provider or safety metric. The Bridgewater reactive/proactive wording reverses once. Workbench examples suggest proactive attention guidance, but the terminology remains to verify.','Sonar’s roughly50k-line codebase example lacks model, workload, metric, and benchmark conditions. Its confidence multiplication is a conceptual framing. Kepler’s retrieval settings are incompletely captured. None is a universal engineering threshold or a calibrated assurance formula.','The failure study’s recorded expected-loss product has undefined events, conditional relationships, and severity units. Incident rankings and exponential growth claims lack denominators and methods in the notes. These are follow-up topics, not established prevalence or expected-loss estimates.']),
 ('appendix-sources','Follow the sources—and retain their boundaries','appendix-sources',{},['The catalog below includes each source used in the core presentation and the evidence atlas. Official session links identify talks; attendee notes remain the source of the captured live claims. Program-only cases are marked as context.','The method paper and firm disclosures are primary external references. Historical releases are not claims about a firm’s latest state, and company-reported outcomes are not independent validation.'])]
 for sid,title,lid,v,notes in appendix:
  slides.append(dict(id=sid,chapter='appendix',title=title,layout=lid,points=[],visualData=v,readerNotes=notes,speakerNotes=['Use this reference page for a follow-up question or later study; it is outside the timed 40-minute path.'],sourceIds=[],externalSources=[],minutes=0,core=False))
 # Link appendix methods to their motivating sources.
 mapping={'appendix-eval-spec':['4607dbbe-8f94-4b0e-91ce-257d1cfb5448','9d72d7ac-a2a2-42cf-b880-5859316d840c'],'appendix-claim':['2d29f925-f16b-41b3-8086-de0524829cbe','a84ca3a8-cc2f-4b50-a635-fc380f6f04f6'],'appendix-measures':['ae273f0b-db0f-4638-8ae3-05874bebf9ca'],'appendix-unknowns':['02f94835-c29d-4cf5-b77a-c5a491b747b8','a84ca3a8-cc2f-4b50-a635-fc380f6f04f6','4add802c-6a68-4e9c-93fb-9c1e017193bc','9d72d7ac-a2a2-42cf-b880-5859316d840c','2d29f925-f16b-41b3-8086-de0524829cbe','e4ca10c6-c8b4-427b-a337-8d2a28e2a7aa']}
 for s in slides:
  if s['id'] in mapping:s['sourceIds']=mapping[s['id']]
  if s['id']=='appendix-passk':s['externalSources']=['https://arxiv.org/html/2107.03374v2']
 enrichment={}
 for name in ['enrichment-strategy-growth.json','enrichment-grounding-workflows.json','enrichment-evals.json','enrichment-structure.json']:
  part=json.loads((P/name).read_text())
  assert not(set(part)&set(enrichment)),name
  enrichment.update(part)
 for s in slides:
  if s['layout']=='cover':continue
  e=enrichment[s['id']]
  s.update(title=e['headline'],lead=e['lead'],insights=e['insights'])
  # Company evidence remains in the source registry; old face labels are obsolete.
  if isinstance(s['visualData'].get('cards'),list):
   for card in s['visualData']['cards']:card.pop('provenance',None)
 return slides

SLIDES=load_slides()
SLIDES[0]['readerNotes']=['This recording-enhanced edition combines twelve original attendee-note sets with a review of the AIE channel, its playlists, official timestamped transcripts and a separately identified Ryan Stevens article. The review screened 90 uploads and inspected 50 official video descriptions.','The 29-slide core remains planned for 40 minutes plus discussion. Read & learn adds company mechanisms, worked examples and source boundaries. No audiovisual viewing or independent validation of company results is claimed.']
for s in SLIDES:
 if s['id']=='appendix-unknowns':
  s['recordingIds']=['bridgewater','range','ramp-evals','ramp','kepler-breakout','kepler-14','vanguard-release']
  s['externalSources'] += [RECS[i]['url'] for i in s['recordingIds']]
  s['readerNotes']=['Recordings resolve the reversed Bridgewater reactive/proactive wording and provide its precision@10 account. Range ownership/reviewer responsibilities are now transcript-backed; Kepler explicitly retains final post-processing. Vanguard’s timing claim concerns mainframe-code research.','Keep Ramp’s keynote separate from Ryan Stevens’s written breakout account and Kepler’s breakout separate from its next-day follow-up. Range’s index label is October 13 while its attended notes remain Day 2; an index label is not an established filming date.','Banking affiliation and “roundedness,” uncertain provider spelling, exact breakout retrieval defaults and several result denominators remain unresolved. Do not turn a confidence metaphor or selected incident coverage into a calibrated assurance or prevalence estimate.']
  s['speakerNotes']=s['readerNotes'][:]
 if s['id']=='appendix-atlas':
  s['readerNotes']=['The company atlas now includes 37 released-source and written-follow-up briefs. It groups newly inspected mechanisms alongside original program and historical disclosure context, without upgrading earlier material by association.','Compare what each system actually does, what the professional still decides and which component remains experimental. A transcript establishes a speaker account; a description establishes its stated scope. Neither independently validates outcomes.']
  s['speakerNotes']=s['readerNotes'][:]
SCRIPT=json.loads((P/'presenter-script.json').read_text())
SPOKEN={s['slideId']:s for s in SCRIPT['sections']}
assert set(SPOKEN)=={s['id'] for s in SLIDES if s['core']}
for s in SLIDES:
 if s['core']:
  talk=SPOKEN[s['id']]
  s['minutes']=talk['minutes']
  s['speakerNotes']=talk['talkTrack']+[talk['transition']]
  s['deliveryCue']=talk['deliveryCue']
# Register every source before constructing HTML (counts and atlas must be stable).
for s in SLIDES:
 s['externalSources']=[u for u in s['externalSources'] if not('ai.engineer' in urlparse(u).netloc and '/schedule' in urlparse(u).path)]
 s['sourceKeys']=list(dict.fromkeys([source_session(i) for i in s['sourceIds']]+[source_external(u) for u in s['externalSources']]))
for row in industry['rows']:
 for sid in row.get('sessionIds',[]):source_session(sid)
 if 'externalIndex' in row:
  source_external(external_wealth_url(row['externalIndex']))
  if row['externalIndex']==1:source_external('https://www.ubs.com/global/en/our-firm/what-we-do/technology/innovation-and-ai.html')
for r in RECS.values():source_external(r['url'])
for s in SLIDES:
 if s['id'] in ['appendix-evidence','appendix-atlas','appendix-sources']:s['sourceKeys']=list(SOURCES)
 # Explicit per-slide provenance prevents vendor/practitioner inference from wording.
 labels=[]
 if any(i in NOTE_IDS for i in s['sourceIds']):labels.append('notes')
 if any(i not in NOTE_IDS for i in s['sourceIds']):labels.append('agenda')
 if any(u in RECORDING_URLS for u in s['externalSources']):labels.append('recording')
 if any(u not in RECORDING_URLS and 'arxiv' not in u for u in s['externalSources']):labels.append('disclosure')
 if s['id']=='workflows-04':labels.append('agenda')
 if s['layout'] in ['worked-example','synthetic-worked-rubric','judge-calibration-and-passk','worked-workflow','appendix-eval-spec','appendix-claim']:labels.append('synthetic')
 labels.append('synthesis');s['evidenceTypes']=list(dict.fromkeys(labels))
 s['evidenceNote']='Company mechanisms are recorded speaker accounts or program/disclosure claims. Practices and diagrams are proposed synthesis. Detailed boundaries and unresolved claims are preserved below.'
 if s['id']=='evals-03':s['evidenceNote']='Judge matrix is a proposed method; the three-attempt strip is synthetic. Ramp and the banking account are unverified notes; Upstart is program context. The method paper supports the pass@k distinction.'
 if s['layout'] in ['worked-example','synthetic-worked-rubric','worked-workflow','appendix-eval-spec','appendix-claim']:s['evidenceNote']='Synthetic teaching example or illustrative contract. Invented values and workflows do not represent a firm result, client recommendation, or validated implementation.'
 if s['id'].startswith('appendix-'):s['evidenceNote']='Reference material outside the timed talk. Attendee accounts, dated program context, historical firm disclosures, and proposed methods retain separate evidence boundaries.'
 if s.get('recordingIds'):s['evidenceNote']='The October 25 review adds organizer transcripts, separately identified official video descriptions, and a speaker-bylined Ramp article. These establish source content, not independently validated company outcomes. Teaching examples and combined methods remain illustrative.'
 if s['id']=='strategy-03':s['evidenceNote']='Range, Arca and Perpetual: released practitioner accounts with explicit review/authority boundaries. Morgan Stanley 2024, UBS 2025 and RBC 2025 remain historical firm disclosures. Range’s online recording label differs from Day 2 attendance placement.'
 s['evidenceNote']=s['evidenceNote'].replace('Stanley2024','Stanley 2024').replace('UBS2025','UBS 2025').replace('RBC2025','RBC 2025')
 cumulative=0
for s in SLIDES:cumulative+=s['minutes'];s['cumulative']=cumulative
assert cumulative==40,cumulative
assert len({s['id'] for s in SLIDES})==len(SLIDES)

def render_slide(s,index):
 chapter,color=CHAPTERS[s['chapter']];is_cover=s['layout']=='cover'
 subtitle=f'<p class="slide-subtitle">{H(s["lead"])}</p>' if s.get('lead') else ''
 example_label='<span class="example-label">Illustrative example</span>' if 'synthetic' in s['evidenceTypes'] and not s['id'].startswith('appendix') else ''
 header=f'<header class="slide-header"><div class="eyebrow"><span class="dot" aria-hidden="true"></span>{H(chapter)}</div><h2 tabindex="-1" class="slide-title" id="title-{s["id"]}">{H(s["title"])}</h2>{subtitle}</header>'
 if is_cover:header=f'<header class="slide-header"><div class="eyebrow"><span class="dot" aria-hidden="true"></span>AI ENGINEER NYC 2026 / LEARNING BRIEFING</div></header>'
 refs='<ul>'+''.join(f'<li><a href="{H(SOURCES[k]["url"])}" target="_blank" rel="noopener noreferrer">{H(k)} · {H(SOURCES[k]["title"])}</a></li>' for k in s['sourceKeys'])+'</ul>' if s['sourceKeys'] else '<p>Editorial framing. See the source appendix for the evidence scope.</p>'
 practice='<aside class="practice"><h3>Practical takeaways</h3><ul>'+''.join('<li>'+H(x)+'</li>' for x in s['points'])+'</ul></aside>' if s['points'] else '<aside class="practice"><h3>Use this resource</h3><p>Every slide contains the argument, example and practical implications. Read & learn adds source context and reference material.</p><p>Source links open the original sites. The presentation itself works offline.</p></aside>'
 notes='<div class="reading-material"><div class="reading-notes"><div><h3>Explanation & evidence</h3>'+paras(s['readerNotes'])+'</div>'+practice+'</div>'+reader_extra(s)+recording_extra(s)+'<div class="reader-evidence"><b>Evidence boundary:</b> '+H(s['evidenceNote'])+'</div><details class="reader-speaker"><summary>Speaker notes</summary>'+paras(s['speakerNotes'])+'</details><div class="reader-references"><h3>Sources for this page</h3>'+refs+'</div></div>'
 label=f'{index+1:02} / {len([x for x in SLIDES if x["core"]]):02}' if s['core'] else 'A%02d'%(index-len([x for x in SLIDES if x['core']])+1)
 visual=body(s)
 if s.get('insights'):
  # The fuller analytical text replaces the earlier slogan/caveat strips.
  visual=re.sub(r'<div class="takehome">.*?</div>','',visual)
  visual=re.sub(r'<p class="small-note">.*?</p>','',visual)
 analysis='<div class="analysis-grid">'+''.join('<section class="analysis-item"><h3>'+H(x['title'])+'</h3><p>'+H(x['text'])+'</p></section>' for x in s.get('insights',[]))+'</div>' if s.get('insights') else ''
 footer_context=('Technical learning briefing · October 2026' if is_cover else source_footnote(s))
 return f'<article class="slide-unit {"dark" if is_cover else ""}" id="slide-{s["id"]}" data-slide="{s["id"]}" data-layout="{s["layout"]}" data-core="{str(s["core"]).lower()}" style="--accent:{color}" aria-labelledby="title-{s["id"]}"><div class="slide-card">{header}<div class="slide-body"><div class="slide-visual">{example_label}{visual}</div>{analysis}</div><footer class="slide-footer"><span class="source-footnote">{H(footer_context)}</span><div class="footer-controls"><button class="ref-button" type="button" aria-haspopup="dialog" aria-controls="sources-dialog" aria-label="Sources for {H(s["title"])}, {len(s["sourceKeys"])} references" data-sources="{s["id"]}">Sources</button><span class="slide-number">{label}</span></div></footer></div>{notes}</article>'

def build():
 rendered=''.join(render_slide(s,i) for i,s in enumerate(SLIDES))
 outline='';previous=None
 for i,s in enumerate(SLIDES):
  if s['chapter']!=previous:outline+='<li class="outline-group">'+H(CHAPTERS[s['chapter']][0])+'</li>';previous=s['chapter']
  label=f'{i+1:02}' if s['core'] else f'A{i-28:02}'
  outline+=f'<li><a href="#present/{s["id"]}" data-slide="{s["id"]}" aria-current="false"><span class="n">{label}</span><span>{H(s["title"])}</span></a></li>'
 payload=json.dumps({'slides':SLIDES,'sources':SOURCES,'durationMinutes':40,'coreCount':29},ensure_ascii=False).replace('</',r'<\/')
 css=(P/'deck.css').read_text();js=(P/'deck.js').read_text()
 htmltext=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="description" content="A 40-minute technical learning presentation on financial-services AI: strategy, groundedness, evaluation, reliable workflows, and professional growth. Includes reading mode, company evidence, speaker notes, and sources."><title>AI Engineer NYC 2026 · From capability to dependable work</title><style>{css}</style></head><body data-mode="read"><a class="skip" href="#main">Skip to presentation</a><header class="appbar"><div class="app-brand"><b>AI ENGINEER NYC 2026</b><br><span>Learning briefing / recordings reviewed October 25</span></div><nav class="bar-controls" aria-label="Presentation controls"><div class="segmented" role="group" aria-label="Viewing mode"><button class="mode-button" data-mode="present" type="button" aria-pressed="false">Present</button><button class="mode-button" data-mode="read" type="button" aria-pressed="true">Read & learn</button></div><button id="outline-toggle" type="button" aria-haspopup="dialog">Outline</button><button id="speaker-toggle" class="optional" type="button" aria-controls="speaker-panel" aria-expanded="false">Speaker notes</button><button id="fullscreen-toggle" class="optional" type="button">Fullscreen</button><button id="print-toggle" type="button">Print / PDF</button></nav></header><noscript><style>.bar-controls,.deckbar{{display:none}}</style><p class="noscript">JavaScript is disabled. The complete reading presentation and all source links remain available below.</p></noscript><main id="main" tabindex="-1"><h1 class="sr-only">AI Engineer NYC 2026: from capability to dependable work</h1><div class="reader-intro"><div class="label-note">A practical conference learning resource</div><h2>From AI capability to dependable work.</h2><p>A thematic synthesis for data scientists, AI engineers, and technical leads. The 29-slide core path is planned for 40 minutes plus discussion; eight appendix pages support deeper review.</p><p>This edition combines twelve attendee-note sets with released transcripts, official video descriptions, a separate Ramp written follow-up, historical disclosures and labeled teaching examples. Thirty-seven company/source briefs extend the reading material; evidence classes remain distinct.</p></div><div class="stage">{rendered}</div><aside class="speaker-panel" id="speaker-panel" aria-labelledby="speaker-title" hidden><h2 id="speaker-title">Speaker notes</h2><div id="speaker-content"></div></aside><footer class="reader-foot">Revised October 25, 2026 · A technical learning briefing for data scientists, AI engineers and technical leads · Recording-enhanced notes, primary written follow-up, dated disclosures and illustrative methods.</footer></main><footer class="deckbar" aria-label="Slide navigation"><button id="prev" class="nav-only" type="button">← Previous</button><div class="progress" aria-hidden="true"><span id="progress-fill"></span></div><span id="progress-status" class="status">Reading presentation</span><button id="next" class="nav-only primary" type="button">Next →</button><span id="time-status" class="time"></span><span class="hint">← → navigate · R read · P present · O outline</span></footer><dialog class="modal" id="outline-dialog" aria-labelledby="outline-title"><header class="modal-head"><h2 id="outline-title">Presentation outline</h2><button id="outline-close" type="button">Close</button></header><div class="modal-body"><p class="modal-note">Core: 40 minutes plus discussion. Appendix: optional evidence and methods. Select a page to jump.</p><ol class="outline-list" id="outline-list">{outline}</ol></div></dialog><dialog class="modal" id="sources-dialog" aria-labelledby="sources-title"><header class="modal-head"><h2 id="sources-title">Evidence & sources</h2><button id="sources-close" type="button">Close</button></header><div class="modal-body" id="source-list"></div></dialog><div id="live-status" class="sr-only" role="status" aria-live="polite" aria-atomic="true"></div><div class="toast" id="toast" role="status" aria-live="polite" hidden></div><script type="application/json" id="deck-data">{payload}</script><script>{js}</script></body></html>'''
 O.mkdir(exist_ok=True);out=O/'ai-engineer-nyc-2026-presentation.html';out.write_text(htmltext)
 (P/'deck-data.json').write_text(json.dumps({'slides':SLIDES,'sources':SOURCES,'durationMinutes':40},indent=2,ensure_ascii=False))
 print(json.dumps({'output':str(out),'coreSlides':sum(s['core'] for s in SLIDES),'appendixPages':sum(not s['core'] for s in SLIDES),'minutes':sum(s['minutes'] for s in SLIDES),'sources':len(SOURCES),'bytes':out.stat().st_size},indent=2))
if __name__=='__main__':build()
