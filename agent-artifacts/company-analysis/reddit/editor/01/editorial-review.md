# Editorial review: company-analysis/reddit (editor/01)

## Skeptic

Thesis: Reddit's Q2 2026 was a genuine beat-and-raise, yet the stock lost about a
fifth of its value in one session because the one forward signal its valuation
underwrites, US daily active uniques, both missed consensus and fell
sequentially for the first time in the five-quarter series. Price moves on the
change in expectations, not the level of results.

Load-bearing claims and how each held:

- **Revenue $804.9M (+61%), EPS $1.25, Q3 guide $860-870M.** Verified against the
  owning primary (s1, Reddit Q2 2026 press release). I opened the filing: it
  carries 804.9, 1.25, 860, 870, 130.3, 77.1, 514.6, 261, 638, and 53.2. All
  match. The +61% and the $865M-midpoint "about 48 percent above" the $584.9M
  September-2025 base (s6) are correctly derived by the writer from the primary
  series, not lifted from a gated figure. 865/584.9 = 1.479. Holds.

- **US DAUq 53.2M missed the 53.98M Zacks consensus and fell from 53.5M (first
  sequential decline in five quarters).** 53.2 vs 53.98 confirmed in s3
  (Yahoo/Zacks); 53.5 confirmed in the Q1 2026 primary (s4); the rising run
  50.3 -> 51.6 -> 52.5 -> 53.5 is owned by s5/s6/s7 and cited where stated. The
  central claim survives its hardest push: the sell-off is not "market punished a
  clean beat," it is a rational-looking re-rating of a durability signal that the
  headline hides. The piece states this and steelmans it.

- **~-21% close-to-close ($178.04 -> $140.67, -20.99%).** Confirmed in s2
  (stockanalysis daily history shows both closes). The headline "lost a fifth"
  and stat strip "-21%" are honest.

- **Consensus and the tape are secondary.** Every data-nb-kind is honest: s1,
  s4, s5, s6, s7 (Reddit releases) and s8 (Reddit Letter) are primary; s2 (price
  aggregator), s3 (Zacks/Yahoo), s9 (Motley Fool) are secondary. Reddit owns the
  financials and guidance; it does not own "what the Street expected" or the
  tape, and the article labels those accordingly. The provider spread (Zacks vs a
  higher bar) is disclosed rather than hidden.

- **Display text.** Headline, dek, and all five subheads were checked descriptor
  by descriptor. The dek is figure-led and uses none of the barred molds
  (masks/already-exceeds, semicolon reversal, suspended question, comma-triad
  with "and"). CEO title "Steven Huffman, President and CEO" matches the filing
  signature. The blockquote matches the Letter verbatim.

- **Citations resolve.** I opened all nine hrefs as printed. The six SEC URLs
  return 200 with a descriptive User-Agent (the initial 403 is SEC's bot policy,
  not a dead link); s2, s3, s9 return 200 directly. Each lands on the source that
  carries its cited figures (verified by fetching and matching the numbers).

One break found and fixed directly: the article stated "a smaller dip near 13
percent had shown up in the after-hours minutes," cited to s2. s2 (close-to-close
prices) does not own an after-hours figure, and the evidence record's own
after-hours range is -7% to -11%, so no available source owns a -13% after-hours
number. The commission only *permitted* noting it; it was miscited and
unsupported, so I cut it (nonessential; the close-to-close -20.99% is intact and
sourced).

## Cut

Direct cuts and fixes:

- Removed the unsupported/miscited "-13% after-hours" sentence (see Skeptic).
- Cut "and separating them is the point" from the section-5 opener: a method
  signpost that grades what the article is doing instead of doing it. The two
  reads that follow separate themselves.
- Fixed the Fig. 3 caption: "The level keeps climbing" contradicted the chart it
  labels (revenue dips Q4'25 $726M -> Q1'26 $663M). Changed to "The level trends
  higher," which is honest against the visible series.
- Fixed the byline placeholder "N min read" -> "7 min read." nb.js does not
  populate the byline (normalizeByline skips any span already containing "min
  read"), and stamp writes only the meta JSON, so the literal "N" would have
  rendered to every reader. reading_minutes is 7.

Worst tell (now gone): "separating them is the point" was the only self-grading
line. No prompt leakage survived the comparison with the writer brief: the
transferable-lesson phrasing is the article's own argument, not an instruction
artifact or an "assignment fulfilled" claim. No run-ons, splices, or em-dash
chains. Heading shapes are varied; two of five share a "The X that Y" frame,
which is within tolerance, not a formula. Furniture (stat strip, table, three
charts, note, pull quote) each carries evidence.

## Reader

What the piece gives beyond its sources: a portable subtraction. No single source
tells the reader to isolate the one forward signal a price underwrites (US DAU),
hold reported level apart from the change in expectations, and see why a
beat-and-raise can still be a defensible ~21% sell-off. The draft-handoff's
original-work sentence claims exactly that, and the article delivers it. The prose
sits closer to the Damodaran/Thompson exemplars than a median summary: it poses
the framing question and answers it with figures immediately, personifies "the
market"/"expectations" only where a specific number follows (53.98M, $743.9M),
reads one chart inflection (growth rolling to 61%, the sequential DAU dip) rather
than narrating every point, and closes by handing over the method with no
buy/sell/allocation call. No call appears anywhere; the ending explicitly refuses
the verdict.

Charts: all three inspected against their committed chart-N.py and the evidence.
chart-1 (Fig. 1, US DAUq) plots 50.3/51.6/52.5/53.5/53.2 with the 53.98 Zacks
marker above and a labeled sequential-decline arrow, axes labeled, source cited.
chart-2 (Fig. 3, revenue + YoY) plots 499.6/584.9/726/663/804.9 and 78/68/70/69/61
on a dual labeled axis. chart-3 (Fig. 2, guidance vs actual) plots the four issued
ranges and three actuals, with Q3'26 marked "not yet reported." Numbers match the
primary; the two truncated y-axes (49-55 and 560-900) are reasonable for the
comparisons and are labeled. All honest.

## Edits

- Cut the unsupported/miscited "-13% after-hours" sentence in the orientation section.
- Cut "and separating them is the point" from the "Two ways to read a one-fifth day" opener.
- Changed Fig. 3 caption "keeps climbing" to "trends higher" (revenue is non-monotonic).
- Changed byline "N min read" to "7 min read".
- Ran `./nb stamp` on the article: words=1646, reading_minutes=7, sources=9.

## Required work

None blocking. Non-blocking notes for the orchestrator's awareness, no action
required to publish: (1) "traded at a rich multiple" in read one is a defensible
qualitative premise but carries no cited multiple, because the evidence record
holds none; the writer correctly did not invent one, and the argument does not
rest on the exact figure. (2) If a -13% after-hours way-station is wanted back,
that is a researcher item: it needs an openable source that owns the after-hours
figure.

## Decision

approve — the load-bearing numbers, chart provenance, source kinds, and resolving
citations all check out, no call is issued, and the remaining defects were
surgical fixes made directly.
