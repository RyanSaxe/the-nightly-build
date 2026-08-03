# Commission: investing/present-value

## Assignment
- Series: investing (Investing Course). Template: `lesson`. Mode: open.
- Slug: `present-value`. Subject: **the time value of money and present value —
  discounting future cash flows to a value today.**
- Authorized by the 2026-08-03 `nb duty` result. One article only.

## Where this sits in the emergent syllabus
Published lessons so far build the reading of a business and the hurdle rate:
income statement (how-a-business-earns-a-profit), cash flow (profit-versus-cash),
balance sheet (what-a-company-owns-and-owes), return on capital
(return-on-capital / ROIC), and cost of capital (cost-of-capital / WACC, the
most recent, 2026-08-02). Cost of capital taught the *rate* that a return must
beat. The unavoidable next prerequisite is what that rate is *for*: discounting.
Present value converts future cash into today's terms and is the mechanical
core of every valuation the course will later build (DCF). Teach discounting and
present value now; do not yet build a DCF or automate anything.

## Required contribution
Teach, from first principles, to a smart reader new to it:
- Why a dollar later is worth less than a dollar now (opportunity cost / the
  cost of capital already taught), made concrete with a worked example.
- The present-value formula PV = CF / (1+r)^t, and multi-period PV as a sum.
  Set it with the equation furniture (annotated form for the core PV
  identity). Show a small worked table discounting a few years of cash flows at
  a stated rate, arriving at a total PV.
- The discount rate is the cost of capital from the prior lesson: connect them
  explicitly so the course compounds rather than restarts.
- The idea of a terminal/continuing value and the perpetuity shortcut
  PV = CF/(r-g) at a level that sets up later DCF work, without turning this
  lesson into a full DCF. Name what is deferred.
Keep everything transferable to any investment, not tied to one company. Use a
company only if it makes the idea real; do not default to Costco again (used
heavily in prior lessons) or to a quarterly-earnings walkthrough.

## Sources
- min_sources: 6 (lesson template floor). Prefer authoritative, citable
  references for the formulas and definitions (a standard corporate-finance
  text or reputable primary explainer; a real Treasury yield or rate figure
  from its owning source to ground the discount rate example). Every URL must
  resolve. This is a teaching piece, so sources anchor definitions and the one
  or two real numbers used, not a news claim.

## Neighbors in this edition
company-analysis/reddit runs tonight and lives in the same Investing section;
it is a market-reaction case, not a valuation lesson. Keep this lesson's
worked example distinct from that piece.

## Prior coverage — do not repeat, and break these shapes
Do not reteach WACC/ROIC/statement-reading; rely on them by reference. Recent
lesson deks lean on a Costco/AEP figure ("Costco turns each invested dollar
into 37 cents of profit"). Do not open on the same company-figure reflex or
copy a prior lesson's section outline. Vary heading shapes.

## Form
Lesson template: opens on "Why this matters", closes on "The takeaway" (both
written after the body and both citation-exempt), with 0-4 flexible teaching
sections between. Word band 1200-2200. Use an annotated equation for the core
PV identity and a small table for the worked discounting. A "Next article" or
"In this article" note is available but not required; do not pad.

## Harness / model record
Harness: Claude Code (Agent SDK), scheduled publication run. Roles run as
isolated subagents on `claude-opus-4-8` (satisfies `capable`/`inherit`).
Per-role reasoning effort is not independently settable through the subagent
interface; each role runs at the session's effort, the closest available option
to the policy's guidance. Editor: model inherit -> `claude-opus-4-8`, effort
target high (ran at session effort). Recorded as a deviation on effort only.
