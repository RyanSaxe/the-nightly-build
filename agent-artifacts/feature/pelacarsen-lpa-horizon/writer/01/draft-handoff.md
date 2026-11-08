# Draft handoff: feature/pelacarsen-lpa-horizon (writer 01)

## Original work

The article converts Lp(a)HORIZON's nmol/L fall into the mg/dL unit of the two Mendelian randomization estimates (66.3 to 84.2 mg/dL, derived three ways with the basis shown), then runs Burgess's per-10 mg/dL slope forward to the hazard ratio each fall predicts, with and without a trial-length discount, and sets those predictions against the trial's confidence intervals; none of the sources does either step.

## Proof

`nb check` with links, the exact command in the brief: BLOCK 0, WARN 0, PUBLISHABLE. 1,190 words (strict band 600 to 1,200, and the count includes the sources list and SVG labels, which is why the prose is tight), 17 sources, 5 min read. Looked at both figures, both tables, the stat strip and the quote card at 390 px and 1280 px in light and dark: no horizontal overflow. On a phone Table 1's third column (the calculation) and Table 2 scroll sideways; the mg/dL result column is placed second so it stays visible.

No warning left on purpose.

## Decisions made without asking

1. Followed "Decision after researcher/01": the piece reports that the fall reached Lamina and Kronenberg's 65.7 mg/dL and was 17 to 35 percent short of Burgess's 101.5, that no gradient appears by size of fall, that the primary interval excludes the predicted effect, and that duration is Nissen's explanation with no source quantifying it. Neither "contradicts the genetics" nor "dose too small" is stated as settled.
2. Table 1 uses three of the researcher's four conversions. I dropped the time-averaged 73.9% x 108.4 = 80.1 mg/dL row because the strict 1,200-word cap counts the sources list and the ACC source it needed. The range 66.3 to 84.2 mg/dL is unchanged, because 80.1 sits inside it. The ACC story is therefore not cited; its reversed arm counts were never used.
3. Headline "Lowering Lp(a) as far as one genetic study required left heart events unchanged": chosen over "what genetics asked for" because the derived fall is 17 to 35 percent short of Burgess, so only the Lamina and Kronenberg claim holds for every derived value. The dek names both estimates. It avoids a framing opener, the "does A and B" shape and the comma triad.
4. Trial figures are cited to Cleveland Clinic Consult QD, with the on-treatment, landmark and design numbers cited to the PubMed abstracts that own them. P values are not printed. The NEJM paper is not cited; the article says its figures come from Cleveland Clinic's summary of the published paper, and the CC source carries a `data-nb-note` saying NEJM could not be opened.
5. HCPLive and the CHD-death composite (HR 0.97) are not used. Heart attack alone (HR 0.99, Healio) stands for the coronary endpoint mismatch.
6. LDL-C and the on-treatment Lp(a) trial detail beyond what is on the page (placebo-arm change, adherence) are reduced to the 35.1% vs 18.3% early-discontinuation figures attached to the on-treatment analysis, and Nissen's background-therapy and siRNA-potency explanations in one sentence. Word cap.
7. Phase 2 percentages are used only to give an implied absolute fall for olpasiran 75 mg (97.4% of 260.3) and lepodisiran pooled 400 mg (93.9% of 253.9), about 240 to 255 nmol/L, with the researcher's caveat (different assays and populations). The 97.4% to 101.1% olpasiran range is not quoted, since values above 100% are an artifact of placebo adjustment.
8. The OCEAN trials' endpoint is labelled "Coronary" and explained in the Table 2 caption; HORIZON's registry follow-up (about 4 years) is shown beside the registry's own figures for the others, with HORIZON's actual median 4.7 years in the prose.
9. Table 2 entry for HORIZON is 148 nmol/L, the AHA's conversion of 70 mg/dL, and is labelled as such only by the AHA citation; the other four are the registries' own nmol/L.

## Arithmetic for the editor to check (all derived here, labelled "derived here" or "an assumption" on the page)

- Table 1: 0.777 x 108.4 = 84.2; 171.2 x (108.4/235.6 = 0.460) = 78.8; 144.1 x 0.460 = 66.3. 171.2 = 235.6 - 64.4; 144.1 = 161.2 - 17.1.
- Burgess slope: OR = 0.942^(x/10); 66 mg/dL gives 0.67, 84 gives 0.60.
- Discount 0.41 = ln(0.78) / ln(0.855^3.867) with 0.855^3.867 = 0.546; applied it gives HR 0.85 (66.3 mg/dL) and 0.81 (84.2). The 0.41 is an assumption that Lp(a) behaves like LDL-C, stated as such.
- Bound in the duration section: ln(0.90) / ln(OR) = 0.27 (66.3 mg/dL) and 0.21 (84.2). That is the share of the lifelong log effect that would have to be delivered in 4.7 years for the trial's interval edge (HR 0.90) to be compatible with the genetic slope. It is the piece's own inference, flagged as derived. It uses the Burgess slope only; Lamina and Kronenberg's smaller requirement implies a steeper slope, so Burgess is the cautious choice (not stated on the page, cut for length).
- Power (Schoenfeld, 993 events, two-sided alpha 0.05, 1:1): HR 0.80 gives 94.0%, 0.85 gives 72.6%, printed as 94% and 73%. The trial's own assumed effect was not available, and the page says the design abstract omits it.
- 17 to 35 percent short of Burgess: 1 - 84.2/101.5 = 17.0%; 1 - 66.3/101.5 = 34.7%. Two of three derived values (78.8, 84.2) are inside Burgess's interval of 71.0 to 137.0; all three are inside Lamina and Kronenberg's 46.3 to 88.3.
- Phase 2 implied fall: 0.939 x 253.9 = 238; 0.974 x 260.3 = 254, printed as roughly 240 to 255 nmol/L.

## Open evidence or voice questions

- NEJM text and supplement were never opened. The 77.7% treatment difference is from the Cleveland Clinic newsroom release, whose own subtraction (78.4 - 3.2) does not equal it; the page uses it only as an input and calls the products derived.
- The NEJM Evidence abstract does not say whether the landmark medians (170 nmol/L fall, 69.5 nmol/L achieved) split pelacarsen patients alone or the pooled population. The page states the thresholds and says the rows condition on three-month response and are not randomized; it does not say who is split.
- Spitz discloses being a site principal investigator for an Amgen Lp(a) trial; the page says so beside his quote, and does not identify which trial he means by "the other secondary prevention trial."
- The statement that a miss at the pending trials' depth "would point to duration or the genetics, and a hit to the size of the fall" is the piece's own inference, not a source's claim. Cut it if the editor judges it unsupported.
- No source asset or chart script was used: the NEJM figures could not be opened, and both visuals are inline SVG drawn for the article (both plot the cited or derived numbers exactly; the bands in Fig. 2 are the derived predictions).
