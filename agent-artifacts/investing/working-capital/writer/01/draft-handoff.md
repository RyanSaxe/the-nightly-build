# Draft handoff: investing/working-capital (01)

## Original-work sentence

The lesson turns the evidence's separate line items into one reproducible
procedure: it walks e.l.f.'s fiscal 2024 net income down through the four signed
working-capital change lines to show cash diverging from profit, then sets e.l.f.
and AutoZone side by side on the same three-count cash conversion cycle so the
reader can compute both and watch the same arithmetic flip sign, from about +132
days to about -33.

## Proof result

Final command, links included:

    ./nb check .nb-work/investing/working-capital/library/investing/working-capital.html --series investing --library /home/user/library-checkout

Result: BLOCK: 0, WARN: 0, verdict PUBLISHABLE. All internal (Background/Go
deeper/sibling-lesson) and external source links resolve. `nb stamp` recorded
words=1980, reading_minutes=9, sources=7 (4 primary, 3 secondary). No warnings
left standing.

During iteration, three W-SENTENCE-DENSITY warnings surfaced and all three were
fixed by splitting the sentences rather than repunctuating.

## Framing precision honored

- e.l.f. is presented as cash diverging from profit, not as negative operating
  cash: net income $127.7M vs operating cash $71.2M, a $56.5M gap, with the prose
  stating plainly that working capital "did not turn the year's cash negative"
  and that high-margin non-cash add-backs kept operating cash positive.
- The cash story uses the cash-flow-statement working-capital figures; the
  Naturium acquisition is named as the reason the balance-sheet deltas are larger
  than the operating cash uses, and the e.l.f. ~132-day cycle is labeled
  directional in prose, in the CCC table caption, and in the equation section.
- AutoZone is the clean negative-working-capital case (payables 114% of
  inventory, net working capital negative $1.18B, cycle about -33 days, OCF above
  net income), sourced to its own 10-K and MD&A.

## Furniture

Two `nb-table`s (the e.l.f. reconciliation of signed change lines; the
e.l.f.-vs-AutoZone CCC comparison) and one annotated `nb-math` equation
(CCC = DIO + DSO - DPO, three colored terms named in the legend). No
article-authored scripts or styles; no charts or source assets were needed.

## Open questions

None blocking. Note for the editor: e.l.f.'s DPO (68.5 days) rests on the
researcher's computed average accounts payable, since e.l.f.'s balance-sheet AP
balances are not itemized in the evidence record; it is presented only inside the
explicitly directional e.l.f. cycle, so no uncited figure stands on its own.
