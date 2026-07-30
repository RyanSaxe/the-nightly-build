# Editor review brief — company-analysis/boeing (invocation 01)

## Role
Fresh-eyes editor. Give the drafted article three ordered reads — skeptic, cut,
reader — per `skills/editor/SKILL.md`. Make surgical cuts and small prose fixes
directly; return anything past a word or clause to the writer, evidence gaps to
the researcher. Approve only with a DONE verdict and no required change.

## Exact inputs
- This review brief.
- `editorial-direction.md` (house floor, headline standard, press voice, template
  identity, series prompt).
- The exact writer brief: `writer/01/brief.md` (so prompt leakage is detectable).
- `writing-coach/01/voice-guide.md`.
- `researcher/01/evidence.md`.
- `writer/01/draft-handoff.md` (open the original-work sentence only in the third
  read).
- Article: `library/company-analysis/boeing.html`; chart provenance
  `library/company-analysis/boeing/chart-1.py` and `chart-1.png`.
- Template context under `.nb-context/`.

## What to test hardest
- The thesis: the operational recovery is real, but the reported operating-cash
  swing is a customer-advances (working-capital) inflow, and free cash flow for the
  half is still negative. Try to break it. Recompute: operating cash flow $1,185M;
  advances +$4,660M; inventories $(3,859)M; capex $(2,008)M; free cash flow
  $(823)M. Check the "ex-advances used ~$3.5B" and the waterfall identity plug
  (+819). Confirm each figure against the owning primary in the evidence Numbers
  section; the GAAP working-capital lines belong to the 10-Q, the non-GAAP free
  cash flow to the releases.
- Audit every `data-nb-kind`: six primary, two secondary; no Boeing figure resting
  on a secondary; the recovery framing (S2/AeroTime) used as a claim to test, not
  as a source of fact.
- Headline and dek as claims: retest against `spec/headlines.md` (no colon-
  subtitle, no hedged question, no semicolon-reversal / comma-triad dek; one earned
  contrast ceiling). The dek must make a claim about the world, not grade the piece.
- Cut: run the delete test; hunt self-grading, stock-revelation frames, signposts,
  prompt leakage against the writer brief; hold punctuation (period-default, em-dash
  discipline). Inspect the chart image and its provenance for honesty.
- Reader: what does the piece give beyond the filings? Compare with the writer's
  original-work sentence. Judge voice against the guide's exemplars. Reread the
  headline as the largest claim.

## Proof
The writer runs `nb check`; current state is BLOCK 0 / WARN 0. If a required change
lands, the writer reruns to BLOCK 0.

## Return
`DONE editor <editorial-review-path>` only with no redraft required, else
`REQUEST writer …` / `REQUEST researcher …`.
