# Commission: feature/data-centers-electricity-prices

Authorized by `nb duty` for 2026-11-06 (open section, no commissions). Template `article`. Slug `data-centers-electricity-prices`.

## The story
A study by researchers at Harvard University and the University of Pennsylvania, covered by the Washington Post on 6 November 2026, reports that data centers have had only a small effect on residential electricity prices and a somewhat larger one on industrial prices. It lands among other recent estimates that disagree even on the sign: some causal estimates find prices fell as data-center capacity grew (one arXiv paper, 2606.19777, and others), a CEPR/VoxEU column finds sizable increases with a larger effect on households, a USC study finds a small positive association, and an E3 report commissioned by the Data Center Coalition finds no evidence of increases. The question has political weight this week: residential bills were a campaign issue and markets are pricing slower data-center spending after the midterms.

## The angle to test
The estimates disagree because they measure different things: different price (residential retail rate vs industrial vs wholesale/capacity), different unit of exposure (gigawatts, facility counts, doublings), different period (pre- vs post-2023 AI buildout), different geography (utility, state, ISO), and different counterfactual (fixed demand vs observed). Put the estimates on one comparable footing where the documents allow, and show the mechanism by which a large new load can lower a rate (fixed network costs spread over more kilowatt-hours) or raise it (capacity and wholesale prices, new transmission and generation allocated to all customers).

This is an angle to test, not a conclusion. If the documents show the disagreement comes from something else, or that one study is plainly the stronger design, the piece says so.

## Decisions
- The new Harvard/Penn study is the news peg. Find and read the study itself (working paper, NBER, SSRN or the authors' pages). If its full text cannot be found, report that to the orchestrator immediately; the piece can still run on the documents that can be opened, but the peg must then be described only as far as the record supports.
- Cite each estimate to its own paper, at the table or equation that owns it, never to coverage.
- Industry-funded work (E3 for the Data Center Coalition) is reported with its sponsor named.
- The PJM capacity auction results and any state utility commission findings may be used where they explain a mechanism, cited to the owner.
- Reader: CS and ML engineers who build production systems; no economics background assumed beyond a regression and a fixed effect.
- Five-minute read, strict 600 to 1200 words, 2 to 4 flex sections, each built around a visual. At least five sources.
- Prefer a drawn mechanism or a comparison of estimates on one scale to a plain bar chart (press/editorial.md).
- Neighbours in this edition: the daily brief (general news, no data-center items) and an RL lesson. No overlap.
- Prior paper coverage: the-position/build-nuclear-power (2026-07-21) on data-center load and nuclear; current-events/2026-08-10 mentioned an estimate that data centers added $23 billion to bills. Do not repeat the nuclear argument.

## Required contribution
A reader leaves able to say, for any headline "data centers raise/lower your bill", which price, which period, which exposure measure and which comparison it rests on, and which of this week's estimates the evidence supports most.

## Decisions recorded after research (orchestrator)
- The Harvard/Penn study (Rana, Kaps and Netessine, SSRN 7580459) could be read only as its abstract. Decision: it stays the news peg, described only as far as the abstract states (design, the two $/MWh figures and their stated shares, the Big Tech vs co-location contrast). Nothing about its sample, standard errors or region definition. The Washington Post piece is not cited.
- The angle is narrowed, not dropped: different prices, exposure units and periods explain much of the disagreement, but the evidence record shows two instrumental-variable studies of the same average retail price (Watten et al.; Meeks et al.) with opposite signs. The piece states that plainly as the residual disagreement and does not claim that measurement differences explain everything.
- Elhai and Zhou's test of retail-price designs is reported as their finding about their own designs, not as a verdict on other papers.
- Watten et al.'s per-doubling wording: cite the coefficient and the paper's own wording; any conversion the piece prints shows its arithmetic and names it as the paper's coefficient times ln 2.
- The "$2.59/MWh per GW" figure is not used (not in the current paper).
- E3 is described with its sponsor and in its own terms (no evidence of cost shifting under existing rate structures, PJM as the exception), never as "no evidence of increases".
- No sourced residential-bill component breakdown exists in the record, so any mechanism drawing shows the direction of each channel with its owner, not invented shares.
- Role models: writing coach and researcher ran on a capable model (sonnet) per the balanced profile; writer high effort, editor inherits the orchestrator's model at high effort.

## Recent-pattern notes supplied to the writer and editor

- Headlines: five of the last six hinge on one precise figure ("$191.26 discount", "$115 billion ... 23 times", "44%"-style, "twice as far", "96 issues"). A figure is welcome only where it is the surprise; do not lead with a number by habit.
- Deks: the recent mold is a figure-laden clause plus a contrast clause hung on "where" or ", and" ("...where Bybit's 2025 haul held no stablecoin and saw 3% to 3.84% frozen"; "..., and production models pretrained with Muon have seen trillions"; "Across a CMU preprint's 30M-to-600M models, ..."). Build the dek differently.
- First section headings recently state a verdict with a contrast ("Muon pretrains better and still loses the fine-tuning trade"; "The panel restores the experts and keeps the retrial"). Vary.
- Recurring closing section shape: "What the second jury has to find" / "...point the other way". Avoid ending on a "what X has to find / decide" heading.
- Recurring phrasing to watch: "works out to", "comes from", "takes the lead".

## Decision recorded at delivery (orchestrator)
- The editor's brief directed it to open Meeks et al. (MIT CEEPR WP 2026-13r) at the IV table and make Table 2 match the paper. The residential IV coefficients (0.056 and 0.071, Table A9) and the IV sample therefore enter the article from that primary at the orchestrator's direction, with the locator recorded in the editorial review, though they are not in researcher/01's record.
