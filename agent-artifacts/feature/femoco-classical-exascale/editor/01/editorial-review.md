# Editorial review: feature/femoco-classical-exascale (editor/01)

## Correct

Thesis, from the draft alone: the prize abstract's "about one-fifth" divides a measured 105-minute run of unstated accuracy by an 8.6-hour quantum projection. The same authors have since lowered that projection to 2.5 hours, and a classical estimate for the same active space was posted in January. The prize adds the first exascale classical run and its measured time. It does not settle the advantage question.

Claims under it, and how each held:

1. The abstract compares 105 minutes measured on 1,280 LineShine nodes with "the best published 8.6-hour single-run projection". Held. I reread the SC26 page verbatim.
2. The 8.6-hour projection has fallen to 2.5 hours for CAS(113e,76o) under the same error rate, cycle time and reaction time. Held against arXiv:2502.15882 Sec. V and arXiv:2605.30455 abstract and Table XXVII. There is one discrepancy between the record and the source. The record calls 2.50 h the one-shot runtime and 2.36 h the expected runtime. Table XXVII's columns run ⟨.⟩ (expected) and then 1 shot, and expected = one-shot / (1 − p_fail) checks: 2.36 / 0.942 = 2.50. The volume column also equals qubits × 2.50 h. So 2.50 h is the expected runtime and 2.36 h is a single shot. The article never calls 2.5 h a single run, so nothing in it is false, and I altered no number. Question for the orchestrator: the abstract's "single-run" wording would compare more closely with 2.36 h, which gives a ratio of 1.35 rather than 1.4. I worked on the assumption that 2.5 h, the figure the paper's text and abstract lead with, stays. If you want the one-shot figure, the ratio sentence and Fig. 2 need changing.
3. The three time figures differ in kind: one measured, two projected, one extrapolated. Held. Zhai et al. p. 10 gives the 8.76 kcal/mol variational bound and "no formal theory of these extrapolations". Low et al. 2026 Sec. VI gives the perfect-overlap assumption and the "strongly subdominant" wording, both verbatim. The break was here. The draft reported the 2026 preprint's claim that trial-state preparation "should be strongly subdominant" and nothing else. The 2025 paper by the same group (Discussion, p. 16) puts phase estimation at 9.99 × 10^8 Toffolis, "similar cost as state preparation (between 7.6×10^8 and 1.3×10^9)". The evidence record carries those figures. I added one sentence giving the 2025 position beside the 2026 one, so the exclusion of preparation cost is neither inflated nor waved away.
4. Chan, Low et al. and Babbush et al. each state their position in their own words. Held. Every quotation was checked verbatim against the Quantum Frontiers post, arXiv:2605.30455 Sec. VI (intro) and the arXiv:2511.09124 v2 HTML. The quote card matches Chan's text exactly.

Headline and dek labels. The old headline had Google cutting the projection. Low et al. 2025 has nine authors: six at Google Quantum AI, plus Macquarie, UIUC, Florida State and QSimulate. The 2026 preprint has seven, six at Google Quantum AI plus Berry at Macquarie. "Google" as the actor was loose, and it is gone. The dek now says "its lead authors at Google Quantum AI", and the body names "Guang Hao Low and colleagues at Google Quantum AI", which both author lists support. The old headline's "since cut" implied an order relative to the prize paper that nobody established. The new "now cut" makes no claim about timing, as the angle decision requires. The opening had put the abstract's "for nearly a decade" "killer app" on CAS(113e,76o), in the article's own voice. The abstract says it of FeMoco, and the 76-orbital space dates from 2018. It is now attributed to the abstract and applied to FeMoco.

Other fixes. The Fig. 2 label "none with GPUs" went further than the CerebroSim text, which describes two LX2 Arm processors per node. It now reads "two Arm CPUs each". "Quantum phase estimation reads out an energy by projecting onto it" was garbled ("it" was the energy). It now follows Chan's wording: a projective measurement of the energy.

Links. All ten printed hrefs return 200 and land on the source: the SC26 page, the Quantum Insider article, seven arXiv abstract pages and the Quantum Frontiers post. Every `data-nb-url` matches its numbered list entry.

Kinds. All ten checked. The Quantum Frontiers post is primary for Chan's own position. CerebroSim is primary for the machine description, and a prize-paper author, Yutong Lu, is among its authors. The Quantum Insider is a secondary repost of the ACM release. No independent source is claimed that the piece does not have.

## Reads well

What went:
- "The abstract states no accuracy, and the SC26 page carries no full paper to check," cut from the last section. It repeated Sec. 3 and both figures. It was also the "has published no such check" closer the recent-pattern notes ask to avoid.
- "Against 8.6 hours, 105 minutes is 4.9 times shorter" became a plain division. "Times shorter" is an inverted ratio, and the reader has to undo it.
- "Google's authors say the same" became "Low and colleagues", which names the people quoted.

Ambiguities fixed. "They proposed a 76-orbital space", coming straight after a sentence about Chan, could have meant him. It now reads "The same paper proposed", and "Chan among them" places him in Li et al. "Zhai et al. are the reverse" used a name the prose had never introduced. Sec. 1 now names Huanchen Zhai.

Lifted. The opening paragraph defined terms before it reached the finding, and the series asks for the finding first. I moved the abstract's claim, the revision and the January estimate to the top, with definitions in the second paragraph. The first heading, "The abstract's 105 minutes and 8.6 hours", was another number noun phrase like the recent record's. It is now "What the abstract's one-fifth divides by", a step in the argument. The remaining headings are built differently from one another and from the recent ones. The voice register held elsewhere: caveats sit beside their numbers, as the guide asks.

## The experience

Both inline SVGs render cleanly at 390 px and 1,200 px in light and dark, with no horizontal page scroll and no overlapping labels. The Fig. 2 bar lengths check against the axis: 8.6 h is 344 units, 2.5 h is 100 and 1.75 h is 70, at 40 units per hour. Putting bars on one axis could suggest a race. The dashed-against-solid encoding, the "projected / measured / extrapolated" labels and the Zhai row with no bar carry the distinction, so I kept the figure. Fig. 1's two-sided layout shows the measured-against-projected split without help from the prose.

What the piece gives beyond its sources: none of them puts the abstract's 8.6-hour denominator next to its authors' own 2.5-hour revision and the January classical estimate, or marks each figure as measured, projected or extrapolated. That shows the one-fifth comparison falls to 1.4 and compares unlike quantities. This matches the writer's original-work sentence.

## Edits

- Headline: "A Gordon Bell team ran FeMoco in 105 minutes against a quantum projection Google has since cut from 8.6 hours to 2.5" → "Gordon Bell winners compare a measured 105-minute FeMoco run with a quantum projection now cut to 2.5 hours" (h1, `<title>`, nb-meta).
- Dek rewritten to carry the "one-fifth", the 8.6 hours, its Google Quantum AI lead authors and the January classical energy (dekline and nb-meta).
- Sec. 1 heading → "What the abstract's one-fifth divides by".
- Sec. 1 reordered: the finding comes first and the definitions second. The Low group and Zhai/Chan are named. "For nearly a decade" and "killer app" are attributed to the abstract and applied to FeMoco.
- "Same Hamiltonian" → "same active space" in Sec. 1 and Fig. 2, so one term is used throughout.
- Phase-estimation sentence reworded to "makes a projective measurement of the energy".
- Li et al. sentence: "Chan among them" added. "They proposed" → "The same paper proposed".
- Ratio sentence rewritten as a division. Numbers unchanged.
- Fig. 2 label "none with GPUs" → "two Arm CPUs each".
- Added: "The 2025 paper had put that preparation at about the same gate count as phase estimation", cited to arXiv:2502.15882, Discussion.
- "Google's authors" → "Low and colleagues". "Babbush and colleagues" → "Babbush and colleagues at Google Quantum AI".
- Cut the repeated no-accuracy sentence from the last section. "Sits on" → "is on". Last sentence recast without the leading "And".
- Sources 3 and 4 renumbered to match the new first-citation order (Low et al. 2026 is now 3, Zhai et al. is now 4).
- On the orchestrator's decision to keep 2.5 h and the 1.4 ratio: the first mention in the body now reads "now put the expected run time at 2.5 hours". The Fig. 2 label reads "2.5 h expected", and the aria-label says the same. To stay in the band, "1,280 nodes of the LineShine supercomputer" became "1,280 LineShine supercomputer nodes", "who published the 8.6 hours" became "authors of the 8.6 hours", and "from their side" was cut.
- Restamped at 1,199 words. Proof: BLOCK: 0 / WARN: 0 / verdict: PUBLISHABLE.

## Decision

approve. The argument holds against its primaries, and every break I found was fixable from the record and the sources. The one open question, expected against one-shot runtime for the 2.5 hours, does not make any printed sentence false.
