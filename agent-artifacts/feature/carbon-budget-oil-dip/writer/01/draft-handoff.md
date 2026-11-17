# Writer handoff: feature/carbon-budget-oil-dip (01)

## Original work

The article sets the 2026 projected fall against the budget's own record of projected, first-estimated and currently estimated growth for 2015 to 2025, which the budget does not chart. The record gives an average central miss of 0.37 points (2015's 0.66 points would turn −0.4% into about +0.3%). The article also breaks the net −158 Mt down by fuel and shows that oil alone (−243 Mt) is larger than the net.

## Proof

`nb check ... --series feature --repo ...` with links: BLOCK 0, WARN 0, PUBLISHABLE. 1184 words, close to the 1200 ceiling. Any editor addition needs a matching cut.

Visuals were checked in `nb preview` with Playwright at 390 px and 1280 px, in light and dark. No horizontal scroll. The SVG labels are clear in both themes after the viewBox was widened. The two PNG charts render at the engine's fixed 1200×675 export, so their type is small on a phone even after fonts were raised to 26–36 px. They are legible, but that is the format's floor.

## Calls made that the editor may want to check

- Chart 2 leaves out 2020 (projected −6.7%, no range) so the scale stays readable, and the caption says so. 2016 is plotted as Table S6 lists it (−0.2%), and the caption notes that the 2016 budget printed +0.2%. Nothing in the prose depends on the 2016 sign.
- India ≈ +141 Mt and China ≈ −112 Mt are in prose only, marked "derived by us". The citation's `data-nb-note` gives the method.
- The "sixth-largest oil fall since 1959" ranking, the "highest total in the dataset" claim and the "about five days" remaining-budget arithmetic are the paper's own calculations from the evidence record's Numbers.
- The 68%-range count is given as a count (0 misses in 10 against about 3 expected), with no claim about calibration, as the researcher asked.
- Carbon Brief, IGCC and GCB2025 key-targets are not cited. The commission dropped the 150 vs 165 line, so nothing needed them.

## Open questions

None blocking. The chart-legibility floor on phones is a format limit for the orchestrator to note, not something this article can fix.
