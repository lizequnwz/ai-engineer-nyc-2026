"""Analytical exhibits: case evidence, engineering mechanisms, and applications."""
from html import escape as h


def table(headers, rows, widths=None):
    cols = '<colgroup>' + ''.join(f'<col style="width:{w}%">' for w in widths) + '</colgroup>' if widths else ''
    head = ''.join(f'<th scope="col">{h(x)}</th>' for x in headers)
    body = ''.join('<tr>' + ''.join(f'<th scope="row">{h(cell)}</th>' if i == 0 else f'<td>{h(cell)}</td>' for i, cell in enumerate(row)) + '</tr>' for row in rows)
    return f'<div class="table-wrap" role="region" aria-label="{h(headers[0])} comparison" tabindex="0"><table class="analytic-table">{cols}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def exhibit(title, body, caption=''):
    note = f'<p class="exhibit-note">{h(caption)}</p>' if caption else ''
    return f'<section class="exhibit"><h3>{h(title)}</h3>{body}{note}</section>'


def pair(left, right, cls=''):
    return f'<div class="exhibit-grid {cls}">{left}{right}</div>'


def note(title, text):
    return f'<div class="analysis-note"><h4>{h(title)}</h4><p>{h(text)}</p></div>'


def process(items):
    return '<ol class="process">' + ''.join(f'<li><span class="process-index">{i + 1:02}</span><h4>{h(title)}</h4><p>{h(text)}</p></li>' for i, (title, text) in enumerate(items)) + '</ol>'


EXHIBITS = {
    'executive-summary': exhibit('Five findings and their engineering implications', table(
        ['Finding', 'Application or perspective and case evidence', 'Implication for our applications'], [
        ['Ground numerical claims', 'Kepler’s financial-research assistant produces cited answers from filings and internal research, separating facts, calculation, and verification.', 'Preserve entity, period, units, result, and derivation through narration.'],
        ['Fit evidence and workflow', 'Vault is a shared research platform for Bridgewater’s people and agents, combining eligible evidence with familiar research habits.', 'Select eligible context and deliver preparation inside a familiar routine.'],
        ['Assess complete-task value', 'Contour applies AI to investment-research workflows, comparing the process and including analyst effort and repairs.', 'Measure accepted work and total effort; distinguish operational gains from causal ROI.'],
        ['Retain improvement evidence', 'Arize Signal investigates agent traces and proposes fixes using issue history and evaluation against human judgment.', 'Turn recurring defects into reproducible cases with reviewed expectations.'],
        ['Make quality affordable', 'Max’s engineering framework matches rigor to software consequences, dependencies, replacement, and maintenance.', 'Reuse standards and reliable checks as tools become shared dependencies.'],
    ], [20, 40, 40]), 'The cases have different evidence maturity. Speaker accounts and our engineering transfers are distinguished throughout.'),

    'three-failures': exhibit('Failure locations require different acceptance evidence', table(
        ['Failure location', 'Representative defect', 'Appropriate check', 'Insufficient check on its own'], [
        ['Source selection', 'Wrong entity, authority, period, or superseded source.', 'Inspect source eligibility and the exact supporting location.', 'The document exists and concerns a similar topic.'],
        ['Numerical meaning', 'A 2023 result inside a later filing; millions confused with billions.', 'Bind entity, metric, unit, scale, reporting period, and source.', 'The retrieved passage contains the same number.'],
        ['Calculation', 'Incorrect growth rate, margin, aggregation, or operand selection.', 'Reconstruct inputs and operation; check the result and scope.', 'The narrative looks plausible or the SQL executes.'],
    ], [17, 28, 30, 25]), 'Kepler’s “17” example illustrates the second category: value alone does not identify what a financial number means.'),

    'fact-address': pair(
        exhibit('Minimum meaning carried by a quantitative claim', table(['Binding', 'What the reviewer needs to establish'], [
            ['Business scope', 'Resolved entity, metric definition, and grouping grain.'],
            ['Temporal meaning', 'Reporting period and relevant as-of or snapshot conditions.'],
            ['Numerical meaning', 'Value, currency or unit, and scale.'],
            ['Evidence and derivation', 'Exact source or query result; operands and operation.'],
        ], [29, 71])),
        exhibit('Illustrative record: advisor A17', table(['Field', 'Synthetic value'], [
            ['Metric / period', 'Net flow / Q3 2026'],
            ['Inputs', '$800,000 purchases; $1,000,000 redemptions'],
            ['Calculation', '$800,000 − $1,000,000 = −$200,000'],
            ['Scope / evidence', 'Advisor A17; frozen synthetic result'],
        ], [28, 72]), 'Our illustration extends the typed-fact pattern to SQL results; it is not Kepler’s internal schema.'),
    ),

    'output-boundary': exhibit('Responsibility split and final-output handling',
        process([
            ('Plan', 'Model determines the facts and steps needed for the question.'),
            ('Retrieve', 'Eligible sources supply typed facts with registered anchors.'),
            ('Calculate', 'Human-written deterministic code computes from supported inputs.'),
            ('Verify output', 'Resolve final numerical claims against the citation registry.'),
        ]) + table(['Final condition', 'Handling described in the talk', 'Engineering implication'], [
            ['Claim resolves', 'Render with inspectable source and calculation.', 'Preserve the binding through final narration.'],
            ['Claim cannot resolve', 'Strip unsupported numerical output; some cases attempt citation repair.', 'Disclose the missing support. Repair must still produce a supported claim.'],
        ], [20, 40, 40]), 'Conceptual reconstruction of Kepler’s account. The model can still hallucinate; the platform-level guarantee was not independently tested.'),

    'one-row': pair(
        exhibit('Requested scope and underlying values', table(['Item', 'Synthetic value'], [
            ['Question', 'Advisor A17 net flow, Q3 2026, USD'],
            ['Teaching definition', 'Purchases minus redemptions'],
            ['Purchases / redemptions', '$800,000 / $1,000,000'],
            ['Correct A17 result', '−$200,000'],
            ['Separate firm aggregate', '+$5,000,000'],
        ], [40, 60])),
        exhibit('Why the +$5m candidate must fail', table(['Check', 'Candidate result', 'Interpretation'], [
            ['Query execution', 'Pass', 'Execution does not establish scope.'],
            ['Returned row count', 'Pass: one row', 'Same shape as the accepted answer.'],
            ['Entity and grain', 'Fail', 'Firm aggregate is assigned to A17.'],
            ['Keyed value', 'Fail', '+$5m differs from −$200k.'],
        ], [31, 26, 43]), 'All data is fictional. Correct net flow alone does not establish dissatisfaction or competitor displacement.'),
    ),

    'october': exhibit('Bridgewater’s demonstrated contrast concerns the evidence path', table(
        ['Dimension', 'Public-chat response in the demonstration', 'Vault response in the demonstration', 'What we can conclude'], [
        ['Question', 'October question about AI investment and the Korean won.', 'Same research theme, with an explicit information window.', 'The relevant cutoff is part of the task.'],
        ['Evidence', 'Supporting material includes July research.', 'Research is scoped to October 1–8 within Vault’s corpus.', 'Temporal eligibility changes what enters synthesis.'],
        ['Interpretation', 'A fluent answer can obscure the age of its evidence.', 'The selected window and sources are inspectable.', 'Review the evidence path before relying on the explanation.'],
    ], [15, 29, 29, 27]), 'This is a demonstration, not a controlled accuracy test. Neither private-data access nor a larger source count proves correctness.'),

    'evidence-window': exhibit('Eligibility decisions before synthesis: our application of the filtering pattern', table(
        ['Decision', 'Text-to-SQL example', 'Meeting-prep example', 'Evidence to retain'], [
        ['Task scope', 'Metric, entity, grain, filters, and comparison period.', 'Advisor, meeting objective, and prior interaction.', 'Resolved question and active scope.'],
        ['Source authority', 'Reviewed definition and applicable data source.', 'Authoritative CRM record and approved material.', 'Source and definition version.'],
        ['Time', 'Business date role, reporting period, and snapshot.', 'Changes since last interaction; meeting information cutoff.', 'Event date, document date, and as-of conditions.'],
        ['Access', 'Metadata and query access for this user.', 'Permission for notes, activity, and underlying documents.', 'Authorized scope at retrieval and source access.'],
    ], [15, 29, 29, 27]), 'Document freshness, reporting period, and event time are different. Saved context does not establish continuing authorization.'),

    'two-readers': exhibit('Design evidence surfaces around their consumers', table(
        ['Dimension', 'Human researcher / salesperson', 'Agent investigation'], [
        ['Attention constraint', 'Small, high-signal set of facts and sources.', 'Broader eligible material may be needed for task coverage.'],
        ['Useful output', 'Concise brief with inspectable claims and gaps.', 'Sources, context, and intermediate evidence for synthesis.'],
        ['Evaluation focus', 'Relevance, support, clarity, and review effort.', 'Coverage, eligibility, retrieval behavior, and task outcome.'],
    ], [22, 39, 39]) + '<div class="benchmark-note"><b>Reported Vault retrieval benchmark:</b> roughly 200 manually labeled questions; precision@10 improved from about 60% to 90–95%.</div>',
    'Precision@10 measures relevance among the top ten documents. It is not answer accuracy or ROI; no held-out evaluation protocol is disclosed.'),

    'inbox': exhibit('Adoption case: preserve a useful habit before introducing new behavior', table(
        ['Existing research habit', 'Vault product response', 'Why the mapping matters'], [
        ['Subscribed broker research arrives in email.', 'Subscription lists become saved searches.', 'Research continues to arrive through a familiar selection routine.'],
        ['Rules organize messages into folders.', 'Folders become saved collections.', 'Users retain organization and a sense of coverage.'],
        ['Researchers inspect familiar streams.', 'Add topic feeds and cross-corpus questions.', 'New capability builds on an established entry point.'],
        ['People assemble useful evidence sets.', 'Collections become context available to agents.', 'Human organization can support further investigation.'],
    ], [33, 33, 34]), 'The speakers’ account: improved search alone did not bring researchers back every morning. Product fit is reported without a measured adoption uplift.'),

    'workday': exhibit('Illustrative preparation packet and acceptance conditions', table(
        ['Business question', 'Required evidence', 'Useful output and acceptance'], [
        ['Why meet?', 'Resolved advisor, objective, prior commitments.', 'A clear purpose linked to current meeting context.'],
        ['What changed?', 'Dated activity since the relevant interaction; source coverage.', 'Supported changes with period, units, and material gaps.'],
        ['What to ask?', 'Prior concerns plus current evidence.', 'Hypotheses framed as questions for rep validation.'],
        ['What to bring?', 'Current approved product and share-class material.', 'Relevant materials with version and approval context.'],
    ], [18, 37, 45]) + note('Workflow boundary', 'Entry through the meeting or Salesforce context can reduce re-entry effort. Rep review completes preparation; accepting a brief does not authorize an outbound action.'),
    'Proposed application, not a delivered feature. Observed activity is not the advisor’s entire wallet and does not identify the cause of a flow change.'),

    'parked-idea': exhibit('The neglected-idea lifecycle in Contour’s account',
        process([
            ('Research produced', 'An analyst spends a day or two on an investment idea.'),
            ('Attention shifts', 'A competing priority displaces the idea from active work.'),
            ('Conditions change', 'Months pass; a relevant price window may be missed.'),
            ('Context revisited', 'Agents are discussed as a way to bring timely prior work back to people.'),
        ]) + pair(
            note('What is useful in the case', 'The opportunity is to recover existing work when conditions change, rather than only generate additional ideas.'),
            note('What is not established', 'No named trade, validated timing improvement, or AI-attributed return is supplied. Kumar says P&L impact is still to come.'),
        ), 'The revisit capability is an emerging direction in the talk. The process is a reconstruction of the described recurring problem.'),

    'compare-work': pair(
        exhibit('What Contour describes', table(['Comparison element', 'Source account'], [
            ['Reference process', 'Document workflows with and without AI.'],
            ['Evidence collected', 'Sources, conclusions, and time used.'],
            ['Observation window', 'One company from earnings to earnings, about three months.'],
            ['Division of work', 'Different agent/human roles around expert calls and synthesis.'],
        ], [36, 64])),
        exhibit('Transfer to our applications', table(['Comparison question', 'What to examine'], [
            ['Equivalent task?', 'Question, information conditions, and acceptance standard.'],
            ['Better outcome?', 'Correct answer or useful preparation packet.'],
            ['Less total effort?', 'Preparation, review, corrections, and reconciliation.'],
            ['Business effect?', 'Observe later outcomes without assuming causality.'],
        ], [36, 64]), 'Our comparison dimensions are a synthesis; no local study or threshold is supplied.'),
    ) + '<p class="exhibit-note">“Live A/B tests” is the speaker’s term. Randomized assignment, effect sizes, and a causal ROI estimate are not documented.</p>',

    'repair-cost': exhibit('Whole-job accounting lens for accepted work', table(
        ['Cost component', 'What it includes', 'Useful operational observation'], [
        ['Generation and tools', 'Model calls, retrieval, and external tooling.', 'Attempts and spend for the complete task.'],
        ['Professional review', 'Source inspection, business judgment, and approval.', 'Time until the output can be accepted.'],
        ['Rework', 'Corrections, retries, and reconciliation elsewhere.', 'Defect type, additional effort, and remaining gaps.'],
        ['Operation and repair', 'Broken connectors, changing calls, and maintenance.', 'Time and ownership required to keep the workflow usable.'],
    ], [22, 39, 39]) + note('Interpretation', 'A cost-per-accepted-task lens needs a clear acceptance definition. Keep rejection and defect rates visible alongside cost; cheap output can still create expensive work.'),
    'The categories and lens are our synthesis. Contour names cost per useful insight without publishing its formula or realized ROI.'),

    'client-concern': exhibit('Fictional advisor A17: distinguish facts, possible relevance, and the proposed question', table(
        ['Evidence', 'What it supports', 'What remains unproven'], [
        ['14 Aug 2026 meeting note: share-class implementation constraints.', 'A dated concern worth checking before another meeting.', 'That the concern remains unresolved.'],
        ['Q3 purchases $800k; redemptions $1m; net flow −$200k.', 'A supported change within the synthetic data’s entity and period.', 'Dissatisfaction, competitor displacement, or cause of flows.'],
        ['Upcoming meeting and current approved material.', 'An opportunity to revisit relevant implementation requirements.', 'That an earlier question still fits the current objective.'],
    ], [37, 31, 32]) + note('Question for professional validation', 'Do those implementation constraints still matter, and what has changed? Check for later resolution, confirm the relevant product/share class, and retain the source date.'),
    'All records, dates, and values are fictional. This applies Contour’s attention-and-timing lesson, not its investment-selection objective.'),

    'next-failure': exhibit('From recurring behavior to evidence for a change decision',
        process([
            ('Observe', 'Traces identify a recurring failure or behavior pattern.'),
            ('Investigate', 'Retain context, issue history, and the explanation.'),
            ('Define acceptance', 'Establish a reviewed case and expected behavior.'),
            ('Propose and evaluate', 'Compare the change with the maintained standard.'),
        ]) + table(['Local example', 'Evidence the next evaluation should retain'], [
            ['Wrong-scope SQL answer', 'Question, data snapshot, entity/grain, rejected answer, accepted keyed values.'],
            ['Stale meeting-prep source', 'Meeting cutoff, source date/version, rejected claim, reviewed evidence selection.'],
        ], [27, 73]), 'Signal’s described lifecycle motivates the pattern. Local examples are ours; evaluation evidence does not imply automatic deployment.'),

    'survives': exhibit('Separate execution lifetime from the lifetime of useful evidence', table(
        ['Concern', 'For a particular run', 'Retained for later work', 'Engineering implication'], [
        ['Execution', 'Workspace, tools, scoped access, temporary credentials.', 'Outputs and relevant run traces.', 'Tear down temporary access independently of retained evidence.'],
        ['Investigation', 'Current context and work in progress.', 'Issue history, progress, and supporting artifacts.', 'Recover from environment failure without losing the investigation.'],
        ['Our evaluation cases', 'Current question, permissions, and fresh source selection.', 'Reviewed question, input snapshot, meaning, and expected result.', 'An old case can remain useful even when new execution needs different evidence.'],
    ], [16, 27, 27, 30]), 'Signal supplies the execution/persistence account. The local evaluation-case distinction is our application, not a prescribed storage topology.'),

    'grader': pair(
        exhibit('Evaluator agreement: conceptual outcome matrix', table(['Judge decision', 'Human accepts', 'Human rejects'], [
            ['Pass', 'Agreement: accepted output.', 'False pass: consequential failure may escape.'],
            ['Fail', 'False failure: unnecessary rework or lost utility.', 'Agreement: rejected output.'],
        ], [26, 37, 37]), 'No measured frequencies or acceptable agreement threshold are implied.'),
        exhibit('Synthetic false pass: the wrong-scope SQL answer', table(['Assessment', 'Reason'], [
            ['Judge passes +$5m', 'Valid execution, one row, and fluent explanation.'],
            ['Business reviewer rejects', 'The figure is the firm aggregate, not advisor A17.'],
            ['Calibration lesson', 'Add adjudicated scope errors and inspect why the judge missed them.'],
        ], [40, 60]), 'Human reference judgments also need consistent definitions and adjudication.'),
    ),

    'quality-spectrum': exhibit('Max’s four factors determine the degree of disposability', table(
        ['Factor', 'More disposable conditions', 'More durable conditions'], [
        ['Consequences of failure', 'Minimal impact; tightly limited purpose.', 'Important professional or business consequences.'],
        ['Dependencies', 'Few users; little reliance from other systems.', 'Many users or downstream systems depend on behavior.'],
        ['Replacement cost', 'Rebuild or discard with little disruption.', 'Replacement requires coordination and preserved meaning.'],
        ['Maintenance cost', 'Little ongoing maintenance or change management.', 'Continuous maintenance and controlled evolution.'],
    ], [24, 38, 38]) + note('Examples in the talk', 'A one-party planning tool and Chromium illustrate different ends of the spectrum. A short-lived tool can still have consequential failure, so lifetime alone is insufficient.'),
    'Conceptual argument, not a Capital One deployment program. Max advises assuming greater durability than initially expected.'),

    'dependency': exhibit('Qualitative application to a shared SQL or meeting-prep service', table(
        ['Factor', 'Question for our applications', 'Resulting engineering responsibility'], [
        ['Failure consequences', 'Who might use a wrong number, source, or interpretation?', 'Make acceptance criteria and consequential failure categories explicit.'],
        ['Dependencies', 'Which people, reports, or workflows rely on the output?', 'Keep interfaces and business meaning stable and inspect changes.'],
        ['Replacement effort', 'What definitions and source bindings would need rebuilding?', 'Retain domain meaning and reproducible cases outside one model’s prose.'],
        ['Maintenance effort', 'Who handles data, connector, model, and behavior changes?', 'Assign ownership and make feedback and checks repeatable.'],
    ], [21, 39, 40]), 'These are engineering implications, not a local risk score. Max also discusses reducing exposure through isolation, limited scope, independence, and redundancy.'),

    'cheaper-rigor': exhibit('Reduce the work needed to apply dependable engineering practices', table(
        ['Practice in Max’s argument', 'Why it lowers repeated effort', 'Connection to the preceding cases'], [
        ['Shared standards', 'Fewer technologies, conventions, and variants to support.', 'Consistent meanings, interfaces, and evidence conventions.'],
        ['Checks inside the workflow', 'Less dependence on remembering a separate validation step.', 'Check quantitative bindings and source eligibility during delivery.'],
        ['Fast deterministic tests', 'Reliable feedback with less setup and investigation.', 'Reproduce keyed-value, calculation, and temporal-scope defects.'],
        ['Realistic service fakes', 'Make integration behavior easier to exercise consistently.', 'Evaluate workflow failure paths without recreating every dependency.'],
    ], [25, 36, 39]), 'Connections in the final column are our synthesis. Building and maintaining the shared infrastructure still requires effort and ownership.'),

    'two-products': exhibit('Acceptance questions derived from the five cases', table(
        ['Responsibility', 'Text-to-SQL', 'Institutional-sales meeting prep'], [
        ['Ground the claim', 'Correct entity, measure, period, grain, units, values, and derivation?', 'Material facts have source, date, scope, and calculation where needed?'],
        ['Select eligible evidence', 'Required definitions and join context; correct date role and access?', 'Current notes, activity, approved materials, and meeting cutoff?'],
        ['Improve the complete task', 'Correct business answer with reasonable review and reconciliation?', 'Useful questions and materials with manageable rep review effort?'],
        ['Learn from failures', 'Retained cases for wrong-scope, incorrect-value, and ambiguous requests?', 'Retained cases for stale sources, unsupported claims, and missed context?'],
        ['Sustain dependable change', 'Shared checks, clear ownership, and maintainable interfaces?', 'Reviewed expectations and dependable workflow integration?'],
    ], [23, 38, 39]), 'Application synthesis, not a production audit or approved roadmap. No company result is assumed to transfer to our systems.'),

    'reflection': exhibit('Conclusions and discussion questions', table(
        ['Key takeaway', 'Engineering meaning', 'Question for the team'], [
        ['Grounded facts', 'Preserve source, time, business meaning, calculation, and final-claim support.', 'Which apparently correct answers need a more explicit acceptance check?'],
        ['Useful delivery', 'Fit the professional’s routine and include review, rework, and operation in value.', 'Where does our experience help or disrupt the existing workflow?'],
        ['Repeatable improvement', 'Retain reviewed cases and make dependable changes easier as dependencies grow.', 'What understanding survives when the same failure recurs?'],
    ], [21, 40, 39]) + note('Discussion: 10 minutes after the 35-minute briefing', 'Allow roughly three minutes per question and one minute for closing reflections. Invite concrete examples and limits on the analogies; no project selection or owner assignment is required.'),
    'The five cases offer design and evaluation principles. Their differing evidence maturity limits claims about measured performance or causal business impact.'),
}


def render_exhibit(slide):
    return EXHIBITS[slide['id']]
