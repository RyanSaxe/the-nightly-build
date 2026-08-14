# Writer handoff: investing/enterprise-to-equity-value (01)

## Original work

The article takes Uber's Q2 2026 10-Q — a filing that nowhere states a
"bridge" — and assembles its scattered lines (debt note, investments note,
equity-method note, non-controlling-interest note, the basic-to-diluted EPS
reconciliation) into the two-step enterprise-value-to-price-per-share
argument, showing from Uber's own reported numbers, not asserted, that its
strategic stakes add more per share than its debt and dilution take away
combined, and separately identifying and resolving a mismatch the filing
itself never flags: the point-in-time share count behind its market quote
versus the period-averaged diluted count its own EPS footnote reports.

## Proof result

`nb stamp` then `nb check ... --series investing --library
/home/user/library-checkout` (first `--no-check-links` while iterating, then
with links checked): **BLOCK: 0**, verdict PUBLISHABLE, both runs.

Warning intentionally left: one `W-SENTENCE-DENSITY` (a 40-word sentence with
three clause joins somewhere in the source-list/bookend region per the tool's
count). I cut nine of ten sentence-density warnings from the first pass by
splitting the flagged sentences; I could not reliably isolate this specific
remaining sentence from the tool's message alone (no line locator, and my own
word-count checks against every long sentence in the body came up short of
40+3), and further blind splitting risked breaking the prose without
confidence it was the right target. It is a WARN, not a BLOCK, and the verdict
is already PUBLISHABLE.

## Open questions

None. The evidence record's two flagged gaps (RSU-specific proceeds not
separable from the blended $4.9B unrecognized-comp figure; no independent DCF
enterprise value for Uber) are both handled in the article as written: the
first by not attempting an RSU-only treasury-stock computation, the second by
back-solving an illustrative enterprise value from market cap and stating
that plainly, twice (in prose and in the closing Verdict note), as the brief
directs.
