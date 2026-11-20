# Commission: feature/top500-ageing-installed-base

Run: scheduled edition of 2026-11-20. Neighbours in this edition: daily-brief/2026-11-20 (which must not carry the TOP500 list as an item) and reinforcement-learning/potential-based-shaping.

## Why this topic

The 68th TOP500 list was released on 16 November 2026, with a release headline about new-system turnover falling to a historic low. The scout's three candidates are in scout-candidates.md. Chosen over the Microsoft 365 outage (the official report sits behind an admin login and the final version, due today, may revise the cause) and WHO's TB estimates (key annexes unread, angle may narrow to two countries).

## The angle to test

The list's own files show its installed base ageing: by the scout's parse, the median system has been on the list for 6 editions, up from 4 in November 2021, and 138 of 500 systems are five or more years old against 45 then. The working claim: the TOP500 increasingly measures an ageing installed base while new large-scale compute goes into AI clusters that never submit an HPL run.

The original work is the paper's own computation across the list files, which the TOP500 release and press coverage do not do. The researcher must reproduce the scout's numbers from the downloaded xlsx files (not trust them), extend the series across every November list available back to at least 2016 (and June lists if cheap), and keep the full series for charting.

## What would break it

- Next Platform reads the dip as a pause before new GPU generations (Rubin, MI400) arrive. Record that view in its own words and test it against the history: have past low-turnover editions been followed by rebounds?
- 2021 may be an unusually young baseline. The series across many years settles that.
- Age by "first appearance" may be confounded by systems re-entering or being upgraded and renamed. The researcher states how the field is defined in the list documentation.
- If the series does not show a sustained trend, the angle becomes whatever the series does show. Report that to me and do not force the claim.

## Shape

Feature template, 600–1200 words, 2–4 sections each built around a visual (series prompt). Likely visuals, the writer decides: the median age or share-over-five-years across editions; newcomers per edition; HPL total growth against the AI-compute growth figure the release cites (only if the release's citation can be traced to its owner, Epoch AI). Charts with `nb chart` from verified series only.

## Production

- Policy (not required): writing-coach low, researcher high, writer high (series override), editor high (required). Actuals: subagents on the orchestrator's model at those efforts.
- min_sources 5.

## Recent-pattern notes for writer and editor

From the last five features (ai-buildout-debt, phone-pouch-bans-achievement, carbon-budget-oil-dip, toolturns-multi-turn-agents, us-measles-elimination-lost):
- Headlines repeatedly set one figure against another ("outweigh ... nearly four to one", "bigger than 2026's whole projected fall", "'half' counts the pandemic years"). A comparison headline is the house habit; use one only if it is the finding.
- Deks repeatedly take the form "<Owner>'s <figure> ... does not separate / follows / leaves ...", criticising a source's figure. This piece is not a correction of the TOP500; do not frame the dek as a gotcha.
- Section headings in ai-buildout-debt and carbon-budget-oil-dip are number-led statements ("Oil falls 243 Mt while coal and India rise", "Past projections missed by 0.37 points on average"). Vary.

## Decisions after research (researcher/01): the angle is revised

The ageing is real and sustained by count of systems, but the commissioned explanation is not supported. Decided angle:

- The finding: systems now stay on the TOP500 far longer than they did through 2019 (median age, share listed five or more years earlier, five-year survival by cohort), because the entry bar, the No. 500 system's HPL result, has grown 5–25% a year since 2020 against 30–69% a year in 2011–2019. A slow-rising bar keeps old machines above it. That mechanism is the piece's spine.
- The old systems sit in the bottom half. New systems still carry most of the list's performance (61.5% from systems first listed in the last two years). Say so; the piece is about the bottom of the list ageing, not the list's capability going stale.
- China's withdrawal from submitting accounts for much of the fall in newcomers. Show or state the non-Chinese count so the newcomer drop is not overstated. The 28-vs-27 newcomer discrepancy with the release: use the file's count and note the release's figure once, without speculating about Horizon beyond what a document says.
- AI clusters: the files do not show where new compute went. Give the TOP500 release's suggestion as the release's, in its words, and say plainly that Epoch's 2.5x-a-year figure is in 8-bit peak capacity and cannot be set against 64-bit HPL. Do not chart the two together. Do not make the AI-cluster story the headline or the conclusion.
- Next Platform's "pause before new chips" view goes in fairly, with the fact that June 2027's list is what would test it.
- The slug stays top500-ageing-installed-base; it fits the revised angle.

## Appendix: the topic scout's candidates (formerly scout-candidates.md, which the researcher brief names; folded in here because the artifact layout allows no extra file)

### Feature candidates, edition of 2026-11-20

#### 1. Microsoft 365's 36-hour outage was a metastable failure (non-AI)

**Angle:** Microsoft's timeline shows the outage outlasting its trigger: by 19:20 UTC load had not risen, returning servers re-failed (23:55), and recovery came only after automated redirects were disabled (01:53) and the July change was reverted (07:20). That is the trigger and sustaining-loop pattern of the metastable-failure literature, a term the report never uses.

**Primary documents opened:**
- Microsoft preliminary PIR EX1550543/MO1550821, 15 Nov (copy hosted by Next): https://next.ink/wp-content/uploads/2026/11/PostIncidentReport.pdf
- The Register, 16 Nov: https://www.theregister.com/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026

**What could be shown:** a loop diagram. A latent lock-contention bug (worse on many-core hardware), the Teams failover 15 h earlier and 14% of capacity out of service set it off. Redirects then put the same load on fewer servers, and more than 80% were down within 2 h. Also a timestamped sequence from 01:07 on 12 Nov to 04:15 on 14 Nov, sorted into trigger, sustaining effect, and what broke the loop. The bulkheads that failed are a second mechanism.

**What might break it:** the final PIR, due today (20 Nov), may revise the cause. The official copy sits in the admin center behind a login, so the hosted copy needs checking.

**Firsthand:** 5

#### 2. The TOP500 is getting old (non-AI-company)

**Angle:** In the list's own files, the median system has been on the list for 6 editions, up from 4 in November 2021, and 138 of 500 systems are five or more years old, against 45 then. The list now measures an ageing installed base while new hardware goes to AI clusters that do not run HPL.

**Primary documents opened:**
- TOP500 release, 16 Nov: https://www.top500.org/news/top500-leadership-holds-steady-new-system-turnover-falls-historic-low/
- List xlsx (no login needed; older lists also available): https://www.top500.org/lists/top500/2026/11/download/TOP500_202611.xlsx
- Next Platform, 16 Nov: https://www.nextplatform.com/hpc/2026/11/16/supercomputer-installs-take-a-dive-in-the-second-half-of-2026/5310221

**What could be shown:** age distributions by "First Appearance" across the November lists, and newcomers per edition (28 by my count, 27 in the release). Also total HPL growth of 4.4% in six months against the 2.5x a year for AI compute that the release cites from Epoch.

**What might break it:** Next Platform reads the gap as a pause before Rubin and MI400 arrive. The June 2027 list could reverse it, and the 2021 list may have been unusually young.

**Firsthand:** 5

#### 3. WHO's TB totals are modelled, and death records halved Mongolia's (non-AI)

**Angle:** In the Global TB Report 2026, WHO's new method built on death records puts Mongolia's 2025 incidence at 223 per 100k, where last year's series had 2024 at 446. India, about a quarter of world cases, is "under review" and goes unpublished. The headline 14% decline since 2015 is therefore mostly model output.

**Primary documents opened:**
- New-method page: https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2026/featured-topics/new-method-to-estimate-tb-incidence-using-tb-mortality-data
- Incidence chapter, with a methods table: https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2026/tb-disease-burden/1-1-tb-incidence
- WHO release, 12 Nov: https://www.who.int/news/item/12-11-2026-amid-challenges-countries-increase-domestic-investment-to-protect-progress-against-tuberculosis
- Previous-vintage CSV (to 2024): https://extranet.who.int/tme/generateCSV.asp?ds=estimates

**What could be shown:**
- Global incidence split by estimation method: prevalence surveys 64%, inventory studies 17%, UHC-index adjustments 10.8% across 123 countries, death-record methods about 2%.
- Mongolia's and Thailand's old and new trajectories side by side.
- The three-source state-space model as a diagram.

**What might break it:** Annex 4 (India) and the technical appendix are unread. If revisions elsewhere are small, the angle narrows to one method in two countries.

**Firsthand:** 4
