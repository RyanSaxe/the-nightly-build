# Editorial review: investing/discounted-cash-flow (editor/02)

Confirmation re-read of the writer's round-02 repair against the two required
items in editor/01. No new full read; scope limited to the fixes and to
guarding against regressions.

## Skeptic

Both required items are resolved, and the arithmetic behind the reconciliation
holds.

**Item 1 — one term for the $1,844.7M operating-asset figure.** The draft now
names it "enterprise value" everywhere it appears, defined once at the identity
equation ("Enterprise value, the worth of the whole operating business, is the
present value of an explicit forecast plus the present value of a single
terminal value"). I grepped every occurrence of "firm value / enterprise
value": thirteen hits, all "enterprise value," zero residual "firm value"
label for the figure. It is consistent across the equation figcaption, the
table row (relabeled "Enterprise value," "The whole operating business: 450 + 1
394"), the move-one-number prose (falls to 1,593, rises to 2,114, grid 1,647 to
2,114), the chart figcaption and alt text, the data-nb-note (now "enterprise-
value identity"), the firm-to-share heading and prose, and the Tube
Investments corroboration (now "two-thirds of enterprise value"). The remaining
uses of "the firm" are verbs ("value the firm from its own cash") or the FCFF
term ("free cash flow to the firm"), not competing labels for the number.

**The DaimlerChrysler reconciliation is honest, and one operation now runs both
firms.** The illustrative firm subtracts net debt from enterprise value
directly: 1,845 − 300 = 1,545, and 1,545 / 100M shares = $15.45. Damodaran's
case is shown "the long way" and reconciled: operating assets 112,847 (named as
his enterprise value) + cash 18,068 − gross debt 64,488 = equity 66,427, or
72.7 DM/share. I checked the reconciliation both ways: 112,847 + 18,068 −
64,488 = 66,427; and net debt = 64,488 − 18,068 = 46,420, so enterprise value −
net debt = 112,847 − 46,420 = 66,427. The two routes agree to the D-mark, and
the equity, per-share figure, and cash/debt numbers all match the evidence
record. The ambiguous "firm value = 130,915" label is gone, and the
inaccurate "the same subtraction" is replaced by "the same bridge... written
the long way," which is true: adding cash and subtracting gross debt is
subtracting net debt.

**Item 2 — year-six cash shown.** "Year five's cash of $136.05 million grows
2.5% to $139.45 million in year six. Over the gap between 9% and 2.5%, that
year-six cash becomes a terminal value of $2,145 million at year five." The
$139.45M figure is now on the page (136.05 × 1.025 = 139.45; 139.45 / 0.065 =
2,145). Resolved.

**Round-01 edits and verified figures intact.** Both "about a seventh"
corrections stand (move-one-number line and takeaway). Spot-recheck of the
load-bearing figures against my round-01 recomputation: explicit PV 450,
terminal 2,145, PV terminal 1,394, enterprise value 1,845, terminal share
75.6%, sensitivity 1,593 / 2,114 with 13.7% / 14.6%, grid span 1,647 to 2,114,
exit multiple 1,600 vs 2,145 (a quarter), Tube two-thirds, growth cap 5.93 vs
6.67 — all unchanged and correct. No new arithmetic or terminology slip
introduced.

## Cut

No cut needed. The repair added roughly one clause of reconciliation prose
(words 2095 → 2149, inside the 1200-2200 band) and nothing in it earns removal:
the reconciliation sentence carries a reasoning step the lesson previously
skipped. The chart script was untouched (its axis already read "enterprise
value"), so no re-render was required. I made no direct edits this round and
did not restamp.

## Reader

The firm-to-share section, the one place round 01 fractured, now reads clean:
one term for the operating-asset value, one bridge (subtract net debt) shown on
both the illustrative firm and a real one, with the long-form Damodaran version
explicitly tied back to it. The lesson still gives what its sources alone would
not: a single firm carried end to end so dominance and fragility of the
terminal value arrive as one reproducible fact. The prose sits with the
voice-guide exemplars.

## Edits

- None this round. No stamp run (no edit made).

## Required work

- None.

## Decision

approve — both required items are resolved, the DaimlerChrysler reconciliation
is arithmetically honest with one net-debt bridge now running both firms, the
year-six cash is explicit, and every previously verified figure and edit
remains intact with no new slip.
