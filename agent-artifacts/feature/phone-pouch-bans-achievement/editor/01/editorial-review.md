# Editorial review: feature/phone-pouch-bans-achievement (editor/01)

## Correct

Thesis, from the draft alone: the release's "half" is a ratio of two yearly rates. Its headline applies that ratio to the whole loss since 2013, and on NAEP most of eighth-grade math's loss came in 2019–22. Claims under it:

1. The ratio runs from half to all on the release's own range, so "half" is the release's cautious end. This held. I reopened the release on prnewswire: "a gradual loss of approximately 0.01 to 0.02 standard deviations per year", "about half of the annual decline in achievement since 2013". Kane's "two-hundredths ... year after year, since 2013" is verbatim in the Gazette.
2. The 2013–24 loss includes the pandemic, and half of NAEP's 11-point grade 8 math loss (5.5) is more than the 3 points lost in 2013–19. The release's own dates establish the first half of this claim. The arithmetic held, with one break. The draft said phones "would have to explain all of the 2013–19 decline and part of the 2019–22 drop", and that does not follow. 5.5 points could include less than all of the pre-2019 decline. What does follow is that even with all 3 pre-2019 points, 2.5 points must come from 2019–22. I rewrote the sentence to say that.
3. The April Allcott et al. study bounds pouch effects at about 0.007 student SD over the first three years, on a different scale. I checked this in the NBER text (p. 3, p. 23): "over the first three years following adoption". The draft said "over three years". It also described the design as using records "for 4,608 schools", but the estimate uses the 2023–25 adopters. Both are now narrowed to what the paper says.
4. By the test the authors wrote in May (Scorecard p. 13), a 0.01 SD gain is not the sharp rise. The quote is verbatim and Kane's "a relatively small effect" is in the Gazette ("It's a relatively small effect, but it's about half the year-over-year loss..."). This held.

Orchestrator concern 1 (NAEP). The release names no dataset for the decline. I re-read it and found nothing; NAEP is not mentioned. The old dek ("Half of eighth graders' 11-point NAEP math loss since 2013, the share ... release says") and old headline ("the eighth-grade math loss that Harvard's phone-ban release calls gradual") both told the reader the release's loss was NAEP's. Both are rewritten so that NAEP is the national record set beside the claim. The body's link to NAEP is now sourced as well. The Scorecard (Figure 1, note p. 6) shows that Kane and Staiger charted NAEP grade 8 as the national trend in May, so the body says "NAEP, the national record the same authors charted in May, matches it".

Assumption I worked on, not a change: the article prints no 2022 or 2024 NAEP score. Its 11 points is the sum of cited rounded changes (285 to 282 from the Digest, then minus 8 and flat from NAGB). A search turned up 272 for 2024 public-school-only grade 8 math, against 284 in 2013. That series gives 12 points, which does not change the argument. If the orchestrator obtains the all-students 2024 score, 274 would confirm the 11.

Fixed quotation. The release reads "an annual boost in achievement growth of 0.01 standard deviations". The draft printed "0.01 SD" inside quotation marks, and I restored the source's words.

Labels. "Harvard's" in the headline was a loose owner. The release is from CEPR at Harvard in partnership with NWEA and Dartmouth, and "half" is the authors' own word in both the release and the Gazette. The headline now names Kane and Staiger.

Kinds and hrefs. Every href was opened. Thirteen return 200. The two NBER PDFs return 403 to curl but serve the PDF to a fetch, which is a bot block a reader will not hit. I agree with the kinds: the release and the Gazette are primary only for the authors' own claims, and NPR via OPB and AP via the Korea Times are secondary. The Dee and Jacob quotes check against OPB.

## Reads well

What went:
- The section paragraph "The release's body compares rates ... Its headline turns that into a share of the total" repeated the orientation's second paragraph. I moved its quote into the orientation and deleted it.
- In the closing section, "Pouch schools' scores grew about 0.01 standard deviations a year faster" restated a figure from section 2. It went, and the sentence now opens on Kane's year-by-year statement.
- The orientation used "half of the historical loss" twice in two paragraphs. The second use became "applies that ratio to the whole loss since 2013".

What I lifted:
- Dee's "making that extrapolation" had no referent. A reader arriving from a link could not tell what extrapolation he meant. I added his preceding sentence from NPR ("these very small test score gains will aggregate and add up over time").
- The orientation called the April study "six researchers" and section 4 called it "Hunt Allcott and colleagues", so a reader could take them for two studies. Allcott is now named in both places.
- In the disclosure, "its figures" could be read as Harvard's site. It now reads "the study's figures".

Nothing came from the briefing files or the voice guide's quoted passages. The percentile line is the voice guide's move (a translation onto a scale the reader already holds) in the article's own numbers, so it stays.

Recent record. The opener does not restate a figure, and the close is a verdict, not a weighing. The headline no longer carries a figure. The new dek is a single clause, avoiding the ", and" and ", which" joins. The heading "A pre-registered study puts a ceiling on the gain" implied a cap on Kane's gain, which the units do not allow. It is now "What the April study rules out", which has no number, and its section label matches. Section 4 also says the release finds no significant difference across school levels; that wording came from the release text.

## The experience

Fig. 2 rendered 917px tall at desktop, and Fig. 3 was a 472px raster stretched to 760px. Both images now carry the documented SVG sizing with a max-width (34rem and 30rem). Fig. 2 is now 693px tall, and Fig. 3 is shown near its native width, so it is no longer soft. A sharper Fig. 3 cannot come from `nb asset`, which rasterizes at a fixed 2x.

On a phone, the study names in the table were set in monospace, and the result column sat off-screen behind the scroll. Study names now use the documented `nb-table-token` cell, and the test-score column comes before the setting. I checked phone and desktop in both themes with no page overflow, and the SVG labels in Fig. 1 hold at 350px.

What the piece gives beyond its sources: the release shows two rates; the piece shows that applying their ratio to the whole loss since 2013 needs at least 2.5 points of the 2019–22 drop on NAEP's record. It then judges the result by the authors' own May test. This matches the handoff's original-work sentence. The headline, as its largest claim, says the "half" counts the pandemic years, and the release's own 2013–24 span supports that.

## Edits

- Headline and `<title>`/meta title: "Kane and Staiger's phone-ban "half" counts the pandemic years" (was 16 words, "Harvard's", implied the release used NAEP).
- Dek: "Set beside NAEP's eighth-grade math record, the "half of the historical loss" that their release says in-school phones may account for exceeds the whole 2013–19 decline."
- Orientation, paragraph 1: Allcott and five co-authors named, with "effects on test scores".
- Orientation, paragraph 2: recast around the release body's "about half of the annual decline" and the headline's move to the whole loss. NAEP is set beside the claim, and the disclosure now says "the study's figures".
- Section 2: the quotation restored to "0.01 standard deviations", and the closing rates paragraph deleted.
- Section 3: "NAEP, the national record the same authors charted in May" added with a Scorecard citation, and the "all of the 2013–19 decline" sentence corrected to the 2.5-point minimum.
- Fig. 2 and Fig. 3 `<img>` given max-widths.
- Section 4 heading and section label: "What the April study rules out" (`what-the-april-study-rules-out`).
- Section 4: the design sentence narrowed to 2023–25 adopters out of 4,608 pouch-buying schools, the bound given "over the first three years", and the middle-school sentence split and stated in the release's terms.
- Dee's preceding sentence added for the referent of "that extrapolation".
- Table: study names as `nb-table-token`, and the test-score column moved before the setting.
- Section 5: the repeated 0.01 sentence cut and the stray [2] removed from Kane's year-effect sentence.
- Stamped at 1,187 words, 5 minutes and 13 sources. Proof with links: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision
approve. The argument holds on the record, and every break was fixable by editing. The display text no longer implies that the release used NAEP.
