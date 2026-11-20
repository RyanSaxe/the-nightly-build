# Editorial review: feature/top500-ageing-installed-base (editor/01)

## Correct
Thesis, from the draft alone: entries now stay on the TOP500 for years because the No. 500 bar has grown 5–25% a year since 2020 against 30–69% in 2011–2019. Under it: (1) the list has aged by count (median six editions, 138 entries five years or older) while the capacity stays young (61.5% of Rmax from entries under two years old); (2) survival arithmetic on the bar explains it, and the cohorts match (3–17% five-year survival outside China for 2012–2017 cohorts, 52–72% for 2020–2021); (3) the November 2026 newcomer low is partly China's exit, and neither the timing reading nor the AI-factory suggestion can be settled from the files.

Each figure was recomputed from series.csv and cohort_survival.csv: bar growth (2011 +63.7% to 2019 +30.5%; 2020–2026 +4.8% to +25.2%), total Rmax growth 25.0–66.7%, the Nov 2012–2019 medians of 1–2 editions, the 126/230 pooled survival, per-cohort non-China rates, the China newcomer range 33–103, ln2/ln1.6 = 1.47, ln2/ln1.114 = 6.42, ln2/ln1.17 = 4.41. All held. The writer's two corrections to the evidence summary are right: 61.5% sits below the 62.0–69.4% range, and both 2021 cohorts crossed ten editions in 2026. The downloaded November 2026 file matches the recorded SHA-256.

Every printed href opened with a 200 and landed on its source. Reread past the quoted passages: the release's "Just 27" sentence is in its lead paragraph, not under "Only 27 Systems Are New", so the locator was wrong and is fixed. The "This suggests" quote, Prickett Morgan's two quotes, the 24 October / 1 November deadlines, Epoch's 2.5x and its 8-bit definition, and the Description page's Year field all match their pages. Kinds hold: TOP500, Epoch and Next Platform are each cited only for what they own; Next Platform as primary for its author's own reading.

Two narrowings to what the record supports. "The ageing is in the bottom half" overstated it, since a quarter of the 138 rank above 201; it now says most of the old machines sit there. The pre-2022 rebound figures were all-country while the next sentence switched to "outside China"; the all-country count is also 39–54 for those nine lists, so the sentence now uses the same population. Neither change avoids recording thin reporting.

## Reads well
Cut "The cohorts show the result." It said nothing; the next sentence gives the cohorts. The rest of the prose passes the placeholder test. The voice is close to the guide: plain, method stated before the finding, rival readings in their holders' words.

The dek led with "Across 30 TOP500 lists", which does not cover the bar growth (that uses 2010–2026), and it gave 5–25% with nothing to measure it against. It now sets 5–25% against 2011–2019's 30–69% and links the two halves with "so", which is the piece's causal claim. It is not a correction of TOP500 and not in the recent "<Owner>'s figure does not..." form. The headline is a causal statement, not a figure-against-figure comparison, and the headings are not number-led.

The closer read as an arithmetic fact without a point. A sentence the record supports now precedes it: the list aged through the 2022–2026 newcomer range, so a rebound to that range would not stop the ageing.

## The experience
At phone width (about 340 px of figure) the 24 px chart type rendered near 7 px. All three charts now use 40 px ticks every four years, 34–36 px legends and annotations, and shorter legend labels in Fig. 2. Year ticks were on the November category, which put June bars visually in the prior year; they now sit on each June so a year reads rightward from its tick. Fig. 1's alt text said the bars stayed under 110 "until 2020"; the 2020 bars are also under, so it now says "through 2020". Checked in light and dark at 390 px and 1280 px.

Beyond its sources, the piece shows from the list files that the ageing comes from the slowing entry bar, measures it by cohort survival, and separates China's withdrawal and the AI-factory suggestion from it. That agrees with the writer's original-work sentence.

## Edits
- Dek (header and nb-meta): rewritten to set 5–25% since 2020 against 30–69% in 2011–2019, with "so" linking it to cohort survival.
- Release quote locator: "Section “Only 27 Systems Are New”" changed to "Lead paragraph, under the headline".
- "The ageing is in the bottom half." changed to "Most of the old machines sit in the bottom half."
- "newcomers outside China held between 39 and 54" changed to "newcomers held between 39 and 54".
- Closer: added "The list aged through those years." before the bar-growth sentence; "Over those years the bar" changed to "The bar".
- Cut "The cohorts show the result."
- Fig. 1 alt text: "until 2020" changed to "through 2020".
- chart-1/2/3.py: larger type, ticks on June every four years, label standoff, shorter Fig. 2 legend; PNGs re-rendered with `nb chart`.
- Restamped: 1,177 words, 8 sources. Proof: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision
approve. The argument holds against the files and sources, and every fault was fixable in place.
