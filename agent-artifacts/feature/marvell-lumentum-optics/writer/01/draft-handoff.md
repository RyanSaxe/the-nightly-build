# Draft handoff: feature/marvell-lumentum-optics (writer 01)

## Original work

The article redraws Marvell's own ownership-keyed module diagrams (deck slides 13 and 14) as one signal path with the order of the link added, then divides the $115 billion by Lumentum's reported, guided and target revenue and sets the result against Marvell's own reconstructed multiple, which shows the price sits at Marvell's multiple at Lumentum's December guidance and needs a $2.0 billion quarter after that to reach Lumentum's target.

## Proof

`nb check ... --series feature --repo /home/user/the-nightly-build` (links included): BLOCK: 0, WARN: 0, PUBLISHABLE. 1192 words, 13 sources, 5 min. No warning left on purpose.

Rendered check: preview built with `nb preview`, Fig. 1 (two inline SVG panels), Fig. 2 (chart-1.png) and the stat strip captured with Playwright at 1100 px and 390 px, light and dark. No horizontal scroll. Fixes made after the first look: oversized arrowheads on the fiber lines, a SerDes label crossing the module outline, an "unmodulated light" label touching the ELSFP box, and chart text too small for a phone (chart fonts raised; `nb chart` exports a fixed 1200x675 canvas). The chart PNG is fixed light paper in dark mode, as spec/charts.md says.

## Open evidence and voice questions (assumptions I worked on)

1. CNBC (source 5) returned 403 to direct fetch, so I could not reopen it. I used only the researcher's two percentages (Marvell down 13%, Lumentum down nearly 19% on 2 November), attributed to CNBC, quoted no wording, and said so in the source's `data-nb-note`. The editor may want that cite checked against the live page.
2. Marvell multiple (18.6x). Computed as the researcher recorded it: 925.7M fully diluted shares (warrants excluded) x $251.56 plus $1.03B net debt (1 August) over $12.6B (slide 20, Marvell's annualized FQ3'27 guidance midpoint). The article labels it the paper's reconstruction and states the warrant exclusion. It mixes a 28 October price with a 1 August balance sheet and Marvell's quarter that ended 31 October.
3. Source 10 is the Rule 425 Form 8-K (`d163169d425.htm`), which I confirmed contains the Merger Agreement text with Sections 4.1(c)(i) and 4.2(c)(i). The researcher's evidence file did not name a separate exhibit URL, and `d163169dex21.htm` returns 404.
4. The "$100B" FAQ figure is reported next to a share-count reconstruction ($102.7B common only; $114.9B fully diluted less cash). The article says the filings do not state what the FAQ counts, per the commission.
5. Lumentum blog (source 7) was reopened and read directly; the CW-laser-plus-separate-modulator sentence is verified. Marvell's 10-K was searched in full: "laser" appears twice, both as "laser drivers".
6. Hurlston's "we supply our lasers to almost all of our competitors" is quoted exactly. "Our competitors" there means Lumentum's, so the article draws no claim about Marvell's competitors.
7. Voice guide: no ambiguity needed resolving. I kept the Lam move (both numbers in one sentence), the Potter move (result then the limit beside it, "For reference"), and no borrowed phrasing.
8. Not used from the evidence by choice: price over operating income and EPS, the termination fees and regulatory fee, and the Inphi comparison, to stay inside 1200 words and the commission's limits.
