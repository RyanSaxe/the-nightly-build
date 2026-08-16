# Draft handoff: investing/margin-of-safety (01)

## Original-work sentence

The article converts the evidence record's static $236–$518 value range into a
live sizing decision: it computes the margin of safety at Adobe's $264.02 price
against the conservative value, the midpoint, and the optimistic value to show
the same price is at once a 12 percent premium and a 30 percent discount, then
pins that whole gap on stage-1 growth as the one input that decides how wide the
cushion must be. The work is visible in the margin table, the price-for-a-real-
margin figures (~$165 and ~$189), and the one-input sensitivity table.

## Proof result

`./nb check … --series investing --library <checkout>` with links on:
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Stamped words=2138,
reading_minutes=9, sources=6. No warnings left standing. `nb render-check`
reported "no Chrome in this environment; skipped", so the KaTeX equation and the
three tables were verified through the deterministic proof and static markup, not
a live browser render.

## Open evidence question (for the orchestrator/editor)

The lesson template floor is 6 sources (`source-policy` confirms
`min_sources: 6`), but the researcher's evidence record supplies 5 distinct
sources: Graham, Damodaran's "DCF Myth 3" (2016), Adobe's 10-K, Adobe's 10-Q,
and the stockanalysis price. To meet the floor I added a sixth, cited as source
3: Aswath Damodaran, "Discounted Cashflow Valuations (DCF): Academic Exercise,
Sales Pitch or Investor Tool?" (2015). It is primary, resolves, and was supplied
with verified quotations and its URL in the writing coach's voice guide; it
carries the in-record claim that a valuation is only an estimate, "almost
guaranteed to be wrong, and more wrong when there is more uncertainty," which the
orientation leans on. The two Damodaran essays do distinct work (the 2015 piece
on the estimate being guaranteed somewhat wrong; the 2016 piece on classifying
uncertainty and demanding a bigger cushion rather than stopping), so this is not
padding, but it does reach one source beyond the evidence record. Please confirm
you are comfortable citing a voice-guide-sourced essay as a body source, or have
the researcher fold it into the evidence record so the claim set and the source
floor agree.

No open voice question. Register followed the guide (calm, first-principles,
figures carrying the point, body addresses no one, the two bookends turn to the
reader).
