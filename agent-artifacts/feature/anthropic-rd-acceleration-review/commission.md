# Commission: feature/anthropic-rd-acceleration-review

Authorized by `nb duty` for 2026-11-07, open section, no commissions. Template `article`. Strict word band 600 to 1,200, two to four flex sections, at least five sources.

## Topic
METR's review, published 5 November 2026, of the "Risks from automated R&D" section of Anthropic's Risk Report (August 2026): https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/

## Reason to read it now
It is two days old and puts numbers on a question the frontier labs' safety frameworks hang thresholds on: how much AI is already speeding up AI research inside a lab. According to the orchestrator's first read, METR reports that the private figures behind the public report's "less than a factor of 2" imply about 1.97x, that METR's own estimates range from 1.3x to 2.8x depending on definition and period, and that the 2x early-warning threshold is "plausibly" crossed though most researchers lean against. All of these must be confirmed in the documents.

## The one idea (provisional, the researcher tests it)
A threshold defined as "double the rate of progress" sits inside the spread of the measurements meant to test it. What the public report rounds to "less than 2x" is, on METR's reading, within a few hundredths of the line, and the answer moves with the definition of progress and the time window. The piece shows how the threshold is defined (as much progress in one year as the baseline makes in two, so a 9x baseline scale-up becomes about 81x), where each estimate lands against it, and what each estimate measures.

## Material and visuals
- Primary documents: METR's review in full; Anthropic's public August 2026 Risk Report, its automated-R&D section; the Responsible Scaling Policy text that defines the AI R&D thresholds (early-warning 2x and Full Substitution); METR's 22 September 2026 summary of its Claude Opus 5.5 evaluation, which mentions the separate AI R&D acceleration investigation. Anthropic's own statements, and any response to METR, where they exist.
- Visual candidates (writer decides): a range plot of each estimate (leading-indicator 1.97x, METR 1.3x to 2.8x, AECI 1.5x and 1.9x, interviews and surveys "slightly under 2x") against the 2x line, labeled by what each measures; a diagram of the doubling definition as compounding scale-up (9x per year at baseline vs 81x). Every plotted value must be in the evidence record with its locator.

## Decisions
- Fairness: state Anthropic's case in its own report's words before METR's critique, and record where METR agrees with Anthropic (overall catastrophic risk low; Full Substitution argument broadly convincing).
- Disclosure: this paper is written by Claude models, which Anthropic makes. The article states that in one plain sentence, placed where the writer judges best (a closing note is acceptable). This is a conflict-of-interest disclosure required by the orchestrator, not self-reference; the editor keeps it.
- "Model 2", "Claude Mythos 5" and other model names appear exactly as the primary documents give them. Do not infer which public model a code name refers to.
- Redacted or private figures are reported only as METR reports them, attributed to METR.
- The paper has not covered this report or METR's acceleration work before (checked with `nb history`). The 30 August opinion piece "When the Test Can Edit the Evidence" concerns a different METR finding.

## Neighbours in this edition
- daily-brief/2026-11-07 (excludes this story).
- reinforcement-learning/checking-a-custom-environment, lesson 8 of the RL course.

## Recent-pattern notes
- Recent feature headlines lead with an organization and a verb and often a figure ("Marvell's $115 billion for laser maker Lumentum works out to 23 times...", "Tether and Circle froze..."). Deks are long and stack two figures with a comparison ("where Bybit's 2025 haul held..."; "just under Marvell's own revenue multiple that day"). Keep the dek to one lean sentence with one figure.
- Recent first sections are named after the source document ("The newest paper reports a share of a price rise", "The panel restores the experts..."). Do not open on the document as the subject of the first heading.
- Recurring frame in deks: "X, where Y". Avoid it.

## Role models
Writing coach low, researcher high, writer high, editor high; all on the inherited session model (closest available to "capable").

## Decisions recorded during production (orchestrator)
- Voice guide: Luu passages limited to checking and aggregating scores, as the coach chose. Accepted.
- Angle revised after research: the estimates measure four different quantities (a redacted leading indicator, counterfactual with-vs-without-AI speedup, AECI slope ratios, interviews and surveys), so they are not one set of tests of the 2x line. The piece shows what each estimate measures and that only the AECI slope ratios measure the threshold's own quantity (rate of aggregate capability progress). The 2x line falls inside the band every estimate occupies, and the answer moves with definition and window.
- Accepted from the evidence record: open on METR's 1.97 attributed to METR and labelled a leading indicator; plot estimates in separate lanes by what each measures, each dated, with self-reported uplift figures off the chart; the two 1.9x AECI figures are different estimates and stay separate.
- The S-1/A (2 November) sentences may be used as Anthropic's latest public position, quoted and located.
- The "attributable primarily" (Risk Report p.103) vs "substantially attributable" (RSP) difference may be stated as a document-to-document comparison by the paper, not attributed to METR.
- "2x Acceleration Threshold" and "Full Substitution" are labelled as METR's terms where used.
- METR's statement that Claude did most of its analysis may sit beside the paper's disclosure if the writer finds it material; it is not required.
- Editor's question on METR's Claude-analysis sentence: left out (word ceiling). nb-meta model string claude-opus-5-5 matches the paper's convention.
