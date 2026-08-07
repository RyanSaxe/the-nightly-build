# Draft handoff: investing/discounted-cash-flow (02, revision)

Single-owner repair of editor/01's two required items. No new claims; every
verified figure and the editor's two "about a seventh" edits stand.

## Required items resolved
1. Bridge terminology unified on **enterprise value** for the $1,844.7M
   operating-asset figure (PV of FCFF at WACC), across prose, the four-line
   table (row relabeled "Enterprise value"), the equation figcaption (now
   defines the term at first use), the chart figcaption, and the chart alt/axis
   (already read "enterprise value," so chart-1.py was unchanged and no
   re-render was needed). The DaimlerChrysler example is reconciled honestly
   rather than called "the same subtraction": Damodaran's operating assets
   (112,847) are named as his enterprise value, and adding cash then subtracting
   gross debt is shown to be subtracting net debt (64,488 gross debt less 18,068
   cash), the identical net-debt bridge run on the illustrative firm. The
   ambiguous "firm value = 130,915" label was dropped so one term names one
   quantity. The Tube Investments corroboration was also moved to "enterprise
   value" for consistency.
2. "Year six's cash is $136.05 million grown by 2.5%" reworded so year six's
   figure is on the page: "Year five's cash of $136.05 million grows 2.5% to
   $139.45 million in year six," which over the 9%-2.5% gap becomes the $2,145M
   terminal value.

## Chosen term
**Enterprise value** — used for the $1,844.7M / $1,845M operating-asset figure
everywhere it appears (prose, table, both figure captions, chart alt and axis),
defined once at the identity equation as "the worth of the whole operating
business."

## Proof
`./nb check ... --series investing` (links included): BLOCK: 0, WARN: 0,
PUBLISHABLE. Stamped words=2149 (band 1200-2200), reading 9 min, sources 6.
