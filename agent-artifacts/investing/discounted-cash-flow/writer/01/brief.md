# writer brief: investing/discounted-cash-flow (01)

Inputs:
  ../../editorial-direction.md            — house/press/template/series standard
  ../../commission.md                     — place in the course, what to teach
  ../../writing-coach/01/voice-guide.md   — craft (arithmetic carries the teaching)
  ../../researcher/01/evidence.md         — the complete claim set; cite only this
  ../../../../library/investing/discounted-cash-flow.html   — the initialized lesson
  ../../../../.nb-context/                 — effective template contract + furniture
Output: writer/01/draft-handoff.md
Proof:  ./nb check .nb-work/investing/discounted-cash-flow/library/investing/discounted-cash-flow.html --series investing --library /home/user/library-checkout

The lesson assembles concepts already taught (present value, free cash flow,
WACC): value the firm as PV of its free cash flow at its cost of capital. Rely
on the earlier lessons by reference; do not re-derive discounting.

Use the evidence exactly:
- Build the teaching on the illustrative firm the record constructed (FCFF
  $100M, +8%/yr for 5 explicit years, r=9%, g=2.5%); label it illustrative.
  Corroborate with Damodaran's real teaching cases (Tube Investments terminal
  value ~66% of firm value; DaimlerChrysler firm→equity bridge) cited as his
  teaching cases, not filings. Anchor "terminal value typically dominates" on
  Mauboussin & Callahan's sourced 70-80% range, not on a single constant.
- Spine (per commission + voice guide): a DCF is an argument about assumptions.
  Teach sensitivity by re-running ONE input at a time and letting the distance
  between two computed numbers be the argument. The record's preserved grid
  (EV and TV-share across r∈{8,9,10}%, g∈{1.5,2.5,3.5}%) is the material. A
  sensitivity table, or an `nb chart` of terminal-value share (or EV) vs g and
  r, is the natural furniture — use it if it explains better than prose; keep
  it honest (label axes, cite the data source = this lesson's own computation).
- Cover the enterprise→equity bridge (subtract net debt) and the terminal-value
  forms (Gordon growth TV=FCF(1+g)/(r-g); exit multiple). Address the live
  disagreements from Contradictions (how to pick g; whether exit multiples
  belong in a DCF; whether the sensitivity indicts the method or its users) —
  weigh them, do not just list them.

Craft: when a computed figure carries the claim, name only which input moved
and stand aside; state the fragility flat where the argument reaches it, not in
a closing caveat; keep the verdict on the tool, never on a security. Habits to
break (recent investing): do NOT build on Costco or Apple; vary the headline
from the "single concrete company fact" mold — find this lesson's own surprise
(e.g. how much of the answer rests on the terminal-value guess). If a chart is
built, inspect the rendered image before proofing.
