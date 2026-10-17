from pathlib import Path
import json

root=Path(__file__).resolve().parent
program=json.loads((root/'program.json').read_text())
sessions=program['sessions']
slots=[]
for day in ('tuesday','wednesday'):
    raw=json.loads((root/f'{day}_rankings.json').read_text())
    slots.extend(raw['slots'] if isinstance(raw,dict) else raw)
slots.sort(key=lambda s:(s['date'],s['startMinutes']))
lookup={s['id']:s for s in sessions}
assert len(slots)==22
assert len({(s['date'],s['startMinutes']) for s in slots})==22
for slot in slots:
    assert len(slot['picks'])==3
    assert len({p['id'] for p in slot['picks']})==3
    for p in slot['picks']:
        s=lookup[p['id']]
        assert (s['date'],s['startMinutes'])==(slot['date'],slot['startMinutes'])
    assert not any('Leadership' in t for t in lookup[slot['picks'][0]['id']]['topics'])
for date in ('2026-10-13','2026-10-14'):
    chosen=[lookup[s['picks'][0]['id']] for s in slots if s['date']==date]
    assert len(chosen)==11
    assert all(a['endMinutes']<=b['startMinutes'] for a,b in zip(chosen,chosen[1:]))
    starts={s['startMinutes'] for s in sessions if s['date']==date and s['type'] in ('talk','breakout')}
    assert starts=={s['startMinutes'] for s in slots if s['date']==date}

keynotes={
'a84ca3a8-cc2f-4b50-a635-fc380f6f04f6':dict(priority=True,focus='Anchor the day in a real institutional knowledge platform. Capture the source-quality contract, buy/build boundary, and ownership decisions; connect this keynote to the 11:55 permissions talk.',question='What quality and entitlement contract must a source satisfy before investors or agents can use it?',caveat='Adoption and business-benefit statements remain speaker-reported.'),
'68a1e78b-569e-4314-a56f-f20508123cbe':dict(priority=False,focus='Listen for concrete financial-services capabilities, constraints, and current deployment patterns. Separate delivered behavior from roadmap.',question='Which capabilities are demonstrated in production, and which remain roadmap?',caveat='Published title is a role label; no abstract is available.'),
'73badd10-6f8c-4c95-b5e7-55fc3d7bafc1':dict(priority=True,focus='Capture controls that preserve useful research and engineering work while constraining agent risk. Ask what is enforced outside the model and what was measured.',question='Which enforced control improved safety without materially reducing task utility?',caveat='The title does not establish that all safety/utility tradeoffs disappear.'),
'5191589c-a70e-4806-99dc-86f7794f46b9':dict(priority=False,focus='Extract principles for AI-assisted software review and code quality that your team can use when building assistants and evaluation pipelines.',question='What evidence should decide which AI-generated changes still need independent review?',caveat='Principles and opinions should be distinguished from measured delivery outcomes.'),
'b2ed4456-5671-4e8e-83fd-684c012fef8c':dict(priority=False,focus='Use the discussion to sharpen task definitions and success criteria for probabilistic systems. Capture a definition of “good” that can become a review rubric.',question='How do you translate a user need into measurable completion criteria?',caveat='Broad predictions about coding automation are the speaker’s framing, not settled facts.'),
'9a9dfcd0-459f-43eb-b3f8-004864b4ad2a':dict(priority=False,focus='An institutional practitioner perspective. Look for a specific investment or operating workflow and how value was established.',question='Where did AI demonstrably change a workflow, and against which baseline?',caveat='Role-label title and no abstract; subject and technical depth remain unknown.'),
'cada670e-c5ea-4977-b3c2-9a68dda26abb':dict(priority=False,focus='Use as horizon scanning. Capture one capability boundary and a bounded implication rather than forcing a near-term assistant application.',question='Which present capability is demonstrated, and what remains a research ambition?',caveat='Description is chiefly a biography; direct fit to internal knowledge/workflow assistants is lower.'),
'871cd5c8-13f4-4fe9-ac49-c8b25d970add':dict(priority=False,focus='Attend with open-ended notes and ask for a concrete capability, limitation, or engineering lesson.',question='Which result can a practitioner inspect or reproduce today?',caveat='Role-label title and no abstract. Affiliation alone does not establish the topic.'),
'caecd5f6-b352-4868-a995-f0f71679caf0':dict(priority=False,focus='Capture a build/hold criterion: which assistant gaps are worth solving now, and which may be overtaken by model progress?',question='What evidence makes a capability gap worth building around today?',caveat='Future frontier progress is uncertain; record the assumptions behind the strategy.'),
'4add802c-6a68-4e9c-93fb-9c1e017193bc':dict(priority=False,focus='Map distinct verification responsibilities during generation, in CI, and after deployment. Translate the loops into owners and defect classes.',question='Which failure class does each loop catch, and what still requires independent verification?',caveat='An engineering framework does not by itself demonstrate reduced production defects.'),
'ee927042-2ba1-44c3-b304-d001ae247839':dict(priority=True,focus='A strong anchor for workflow agents. Capture an auditable process map, boundaries around agent loops, and evidence used to grant more autonomy.',question='Where does human authority remain, and how does measured quality change the autonomy boundary?',caveat='Transfer the boundary-design method; agree policies under your own operating requirements.'),
'02f94835-c29d-4cf5-b77a-c5a491b747b8':dict(priority=False,focus='Listen for the financial-services product direction and unresolved enterprise requirements. Useful input to a build/buy conversation.',question='Which requirements are met today, and which need independent testing or remain future direction?',caveat='Product direction is not procurement-ready evidence or a validated fit for Fidelity.'),
'01982251-7fdc-4828-8520-fb34b9bc7564':dict(priority=True,focus='Bring back one concrete attack path, the enforcement point of its defense, and a residual failure worth testing in your assistant threat model.',question='What attack still succeeds after the proposed defense, and how can a team reproduce the test safely?',caveat='A demonstrated incident establishes a failure mode, not its prevalence across systems.'),
'44e9d04a-e8b4-418c-8a85-02fbb9263dd0':dict(priority=False,focus='Capture the institutional use case, baseline, operating model, and evidence behind any claimed benefit.',question='What changed in the workflow, and how was its value measured?',caveat='The sparse abstract only identifies a customer co-presentation; detailed architecture is unconfirmed.'),
'1cbc625f-7f07-49bb-9c5c-57c95f07ba77':dict(priority=True,focus='One of the strongest fits across both days. Capture a minimal behavior specification, judge-applicability rule, and how trajectory failures guide system changes.',question='How are behavior judges validated, critical behaviors selected, and specification growth controlled?',caveat='A correct final answer can conceal an unreliable process; judge quality also requires validation.'),
'af8422e8-d5f8-4dbd-a918-6360f5bfba80':dict(priority=False,focus='A physical-world-model horizon session. Capture one bounded insight about simulation; avoid turning it into an immediate financial-assistant recommendation.',question='Which demonstrated simulation capability has a clear validity boundary?',caveat='Lower direct alignment to your confirmed research-assistant and workflow-agent priorities.')
}
assert len(keynotes)==16
included=[s for s in sessions if s['date'] in ('2026-10-13','2026-10-14')]
assert len(included)==140
assert {s['id'] for s in included if s['type']=='keynote'}==set(keynotes)
fields=['id','date','startMinutes','endMinutes','startsAt','endsAt','type','format','title','room','topics']
slim=[]
for s in included:
    row={k:s[k] for k in fields}
    row['speakers']=[{k:p[k] for k in ('name','company','role')} for p in s['speakers']]
    row['hasAbstract']=bool(s['description'].strip())
    slim.append(row)
data=dict(generatedAt=program['generatedAt'],sessions=slim,slots=slots,keynotes=keynotes)
(root/'report_data.json').write_text(json.dumps(data,indent=2,ensure_ascii=False))
html=(root/'report.html').read_text().replace('__REPORT_CSS__',(root/'report.css').read_text()).replace('__REPORT_JS__',(root/'report.js').read_text()).replace('__REPORT_DATA__',json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
assert '__REPORT_' not in html
output=root.parent/'outputs'/'ai-engineer-nyc-2026-field-guide.html'
output.write_text(html)
print(json.dumps({'file':str(output),'bytes':output.stat().st_size,'slots':len(slots),'rankedChoices':sum(len(s['picks']) for s in slots),'programEntries':len(included),'keynotes':len(keynotes),'defaultOverlaps':0,'defaultLeadershipTrackSelections':0},indent=2))
