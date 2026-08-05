# review-brief: investing/free-cash-flow (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/editorial-direction.md — governing standard, `lesson` identity, series prompt, declared reader
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/writer/01/brief.md — the exact writer brief (instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/writing-coach/01/voice-guide.md — voice guide (read FIRST)
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/researcher/01/evidence.md — the evidence (verified Apple figures)
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/writer/01/draft-handoff.md — handoff + original-work sentence + open question
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/library/investing/free-cash-flow.html — the article to review (make direct cuts HERE)
- /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/investing/free-cash-flow/agent-artifacts/investing/free-cash-flow/editor/01/editorial-review.md

Run environment: harness = claude-code, model = inherit (Opus-class), high effort (REQUIRED stage).

Recent-pattern notes:
- Break the shapes of `investing/profit-versus-cash` and `return-on-capital` (opener/closer/headings). `nb history --structure` if needed; use only as a negative constraint.

This round's focus:
- **Every Apple figure must be recomputed and matched to the owning primary (FY2025 10-K):** net income 112,010; operating cash flow 111,482; capex (payments for acquisition of PP&E) 12,715; FCF = 98,767; and the FY2024 comparison (OCF 118,254, capex 9,447, FCF 108,807; net income 93,736). Confirm the headline claim "profit rose while free cash flow fell" is exactly the ~19% up / ~9% down the filing supports, with the right denominators/periods (USD millions; fiscal years ended late Sep). A wrong number in display text (the headline carries one) is the costliest error.
- Verify FCF is presented as a constructed non-GAAP measure (SEC C&DI 102.07 cited) and that FCFF/FCFE are NOT conflated with the OCF−capex figure. Statement structure anchored to IAS 7 (href resolves); confirm no non-resolving FASB href is printed. Open every citation href.
- `lesson` template gates: fixed order (Why-this-matters → body → takeaway); NEITHER bookend summarizes the body; opener sets up what the takeaway resolves; every term defined in plain words at first use; 2-3 ideas taught completely (not shrunk). Background lists earlier lessons as optional; the lesson stands without them.
- Writer's open question: the two Go-deeper rows also appear in the source list — rule whether Go-deeper should be distinct from cited sources (minor; not blocking). 
- Furniture: the OCF→FCF bridge table and the FCFF/FCFE equation must each carry reasoning, not decorate; check the table numbers against the evidence.
- Second read (cut): enforce prose/punctuation standards (the writer already split one semicolon-chain — check for others). Third read: what does the reader get beyond the sources (the constructed two-year bridge), and is the prose closer to the voice-guide exemplars than a median summary?
- After any direct cuts run `nb stamp`. Decision: approve or revise, naming each required item's owner.
