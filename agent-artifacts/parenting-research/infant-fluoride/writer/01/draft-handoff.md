# Draft handoff: parenting-research/infant-fluoride (01)

## Original work

Across the AAP, ADA, USPSTF, Cochrane-toothpaste, and Cochrane-varnish
sources, no single cited document states that its own trial-age floor is
shared by every other evidence base behind the "start at six months"
guidance; the article cross-reads their population lines (Walsh's "1 to 6
years," Marinho's "1 to 15 years," USPSTF's own trial-age table) to make that
shared floor explicit in one place. On top of that cross-read, the article
draws a distinction none of the fourteen cited sources draws for the reader:
it treats the toothpaste/varnish age gap and the supplement/FDA gap as two
different kinds of uncertainty rather than parallel instances of "guidance
outruns evidence" — the first is an evidentiary gap that the fluorosis-timing
trials, read directly, show doesn't move the risk (so the toothpaste
guidance is safe to act on now), while the second is a live, unresolved
regulatory dispute between the FDA and standing pediatric guidance (so it
isn't). That distinction is what the closing section and its "settled /
not settled" framing turn on.

## Proof result

`./nb check .nb-work/parenting-research/infant-fluoride/library/parenting-research/infant-fluoride.html --series parenting-research --library /home/user/library-checkout` (links checked): **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**. No warnings were left in place; the initial pass surfaced 9 W-SENTENCE-DENSITY findings, all fixed by splitting the flagged sentences (confirmed against the engine's own `sentence_density` heuristic, not just re-running the proof blind).

`nb stamp` was run last after these fixes: words=2552, sources=14, reading_minutes=11 (series band 1200-3000; template flex-section band 2-6, used 5).

## Notes for the editor

- Sources 7 and 8 (Wong et al. 2024 fluorosis review; Wright et al. 2014 JADA
  review) carry `data-nb-kind="primary"` per the evidence record's own Kind
  line for each ("primary in principle... but read only at one remove" /
  "via an independent critical abstract"), even though both were read via a
  secondary rendering rather than the publisher's own page. Worth a second
  look if the house standard reads that hedge as "secondary" rather than
  "primary."
- The community-water-fluoridation policy dispute (Utah/Florida bans, the
  2024 EPA court ruling) is confined to two sentences at the end of the FDA
  section, explicitly marked as a separate question from the supplement-drop
  decision, per the commission's boundary.
- No source asset was captured. The evidence record flagged the CDC/AAP/ADA
  dosage table as a possible source asset, but the table's values (not its
  printed layout) are what the argument needs, so it is reproduced as an
  authored `nb-table` instead of a captured image.
