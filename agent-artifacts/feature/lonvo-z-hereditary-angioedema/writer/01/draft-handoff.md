# Draft handoff: feature/lonvo-z-hereditary-angioedema (writer 01)

## Original work

The article puts HAELO's endpoint on one axis with five placebo-controlled prophylaxis trials (plus a derived C1-INH SC point), each with its counted window, arm sizes and prior-prophylaxis share, shows that lonvo-z's 87% overlaps lanadelumab's 87% and garadacimab's 89.2%, and shows that Intellia's ACAAI 81% and 89% are within-patient figures that cannot sit on that axis, with the 89% resting on 10 patients at month 36 and 4 at month 41 or later.

## Proof

`nb check` (exact brief command, links included): BLOCK: 0, WARN: 0, PUBLISHABLE. 1,199 words (band 1,200), 16 sources, 5 min.
Every visual was rendered with `nb preview` and captured with Playwright at 390 px and 1100 px, light and dark. No page-level horizontal overflow. The table scrolls inside its card on a phone, by design. Fig. 2 and Fig. 3 are light-paper PNGs in dark mode (engine behaviour).

## Decisions and open questions

- Source asset not captured. `nb asset image` on the slide 31 JPG returned HTTP 403 from sec.gov (default Python user agent). I did not try to get around the block. Fig. 3 is instead an `nb chart` (chart-2.py) built from the record's verified figures: at-risk counts exact (93, 81, 71, 24, 16, 10, 4), attack rates approximate and labelled so in the chart and caption (3.3, about 0.3, 0.2, 0.1, 0.0, as read from slide 31 by the researcher). An editor who wants the slide itself needs a fetch that sec.gov accepts.
- The slide 29 follow-up conflict (median vs mean 7.6 months) is stated in the text rather than resolved.
- "Many of whom had stopped it" (placebo patients on prophylaxis): 71% of all 80 were on prophylaxis at entry, the placebo arm's own share is not in the record.
- The reading that the 81% looks smaller because its baseline was measured on prophylaxis is the researcher's inference (contradiction 6). The article labels it as the article's inference.
- Garadacimab is plotted with the FDA label analysis (89.2%). The Lancet's 87% (58 to 96) is in the text, not the chart.
- COMPACT's 87% is derived from the label's 0.52 and 4.03 and drawn as an open marker with no interval. Dashes in the table are figures the record does not give (APeX-2 attack-free, COMPACT prior prophylaxis).
- Fig. 2 and the table use primary endpoints only. Sebetralstat is in Fig. 1 and one sentence, not in the comparison, because KONFIDENT has no attack-rate endpoint.
- The 14 November oral sessions are not reported, and I dropped the sentence that mentioned them for length.
- Dropped for the 1,200-word limit: the August 2026 HLA allele finding, the infusion-reaction and any-adverse-event rates, and the 8 Sep BLA/PDUFA dates.
- nb-meta model is "Claude Sonnet 5.5", as the brief gives it.

## Display text checked

Headline, dek, subheads against the record. 87%, 0.26 v 2.10, 81%, 89%, 24-week window, 5 and 14 November dates, 35 and 93 patients all match. The dek in nb-meta and the rendered dekline are identical (the proof checks this). Recent-pattern habits avoided: no prepositional-frame or ", and" dek, no "arithmetic", one figure-led heading at most, the opener is the drug and its trial result, and the close states the 24-week and 10-patient counts and not a pending dataset.
