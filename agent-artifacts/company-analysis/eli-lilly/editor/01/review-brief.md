# editor review-brief: company-analysis/eli-lilly (01)

Inputs (read in the order your skill names):
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/editorial-direction.md
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/writing-coach/01/voice-guide.md
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/writer/01/brief.md  (the exact writer brief — for instruction-leakage checks)
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/researcher/01/evidence.md
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/writer/01/draft-handoff.md  (original-work sentence — open only on the third read)
- .nb-work/company-analysis/eli-lilly/library/company-analysis/eli-lilly.html  (the article; includes chart-1.py / chart-1.png)
- .nb-work/company-analysis/eli-lilly/.nb-context/  (template contract, furniture)

Output: .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/editor/01/editorial-review.md

After any direct prose cuts, run `nb stamp`. Inspect the chart per your skill:
compare chart-1.py's numbers to the evidence record and cited primary, and read
the rendered chart-1.png as a reader (labels, scales, honesty, cited source in
caption). The writer owns proof and any chart/markup change; route those back.

Recent-pattern notes (verify the writer broke these, don't reintroduce):
Recent company pieces opened with the beat-vs-bar headline number and marched
quarter-metric by quarter-metric, closing on "two ways to read it" or a
compounder thesis-check. The desk has leaned heavily AI-infrastructure lately;
this is a pharma piece and should not read like those. Headlines guide bans the
colon-subtitle headline and the hedged-contrast/comma-triad dek.

This round's focus (the writer flagged these open questions — resolve them):
- The CEO "produced at scale" call line: the writer paraphrased it and cites a
  third-party transcript (s4) as secondary only, attributing the -9% underlying
  US-price figure to the owning primary release (s1). Confirm this handling is
  honest (no quote attributed to a source that only reports it) or fix/route it.
- One uncited GLP-1 teaching clause: decide cite-or-cut and apply.
- Push hardest on the durability thesis and the decomposition's honesty: the
  piece must present the volume/price split as Lilly's OWN reported numbers with
  the unquantified FX/other residual acknowledged (worldwide +60% vol / -13%
  price vs +48% reported), not as independently derived fact. Verify the US -3%
  "flattered by rebate adjustments, ~9% underlying decline" claim traces to
  Lilly's own caveat. Confirm NO buy/sell/allocation call appears.
- Tariff: confirm it is framed as a contingent future risk Lilly is largely
  exempt from (not a live overhang), with the correct effective date.
- Audit every data-nb-kind and open every citation href (must resolve to the
  source's own page). Check all display-text figures against the owning primary.
