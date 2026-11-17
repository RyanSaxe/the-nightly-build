# Editorial review: feature/carbon-budget-oil-dip (editor/01)

Editor model: claude-opus-5-5 (Claude Code), high effort.

## Correct

Thesis, from the draft alone: the Global Carbon Budget projects a 0.4% fall in 2026 fossil CO2, but its own 68% range reaches a rise, and the budget's past projections miss by more than enough to change the sign. Under it:

1. Oil's fall (−243 Mt) is larger than the net fall (−158 Mt); coal and India push the other way. Held. I recomputed every fuel change from the evidence record's fuel series (rows 285–286) and the carbonation sink from the budget series (0.597 → 0.566 Gt, +31 Mt). The terms sum to −158. India +141 Mt and China −112 Mt reproduce from the national-file 2025 bases × 3.664 × the preprint's rounded percentages, and the draft labels both as derived. I reran the oil ranking against the dataset in the scratchpad (sheet "Fossil Emissions by Category", Oil column). 2026's −243 Mt is sixth, after 2020, 1992, 1981, 1980 and 2009, as printed.
2. Land-use change lifts total CO2 to 43.3 Gt, the highest in the series. Held. From the dataset, B + C − G gives 43.32 for 2026, ahead of 42.75 (2025), 42.42 (2018) and 42.32 (2024). The SVG bar heights match the record's 2026 partition to 0.1 unit. The sentence saying the ±3.2 Gt level uncertainty is mostly shared between adjacent years is an inference, not a quotation. The preprint supports it by keeping baseline-level uncertainty out of the growth range (§3.1.4, lines 1045–1046), and the draft states that the budget gives no figure for the change. I left it in.
3. The projection record (Table S6) shows a mean central miss of 0.37 points and a maximum of 0.66 (2015). That is about the distance from −0.4% to zero. Held. Recomputed from the ten ranged years: the misses sum to 3.66. If the 2016 budget's printed +0.2% is used in place of Table S6's −0.2%, the mean is 0.33, and "about one average miss from zero" still holds. The chart caption already discloses the 2016 conflict, so nothing in the prose rests on it, as the decisions log requires.

Breaks and fixes:

- **ScienceDaily attribution (s6).** The draft said "a university release reprinted by ScienceDaily said" emissions "may finally be turning a corner". I opened the page. The phrase is ScienceDaily's figcaption on a Shutterstock photo. The page credits "Materials provided by University of Exeter … Content may be edited for style and length", and the GCP press release that the universities issued does not contain the phrase. So nobody has shown the phrase to be the university's. I narrowed the attribution to the document that prints it: "ScienceDaily's edited version of the University of Exeter's release says…". `data-nb-kind="secondary"` stays correct now that ScienceDaily owns the wording. I put a question to the orchestrator below, because the evidence record calls this page a reprint.
- **Waterfall reading.** "Oil's bar … reaches further than the net bar" is false as drawn. Oil's bar ends at about −153, above the net bar's −158, so it is longer, not lower. Now "is longer than".
- **Elasticity.** The Nature Climate Change paper says a mean 20% rise *would* imply an elasticity of 0.1. Its 20% is a working figure, not a measured mean. "implies" became "would imply".
- **Remaining-budget arithmetic.** The brackets printed 3.46 and 3.45. A reader who checked them would get under four days, against the "about five days" in the text. Now 3.464 and 3.451, which give 4.7 days.
- **Chart 2 caption.** The 2026 point and range come from the preprint, not Table S6. Added the s1 citation (Abstract, p. 6).

Headline, dek and headings checked against their owners: −0.4%, the −1.5% to +0.6% range, the 2015 −0.6% projection and +0.06% first estimate, 243 Mt, 43.3 Gt. All match.

Every href opened as printed (curl, following redirects). All return 200 and land on the source. The s2 supplement DOI downloads the supplement zip, which is the source itself. Kinds: the NCC paper is marked primary and is not presented as independent (the prose says "by six of the budget's authors"). The GCP press release and the EIA STEO are primary, which is correct.

## Reads well

Nothing was cut for saying nothing. I ran the placeholder test on the first and last sentence of each paragraph, section and figure. Each one depends on its nouns or figures. The last sentence of the article ("A miss the size of 2015's would turn the projected fall into a rise of about 0.3%") is arithmetic the piece has set up, and it stays.

Nothing traced to the briefing. The commission's withdrawn "first projected decline" framing does not appear. The decisions log's "driven by oil alone" appears as a measured comparison (−243 against −158), not as the log's sentence. Nothing traced to the voice guide's exemplars. The bracketed working ([1.9 ÷ 20], [0.73 − 0.16]) follows the guide's advice on method, and none of Ritchie's wording is borrowed.

Against the recent record: the headline does not use "as" or "trades … for". The dek does not open with a possessive organization or "By … arithmetic". The outline ends on the projection record, not on a what-is-not-known table. The first flex section opens on the waterfall, not on a baseline framing.

One heading changed. "The 2015 projection's sign flipped, then flipped back" named a detail of the section. The section's argument is the average miss, and that miss is what the conclusion turns on. It is now "Past projections missed by 0.37 points on average". Read alone, the four headings now carry the argument in order. The prose register already matches the guide (it points at marks, says what they do, and gives the cause), so I lifted nothing else.

## The experience

I built the page with `nb preview` and captured it with Playwright at 390 px and 1280 px, in light and dark. There is no horizontal scroll and both PNGs load. The SVG's labels are clear in both themes and the dashed residual box reads as different from the measured sinks. The two Plotly PNGs keep a white panel in dark mode. Their type is small at phone width but readable, which is the export floor the writer reported. No component was added or cut. Each section already has one visual that its prose explains.

What the piece gives beyond its sources: it puts the 2026 projection on the budget's own 2015–2025 record of projected against realized growth, a record the budget tabulates but never charts or summarizes. It also shows that a typical miss is as large as the projected fall. That matches the original-work sentence in the handoff. The headline, read last, is the comparison the waterfall proves.

## Edits

- §2 (oil-falls-coal-and-india-rise), first paragraph: "reaches further than" → "is longer than".
- §2, fourth paragraph: "a university release reprinted by ScienceDaily said" → "ScienceDaily's edited version of the University of Exeter's release says".
- §2, NCC paragraph: "implies a short-run demand elasticity" → "would imply a short-run demand elasticity".
- §3 (land-use-lifts-total-co2), last paragraph: brackets 3.46 → 3.464 and 3.45 → 3.451.
- §4: heading, `data-nb-section` and `id` changed from "The 2015 projection's sign flipped, then flipped back" / `the-2015-sign-flipped-then-flipped-back` to "Past projections missed by 0.37 points on average" / `past-projections-missed-by-0-37-points`.
- §4, chart 2 caption: added s1 citation (Abstract, p. 6, 2026 projection and range).
- Ran `nb stamp`: 1189 words, 5 minutes, 9 sources. Full proof with links: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. The argument holds against the primaries, and the five breaks above were narrowing or precision fixes that are now made.
