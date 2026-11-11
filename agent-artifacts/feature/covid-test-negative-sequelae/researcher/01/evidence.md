# Evidence: feature/covid-test-negative-sequelae (researcher 01)

The PNAS paper is open access (CC BY) and I read it in full from the PMC/Europe
PMC copy, along with its 429-page SI appendix. Every count in the commission's
story matches the paper: 43/5/0 attributable outcomes under the test-based
design and 262/286/369 under the unrestricted design. Three facts in the
commission need correcting. (1) The paper was published online on **27 October
2026** (issue of 3 November 2026, vol. 123 no. 44), not about 10 November.
CIDRAP's report is dated 9 November. (2) The windows are defined in days
(30–119, 120–359, 360–719 after enrollment). The paper glosses them as 1–4,
5–12 and 13–24 months. (3) The two designs do not differ only in the control
group. The unrestricted design's cases are everyone with a COVID diagnosis code
(10.1 million), while the test-based design's cases are people whose first PCR
test claim was followed by a COVID diagnosis within 7 days (2.8 million).
Claims carry no lab results, so "positive" and "negative" are inferred from
diagnosis codes. The angle's mechanism is well supported by the paper's own
placebo-case experiment (negative-tested people versus untested people). The
counterpoint is well supported too: the authors' own figures say 20.2% of
test-negative controls later tested positive within two years, and 2 of 49
negative-control outcomes ran below 1. Al-Aly's 2023 objection that
test-negative controls are "people who are sick" is on the record. The evidence
is thinner in four places. No independent expert has publicly commented on this
paper that I could find. The paper's "unrestricted control" analysis is the
authors' re-implementation in Komodo claims, not a reanalysis of the VA cohorts,
and the VA papers themselves report null negative-outcome controls (neoplasms,
accidental injuries), which the Komodo re-implementation did not reproduce.
Two test-negative or test-anchored studies (Mizrahi et al., BMJ 2023; RECOVER,
JAMA 2023) still find several effects at 6–12 months. Claims data also under-record
fatigue and cognitive symptoms. The evidence supports "most of the late-window
signal in an unrestricted design run on these claims is a comparison-group
artifact". It does not support a claim that a fixed share of the VA studies'
published findings is an artifact.

## Sources

### 1. The PNAS paper (full text)

```text
URL:         https://doi.org/10.1073/pnas.2604414123 (publisher page https://www.pnas.org/doi/10.1073/pnas.2604414123 returns 403 to automated fetch; open-access copy read at https://pmc.ncbi.nlm.nih.gov/articles/PMC13732191/, via the Europe PMC full-text XML)
Kind:        primary. The authors own the design, data processing, counts and conclusions.
Establishes: firsthand: cohort construction, the counts per window per design, negative-control results, placebo-case (negative control exposure) results, limitations, conclusion.
Paraphrase:  Title "Revised estimates of types and duration of long COVID symptoms based on claims records from 245 million US patients". Authors: Hamed Nilforoshan, Julia Reisler, Erfan Jahanparast (equal contribution), Michael Moor, Steven N. Goodman, Stefan Wager, Jure Leskovec. Affiliations as printed: Nilforoshan, Reisler, Moor, Leskovec, Department of Computer Science, Stanford University; Jahanparast, Department of Computer Science, University of California, Berkeley; Moor also Department of Biosystems Science and Engineering, ETH Zurich; Goodman, Department of Epidemiology and Population Health, Stanford University (corresponding author); Wager, Stanford Graduate School of Business. Edited by Elizabeth A. Stuart, Johns Hopkins University (guest editor). Received 11 Feb 2026; accepted 9 Sep 2026; published online 27 Oct 2026; issue date 3 Nov 2026 (PNAS 123(44): e2604414123). Licence CC BY 4.0. Authors declare no competing interest. Funding includes NSF, Stanford HAI, Chan Zuckerberg Initiative, Amazon, Genentech, GSK, Hitachi, SAP, UCB (Acknowledgments).
             Data: de-identified US insurance claims from Komodo Health, two extracts totalling 14.4 billion claims from 244.7 million patients. A "Pandemic" extract holds patients with any COVID-related activity. A "Control" extract is a random sample of patients with no recorded COVID-19 diagnosis, which "may include individuals who received COVID-19 testing and/or vaccination". Observation ended 4 April 2023. Restricted to people with at least one claim in 2019 (Methods M1).
             Designs (Methods M2): enrollment window 1 March 2020 to 1 March 2021; follow-up for post-acute outcomes starts 30 days after enrollment; all must be alive at day 30.
             (a) Unrestricted control: cases = first confirmed COVID diagnosis (ICD-10 U07.1, or B97.29 before 1 April 2020); controls = Control-extract patients with no COVID diagnosis, assigned enrollment dates drawn from the cases' dates. Designed "to closely follow Al-Aly et al." (ref 10), with ZIP-3 rather than residential address (Discussion).
             (b) Test-based control (primary): enrolled at first PCR test claim; cases = COVID diagnosis within 7 days of that test; controls = no COVID evidence within 7 days; controls down-sampled 5:1 per enrollment day.
             (c) Placebo-case unrestricted design: "cases" = people whose first PCR test was negative and who had no COVID evidence before or after; controls from the Control extract.
             All controls reweighted by a synthetic-control method to match cases on 4 years of pre-enrollment history across all 614 outcomes, healthcare utilization, and demographics (Methods M3).
             Threshold for an "attributable" outcome: RR ≥ 1.1 and P < 0.05 after Bonferroni correction within each window (Results; Fig. 1 legend).
Locators:    Abstract; Significance; Results ("Number and Duration…", "Comparing False Attribution Rates…", "Characterizing Long COVID Symptoms…", "Biases Due to Selective COVID-19 Testing", "Study Design Validation"); Discussion; Methods M1–M3; Fig. 1–4.
Quote:       Abstract: "Across 614 clinical outcomes followed over 2 y, the test-based design resulted in 83.5% fewer symptoms being attributable to COVID-19 between 30 to 119 d after infection (43 attributable symptoms vs. 262 for the unrestricted control design), a 98.2% reduction at 120 to 359 d (5 vs. 286), and a 100% reduction at 360 to 719 d (0 vs. 369)."
Quote:       Abstract (closing sentences): "The test-based control design may modestly underestimate some effects. This study does not indicate that symptoms beyond one year are not genuine but that their attributability to COVID-19 is uncertain."
Quote:       Discussion (conclusion sentence): "This analysis suggests that while long COVID remains a serious concern, it may have fewer symptoms—and ones of shorter duration and lower overall severity—than previously thought."
Quote:       Discussion, final paragraph: "We investigated in depth and demonstrated the degree to which large-scale studies using unrestricted control designs have likely substantially overestimated the number and duration of long COVID symptoms."
Quote:       Results, late window: "This is not to diminish the reality of such symptoms; rather, it suggests that they are unlikely to be specific to COVID-19. These symptoms may be due to a non-COVID condition that led to the initial hospital visit or COVID-19 testing, or some other factor. Ultimately, their cause is not discernible with the methods used here."
```

Stated limitations (Discussion, paragraphs beginning "Our approach, while a
substantial improvement…" through "Relative risks near 1.0…"):

- Claims are billing records and may lack clinical accuracy and granularity.
- At-home tests are invisible unless the person presented to the health system.
- The test-based design "narrows the target population". It estimates effects
  only for people who sought healthcare and a PCR test.
- Patients are linked by a hash of name, sex and date of birth, so
  misidentification is possible (robustness check in SI Fig. S8, Pearson 0.99).
- Possible mild negative bias: "two of 49 negative control outcomes were
  significantly reduced in the test-positive individuals. This is likely due to
  conditioning on testing, which may lead to collider bias." Test-negative
  people may have come in for other ailments (cancer is the example) or for a
  non-COVID respiratory illness that "could produce a nonspecific prolonged
  viral syndrome".
- Unmeasured differences between test-positive and test-negative people cannot
  be adjusted for.
- Survivor selection: 1.2% of test-positives versus 0.62% of test-negatives died
  within 30 days, a "potentially" downward bias that the authors call "very
  small" in this cohort.
- Later infection among controls: 0.6–1.1% of controls tested positive in any
  30-day period. 4.2% had tested positive within 119 days, 10.1% within 359 days
  and 20.2% within 2 years, "again resulting in conservative effect estimates".
- The RR ≥ 1.1 threshold means "there may be undetected small effects".

### 2. PNAS SI Appendix (Appendix 01, 429 pages)

```text
URL:         https://pmc.ncbi.nlm.nih.gov/articles/PMC13732191/ (Supplementary Materials, "Appendix 01 (PDF)", file pnas.2604414123.sapp.pdf; obtained via the Europe PMC supplementaryFiles service)
Kind:        primary. Same authors, same analysis.
Establishes: firsthand: cohort sizes and attrition, the fact that positivity is inferred from diagnosis codes, per-window shares of outcomes with RR ≥ 1.1, the placebo-case correlation, the later-positive curve for controls.
Paraphrase:  Extended Methods S2: cohort attrition for all three designs (numbers in Numbers below). PCR test identified by CPT/HCPCS codes; "COVID-19 cases are defined as those who received a positive test result subsequent to testing, that is, they were diagnosed with COVID-19 within 7 days of testing". 614 outcomes = 565 plausibly caused by COVID + 49 negative controls, filtered from 695 (Extended Methods S1.2), mostly from CCSR categories.
             Tables S1–S2: before weighting, unrestricted controls had fewer visits than cases (total visits per patient 31.56 vs 54.0; ER 0.8 vs 1.56). Test-negative controls were close to cases even unweighted (47.92 vs 46.53; ER 1.23 vs 1.25). After weighting, both designs match on visit history.
             Fig. S1: adult cerebral palsy. Cases in the unrestricted design show rising cerebral palsy claims before their COVID diagnosis, while unrestricted controls stay flat. Test-negative controls show the same pre-test rise as cases.
             Fig. S2: placebo-case RRs correlate with unrestricted-design COVID RRs (Spearman 0.48) across 614 outcomes at days 30–120. In the test-based design the correlation is −0.22.
             Fig. S5: share of the 614 outcomes with RR ≥ 1.1 (no significance filter stated in the legend). Unrestricted: 82.7%, 77.5%, 85.0%. Placebo-case unrestricted: 82.5%, 66.6%, 54.8%. Test-based: 8.8%, 2.3%, 1.6% (days 30–120, 120–360, 360–720).
             Fig. S7: cumulative share of test-negative controls who later test positive (4.2% / 10.1% / 20.2%).
             Figs. S15–S80: per-system RR panels for every outcome, design and window (images; per-outcome numbers are not tabulated in text).
Locators:    SI pp. 3–4 (Extended Methods S1–S2); Tables S1–S3 (pp. 11–13); Fig. S1, S2, S5, S6, S7 (pp. ~7–20); Figs. S15–S80 (per-system).
```

### 3. Stanford University news release (via EurekAlert!)

```text
URL:         https://news.stanford.edu/stories/2026/10/long-covid-health-affects-study-design (Stanford Report; 403 to automated fetch). Read via the EurekAlert! copy https://www.eurekalert.org/news-releases/1149648 (release dated 28 Oct 2026), corroborated by the healthcare-in-europe.com reprint (source line credits Stanford University).
Kind:        primary for the authors' own public statements (Stanford is the authoring institution). Secondary for the study's facts, which the paper owns.
Establishes: authors' quotes and titles as Stanford gives them. The release's "98 percent fewer" figure repeats the paper's 98.2% (days 120–359).
Paraphrase:  The issuer is Stanford University's news office (Stanford Report), not a Stanford Medicine release. Titles as the release gives them: Jure Leskovec, "Alfred and Rebecca Lin Professor" in the School of Engineering (co-senior author). Stefan Wager, associate professor of operations, information, and technology, Stanford GSB (co-senior author). Hamed Nilforoshan, doctoral student in computer science (first author). Steven Goodman, professor of epidemiology and population health, Stanford School of Medicine. The release says insurance records may miss fatigue and cognitive symptoms that go undiagnosed or uncoded.
Locators:    Body paragraphs. I read the release through a summarizing fetch, not raw HTML, so check exact quote wording against the page before printing it.
Quote:       Leskovec: "This doesn't mean long COVID is 98% less common." / "Even with 244 million patients, you can get highly precise answers to the wrong question." / "If you compare people who tested positive for COVID with people who were never tested, you risk attributing differences in their underlying health and healthcare-seeking behavior to the virus itself."
Quote:       Goodman: "These findings indicate that long COVID may be more similar to other extended post-viral syndromes than many have thought."
```

### 4. CIDRAP News on the PNAS paper

```text
URL:         https://www.cidrap.umn.edu/covid-19/new-study-links-covid-fewer-long-term-health-problems
Kind:        secondary. CIDRAP (University of Minnesota) reports on the paper from outside.
Establishes: only that the paper was covered and how. Its counts (43/262, 5/286, 0/369) match the paper. Quotes only the study team, with no outside expert.
Paraphrase:  By Laine Bergeson; datePublished 2026-11-09. Uses the month glosses (1–4, 5–12, 13–24 months). Lists the organ systems in the early window. Two imprecisions: it says the claims cover "the first four months after they tested", but follow-up ran to 2 years. It also says people tested while seeking care for other illnesses were "included in the comparison groups", but in the paper's mechanism those people are among the cases, not the comparison group.
Locators:    Paragraphs 2–8.
```

### 5. Al-Aly, Xie, Bowe, Nature 2021 (VA, 6 months)

```text
URL:         https://www.nature.com/articles/s41586-021-03553-9 (doi 10.1038/s41586-021-03553-9)
Kind:        primary for its own design and results. It is the study the PNAS unrestricted design was modelled on.
Establishes: VA control-group definition, its negative-outcome and negative-exposure control results.
Paraphrase:  73,435 non-hospitalized VHA users with COVID-19 (positive test 1 March to 30 Nov 2020, alive at day 30) versus 4,990,835 VHA users "who did not have a positive test for COVID-19" (70 matched per case, enrollment dates matched to the case's positive-test date). Controls were not required to have been tested. Both groups had to have encountered the VHA in 2019. Median follow-up about 126–130 days (6-month horizon). 379 diagnostic categories plus medications and labs (821 outcomes in all); significance threshold P < 6.57 × 10⁻⁵. Negative-outcome controls: HR 1.03 (0.94–1.12) for neoplasms and 1.03 (0.95–1.12) for accidental injuries. A negative-exposure control (influenza vaccine in odd vs even months) produced no significant associations across all 821 outcomes. A second comparison set hospitalized COVID patients against patients hospitalized with seasonal influenza.
Locators:    Results, first paragraph of the non-hospitalized section; Methods, "Cohort" and "Negative outcome and exposure controls"; Discussion, limitations paragraph.
Quote:       Limitations: "we cannot completely rule out residual confounding effects."
```

### 6. Bowe, Xie, Al-Aly, Nature Medicine 2023 (VA, 2 years)

```text
URL:         https://doi.org/10.1038/s41591-023-02521-2 (PMC10504070)
Kind:        primary.
Establishes: VA 2-year estimates under a non-infected (untested-inclusive) control.
Paraphrase:  138,818 people with infection versus 5,985,227 VHA users "with no evidence of SARS-CoV-2 infection", followed 2 years for 80 prespecified sequelae (77 in the per-sequela analyses). Non-hospitalized: 69% of sequelae became non-significant by 2 years; 31% (24 of 77) remained increased. Hospitalized: 65% (50 of 77) remained increased. Cumulative 2-year DALYs 80.4 per 1,000 (non-hospitalized) and 642.8 (hospitalized). Negative outcome control (neoplasms) null in every period. The authors' own limitation runs the opposite way from PNAS: untested infections in the control group "might result in underestimation of risks". No multiple-comparison adjustment for prespecified analyses (figure legends).
Locators:    Abstract; Results paragraphs on nonhospitalized/hospitalized at 2 years; "Negative outcome control"; Methods (control construction); Discussion limitations.
```

### 7. Cai, Xie, Topol, Al-Aly, Nature Medicine 2024 (VA, 3 years)

```text
URL:         https://doi.org/10.1038/s41591-024-02987-8 (PMC11186764)
Kind:        primary. It is the study cited in the PNAS abstract's second sentence.
Establishes: VA 3-year estimates, control definition, negative outcome control.
Paraphrase:  135,161 people infected March–December 2020 versus 5,206,835 VHA users who "did not have a positive SARS-CoV-2 test" between 1 March 2020 and 30 March 2021, each with at least two VA encounters at least 180 days apart in the prior 2 years, with random T0 drawn from the cases' distribution. Non-hospitalized: IRR for PASC 1.23, 1.16, 1.05 in years 1, 2, 3; increased risk in all 10 organ systems in year 1, 9 in year 2, 3 in year 3 (neurologic, pulmonary, gastrointestinal); 41.2 sequelae and 9.6 DALYs per 1,000 in year 3. Hospitalized: IRR 2.82, 1.57, 1.34; 7 organ systems still elevated in year 3. Negative outcome control (incident neoplasm) IRRs about 0.92–1.03, all CIs crossing 1.
Locators:    Abstract; Results (lines on IRRs by year and organ systems); "negative outcome control" paragraph; Methods (control cohort); Discussion limitations.
```

### 8. RECOVER adult cohort, Thaweethai et al., JAMA 2023

```text
URL:         https://doi.org/10.1001/jama.2023.8823 (PMC10214179)
Kind:        primary.
Establishes: a prospective, symptom-survey estimate with a test-anchored uninfected group.
Paraphrase:  9,764 participants (89% infected) at 85 sites. Table 1 shows 8,646 infected and 1,118 uninfected. Uninfected participants' index date was a past negative SARS-CoV-2 test, and those with antibody evidence of prior infection were reclassified as infected. 37 of 44 self-reported symptoms had adjusted OR ≥ 1.5 (infected vs uninfected) at 6 months or later. 10% (224 of 2,231) of those first infected on or after 1 Dec 2021 and enrolled within 30 days were PASC-positive at 6 months.
Locators:    Abstract (Results); Table 1; Methods (index date definitions). Only the abstract, Table 1 and Methods were read in full.
```

### 9. Mizrahi et al., BMJ 2023 (Maccabi, Israel), a prior test-negative design

```text
URL:         https://doi.org/10.1136/bmj-2022-072529 (PMC9832503)
Kind:        primary.
Establishes: a test-negative-design study of mild COVID that still finds late-period (181–360 day) effects.
Paraphrase:  1,913,234 Maccabi members who had a PCR test between 1 March 2020 and 1 October 2021. 70 outcomes. Infected unvaccinated patients matched to uninfected (test-negative) people. Significant increases in both early (30–180 d) and late (180–360 d) periods: anosmia/dysgeusia HR 4.59 then 2.96; cognitive impairment 1.85 then 1.69; dyspnoea 1.79 then 1.30; weakness 1.78 then 1.30; palpitations 1.49 then 1.16. Hair loss, chest pain, cough, myalgia and respiratory disorders were elevated only early.
Locators:    Abstract (Results, Conclusions).
Quote:       Conclusions: "This nationwide study suggests that patients with mild covid-19 are at risk for a small number of health outcomes, most of which are resolved within a year from diagnosis."
```

### 10. CIDRAP News, 12 Jan 2023: expert criticism of the Maccabi test-negative study

```text
URL:         https://www.cidrap.umn.edu/covid-19/study-says-most-long-covid-symptoms-resolve-1-year-after-mild-cases-experts-not-so-sure
Kind:        secondary as reporting. The quotes are firsthand statements of named critics, so it is the record that Al-Aly made this argument.
Establishes: the strongest named on-record criticism of test-negative controls for post-acute outcomes. It was aimed at the Maccabi study, not the PNAS paper.
Paraphrase:  By Mary Van Beusekom; datePublished 2023-01-12. Ziyad Al-Aly, MD, "clinical epidemiologist at the Washington University School of Medicine in St. Louis and chief of research and development at the Veterans Affairs St. Louis Healthcare System", calls the test-negative design the study's "fundamental flaw". He says his group found that people with a negative COVID test had a higher cancer risk because they came in for chemotherapy and other reasons. Robert Wachter, MD, "chair of the Department of Medicine at the University of California San Francisco", raises reporting bias (who mentions a symptom at a visit). Eric Topol, MD, "founder and director of the Scripps Research Translational Institute", attributes the optimism to the cohort's young age (mean 25).
Locators:    Section "The problem with test-negative designs"; section "False assurances, gaslighting".
Quote:       Al-Aly: "People don't usually test for SARS-CoV-2 or for any other reason without an indication." / "When you test people, you're testing against people who are sick." / "It makes it look like COVID-positive people have a resolution of symptoms when in reality it's a suboptimal design that may give us a false assurance."
Quote:       Al-Aly: "What we found is that people with a COVID-negative test had a higher risk of cancer, and it turns out that people who had come to the hospital for testing did so for chemotherapy or other reasons."
```

### 11. Ayoubkhani et al., eClinicalMedicine 2026 (methods review)

```text
URL:         https://doi.org/10.1016/j.eclinm.2026.103833 (PMC13011065)
Kind:        secondary on any one study. The authors (University of Leicester, ONS, Imperial, UCL and others) own the methodological argument, and it is independent of both camps here.
Establishes: the published case that negative-test controls are contaminated by infection and that this biases toward the null. It also says untested people differ from regular testers.
Paraphrase:  "Considerations for epidemiological studies investigating emerging post-acute infection syndromes: Long Covid as a case study", Daniel Ayoubkhani (University of Leicester; ONS) and 20 co-authors, first published 16 March 2026, eClinicalMedicine vol. 94, 103833. It prefers an "always negative" to a "never positive" control because people who never test differ in ways related to Long Covid risk, as in vaccine test-negative designs. It notes that a negative test is not proof of no infection and gives LFD sensitivity of 85% at high viral load and as low as 40% in asymptomatic infection, while PCR also misses some. Its table of control-group options warns that repeat test-negatives "may have other underlying health conditions causing symptoms".
Locators:    Section on control groups (paragraphs around refs 94–102); comparison table rows on test-negative controls.
Quote:       "Any control group defined by negative tests will therefore inevitably be contaminated by people who have had COVID-19, and this exposure misclassification will attenuate the difference in symptom prevalence between the exposed and control groups towards the null of no difference."
```

### 12. Høeg, Ladhani, Prasad, BMJ Evidence-Based Medicine 2024

```text
URL:         https://doi.org/10.1136/bmjebm-2023-112338 (PMC11137465)
Kind:        secondary (an analysis/opinion piece, cited by PNAS as ref 32). It owns its argument, not any study's numbers.
Establishes: a prior published critique of untested/never-diagnosed controls, naming the VA work. It also says test-negative designs bias "in both directions".
Paraphrase:  Tracy Beth Høeg and Vinay Prasad (Epidemiology and Biostatistics, UCSF) with Shamez Ladhani (Public Health England; St George's University of London). Argues that VA research "has produced misleading results" because people diagnosed through the VA differ in health from controls. On test-negative designs: "this design is prone to bias as test-positive individuals are not the same as test-negatives and this can affect results in both directions". Example: a Swiss Omicron study with PASC 11.7% (cases) versus 10.4% (test-negative controls) at 12 weeks.
Locators:    Sections "Inappropriately-matched controls" and "Control groups created using test-negative design".
```

## Contradictions

- **Publication date.** The commission says "about 10 November 2026". The paper
  was published online on 27 Oct 2026, with an issue date of 3 Nov 2026
  (PNAS/PMC front matter; Crossref). The Stanford release went out on 28 Oct and
  CIDRAP's report on 9 Nov.
- **"Only the control group changed."** The commission says this, and the
  paper's own framing invites it ("an unrestricted control analysis using the
  same data"), but the case groups differ too. Unrestricted cases are anyone
  with a first COVID diagnosis code (10,118,877 alive at day 30). Test-based
  cases are people diagnosed within 7 days of their first PCR test claim
  (2,832,575). The enrollment anchor also differs: diagnosis date versus first
  test date (SI Extended Methods S2; Fig. 1A). So the contrast is between two
  designs, of which the control group is the largest difference.
- **"PCR-positive vs PCR-negative."** Claims carry no lab results. "Positive"
  means a COVID diagnosis code within 7 days of a PCR test claim, and "negative"
  means no COVID evidence within 7 days (SI S2; Methods M2).
- **VA negative controls versus the PNAS unrestricted replica.** In the Komodo
  re-implementation, the unrestricted design flagged 53.1% of 49 negative-control
  outcomes, including injury by lightning/drowning/electrocution (+76%) and
  firearm injuries. The VA studies that the replica was modelled on reported
  null negative-outcome controls: neoplasms HR 1.03 (0.94–1.12) and accidental
  injuries HR 1.03 (0.95–1.12) at 6 months, neoplasms null over 2 and 3 years, and
  a null negative-exposure control across 821 outcomes (Al-Aly 2021; Bowe 2023;
  Cai 2024). The VA control groups also required prior VHA encounters (in 2019,
  or two visits 180+ days apart), while the PNAS replica required one claim in
  2019. The PNAS paper does not reconcile its replica's negative-control failures
  with the VA papers' passes. Any statement that the VA findings are artifacts is
  therefore an inference from a re-implementation, not a reanalysis.
- **Test-anchored studies that still find late effects.** Mizrahi (BMJ 2023;
  test-negative design) found cognitive impairment HR 1.69, dyspnoea 1.30,
  weakness 1.30, palpitations 1.16 and anosmia/dysgeusia 2.96 at 181–360 days.
  PNAS's test-based design finds only 5 outcomes at 120–359 days (myopathy, hair
  loss, PE, acute PE, respiratory failure), none cognitive. Thresholds differ
  (PNAS needs RR ≥ 1.1 with Bonferroni across 614 outcomes; Mizrahi reports 70
  prespecified outcomes), and so do the outcome sources (claims vs Maccabi EHR)
  and populations. RECOVER (JAMA 2023) found 37 self-reported symptoms with
  aOR ≥ 1.5 at ≥6 months against a test-anchored uninfected group. PNAS
  (Discussion) compares RECOVER's 37 with its own 43 at days 30–119, but
  RECOVER's survey was at 6 months or later, which falls in PNAS's middle window,
  where PNAS finds 5.
- **RECOVER figures in PNAS versus the JAMA paper.** PNAS's Discussion gives
  RECOVER as infected N = 7,992 and uninfected N = 1,347, and says test-negatives
  who later developed COVID "were crossed over". The JAMA paper's Table 1 shows
  8,646 infected and 1,118 uninfected (total 9,764). My partial read of its
  Methods found later-infected uninfected participants excluded and those with
  antibody evidence reclassified. I did not find the PNAS numbers in the JAMA
  paper. They may come from a different RECOVER analysis set. Unresolved.
- **Direction of the contamination bias.** Bowe 2023 says untested infections
  in its control group would cause *under*estimation. PNAS says the
  20.2%-later-positive contamination of its test-negative controls is
  "conservative". Both are biases toward the null on their own designs. PNAS's
  claim is that the larger untested-control bias runs the other way (selection
  into testing). These do not conflict, but a writer should not present
  "contamination" as unique to test-negative controls.
- **Critics of the design.** Al-Aly's on-record critique (CIDRAP, Jan 2023) is
  that test-negative controls are sick people and make COVID effects look as if
  they resolve, and he cites a test-negative cancer excess in his group's own
  work. The PNAS authors concede the mechanism (collider bias; cancer as the
  example) but measure it as small: 2 of 49 negative controls below 1, and a
  placebo correlation of −0.22. Al-Aly's critique predates this paper and was
  aimed at the Maccabi study.
- **Press-release wording.** Leskovec's "98 percent fewer" figure refers only to
  days 120–359. CIDRAP's "first four months after they tested" understates the
  follow-up, which ran to 2 years.

## Numbers

```text
Figure: 14.4 billion claims; 244.7 million patients
Owner:  PNAS paper, Abstract and Methods M1 (SI S1: Pandemic extract 48,812,613,382 claims / 228,010,550 patients; Control extract 5,759,362,767 claims / 33,749,570 patients)
Scope:  Two Komodo extracts combined; observation to 4 Apr 2023. Note 228.0 M + 33.7 M = 261.8 M exceeds 244.7 M; the paper does not explain the overlap.

Figure: 614 outcomes (565 plausibly COVID-caused + 49 negative controls)
Owner:  PNAS SI Extended Methods S1.2
Scope:  Filtered from 695 candidates by excluding very rare outcomes

Figure: Attributable outcomes, test-based design: 43 / 5 / 0
Owner:  PNAS Abstract; Results; Fig. 1B
Scope:  Of 614 outcomes; windows days 30–119 / 120–359 / 360–719; RR ≥ 1.1 and Bonferroni P < 0.05

Figure: Attributable outcomes, unrestricted design: 262 / 286 / 369
Owner:  PNAS Abstract; Results; Fig. 1B
Scope:  Same outcomes, windows, thresholds

Figure: Reduction 83.5% / 98.2% / 100%
Owner:  PNAS Abstract
Scope:  (unrestricted − test-based) / unrestricted per window

Figure: Share of 614 outcomes with RR ≥ 1.1 — unrestricted 82.7% / 77.5% / 85.0%; placebo-case 82.5% / 66.6% / 54.8%; test-based 8.8% / 2.3% / 1.6%
Owner:  PNAS SI Fig. S5 legend
Scope:  Days 30–120 / 120–360 / 360–720; the legend states the RR threshold only, so these are not the Bonferroni-significant counts

Figure: Negative-control false-association rate 53.1% (unrestricted) vs 4.1% (test-based)
Owner:  PNAS Results, "Comparing False Attribution Rates"; Fig. 3
Scope:  49 negative-control outcomes; RR ≥ 1.1 (unrestricted) or RR ≤ 0.9 (test-based) with P < 0.05 unadjusted. The test-based 4.1% = 2 of 49, both *below* 1

Figure: Lightning/drowning/submersion/electrocution/vibration injury +76%; adult congenital malformations of eye/ear/face/neck +18.6%
Owner:  PNAS Results; Fig. 3
Scope:  Unrestricted design, days 30–119; test-based RRs non-significant, at or below about 1.0

Figure: Placebo cases: 82.5% of outcomes RR ≥ 1.1 at days 30–119; Spearman 0.48 with unrestricted COVID RRs (P < 10⁻⁴); test-based Spearman −0.22
Owner:  PNAS Results "Biases Due to Selective COVID-19 Testing"; SI Fig. S2
Scope:  614 outcomes, days 30–120

Figure: Cohort sizes, test-based design: 39,967,054 first PCR tests → 39,199,683 with no prior COVID → cases 2,866,888 → 2,832,575 alive at day 30; controls 36,320,411 → 36,095,303 alive at day 30 → down-sampled 5:1 to 14,162,875
Owner:  PNAS SI Extended Methods S2 (Table S2 prints 2,832,376 cases / 14,162,370 controls)
Scope:  First PCR test 1 Mar 2020–1 Mar 2021

Figure: Cohort sizes, unrestricted design: cases 10,445,894 diagnosed → 10,431,860 → 10,118,877 alive at day 30; controls 18,084,711 with no COVID diagnosis → 17,728,714 → 17,717,308
Owner:  PNAS SI Extended Methods S2 (Table S1 prints 10,116,899 / 17,716,950)
Scope:  Diagnosis 1 Mar 2020–1 Mar 2021; controls from Control extract, which may include tested people

Figure: Cohort sizes, placebo-case design: 27,263,919 negative-tested "cases"; 17,726,124 controls
Owner:  PNAS SI Extended Methods S2 (Table S3: 27,263,919 / 17,701,534)
Scope:  As above

Figure: Unweighted visit history per patient: unrestricted cases 54.0 total (ER 1.56) vs controls 31.56 (ER 0.8); test-based cases 46.53 (ER 1.25) vs controls 47.92 (ER 1.23)
Owner:  PNAS SI Tables S1, S2
Scope:  4-year pre-enrollment; equal after weighting in both designs

Figure: Test-negative controls later testing positive: 4.2% by day 119; 10.1% by day 359; 20.2% by 2 years; 0.6–1.1% per 30 days
Owner:  PNAS Discussion; SI Fig. S7
Scope:  Test-based control group

Figure: 30-day mortality 1.2% (test-positive) vs 0.62% (test-negative)
Owner:  PNAS Discussion
Scope:  Excluded from post-acute analysis by the alive-at-30-days rule

Figure: Early-window RRs (test-based): myopathy 3.1; hair loss 1.89; palpitations 1.21; malnutrition 1.20; fatigue 1.12
Owner:  PNAS Fig. 2 legend
Scope:  Days 30–119; Bonferroni-corrected bootstrap CIs ≥ 1.1

Figure: Middle-window survivors (test-based, RR > 1.1): myopathy, hair loss, pulmonary embolism, acute pulmonary embolism, respiratory failure/insufficiency/arrest (5)
Owner:  PNAS Results "Characterizing Long COVID…"; Fig. 2B
Scope:  Days 120–359. Pneumonia, shortness of breath, chest pain and fatigue have RR 1.0–1.1 but significant risk differences

Figure: VA 2021: 73,435 non-hospitalized COVID vs 4,990,835 VHA controls; negative-outcome HR 1.03 (neoplasms), 1.03 (accidental injuries)
Owner:  Al-Aly et al., Nature 2021
Scope:  ~6 months post-acute; positive test 1 Mar–30 Nov 2020

Figure: VA 2-year: 138,818 vs 5,985,227; non-hospitalized 24 of 77 sequelae still elevated at 2 y (31%); hospitalized 50 of 77 (65%)
Owner:  Bowe et al., Nat Med 2023
Scope:  2 years; 80 prespecified sequelae

Figure: VA 3-year: 135,161 vs 5,206,835; non-hospitalized PASC IRR 1.23 / 1.16 / 1.05 (years 1/2/3); organ systems elevated 10 / 9 / 3; year-3 burden 41.2 sequelae and 9.6 DALYs per 1,000
Owner:  Cai et al., Nat Med 2024
Scope:  Infected Mar–Dec 2020; 3 years

Figure: RECOVER: 9,764 participants (8,646 infected / 1,118 uninfected per Table 1); 37 of 44 symptoms aOR ≥ 1.5; 10% PASC-positive at 6 months (224/2,231)
Owner:  Thaweethai et al., JAMA 2023
Scope:  ≥6 months after infection or test; self-reported symptoms

Figure: Maccabi test-negative: 1,913,234 tested; late (181–360 d) HRs anosmia/dysgeusia 2.96, cognitive impairment 1.69, dyspnoea 1.30, weakness 1.30, palpitations 1.16
Owner:  Mizrahi et al., BMJ 2023
Scope:  Mild COVID, unvaccinated vs uninfected; 70 outcomes
```

Chart-ready table (PNAS, attributable outcomes of 614; RR ≥ 1.1 and Bonferroni
P < 0.05):

| Window (days after enrollment) | Paper's gloss | Unrestricted control | Test-based control | Reduction |
|---|---|---|---|---|
| 30–119 | 1–4 mo | 262 | 43 | 83.5% |
| 120–359 | 5–12 mo | 286 | 5 | 98.2% |
| 360–719 | 13–24 mo | 369 | 0 | 100% |

Supporting series (SI Fig. S5, share of 614 outcomes with RR ≥ 1.1, no
significance filter):

| Window | Unrestricted (COVID cases) | Unrestricted (placebo: negative-tested "cases") | Test-based |
|---|---|---|---|
| 30–120 | 82.7% | 82.5% | 8.8% |
| 120–360 | 77.5% | 66.6% | 2.3% |
| 360–720 | 85.0% | 54.8% | 1.6% |

The placebo column shows the mechanism. People whose only "exposure" is a
negative test look nearly as harmed as COVID cases when compared with
Control-extract people.

Earlier-study design comparison:

| Study | Cases | Comparison group | Tested controls required? | Horizon | Headline |
|---|---|---|---|---|---|
| Al-Aly, Nature 2021 (VA) | 73,435 non-hosp., positive test | 4,990,835 VHA users without positive test | No | ~6 mo | Multisystem sequelae; negative-outcome controls null |
| Bowe, Nat Med 2023 (VA) | 138,818 | 5,985,227 VHA users, no evidence of infection | No | 2 y | 31% (non-hosp.) / 65% (hosp.) of 77 sequelae still elevated at 2 y |
| Cai, Nat Med 2024 (VA) | 135,161 | 5,206,835 VHA users without positive test | No | 3 y | Non-hosp. IRR 1.05 in year 3; 3 organ systems |
| Mizrahi, BMJ 2023 (Maccabi) | infected, unvaccinated | test-negative members | Yes | 1 y | Few outcomes; most resolve within a year; 5 persist to 181–360 d |
| Thaweethai, JAMA 2023 (RECOVER) | 8,646 infected | 1,118 uninfected, indexed to a negative test | Yes (per protocol, not care-seeking) | ≥6 mo | 37 symptoms aOR ≥ 1.5 |
| Nilforoshan, PNAS 2026 | 2,832,575 (test-based) | 14,162,875 test-negative | Yes (care-seeking PCR) | 2 y | 43 / 5 / 0 |

## Limits

- No independent expert reaction to the PNAS paper exists that I could find.
  CIDRAP (9 Nov), the Stanford release, healthcare-in-europe.com and StudyFinds
  quote only the authors. Searches for Al-Aly, Topol and others responding to
  this paper found nothing. The commission's rule applies: say no one has
  commented yet.
- I could not get per-organ-system counts of surviving outcomes per design.
  The SI gives per-system RR panels (Figs. S15–S80) only as images, and the
  GitHub repo (snap-stanford/longcovid) holds code but no results files. What I
  have: the named systems in the early window (respiratory, cardiovascular,
  renal, immune, musculoskeletal, gastrointestinal, neurologic, dermatological),
  the top-25 list in Fig. 2A, and the 5 middle-window survivors. A "which
  survive" visual can be built from those named outcomes, not from system
  counts.
- I could not establish what share of the VA studies' published sequelae would
  disappear under a test-based design. Nobody has reanalysed the VA data that
  way. The PNAS comparison uses its own unrestricted replica in Komodo claims.
- I could not confirm the PNAS paper's RECOVER figures (7,992 / 1,347; "crossed
  over") against the JAMA paper. The JAMA Table 1 numbers differ.
- I read the Stanford release through EurekAlert! with a summarizing fetch, so
  its quotes should be checked word for word on the page before printing. The
  news.stanford.edu original returned 403.
- I could not read the Undark 2024 piece in which Al-Aly reportedly criticized
  a Danish test-negative study (403).
- Claims data cannot measure fatigue or cognitive symptoms that are not coded.
  The release and the paper both say so, and the size of that under-recording
  is not established anywhere I read.

## Source assets

```text
Asset: PNAS Fig. 1 (Panel A: two-row diagram of the unrestricted vs test-based designs, showing who is enrolled at a healthcare visit and when; Panel B: line chart of attributable-outcome counts by window for both designs)
Shows: The whole argument in one figure: the enrollment mechanism and the 262/286/369 vs 43/5/0 divergence
Crop:  Panel B alone must keep the y-axis label stating the threshold (significant and RR ≥ 1.1) and the day-window x-axis; Panel A must keep the "Healthcare visit" / "Enrollment date" legend. CC BY 4.0, credit Nilforoshan et al., PNAS 2026
```

```text
Asset: PNAS Fig. 3 (paired RR bar charts for 10 negative-control outcomes, unrestricted vs test-based)
Shows: Implausible "effects" (e.g. lightning/drowning injuries) appear under the unrestricted design and vanish under the test-based design
Crop:  Keep both panels side by side and the outcome labels; keep the red significance colouring and its meaning
```

```text
Asset: PNAS SI Fig. S1 (adult cerebral palsy claims over time before and after enrollment, cases vs controls, both designs)
Shows: The selection mechanism concretely: cases' pre-test rise in an unrelated condition is matched by test-negative controls but not by untested controls
Crop:  Must keep the pre-enrollment portion of the time axis and both control lines (unweighted and weighted)
```

```text
Asset: PNAS SI Fig. S2B (scatter of 614 outcomes: placebo-case RR vs COVID RR, unrestricted vs test-based)
Shows: The negative-test "exposure" predicts the unrestricted design's COVID effects (Spearman 0.48) but not the test-based design's (−0.22)
Crop:  Keep both panels and the correlation values
```

```text
Asset: PNAS SI Fig. S7 (cumulative fraction of test-negative controls later testing positive)
Shows: The size of control contamination over follow-up, which grows to 20.2% by 2 years
Crop:  Keep the x-axis in days and the y-axis fraction
```

```text
Asset: PNAS Fig. 2 (top-25 outcomes, RR and RD at days 30–119 and the same outcomes at 120–359)
Shows: Which outcomes survive into the middle window
Crop:  Keep the outcome labels and both RR panels. The RD panels are optional
```

Al-Aly 2021, Bowe 2023, Cai 2024, Mizrahi 2023, RECOVER 2023, Ayoubkhani 2026
and Høeg 2024: none were needed. Their figures are better restated in the
design-comparison table than cropped. The Cai 2024 Fig. 3 per-year organ-system
panel exists (CC BY) if one is wanted.

## Discarded

```text
https://studyfinds.com/long-covid-real-some-symptoms-overcounted/: secondary repeat of the paper and release; no independent comment; its figures are owned by the paper
https://humanprogress.org/study-finds-fewer-shorter-long-covid-effects-after-correcting-bias/: reprint of the Stanford release
https://healthcare-in-europe.com/en/news/study-definition-what-is-long-covid.html: reprint of the Stanford release (29 Oct 2026); used only to corroborate author titles and that no outside expert is quoted
https://www.scimex.org/newsfeed/long-covid-symptoms-and-duration-revised: 403; PNAS press-release mirror, nothing beyond the paper
https://news.stanford.edu/stories/2026/10/long-covid-health-affects-study-design: 403 to automated fetch; content read via EurekAlert! copy
https://undark.org/2024/07/25/long-covid-clash-of-definition-study-design/: 403; could not verify the Al-Aly quotes it reportedly carries about a Danish study
https://krbyers.substack.com/p/revealed-what-144-billion-medical: individual newsletter, not an expert in a position to know; not read further
https://www.japantimes.co.jp/news/2026/11/03/world/science-health/long-covid-recovery-study/: about a different (Annals of Internal Medicine) study, per search summary
https://github.com/snap-stanford/longcovid: code only, no result tables; nothing citable for counts
```
