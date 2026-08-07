# Editorial review: investing/discounted-cash-flow (editor/01)

## Skeptic

Thesis: the terminal value is at once the largest part of a DCF answer and the
shakiest, so a DCF is best read as an argument about two or three assumptions
rather than a machine that prints a company's worth. The load-bearing claims:
(1) most of a firm's value sits in the terminal value — three-quarters in the
worked firm, 70-80% typically; (2) that same terminal value is the most
sensitive, a one-point move in r or g swinging the answer roughly a seventh;
(3) the enterprise-to-equity bridge is a subtraction, so the judgment lives
upstream in the cash flows and terminal value; (4) the authorities split on
whether the sensitivity indicts the tool or the hand, but agree the fragility
is real and lives in the inputs. The draft states all four cleanly.

Arithmetic was the top risk, so I recomputed the illustrative firm from the raw
inputs (FCFF $100M, +8%/yr for five years, r=9%, g=2.5%) rather than trusting
the evidence record.

- Explicit FCFF: 100, 108, 116.64, 125.97, 136.05. PV at 9% = 91.74 + 90.90 +
  90.08 + 89.24 + 88.42 = **$450.4M**. Article says $450M. Matches.
- TV_5 = 136.05 x 1.025 / (0.09 - 0.025) = 139.45 / 0.065 = **$2,145.4M**.
  Article $2,145M. Matches.
- PV of TV = 2,145.4 / 1.09^5 = 2,145.4 / 1.53862 = **$1,394.4M**. Article
  $1,394M. Matches.
- Enterprise value = 450.4 + 1,394.4 = **$1,844.7M** -> $1,845M. Matches.
- Terminal share = 1,394.4 / 1,844.7 = **75.6%**. Matches the table and the
  "three-quarters" headline.

I then recomputed all nine sensitivity-grid cells independently. Every one
lands on the evidence grid to the rounded dollar: r=8% row 1,909 / 2,189 /
2,593; r=9% row 1,647 / 1,845 / 2,114; r=10% row 1,447 / 1,593 / 1,783. The
TV-share grid (69.7% to 82.1%) also reproduces. The article's specific
sensitivity sentences check out: r 9->10% at g=2.5% gives 1,593 (down 13.66% ~
13.7%); g 2.5->3.5% at r=9% gives 2,114 (up 14.61% ~ 14.6%); g 1.5->3.5% at
r=9% spans 1,647 to 2,114. The exit-multiple illustration (200 x 8 = 1,600 vs
2,145, a 25.4% cut) and the Tube Investments ~two-thirds and DaimlerChrysler
bridge (130,915 - 64,488 = 66,427, 72.7 DM/sh) all match the evidence. The
1954-2015 growth-cap data (5.93% vs 6.67%) and the g->r infinity statement
match Damodaran.

Prose, table, and chart agree with each other and the evidence. The chart-1.py
provenance recomputes EV(r,g) with the same identity and the same held-fixed
explicit stream; its plotted points (base case ~1,845 on the r=9% line, 8%/9%/
10% lines at 2,189/1,845/1,593 at g=2.5%) match the grid and the alt text.

One arithmetic overstatement did break. "More than a seventh in either
direction" (move-one-number section) and "more than a seventh" (takeaway) are
both false for the smaller single-point moves: r up a point is -13.7% and g
down a point is -10.7%, both under a seventh (14.29%). Only the up moves exceed
it. The honest central figure is "about a seventh," which the draft handoff
itself uses. I softened both in place. The dek's "fifteen percent" is the
g-up move (14.6%) rounded, defensible for a one-line dek.

Display text verified descriptor by descriptor. Headline: "Three-quarters"
tracks the 75.6% base share; it is off the recent "single concrete company
fact" mold and carries subject-verb-surprise. Dek commits to a claim about the
world (the terminal chunk is shakiest; a one-point g move swings ~15%), not a
grade of the article. Section headings each name a step in the piece's own
nouns, shapes varied, no scaffolding slots. Every named figure in display text
is sourced.

Citations: all six `data-nb-kind="primary"` labels are defensible (each author
owns the claim it carries; CFA and Mauboussin are the independent
corroborators the standard asks for). I opened the hrefs. The CFA 2026 reading
resolves and states the identity, constant-growth formula, and equity bridge as
cited. The Morgan Stanley landing page resolves with the right authors and
title; the 70-80% quote lives in the PDF it hosts, which is the source's own
canonical page and the deliberate choice recorded in the evidence. All three
Damodaran PDFs resolve to the exact cited files. No miscitation found.

The one conceptual break is in the firm-to-share section, and it is not
arithmetic — it is terminology and teaching. The lesson states the bridge as
"subtract net debt (debt minus cash)" and runs it on the illustrative firm:
$1,845M - $300M = $1,545M. Here $1,845M is operating-asset value (PV of FCFF),
and cash is handled inside net debt. It then says "Damodaran runs the same
subtraction on a real firm" and shows operating assets 112,847 **plus cash**
18,068 = firm value 130,915, **minus gross debt** 64,488 = equity 66,427. That
is not the same subtraction: one subtracts net debt from operating assets, the
other subtracts gross debt from a cash-inclusive figure. Both reach equity
correctly, but "firm value" now denotes two different quantities (operating
assets in one case, operating assets plus cash in the other), and the chart
labels the very same $1,845M "enterprise value," a third undefined term for it.
For a lesson whose whole job is to teach this bridge cleanly, reusing one name
for two amounts and calling two different procedures "the same subtraction"
undercuts the teaching. This needs the writer; a word-swap would paper over it
without resolving which quantity "firm value" names.

## Cut

The piece is already lean and I found no earns-its-place failures to remove. No
prompt leakage: the brief's framing language ("an argument about assumptions,"
"re-run one input") is recast as teaching, not copied, and there are no
planning labels, selection rules, or claims that the article fulfilled its
assignment. Banned-terms and run-on checks came back clean on the read (the
proof reported WARN 0). Punctuation is plain; the two "not X, it is Y" moves
(the why bookend's "The aim is not to trust the number. It is to know which
guess..." and the takeaway's "not a machine... It is a way...") each correct a
real, named misconception and stay within the one-or-two ceiling. The verdict
note earns its emphasis and lands on the tool, never a security. The chart is
evidence, not decoration: it carries the r/g fan-out the prose could only
assert. My only edits were the two "seventh" corrections above; both are
within-clause fixes, no new prose.

One clarity nit I left for the writer rather than touch: "Year six's cash is
$136.05 million grown by 2.5%" reads as if $136.05M (year five's figure) is
year six's cash. The result ($139.45M) is never shown even though the voice
guide asks the figure to be the payload. Minor, non-blocking, but worth a pass.

## Reader

What the piece gives beyond its sources: a single firm carried all the way
through so that "the terminal value dominates" and "the terminal value is the
most fragile input" arrive as one reproducible fact rather than two borrowed
assertions, with the reader handed the inputs to rerun. That is exactly the
original-work claim in the draft handoff, and it survives the read. The prose
sits closer to the voice-guide exemplars (Damodaran's grid-teaches-the-point
move, the flat declarative of the weak point) than to a median summary: the
numbers do the arguing and the prose names only which input moved. The one
place the reading stumbles is the firm-value/bridge section, where the
terminology fractures.

## Edits

- move-one-number: "moves the answer more than a seventh in either direction"
  -> "about a seventh" (the down moves are 13.7% and 10.7%, under a seventh).
- takeaway: "moves the whole valuation by more than a seventh" -> "about a
  seventh" (same reason).
- Ran `./nb stamp`; words 2097 -> 2095, sources 6, reading 9 min.

## Required work

- **writer** — Fix the firm-to-share section so "firm value" names one quantity
  throughout. As written, the illustrative bridge subtracts net debt from
  operating-asset value ($1,845M) while the DaimlerChrysler bridge adds cash
  and subtracts gross debt from a cash-inclusive "firm value" (130,915), and the
  chart calls the illustrative figure "enterprise value." Pick one term for the
  operating-asset value and reconcile the two bridge forms (net debt vs. cash
  minus gross debt), or drop the "the same subtraction" claim, which is not
  accurate as stated. Markup/asset changes (the chart axis label and the img
  alt text saying "enterprise value") are the writer's to align, not mine.
- **writer** (minor) — Reword "Year six's cash is $136.05 million grown by
  2.5%" so year six's figure ($139.45M) is the one on the page; as written the
  year-five number reads as year six's cash.

## Decision

revise — the arithmetic is sound and now matches the article throughout, but a
lesson that teaches the enterprise-to-equity bridge cannot use "firm value" for
two different quantities and call two different procedures "the same
subtraction"; that needs the writer.
