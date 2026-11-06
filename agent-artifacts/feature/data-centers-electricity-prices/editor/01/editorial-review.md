# Editorial review: feature/data-centers-electricity-prices (editor/01)

## Correct

Thesis, from the draft alone: this year's estimates agree that data-center load raised wholesale and capacity prices, and most of their disagreement over household rates follows from which price, period and dose each one measures. Under it sit three claims. First, the peg paper's $1.7/MWh is a share of an observed rise, about 1% of the 2025 national residential price. Second, a rate is costs over sales, and new load lowers it only through fixed-cost spreading, past the Dallas Fed threshold s*. Third, two instrumental-variable studies of the residential rate still find opposite signs, so sorting by measure does not explain everything.

Claim one held. Rana's and Kaps's pages confirm Wharton and Harvard Business School, the abstract gives the $5.4 and $1.7 and their shares, and EIA prints residential 17.30 cents/kWh for 2025. 1.7/173 is 0.98%. Every peg statement stays inside the abstract.

Claim two held. I opened Dallas Fed WP 2606r1. Equation 15 on PDF p.55 is s* = (1 + d)/(1 + d + η). The worked values check: 1.1/2.1 = 0.524 and 1.1/1.6 = 0.6875. Assumption 1 and "unlikely to hold in reality" are on PDF p.53, not p.51 as cited, so I moved the locator. Meeks Sections 7.1 and 7.2 do report generation additions and larger authorized rate bases after entry at investor-owned utilities.

Claim three held, and Table 2 was wrong in the way the writer suspected. Meeks's IV results are in Appendix B.4 and Table A9 (PDF pp.62-65 and p.87). The outcome is ln(average retail price) and the regressor is ln(1 + cumulative MW). The 0.073 and 0.078 are the all-customer column, one per instrument. The residential coefficients are 0.056 and 0.071, with Kleibergen-Paap F of 48.4 and 124.8. The IV sample is 16,874 utility-state-years and keeps utilities that already hosted data centers. The "973 utilities" in the draft belong to the entry design in Table 2 of the paper, not the IV. Table 2 of the article now prints the residential IV coefficients, their regressor and F, and the IV sample. It drops the +2.1% entry estimate, which is not an IV result and already appears in Table 1. Watten's "48 states" was an inference from 480 observations, so the row now prints the 480 state-years the paper reports. The Meeks instrument row now names both exposure measures (2005-07 establishments or jobs). This uses figures from the paper that the evidence record did not carry. The brief directed me to open the paper and make the table match it. The record's "0.073 to 0.078 for average retail price" is underspecified, not contradicted, so I did not escalate.

Both papers describe their coefficients as roughly elasticities: Watten says the inverse hyperbolic sine behaves like a natural log and reads the coefficient per 10% of capacity, and Meeks says its coefficients approximate elasticities where capacity is well above 1 MW. That puts the disagreement on one scale, −0.035 against +0.056 to +0.071, and I added one sentence saying so.

Table 1, recomputed against the record and the papers. Dallas Fed +6.9% (2021-25), Elhai and Zhou +$1.63/MWh (2025), USC +$3.44/MWh, the IMM's $23,100,955,341 over three delivery years, Rana's two figures, Scalera's +4% per hyperscaler facility and USC's +0.62% per doubling all match their owners. Watten's −6% is the coefficient times the 1.6 mean change, and page 3 of the paper applies it to 2019-24 growth, so the row now says "over 2019-24". The estimation window column stays 2015-24. Meeks's +5.2% is the investor-owned residential figure (Table 3 of the paper). The draft printed it beside "investor-owned" with no class, where readers could take it for the 5.6% all-customer figure, so the row now reads as residential. The per-doubling conversion, −0.035 × ln 2 = −0.0243, is right and is labelled as arithmetic against the paper's own −3.5%.

Labels. Elhai and Zhou list themselves as Harvard University, with no department, so "Harvard economists" became "Harvard researchers". The headline, dek and subheads hold against their owners.

Links. Every href returned the document with a browser request, except SSRN (Cloudflare challenge) and the CEPR discussion-paper page (Cloudflare block page). Both are the documents' own addresses, gated and not dead. The Scalera abstract was confirmed on the author's page at data-nb-url.

Source kinds. Two were wrong. The NCEA brief is co-written by Shon Hiatt, an author of the USC study it summarizes, so it reports from inside the authoring party and is primary. The E3 report is cited for its own PJM decomposition and its own rate-making primer, which E3 owns, so it is primary too. Its sponsor stays named in the sentence, in Fig. 1 and in the source line.

## Reads well

Went:
- "Its full text could not be obtained." It dangled after the EIA sentence, where "its" pointed at the wrong noun. Replaced with "We could read only the paper's abstract", which states the limit in the first person the ranking already uses.
- The ownership and customer-class paragraph in the last section. It opened a separate disagreement (investor-owned versus cooperatives, industrial versus residential) that does not bear on the section's claim, and it paid for the elasticity sentence under the cap.
- "the record supports", in the ranking. "The record" means something only to the researcher. Now "these studies support".

Lifted:
- The opener's "their load", which read as the studies' load, is now "data-center load".
- The IV definition said the instrument "moves where data centers go but not prices directly". That stated the exclusion restriction as fact. It now reads "predicts where data centers go and, by assumption, reaches prices only through them".
- The dek led with an unscaled $1.7 per megawatt-hour, which is the figure-first mold in the recent-pattern notes. It now states what the sorting leaves: nine estimates bracket the household effect at −6% to +5.2% without settling its sign. It does not restate the headline, and it avoids the "where" and ", and" contrast clause.

I found nothing borrowed from the briefing files or the voice guide's passages, and no opener, closer or heading that repeats the recent record. The last sentence ends on Elhai and Zhou's convexity point and passes the placeholder test. The register is the Davis walk-through the guide asks for.

## The experience

The tables, Fig. 1 and the equation render cleanly at 390px and 1280px in light and dark, with no horizontal page scroll. Table 2 still scrolls sideways inside its wrapper on a phone, which is the runtime's table behaviour. Table 2 now tells the reader what each coefficient is on, so the opposite signs can be compared instead of taken on trust. The last section is shorter and moves from the two IV designs to Elhai and Zhou's critique and then to the ranking without a detour.

Beyond its sources, the piece sorts nine estimates by the price, dose and period each one uses. It shows with the costs-over-sales identity and the Dallas Fed threshold how one load can push a rate either way. It puts Watten's and Meeks's residential coefficients on one elasticity scale, where they still disagree in sign. That matches the writer's original-work sentence, with the elasticity comparison now made explicit. The headline's claim, agreement on wholesale and a split on household rates, is what the tables show.

## Edits

- Dek (page and nb-meta) rewritten.
- Opener: "This year's studies ... their load" became "Studies published this year agree that data-center load".
- Peg: "Its full text could not be obtained." became "We could read only the paper's abstract."
- Table 1, Watten: "over 2019–24" added to the −6% estimate.
- Table 1, Meeks: estimate "+2.1%, investor-owned +5.2%", price "Utility residential".
- Dallas Fed Assumption 1 locator: PDF p.51 became p.53.
- Section 4 opener: IV definition reworded, and an elasticity sentence added (−0.035 against +0.056 to +0.071).
- Table 2 unit row: 480 state-years and 16,874 utility-state-years.
- Table 2 Meeks instrument: "2005–07 data-processing firms or jobs × Big Tech capital spending".
- Table 2 Meeks result: "Residential +0.056 and +0.071 on ln(1 + MW), one per instrument (F 48.4, 124.8)".
- Table 2 Meeks locator: Appendix B.4, PDF pp.62-65; Table A9, PDF p.87; IV paragraph p.30.
- Ownership and industrial paragraph cut.
- "Harvard economists" became "Harvard researchers".
- Ranking: "the record supports" became "these studies support".
- Source 7 (NCEA) and source 12 (E3): data-nb-kind changed from secondary to primary.
- Restamped: 1,185 words, 5 minutes, 12 sources.

## Decision

approve: the argument holds, Table 2 now prints the paper's residential IV result, and the proof with links reads BLOCK: 0, WARN: 0, PUBLISHABLE.
