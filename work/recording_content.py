"""Recording follow-ups shared by conference notes and the reading report."""
from pathlib import Path
import json
import html

W = Path(__file__).resolve().parent
DATA = json.loads((W / 'recording_evidence.json').read_text())
RECORDS = {r['id']: r for r in DATA['records']}
H = lambda s: html.escape(str(s), quote=True)

LESSONS = [
    ('Build three complementary evaluation views',
     'An acceptable result, an acceptable process and an authorized state transition are separate requirements. A report can contain the right total while using stale facts; an accounting agent can make a reconciliation tie by inventing an adjustment; a sound draft can still be sent without permission. Keep diagnostic scores, complete-task acceptance and critical blockers separate.',
     'For one historical task, retain its original data and allowed tools. Add a missing-evidence variant and a tempting prohibited shortcut. Score the final artifact, the consequential decisions, and the action boundary. Record not-applicable behavior separately from compliance.',
     ['basis','vals','coinbase','sofia-release','air-canada-release']),
    ('Treat numerical grounding as a chain of checks',
     'Retrieval relevance does not establish financial meaning. Select the eligible source, resolve the correct fact, retain units and period, compute reproducibly, and validate the final output. A citation attached after generation cannot repair a wrong entity, superseded filing or unsupported calculation.',
     'Use a typed claim containing entity, metric, period, unit/currency, source version, as-of cutoff and derivation. Test date parsing, negative signs, nulls, join coverage and evidence survival after export. This combined contract is our synthesis rather than one firm\'s disclosed architecture.',
     ['bridgewater','kepler-14','kepler-breakout','southbridge','openai','compound']),
    ('Give memory time, ownership and a correction policy',
     'Memory is useful when it preserves reusable procedure and current evidence. It is harmful when it carries old amounts, unexamined rules or injected instructions into the next task. Task checkpoints, professional know-how and changing business beliefs have different lifetimes.',
     'Advance a test business one period: change the amounts and one procedure. Require fresh facts and revalidation of the changed rule. Store source time, correction history and sensor health. Missing observations remain unknown. Freeze historical snapshots so later outcomes cannot leak backward.',
     ['ramp-evals','citadel','arize','bloomberg']),
    ('Make long-running work durable and authority explicit',
     'These examples separate persistent progress from bounded executions, waiting states and human handoffs. Perpetual shows one design in which deterministic orchestration owns progress and the model supplies bounded judgments. A valid schema does not by itself authorize an external action.',
     'Record the approved plan version, exact payload, next event, deadline and owner. Distinguish failed from outcome-unknown external actions; inspect the latter before retrying. Test that revocation, tenant boundaries, budgets and required approvals are enforced outside the model.',
     ['arca','perpetual','coinbase','two-sigma','credit-karma','bloomberg']),
    ('Measure reviewed work and preserve replaceable implementations',
     'Leading examples put proprietary data, professional methods, evaluation assets and operational controls around increasingly interchangeable models. The same approach can support financial preparation, transaction modeling, software modernization and credit operations, but each has a different accepted work product and latency budget.',
     'Compare equivalent completed work at agreed quality. Include unsuccessful attempts, review, rework, tools and support. Preserve the task definitions and scorecards when changing models or scaffolding. A lower token bill, adoption count or faster first draft is only one part of the result.',
     ['coatue','blackstone-norm','apollo-rowspace','wells-fargo','jellyfish','contour-release']),
    ('Grow by discovering the bottleneck and proving the repair',
     'The engineer\'s durable responsibility is to understand the work, define good completion, instrument execution, diagnose failures and verify changes. Faster code creation can shift the constraint to review, operations or security. Making checks cheaper and easier is therefore part of product engineering.',
     'Own one complete improvement cycle: interview the practitioner, write an acceptance contract, inspect a failure trace, test one repair, examine paired regressions and review the current exported artifact. Retain the learning so the next engineer starts from evidence.',
     ['laurie-release','capital-one','arize','sonar','monzo-release','prime-intellect'])
]

def links(ids):
    return ' · '.join(f'[{RECORDS[i]["company"]}]({RECORDS[i]["url"]})' for i in ids)

def daily_update(day):
    ids = (['bridgewater','two-sigma','kepler-breakout','contour-release','failure-study-release','arize']
           if day == 1 else ['range','ramp-evals','sonar','openai','basis','coinbase','perpetual','citadel'])
    out = ['## Recording follow-up · October 25, 2026',
           'The original attendee observations above are preserved. The following later-source findings clarify them or add related sessions; this is not a claim of additional attendance. The [complete recording supplement](ai-engineer-nyc-2026-recording-supplement.md) contains the wider thematic synthesis and source limits.']
    for i in ids:
        r = RECORDS[i]
        out += ['### ' + r['company'], r['mechanism'],
                '**Practical implication:** ' + r['practice'],
                '**Source and scope:** ' + r['evidence'] + '. ' + r['limit'],
                f'[Read / watch source]({r["url"]})' +
                (f' · [Recording at the session start]({r["watch"]})' if r.get('watch') else '')]
    out += ['### Clarifications that remain open',
            'The Comet/NatWest affiliation discrepancy and the banking notes\' “roundedness” label remain unresolved. OpenAI\'s uncertain provider spelling is not guessed. The failure-study expression is not adopted as a calibrated expected-loss formula. Ryan Stevens\'s written account is separate from Alexander Shevchenko\'s recorded keynote. Range\'s online recording is labeled October 13; its attended notes remain in Day 2.']
    return '\n\n'.join(out) + '\n'

def markdown():
    out = ['# AI Engineer NYC 2026 — recording-enhanced learning report',
           '**Updated October 25, 2026 · For data scientists, AI engineers and technical leads**',
           'The central lesson is to engineer a complete, reviewable work product: the right evidence, the right professional method, an explicit acceptance decision and controlled execution. The newly available material makes that lesson concrete through wealth planning, investment research, credit operations, accounting, fraud modeling and software delivery.',
           '## What this update adds',
           '- More direct wealth cases: Range\'s planner-owned skills, Arca\'s event-driven service work and Perpetual\'s compiled, approved workflows.\n- A separate process-evaluation layer from Basis, plus answer-first test construction and regression vectors.\n- Specific retrieval, fact-resolution, context-preparation and temporal-memory mechanisms.\n- A clearer financial strategy: preserve data, expert knowledge and acceptance assets while evaluating changing models and harnesses.\n- A practical growth path built around discovering user needs and proving improvements.',
           '## Research coverage and reading limits', DATA['method'],
           'The 52-session archive is a livestream-derived collection, not the full breakout program. The inspected channel descriptions include additional individual releases. A description confirms its stated scope and chapter topics; it does not substitute for a full transcript. All company outcomes remain attributed reports. Earlier Morgan Stanley (2024), UBS (2025) and RBC (2025) examples retain their dated corporate-disclosure status. No missing NYC talk was replaced with another year\'s recording.',
           '## Six lessons to teach the team']
    for n, (title, argument, exercise, ids) in enumerate(LESSONS, 1):
        out += [f'### {n}. {title}', argument, '**Try this:** ' + exercise, '**Evidence:** ' + links(ids)]
    out += ['## Worked example: a correct-looking answer can fail three ways',
            'This example is invented. A reviewer requests a current monthly cash-flow snapshot. Approved income is $8,000; current expenses are $6,000; superseded expenses are $5,500. The task permits a draft only.',
            '| Candidate | Arithmetic | Evidence / behavior | Decision |\n|---|---|---|---|\n| $8,000 − $5,500 = $2,500 | Correct on stated operands | Uses superseded expenses | Reject current-source validity |\n| $8,000 − $6,000 = $2,000 | Correct and reconstructable | Uses current facts; flags missing insurance information | Eligible for professional draft review |\n| Edits a record so the books tie | May make the final total match | Unsupported intervention | Reject process adherence |\n| Sends a correct draft without approval | Correct contents possible | Exceeds the permitted action | Block execution |',
            'The lesson is not to replace exact checks with a judge. Use exact checks where possible, an expert rubric for substantive quality, a behavior check for consequential decisions, and an enforcing service for action authority. Human approval of a draft and permission to execute are separate events.',
            '## Company stories, grouped by method']
    for theme in dict.fromkeys(r['theme'] for r in DATA['records']):
        out.append('### ' + theme)
        for r in DATA['records']:
            if r['theme'] != theme:
                continue
            out += ['#### ' + r['company'], r['mechanism'],
                    '**Transferable practice:** ' + r['practice'],
                    '**Boundary:** ' + r['limit'],
                    f'**Source:** [{r["evidence"]} — {r["title"]}]({r["url"]})' +
                    (f' · [Timestamped recording]({r["watch"]})' if r.get('watch') else '')]
    out += ['## A compact practitioner playbook',
            '| Stage | Artifact to keep | Check before moving on |\n|---|---|---|\n| Understand the job | Reviewed task specification and baseline | A practitioner recognizes completed work |\n| Prepare evidence | Authorized, time-scoped input snapshot | Meaning, coverage, access and freshness |\n| Evaluate | Cases, rubrics, behavioral specs and judge calibration | Critical failures cannot disappear in an average |\n| Execute | Approved plan, payload and workflow state | Authority, retries, interruption and recovery |\n| Improve | Reproducible failure and paired experiment | Fix the mechanism without hiding a regression |\n| Deliver | Current artifact plus sources and limitations | Values, evidence and usability survive export |',
            '## What changed from the earlier notes',
            '- **Bridgewater:** the intended progression is reactive resource → proactive participant; its reported retrieval metric is precision@10.\n- **Range:** ownership and separate review are now transcript-backed. The online recording date differs from attendance placement.\n- **Kepler:** the breakout release and next-day follow-up are separate editions; final verification remains necessary.\n- **Ramp:** the Ryan Stevens article supplies ablation and roll-forward details; Alexander Shevchenko\'s keynote supplies different specialist-model research.\n- **Vanguard:** the speedup title concerns mainframe-code research, not investment research.\n- **Blackstone / Norm.ai:** attribute Norm\'s evaluation assets to Norm; panel participation does not prove deployment.\n- **Citadel Securities:** preserve the firm name; do not merge its organizational-memory case with Citadel employment histories.\n- **Still open:** banking affiliation/terminology, exact breakout retrieval settings, several result denominators, and uncertain provider spelling.',
            '## Recommended review path',
            'Use the presentation\'s 29-slide core for the 40-minute team briefing. Use Read & learn for the expanded explanations. For a technical discussion, choose one source pair: Basis + Ramp on evaluation; Bridgewater + Kepler on grounding; Range + Perpetual on expertise and authority; or Arize + Capital One on engineering growth. Follow the timestamped links to inspect the original claim before adopting a numerical target.',
            'This report is a synthesis of conference learning, not a Fidelity deployment commitment or an independently validated industry benchmark.']
    return '\n\n'.join(out) + '\n'

def render_digest():
    items = ''.join('<article class="day1-lesson"><h3>' + H(title) + '</h3><p>' + H(argument) +
                    '</p><p><b>Practice:</b> ' + H(exercise) + '</p><p>' +
                    ' · '.join(f'<a href="{H(RECORDS[i]["url"])}" target="_blank" rel="noopener noreferrer">{H(RECORDS[i]["company"])}</a>' for i in ids) + '</p></article>'
                    for title, argument, exercise, ids in LESSONS)
    return '<section id="recording-update"><div class="section-head"><div class="section-no">RECORDING UPDATE / OCTOBER 25</div><h2>The released talks make the methods concrete.</h2><p>' + H(DATA['method']) + '</p></div><div class="day1-lessons">' + items + '</div></section>'

if __name__ == '__main__':
    out = W.parent / 'outputs' / 'ai-engineer-nyc-2026-recording-supplement.md'
    out.write_text(markdown())
    print(f'Saved recording supplement: {out} ({out.stat().st_size:,} bytes)')
