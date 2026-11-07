# Evidence record: feature/anthropic-rd-acceleration-review (researcher 01)

Every figure in the commission checks out against METR's 5 November review: 1.97, 1.3 to 2.8, AECI 1.5x and 1.9x, "slightly less than twice as fast", "plausible", and "most relevant researchers ... lean toward the threshold not having been crossed". The 81x doubling example appears word for word in RSP v3.4 and the August 2026 Risk Report. The angle as written does not survive one test. The estimates do not measure one quantity, so they cannot honestly share one axis as tests of the threshold. The 1.97 is METR's own calculation from a redacted internal leading indicator. Anthropic describes leading indicators as metrics that predict later capability trends, and the RSP threshold is defined on "AI aggregate capabilities". The private sentence behind it also assumes that "all of the observed speedup" is due to AI, so it is an upper bound on attribution. The "slightly less than 2x" estimates are counterfactual speedups (with AI versus without), and the RSP v3.4 changelog says a counterfactual speedup alone does not cross the threshold. Only the AECI slope ratios (1.5x, 1.53x, 1.70x, 1.9x, 1.9x) measure the threshold's quantity directly, and those come from different model sets, fits and dates. The angle holds in a narrower form. Every estimate that measures a rate of progress falls between about 1.1x and 2.9x, the line sits inside that band, and the answer moves with the definition and the window. Three findings go beyond the commission. First, the public Risk Report states the threshold with a stricter attribution test ("attributable primarily") than the RSP text ("plausible that this doubling is substantially attributable"). Second, Anthropic's own public AECI slope figure rose from 1.53x (Opus 5.5 card, 22 September) to 1.70x (Haiku 5.5 card, 7 October). Third, Anthropic's amended S-1 (2 November) says internal estimates for future models indicate it "may imminently meet" the threshold, and says it "ha[s] in the past not identified" a significant acceleration until after it occurred. The thin parts: the leading indicators and METR's 1.3 to 2.8 analysis are redacted, so nobody outside can check what they measure, and I found no Anthropic public response to METR's review.

## Sources

### S1. METR, review of the Risk Report's automated-R&D section

```text
URL:         https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/
Kind:        Primary for METR's judgments and METR's own calculations (1.97, 1.3–2.8, AECI 1.5x/1.9x
             re-estimates, preferred language). Secondary for the private Risk Report's wording: it is
             the only public copy of those passages, and METR reports them as an outside party with
             Anthropic-approved redactions.
Establishes: Firsthand: METR's assessment and calculations. Repeats: quotes from the public and private
             Risk Report and RSP v3.4 (the public quotes match the PDF; see S2 and S3).
Locators:    Section headings on the page: "Executive summary"; "Summary of Anthropic's Risk Report";
             "METR's assessment" > "Claim 1", "Claim 2", "Claim 3", "Despite this…"; "Process details";
             footnotes 1–3. Dated November 5, 2026. Authors (fn 1): Tom Cunningham, Nate Rush,
             Parker Whitfill, Hjalmar Wijk. The page gives no job titles.
```

Paraphrase, by locator:

- Redaction summary (top): Anthropic had rights to redact non-public information. METR could disclose whether it did, and says that every redaction important to its conclusions is described in the post.
- Executive summary, para 1–3: METR agrees catastrophic risk from July 15th models was low, "but we think it is plausible that they had crossed their early warning threshold at the time." The public report's not-crossed claim "relies on contestable judgment calls that aren't communicated clearly". "While both METR's researchers on this project and Anthropic's relevant staff lean toward it not having been crossed, we think it is plausible that it had been, and we believe the public report overall understates the level of acceleration that was occurring." The review was part of a "high-access assessment" in which Anthropic shared a private version of the Risk Report.
- Summary section: the names "Full Substitution Threshold" and "2x Acceleration Threshold" are METR's. Quote: "although we give these thresholds names for clarity … they do not have names in the RSP." Footnote 2 quotes the RSP v3.4 operationalization in full, including the 81x example.
- Summary section: the overall "low/medium/high" rating is about the risk that models directly enable catastrophe, not the risk of crossing the RSP threshold. METR got this "Based on these descriptions and conversations with Anthropic staff".
- METR's assessment, Full Substitution: METR finds the not-crossed argument "broadly compelling", with confidence "much lower than it was in the past" because no unsaturated high-confidence benchmarks remain.
- METR's assessment, 2x threshold: "Most relevant researchers at METR and Anthropic lean toward the threshold not having been crossed on July 15th, but we think it is plausible that it had been."
- Claim 1 (leading indicators): the private report says "[redacted] progress rates have less than doubled even if we attributed all of the observed speedup to AI assistance". METR's note says "the acceleration rate implied by [redacted]×/yr is 1.97. The 1.97 figure does not appear in the private report; this is our calculation that combines the report's estimate of the current rate of progress above with an estimate of the historical rate of progress elsewhere in the private report." METR says "around 2" would describe it better. METR's own analysis of the leading indicators "finds a range of reasonable estimates, between 1.3 and 2.8". It reports "substantial methodological uncertainty", and says Anthropic redacted that discussion. METR's preferred language adds: "We are uncertain how these leading indicators relate to downstream capabilities."
- Claim 2 (attribution): the private report quotes give "slightly less than twice as fast as it would be without AI assistance" and "slightly less than a factor of 2 for [redacted]. … more likely to be an overestimate than an underestimate; nonetheless … it seems plausible we do exceed this factor of 2 overall." METR "broadly agree[s] with the private risk report's assessment". METR's preferred language says the factor rests on "interviews with research leads and informal surveys".
- Claim 3 (AECI): the public report omits the private qualification that Anthropic expected higher scores from later Model 2 snapshots, and "further snapshots of Model 2 did improve on AECI by about the same amount as Mythos 5 did over Mythos Preview." "If we reuse the data that was used in the Risk Report, the estimated acceleration is around 1.5x. After the publication of the Risk Report, Anthropic added data from more benchmarks, which estimates an acceleration of 1.9x using the same set of models." Fn 3: a naive extrapolation using only the models most optimized for capability "led us to more correctly forecast future AECI scores".
- "Despite this…": METR thinks 2x counterfactual acceleration by July 15th plausible, but "significantly greater acceleration would likely be necessary" for the catastrophic scenarios. METR "cannot rule out a substantial further acceleration in the pace of capabilities progress over the next 6 months. This could rapidly lead to 'high' risk".
- Process details: Anthropic asked METR to write the review after the engagement began, and the scope "was never formalized". Timeline: 12 Aug sharing begins; 14 Aug unredacted report shared; 18 Sep first draft; 28 Oct final redaction guidance; 29 Oct Anthropic approves.

### S2. Anthropic, Risk Report: August 2026 (public, redacted)

```text
URL:         https://www.anthropic.com/aug-2026-risk-report  (Anthropic's own link from its RSP page; it
             redirects to the PDF at https://assets.claude.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378.pdf.
             METR links the same file at https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf)
Kind:        Primary. Anthropic authored it and owns its risk determinations. 186 pages; printed page
             numbers match PDF page numbers.
Establishes: Firsthand: Anthropic's public case, the threshold text it reports, AECI figure, coverage date.
Locators:    Table 1.2.B p.11; §1.3.1 and Table 1.3.1.A p.13 (fn 4, 5); §1.3.3 p.14; §1.3.4–1.4 p.15–16;
             §3.1 Table 3.1.A p.93–94; §3.2 p.94–96; §3.4 p.97; §3.4.2 p.99; §3.5 p.101–102;
             §3.5.1 p.102–103; §3.5.2 p.103; §3.8–3.9 p.112; §3.10 Table 3.10.A p.113–114.
```

Paraphrase, by locator:

- p.11, Table 1.2.B, "Current usage and capabilities": "Claude now authors a large majority of the code merged into our production codebases. We believe our internal AI R&D efforts are significantly faster than they would be without AI assistance, but not yet by a factor of 2 (though we are uncertain and measurement is difficult)." Overall risk: "Low. We do not believe our models meet either RSP criterion … we are seeing early signs of acceleration." (The §3.1 table on p.93 has "early signs of potential acceleration". METR quotes the p.93 wording.)
- p.13, §1.3.1: the threshold was updated in v3.1 and v3.4. RSP v3.0 wording: "compress two years of 2018 – 2024 AI progress into a single year." Current wording is quoted in S3 below. Fn 4 has the "double the rate of progress" definition and the 9x to 81x example. Fn 5: "Over at least three model generations."
- p.14, §1.3.3: coverage date July 15, 2026. The report covers the period from the February 24, 2026 report to that date.
- p.15, §1.3.4: the only redactions in the all-staff version are in §3.5.
- p.15–16, §1.4: "Model 2, which is somewhat more capable than Mythos 5 … does not display a capability jump of the degree observed from Claude Opus 4.6 to Mythos Preview."
- p.97, §3.4: the substitution argument, quoted by METR. Fn 40: Anthropic has not run experiments spending 5x the cost of a researcher, "so this claim is in some ways unverified".
- p.99, §3.4.2: Mythos Preview staff survey, "geometric mean self-reported uplift was on the order of 4×". 1 of 18 respondents thought there was already a drop-in entry-level replacement. Anthropic says "productivity uplift on individual tasks does not translate directly into acceleration of research progress" and that it has "deprioritized this source of evidence".
- p.101, §3.5: "The most acute version of this threat model … is a transition to super-exponential progress … producing something like a 10³–10¹⁰× effective scaleup within a year." "The risk threshold set out in our RSP—a doubling of the pace of progress beyond pre-AI-acceleration rates, attributable to automation of AI R&D—functions as a potential early warning, rather than evidence that the threat has already materialized."
- p.102, §3.5: AECI is "our internal fork of Epoch AI's Epoch Capability Index". Leading indicators are "metrics that we believe could be predictive of later trends in AECI". "The nature of these indicators, and trends in them, are sensitive and not included in the public version of this report."
- p.102, Figure 3.5.A: "Frontier trend through Claude Opus 4.6: 13.5 AECI/yr (n=8)". Mythos Preview and Mythos 5 plot above the dashed line.
- p.103, §3.5.1: Mythos Preview's departure from trend is attributed to "specific research progress that … we do not believe was significantly accelerated by AI". Mythos 5 "lies above the historical score trendline by a similar amount to Mythos Preview, which is weak evidence against a dramatic increase". Model 2 is "around 1.5 points higher on AECI than Claude Mythos 5, with large error bars".
- p.103, §3.5.2: "Our leading indicators point to a picture of meaningful acceleration starting in early-to-mid 2025, though by less than a factor of 2. We are fairly confident in attributing the acceleration in 2025 to factors other than our use of AI models, though we also believe that our AI models have been a key factor in the faster trends continuing through the coverage date." Quote: "We conclude that the overall pace of progress remains below the RSP threshold of a doubling over pre-AI-assisted rates of progress attributable primarily to AI R&D automation, but even with our additional sources of data this conclusion is uncertain and subject to some lag". The word "primarily" is the evidence; see Contradictions.
- p.112, §3.8: "we believe it is plausible that this threat model will become a major concern in the next 6–12 months." §3.9: "bearing in mind that we may cross this threshold in the coming year."

### S3. Anthropic, Responsible Scaling Policy v3.4

```text
URL:         https://www-cdn.anthropic.com/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf
             (listed as "Version 3.4" on https://www.anthropic.com/responsible-scaling-policy)
Kind:        Primary. Anthropic's policy text, which defines the threshold.
Establishes: Firsthand: the threshold definition and the v3.4 change rationale.
Locators:    Title "Version 3.4, Effective July 8, 2026" (p.1). Threshold table, row "Automated R&D in key
             domains", p.8–9; footnotes 8 and 9 on p.9. Changelog entry "July 8, 2026 (RSP v3.4)", item 1, p.19–20.
```

- p.9, threshold text: "We will consider this threshold to be met if we determine that either (1) our models would be able to fully substitute for our entire set of Research Scientists and Research Engineers, at competitive costs (i.e., within a factor of 5); or (2) there is 'dramatic acceleration' of the pace of AI progress for reasons that likely relate to the automation of AI R&D. We would consider scenario (2) to have occurred where (a) we observe or expect double the rate of progress [fn 8] in AI aggregate capabilities compared to both the rate we'd expect and the fastest rate of extended progress [fn 9] we've observed in the absence of significant AI contributions to AI R&D and (b) it is plausible that this doubling is substantially attributable to the automation of research and/or engineering (as opposed to other factors, such as increased headcount, compute, or general productivity), such that continuation of the trend in AI progress seems likely to lead to even greater acceleration."
- p.9, fn 8: "'Double the rate of progress' means 'as much progress in one year as one would see in two years at baseline.' For example, if baseline progress involved a 3× scaleup in compute and a 3× improvement in algorithmic efficiency (for a 9× 'effective scaleup'), 'double the rate of progress' would entail something like an 81× effective scaleup. This is not the same idea as 'doubling researchers' productivity,' since doubling inputs does not necessarily double the rate of progress." Fn 9: "Over at least three model generations."
- The RSP text does not call this an "early warning" threshold. That phrase is the Risk Report's (S2 p.101) and METR's (S1).
- p.19–20, changelog item 1 (this passage is evidence in its wording): "It revises the Automated R&D capability threshold in light of further issues that have come up in discussion - particularly the question of whether we'd consider the threshold to be crossed if the overall rate of AI progress were constant or slowing, but we estimated that it was dramatically faster than it would be in the absence of advanced AI tools. We would not: in this case there could be a strong argument for expecting the trend to continue rather than accelerate … This threshold is intended to capture the onset of dramatic recursive self-improvement, and has proven difficult to operationalize."

### S4. Anthropic, RSP web page (version list and update notes)

```text
URL:         https://www.anthropic.com/responsible-scaling-policy
Kind:        Primary. Anthropic's own changelog page.
Establishes: Version dates; v3.1 rationale for the doubling definition.
Locators:    "Current and Prior Versions" list; update notes dated "April 2, 2026" and "July 8, 2026".
```

- Versions: 3.4 effective July 8, 2026; 3.0 effective February 24, 2026. The page is headed "Last updated Aug 14, 2026" and lists the August 2026 Risk Report under August 14, 2026.
- April 2, 2026 note: in v3 the "compress two years … into a single year" language "could have been read as AI 'doubling the rate of progress in aggregate AI capabilities', or 'doubling the productivity of researchers'. In v3.1, we are clear that we mean the former and not the latter."

### S5. METR, Independent Assessment of AI R&D Acceleration at Anthropic in October 2026

```text
URL:         https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/
Kind:        Primary. METR's own assessment and calculations, published November 5, 2026, with an
             update log dated November 6, 2026 (AEF-1 checklist corrections only).
Establishes: Firsthand: METR's October 2026 estimates, its definitions, robustness ranges, process, redactions.
Locators:    Anchors #executive-summary, #our-conclusions-on-risk, #key-findings, #process-details,
             #limitations, #methodology, #benchmark-scores-aeci, #evidence-of-ai-speedup,
             #interview-quotes, #adversarial-robustness, #process-transparency-disclosures, #update-log.
```

- Redaction summary: "Anthropic redacted a majority of the evidence we found most informative for these conclusions." The public "has to rely on METR's judgment much more than would be ideal".
- #executive-summary / #our-conclusions-on-risk: "As of October 2026, Anthropic is likely improving the capabilities of their models on well-specified tasks at around twice the rate they did between March 2024 and October 2025. … we would not be surprised if the true acceleration was closer to 1.3x or 3x the historical rate." This is a subjective conclusion of "most METR staff who worked on this project", and the team still has "internal disagreements". METR guesses "a majority (perhaps ≈80%) of the current (October 2026) acceleration is due to AI". It is "confident" the acceleration was not due to faster growth in training compute.
- #key-findings, terminology: "a 2x acceleration means that 2 years of historical progress is made in 1 year. If AECI's historical trend was 15 points/year, then increasing to 30 points/year implies an acceleration rate of 2 … If a variable is growing 3x/year, then to make 2 years of progress in 1 year the growth rate must be (3²)x/yr = 9x/yr (and acceleration can be written as ln(9)/ln(3) = 2)."
- #key-findings: AECI "accelerated 1.9x [95% confidence interval: 1.5–2.8x] since October 2025". Breakpoint estimated at October 7, 2025 (#benchmark-scores-aeci). The series includes the internal models Model 2 (finished training July 2026), Model 3 (Aug–Sep 2026) and Model 4 (Sep–Oct 2026) (#methodology). "Our estimated acceleration is greater than that reported in the Haiku 5.5 system card (1.7x) primarily because of the inclusion of data on newer unreleased models." Robustness checks run from 1.1x to 2.9x.
- #key-findings, interviews: "a quite wide range of estimates, but centered around a 2x acceleration". Slack polls reached "12x in October 2026" self-reported uplift. METR calls these "only very loose evidence" and warns that "individual uplift/speedup estimates do not correspond to acceleration rates."
- #process-details: METR staff equal to 2.5 FTE worked eleven weeks (Aug 12 to Oct 29). "In this assessment, we do not pay special attention to the thresholds set in the RSP." Anthropic "changed the scope of this project midway to exclude compute verification". This engagement "is distinct from the assessment announced on October 15". METR took no payment. Anthropic provided free tokens and devices.
- #methodology: three growth rates. Historical (before the detected trend change), current (as of October 2026), counterfactual ("as of October 2026, if Anthropic could not use AI"). "The first two are observable quantities. The counterfactual growth rate we can only guess at." Instantaneous acceleration differs from cumulative acceleration, and "some interviews and documents are implicitly or explicitly discussing cumulative acceleration".
- #benchmark-scores-aeci: link-function table. Logistic 1.9x [1.5–2.8]; probit 1.8x [1.3–2.7]; cauchit 2.8x [2.0–4.1]; complementary log-log 1.1x [0.8–1.5]; log-log 2.9x [2.1–4.9]; learned Stukel 2.6x [1.8–4.1]. Out-of-sample R² is 86.1–87.2% across all of them. Snapshot variants 1.9–2.2x; benchmark variants 1.9–2.2x; regularization 1.9–2.1x. With all developers' frontier models the estimate is 1.4x, with two interpretations given. "New internal models make a permanent slope change look more plausible than a one-time jump at Mythos Preview." Model 4 is above 50% on all 15 of its benchmarks; AECI 178.6 (179.7 without 3 suspect benchmarks).
- #interview-quotes: Claude-coded tally of 11 interviewees on ">2x acceleration in their area of work": Yes 2, Leans yes 3, Borderline/unclear 4, Leans no 0, No 2. "each interviewee often interpreted the question in somewhat different ways, e.g. whether they are referring to cumulative or instantaneous speedup".
- #adversarial-robustness: "Claude was deeply involved in … the majority of our own analysis." METR detected no systematic bias. This bears on the paper's own disclosure.
- #process-transparency-disclosures, "Other disclosures": "We made significant clarity edits, particularly to the Risk Report Review, in response to feedback … In some cases we felt this feedback toward METR staff was overly forceful". METR says the final review is not "significantly distorted by this". COI: one team member had discussions with Anthropic about a role, received an offer and declined it, and also held equity in a competitor. That member's work was checked by an unconflicted colleague.

### S6. METR, Summary of METR's predeployment evaluation of Claude Opus 5.5

```text
URL:         https://metr.org/blog/2026-09-22-claude-opus-5-5/
Kind:        Primary for METR's September statements. The independence note says Anthropic "had the
             opportunity to review and edit the text", and the same text appears in the Opus 5.5 system
             card §2.3.6 (S7).
Establishes: METR's earlier estimate, before the full assessment.
Locators:    "Summary of evidence" (fourth bullet); "Conclusions" part (B).
```

- Summary of evidence: one input was "A highly experimental and preliminary report from a separate METR assessment of AI R&D acceleration inside Anthropic", whose team "shared its conclusions with us, but was not able to share the supporting evidence".
- Conclusions (B): "The estimate provided by the preliminary AI R&D report is '~1.5X overall acceleration in capabilities due to AI (i.e. 1.5 years in 1 year), with perhaps 30% chance of 2X acceleration.'" "because the preliminary report did not specify the time period for this estimate, it is unclear whether this estimate applies to the development of Claude Opus 5.5 or another period." It also says the work "was not meant to verify claims about compliance with any specific threshold". This gives METR's own estimate on two dates: about 1.5x in September, about 2x in November.

### S7. Anthropic, Claude Opus 5.5 System Card (September 22, 2026)

```text
URL:         https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf
Kind:        Primary. Anthropic's threshold determination and AECI fit for that release.
Establishes: Anthropic's public AECI slope ratio as of 22 September; its threshold reasoning after the Risk Report.
Locators:    §2.3.1.1 p.34; §2.3.2 p.34–35; §2.3.5.3 Table 2.3.5.3.A p.39; Figure 2.3.5.3.B p.40; text p.40–41.
```

- p.34, §2.3.1.1: "Autonomy threat model 2 is not applicable to Claude Opus 5.5". Grounds: "(1) we do not observe a sustained AI-attributable 2× acceleration in the pace of our overall AI progress". It also notes "we've seen acceleration to one or more highly relevant internal metrics".
- p.35, §2.3.2: "our internal measures of AI-driven research acceleration … which are only partially published, do not show a sustained AI-attributable 2× acceleration … though some of these measures have moved".
- p.40, Figure 2.3.5.3.B legend: "Frontier trend 14.7/yr, fitted +5.9 jump at Claude Mythos Preview"; "Frontier trend 14.4/yr, fitted breakpoint at Sep 2025 → 22.2/yr". Caption: "The one-time jump model is a better fit to the data in 99 of 100 resampled fits."
- p.41: the trend-break hypothesis gives "a slope change from 14.4 to 22.2 points per year, with the fitted break in September 2025 and a 1.53x increase (95% range 1.20 to 1.82). The first hypothesis fits the data better, but under either reading the slope has not doubled."
- p.39: "AECI values from this fit are not comparable to the AECI values in earlier system cards" (each refit re-estimates the scale). Opus 5.5 AECI 169.36 on this fit.

### S8. Anthropic, Claude Haiku 5.5 System Card (October 7, 2026)

```text
URL:         https://assets.claude.com/e1080d6bf5ae2018ea3c2f414064be03232f5be5.pdf  (linked from S5)
Kind:        Primary.
Establishes: Anthropic's public AECI slope ratio as of 7 October.
Locators:    §2.3.2, Figure 2.3.2.A p.20 (legend). The 1.70x appears only in the figure legend, not in body text.
```

- p.20, figure legend (read from the rendered figure): "Frontier trend 16.2/yr, fitted +7.3 jump at Claude Mythos Preview"; "Frontier trend 15.3/yr, fitted breakpoint at Sep 2025 → 26.1/yr (1.70× slope change)". Body text: Opus 5.5 scores 174.56 on this fit, against 169.36 on the 22 September fit, which shows the scale shifts between refits. §2.3.3 carries forward the Opus 5.5 not-crossed determination.

### S9. Anthropic, PBC, Form S-1/A (filed 2 November 2026) and Form S-1 (filed 26 October 2026)

```text
URL:         https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm  (S-1/A)
             https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm  (S-1)
Kind:        Primary. Anthropic's securities filings (CIK 0002130357), made under legal liability.
Establishes: Anthropic's latest public statement on the threshold, made after the Risk Report and before METR's publication.
Locators:    Risk Factors > "Risks Related to our Business and Industry" > risk factor beginning "Our success
             depends in large part on our ability to continue to develop the most advanced and capable AI
             models"; paragraph beginning "In addition, our increasing use of AI systems…", S-1/A p.30.
```

- S-1/A quote (this wording is evidence): "Much of our evidence regarding the pace of such AI-driven acceleration is derived from lagging indicators … As a result, we have in the past not identified, and may in the future not identify, a significant acceleration in our rate of development until after it has occurred. For example, our internal estimates and our expectations regarding future models, rather than our current models, indicate that we may imminently meet our Responsible Scaling Policy's definition of 'dramatically accelerated progress attributable to AI.' We have not designated any of our current models as exceeding this threshold, and we continue to assess the underlying data."
- S-1 (26 October) had only: "we may not identify a significant acceleration in our rate of development until after it has occurred." The amendment added "have in the past not identified" and the "may imminently meet" sentence.
- Note: the quoted phrase "dramatically accelerated progress attributable to AI" does not appear verbatim in RSP v3.4 (S3 says "dramatic acceleration").

### S10. Anthropic, "An update on independent evaluators" (October 15, 2026)

```text
URL:         https://www.anthropic.com/news/an-update-on-independent-evaluators
Kind:        Primary. Anthropic's account of its arrangements with METR.
Establishes: The October "employee-like access" arrangement is a different engagement from S1/S5.
Locators:    Opening paragraphs; "What we mean by 'employee-like access'"; footnote 2 (updated October 16).
```

- Six METR employees were onboarded with "employee-like access". "Anthropic can't veto publication, but we can require them to redact information if it falls into predefined categories". S5 says its engagement "is distinct from the assessment announced on October 15", so the S1/S5 findings come from the earlier, narrower engagement.

### S11. Anthropic, "Measurements for understanding the pace of AI development inside frontier labs"

```text
URL:         https://www.anthropic.com/institute/measuring-pace-of-ai-development
Kind:        Primary. Anthropic's own metrics. No publication date appears in the page text I extracted.
Establishes: A different measure of AI's role in AI R&D (share of work automated), not a rate of progress.
Locators:    Section "(1) Measuring AI-led AI R&D", "What we found"; Appendix "Measuring AI-led R&D".
```

- "As of August 2026, Claude is not operating fully autonomously for any measured subset of AI R&D work. Claude 'leads' 26% of Anthropic's AI R&D work. The share of work at or above 'AI collaborates' is above 90%." Built from a July 2026 task tree rated by a Claude judge. It is useful only to show what the acceleration estimates are not: a share of work is not a rate of progress.

## Contradictions

1. **Public "less than a factor of 2" against private 1.97.** S2 p.103 says the leading indicators show acceleration "by less than a factor of 2". METR (S1, Claim 1) computes 1.97 from the private report's figures. Caveats an editor will test: the 1.97 is METR's arithmetic and does not appear in the private report. It pairs the private report's current rate with a historical rate "elsewhere in the private report", and it is not stated whether that is the RSP's "fastest rate of extended progress". It measures a redacted leading indicator, not AI aggregate capabilities. The private sentence assumes all the speedup is due to AI.

2. **Attribution test: RSP against public report.** RSP v3.4 (S3 p.9) requires (a) a doubling and (b) that "it is plausible that this doubling is substantially attributable" to automation. The public report's conclusion (S2 p.103) tests against "a doubling … attributable primarily to AI R&D automation". "Plausibly substantially" is a lower bar than "primarily". S2 p.103 also says Anthropic is "fairly confident" the 2025 acceleration came from non-AI factors. Under the RSP's (b), a plausible AI attribution would be enough. METR's Claim 2 makes a related point: the private report calls an AI-attributable factor above 2 "plausible". METR does not mention the "primarily" wording.

3. **Counterfactual speedup is not the threshold quantity.** The private report's "slightly less than twice as fast as it would be without AI assistance" (S1 Claim 2), the public "not yet by a factor of 2" (S2 p.11), and the interview evidence (S5) are counterfactual ratios. The RSP v3.4 changelog (S3 p.19–20) says a large counterfactual speedup with a constant or slowing observed rate would not cross the threshold. Condition (a) is about the observed rate against the historical baseline. Counterfactual evidence bears on condition (b).

4. **One-time jump against permanent slope change.** Anthropic (S2 p.103; S7 p.40–41) prefers a one-time jump at Mythos Preview, which wins in 99 of 100 resampled fits on its 22 September fit. METR (S5 #benchmark-scores-aeci, figure "jump-vs-slope-change") reports that a fit through Mythos 5 that is held out on later models gives RMSE 1.9 for the slope change against 3.9 for the jump, with the slope change lower "in 81% of bootstrap draws". The difference is mainly the internal Models 2 to 4, which Anthropic's public cards do not plot.

5. **Anthropic's own public AECI ratio moved.** S7 (22 Sep): 1.53x (1.20–1.82), breakpoint Sep 2025. S8 (7 Oct): 1.70x on a refit (15.3 to 26.1/yr). Both cards conclude not crossed. METR's re-fits of the card scores on its 7 Oct 2025 breakpoint give 1.65x to 1.76x (S5 figure "estimate-comparison-grid"), so METR's numbers for the cards differ slightly from the cards' own headline figures.

6. **Same number, different estimate: two "1.9x" figures.** S1 Claim 3's 1.9x is the Risk Report's model set (through the July coverage date) re-estimated with more benchmarks. S5's 1.9x [1.5–2.8] adds the internal Models 2 to 4, with data through October 2026 and a breakpoint of 7 October 2025. A chart must not merge them.

7. **Leading indicators against AECI in Anthropic's own account.** S2 p.103 dates "meaningful acceleration" to "early-to-mid 2025" from the leading indicators. The AECI breakpoints are Sep 2025 (S7, S8) and 7 Oct 2025 (S5). Leading indicators are supposed to precede AECI (S2 p.102), so this ordering is consistent and not a conflict, but the windows differ.

8. **Opus 5.5 card tone against the Risk Report.** S7 p.34 says "we've seen acceleration to one or more highly relevant internal metrics". S2 says "early signs of (potential) acceleration". The S-1/A (S9) goes further, with "may imminently meet" for future models. None of these says the threshold was crossed for any current model.

9. **"Early warning" label.** The commission calls 2x the "early-warning threshold". The RSP text gives it no name and no "early warning" label. That framing is in the Risk Report p.101 ("functions as a potential early warning") and in METR's review. "2x Acceleration Threshold" and "Full Substitution Threshold" are METR's coinages (S1).

10. **Where METR agrees with Anthropic.** Catastrophic risk on July 15 was low (S1 exec summary and "Despite this…"). The Full Substitution argument is "broadly compelling" (S1). Researchers at both organizations lean toward not crossed (S1).

I searched for a public Anthropic response to the 5 November METR publications (Anthropic newsroom pages linked from S5, web search, and the TechTimes and The Decoder coverage) and found none. TechTimes's "Anthropic declined to comment" refers to a Reuters question about its IPO timing, not to METR.

## Numbers

The threshold:

```text
Figure: 2x = "as much progress in one year as one would see in two years at baseline"
Owner:  RSP v3.4 fn 8, p.9 (S3); repeated Risk Report fn 4, p.13 (S2)
Scope:  AI aggregate capabilities, against both the expected rate and the fastest extended rate (≥3 model
        generations) without significant AI contributions; plus plausible substantial attribution to automation
```

```text
Figure: baseline 3x compute × 3x algorithmic efficiency = 9x effective scaleup per year; doubling ≈ 81x per year
Owner:  RSP v3.4 fn 8 (S3) ("something like an 81× effective scaleup")
Scope:  illustrative; 81 = 9², i.e. two baseline years compounded into one
```

```text
Figure: in linear index points: 15 points/yr → 30 points/yr = acceleration 2; in multiplicative terms 3x/yr → 9x/yr, ln9/ln3 = 2
Owner:  METR (S5 #key-findings, "Terminology")
Scope:  METR's definition: acceleration = ratio of growth rates
```

```text
Figure: decision-relevant extreme: 10³–10¹⁰× effective scaleup within a year
Owner:  Risk Report §3.5 p.101 (S2)
Scope:  Anthropic's description of super-exponential progress, against which 2x is an early warning
```

Estimates. Each line gives what it measures, its input, and its period.

```text
Figure: 1.97 (acceleration rate)
Owner:  METR's calculation (S1 Claim 1) from the private Risk Report's figures
Scope:  one redacted leading indicator; current rate "[redacted]×/yr" over a historical rate from elsewhere in the
        private report; assumes all speedup due to AI; as of the July 15, 2026 coverage date. Upper bound on AI attribution.
```

```text
Figure: 1.3 to 2.8 (range of "reasonable estimates")
Owner:  METR (S1 Claim 1); the analysis itself is redacted
Scope:  Anthropic's internal leading indicators; varies "depending on the definition and time period"; neither the
        definitions nor the periods are public
```

```text
Figure: "less than a factor of 2"
Owner:  Anthropic, public Risk Report §3.5.2 p.103 (S2)
Scope:  leading indicators, acceleration "starting in early-to-mid 2025", to July 15, 2026
```

```text
Figure: "significantly faster … but not yet by a factor of 2"
Owner:  Anthropic, public Risk Report Table 1.2.B p.11 (S2)
Scope:  counterfactual: internal AI R&D with vs without AI assistance; as of July 15, 2026
```

```text
Figure: "slightly less than twice as fast as it would be without AI assistance"; "plausible we do exceed this factor of 2"
Owner:  Anthropic private Risk Report, as quoted by METR (S1 Claim 2)
Scope:  counterfactual end-to-end growth in [redacted]; as of July 15, 2026; METR says based on interviews with
        research leads and informal surveys
```

```text
Figure: ≈1.5x (AECI acceleration)
Owner:  METR re-estimate (S1 Claim 3)
Scope:  AECI, using the data used in the Risk Report (models through the July 15 coverage date)
```

```text
Figure: 1.9x (AECI acceleration)
Owner:  METR, using benchmark data Anthropic added after publication (S1 Claim 3)
Scope:  same set of models as the Risk Report, more benchmarks
```

```text
Figure: 1.53x (95% range 1.20–1.82); 14.4 → 22.2 AECI points/yr
Owner:  Anthropic, Opus 5.5 System Card p.41 and Fig 2.3.5.3.B p.40 (S7)
Scope:  public Anthropic frontier models, trend-break fit with breakpoint Sep 2025; fit of September 18, 2026;
        Anthropic prefers the one-time-jump fit (+5.9 points at Mythos Preview)
```

```text
Figure: 1.70× slope change; 15.3 → 26.1 AECI points/yr
Owner:  Anthropic, Haiku 5.5 System Card Fig 2.3.2.A p.20 (S8)
Scope:  public Anthropic models, refit, breakpoint Sep 2025; card dated October 7, 2026
```

```text
Figure: 1.9x [95% CI 1.5–2.8]; ≈15 → ≈29 AECI points/yr
Owner:  METR (S5 #key-findings; chart "aeci-main.png" labels "+15/yr" and "+29/yr")
Scope:  Anthropic public and internal models (incl. Models 2–4), dated by availability to most Anthropic
        employees; breakpoint October 7, 2025; through October 2026
```

```text
Figure: 1.1x to 2.9x (robustness range); 1.4x with all developers' frontier models (≈17 → ≈24/yr per the grid)
Owner:  METR (S5 #benchmark-scores-aeci)
Scope:  AECI link-function and model-set variations; same period as above
```

```text
Figure: "around twice the rate"; would not be surprised by 1.3x or 3x; ≈80% of current acceleration due to AI
Owner:  METR subjective conclusion (S5 #our-conclusions-on-risk)
Scope:  capabilities on "well-specified tasks", October 2026 vs March 2024–October 2025; all evidence incl. redacted
```

```text
Figure: "~1.5X overall acceleration in capabilities due to AI … perhaps 30% chance of 2X"
Owner:  METR preliminary report, quoted in METR's Opus 5.5 summary (S6)
Scope:  counterfactual ("due to AI"); time period unspecified per METR; published September 22, 2026
```

```text
Figure: interview tally on ">2x acceleration from Claude": Yes 2, Leans yes 3, Borderline/unclear 4, Leans no 0, No 2
Owner:  METR (S5 #evidence-of-ai-speedup, #interview-quotes)
Scope:  11 researchers, mix of cumulative/instantaneous and personal/org-wide readings; Claude-coded
```

Not acceleration rates. Do not plot these on the same axis as the estimates above.

```text
Figure: geometric mean self-reported uplift ≈4× (1 of 18 saw a drop-in entry-level replacement)
Owner:  Anthropic, Risk Report §3.4.2 p.99 (S2)
Scope:  staff survey for Claude Mythos Preview; individual productivity, not rate of progress
```

```text
Figure: ≈12x average self-reported uplift
Owner:  METR reporting Anthropic Slack polls (S5)
Scope:  most capable internal model, October 2026; "very loose evidence"
```

```text
Figure: 26% of AI R&D work "AI leads"; >90% at or above "AI collaborates"; 0% fully autonomous
Owner:  Anthropic (S11)
Scope:  task basket from July 2026, rated as of August 2026; share of work, not rate
```

Series for a chart (Anthropic's public estimate of the AECI slope ratio over time, from its own documents):

```text
Aug 14 2026  Risk Report (data to Jul 15): one-time jump preferred; no ratio published; 13.5 AECI/yr pre-trend (Fig 3.5.A)
Sep 22 2026  Opus 5.5 card: 1.53x (1.20–1.82)
Oct 7  2026  Haiku 5.5 card: 1.70x
```

METR's estimates over time:

```text
Sep 22 2026  ~1.5x due to AI, ~30% chance of 2x (S6; preliminary, period unspecified)
Nov 5  2026  ~2x (1.3x–3x) overall; AECI 1.9x [1.5–2.8]; leading indicators 1.3–2.8; 1.97 implied at Jul 15 (S1, S5)
```

## Limits

- Leading indicators: their nature, units and trends are redacted (S2 p.102; S1). Nobody outside can establish what the 1.97 or the 1.3 to 2.8 measures, beyond "metrics … predictive of later trends in AECI".
- I could not establish whether the historical rate behind the 1.97 is the RSP's "fastest rate of extended progress … over at least three model generations" or some other baseline. METR says only "an estimate of the historical rate of progress elsewhere in the private report".
- The definitions and periods behind METR's 1.3 to 2.8 range are redacted (S1).
- The private Risk Report is visible only through METR's quotes. I could not check those quotes against the document.
- Anthropic response: I found no public statement from Anthropic responding to METR's 5 November review or assessment. The closest is the S-1/A of 2 November.
- Plotting on one axis: the estimates are all dimensionless ratios, but they are ratios of four different things. (i) Observed growth-rate ratios of AECI, which is the RSP's "aggregate capabilities" quantity. (ii) Growth-rate ratios of undisclosed internal leading indicators. (iii) Counterfactual with-AI versus without-AI ratios. (iv) METR's subjective all-evidence judgment. Only (i) is directly comparable to the RSP's condition (a). They can share an axis only if each is drawn in a labeled lane by quantity and dated, with the 2x line drawn across all lanes and a note that the line means condition (a) only for lane (i). Self-reported uplift (4x, 12x) and the 26% automation share should stay off it.
- The AECI scale is refit between documents (S7 p.39), so absolute AECI scores (161.88, 169.36, 174.56, 178.6) are not comparable across S2, S7, S8 and S5. Slope ratios are the comparable figure.
- The RSP does not say how "we've observed" is scoped: Anthropic's models only, or the industry frontier. That matters for METR's 1.4x all-developer reading (the industry's historical slope was steeper).
- I did not read METR's May 2026 review of the February Risk Report or METR's 14 October proposal post. Neither was needed to confirm the commission's figures.

## Source assets

```text
Asset: METR chart "As of October 2026, benchmark scores appear to be growing at 1.9× their pre-October 2025 rate"
       — https://metr.org/assets/images/ai-rd-acceleration-assessment/aeci-main.png, S5 #key-findings
Shows: AECI by model, 2024–Oct 2026; grey +15/yr trend, black +29/yr after Oct 2025; internal models (orange) incl. Models 2–4
Crop:  keep title (with CI), both slope labels, the internal/public legend and the Model 2–4 labels; the headline
       numbers sit in the title, so a crop that drops it loses the 1.5–2.8 interval
```

```text
Asset: METR chart "Fit only through Mythos 5, a permanent acceleration predicts the later models better than a one-time jump"
       — https://metr.org/assets/images/ai-rd-acceleration-assessment/jump-vs-slope-change.png, S5 #benchmark-scores-aeci
Shows: Anthropic's one-time-jump hypothesis (labeled "[Anthropic August Risk Report hypothesis]") against a slope change,
       tested on held-out later models; RMSE 1.9 vs 3.9; 81% of bootstrap draws
Crop:  keep the shaded "held out of fit" region, both fit lines and the footer legend with RMSEs and the 81% line
```

```text
Asset: METR grid "Vary methodology that estimates trends over time" / "Vary methodology that calibrates model scores"
       — https://metr.org/assets/images/ai-rd-acceleration-assessment/estimate-comparison-grid.png, S5 #benchmark-scores-aeci
Shows: the same data giving 0.99x to 1.90x depending on model set, dating and calibration; includes METR's re-fits of the
       Haiku 5.5 (1.76x/1.73x) and Opus 5.5 (1.68x/1.65x) card scores
Crop:  the full grid is too tall for a phone; the top row (1.90, 1.74, 1.71, 1.09, 1.39) with column headers carries the
       point. Keep the footnote's breakpoint date (October 7, 2025) in the caption
```

```text
Asset: METR sketch "We guess most of the current acceleration in AECI is due to AI"
       — https://metr.org/assets/images/ai-rd-acceleration-assessment/attribution-sketch.png, S5 #our-conclusions-on-risk
Shows: historical trend, observed AECI with AI, and best-guess AECI without AI; the three growth rates that separate
       observed acceleration from counterfactual attribution
Crop:  must keep "Illustrative sketch, not real data" and the "FAKE DATA" watermark; it is a mechanism diagram, not evidence
```

```text
Asset: Risk Report Figure 3.5.A "Anthropic ECI over time", p.102 (S2)
Shows: what the public report showed: trend through Opus 4.6 at 13.5 AECI/yr, Mythos Preview and Mythos 5 above it, no Model 2
Crop:  keep the legend line with 13.5 AECI/yr and the Mythos labels; omit the paragraph text above
```

```text
Asset: Opus 5.5 System Card Figure 2.3.5.3.B, p.40 (S7), and Haiku 5.5 System Card Figure 2.3.2.A, p.20 (S8)
Shows: Anthropic's two competing fits with their slope figures in the legend (14.4 → 22.2/yr; 15.3 → 26.1/yr, "1.70× slope change")
Crop:  keep the two-line legend; the 1.70× exists only in the Haiku legend
```

```text
Asset: RSP v3.4 threshold table row and fn 8, p.9 (S3)
Shows: the operative definition and the 81x example
Crop:  text, not a visual; better quoted than captured
```

S1 (METR review): None found. The page is text with two-column public/private quote boxes. The quote boxes under Claim 1 could be captured, but quoting works as well.
S6, S9, S10, S11: None found for this argument.

## Discarded

```text
https://the-decoder.com/metr-finds-anthropic-may-have-crossed-its-own-ai-acceleration-warning-threshold-back-in-july/: secondary; every figure (15→29/yr, 80%, 1.97, 1.3–3) traced to S1/S5; adds only an unquoted reference to a Daniel Kokotajlo post on X, which I did not open
https://www.techtimes.com/articles/330164/20261106/anthropic-ai-acceleration-hits-19x-benchmarks-metr-calls-anthropic-threshold-defense-overstated.htm: secondary; used only as a lead to the S-1/A and the Opus 5.5 card's 1.53x, both verified in the primaries; its "Anthropic declined to comment" concerns IPO timing, not METR
```

## Questions for the orchestrator

1. The commission's one idea treats 1.97 as "the public report's 'less than 2x' … within a few hundredths of the line". That is true of one redacted leading indicator, by METR's arithmetic, under a full-attribution assumption. It is not true of the RSP's own quantity (AECI, aggregate capabilities), where Anthropic's published figures were 1.53x and 1.70x. Provisional decision: keep 1.97 as the opening finding, but always attribute it to METR, call it a leading indicator, and set it against the AECI lane.
2. Provisional decision on the range plot: lanes by measured quantity (AECI slope ratio, leading indicator, counterfactual speedup, METR overall judgment), each point dated, the 2x line across all lanes, and self-reported uplift excluded. Please confirm or overrule.
3. The S-1/A (2 November) is new primary material outside the commission. It contains Anthropic's own "may imminently meet" for future models and "have in the past not identified". Provisional: offer it to the writer as Anthropic's most recent public position, quoted exactly and scoped to future models.
4. The "attributable primarily" (public report) versus "plausible … substantially attributable" (RSP) difference is my finding, not METR's. Provisional: offer it to the writer, attributed to the documents with page locators and not presented as METR's critique.
5. Disclosure: METR states Claude did "the majority of our own analysis" (S5 #adversarial-robustness). The writer may want this next to the paper's own Claude disclosure.
