# Editorial review: feature/pelacarsen-lpa-horizon (editor/01)

## Correct

Thesis, from the draft alone: pelacarsen lowered Lp(a) by roughly the absolute amount one Mendelian randomization estimate requires for a clinically meaningful coronary benefit, and Lp(a)HORIZON ruled that benefit out over 4.7 years. The claims under it:

1. Converted to mg/dL, the fall was 66 to 84 mg/dL. That reaches Lamina and Kronenberg's 65.7 and is 17 to 35 percent short of Burgess's 101.5.
2. The genetic papers' prediction for a fall of that size is outside the trial's interval (0.90 to 1.15), and the landmark and on-treatment analyses show no gradient.
3. Duration is Nissen's explanation, and no source measures it.
4. The pending trials enrol above HORIZON's threshold with drugs that lowered Lp(a) more in phase 2.

I recomputed every figure from the handoff against the opened sources.

- **Conversion.** 235.6 − 64.4 = 171.2. 161.2 − 17.1 = 144.1. 108.4 / 235.6 = 0.4601. The products are 84.2, 78.8 and 66.3. Shortfalls against Burgess are 17.0% and 34.7%. Interval membership is as printed. The inputs match Consult QD's baseline table and results text and the Cleveland Clinic newsroom's 77.7%. I kept all three rows. They use the trial's own percentage, its own paired medians or both, so no conversion factor comes from outside the sources, and the page says the ratio of medians is not a patient-level conversion. The lowest value, 66.3, clears 65.7 by only 0.6 mg/dL, and the headline depends on it. Two source-given equivalences also keep the time-averaged value above 65.7: 66.6 on the AHA's 109/236 and 67.7 on the design paper's 70/149. The discredited factor of 2.5 would give 57.6. I judged the headline supportable on the trial's own medians.
- **The 0.41 trial-length discount: cut.** ln(0.78)/ln(0.546) = 0.41 is correct. Its premise is that Lp(a)'s ratio of treatment effect to lifelong effect equals LDL cholesterol's, and no source states that. Opening Burgess past the quoted passage showed a sourced route to the same prediction. His conclusion reads: "The clinical benefit of lowering Lp(a) is likely to be proportional to the absolute reduction ... approximately 100 mg/dL may be required to produce a clinically meaningful reduction in the risk of CHD similar in magnitude to what can be achieved by lowering LDL-C level by 38.67 mg/dL." Lamina and Kronenberg say "the same potential effect on clinical outcomes that can be reached by lowering LDL-C by 38.67 mg/dL." The CTT abstract gives RR 0.78 per 1 mmol/L for major vascular events, over a median follow-up of 4.8 years (statin against control) and 5.1 years (more against less intensive). The prediction is now stated as the genetic papers' own translation: 0.78^(x/101.5) gives 0.850 at 66.3 and 0.814 at 84.2. These are numerically identical to the old 0.81 to 0.85, because 0.942^10.15 = 0.546. The page no longer depends on a discount the article invented. The "treatment" band in Fig. 2 now runs from 0.78, where Lamina and Kronenberg's requirement sits, to 0.85, and was redrawn on the existing log scale (x = 250.4 + 385.5·ln HR).
- **The 0.21 to 0.27 bound: cut.** ln(0.90)/ln(0.674) = 0.267 and ln(0.90)/ln(0.605) = 0.209 are correct. The bound measures a "share of the lifelong log effect" against the 0.41 for LDL cholesterol, and inherits the same unsupported premise. In its place, the duration section states the sourced fact underneath it. The statin trials behind the 0.78 ran about five years, close to HORIZON's 4.7, so Nissen's explanation needs Lp(a)'s benefit to arrive more slowly than LDL cholesterol's. No source measures that. The heading now carries this step.
- **Schoenfeld power: cut.** sqrt(993/4) = 15.76. HR 0.80 gives Φ(1.556) = 94.0% and HR 0.85 gives Φ(0.601) = 72.6%, so the arithmetic is right. It assumes a two-sided alpha of 0.05 for the overall population. The design abstract says the trial used multiplicity control across two primary populations, and no opened source gives the alpha split. Halving alpha would give 89.9% for HR 0.80. The sentence now reports the 993-event stopping rule and that the design abstract does not state the effect the trial was powered to detect. The confidence interval already shows what was excluded.
- **Phase 2 absolute falls: cut.** 0.939 × 253.9 = 238 and 0.974 × 260.3 = 254. They apply placebo-adjusted mean percentages to medians from different assays and set the result against a placebo-unadjusted median difference. The record warns against using these as a head-to-head comparison. They are replaced by the three sourced percentages: 94%, 97%, and pelacarsen's 77.7% from its 12-month result. The caveat on assays, populations and time points stays.
- **Headline.** "As far as one genetic study required" holds against the record and against Lamina and Kronenberg's wording ("required reduction"), with the margin noted above. "Left heart events unchanged" can be parsed as "left-heart events", and the primary endpoint includes stroke and cardiovascular death, so it now reads "did not reduce cardiovascular events".
- **Citations.** I opened every href as printed. The PubMed and registry pages need a browser: plain curl gets a cookie wall from PubMed and a JavaScript shell from ClinicalTrials.gov. I opened them in headless Chromium and through the registry API. All land on the right document, and every locator holds. Four breaks, all fixed:
  - The 4.7-year follow-up in the opener was cited only to the AHA release, which does not give it. I added Consult QD ("median follow-up of 4.7 years") and renumbered the sources by first appearance.
  - Nissen's quote card cut his sentence at "protected." without marking the cut. Consult QD continues "...protected from Lp(a)-related cardiovascular events." I restored the full sentence.
  - The source note on NCT07157774 said the MOVE-Lp(a) name does not come from the registry. The registry record carries the acronym MOVE-Lp(a), so I removed the note.
  - Fig. 1's aria-label said "derived four ways" for three values. I corrected it.
- **Spitz.** Healio's box continues past the quoted line: "I think that the olpasiran (Arrowhead/Amgen) trial will be next." I added that he named olpasiran, which ties his quote to the OCEAN(a)-Outcomes sentence that follows. His Amgen disclosure stays beside the quote.
- **`data-nb-kind`.** Every value holds. The AHA release, both Cleveland Clinic pages and Healio are secondary. The abstracts and registry records are primary. The page claims no independent corroboration it lacks.

## Reads well

- **Cut because it said nothing or rested on the cut steps.** "That predicts a hazard ratio of 0.81 to 0.85, and presumes Lp(a) behaves like LDL cholesterol, which is the hypothesis under test." It went with the discount. The 0.21 to 0.27 sentence went because a reader could not use it without the construct behind it.
- **Lifted.** "Found 2.5 matched measured nmol/L worse" now names "the fixed factor of 2.5". "The on-treatment analysis, which handles ..." now says what the analysis counts, which is events on the drug and for 112 days after, and why it matters. "Predicts 0.85 to 0.81" now says what it predicts.
- **Dek.** The old dek gave the same numbers as the headline and the opener. The new one names the trial and adds the finding the headline leaves out, that the trial ruled out the predicted benefit. It does not open with a framing prepositional phrase and is not a comma triad. The headline avoids the "X does A and B the rest" shape.
- **Edges.** I read every first and last sentence on its own. The closer is a dated registry fact and stays. The "miss at that depth ... hit to the size of the fall" sentence is the piece's own inference, and the handoff flagged it. I kept it because the comparison it rests on (higher entry, deeper phase 2 lowering, similar follow-up) is now sourced on the page. I found no voice-guide borrowings or briefing leaks.

## The experience

The page renders at 390 px and 1280 px in light and dark with no horizontal overflow. In Fig. 2 the treatment band now begins at the 0.8 tick and its two-line label clears the lifelong label at phone width. Fig. 1 is unchanged apart from its aria-label. Both tables, the stat strip and the quote card render correctly. The piece gives the reader something its sources do not. It puts the trial's nmol/L result in the genetic papers' mg/dL unit. It then turns those papers' own LDL-cholesterol yardstick into the benefit they predicted for a fall of that size, which the trial's interval excludes. That lines up with the writer's original-work sentence, minus the discount step, which is now carried by sourced links.

## Edits

- Headline and nb-meta title: "Cutting Lp(a) as far as one genetic study required did not reduce cardiovascular events".
- Dek, both copies: rewritten to name Lp(a)HORIZON and say it ruled out the benefit tied to a fall that size.
- Opener: added the Consult QD citation for the 4.7-year follow-up.
- Stat strip: "median Lp(a) fall" relabelled "fall in pelacarsen's median Lp(a)".
- Conversions paragraph: "the fixed factor of 2.5".
- Fig. 1 aria-label: "three ways".
- Interval heading: "...excludes the benefit the genetic estimates predict".
- Interval paragraph: the 0.41 discount replaced by Burgess's and Lamina and Kronenberg's LDL-cholesterol equivalence plus CTT's 0.78 (five-year median), giving 0.85 to 0.81 and 0.78.
- Fig. 2: treatment band moved to 0.78 to 0.85 and relabelled "Treatment prediction". Aria-label and caption updated, with Burgess and CTT cited.
- Power sentence replaced with the 993-event stopping rule and the unstated assumed effect.
- On-treatment sentence rewritten to define the analysis.
- Duration heading: "Nissen's lifelong explanation needs Lp(a) to act more slowly than LDL".
- Quote card: Nissen's sentence restored in full.
- Duration paragraph: 0.21 to 0.27 bound cut. Statin-trial duration and "no source measures how fast" added. "siRNA" spelled out.
- Pending-trials paragraph: derived 240 to 255 nmol/L cut, pelacarsen's 77.7% put beside the phase 2 percentages, "time points" added to the caveat.
- Spitz: "and named olpasiran's as next". "In patients with a prior event" cut for length.
- Sources: renumbered by first appearance (Consult QD is now 2, Burgess 3, Lamina and Kronenberg 4). Wrong note on NCT07157774 removed.
- Ran `nb stamp`: 1,199 words, 17 sources, 5 min. `nb check`: BLOCK 0, WARN 0, PUBLISHABLE.

Decisions made without the orchestrator:

- I treated the genetic papers' own LDL-cholesterol equivalence, together with CTT, as source support for the treatment-scale prediction. Because the numbers match the cut discount exactly, the change is to what supports the figure, not to the figure. If the orchestrator reads "cut, rather than leave labelled" as requiring no treatment-scale prediction at all, the band and the "predicts ratios of 0.85 to 0.81" sentence can come out. The argument would then rest on Lamina and Kronenberg's requirement mapping to 0.78.
- I kept the headline on a 0.6 mg/dL margin over Lamina and Kronenberg's estimate, as computed from the trial's paired medians.
- `nb-meta` still records the writer's model (claude-sonnet-5-5). I left it unchanged.

## Decision

Approve. The argument held once the unsupported steps came out, and every remaining figure traces to an opened source or to arithmetic shown on the page.
