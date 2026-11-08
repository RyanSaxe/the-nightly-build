# Evidence record: Lp(a)HORIZON and the genetic estimates (researcher 01)

Checked 8 November 2026. The evidence supports three things firmly: Lp(a)HORIZON (NCT04023552) found no effect of pelacarsen on its four-part cardiovascular composite (hazard ratio 1.02, 95% CI 0.90-1.15, 511 vs 503 first events in 4,157 vs 4,165 analysed patients, median follow-up 4.7 years); Lp(a) fell from a median of about 236 nmol/L to 64.4 nmol/L at 12 months on drug and stayed at 233.4 nmol/L on placebo; and the two Mendelian randomization papers the commission names express their requirement in mg/dL (Burgess 2018: about 101.5 mg/dL; Lamina and Kronenberg 2019: 65.7 mg/dL, both measured against a 38.67 mg/dL = 1 mmol/L LDL-C change). It is thin in three places. I could not open the NEJM paper or its supplement (HTTP 403 from nejm.org), so every trial figure below comes from the investigators' own releases, the PubMed abstract of the companion NEJM Evidence paper, and press reports that quote the presentation; the trial's stated power assumptions (assumed hazard ratio, assumed event rate) are not confirmed from any document I could open; and the trial reports Lp(a) in nmol/L for its on-treatment values while the genetic estimates are in mg/dL, so the absolute reduction in the genetic papers' unit is not published in anything I read and any mg/dL figure for the reduction is my derivation, flagged as such. The evidence partly undermines the commissioned framing "the trial tested a smaller dose than 78% suggests": by the paper's own measured scale the median reduction (about 171 nmol/L) is, on every conversion I can defend, in the range of the Lamina and Kronenberg requirement and somewhat under the Burgess one, and the landmark analysis of patients with the largest reductions shows no benefit either (see Contradictions and the closing note under Limits).

## Decisions made without asking (orchestrator could not answer)

1. NEJM full text and supplement were gated (403 on `nejm.org/doi/full/10.1056/NEJMoa2610159`, also via WebFetch). I did not pursue further routes. The brief's fallback set was used: AHA news release, Cleveland Clinic newsroom release, Cleveland Clinic Consult QD article, registry record, plus the PubMed abstract of the NEJM Evidence extended analyses and the published design paper abstract. I did not find the AHA slides themselves.
2. I treated the Cleveland Clinic and AHA releases as primary for what the investigators said and as the nearest available owners of the trial numbers, and labelled every trial figure by which document gave it. Where two documents disagree I report both (see Contradictions).
3. I did not convert nmol/L to mg/dL on the writer's behalf. Where I give an mg/dL equivalent it is labelled "derived" with its basis. The only conversion bases I found in sources are listed under Numbers.

## Sources

### The trial

```text
URL:         https://doi.org/10.1056/NEJMoa2610159  (NEJM, article page https://www.nejm.org/doi/10.1056/NEJMoa2610159)
Kind:        primary (the trial report), but NOT READ: nejm.org returned 403 to every request
Establishes: Only bibliographic facts, via Crossref (https://api.crossref.org/works/10.1056/NEJMoa2610159): title "Pelacarsen and Cardiovascular Outcomes in Patients with High Lipoprotein(a)"; first author Leslie Cho, Cleveland Clinic; last author Steven E. Nissen; 21 authors; funder Novartis; published online 7 November 2026; 21 references including Burgess 2018 (doi 10.1001/jamacardio.2018.1470) and the Atherosclerosis mg/dL-nmol/L concordance paper.
Paraphrase:  The deposited reference list includes Burgess et al. JAMA Cardiology 2018 (doi 10.1001/jamacardio.2018.1470) and has no entry with Lamina and Kronenberg's DOI (10.1001/jamacardio.2019.1041); a few references carry no DOI, so this does not prove it is uncited. Nothing about its content was verified.
Locators:    Crossref metadata record only.
```

```text
URL:         https://clinicaltrials.gov/study/NCT04023552
Kind:        primary (sponsor's registry record for the trial; Novartis is the sponsor)
Establishes: Design as registered: phase 3, randomized, parallel, double-blind (participant, investigator), placebo-controlled; pelacarsen (TQJ230) 80 mg subcutaneously monthly vs matching placebo; enrollment 8,323 (actual); start 2019-12-12; primary completion 2026-07-16 (actual); status COMPLETED, last updated 2026-08-28; sponsor Novartis Pharmaceuticals. Official title "A Randomized Double-blind, Placebo-controlled, Multicenter Trial Assessing the Impact of Lipoprotein (a) Lowering With Pelacarsen (TQJ230) on Major Cardiovascular Events in Patients With Established Cardiovascular Disease". No results posted (hasResults false on 2026-11-08). No power assumptions anywhere in the record; no protocol or SAP attached.
Paraphrase:  Two primary outcomes: time to first committee-confirmed expanded MACE (cardiovascular death, non-fatal MI, non-fatal stroke, urgent coronary revascularization requiring hospitalization) in patients with Lp(a) >= 70 mg/dL, and the same in the subpopulation with Lp(a) >= 90 mg/dL, "approximately 4 years". Secondary: three-component MACE (CV death, MI, stroke); CHD composite (CHD death, MI, urgent revascularization); all-cause death; change in log Lp(a) at year 1. Key inclusion: Lp(a) >= 70 mg/dL at screening by central laboratory; MI >= 3 months and <= 10 years before screening, or ischemic stroke in the same window, or symptomatic peripheral artery disease.
Locators:    Primary outcomes, secondary outcomes and eligibility modules of the registry record (read through the registry's v2 JSON API, address given above is the human page).
```

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/40185318/   (Cho L, Nicholls SJ, Nordestgaard BG, et al. Am Heart J 2025;287:1-9, doi 10.1016/j.ahj.2025.03.019)
Kind:        primary (design paper written by the trial's steering authors and Novartis employees)
Establishes: Abstract read in full; full text NOT read (sciencedirect.com 403). Design: 8,323 patients, Lp(a) >= 70 mg/dL "(approximately 149 nmol/L)", 1:1, monthly SC pelacarsen 80 mg or placebo; "The minimum follow-up is required to be 2.5 years. The study will end when 993 CEC confirmed primary CV events have accumulated. Based on the current event accrual trend, the overal study duration is anticipated to be approximately 6 years." Primary endpoint tested in the overall population and in Lp(a) >= 90 mg/dL ("approximately 192 nmol/L") with multiplicity control.
Paraphrase:  The trial was event-driven: 993 adjudicated first primary events. The stated conversion basis here is 70 mg/dL ~ 149 nmol/L and 90 mg/dL ~ 192 nmol/L (a factor of about 2.13). The power statement (assumed hazard ratio, power, alpha, assumed placebo event rate, assumed Lp(a) lowering) sits in the full text and I could not open it. A search summary claimed the paper states ">90% power for a hazard ratio of about 0.80 overall or 0.75 in the >= 90 mg/dL subpopulation" and that pharmacodynamic modelling predicted about an 80% time-averaged Lp(a) reduction; I could not verify either claim in the document. Treat both as unconfirmed.
Locators:    Abstract, "Study design" paragraph.
Quote:       "The study will end when 993 CEC confirmed primary CV events have accumulated."
```

```text
URL:         https://newsroom.heart.org/news/lp-a-horizon-trial-lp-a-fell-by-78-but-cardiovascular-outcomes-unexpectedly-neutral
Kind:        secondary on the trial (the American Heart Association reports a presentation it hosted, with the investigator's quotes), primary for what Nissen said. Published 7 November 2026, embargo lifted 8:50 am CT.
Establishes: Trial description and Nissen's statements. 797 sites, 42 countries; 14,249 screened; 8,323 enrolled (mean age 60, 27% women, 26% diabetes); 82% prior MI, 10% prior ischemic stroke, 14% symptomatic PAD; 37% early-onset events. Median baseline Lp(a) "109 mg/dL (236 nmol/L)" for all participants; threshold "70 mg/dL (148 nmol/L)" and "90 mg/dL (192 nmol/L)". About 75% already met guideline criteria for blood pressure and cholesterol; 77-78% on high-intensity statins. Reduction "by an average of 78%". Serious adverse events 37.3% pelacarsen vs 41.1% placebo; anaphylaxis in 19 pelacarsen patients, none on placebo, no deaths; about 21% (pelacarsen) vs more than 7% (placebo) stopped study drug for adverse reactions. Less than 4% of participants were of African ancestry; 78% self-identified as white. Says the primary analysis and "Extended" analyses were published simultaneously in NEJM and NEJM Evidence.
Paraphrase:  The release gives no hazard ratio, no event counts, no confidence interval. It uses 148 and 192 nmol/L as the conversions of 70 and 90 mg/dL. It defines the primary composite as including "death from any cardiovascular cause", the registry and other sources say cardiovascular death.
Locators:    "Research Highlights", "What are the study's key findings?", "What are the study's details, background, design and limitations?".
Quote:       "I cannot avoid the disappointing conclusion – it didn't work. Pelacarsen improved Lp(a) measures significantly – 78% lower; however, cardiovascular outcomes were unchanged. The neutral finding was unexpected and surprising to the medical community." (Steven E. Nissen, M.D., FAHA, "senior author of the new study and chief academic officer of the Miller Family Heart, Vascular & Thoracic Institute at the Cleveland Clinic in Cleveland, Ohio").
```

```text
URL:         https://consultqd.clevelandclinic.org/lipoproteina-reduction-with-pelacarsen-has-no-impact-on-cardiac-events
Kind:        secondary in form (a Cleveland Clinic clinician-facing article summarising the paper), but it is the institution of the first author, the principal investigator and the study chair, and it reproduces the paper's tables. Treat its numbers as the nearest available copy of the NEJM figures, not as the paper. Published 7 November 2026.
Establishes: The most complete public set of NEJM numbers. Randomized 8,350, efficacy analysis 8,322 (pelacarsen 4,157; placebo 4,165); enrolled December 2019 to July 2022; median follow-up 57 months (4.7 years); primary endpoint assessed in 97.2%; vital status 99.3%. Randomization stratified by screening Lp(a); the >= 90 mg/dL stratum was 78.6% of each group. Baseline table: median Lp(a) 235.6 nmol/L (108.4 mg/dL) pelacarsen vs 236.2 nmol/L (108.2 mg/dL) placebo; median LDL-C 65.0 vs 64.2 mg/dL; median hsCRP 0.8 mg/L both; high-intensity statin 77.1% vs 78.2%; SBP 125.5 vs 125.1 mm Hg. Lp(a) at 12 months: median 64.4 nmol/L pelacarsen vs 233.4 nmol/L placebo, "an estimated 77.7% treatment difference". "Over the course of the trial, the time-averaged reduction from baseline was 161.2 nmol/L with pelacarsen versus 17.1 nmol/L with placebo." Primary: 511 (12.3%) vs 503 (12.1%), HR 1.02 (95% CI 0.90-1.15) in Lp(a) >= 70 mg/dL; 402 (12.3%) vs 403 (12.3%), HR 1.00 (95% CI 0.87-1.15) in >= 90 mg/dL. Safety: drug-related AEs 56.8% vs 18.0%; AEs leading to discontinuation 20.6% vs 7.5%; premature discontinuation of trial regimen for any reason 35.1% vs 18.3%; mean exposure to study drug 3.5 years pelacarsen vs 4.0 years placebo.
Paraphrase:  Nissen's stated explanations (quoted below) and the investigators' framing. Nissen says: "This is very close to what was seen in phase 2 trials, so the drug did what it was supposed to do in terms of Lp(a) lowering." On lifelong exposure: "If you have a low Lp(a) level from your genetics, it's present from birth ... Here we intervened and lowered patients' Lp(a) to a more normal level for a median of 4.7 years, but that's not a lifetime ... It may be that a person needs to have lifelong Lp(a) reduction to be protected." On background therapy: intensive LDL and blood pressure control "may have limited the ability to detect an additional benefit"; event rates "on the low side"; "The trial needed to continue a bit longer than we expected in order to obtain the requisite number of events because the event rate was relatively low." On potency: pelacarsen "reduces Lp(a) to a lesser degree than the small interfering RNA [siRNA] agents in ongoing trials". Disclosure: "the Cleveland Clinic Coordinating Center for Clinical Research (C5Research) has received funding to conduct clinical trials from multiple biopharmaceutical companies, including Novartis"; Nissen receives no personal compensation.
Locators:    Sections "Lp(a)HORIZON backdrop and design", "Patient characteristics", "Primary efficacy results", "Safety and tolerability", "Making sense of the findings", "What's next?". The two baseline and result tables are in the article body.
Quote:       "These results were disappointing and unexpected, particularly given the findings of prior observational and Mendelian randomization studies" ... "And they don't represent a near miss. The hazard ratio for the primary endpoint in the full study cohort was 1.02, and our extensive secondary analyses showed that no matter how you slice the data, the result was essentially the same — neutral." (Steven Nissen, MD, "study chair of Lp(a)HORIZON and Chief Academic Officer of Cleveland Clinic's Heart, Vascular and Thoracic Institute").
             "Regardless of the findings of Lp(a)HORIZON, it is important to remember that Lp(a) is a causal risk factor" (Leslie Cho, MD, "the trial's first author and principal investigator, Co-Section Head of Preventive Cardiology at Cleveland Clinic").
```

```text
URL:         https://newsroom.clevelandclinic.org/2026/11/07/cleveland-clinic-trial-shows-novel-lipoproteina-drug-did-not-reduce-major-cardiovascular-events-after-nearly-5-years
Kind:        secondary on the trial (institutional news release), primary for the institution's statements
Establishes: Reduction from baseline in Lp(a) at one year "3.2% in the placebo group and 78.4% in the pelacarsen group with an estimated treatment difference of 77.7% percentage points". LDL-C after one year "fell to 62.3 mg/dL with pelacarsen, but rose to 71.2 mg/dL with the placebo. Overall, pelacarsen lowered LDL by 13.3 percentage points compared to placebo." 8,322 patients randomized December 2019 to July 2022; median follow-up 57 months. Primary endpoint 12.3% vs 12.1%.
Paraphrase:  The only source I found for the LDL-C difference between arms. Note that 78.4 minus 3.2 is 75.2, not 77.7: the 77.7 is a model-based "estimated treatment difference" and the release does not say how it was computed.
Locators:    Body paragraphs 8-9 of the release.
```

```text
URL:         https://www.acc.org/Latest-in-Cardiology/Articles/2026/11/06/14/37/sat-10am-lpa-aha-2026
Kind:        secondary (American College of Cardiology news story on the presentation, 7 November 2026)
Establishes: "pelacarsen resulted in a 78.4% reduction in Lp(a) levels after 12 months of treatment and to a time-averaged percentage change from baseline of -73.9% over an average of five years." Average baseline "236 nmol per liter". Says "503 vs. 511 patients, respectively" for pelacarsen vs placebo, which reverses the order shown in every other source (511 pelacarsen, 503 placebo; see Contradictions). Reports the NEJM Evidence analyses as on-treatment, uninterrupted treatment (no interruption >60 days), total events, and subgroups by Lp(a), LDL-C and hsCRP. Nissen: "siRNA therapeutics may reduce Lp(a) to a greater extent and be better tolerated". Nissen: "A single trial does not provide definitive evidence of a lack of benefit of lowering Lp(a) as a strategy to reduce the cardiovascular risk."
Paraphrase:  Source of the -73.9% time-averaged figure. Titles: "Steven E. Nissen, MD, MACC".
Locators:    Paragraphs 2-5.
```

```text
URL:         https://www.hcplive.com/view/lp-a-horizon-shows-pelacarsen-lowers-lp-a-78-but-not-cardiovascular-events
Kind:        secondary (trade press that cites the NEJM paper directly: Cho L, Nicholls SJ, Frndak S, et al., doi 10.1056/NEJMoa2610159)
Establishes: Reproduces NEJM figures. At 12 months Lp(a) fell 78.4% with pelacarsen and 3.2% with placebo (difference 77.7 percentage points; 95% CI 77.0-78.4). 511/4157 (12.3%) vs 503/4165 (12.1%), HR 1.02 (95% CI 0.90-1.15; P = .76). >= 90 mg/dL: HR 1.00 (95% CI 0.87-1.15; P = .99). Three-component MACE 10.2% vs 10.1%, HR 1.01 (0.88-1.16). CHD-death composite 9.4% vs 9.7%, HR 0.97 (0.85-1.12). All-cause death 5.7% vs 5.9%, HR 0.98 (0.82-1.17). Median baseline Lp(a) 235.8 nmol/L; 76.6% prior MI; 77.6% high-intensity statin. Patients aged 18-80. Anaphylaxis 19 vs 0; eight hypersensitivity reactions led to hospitalisation. "After a suspected case of anaphylaxis in March 2023, pelacarsen injections were moved to a medically supervised setting for 6 months before at-home dosing resumed." The investigators "suggested short-term Lp(a) reduction may not confer the benefit linked to lifelong lower levels in mendelian randomization studies, and strict background risk-factor control may have limited any added benefit."
Paraphrase:  Source of the P values I judge consistent with the confidence intervals (see Contradictions) and of the supervised-dosing detail.
Locators:    Body, sections "Lp(a)HORIZON trial design and pelacarsen MACE results", "Pelacarsen safety, tolerability, and discontinuation in Lp(a)HORIZON".
```

```text
URL:         https://www.healio.com/news/cardiology/20261107/pelacarsen-no-better-than-placebo-in-patients-with-high-lipoproteina-heart-disease
Kind:        secondary (trade press reporting Nissen's presentation and press conference, with an outside cardiologist's comment)
Establishes: Components of the primary endpoint: MI HR 0.99 (0.82-1.18); stroke 1.06 (0.82-1.37); urgent revascularization 1.04 (0.8-1.36); CV death 0.93 (0.73-1.19). Extended analyses: on-treatment HR 0.98 (0.85-1.12); uninterrupted treatment HR 1.09 (0.89-1.34); total events rate ratio 1.00 (0.87-1.14); landmark at 3 months among those alive and event-free: reduction in Lp(a) at or above the median of 170 nmol/L, HR 1.09 (0.92-1.29); achieved Lp(a) at or below the median of 69.5 nmol/L, HR 1.10 (0.93-1.29). Primary-endpoint result "did not vary by baseline Lp(a), LDL, high-sensitivity C-reactive protein or time between qualifying CVD event and enrollment." Nissen at the press conference: "Background therapy was optimized with baseline LDL cholesterol and blood pressure among the lowest achieved of any CV outcome trial, which may have precluded showing further benefits."; "it does lower our expectations for the likelihood of success"; "I am worried that people ... will bail out on the Lp(a) hypothesis. That would be a tragic outcome." Outside cardiologist Jared A. Spitz, MD, FACC, FAHA, Inova Schar Heart and Vascular, who "reports being a site principal investigator for a trial of a Lp(a) drug sponsored by Amgen": "This was about as neutral a trial as a trial can get." and "we have to wait until we see the other secondary prevention trial."
Paraphrase:  Healio prints "148 mmol/L" for the 70 mg/dL threshold; this is a typo for nmol/L. Source for the stroke and revascularization component hazard ratios. Titles: Nissen as "chief academic officer of the Sydell and Arnold Miller Family Heart, Vascular & Thoracic Institute and the Lewis and Patricia Dickey Chair in Cardiovascular Medicine at Cleveland Clinic", "Healio | Cardiology Today Editorial Board Member".
Locators:    Body from "For Lp(a)HORIZON, Nissen and colleagues randomly assigned ..." to the end of the extended-analyses list; Spitz perspective box.
```

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/42998055/   (Nissen SE, Cho L, Frndak S, et al. "Extended Analyses of Pelacarsen and Cardiovascular Outcomes in Patients with High Lipoprotein(a)." NEJM Evid 2026 Nov 7; doi 10.1056/EVIDoa2600373)
Kind:        primary (the extended-analyses paper, abstract only; full text on evidence.nejm.org returned 403)
Establishes: On treatment: primary endpoint in 434 participants (10.4%) placebo and 380 (9.1%) pelacarsen, HR 0.98 (95% CI 0.85-1.12). Uninterrupted treatment: 167 (11.0%) pelacarsen vs 204 (10.1%) placebo, HR 1.09 (0.89-1.34). Total events: 644 pelacarsen vs 646 placebo, rate ratio 1.00 (0.87-1.14). Landmark at 3 months (alive and free of the endpoint): HR 1.09 (0.92-1.29) for reduction in Lp(a) at or above the median (170 nmol/l); HR 1.10 (0.93-1.29) for achieved Lp(a) at or below the median (69.5 nmol/l). No association in subgroups by median baseline Lp(a), LDL-C, hsCRP, or time from qualifying event. Seven of the 23 listed authors are affiliated with Novartis Pharmaceuticals (Wang, Manning, Zhao, Mueller-Edenborn, Nuehrenberg, Lesogor, Cao).
Paraphrase:  This is the document that owns the on-treatment, landmark and subgroup numbers. The 3-month median reduction in the pelacarsen group is stated as 170 nmol/L (a change, not a level) and the median achieved level as 69.5 nmol/L, both in nmol/L. The abstract does not state whether the landmark medians are computed in pelacarsen patients only or in the pooled population compared to placebo, so I cannot say exactly what the "median" splits.
Locators:    Abstract, RESULTS paragraph.
```

```text
URL:         https://www.novartis.com/news/media-releases/novartis-announces-lpahorizon-phase-iii-topline-results-pelacarsen-patients-elevated-lpa-and-established-cardiovascular-disease-cvd
Kind:        primary (Novartis, the trial sponsor, ad hoc announcement dated 4 September 2026; title "Novartis announces Lp(a)HORIZON Phase III topline results for pelacarsen in patients with elevated Lp(a) and established cardiovascular disease (CVD)")
Establishes: The trial "did not meet its primary endpoint" and "Lower lipoprotein (a), Lp(a), levels were achieved with pelacarsen in this study population, which was receiving guideline-directed treatments". No effect size, no Lp(a) reduction, no follow-up. The release does not offer a reason for the miss beyond noting background guideline-directed therapy. Describes pelacarsen as "designed to potently inhibit lipoprotein (a), Lp(a), production at its source", licensed from Ionis.
Paraphrase:  Novartis states the endpoint was missed "in the overall study population". The phrase "in the overall study population" appears in the sentence "the findings did not demonstrate that this translated into reduced cardiovascular risk in the overall study population"; the release does not say anything about subgroups.
Locators:    First paragraph and the Aradhye quote.
Quote:       "Although lower Lp(a) levels were observed with pelacarsen, the findings did not demonstrate that this translated into reduced cardiovascular risk in the overall study population. These are not the results we hoped for" (Shreeram Aradhye, President, Development and Chief Medical Officer, Novartis).
```

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/42250319/   (Cho L, Nordestgaard BG, Chang B, et al. "Concordance of Lipoprotein(a) measurements in mg/dL and nmol/L: Insights from the Lp(a)HORIZON trial." Atherosclerosis 2026 Jul;418:120796, doi 10.1016/j.atherosclerosis.2026.120796)
Kind:        primary on the trial's own measurement (written by trial investigators; includes Novartis employees); abstract only, full text not opened
Establishes: Lp(a) in the Lp(a)HORIZON screening programme was measured with the Roche Tina-quant Lipoprotein(a) Gen 2 mass and molarity assay. Of 14,247 screened, 13,666 had Lp(a) measured in both mg/dL and nmol/L. Converting mg/dL to nmol/L: the Copenhagen General Population Study (CGPS) formula agreed better with measured nmol/L (mean absolute error 16.95; NRMSE 0.21) than the "until recently widely used" factor of 2.5 (MAE 42.30; NRMSE 0.44). At the trial's selection thresholds, accuracy of the converted value was 97% (CGPS) and 92% (factor 2.5) at 70 mg/dL, 94% and 85% at 90 mg/dL.
Paraphrase:  The trial investigators themselves say a fixed factor of 2.5 is a poor conversion; the abstract does not give the CGPS formula. The paper means the trial had both units for each screened patient, but the on-treatment values reported in the releases are nmol/L only.
Locators:    Abstract, METHODS and RESULTS.
```

### The Mendelian randomization estimates

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/29926099/   (Burgess S, Ference BA, Staley JR, et al. "Association of LPA Variants With Risk of Coronary Disease and the Implications for Lipoprotein(a)-Lowering Therapies: A Mendelian Randomization Analysis." JAMA Cardiol 2018;3(7):619-627, doi 10.1001/jamacardio.2018.1470)
Kind:        primary (the Mendelian randomization analysis; authors include Ference, Nordestgaard, Butterworth, Danesh, some with industry ties disclosed including Novartis and Ionis)
Establishes: Abstract read in full; full text not opened (PMC and Europe PMC full text were not retrievable). Unit: mg/dL, Lp(a) "mass concentration". Individual participant data from 5 studies (20,793 CHD cases, 27,540 controls) with external validation from summarized data from 48 studies (62,240 cases, 127,299 controls). All participants were of white European ancestry; mean age 57.5 years; 53% men. Finding: "The association of genetically predicted Lp(a) with CHD risk was linearly proportional to the absolute change in Lp(a) concentration." A 10 mg/dL lower genetically predicted Lp(a) was associated with a 5.8% lower CHD risk (OR 0.942; 95% CI 0.933-0.951), while a 10 mg/dL lower genetically predicted LDL-C was associated with a 14.5% lower CHD risk (OR 0.855; 95% CI 0.818-0.893). Hence "a 101.5-mg/dL change (95% CI, 71.0-137.0) in Lp(a) concentration had the same association with CHD risk as a 38.67-mg/dL change in LDL-C level" (38.67 mg/dL = 1 mmol/L). Conclusion: "Large absolute reductions in Lp(a) of approximately 100 mg/dL may be required to produce a clinically meaningful reduction in the risk of CHD".
Paraphrase:  Outcome is coronary heart disease, not the trial's four-part composite that includes stroke and CV death. The ORs are for lifelong genetic differences, not a 4.7-year treatment. The paper also says that randomized trials of therapies that lowered Lp(a) by 25% to 35% had shown no CHD benefit, which is the prior the trial was meant to answer with a larger reduction.
Locators:    Abstract: Importance, Results, Conclusions.
Quote:       "A 10-mg/dL lower genetically predicted Lp(a) concentration was associated with a 5.8% lower CHD risk (odds ratio [OR], 0.942; 95% CI, 0.933-0.951)".
```

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/31017618/   (Lamina C, Kronenberg F; Lp(a)-GWAS-Consortium. "Estimation of the Required Lipoprotein(a)-Lowering Therapeutic Effect Size for Reduction in Coronary Heart Disease Outcomes: A Mendelian Randomization Analysis." JAMA Cardiol 2019;4(6):575-579, doi 10.1001/jamacardio.2019.1041)
Kind:        primary (the Mendelian randomization analysis; Kronenberg, Medical University of Innsbruck, discloses fees from Kaneka and Amgen)
Establishes: Abstract read in full; full text not opened. Unit: mg/dL. 13,781 individuals from the Lp(a)-GWAS-Consortium (5 mainly population-based studies of European ancestry, all Lp(a) measured in one laboratory) and 20,793 CHD cases / 27,540 controls from the CHD Exome+ consortium; 27 SNPs. "We estimated that the required reduction in Lp(a) effect size would be 65.7 mg/dL (95% CI, 46.3-88.3) to reach the same potential effect on clinical outcomes that can be reached by lowering LDL-C by 38.67 mg/dL." Caveat from the authors: the estimate "is determined by the observed effect estimates of single-nucleotide polymorphisms on Lp(a) concentrations and is therefore influenced by the standardization of the Lp(a) assay used. As a consequence, calculations of the required Lp(a)-lowering potential of a drug to be clinically effective might have been overestimated in the past."
Paraphrase:  Same outcome (CHD), same unit and same LDL yardstick as Burgess, but a smaller requirement. The 65.7 mg/dL figure is the authors' reply to the 101.5 mg/dL figure: they say assay calibration pushes the requirement down. Lamina and Kronenberg do not state a per-10 mg/dL odds ratio in the abstract, so a predicted risk reduction for a given mg/dL cannot be computed from Lamina alone without the full text.
Locators:    Abstract: Results, Conclusions and Relevance.
```

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/21067804/   (Cholesterol Treatment Trialists' Collaboration. Lancet 2010;376:1670-1681, doi 10.1016/S0140-6736(10)61350-5)
Kind:        primary (the meta-analysis of 26 randomized statin trials)
Establishes: Abstract read: rate ratio 0.78 (95% CI 0.76-0.80) for major vascular events per 1.0 mmol/L LDL-C reduction in randomized trials. Used here only as the trial-based counterpart of the genetic LDL slope for my illustrative scaling below. I did not open the full text for follow-up duration.
Locators:    Abstract, Findings.
```

### The other outcome trials (registry records)

All read through the ClinicalTrials.gov v2 API on 8 November 2026; the human pages are `https://clinicaltrials.gov/study/NCT...`.

```text
URL:         https://clinicaltrials.gov/study/NCT05581303   (OCEAN(a)-Outcomes, olpasiran)
Kind:        primary (sponsor's registry record; sponsor Amgen)
Establishes: Phase 3, double-blind, placebo-controlled; 7,297 enrolled (actual); started 2022-12-14; status active, not recruiting; primary completion 2028-03-31 (estimated); verified 2026-10, last posted 2026-10-27. Inclusion: age 18 to <= 85, "Lp(a) >= 200 nmol/L during screening", prior MI and/or coronary revascularization by PCI plus at least one additional risk factor. Primary outcome: time to CHD death, MI or urgent coronary revascularization, "approximately 5 years". Stroke and cardiovascular death are not in this primary endpoint.
Locators:    Eligibility and primary outcomes modules.
```

```text
URL:         https://clinicaltrials.gov/study/NCT07136012   (OCEAN(a)-PreEvent, olpasiran, first events)
Kind:        primary (sponsor's registry record; Amgen)
Establishes: 11,000 (estimated); started 2025-08-22; recruiting; primary completion 2031-10-20 (estimated). Inclusion: age >= 50, "Lp(a) >= 200 nmol/L", multiple ASCVD risk factors and/or evidence of atherosclerosis; excludes prior MI, stroke, TIA, acute limb ischemia, prior or planned arterial revascularization. Primary outcome CHD death, MI or urgent coronary revascularization, up to about 6.2 years. A primary-prevention trial.
Locators:    Eligibility, primary outcomes.
```

```text
URL:         https://clinicaltrials.gov/study/NCT06292013   (ACCLAIM-Lp(a), lepodisiran)
Kind:        primary (sponsor's registry record; Eli Lilly)
Establishes: Phase 3; 17,300 (estimated, includes about 1,700 added in an addendum testing an alternative dosing schema); started 2024-03-05; active, not recruiting; primary completion 2029-03 (estimated). Inclusion "Lipoprotein(a) [Lp(a)] >= 175 nanomoles per liter (nmol/L)"; either established ASCVD with an event or revascularization, or age >= 55 and at risk of a first event. Primary outcome MACE-4 (cardiovascular death, nonfatal MI, nonfatal ischemic stroke, urgent coronary revascularization), "About 4.5 Years".
Locators:    Brief summary, eligibility, primary outcomes.
```

```text
URL:         https://clinicaltrials.gov/study/NCT07157774   (MOVE-Lp(a), muvalaplin; the title does not use that name, the name comes from the Blaha slide deck below and Cleveland Clinic's article)
Kind:        primary (sponsor's registry record; Eli Lilly)
Establishes: Phase 3 oral drug; 10,450 (estimated); started 2025-09-02; recruiting; primary completion 2031-03 (estimated). Inclusion "Lp(a) >= 175 nmol/L"; prior ASCVD event within 10 years or at risk of a first event. Primary outcome MACE-4, "About 5.25 Years".
Locators:    Eligibility, primary outcomes.
```

Not outcome trials, recorded so the writer does not mistake them: pelacarsen's aortic stenosis trial NCT05646381 (phase 2, 502, estimated primary completion 2030-03-12); olpasiran imaging trial NCT07293260; lepodisiran imaging trial NCT07613294. The registry search found no further phase 3 cardiovascular-event trial of an Lp(a)-lowering drug (searched olpasiran, lepodisiran, muvalaplin, zerlasiran/SLN360, pelacarsen, AMG 890, LY3473329, LY3819469; zerlasiran has only a completed phase 2, NCT05537571).

### Phase 2 data on how much each drug lowers Lp(a) (PubMed abstracts)

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/36342163/   (O'Donoghue ML et al., NEJM 2022;387:1855-1864, OCEAN(a)-DOSE, olpasiran; funded by Amgen)
Kind:        primary (phase 2 dose-finding report, abstract)
Establishes: 281 patients with established ASCVD and Lp(a) > 150 nmol/L; median baseline Lp(a) 260.3 nmol/L; median LDL-C 67.5 mg/dL. Placebo-adjusted mean percent changes at week 36: -70.5% (10 mg every 12 weeks), -97.4% (75 mg), -101.1% (225 mg every 12 weeks), -100.5% (225 mg every 24 weeks). Percentages over 100 are a property of the placebo-adjusted estimate.
Locators:    Abstract, Results.
```

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/40162643/   (Nissen SE et al., NEJM 2025;392:1673-1683, ALPACA, lepodisiran; funded by Eli Lilly)
Kind:        primary (phase 2 report, abstract)
Establishes: 320 participants, median baseline Lp(a) 253.9 nmol/L. Placebo-adjusted time-averaged change from day 60 to day 180: -40.8 (16 mg), -75.2 (96 mg), -93.9 percentage points (pooled 400 mg).
Locators:    Abstract, Results.
```

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/39556768/   (Nicholls SJ et al., JAMA 2025;333:222-231, muvalaplin, phase 2; Lilly employees among authors)
Kind:        primary (abstract)
Establishes: 233 participants with Lp(a) >= 175 nmol/L; 12 weeks; placebo-adjusted reductions with the intact-Lp(a) assay of 47.6%, 81.7%, 85.8% at 10, 60, 240 mg/day; with an apo(a)-based assay 40.4%, 70.0%, 68.9%. The assay changes the percentage by up to 17 points.
Locators:    Abstract, Results.
```

```text
URL:         https://pubmed.ncbi.nlm.nih.gov/31893580/   (Tsimikas S et al., NEJM 2020;382:244-255, pelacarsen phase 2)
Kind:        primary (abstract)
Establishes: 286 patients, screening Lp(a) >= 60 mg/dL (150 nmol/L) - the paper itself equates 60 mg/dL with 150 nmol/L, a factor of 2.5. Median baseline 204.5-246.6 nmol/L across groups. Mean percent decrease 72% at 60 mg every 4 weeks and 80% at 20 mg weekly; the monthly 80 mg dose used in HORIZON was not tested in this trial.
Locators:    Abstract, Methods and Results.
```

### Context only

```text
URL:         https://cdn.aglty.io/continuingeducation/uploads/handouts/2026-06-03-sa/3-3_Blaha_Lpa_OL.pdf
Kind:        secondary (conference slide deck by Michael J. Blaha, MD, MPH, Professor of Cardiology and Epidemiology and Director of Clinical Research, Johns Hopkins Ciccarone Center; Blaha is an author of the NEJM Evidence paper, so not independent of the trial; deck dated 5 June 2026, before the result)
Establishes: A pre-result comparison of the trials. Slide 18: "Across 2 key studies, it is estimated that Lp(a) is needed to be reduced by 66-90 mg/dL to reduce ASCVD ~20%." Gives ACCLAIM-Lp(a) as "approximately 12,500 participants ... with 1,276 4-pt MACE events" (registry now lists 17,300, so this is an older design number; the 1,276 events belong to lepodisiran, not HORIZON). Says HORIZON baseline included "~79% with Lp(a) >= 90 mg/dL" and "Mean LDL ~65 mg/dl". Slide 38: "HORIZON - ultimate scientific experiment, but some risky elements that may diminish chance of success".
Paraphrase:  Useful as a dated record that one of the trial's authors expected a roughly 20% reduction to require 66-90 mg/dL. The deck cites its two studies only as graphics, which I could not read as text, so I take "66-90" as Blaha's statement, not as a finding I verified. It does not match Burgess's 101.5 mg/dL; Lamina's 65.7 is at the low end.
Locators:    Slides 17-18, 22-23, 29-30, 38.
```

## Contradictions

1. Sample size. The registry, AHA release, Novartis release and the design paper give 8,323. Cleveland Clinic and HCPLive give 8,350 randomized and 8,322 in the efficacy analysis (4,157 + 4,165 = 8,322). The AHA release says 8,323 "enrolled", from 14,249 screened; the Atherosclerosis concordance paper says 14,247 screened. I could not read the NEJM paper's flow diagram. Use "8,322 analysed" for the denominators of the hazard ratio and "about 8,300" elsewhere, and do not say 8,323 were randomized.
2. Which arm had which count. ACC prints "503 vs. 511 patients, respectively" for pelacarsen vs placebo. Cleveland Clinic and HCPLive give 511 (12.3%) pelacarsen and 503 (12.1%) placebo; 12.3% of 4,157 = 511 and 12.1% of 4,165 = 504, which confirms the order of the other two. ACC's order is an error.
3. P values. Cleveland Clinic's Consult QD table gives P = .69 (full cohort) and P = .82 (>= 90 mg/dL). HCPLive and Healio give P = .76 and P = .99. The confidence intervals fit the second pair: for HR 1.02 with CI 0.90-1.15, z = ln(1.02)/0.0625 = 0.32, P about 0.75; for HR 1.00, P about 1. The Cleveland Clinic P values do not fit their own intervals. Prefer .76 and .99, flag as "reported by HCPLive and Healio", and prefer not to print P at all, since the hazard ratio and interval carry it.
4. What "78%" means. Four different reductions circulate: 78.4% (mean percent change from baseline at 12 months, Cleveland Clinic newsroom and ACC); 77.7% (placebo-adjusted "estimated treatment difference", 95% CI 77.0-78.4, HCPLive, Cleveland Clinic newsroom); -73.9% (time-averaged percent change over the trial, ACC); and 72.7%, which is my own calculation from the median levels (235.6 to 64.4 nmol/L = 171.2 nmol/L; 171.2 / 235.6). The 12-month median-to-median fall (72.7%) is lower than the mean-of-percentages (78.4%), because a mean of individual percentage changes is not the percentage change in the median. Placebo-adjustment by subtraction (78.4 - 3.2 = 75.2) does not give 77.7 either. Do not mix them in one sentence, and name which one is used. Nissen's "78% lower" in the AHA release is the loose form.
5. The conversion factor. Sources give different mg/dL to nmol/L ratios: AHA 70 to 148 (2.11) and 90 to 192 (2.13) and median 109 to 236 (2.17); design paper 70 to ~149 and 90 to ~192; Cleveland Clinic median 108.4 mg/dL to 235.6 nmol/L (2.17); the phase 2 pelacarsen paper 60 to 150 (2.5). The Atherosclerosis paper by the trial's investigators states the factor 2.5 was "until recently widely used" and agreed worse with measured values than the CGPS formula. The ratio of medians of two separately measured quantities is not a conversion of one patient's value.
6. Hazard ratio versus raw percentages in the NEJM Evidence on-treatment result. 380 of the pelacarsen group (9.1%) vs 434 of the placebo group (10.4%) look like a 12% lower crude rate, yet the stated HR is 0.98 (0.85-1.12). The crude counts have different exposure times because the on-treatment analysis censors at discontinuation plus 112 days (Cleveland Clinic article) and 35.1% of pelacarsen patients vs 18.3% of placebo patients stopped early. Do not present 9.1% vs 10.4% as a benefit.
7. Event-count claim in a search summary. An automated search summary attributed "approximately 12,500 participants and 1,276 4-pt MACE events" to HORIZON. In the Blaha deck those figures are for lepodisiran's trial. HORIZON's target was 993 events.
8. Power claims I could not verify. An unsigned explainer on ecgwaves.com (updated 5 October 2026, before the result) argues the trial was underpowered for a 12-18% effect. The ecgwaves arithmetic (about 94% power for a hazard ratio of 0.80, about 73% for 0.85, about 52% for 0.88, with 993 events) matches my own check below. Its further claim that a 70 mg/dL entrant with a 75% fall should expect 12-18% relative risk reduction is the article's own table, not a number from a source paper, and it conflicts with what the Burgess slope gives unscaled (about 27%). It is a pre-result opinion by an unnamed author; do not cite it for any figure.
9. Is the null a contradiction of the genetics, or a smaller dose? The commission asks the piece to settle this from the documents. The documents point both ways, and neither source gives a decisive test:
   - For "smaller dose than 78% suggests": the Burgess requirement (101.5 mg/dL, and its lower confidence limit 71.0) is larger than the derived achieved reduction of roughly 66-84 mg/dL (Numbers, derived). Nissen says pelacarsen "reduces Lp(a) to a lesser degree" than siRNAs, whose phase 2 reductions were -97% to -101% (olpasiran) and -94% (lepodisiran, 400 mg).
   - Against it: the trial's reduction is at or above the Lamina and Kronenberg requirement (65.7 mg/dL; CI 46.3-88.3) by the derived numbers; Blaha, a trial author, expected 66-90 mg/dL to be enough for about 20%; in the landmark analysis the half of patients with the largest 3-month falls (at or above 170 nmol/L) had HR 1.09 (0.92-1.29), and the half with the lowest achieved levels (at or below 69.5 nmol/L) had HR 1.10 (0.93-1.29), so there is no gradient, and the trial's CI (0.90-1.15) excludes a 20% reduction. The investigators themselves frame the neutral result as a failure of the genetic prediction ("unexpected, particularly given the findings of prior observational and Mendelian randomization studies") and offer exposure duration (4.7 years versus lifelong) and low residual risk on background therapy as reasons, which are explanations, not measurements.
   - Both readings are weakened by two facts: the landmark comparison is not randomized (it conditions on 3-month response among patients alive and event-free), and the MR estimates are lifelong, so a 4.7-year treatment effect is expected to be smaller, by an amount that no source quantifies for Lp(a).
10. Endpoint mismatch. The MR papers estimate coronary heart disease; the trial's primary endpoint includes stroke and cardiovascular death. The closest trial components to CHD are MI (HR 0.99, 0.82-1.18; Healio) and the CHD composite with CHD death (HR 0.97, 0.85-1.12; HCPLive); neither shows an effect. Olpasiran's trials also drop stroke from the primary endpoint.
11. LDL. Cleveland Clinic's release reports LDL-C at one year at 62.3 mg/dL on pelacarsen and 71.2 mg/dL on placebo. Pelacarsen arm LDL-C was 8.9 mg/dL lower than placebo at one year (13.3 percentage points by the release's own measure) with no outcome difference. No source I read says how much of that difference comes from the Lp(a) particle's cholesterol being counted in the LDL-C assay, so the writer should report the difference and not explain it.

## Numbers

### The trial

```text
Figure: Primary composite (CV death, nonfatal MI, nonfatal stroke, urgent coronary revascularization requiring hospitalization): 511 of 4,157 (12.3%) pelacarsen vs 503 of 4,165 (12.1%) placebo; HR 1.02, 95% CI 0.90-1.15
Owner:  NEJM, Cho et al. 2026 (doi 10.1056/NEJMoa2610159) - not opened; values via Cleveland Clinic Consult QD, HCPLive, Healio
Scope:  Lp(a) >= 70 mg/dL cohort, efficacy analysis n = 8,322, median follow-up 57 months (4.7 years), first events
```

```text
Figure: Same composite in the Lp(a) >= 90 mg/dL subpopulation: 402 (12.3%) vs 403 (12.3%); HR 1.00, 95% CI 0.87-1.15
Owner:  NEJM, Cho et al. 2026 - not opened; values via Cleveland Clinic Consult QD, HCPLive, Healio
Scope:  78.6% of each arm (about 3,270 per arm; derived); stratification factor at randomization
```

```text
Figure: Median Lp(a) at baseline 235.6 nmol/L (108.4 mg/dL) pelacarsen; 236.2 nmol/L (108.2 mg/dL) placebo
Owner:  NEJM baseline table (not opened); values via Cleveland Clinic Consult QD
Scope:  Medians; assay Roche Tina-quant Lp(a) Gen 2 (Atherosclerosis 2026 abstract)
```

```text
Figure: Median Lp(a) at 12 months 64.4 nmol/L pelacarsen vs 233.4 nmol/L placebo (no mg/dL value published in anything I read)
Owner:  NEJM (not opened); via Cleveland Clinic Consult QD and Healio
Scope:  Medians at month 12
```

```text
Figure: Percent change in Lp(a) from baseline at 12 months: -78.4% pelacarsen, -3.2% placebo, estimated difference 77.7 percentage points (95% CI 77.0-78.4)
Owner:  NEJM (not opened); via HCPLive, Cleveland Clinic newsroom
Scope:  12 months; means of per-patient changes or a model estimate (not stated)
```

```text
Figure: Time-averaged change from baseline over the trial: -73.9% (percent) for pelacarsen (ACC); in nmol/L, 161.2 pelacarsen vs 17.1 placebo (Cleveland Clinic Consult QD)
Owner:  NEJM (not opened); via ACC and Cleveland Clinic Consult QD
Scope:  Time-averaged over the follow-up (average about five years per ACC)
```

```text
Figure: Landmark (3 months, alive and event-free): median reduction 170 nmol/L; median achieved level 69.5 nmol/L. HR 1.09 (0.92-1.29) for reductions at or above the median; HR 1.10 (0.93-1.29) for achieved levels at or below the median
Owner:  NEJM Evidence, Nissen et al. 2026 (doi 10.1056/EVIDoa2600373), abstract read at PubMed 42998055
Scope:  Landmark at 3 months; compared with placebo; not randomized comparison of response groups
```

```text
Figure: On-treatment analysis 380 (9.1%) pelacarsen vs 434 (10.4%) placebo, HR 0.98 (0.85-1.12); uninterrupted treatment 167 (11.0%) vs 204 (10.1%), HR 1.09 (0.89-1.34); total events 644 vs 646, rate ratio 1.00 (0.87-1.14)
Owner:  NEJM Evidence (abstract at PubMed 42998055)
Scope:  On treatment = taking study drug and 112 days after stopping (Cleveland Clinic Consult QD); uninterrupted = no interruption > 60 days. Implied denominators (derived from the percentages): about 1,520 pelacarsen and 2,020 placebo patients had uninterrupted treatment, roughly 37% and 48% of each arm
```

```text
Figure: Adherence: premature discontinuation of trial regimen for any reason 35.1% pelacarsen vs 18.3% placebo; AEs leading to discontinuation 20.6% vs 7.5%; mean exposure 3.5 vs 4.0 years
Owner:  NEJM (not opened); via Cleveland Clinic Consult QD, HCPLive, Healio
Scope:  Whole trial
```

```text
Figure: Components: MI HR 0.99 (0.82-1.18); stroke 1.06 (0.82-1.37); urgent revascularization 1.04 (0.80-1.36); CV death 0.93 (0.73-1.19); three-component MACE 10.2% vs 10.1% HR 1.01 (0.88-1.16); CHD-death composite 9.4% vs 9.7% HR 0.97 (0.85-1.12); all-cause death 5.7% vs 5.9% HR 0.98 (0.82-1.17)
Owner:  NEJM (not opened); via Healio and HCPLive
Scope:  Full cohort, pelacarsen vs placebo
```

```text
Figure: Background: median LDL-C 65.0 (pelacarsen) vs 64.2 (placebo) mg/dL at baseline; at 12 months 62.3 vs 71.2 mg/dL; high-intensity statin 77.1% vs 78.2%; median hsCRP 0.8 mg/L both arms
Owner:  NEJM (not opened); via Cleveland Clinic Consult QD and Cleveland Clinic newsroom
Scope:  Baseline medians; LDL at 12 months as reported (mean or median not stated)
```

```text
Figure: Design: 993 adjudicated primary events to end the study; minimum follow-up 2.5 years; anticipated total duration "approximately 6 years"; primary completion actual 2026-07-16 (first randomization 2019-12-12, about 6.6 years); observed first events 511 + 503 = 1,014
Owner:  Design paper (Am Heart J 2025;287:1-9, abstract); registry record
Scope:  Event-driven; the observed count slightly exceeds the 993 target
```

### Derived by the researcher (not in any source; the writer must label them the same way)

These use only figures above and my stated assumptions. The editor should check the arithmetic, not search for them.

```text
Figure: Pelacarsen median fall at 12 months: 235.6 - 64.4 = 171.2 nmol/L (72.7%); placebo 236.2 - 233.4 = 2.8 nmol/L. Time-averaged placebo-adjusted fall: 161.2 - 17.1 = 144.1 nmol/L
Owner:  Cleveland Clinic Consult QD for the inputs; arithmetic mine
Scope:  nmol/L throughout; no conversion involved
```

```text
Figure: Approximate fall in mg/dL, four ways, each with its assumption:
        (a) 77.7% x 108.4 mg/dL = 84.2 mg/dL (assumes the placebo-adjusted percentage applies to the median baseline in mg/dL)
        (b) 73.9% x 108.4 = 80.1 mg/dL (time-averaged percentage, same assumption)
        (c) 171.2 nmol/L x (108.4 / 235.6) = 78.8 mg/dL (uses the trial's own paired medians, 0.460 mg/dL per nmol/L, as a conversion; the ratio of medians is not a patient-level conversion)
        (d) 144.1 nmol/L x 0.460 = 66.3 mg/dL (time-averaged, placebo-adjusted, same ratio)
        A defensible range is about 66-84 mg/dL. The trial's investigators say the fixed factor 2.5 is inaccurate, and 171.2 / 2.5 = 68.5 mg/dL, which is within that range.
Owner:  Mine, from Cleveland Clinic Consult QD inputs
Scope:  Median patient; assumes the published medians describe a typical patient
```

```text
Figure: Burgess slope: OR 0.942 per 10 mg/dL, log-linear in absolute mg/dL, so the genetically predicted lifelong OR for CHD is 0.942^(X/10): X = 66 mg/dL gives 0.674; X = 79 gives 0.624; X = 84 gives 0.605; X = 101.5 gives 0.545 (equal to the genetic LDL-C OR for 38.67 mg/dL, 0.855^3.867 = 0.546, a check on the arithmetic)
Owner:  Burgess et al. JAMA Cardiol 2018 (inputs); arithmetic mine
Scope:  Lifelong genetic exposure, CHD, European ancestry, mg/dL mass; not a 4.7-year treatment
```

```text
Figure: Illustrative duration scaling (my assumption, not a finding): the CTT trial slope for LDL-C is RR 0.78 per 1.0 mmol/L, the Burgess genetic slope is OR 0.546 per 1.0 mmol/L; the ratio of log effects is ln(0.78)/ln(0.546) = 0.41. Applying 0.41 to the Burgess Lp(a) slope gives an expected trial-length HR of about 0.85 for a 66 mg/dL fall, 0.82 for 79, 0.81 for 84. The trial's 95% CI (0.90-1.15) excludes all three
Owner:  Mine; inputs CTT 2010 (RR 0.78) and Burgess 2018 (OR 0.855 per 10 mg/dL LDL-C)
Scope:  Assumes Lp(a) behaves like LDL-C in the ratio of trial-length to lifelong effect; CTT follow-up duration not verified here; Lp(a) may not behave like LDL-C, which is the hypothesis under test
```

```text
Figure: Power with 993 events: Schoenfeld approximation, two-sided alpha 0.05, 1:1: HR 0.75 gives 99.5%; 0.80 gives 94.0%; 0.85 gives 72.6%; 0.88 gives 52.2%; 0.90 gives 38.2%. With the observed 1,014 events: 99.6%, 94.4%, 73.5%, 53.0%, 38.9%. Halving alpha for the two primary populations (0.025) gives 89.9% for HR 0.80
Owner:  Mine (standard formula); the 993 is from the design paper abstract
Scope:  Assumes equal allocation and proportional hazards; the trial's own planned hazard ratio, alpha split and event rate are unconfirmed (Limits)
```

```text
Figure: Smallest effect the observed event count could detect: with about 1,014 events, 80% power at alpha 0.05 corresponds to HR 0.84; the observed standard error of log HR is 0.0625 (from the CI 0.90-1.15), matching sqrt(4/1014) = 0.0628. The 95% CI excludes a risk reduction larger than about 10% and an increase larger than about 15%
Owner:  Mine; inputs HCPLive/Cleveland Clinic CI
Scope:  Full cohort
```

### The genetic yardsticks, each in its own unit

```text
Figure: Burgess 2018: 101.5 mg/dL (95% CI 71.0-137.0) of lower Lp(a) = the genetic CHD effect of 38.67 mg/dL (1 mmol/L) lower LDL-C; slope OR 0.942 (0.933-0.951) per 10 mg/dL
Owner:  Burgess et al., JAMA Cardiol 2018;3:619-627
Scope:  Mass concentration, mg/dL; European ancestry; CHD; individual-level data from 5 studies, summarized data from 48
```

```text
Figure: Lamina and Kronenberg 2019: 65.7 mg/dL (95% CI 46.3-88.3) for the same LDL-C yardstick (38.67 mg/dL)
Owner:  Lamina C, Kronenberg F, JAMA Cardiol 2019;4:575-579
Scope:  mg/dL, one-laboratory assay in the Lp(a)-GWAS Consortium, European ancestry; the authors say assay standardization changes the figure
```

### The pending trials, in each registry's own unit

| Trial (NCT) | Drug, sponsor | Enrolment (status) | Lp(a) entry threshold | Population | Primary endpoint | Primary completion (registry) |
|---|---|---|---|---|---|---|
| Lp(a)HORIZON (NCT04023552) | pelacarsen, Novartis | 8,323 (completed) | >= 70 mg/dL (~148-149 nmol/L); median 236 nmol/L | prior MI, ischemic stroke or symptomatic PAD | CV death, MI, stroke, urgent revascularization | 2026-07-16 (actual) |
| OCEAN(a)-Outcomes (NCT05581303) | olpasiran, Amgen | 7,297 (active, not recruiting) | >= 200 nmol/L | prior MI and/or PCI plus another risk factor | CHD death, MI, urgent revascularization | 2028-03-31 (estimated) |
| ACCLAIM-Lp(a) (NCT06292013) | lepodisiran, Lilly | 17,300 estimated (active, not recruiting) | >= 175 nmol/L | established ASCVD or age >= 55 at risk of first event | CV death, MI, ischemic stroke, urgent revascularization | 2029-03 (estimated) |
| MOVE-Lp(a) (NCT07157774) | muvalaplin (oral), Lilly | 10,450 estimated (recruiting) | >= 175 nmol/L | prior ASCVD event in 10 years or at risk of first event | same MACE-4 | 2031-03 (estimated) |
| OCEAN(a)-PreEvent (NCT07136012) | olpasiran, Amgen | 11,000 estimated (recruiting) | >= 200 nmol/L | age >= 50, no prior event | CHD death, MI, urgent revascularization | 2031-10-20 (estimated) |

Phase 2 Lp(a) lowering of the same drugs (placebo-adjusted percent, nmol/L baselines): olpasiran -97.4% to -101.1% at week 36 in the 75-225 mg groups from median 260.3 nmol/L; lepodisiran -93.9 percentage points pooled 400 mg (day 60-180) from median 253.9 nmol/L; muvalaplin -81.7% and -85.8% (intact-Lp(a) assay) or -70.0% and -68.9% (apo(a) assay) at 60 and 240 mg/day. The trials' thresholds are in nmol/L and HORIZON's in mg/dL; the approximate nmol/L equivalents are stated in the AHA release and the design paper, not mine. A reduction of 97% from a baseline of 260 nmol/L is about 252 nmol/L, against about 171 nmol/L for pelacarsen from 236 nmol/L; those are arithmetic from medians in different assays and should not be used as a head-to-head. What fraction of HORIZON patients had Lp(a) >= 200 or >= 175 nmol/L is not in any document I read.

## Limits

- The NEJM paper and supplement were not read. Every trial number is therefore secondhand, from the Cleveland Clinic article (which reproduces the paper's tables), HCPLive, Healio, the Cleveland Clinic newsroom, the AHA and ACC; the NEJM Evidence figures come from the PubMed abstract. The writer should cite the NEJM paper (doi 10.1056/NEJMoa2610159) only for claims that the secondary documents attribute to it, and say the paper itself could not be opened. The AHA slides were not located.
- Trial power assumptions: not established. The design paper gives 993 events, 2.5 years minimum follow-up and about 6 years anticipated duration, but its assumed hazard ratio, power, alpha and event rate sit in full text I could not open (sciencedirect.com 403). A search summary claimed ">90% power for HR ~0.80 overall and 0.75 for >= 90 mg/dL" and "about 80% time-averaged Lp(a) reduction predicted"; neither is confirmed by a document I read. The registry has no power statement and no protocol. The piece can state the 993-event design and my own power arithmetic labelled as such; it cannot state the trial's assumed effect.
- On-treatment Lp(a) in mg/dL, in either arm: not published in anything I read. The 12-month and landmark values are in nmol/L only. Every mg/dL figure for the achieved reduction is derived, with the range 66-84 mg/dL depending on the method; the commission's instruction not to convert without a source's basis means the piece should put the trial's numbers in nmol/L, the genetic estimates in mg/dL, and state the derived mg/dL range only with its basis (the trial's own paired medians, or the 2.5 factor that the trial's investigators call inaccurate).
- Both Mendelian randomization papers were read in abstract only (PubMed); full text via PMC and Europe PMC was not retrievable, so their assays, cohort units and sensitivity analyses are not checked. Lamina and Kronenberg give no per-10 mg/dL slope in the abstract.
- The Kaplan-Meier curve, forest plot and Lp(a)-over-time figure in the NEJM paper were not seen, so I cannot describe their content or confirm they exist as figures. No data on the shape of the event curves, hazard proportionality, or event rate per arm over time.
- Per-protocol, adherence and dropout: covered by the on-treatment, uninterrupted-treatment and discontinuation figures above. Not covered: how many pelacarsen patients had an achieved Lp(a) in mg/dL above or below any particular value; any analysis restricted to patients with Lp(a) above the olpasiran and lepodisiran thresholds (200 and 175 nmol/L); any analysis of the supervised-dosing six-month period after March 2023 (reported only as a fact).
- Statements on why: Nissen (study chair, senior author) and Cho gave reasons (lifelong vs 4.7-year exposure; low residual risk on intensive background therapy; low event rate; potency of siRNAs). Novartis's release gives no reason. Outside cardiologists Deepak L. Bhatt (Mount Sinai) and Jared A. Spitz (Inova) are on the record, but Bhatt spoke in September before the data and Spitz discloses being a site investigator for an Amgen Lp(a) trial. I did not find a statement from Ionis I could open (ir.ionis.com returned 403; a search summary quoted its CEO, unverified, so do not use it). I did not find an independent statistician's critique of the primary analysis or an NEJM editorial.
- No outside cardiologist or statistician was found who has read the full NEJM paper and challenged the primary analysis. All commentary I read is dated 7 November or earlier.
- Time-limited: all registry dates are estimates as of the verification dates stated (August to October 2026) and change.
- Closing note on the commissioned angle: the angle ("whether the trial tested a smaller dose of the hypothesis than the 78% suggests") is not supported cleanly. Using the trial's own median numbers, the reduction is at or above the Lamina and Kronenberg requirement, below the Burgess central estimate, and the half of patients with the largest reductions did no better (landmark HR 1.09), while the trial CI excludes a 20% reduction. What the documents leave open is the duration question: the genetic estimates are lifelong and no source quantifies what a 4.7-year exposure should deliver for Lp(a). The piece should not claim the null is a contradiction of the genetics, or that the dose was too small, as settled. It can show, with the labelled arithmetic, that the shortfall against Burgess's central estimate is about 17-35% of the required fall (66-84 versus 101.5 mg/dL) and that no source resolves the duration question.

## Source assets

```text
Asset: Primary-endpoint Kaplan-Meier figure (cumulative incidence of the four-part composite, pelacarsen vs placebo) and the forest plot of subgroups in the NEJM paper (doi 10.1056/NEJMoa2610159)
Shows: Whether the curves separate at any point; the investigators' phrase for the curves in the AHA coverage is "right on top of each other" (Spitz, Healio), which I did not see for myself
Crop:  Axes, the number-at-risk table, the hazard ratio and interval; omit the journal furniture. NOT confirmed to exist and NOT viewed; NEJM is paywalled (403) and its figures are copyrighted by the Massachusetts Medical Society. Capture under the source-assets spec is not permissible without a legitimate open version; I found none. Do not plan around this asset.
```

```text
Asset: Tables in the Cleveland Clinic Consult QD article: the baseline-characteristics table and the primary-result table (https://consultqd.clevelandclinic.org/lipoproteina-reduction-with-pelacarsen-has-no-impact-on-cardiac-events)
Shows: Per-arm baseline Lp(a) in both units and the two hazard ratios side by side
Crop:  The two data tables only; omit advertising and page furniture. These are HTML tables copied from the NEJM paper by a participating institution, so are secondary; their P values are inconsistent with the confidence intervals (Contradictions item 3). Better to rebuild as a chart or table in the article from the numbers than to capture.
```

```text
Asset: Registry records for the pending trials on ClinicalTrials.gov (NCT05581303, NCT06292013, NCT07157774, NCT07136012): the Eligibility and Primary Outcome sections of each page
Shows: The Lp(a) entry thresholds in nmol/L, the endpoint definitions and the estimated primary completion dates, from the sponsors' own records
Crop:  The inclusion line with the Lp(a) threshold, the primary outcome line and the "Primary Completion" date for each trial; omit unrelated sections. The records are US National Library of Medicine public records; `nb asset web` on the study page is a plausible method, but the page is JavaScript-rendered and I did not test a capture, and dates will change on update, so record the capture date. A comparison table the article builds itself from the registry fields is the safer route and it is already set out above.
```

```text
Asset: Open-access figures in the design paper (Am Heart J 2025) and the Atherosclerosis concordance paper (2026), for example the trial schema or the Bland-Altman plots of mg/dL against nmol/L
Shows: The trial schema, or how far a mg/dL value converted by a fixed factor departs from the measured nmol/L value
Crop:  The plot or schema only, with its axes and legend. Europe PMC metadata lists the license of both as CC BY, but sciencedirect.com returned 403 and I did not see either figure, so I do not know what they show; verify the license on the publisher page before any capture.
```

AHA release images (an organ illustration, Nissen's portrait, the Scientific Sessions logo) carry the AHA/ASA Multimedia Materials Usage Policy and show no data; not useful.

## Discarded

```text
https://www.statnews.com/2026/11/07/aha-conference-news-novartis-lp-a-pelacarsen-heart-disease-trial-mystery/: STAT+ paywall; only the first two paragraphs readable, and they repeat the headline finding without numbers.
https://www.tctmd.com/news/full-lpahorizon-results-affirm-lack-pelacarsen-benefit-secondary-prevention: 403 on fetch; not read.
https://ir.ionis.com/node/35106: 403 on fetch; not read.
https://ecgwaves.com/articles/zeus-and-lpa-horizon-trials-why-ziltivekimab-and-pelacarsen-failed: unsigned, pre-result (updated 5 October 2026), secondary commentary; its power arithmetic matches mine but the 12-18% expected-benefit table is its own; read through a summary only.
https://www.drozdogan.com/en/should-elevated-lp-a-be-treated-the-level-fell-but-the-risk-did-not/: personal site of a professor; does not quote the design paper's power statement; no figure used.
https://thepeptidelist.substack.com/p/the-lpa-number-fell-the-cardiovascular: Substack; surfaced only in a search summary (which also contained an unrelated niacin figure); not opened and not relied on.
https://www.healio.com/news/cardiology/20260908/not-the-results-we-hoped-for-lpalowering-drug-pelacarsen-fails-to-reduce-cv-events: read; repeats the Novartis topline release plus Bhatt's pre-data comment; adds nothing the Novartis release does not own, except Bhatt's remarks (Deepak L. Bhatt, MD, MPH, MBA, Icahn School of Medicine at Mount Sinai; reports research funding from Novartis).
https://www.clinicaltrialsregister.eu/ctr-search/trial/2019-001076-11/GB: fetched but returned a 244-byte stub; no content.
https://www.nejm.org/doi/full/10.1056/NEJMoa2610159, https://evidence.nejm.org/doi/full/10.1056/EVIDoa2600373, https://www.sciencedirect.com/science/article/pii/S0002870325001012: 403 (gated); the first two are recorded above as the documents that own the numbers, not read.
https://pmc.ncbi.nlm.nih.gov/articles/PMC6487909/ and /PMC6481553/: returned a 21 KB bot-check page, not the paper; abstracts via PubMed used instead.
https://www.epocrates.com/online/article/first-major-trial-of-lp-a-lowering-fails-to-cut-cv-events, https://www.pharmacytimes.com/view/pelacarsen-ziltivekimab-miss-cv-end-points-what-to-know, https://www.lipid.org/resource/top-line-results-from-the-phase-3-lpahorizon-trial/: appeared in search results; not opened, since they could only repeat the Novartis topline or the presentation.
A search summary's claim that the Cleveland Clinic coverage said "at the usual conversion factor of about 2.5 ... around 70 mg/dL": that was the summariser's own calculation, which it flagged as such; not from any document.
```
