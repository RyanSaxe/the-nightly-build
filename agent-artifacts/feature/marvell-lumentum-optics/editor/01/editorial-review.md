# Editorial review: feature/marvell-lumentum-optics (editor/01)

## Correct

Thesis, from the draft alone: Marvell is buying the light sources that sit next to its own electronics in an optical link, and at Marvell's 28 October price the $115 billion is 22.8 times Lumentum's run-rate revenue. It comes down to Marvell's own multiple only at Lumentum's December guidance, and to 14.4 times at Lumentum's own target. Under it:

1. In the deal deck's drawings, Marvell owns the DSP, drivers and TIAs and Lumentum owns the lasers and photodiodes. In co-packaged optics the photonic chip moves to Marvell and Lumentum keeps only the external laser. Held. I rendered slides 13 and 14 from the deck PDF. The colors match Fig. 1, slide 13 does label "Electronics" and "Photonics", and slide 14 colors the XPU, switch, PIC and EIC blue and the ELSFP's UHP lasers green, with one ELSFP feeding several PICs. I searched the whole Marvell 10-K for "laser": it appears twice, both as "laser drivers". Two sentences were looser than the sources. The DSP was said to turn SerDes lanes "into the optical signal", but it produces the electrical signal that drives the laser. And "the slide draws the silicon-photonics modulator as Marvell's" was wrong because the slide draws a PIC and never names a modulator. I rewrote both. The CW-laser sentence copied the Lumentum blog almost word for word without quotation marks, so I paraphrased it.
2. The multiples. I recomputed every one: 115/3.014 = 38.2; 115/3.7428 (665.5 + 808.4 + 1,006.3 + 1,262.6) = 30.7; 115/5.0504 = 22.8; 115/6.4 = 18.0; 115/8 = 14.4. Marvell: 925.67M shares × $251.56 + ($4,962.9M − $3,932.8M) = $233.9B, divided by $12.6B gives 18.6. Leaving out the in-the-money warrants does understate it. The 10-Q shows no short-term debt at 1 August. Growth: 136.5% and 25.5% are printed in the release, 1,600/1,262.6 = 26.7%, and 2,000/1,600 = 25%. Each denominator and period matches its source. The break was in the headline. "Marvell pays 23 times run-rate revenue" read like a deal term the companies had announced, and neither company states a multiple. The new headline says the figure "works out to" 23 times. The opener now says "Neither company states a multiple" before it divides. The section heading "Five revenue figures give five prices" was wrong, because there is one price and five multiples. The draft also said "beside its optical chips", but Marvell's parts in the link are electronics, so that label went.
3. The $100 billion against the $115 billion. 90,684,914 × $1,132 = $102.7B, and 103.29M × $1,132 = $116.9B, less $1,979.6M = $114.9B. All three figures appear in Section 4.1(c)(i) and the balance sheet. "Unvested awards" did not fit options, so it now reads "options, stock awards". The 28 October basis for the $115 billion was cited only to the release, which dates only the premium to that day. I added slide 9 ("undisturbed share price on October 28, 2026", ~$252) as the second citation.
4. The $550 billion and the shortage. The TAM figures check against slide 11, Investor Day pages 30 and 31, OFC slide 30 and the call ($60 billion, "in interconnect, and it's really in scale-up"). The draft had a misattribution. "The tight supply is not the reason we're wanting to enter this transaction now" is Murphy's answer to Tom O'Malley, not to Vivek Arya, yet the draft gave it as his reply to Arya. In his actual answer to Arya, Murphy says "there are supply shortages today across the industry" and points to Marvell's XPUs, switches and DSPs at the same hyperscalers ("the design wins are real"). The paragraph now quotes that answer. "1.28 times the $90 billion-plus" is now "at most", since the denominator is a floor.

CNBC (old source 5) could not be confirmed. A browser-style curl request returned 403 (Akamai), and I made no further attempt to get around the block. The commission allows the post-announcement moves only as CNBC reported them, so the sentence and the source were cut. The fixed-ratio point still stands on the Merger Agreement. Twelve sources remain, all primary. Every printed `href` returned 200: the SEC documents, the two Marvell PDFs, the Lumentum PDF and the blog. Every `data-nb-kind` is primary and sits with the party that owns the claim. The quoted passages I checked in the source text were Hurlston ("almost all of our competitors"), Arya, both Murphy quotes, "outpacing our current supply", the FAQ's "approximately $100 billion", and slide 38's "not intended to represent guidance on actual outcomes". All of them are verbatim.

## Reads well

Cut because it said nothing: "Lumentum's lasers are not captive" was a metaphor standing in front of a quote that already makes the point.

Cut because it came from a quoted passage: "For reference," is Potter's clause from the voice guide.

Cut because it repeated the piece: section 3's "the target model's $2 billion quarter is 25% above that midpoint" came back in the closing paragraph. It now appears once, at the close.

Rebuilt: the dek. The old one ("is still 14 times revenue, even if...") rated the number with "still", and it gave the target multiple the dek's place when the piece's own finding is the comparison with Marvell's multiple. The new dek states that comparison and its date, with no "where" clause. The headline drops "pays", because the deal has not closed and the price floats, and it names Lumentum. The section-2 heading repeated the opening sentence for the third time. It now states that section's own step: co-packaged optics leaves Lumentum the light source. The closing paragraph said the price "equals" Marvell's multiple, but 18.0 is below 18.6. It now says "just under", and the paragraph ends on the guidance limit next to the claim it limits, not on a roundup. I moved the Arya and Murphy exchange ahead of the shortage evidence, so "the shortage" has a referent and Lumentum's filings answer Murphy's missing supply figure.

## The experience

Fig. 1 had labels colliding. "Unmodulated light" ran into the ELSFP box, and on desktop "SerDes" crossed the module outline. I re-anchored the first label and set the second at 10px. The legend's third item was breaking mid-phrase on a phone, and each item now stays on one line. In Fig. 2 the label text was about 5.5 CSS px at 390px width. I raised the chart fonts, dropped the legend, since each point's label already names its basis and the caption explains the target, and moved the target label so it no longer runs into the December label. All of this was checked after a rebuild at 390 and 1100px in light and dark: no horizontal scroll and no overlaps left.

What the piece gives beyond its sources: it sets Marvell's own drawing of who owns each block in the link beside the price divided by every revenue figure Lumentum has published, and it shows that the price reaches Marvell's own multiple only at Lumentum's December guidance. That matches the handoff's original-work sentence.

## Edits

- Headline and `<title>`/nb-meta: "Marvell's $115 billion for laser maker Lumentum works out to 23 times its revenue run rate".
- Dek (body and nb-meta): "Priced at Marvell's 28 October close, the deal comes to 18 times Lumentum's annualized December guidance, just under Marvell's own revenue multiple that day."
- Opener: added "Neither company states a multiple" and recast the 22.8 sentence as a division.
- Added a slide 9 citation to the 28 October basis.
- Cut the CNBC share-move sentence and its source, and renumbered sources 6–13 to 5–12.
- Section-2 heading changed to "Co-packaged optics leaves Lumentum the light source".
- Corrected the DSP and driver functions.
- Paraphrased the blog's CW-laser sentence, and stated the EML's two jobs.
- "The slide draws the silicon-photonics modulator" became "Slide 14 draws that photonic chip".
- Cut "Lumentum's lasers are not captive."
- Section-3 heading: "prices" became "multiples".
- Cut the duplicated 25% sentence from section 3.
- Cut "For reference,".
- Recast the 18.6-times sentence.
- "Unvested awards" became "options, stock awards".
- Added the slide 9 and 20 citation to the Fig. 2 caption for the dashed line.
- "1.28 times" became "at most 1.28 times".
- Replaced the misattributed Murphy quote with his answer to Arya, and added "He gave no supply figure."
- Put the Arya paragraph ahead of the shortage evidence.
- Shortened the overlap-inference sentence.
- Rewrote the closing paragraph ("just under", target step, guidance limit).
- Fig. 1: re-anchored "unmodulated light", set the SerDes labels at 10px, and stopped the legend items wrapping.
- chart-1.py: raised fonts, removed the legend, moved the target label to bottom center, and re-rendered with `nb chart`.
- `nb stamp`: 1194 words, 12 sources.

## Decision

Approve. Each break was a wording, attribution or citation fault I could fix from the record and the sources, and the argument stands. Proof: BLOCK 0, WARN 0, PUBLISHABLE.
