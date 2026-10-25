"""Day 1 content shared by the Markdown synthesis and HTML report."""
from pathlib import Path
import json, html
from recording_content import daily_update
W=Path(__file__).resolve().parent
NOTES=json.loads((W/'day1_notes_data.json').read_text())
SYNTH=json.loads((W/'day1_learning_synthesis.json').read_text())
SESSIONS=NOTES['sessions']
LEARNINGS=SYNTH['learnings']
LEARNINGS[0]['synthesis']=LEARNINGS[0]['synthesis'].replace('reaching people through familiar channels','drawing on familiar information channels')
LEARNINGS[2]['practicalTips'][2]='Turn a found failure into a regression case, then verify the fix against that case and a separate assessment set.'
H=lambda s:html.escape(str(s),quote=True)
SOURCE_URL='https://ai.engineer/nyc/2026/schedule?session='
BY_D1={f'D1-{i:02}':s for i,s in enumerate(SESSIONS,1)}
EVIDENCE='All seven named sessions were marked “Speaker claim” in the supplied notes. Vault and Two Sigma were marked production, speaker-reported; the other five were marked unclear. No result is upgraded to independently checked or internally validated evidence.'
APPLICATIONS=[
 {'title':'Socrates text2SQL','hypothesis':'Correctly executing SQL and correctly answering a business question are different outcomes. A traceable query/result path and risk-weighted review could help evaluate the whole task.','test':'Compare a small representative set of questions with authoritative expected results against the current query workflow on the same data snapshot. Include ambiguous definitions, wrong periods, duplicate joins, wrong grain, missing data, and access-denied cases. Keep assessment cases separate from tuning.','measure':'Business-meaning and result correctness; important numerical errors; appropriate clarification or abstention; accepted completion; review/rework time; cost per accepted task.','limit':'This is a proposed test, not a description of Socrates’ current architecture or a finding that it lacks any capability.'},
 {'title':'Sales meeting-preparation agent','hypothesis':'A focused, evidence-grounded brief delivered at the right time may help preparation, while proactive delivery can also increase noise.','test':'Compare current preparation with an agent brief on the same approved historical or synthetic cases and an explicit information cutoff. Review factual support, relevant omissions, and usefulness. Test delivery timing separately from content quality.','measure':'Accepted brief quality; wrong-client or unsupported claims; important missed developments; freshness; relevance/noise; preparation plus review time; cost per accepted brief.','limit':'Preparation benefits do not establish better forecasts or incremental sales. The current implementation, intended user group, and performance are not assumed.'}
]
FOLLOWUPS=[
 'Bridgewater: confirm the reactive/proactive wording; obtain retrieval task definitions, benchmark results, and evidence on feed usefulness.',
 'Two Sigma: clarify the risk-scoring rubric, enforcement points, and approval-classifier false negatives and interruption burden.',
 'Failure study: obtain incident selection/labeling methods, denominators, and the exact definitions and conditioning of the loss heuristic.',
 'Contour: clarify assignment or matching, the definition of useful insight, the three-month observation window, and full cost accounting.',
 'Kepler: clarify deterministic verification scope, citation-repair failure behavior, and the exact meaning/order of the retrieval settings.',
 'Arize: verify the product and evaluator-skill names and ask how diagnostic accuracy and proposed fixes are evaluated.',
 'Closing reflection: identify the source and the unnamed study before presenting either as an attributed empirical finding.'
]

def markdown():
    out=['# '+NOTES['title'],'**Date:** Tuesday, October 13, 2026  \n**For:** Principal Data Scientist, Fidelity Investments  \n**Basis:** Seven session-note sets supplied by the attendee, plus an unattributed closing reflection.','## Executive synthesis',*NOTES['executive'],'## Evidence and reading conventions',EVIDENCE,'Session descriptions below distinguish what the notes record from editorial takeaways, proposed tests, and unanswered questions. Blank or prefilled questions in the raw notes are not treated as answered. Official schedule links identify sessions; they do not verify the details captured in attendance.','## Seven cross-session learnings']
    for i,l in enumerate(LEARNINGS,1):
        links=', '.join(f'[{sid} · {BY_D1[sid]["speaker"].split(" · ")[-1]}]({SOURCE_URL}{BY_D1[sid]["id"]})' for sid in l['sessions'])
        out += [f'### {i}. {l["title"]}',l['synthesis'],'**Practical tips:**',*['- '+x for x in l['practicalTips']],'**Evidence limit:** '+l['limit'],'**Sessions:** '+links]
    out+=['## Coherent session notes']
    for i,s in enumerate(SESSIONS,1):
        out += [f'### D1-{i:02} · {s["title"]}',f'**Speaker/company:** {s["speaker"]}  \n**Time:** October 13, 2026 · {s["time"]}  \n**Room:** {s["room"]}  \n**Evidence:** Speaker claim  \n**Maturity:** {s["maturity"]}  \n**Official session:** [{s["title"]}]({SOURCE_URL}{s["id"]})','**Central idea:** '+s['centralIdea'],'#### What the notes record',*['- '+x for x in s['observations']],'#### Takeaway',s['takeaway'],'#### Practical tips',*['- '+x for x in s['tips']],'#### Limits and unresolved details',s['limits'],'#### Questions to pursue',*['- '+x for x in s['questions']]]
    r=NOTES['closingReflection']
    out+=['## Unattributed closing reflection: '+r['title'],'**Attribution:** '+r['attribution'],*['- '+x for x in r['ideas']],'**Evidence limit:** '+r['limit'],'## Tensions worth retaining in the team report','- **Recall versus attention:** broader agent retrieval may help coverage, while human-facing feeds still need precision, timeliness, and limited noise.','- **Automation versus oversight:** an approval classifier may reduce interruption burden and can also miss consequential cases. Evaluate both sides.','- **Disposable software versus durable consequence:** a short-lived tool can still expose data or produce a consequential wrong answer. Maintenance needs and immediate risk require separate judgments.','- **Citation support versus correctness:** deterministic arithmetic and a valid citation do not by themselves establish that the entity, period, definition, or interpretation is correct.','- **Adoption versus value:** usage, useful outputs, process efficiency, and attributable financial impact require different measures.','## Optional application hypotheses from your notes','These respond to the questions you raised about Socrates and sales meeting preparation. They are proposals for discussion, not commitments or claims about your current systems.']
    for a in APPLICATIONS:
        out += ['### '+a['title'],'**Hypothesis:** '+a['hypothesis'],'**Smallest useful comparison:** '+a['test'],'**Measures:** '+a['measure'],'**Limit:** '+a['limit']]
    out+=['## Priority follow-ups',*['- '+x for x in FOLLOWUPS],'## Suggested team readout','1. Lead with three findings: task-specific information access, risk-based operating controls/evaluation, and counterfactual value measurement.','2. Explain the Bridgewater, Two Sigma, and Contour mechanisms, then use Kepler to make numerical trust concrete.','3. Discuss the durability and oversight tradeoffs rather than presenting every technique as universally beneficial.','4. Close with proposed evaluation questions and the evidence still missing. Day 2 can strengthen, qualify, or revise the argument.','## Source and editorial notes','Primary source: the attendee’s pasted Day 1 notes, supplied October 13, 2026. The wording has been corrected for spelling and organized for coherence. Ambiguous details remain explicit. No slides, recordings, datasets, product documentation, or independent results were inspected for this synthesis. Session metadata matches the previously saved official program; the schedule has not been newly verified.','The raw notes remain the underlying record. In particular, the reactive/proactive reversal, the undefined expected-loss terms, the unspecified A/B design, the recorded retrieval settings, and the unverified product/skill names have not been silently resolved.']
    return '\n\n'.join(out)+'\n'+daily_update(1)

def render_html(refs):
    lead='<div class="day1-lessons">'
    for i,l in enumerate(LEARNINGS,1):
        ids=[BY_D1[x]['id'] for x in l['sessions']]
        lead+=f'<article class="day1-lesson"><span class="lesson-num">{i:02}</span><h3>{H(l["title"])}</h3><p>{H(l["synthesis"])}</p><ul>{"".join("<li>"+H(x)+"</li>" for x in l["practicalTips"])}</ul><p class="day1-limit"><b>Limit:</b> {H(l["limit"])}</p><div class="day1-source">Attendee notes · {refs(ids,True)}</div></article>'
    lead+='</div>'
    session_html=''
    for i,s in enumerate(SESSIONS,1):
        session_html+=f'<details class="day1-session source-details" id="day1-session-{i}"><summary><span class="day1-session-num">D1-{i:02}</span><span>{H(s["title"])}<small>{H(s["speaker"])} · {H(s["time"])}</small></span><span class="pill">Speaker claim</span></summary><div class="day1-session-body"><p class="day1-meta"><b>Room:</b> {H(s["room"])} · <b>Maturity:</b> {H(s["maturity"])}</p><p class="day1-central">{H(s["centralIdea"])}</p><h4>What the notes record</h4><ul>{"".join("<li>"+H(x)+"</li>" for x in s["observations"])}</ul><div class="grid2"><div><h4>Takeaway · synthesis</h4><p>{H(s["takeaway"])}</p><h4>Practical tips</h4><ul>{"".join("<li>"+H(x)+"</li>" for x in s["tips"])}</ul></div><div><h4>Evidence limits</h4><p>{H(s["limits"])}</p><h4>Questions to pursue</h4><ul>{"".join("<li>"+H(x)+"</li>" for x in s["questions"])}</ul></div></div><div class="day1-source">Session identifier: {refs([s["id"]])}. Mechanism details above are from attendee notes.</div></div></details>'
    applications=''.join(f'<article class="panel"><div class="eyebrow teal">Optional application hypothesis</div><h3>{H(a["title"])}</h3><p>{H(a["hypothesis"])}</p><h4>Smallest useful comparison</h4><p>{H(a["test"])}</p><h4>Measures</h4><p>{H(a["measure"])}</p><p class="day1-limit">{H(a["limit"])}</p></article>' for a in APPLICATIONS)
    reflection=NOTES['closingReflection']
    return f'''<section id="day1"><div class="section-head"><div class="section-no">02 / DAY 1 · OCTOBER 13</div><h2>Seven sessions, one operating story.</h2><p>These are substantive learnings synthesized from your notes. The detailed session records are expandable; each keeps its reported mechanism, practical takeaway, limits, and follow-up questions together.</p></div><div class="coverage-badges"><span class="pill">7 named session-note sets</span><span class="pill">All evidence: speaker claim</span><span class="pill">2 production labels · speaker-reported</span><span class="pill">1 unattributed closing reflection</span></div><div class="day1-flow" aria-label="Day 1 synthesis workflow"><div><b>Information</b><span>Scope, retrieve, ground</span></div><div><b>Authority</b><span>Own, constrain, escalate</span></div><div><b>Evaluation</b><span>Seek failures, verify repairs</span></div><div><b>Value</b><span>Compare, accept, measure</span></div></div><details class="day1-retrospective source-details"><summary>Day 1 cross-session learning record · October13</summary>{lead}</details><h3 style="margin-top:34px">Session-by-session synthesis</h3><p class="small muted">Open a session for the coherent notes. Original unanswered prompts remain questions rather than findings.</p>{session_html}<article class="panel day1-reflection"><div class="eyebrow teal">Closing reflection · speaker/source not captured</div><h3>{H(reflection["title"])}</h3><ul>{"".join("<li>"+H(x)+"</li>" for x in reflection["ideas"])}</ul><p class="day1-limit">{H(reflection["limit"])}</p></article><h3 style="margin-top:32px">Two application questions you raised</h3><p class="small muted">These are bounded proposals for discussion. They do not assume your systems’ current architecture, performance, or roadmap.</p><div class="grid2 day1-applications">{applications}</div><details class="day1-followups source-details"><summary>Priority follow-ups to strengthen the report</summary><ul>{"".join("<li>"+H(x)+"</li>" for x in FOLLOWUPS)}</ul></details></section>'''

def theme_note(theme_id):
    ss=[s for s in SESSIONS if theme_id in s['themeLinks']]
    if not ss:return '<div class="day1-theme-update"><b>Coverage:</b> No direct session notes supplied for this theme. The content below remains the October 10 agenda-based perspective.</div>'
    return '<div class="day1-theme-update"><b>Day 1 update · attendee notes:</b><ul>'+''.join(f'<li>{H(s["takeaway"])} <a href="#day1-session-{SESSIONS.index(s)+1}">{H(s["speaker"].split(" · ")[-1])} notes ↗</a></li>' for s in ss)+'</ul><p>The case descriptions below retain their original program-source status; they are not all attended or verified.</p></div>'

if __name__=='__main__':
    out=W.parent/'outputs'/'ai-engineer-nyc-2026-day-1-notes.md'
    out.write_text(markdown())
    print(f'Saved coherent Day 1 Markdown synthesis: {out} ({out.stat().st_size:,} bytes)')
