# Draft handoff: feature/data-centers-electricity-prices (writer 01)

## Original work

The article sorts this year's data-center price estimates by the price, dose, period and comparison each one uses (Table 1), draws the costs-over-sales identity that lets one new load push an average rate both ways (Fig. 1 and the Dallas Fed threshold), and shows that this sorting explains the wholesale-versus-retail disagreement but not the opposite signs Watten et al. and Meeks et al. get for the same residential rate (Table 2).

## Proof

`./nb check .../library/feature/data-centers-electricity-prices.html --series feature --repo /home/user/the-nightly-build` (links checked): `BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE. Stamped at 1,195 words, 5 minutes, 12 sources. The series is strict and the cap is 1,200, so an edit that adds words has to cut the same number somewhere else. The proof counts the table, SVG, citation numerals and the sources list.

No warnings were left.

## Decisions a reviewer should check

- **Watten "per doubling".** The text prints the coefficient (−0.035), the arithmetic labelled as the coefficient times ln 2 (≈ −2.4%), and the paper's own −3.5% reading, as the commission directs. Table 1 carries the paper's −6% figure for the average customer, which matches coefficient × 1.6.
- **Dallas Fed worked example.** The d = 0.1, η = 1 (and η = 0.5) values are labelled as illustrative round numbers, not the paper's calibration. I read the paper's Section 7 (PDF pp.51–55) only to confirm that d enters Equation 15 as a fraction and to confirm the wording of Assumption 1. I added no claim from it beyond what the evidence record holds.
- **Peg.** The peg is described only as far as the abstract goes: the design, the two $/MWh figures and their shares. The "about 1%" is the researcher's size comparison against EIA's 2025 national residential average, used only for scale. I cut the Big Tech versus co-location contrast to stay within the word cap. Netessine's affiliation is not given, because no opened primary states it. "Wharton and Harvard Business School" rests on Rana's and Kaps's own pages.
- **E3.** The sponsor is named in the sentence and in Fig. 1. E3 is described by its one-year PJM decomposition, and the text says it uses a different counterfactual from the monitor's re-clearing. It is not described as "no evidence of increases".
- **Ranking.** The judgment is in the first person ("We would put most weight on…"): wholesale and capacity rows are best supported, and the household rate is supported as a size (−6% to +5.2%) and not as a sign.
- **Contradictions.** #1, #2 (in brief), #3, #5, #6, #7 and #8 are addressed in the prose. #4 (which wholesale component moves, USC vs Meeks) is left out. Neither side is a retail measure and the piece does not break wholesale prices into components. #9: none of the stale figures is used.
- **Scalera.** Only the +4% per hyperscaler facility figure appears (Table 1). The +13% per standard deviation of ten data centers was cut to stay within the word cap, so the "−6% to +5.2%" band in the judgment covers the per-customer averages in Table 1.
- **Tables on a phone.** Table 1 puts the estimate next to the study so both show at 390px, and the other columns scroll. In Table 2 the Meeks column needs a sideways scroll on a phone, which is how the runtime wraps nb-table. Fig. 1 and the equation render cleanly at 390px and 1280px in light and dark themes.

## Open questions

- Evidence: the Meeks IV coefficient (0.073 to 0.078) is recorded as being "for average retail price". The record does not say whether it is all-class or residential, or whether the outcome is logged. Table 2 prints it as "on log capacity" with no class, and pairs it with the +2.1% residential DiD figure.
- Voice: none.
