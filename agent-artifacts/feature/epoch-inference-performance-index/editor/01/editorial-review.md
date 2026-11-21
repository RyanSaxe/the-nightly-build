# Editorial review: feature/epoch-inference-performance-index (editor/01)

## Correct

Thesis: Epoch's 25× GB300-over-H100 figure is one average of four per-model ratios that run from 8× to 217×, and the index behind it, and the 4.6× capacity series built on it, has not been checked against measurement on an H100. Claims under it: (1) the 25 is the reciprocal of the mean of four scores, which is the harmonic mean of the ratios, and a geometric mean gives 59; (2) on Epoch's own scores the 25 factors into 13.6× from H100 to B300 HGX and 1.85× from the 72-GPU rack, and the datasheets explain little of the first step; (3) the series' rise in capacity per unit of compute is about 95 percent change in which chips were bought.

How each held:

- Per-model ratios (the orchestrator's open question). Recomputed from `only_0` to `only_3` of the author's score matrix, H100 row `H100 SXM · FP8 · 400G`: 0.022619, 0.006303, 0.125202, 0.004604, giving 44.2×, 158.7×, 7.99× and 217.2×. Their mean is 0.039682, equal to the headline column `log_50_400`, so 25.20×; geometric 59.06×; Qwen's share of the sum 78.9 percent. The writer's figures stand and the evidence record's 43.5/166.7/200 are rounding artefacts.
- Sensitivity range broke. The draft said the 28 scenarios run from 19.5× to 89.5× "setting aside single-speed ones". That range also excludes the four single-model scenarios (`only_1` gives 158.7×, `only_3` 217.2×). Fixed to "leaving aside those that keep one model or one speed". "Reweightings" became "named scenarios", the README's term, since the set includes input-ratio and decode-only runs.
- FP4 inference broke. The draft placed SemiAnalysis's 100× and 65× both at 116 tok/s/user. In the newsletter the 65× FP8-vs-FP8 sentence gives no speed, and the "65x (116 tok/s/user)" passage is tokens per dollar. The evidence record carries the same error. The sentence now states both as "up to" figures against an FP8 H100 and makes the 1.5× conditional on both maxima sharing an operating point. This narrowed the claim to what the source prints.
- Precision. The draft said the index models only the H100 in FP8 and the "other 20 profiles" in FP4. The methodology names H100, H200 and TPU v7 as FP8, so the count of 20 was only right with all three named. Fixed.
- InferenceX citation note. The draft's note called the figures indicative because of an "Unofficial deployment" banner. In the saved HTML the banner is hidden unless `location.hostname` differs from `inferencex.semianalysis.com`, and the page was fetched from that host, so the banner is an artefact of reading the HTML offline. The note now says where the figures were read. Flagged to the orchestrator because the evidence record leaves this open.
- Validation. Checked against the validation README: 11.6 percent at five Kimi K3/GB300 points with both phases at 50 percent of SOL, 256.3 percent at undiscounted SOL, 40 to 344 percent for other pairs, no H100 row, and the quoted "not a universal 12% error bar on the index". The README's next-evidence paragraph lists checks on Qwen and the MAI proxy as still to do, which I added: the model behind 79 percent of the H100's score has no measurement check. The brief asked that the article say the IPI is modelled and thinly validated where the argument leans on it. It now does so in the dek, the opener, the validation paragraph and the closer.
- Other figures recomputed and held: 13.6× (0.5407/0.0397) and 1.85× (1/0.5407; report "about 1.9×"); datasheet ratios 2.27, 2.31, 3.6, 1.11, 1.03, 1.0; 4.583× and 2.594×; 77 percent; counterfactual 4.4953×, which rounds to 4.50×; compute shares; TPU v7 17.4 percent of added capacity against Blackwell's 17.8; waterfall terms against the record's midpoint split; InferenceX 11.8, 25.5, 35.9.
- Labels. The report is by Jason Li of Epoch AI. The draft never named him in the body and called him "the index author". He is now named in the dek and opener.
- Links. Every href opened. The Epoch, SemiAnalysis and CSV addresses return 200. The three github.com blob addresses return 403 from this session's proxy ("GitHub access to this repository is not enabled for this session"), not from GitHub. The same paths return 200 on raw.githubusercontent.com, and Epoch's report links these exact github.com URLs. `nb check --check-links` passes.
- Kinds. The Epoch hardware database (s5) is cited for FP8, bandwidth and capacity figures that Nvidia owns. Epoch repeats them from the datasheets, so it is secondary for those claims and is now labelled secondary. Li's GitHub documents are primary for his own scores and checks. They are one author with the Epoch report, and the article does not present them as independent.

## Reads well

Went:
- "That FLOP/s undercount holds on every model in the index." Its referent, "undercount", was never set up. It was folded into the next sentence as the consequence of the 8× floor.
- "Epoch's report concedes the choice." This graded the source. It became "In a footnote, Epoch's report says".
- "Measured H100 ratios come from elsewhere." A connective that said nothing the next sentence did not. Cut.
- The closer "Only one model on one chip, a GB300, has matched measurement closely..." This repeated the new dek and the validation paragraph. It was replaced with the methodology's statement that the scores carry no confidence interval, which ends on what the 4.6× interval leaves out.
- "and leaves out any error in the scores" became "only". The next sentence carries the point.

Repeats of the recent record:
- The headline "Epoch's 25× GB300 figure depends on how it averages four models" used the possessive-figure-plus-verb mould of the 18 November "Kane and Staiger's phone-ban 'half' counts the pandemic years". It now puts the subject first and the range as the surprise: "Epoch averages GB300 leads of 8× to 217× over the H100 into 25×".
- The dek joined two clauses with ", and", and its first clause restated what the new headline implies. It is now a single sentence with a stance and a named author.
- Heading 2, "Averaging the scores, not the ratios", was an antithesis whose misconception the section never states. It became "A harmonic mean of four ratios", the section's actual identity.
- Heading 3, "The rack contributes a factor of 1.85", was another declarative sentence with a count. It also headed the smaller of the section's two steps. It became "13.6× from the chip, 1.85× from the rack".

The register held close to the voice guide: ratios sit beside their inputs and the doubt is aimed at the method. I found no exemplar phrasing borrowed into the article.

## The experience

Figure 1 (inline SVG) renders cleanly at 1280 px light and at 390 px dark. The panels stack and none of the labels overlap. Its right-hand bars are to scale (0.125 to 152 units, the mean line at 0.0397). Figure 2's log bars and three reference lines match the score matrix. Figure 3's waterfall matches the record's terms. Its axis read "GB300e per H100e", units the prose never defines, so I changed it to "GB300 units per H100 of 8-bit compute" and re-rendered it with `nb chart`. The table's long row label wrapped on a phone. It is shortened, since the prose already gives 8 and 72 GPUs. Neither page scrolls sideways.

What the piece gives beyond its sources: it shows from Li's own score matrix that the 25× is a harmonic-type average held down by one model, splits it into a chip step and a rack step, and splits the capacity series' rise into chip mix and score drift. Epoch publishes none of these. This matches the writer's original-work sentence. The headline is the article's largest claim and the second section shows it in full.

## Edits

- Headline, `<title>` and nb-meta title rewritten.
- Dek rewritten in the page and in nb-meta, and the author named.
- Opener names Jason Li. The "undercount" sentence was merged into the range sentence, and the 59/no-H100 sentence was split in two.
- "The result is speed-of-light" became "a speed-of-light estimate, with no discount for software".
- The Fig. 1 caption now says "illustrative curves".
- Section 2 heading and id changed to "A harmonic mean of four ratios" / `harmonic-mean`.
- The footnote sentence reopened with "In a footnote, Epoch's report says".
- The scenario-range sentence was corrected to exclude single-model and single-speed scenarios.
- "The author" and "its author" became "Li" in the body and in the Fig. 2 caption.
- A sentence on the Qwen check as unfinished work was added, and the s3 locator extended.
- "Measured H100 ratios come from elsewhere." cut. "InferenceX has" became "InferenceX measured".
- The s6 note was replaced, since the banner is an offline-render artefact.
- Section 3 heading and id changed to "13.6× from the chip, 1.85× from the rack" / `chip-and-rack`.
- "Epoch's scores split the 25" became "On Epoch's scores the 25 factors".
- "No source separates" became "none of these sources separates".
- The FP4 sentence now makes the 1.5× conditional and no longer puts the 65× at 116 tok/s/user.
- The FP8 profiles now name the H100, H200 and TPU v7.
- Table row label shortened.
- Closer rewritten, with a citation to the methodology's "What the evidence supports" (s8).
- s5 `data-nb-kind` changed from primary to secondary.
- chart-2.py y-axis title changed and chart-2.png re-rendered.
- nb-meta words updated to 1193.

## Decision

Approve. The corrections were edits within the record and the sources, and the proof is clean at 1193 words.
