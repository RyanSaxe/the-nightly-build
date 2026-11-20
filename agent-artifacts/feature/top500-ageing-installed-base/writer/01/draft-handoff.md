# Writer handoff: feature/top500-ageing-installed-base (01)

## Original work

The article counts age, newcomers and five-year survival across the 30 TOP500 list files that carry First Appearance, and ties the list's ageing to the slowing growth of the No. 500 Rmax with simple survival arithmetic (Fig. 2 draws it on the real bar). Neither the TOP500 release nor the press coverage does either step.

## Proof

`nb stamp` then the brief's exact `nb check` (links included): BLOCK 0, WARN 0, PUBLISHABLE. 1,179 words, 8 sources. No warnings left.

Charts were checked as PNGs and in `nb preview` at 390 px and 1280 px, light and dark. The renderer exports a fixed 1200×675 canvas, so I used 24–26 px type and year-only ticks to keep the charts readable at phone width. Tick text is still small on a phone.

## Decisions for the editor

- The newcomer count is the file's 28. The release's 27 appears once, quoted, with Horizon at No. 24 on the live list as the stated difference. There is no speculation about why.
- The dek's "more than half of the machines that entered in 2020 and 2021" is all-country: 126 of 230 were still listed ten editions after entry (cohort_survival.csv, present_after_10). By cohort the share is 45–66%, so the 2020-06 cohort alone is under half. The body gives the non-China 52–72% and the pooled 126 of 230.
- Evidence summary correction: the 71 entries from the 2021 cohorts crossed ten editions in June and November 2026, so "this year". The record's "this year and last" is wrong.
- Evidence summary correction: 61.5% is just under the 62.0–69.4% November range, not inside it. The prose says "a little under".
- Next Platform is marked `primary` because the article cites it only for Prickett Morgan's own view.
- The 8-bit definition of H100e is cited to Epoch's chip-sales explorer post [8], since the doubling insight [7] does not state it.
- The closing claim ("5–17% a year … more than four years") uses November-on-November bar growth for 2022–2026 and ln 2 / ln 1.17 = 4.4.

## Open questions

None blocking.
