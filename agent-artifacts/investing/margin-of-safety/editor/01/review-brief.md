# editor review-brief: investing/margin-of-safety (01)

Inputs (paths relative to the workspace root `.nb-work/investing/margin-of-safety/`):
- `agent-artifacts/investing/margin-of-safety/editorial-direction.md`
- `agent-artifacts/investing/margin-of-safety/commission.md`
- `agent-artifacts/investing/margin-of-safety/writer/01/brief.md` — the exact writer brief (check the draft against it for leakage)
- `agent-artifacts/investing/margin-of-safety/writing-coach/01/voice-guide.md`
- `agent-artifacts/investing/margin-of-safety/researcher/01/evidence.md`
- `agent-artifacts/investing/margin-of-safety/writer/01/draft-handoff.md`
- `library/investing/margin-of-safety.html` — the drafted lesson (proof passes at BLOCK: 0, links included)
- `.nb-context/` — effective template contract and furniture catalogs

Output: `agent-artifacts/investing/margin-of-safety/editor/01/editorial-review.md`

## Recent-pattern notes (investing desk, to catch formula)
- Recent lessons open their first body section on "What the [shortcut / terminal value] leaves out / takes on faith." Confirm this opener is not that mold.
- Recent lessons are built as a two-named-company head-to-head (Copart/Crocs, Coca-Cola/Verizon). This one should be Adobe's value against its price, no forced second company. Confirm.
- Recent deks are number-punch one-liners ("worth four times", "roughly triples"). Confirm this dek is its own construction.

## This round's focus
- Arithmetic is load-bearing. In the skeptic read, recompute the Adobe range and the margins against the evidence record's inputs: conservative ~$235.66, optimistic ~$518.03, price $264.02, and the resulting margins (a ~12% premium to conservative, a ~30% discount to the midpoint). The whole lesson rests on these numbers being right and on stage-1 growth being the swing input.
- The $236 and $518 endpoints must read as outputs of stated assumptions, never as figures Adobe reported. Confirm the after-tax-operating-income choice and the ~$1.9B stock-comp add-back are explicit where NOPAT first appears.
- Source floor and the 6th source: the researcher record held 5 sources against the lesson's 6-source floor, so the writer added Damodaran's 2015 "DCF: Academic Exercise, Sales Pitch or Investor Tool?". The orchestrator accepts a sixth source in principle, but it must hold as read and supporting. Open that citation's href yourself, confirm it resolves and that the passage genuinely supports the exact claim it is attached to (not merely the general topic), and confirm the article legitimately carries 6 real, distinct sources. If the 6th does not hold up, route it to the researcher to source the claim properly rather than letting a thin citation stand.
- Graham is cited to ch. 20 as read with a locator; confirm no page or edition detail was invented.
- The math furniture (the value-bridge equation) and the three tables were validated by the deterministic proof only; `nb render-check` was skipped for lack of Chrome. Read the KaTeX and table markup carefully for anything a browser render in CI would break.

The lesson template allows the `why` and `takeaway` bookend cards to address the reader; judge them like any other sentence for whether they say something. Open every citation href. Verify display text descriptor by descriptor. Edit directly what you own; route only reporting, evidence, or a redraft. You are the required fresh-eyes editor at high effort; make all three reads.
