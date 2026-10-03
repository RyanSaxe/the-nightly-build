# Evidence record: feature/ai-economy-atlas (01)

The sources establish what each ATLAS headline figure measures, and the measurement
matches the commission's angle. Every work-usage "share" the commission lists is a share
of conversational-AI request volume within a geography, defined in the public dataset's
own data dictionary as "percentage share of total work volume within the geographic
scope." The ATLAS report and the AI-in-Science paper both state in their own words that a
request count is not a measure of task completion, saved time, or labor hours. The
occupation and region shares are not adjusted for how many workers in that occupation or
country exist; only the separate cross-country per-capita intensity metric is adjusted for
platform penetration. So the shares move with who converses with Gemini and how much, which
is the distinction the commission wants to carry through the figures. The science survey's
"almost 7 hours a week" is a self-reported belief from a 637-person non-probability panel
the authors say is not representative.

The angle holds. Where the record is thin: the specific per-country multipliers (India
1.6x, Brazil/Germany 1.4x and 7%, Japan 4%) and the exact U.S. 30% figure for computer and
mathematical occupations are owned by the interactive's detail cards and by Figure 1 of the
report. They are not reproducible from the released public CSV, which exposes only the top
three minor occupation groups per country and withholds major-group volume shares. I
verified their definition and framing against the dataset README, the methodology page, and
the report, and I recomputed the closest available figure (U.S. computer-and-mathematical
broad occupations sum to 20.06% of work volume in the public data, before the "All Other"
detailed occupations the report adds back to reach ~30%). I confirmed the five headline
numbers' exact wording against the blog, which is secondary to its own data.

## Sources

```text
URL:         https://ai.google/static/documents/GoogleATLASv1.pdf
Kind:        primary — Google and Google DeepMind are the authoring and measuring party; this report owns the work-usage figures
Establishes: the ATLAS v1.0 sample, the work/non-work classification pipeline, the occupation-share and task-saturation metrics, and the report's own limitations
Paraphrase:  ATLAS v1.0 analyzes 14,653,926 de-identified interactions across the Gemini App, Google AI Mode, and Gemini API between April 6 and April 19, 2026. An automated classifier splits interactions into work and non-work; work interactions map to BLS 2018 SOC occupations and O*NET v30.2 tasks via the OCTO clustering tool. Figure 1 compares U.S. work-related Gemini interaction shares by major occupation group against OEWS May 2024 employment shares; "Computer and Mathematical" sits at roughly 30% of U.S. work interactions against about 3-4% of U.S. employment. Work-related activity is 14% of conversational (non-API) usage. The report states the depth of use is shallow: AI is used for 21% of tasks in the median occupation with any use, only 3% of occupations show use on over 75% of their tasks, and end-to-end automation attempts are under 10% of non-routine-cognitive conversations.
Locators:    Abstract (p.1); Executive Summary findings 1-10 (pp.2-4); Sec 2 "Data and Methods" + 2.3 "Limitations" (pp.5-7); Sec 3.3 "Occupational AI Usage," Fig 1 + Table 1 (pp.10-12); Sec 3.4, Figs 3-4 (pp.14-17); footnote 1 (p.2)
Quote:       "ATLAS v1.0 measures behavioral interactions, not definitive productivity outcomes. A completed conversation does not guarantee that the user accomplished their intended goal, saved time, or produced measurable economic value." (Sec 2.3, p.7)
```

```text
URL:         https://ai.google/economy/atlas/
Kind:        primary — the interactive is the authoring party's own presentation and owns the per-country detail figures
Establishes: how the interactive frames the occupation chart (two distinct axes) and the per-country breakdowns the blog quotes
Paraphrase:  The interactive loads from https://ai.google/economy/atlas/embed-report-2026/ . Its occupation beeswarm is described as "Each circle represents a broad occupation positioned by share of tasks with non-negligible AI usage," with circles "sized to indicate relative vo[lume]." So the interactive separates task-saturation depth (position) from usage-pool volume (size). Insight text states: "Workplace AI adoption spans all industry sectors and 68.5% of all occupations. Within jobs, however, people use AI selectively for only ~21% of tasks"; "Nearly 65% of work-related AI interactions involve non-routine cognitive tasks ... Explicit task automation accounts for under 10% of these conversations"; "task automation appears in about 26.9% of routine cognitive interactions ... but is rarely used for creative or interpersonal work"; and for manual trades, "they're 2x m[ore]" likely to use multimodal AI. The country detail cards (India, Brazil, Germany, Japan) render from the site's internal data, not the public CSV.
Locators:    Interactive sections Home / Work / Geography; embed document at /economy/atlas/embed-report-2026/ ; insight cards "Workplace diffusion is wide and shallow," "Collaboration over automation," "Automation rate by task type," "Manual workers are using multimodal AI to solve problems in real time"
Quote:       "Each circle represents a broad occupation positioned by share of tasks with non-negligible AI usage."
```

```text
URL:         https://ai.google/economy/atlas/data/atlas_v1_public_data.zip  (served from /economy/atlas/embed-report-2026/data/atlas_v1_public_data.zip)
Kind:        primary — Google's released dataset and data dictionary (CC-BY 4.0); owns the operational definition of every share
Establishes: the exact denominator for occupation and region shares, and which figures the public data can and cannot reproduce
Paraphrase:  The archive holds atlas_v1_work_occupations.csv, atlas_v1_geography_intensity.csv, atlas_v1_household_activities.csv, and README.md. The README defines percentage_of_total as "Percentage share of total work volume within the geographic scope" (GLOBAL or US), available only at the broad-occupation level. It defines non_negligible_ai_use and intensive_ai_use as task saturation (share of an occupation's O*NET tasks with observed use above a 25-user and 100-user threshold), reported only at the global level, and full_automation_pct as "the estimated proportion of work interactions where users requested end-to-end task execution rather than iterative co-piloting." It warns that broad-level shares "will not aggregate to the Major occupation shares ... This stems from the exclusion of 'All Other' Detailed occupations." Geography rows give work_share_pct, a per-capita intensity_quintile "adjusted based on variation in platform penetration," top-three languages, and top-three minor occupation groups per country with their volume-share percentages. Differential privacy and suppression are applied.
Locators:    README.md lines 29-66 (occupational metrics + column table), 90-125 (geography), 40-54 (task saturation/automation definitions), 34-38 ("All Other" aggregation note)
Quote:       "percentage_of_total | float | Percentage share of total work volume within the geographic scope | 0.00% to 100.00%"
```

```text
URL:         https://ai.google/economy/atlas/methodology/
Kind:        primary — the project's methodology note
Establishes: the classification pipeline and that shares are built from request volume
Paraphrase:  Confirms the automated work/non-work classifier, the OCTO clustering, the SOC+O*NET mapping for work and ATUS for non-work, the 14,653,926-interaction sample over April 6-19 2026, and that "share of AI usage per occupation group" is "the relative volume of conversational AI queries associated with each occupation group." States the cross-country analysis adjusts for Google app penetration differences between countries.
Locators:    Methodology page, "Classification," "Share of AI Usage per Occupation Group," "Sample," "Cross-country" sections
Quote:       Share of AI usage per occupation group is "the relative volume of conversational AI queries associated with each occupation group per capita."
```

```text
URL:         https://ai.google/static/documents/AI-in-Science.pdf
Kind:        primary — the Google / Google DeepMind / MIT FutureTech science paper ("AI in Science: Early Insights," September 2026); owns the scientist-survey figures
Establishes: the "nearly half use AI daily" and "almost 7 hours saved" figures, their survey instrument, sample, and the authors' stated limitations
Paraphrase:  Three data sources: ~15 million Gemini interactions (the ATLAS 1.0 corpus, sampled early April 2026) filtered through a three-stage classifier to ~360,000 science interactions; an inventory of 2,690 specialized AI models; and an original survey of 637 active scientists in the U.S. and U.K. run by a third-party provider through the More in Common online panel between 27 July and 11 August 2026, using a four-criterion screen, reported unweighted and explicitly "not ... representative of the universe of scientists." Figure 11 reports self-reported AI-use frequency: "Intensively (e.g. Daily)" 46.6% (n=297), "Frequently (e.g. Weekly)" 30.6% (n=195), "Sometimes" 15.5% (n=99), "Rarely or Never" 7.2% (n=46); Daily Active 46.6%, Weekly+ 77.2%. The time-saving figure: "just below three quarters of respondents report that AI saves them time on net ... compared to only 6% reporting net time lost. The average scientist's time savings are around 6.9 hours per week," following the firm-productivity method of Yotzov et al. (2026). Limitations (Sec 6.1): selection bias from enthusiastic AI users over-responding, which "could potentially overestimate the real adoption rate and the average weekly time savings"; results are "associations rather than causality." Footnote 14 (p.11) on the log data: "we only know the absolute numbers of requests, rather than having measures of interactions that are equivalent total labor hours. We also do not see task completion or saved time."
Locators:    Abstract (p.1); Sec 2.2.3 "Scientist Survey" (p.7); Sec 5.1-5.2 + Fig 11 (pp.22-24); Sec 6.1 "Limitations" (pp.26-29); footnote 14 (p.11)
Quote:       "almost 47% of the surveyed researchers use some form of AI daily, while another 31% use it weekly." (p.23) / "The average scientist's time savings are around 6.9 hours per week." (p.23)
```

```text
URL:         https://futuretech.mit.edu/publication/scientific-work
Kind:        primary — the MIT FutureTech taxonomy (Emmens, Liu, Trišović, Thompson, 14 September 2026) that both Google papers map onto
Establishes: the scientific-task taxonomy structure and its definition of scientific work
Paraphrase:  "Scientific Work" builds a taxonomy from scientific research job adverts (the AI-in-Science paper cites ~3.8 million adverts and over 64 million extracted task instances, consolidated to ~210,000 representative tasks; the page states 208,202). The hierarchy is 12 Level-1 task areas, 114 Level-2 categories, and 2,433 Level-3 groups. It defines a scientific research job as one whose primary responsibility is to generate, or support generation of, new scientific knowledge, and characterizes scientific tasks as more cognitive, less interpersonal, less manual, and less codifiable than general economic tasks.
Locators:    Publication page "Scientific Work"; cross-referenced in AI-in-Science Sec 2.2.4 (p.8)
Quote:       Taxonomy covers "12 Level-1 areas, 114 Level-2 areas, and 2,433 Level-3 groups" (AI-in-Science, p.8).
```

```text
URL:         https://blog.google/innovation-and-ai/technology/ai/ai-economy-atlas-september-2026/
Kind:        secondary — Google's announcement post; secondary to its own data per the source policy; owns the exact public phrasing of the five headline numbers
Establishes: the verbatim wording of each commission figure, so the writer quotes the claim as the study framed it
Paraphrase:  The post states the five figures the commission lists. It links the interactive, the AI-in-Science paper, and the MIT FutureTech taxonomy.
Locators:    Post body, "Work" and "Science" sections
Quote:       "computer and mathematical occupations accounting for 30% of work-related AI usage, double the share in the rest of the world"; "India's creative industry ... arts, design, and media occupations making up 19% of work-related AI usage, 1.6 times the global average"; "In Brazil and Germany, 7% of work AI usage goes toward manual tasks (1.4 times the global average), compared to 4% in Japan"; "Nearly half of surveyed scientists use some form of AI every day"; "savings of just below seven hours a week"
```

```text
URL:         https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/  (arXiv: https://arxiv.org/abs/2507.09089)
Kind:        primary for its own result, independent of Google — a randomized controlled trial on the gap between perceived and measured AI time savings
Establishes: that self-reported or forecast time savings from AI can run opposite to measured time, which bears on reading the survey's "6.9 hours saved"
Paraphrase:  METR (Joel Becker, Nate Rush, Beth Barnes, David Rein), 10 July 2025. 16 experienced open-source developers completed 246 real tasks from their own repositories, randomized to use or not use early-2025 AI tools. With AI allowed, they took 19% longer. They had forecast a 24% speedup beforehand and still believed AI had sped them up by 20% afterward. The page carries a note that a February 2026 METR follow-up on late-2025 tools found different results, so this is a point estimate for early-2025 tools on expert open-source work, not a general law.
Locators:    METR blog post, "Headline result" and "Discussion"; arXiv 2507.09089
Quote:       "When developers are allowed to use AI tools, they take 19% longer to complete issues—a significant slowdown that goes against developer beliefs and expert forecasts."
```

```text
URL:         https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/  (SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5219933)
Kind:        primary for its own result, independent of Google — labor-economics study on whether chatbot adoption and self-reported time savings show up in measured outcomes
Establishes: that widespread AI adoption and reported time savings need not translate into measured hours or earnings, which bounds what a usage share or a time-saving self-report can claim about economic impact
Paraphrase:  Anders Humlum (Chicago Booth) and Emilie Vestergaard, Becker Friedman Institute, April 2025. Two large adoption surveys (late 2023 and 2024) across 11 exposed occupations, linked to Danish administrative employer-employee records. Despite rapid adoption, difference-in-differences estimates find precise null effects on earnings and recorded hours, ruling out effects larger than about 1-2%. Average self-/employer-reported time savings among users are modest (about 3% of hours, reported in coverage as ~2.8 hours per week saved), and only a small share passes through to earnings; new AI-created tasks offset part of the saved time.
Locators:    BFI WP 2025-56 abstract and Secs on time use and earnings; SSRN 5219933
Quote:       "AI chatbots have had no significant impact on earnings or recorded hours in any occupation, with confidence intervals ruling out effects larger than 1%." (abstract, as reported; a later version states "ruling out effects larger than 2% two years after")
```

## Contradictions

- Public dataset vs headline, U.S. computer/mathematical: the blog and Figure 1 report ~30%
  of U.S. work AI usage. The released public CSV cannot reproduce this. Summing every U.S.
  broad-occupation share in the 15- series (computer and mathematical) gives 20.06%. The
  README states broad shares exclude "All Other" detailed occupations and so do not
  aggregate to the major-group total, which accounts for the ~10-point gap. The 30% figure
  is therefore only directly available in Figure 1 and the interactive, not in the public
  data. Record the 30% to the report's Figure 1, not to the dataset.
- "7 hours" has two distinct referents in the science paper. The net time *saved* is ~6.9
  hours/week (Sec 5.2, p.23). Separately, scientists report *spending* "about 7 hours per
  week" on data analysis and interpretation (Sec 5.2, p.23). The commission's "~7 hours
  saved" is the first. Do not conflate them.
- Science-survey adoption (46.6% daily) vs ATLAS workplace depth. The science paper reports
  heavy, frequent adoption among scientists; the ATLAS report stresses shallow penetration
  (21% of tasks in the median occupation). These are not in conflict: the first is
  self-reported frequency of any use from a survey, the second is task saturation from logs.
  The writer should keep the two metrics apart rather than reconcile them.
- Independent evidence vs the survey's time-saving reading. METR (measured time opposite to
  perceived) and Humlum-Vestergaard (adoption and reported savings without measured hours or
  earnings effects) both cut against treating the 6.9-hour self-report as a measured economic
  gain. Neither studies scientists specifically; they bound the inference, not the datum.

## Numbers

```text
Figure: U.S. "Computer and Mathematical" = ~30% of U.S. work-related AI usage; ~3-4% of U.S. employment (OEWS May 2024)
Owner:  ATLAS v1.0 report, Figure 1 (p.11), and blog
Scope:  share of U.S. work-related Gemini request volume (App + AI Mode + API), April 6-19 2026; "double the share in the rest of the world" implies rest-of-world ~15% (not given as a number in the public data)
```

```text
Figure: U.S. computer-and-mathematical broad occupations = 20.06% of U.S. work volume in the public CSV (15-1250 9.22; 15-1240 5.22; 15-1290 2.19; 15-1210 1.23; 15-1230 0.98; 15-1220 0.62; 15-2050 0.23; 15-2040 0.20; 15-2020 0.09; 15-2030 0.04; 15-2010 0.03; 15-2090 0.01)
Owner:  atlas_v1_work_occupations.csv (US rows)
Scope:  broad-occupation volume shares, excludes "All Other" detailed occupations; does not equal the 30% major-group headline (README note)
```

```text
Figure: India "Arts, Design, Entertainment, Sports, and Media" = 19% of work AI usage, 1.6x the global average
Owner:  interactive country card + blog (implies global arts major-group share ~11.9%)
Scope:  share of India work request volume; public CSV confirms only the minor group "Art and Design Workers" at 10.15% of India work volume (top_occupation_3), consistent with but not equal to the 19% major-group figure
```

```text
Figure: Brazil and Germany = 7% of work AI usage on manual tasks (1.4x global); Japan = 4%
Owner:  interactive country cards + blog (implies global manual-task share ~5%)
Scope:  share of each country's work request volume directed at manual tasks; not in the public CSV; Brazil/Germany/Japan work_share_pct overall = 12.86% / 10.86% / 14.87%
```

```text
Figure: scientists using AI "Intensively (e.g. Daily)" = 46.6% (n=297); Weekly 30.6% (n=195); Sometimes 15.5% (n=99); Rarely/Never 7.2% (n=46); Weekly+ = 77.2%
Owner:  AI-in-Science, Figure 11 (p.24)
Scope:  self-report, 637 U.S./U.K. scientists, More in Common panel, 27 Jul-11 Aug 2026, unweighted, not representative; question asked how intensively they use AI in their scientific research
```

```text
Figure: scientists' net time saved = ~6.9 hours/week (abstract: "just below 7 hours"); ~74% report net time saved, 6% net time lost
Owner:  AI-in-Science, Sec 5.2 (p.23)
Scope:  self-reported, same 637-scientist survey; method follows Yotzov et al. (2026)
```

```text
Series (task-metric table, GLOBAL major occupation groups) — columns: non_negligible_ai_use % / intensive_ai_use % / full_automation_pct % / non_routine_cognitive_pct %
15-0000 Computer & Mathematical: 46.36 / 30.26 / 15.94 / 89.45
13-0000 Business & Financial Ops: 42.99 / 28.35 / 7.37 / 79.55
41-0000 Sales & Related:          38.96 / 19.35 / 5.84 / 23.12
43-0000 Office & Admin Support:   38.45 / 23.87 / 30.30 / 6.23
27-0000 Arts/Design/Media:        37.63 / 23.11 / 3.45 / 87.24
11-0000 Management:               32.50 / 17.10 / 1.82 / 57.46
17-0000 Architecture/Engineering: 27.95 / 13.75 / 5.83 / 90.63
19-0000 Life/Physical/Soc Science:25.07 / 11.79 / 2.20 / 91.06
23-0000 Legal:                    22.76 / 16.26 / 4.42 / 94.15
29-0000 Healthcare Practitioners: 17.18 / 6.65  / 7.63 / 53.18
49-0000 Install/Maint/Repair:     18.96 / 9.81  / 0.64 / 30.61
31-0000 Healthcare Support:       11.57 / 4.48  / 18.11 / 8.12
51-0000 Production:               11.04 / 3.34  / 10.16 / 28.11
37-0000 Building/Grounds Cleaning: 9.52 / 1.19  / 2.57 / 9.31
Owner:  atlas_v1_work_occupations.csv (GLOBAL rows); full 22-group series in file
Scope:  task saturation and intent metrics, global, April 2026; distinct from the volume shares above — this is depth of use within a job, not share of the usage pool
```

```text
Figure: workplace depth — AI used for 21% of tasks in the median occupation with any use; 68.5% of occupations show some use; 3% of occupations show use on >75% of tasks; 11% on >half
Owner:  ATLAS v1.0 report Sec 3.4 / Figs 3-4 (pp.14-17) + interactive
Scope:  O*NET task saturation, global, April 2026
```

```text
Figure: end-to-end automation attempts < 10% of non-routine-cognitive conversations; ~65% of work interactions are non-routine cognitive; routine-cognitive automation ~26.9%
Owner:  ATLAS v1.0 report Executive Summary finding 3 (pp.2-3) + interactive
Scope:  intent classification over work conversations, April 2026
```

## Limits

- The per-country headline multipliers the commission names (India 1.6x, Brazil/Germany
  1.4x and 7%, Japan 4%) and the U.S. 30% major-group figure are not reproducible from the
  released public dataset. The public CSV withholds major-group volume shares and exposes
  only the top three minor occupation groups per country. I confirmed the definition and
  framing of these figures from the README, the methodology page, and the report, and gave
  the closest reproducible figures, but I could not independently recompute the exact
  multipliers. Treat them as owned by the interactive's internal data and the report's
  Figure 1.
- The "rest of the world" and "global average" baselines behind "double" (computer/math),
  "1.6x" (arts), and "1.4x" (manual) are not published as explicit numbers in the public
  data; they are implied by the multipliers. The writer can state the implied baselines
  (~15%, ~11.9%, ~5%) only as back-calculations, labeled as such.
- ATLAS occupation shares exclude paid/enterprise Gemini API usage (report Sec 2.3,
  limitation 1), so professional and enterprise work is under-represented by the authors'
  own account. This bounds the "who is using it" reading in the same direction as the angle.
- The science survey's selection bias runs one way the authors name: enthusiastic AI users
  over-respond, so 46.6% daily and 6.9 hours saved are, in the authors' words, likely
  over-estimates of the scientist population. I could not find the survey's response rate or
  the panel's sampling frame beyond "More in Common online panel"; the paper gives neither.
- The independent limit-literature (METR, Humlum-Vestergaard) is about general knowledge
  work and chatbot users, not scientists, and not Gemini specifically. It constrains the
  inference from a self-reported time saving to a measured economic gain; it does not
  measure the ATLAS or science-paper populations. METR's own February-2026 follow-up
  reportedly found different results for later tools, which the writer should note if the
  METR point is used.
- Everything asked about the denominators and the gathering method (telemetry/classifier
  vs survey, sample sizes, dates) was established. The classifier is probabilistic; the
  report states granular occupation findings "carry more uncertainty than broader,
  major-group trends" (Sec 2.3, limitation 4).

## Source assets

```text
Asset: ATLAS v1.0 report, Figure 1, "White-Collar Professions Are Overrepresented in AI Usage Relative to US Employment" (p.11)
Shows: the gap between an occupation's share of U.S. AI request volume (orange) and its share of U.S. employment (blue) — the exact visual the piece's argument rests on, with Computer and Mathematical at ~30% usage vs ~3-4% employment
Crop:  keep both the orange usage dots and blue employment dots and the axis label "Percentage of Total (%)"; keep the top rows (Computer and Mathematical, Business and Financial, Office and Admin) legible; the caption's "shares of US work-related Gemini interactions ... to shares of civilian US employment" must stay or be restated
```

```text
Asset: ATLAS v1.0 report, Figure 4, "For Occupations with Observed Gemini Usage, Workers Are Generally Using AI for Less Than One Quarter of Their Tasks" (p.17)
Shows: the task-saturation distribution clustered below 0.25 — the depth metric that the volume-share metric is distinct from
Crop:  retain the x-axis "Saturation Share" and the mass of the distribution below 0.25; do not crop out the long thin right tail, which carries the "few occupations are saturated" point
```

```text
Asset: AI-in-Science, Figure 11, "Self-Reported Frequency of AI Use in the Sample of Scientists" (p.24)
Shows: the 46.6% / 30.6% / 15.5% / 7.2% split with n per bar and the survey question in the note
Crop:  keep the percentage and n= labels and the note stating "Survey of 637 scientists ... More in Common ... July-August 2026"; the note is what marks the figure as self-report, so it must stay
```

```text
Asset: atlas_v1_work_occupations.csv (GLOBAL major-group rows), rendered as a table or chart
Shows: usage-volume share vs task-saturation vs automation intent side by side, so one occupation's "big share of usage" sits next to its "shallow share of tasks" — the piece's central comparison, buildable with nb chart from a verified series (table in Numbers above)
Crop:  n/a (data series)
```

## Discarded

```text
URL: https://ai.google/economy/atlas/  (first fetch) — returned the generic ai.google nav shell, not the interactive content; superseded by the embed document at /economy/atlas/embed-report-2026/
URL: https://blog.google/technology/ai/ai-economy-atlas/ — 404; the live post is at /innovation-and-ai/technology/ai/ai-economy-atlas-september-2026/
URL: https://axios.com/2026/07/23/google-ai-adoption-work-atlas — secondary coverage of ATLAS; adds no number the primaries lack, and reports an earlier July snapshot
URL: https://ppc.land/google-finds-ai-touches-68-of-jobs-but-only-21-of-their-tasks/ — secondary; the 68%/21% figures are read directly from the report instead
URL: https://the-decoder.com/ai-coding-can-make-developers-slower-even-if-they-feel-faster/ — secondary retelling of the METR study; the METR primary and arXiv are cited instead
URL: https://marginalrevolution.com/.../large-language-models-small-labor-market-effects.html — secondary blog note on Humlum-Vestergaard; the BFI/SSRN primary is cited instead
URL: https://www.fortegrp.com/insights/task-level-not-job-level-... — vendor commentary on ATLAS; no independent measurement
```
