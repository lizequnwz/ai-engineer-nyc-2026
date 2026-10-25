"""Day 2 notes and the combined conference synthesis."""
from pathlib import Path
import json,html
from recording_content import daily_update
from urllib.parse import urlparse,parse_qs
from day1_report_content import NOTES as DAY1
W=Path(__file__).resolve().parent
NOTES=json.loads((W/'day2_notes_data.json').read_text())
SYNTH=json.loads((W/'day2_learning_synthesis.json').read_text())
SESSIONS=NOTES['sessions'];LEARNINGS=SYNTH['learnings']
H=lambda s:html.escape(str(s),quote=True)
URL='https://ai.engineer/nyc/2026/schedule?session='
BY_ID={s['id']:s for s in DAY1['sessions']+SESSIONS}
BY_SOURCE={f'D1-{i:02}':s for i,s in enumerate(DAY1['sessions'],1)}
for source in SYNTH['day2Sources']:
 sid=parse_qs(urlparse(source['sourceUrl']).query)['session'][0]
 BY_SOURCE[source['id']]=BY_ID[sid]
def note_anchor(s):
 for day,items in [('day1',DAY1['sessions']),('day2',SESSIONS)]:
  for i,item in enumerate(items,1):
   if item['id']==s['id']:return f'{day}-session-{i}'
 raise ValueError(s['id'])
EVIDENCE='Five Day 2 session-note sets are identified. Sonar, OpenAI, and the banking session explicitly record Speaker claim and unclear maturity. Ramp and Range have no explicit evidence/maturity fields in the raw notes; they remain unverified attendee-reported speaker accounts. Range was identified through your company clarification and the current official program. No implementation or result is upgraded to independently checked evidence.'

def markdown():
 out=['# '+NOTES['title'],'**Date:** Wednesday, October 14, 2026  \n**For:** Principal Data Scientist, Fidelity Investments  \n**Scope:** New Day 2 material only; the attachment’s repeated Day 1 notes are not counted again.','## Executive synthesis',*NOTES['executive'],'## Evidence and attribution',EVIDENCE,'Session links identify the talks. The October14 official schedule was checked for the five Day2 records; it confirms Range and the updated Ramp title. The banking speaker affiliation differs: the notes and October10 snapshot say Comet, while the October14 program says NatWest. The discrepancy remains unresolved and is not used to assign the Cora example to a bank.','## Coherent session notes']
 for i,s in enumerate(SESSIONS,1):
  out += [f'### D2-{i:02} · {s["title"]}',f'**Speaker/company:** {s["speaker"]}  \n**Time:** October 14, 2026 · {s["time"]}  \n**Room:** {s["room"]}  \n**Evidence:** {s["evidence"]}  \n**Maturity:** {s["maturity"]}  \n**Official session:** [{s["title"]}]({URL}{s["id"]})','**Central idea:** '+s['centralIdea'],'#### What the notes record',*['- '+x for x in s['observations']],'#### Takeaway · editorial synthesis',s['takeaway'],'#### Practical tips · proposed practices',*['- '+x for x in s['tips']],'#### Evidence limits',s['limits'],'#### Questions to pursue',*['- '+x for x in s['questions']]]
 out+=['## How Day 2 develops the Day 1 learnings']
 for i,l in enumerate(LEARNINGS,1):
  sources=[BY_SOURCE[k] for k in l['sources']]
  out += [f'### {i}. {l["title"]}',l['synthesis'],'**Practical implications:**',*['- '+x for x in l['practicalTips']],'**Limit:** '+l['limit'],'**Sessions:** '+', '.join(f'[{s["title"]}]({URL}{s["id"]})' for s in sources)]
 out+=['## Three messages for the team report']
 for i,r in enumerate(SYNTH['reportBackMessages'],1):out += [f'### {i}. {r["headline"]}',r['message'],'**Evidence boundary:** '+r['evidenceBoundary']]
 out+=['## Priority follow-ups',*['- '+x for x in NOTES['followups']],'## Editorial and source notes','Primary content source: your pasted Day2 notes, supplied October14, 2026, and your subsequent clarification that the financial-planning company was Range. Session metadata was matched to the official conference schedule refreshed October14. Speaker claims, official program facts, our interpretations, and proposed tests are kept distinct.','The raw notes’ uncertain terms—“crunchable” and “roundedness”—remain unresolved. The 50k-line code example, eight-to-four skill bundle, and 100K/day conversation volume are preserved as contextual claims, not universal thresholds or verified outcomes. Prefilled questions about approval evidence, release/rollback, and judge validation remain unanswered.','No slide deck, recording, benchmark dataset, product specification, deployment, or financial outcome was independently verified.','Official schedule: [AI Engineer NYC 2026](https://ai.engineer/nyc/2026/schedule).']
 return '\n\n'.join(out)+'\n'+daily_update(2)

def render_combined(refs):
 cards=''
 for i,l in enumerate(LEARNINGS,1):
  ss=[BY_SOURCE[x] for x in l['sources']]
  cards+=f'<article class="crossday-lesson day1-lesson"><span class="lesson-num">{i:02}</span><h3>{H(l["title"])}</h3><p>{H(l["synthesis"])}</p><ul>{"".join("<li>"+H(x)+"</li>" for x in l["practicalTips"])}</ul><p class="day1-limit"><b>Evidence limit:</b> {H(l["limit"])}</p><div class="day1-source">Across both days · {refs([s["id"] for s in ss],True)}</div></article>'
 comparisons=[('Information → completed work','Bridgewater: sources, ontology, time scoping, different human/agent needs.','Range: practitioner-authored skills; OpenAI: inspectable sources and useful artifacts.','Assess the reviewed analysis, meeting brief, or artifact, including missing facts and corrections.'),('Controls → prevention + verification','Two Sigma: registration, access boundaries, approval triage.','Sonar: intent, guardrails, independent checks, repeatable evidence.','Give preventive constraints and verification different responsibilities; measure coverage and exceptions.'),('Evaluation → a quality vector','Failure study and Arize: risk-based tests, traces, improvement.','Ramp: task success and ablations; banking session: quality dimensions and configured judges.','Keep critical failures, task completion, experience, judge errors, and repeated-attempt costs visible.'),('Usage → accepted capacity and value','Contour: comparisons, useful insight, costs and outcomes.','Range: parallel drafting with planner review.','Measure accepted capacity and total human effort before claiming better advice, revenue, or ROI.')]
 table=''.join('<tr>'+''.join('<td>'+H(x)+'</td>' for x in row)+'</tr>' for row in comparisons)
 return f'<section id="synthesis"><div class="section-head"><div class="section-no">02 / TWO-DAY SYNTHESIS</div><h2>What the two days add up to.</h2><p>Seven conclusions connect the notes across firms and sessions. Each is a proposed operating lesson, with practical techniques and the limits of the evidence attached.</p></div><div class="day1-lessons crossday-lessons">{cards}</div><h3>How the argument developed</h3><div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable comparison of the two days"><table class="crossday-table"><thead><tr><th scope="col">Thread</th><th scope="col">Day 1 foundation</th><th scope="col">Day 2 development</th><th scope="col">Report-back implication</th></tr></thead><tbody>{table}</tbody></table></div></section>'

def render_day2(refs):
 records=''
 for i,s in enumerate(SESSIONS,1):
  extra=''
  if i==1:
   extra='<div class="confidence-four" aria-label="Conceptual code confidence framework">'+''.join('<div><b>'+a+'</b><span>'+b+'</span></div>' for a,b in [('Intent','Goals and standards'),('Guardrails','Guide and govern'),('Verification','Independent and thorough'),('Evidence','Auditable and repeatable')])+'</div><p class="day2-footnote">Recorded as a multiplicative conceptual framework; no calibrated probability or numerical scale was supplied.</p>'
  if i==4:
   extra='<div class="skills-five" aria-label="Range five-step skill development process">'+''.join(f'<div><span>{j:02}</span><b>{a}</b><small>{b}</small></div>' for j,(a,b) in enumerate([('Pick','Repeatable work you can judge'),('Teach','Explain the why'),('Pack','Questions and limits'),('Test','Examine real task behavior'),('Ship','Put the skill into use')],1))+'</div><p class="day2-footnote">Five steps as recorded; test coverage, release criteria, and measured benefits were not captured.</p>'
  if i==5:
   extra='<div class="quality-three" aria-label="Quality dimensions recorded in the banking session"><div><b>Safety</b><span>Bias; “roundedness” unresolved</span></div><div><b>Task</b><span>Completion, coverage, completeness</span></div><div><b>Experience</b><span>Satisfaction, knowledge retention</span></div></div><p class="day2-footnote">Dimension labels are from the notes; scoring definitions, thresholds, and measured outcomes were not captured.</p>'
  records+=f'<details class="day1-session day2-session source-details" id="day2-session-{i}"><summary><span class="day1-session-num">D2-{i:02}</span><span>{H(s["title"])}<small>{H(s["speaker"])} · {H(s["time"])}</small></span><span class="pill">Unverified speaker account</span></summary><div class="day1-session-body"><p class="day1-meta"><b>Room:</b> {H(s["room"])}<br><b>Evidence:</b> {H(s["evidence"])}<br><b>Maturity:</b> {H(s["maturity"])}</p><p class="day1-central">{H(s["centralIdea"])}</p>{extra}<h4>What the notes record</h4><ul>{"".join("<li>"+H(x)+"</li>" for x in s["observations"])}</ul><div class="grid2"><div><h4>Takeaway · synthesis</h4><p>{H(s["takeaway"])}</p><h4>Practical tips</h4><ul>{"".join("<li>"+H(x)+"</li>" for x in s["tips"])}</ul></div><div><h4>Evidence limits</h4><p>{H(s["limits"])}</p><h4>Questions to pursue</h4><ul>{"".join("<li>"+H(x)+"</li>" for x in s["questions"])}</ul></div></div><div class="day1-source">Official session identifier: {refs([s["id"]])}. Mechanism details above are from attendee notes.</div></div></details>'
 return f'<section id="day2"><div class="section-head"><div class="section-no">03 / DAY 2 · OCTOBER 14</div><h2>From principles to testable workflows.</h2><p>Five session-note sets, including the Range case you identified. The four originally linked talks and the clarified Range talk are matched to current official metadata; the repeated Day1 content was not counted again.</p></div><div class="coverage-badges"><span class="pill">5 identified session-note sets</span><span class="pill">3 explicit speaker-claim labels</span><span class="pill">2 evidence/maturity labels not captured</span><span class="pill">Range attribution confirmed</span></div><div class="day2-intro">{"".join("<p>"+H(x)+"</p>" for x in NOTES["executive"])}</div><p class="notice">{H(EVIDENCE)}</p>{records}<details class="day1-followups source-details"><summary>Day 2 follow-up questions</summary><ul>{"".join("<li>"+H(x)+"</li>" for x in NOTES["followups"])}</ul></details></section>'

def theme_note(theme_id,day1_sessions):
 ss=[(1,s) for s in day1_sessions if theme_id in s['themeLinks']]+[(2,s) for s in SESSIONS if theme_id in s['themeLinks']]
 if not ss:return '<div class="day1-theme-update"><b>Coverage:</b> No direct session notes supplied for this theme; the cases below remain October10 agenda context.</div>'
 return '<div class="day1-theme-update"><b>Attendee-note updates · both days:</b><ul>'+''.join(f'<li><span class="pill">Day {d}</span> {H(s["takeaway"])} <a href="#{note_anchor(s)}">Read the session notes ↗</a></li>' for d,s in ss)+'</ul><p>The remaining case descriptions retain their original program-source status. A note on one firm does not verify the other examples.</p></div>'

if __name__=='__main__':
 out=W.parent/'outputs'/'ai-engineer-nyc-2026-day-2-notes.md'
 out.write_text(markdown())
 print(f'Saved Day2Markdown: {out} ({out.stat().st_size:,} bytes)')
