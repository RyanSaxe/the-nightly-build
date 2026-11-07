# Editorial review: feature/anthropic-rd-acceleration-review (editor/01)

## Correct

Thesis, from the draft alone: the published estimates of AI-driven acceleration at Anthropic measure four different things, and only the AECI slope ratio measures the quantity in the RSP's doubling condition. Claims under it:

1. METR computes 1.97 from the private Risk Report's figures behind the public "less than a factor of 2", on a redacted leading indicator. Held. Checked against METR's review, Claim 1, including that the 1.97 is METR's calculation and that the private sentence attributes "all of the observed speedup" to AI.
2. The RSP v3.4 doubling is condition (a), on aggregate capabilities. A with-and-without-AI comparison speaks only to (b), and the public Risk Report states (b) more strictly ("attributable primarily") than the RSP ("plausible … substantially attributable"). Held. Checked against the RSP PDF p.9 and the changelog on pp.19–20, and against the Risk Report PDF p.103.
3. For 15 July, METR's two AECI figures (about 1.5 on the report's data, 1.9 with more benchmarks) are under 2. Anthropic's own published ratio went from 1.53 to 1.70, and METR's October estimate is 1.9 (1.5–2.8). The link function alone moves that from 1.1 to 2.9. Held. Checked against METR's assessment (#key-findings, #methodology, #benchmark-scores-aeci; the RMSE 1.9 against 3.9 and the 81% are in the alt text of the jump-vs-slope-change figure), the Opus 5.5 card p.41, and the Haiku 5.5 card p.20, where I rendered the figure and read "1.70× slope change" in its legend.

Breaks and fixes:

- **Headline.** "No measure of Anthropic's AI-driven acceleration rules out 2x" is false on the article's own page. The Opus 5.5 card's 95% range for its 1.53 is 1.20 to 1.82, and Fig. 2 plots it. METR's complementary log-log row, 1.1x (0.8–1.5), is in the table. Both exclude 2. The lede's "none of the four rules out 2" had the same fault. I rewrote the headline to the claim the piece does defend, "Only the capability index measures what Anthropic's 2x threshold counts", and cut the clause from the lede. The dek's 1.97 "on a redacted indicator the threshold does not name" now gives the headline its instance.
- **Lane C basis.** The draft said METR "says" the private report's "slightly less than twice as fast" rests on interviews and surveys. That phrase comes from METR's proposed replacement wording for the report, written in Anthropic's voice, and not from a statement about the private report's method. I narrowed the sentence to say so.
- **Researchers' lean.** METR writes "most relevant researchers at METR and Anthropic". "Researchers at both organizations" dropped the "most". Restored.
- **Disclosure citation.** The disclosure carried citation 4, and METR's assessment does not say who writes this paper. The citation was left behind when the writer cut METR's Claude-analysis line. I removed it and took #adversarial-robustness out of source 4's locator. I added #methodology, which is where the Model 2–4 training dates in the prose come from.
- Every printed href returns 200 and lands on the cited document (`nb check --check-links` also passes). All eight `data-nb-kind="primary"` labels hold. Each document is the owner of what it is cited for, and the METR review is cited for the private report only through METR's attributed quotations. Fig. 2's coordinates match every plotted value on the 1-to-3 linear axis.
- Noted and kept: the S-1/A clause "estimates for future models" compresses "our internal estimates and our expectations regarding future models, rather than our current models". The filing's "rather than our current models" supports that reading.

## Reads well

What went:

- "METR agrees with Anthropic that catastrophic risk on 15 July was low." This repeated the lede's second paragraph almost word for word. The agreement the commission requires is stated once, in the lede.
- "and none of the four rules out 2". Gone for correctness, as above.

Lifted or made exact:

- "Anthropic reads lane A as a one-time jump" had Anthropic reading the paper's own chart lane. Now "the AECI record".
- "The Opus 5.5 card" was the first prose mention of that document, and a reader arriving from a link had no referent. Now "Anthropic's Claude Opus 5.5 system card".
- "about 15 to 29 index points a year" read as a range. Now "a rise from about 15 to 29".
- "the estimates that reach 2 sit in lanes B and C" is now "only estimates in lanes B and C reach 2".
- The last sentence ended on a bare "1.9 (1.5–2.8)" and left the reader to finish the conclusion. It now says the interval spans the line, which is the arithmetic the piece has been building toward.

The register matches the voice guide: wording quoted before judgment, the definition and window named next to each number, and one term per quantity. I found no wording taken from the voice guide's passages or from the commission's sentences. The headings ("Three hundredths from the line", "Two baseline years in one", "Each estimate, by what it measures", "A fit choice moves the estimate from 1.1 to 2.9") are each built differently. None names a source document, and none copies the recent organization-verb-figure headline or the "X, where Y" dek.

## The experience

The page leads with two figures, and both work. Fig. 1 shows the doubling as compounding. Fig. 2 puts every estimate in a lane by what it measures and shows the 2x line as condition (a) only in lane A. I rebuilt the page with `nb preview` and captured it with Playwright at 390 and 1,280 px in light and dark. The page has no horizontal scroll, and nothing overlaps in Fig. 1, Fig. 2, the table or the new headline. Fig. 2's labels are small on a phone (about 8 px rendered) but legible. The only visual I changed is the headline, which wraps to three lines on a phone.

What the piece gives beyond its sources: METR's review puts 1.97, 1.3–2.8, "slightly less than twice" and the AECI 1.5 and 1.9 on one page as if they test the same line. The article shows that the near-2 figures sit on a leading indicator and a counterfactual, while for July the RSP's own quantity read 1.5 and 1.9, with only the October interval spanning 2. It also catches the Risk Report's "primarily", which neither METR nor Anthropic points out. This matches the writer's original-work sentence, and the new headline now states it.

## Edits

- Headline, `<title>` and nb-meta title: "No measure of Anthropic's AI-driven acceleration rules out 2x" → "Only the capability index measures what Anthropic's 2x threshold counts".
- Lede: "Researchers at both organizations" → "Most of the relevant researchers at both organizations".
- Lede: cut ", and none of the four rules out 2".
- Lane C paragraph: the sentence on the private estimate's basis now attributes the interviews-and-surveys phrase to METR's proposed wording.
- Fit section: "Anthropic reads lane A" → "Anthropic reads the AECI record".
- Fit section: "The Opus 5.5 card" → "Anthropic's Claude Opus 5.5 system card".
- Fit section: "about 15 to 29 index points a year" → "a rise from about 15 to 29 index points a year".
- Cut "METR agrees with Anthropic that catastrophic risk on 15 July was low." and recast the next sentence as "METR finds 'broadly compelling' Anthropic's case that its models could not yet replace its research staff".
- Close: "the estimates that reach 2 sit in lanes B and C" → "only estimates in lanes B and C reach 2".
- Close: "1.9 (1.5–2.8)." → "1.9, and its interval of 1.5 to 2.8 spans the line."
- Disclosure: removed citation 4. The sentence itself is unchanged.
- Source 4 locator: dropped #adversarial-robustness, added #methodology.
- Reran `nb stamp`: 1,197 words, 8 sources, 5 minutes.

## Decision

approve. Every break was fixable from the record and the sources, and no change remains for the writer. Proof after edits: BLOCK 0, WARN 0, PUBLISHABLE, with link checking as well.

## Questions for the orchestrator

- Not blocking. METR says Claude was "deeply involved in … the majority of our own analysis" (assessment, #adversarial-robustness), and METR found no systematic bias. The fact bears on how far to trust the review, and it would sit beside the disclosure. Adding it means about 20 words, and the piece is at 1,197 of 1,200, so it would need an equal cut. I left it out. If you want it in, the S-1/A's second clause is the cut I would make.
- The writer's question on the nb-meta model string (`claude-opus-5-5`) is still open and is yours to answer. I did not change it.
