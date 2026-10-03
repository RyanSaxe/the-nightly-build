# writer brief: feature/ai-economy-atlas (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- voice-guide.md (../../writing-coach/01/voice-guide.md)
- evidence.md (../../researcher/01/evidence.md) — the complete claim set; draft only from it.
- commission.md (../../commission.md) — the angle and the original-work target.
Output: ../../writer/01/draft-handoff.md (edit the article in place at
  .nb-work/feature/ai-economy-atlas/library/feature/ai-economy-atlas.html)
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/ai-economy-atlas/library/feature/ai-economy-atlas.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Documented markup only (`.nb-context/`). Ask me if the evidence
cannot supply a fact you need.

The angle holds, and the evidence sharpened it. Settled points to build on:
- The ATLAS work "shares" are, by the dataset's own data dictionary, shares of
  conversational-request VOLUME within a geography (classifier over 14,653,926 Gemini
  App/AI Mode/API interactions, 6-19 April 2026, paid/enterprise API excluded) — not
  shares of jobs, of task-help, or of labour hours. Both Google papers say so in their
  own words (ATLAS Sec 2.3 "measures behavioral interactions, not definitive productivity
  outcomes"; AI-in-Science fn 14 "we only know the absolute numbers of requests ... we
  also do not see task completion or saved time"). This is the piece's spine.
- The interactive separates two axes: usage-VOLUME share vs task-SATURATION depth
  (~21% of tasks in the median occupation). The verified global major-group series
  (volume / saturation / automation / non-routine-cognitive for all 22 groups) is in the
  evidence Numbers section and is the material for a chart contrasting volume-share
  against saturation depth. Build the chart only from that verified series, with `nb chart`;
  look at the rendered image; cite the data source in the caption.
- Attribution discipline on the headline numbers: the U.S. ~30% computer/math figure and
  the per-country multipliers (India 1.6x, Brazil/Germany 1.4x & 7%, Japan 4%) come from
  the interactive's internal data and the report's Figure 1 and are NOT reproducible from
  Google's public dataset (summing the public U.S. computer/math broad groups gives
  ~20.06%; the gap is the "All Other" detailed groups the public breakdown drops). The
  implied global baselines behind "double"/"1.6x" are back-calculations, not published.
  So attribute these to the report/interactive as published figures; do not present them
  as independently recomputed, and where you use the public-dataset number say it is the
  public-dataset number. This gap is itself fair game for the analysis.
- The science survey: 637 US/UK scientists, More in Common panel, 27 Jul-11 Aug 2026,
  UNWEIGHTED and explicitly not representative; 46.6% daily (n=297); net ~6.9 hrs/week
  SAVED, self-reported. Keep "~6.9 hrs saved" distinct from "~7 hrs spent on data
  analysis" — do not conflate. The authors say selection bias likely over-estimates both
  adoption and savings; carry that.
- To weigh the self-report-to-economic-gain inference fairly, the evidence records METR's
  2025 RCT (developers 19% slower with AI while believing they were 20% faster) and Humlum
  & Vestergaard 2025 (chatbot adoption, ~3% reported time savings, precise-null effects on
  hours/earnings). Neither studies scientists; use them to bound the inference, not to
  claim they refute the ATLAS. METR's Feb-2026 follow-up reportedly differed (flagged) —
  represent it fairly if you use it.

Required original work: do with these numbers something the ATLAS does not. The strongest
line the evidence supports: carry the volume-share-vs-task-help distinction through one or
two specific figures to a checkable statement about what the 30% (and the ~6.9 hours) does
and does not establish about AI at work. Put that one-sentence original-work claim in
draft-handoff.md. Be fair: state what the ATLAS set out to measure, in its authors' terms,
before testing the reading built on it; it is a serious effort, not a target.

Recent-habit notes to break (this desk; the editor compares):
- Dek molds to avoid: the dependency-clause tail ("whose durability depends on X and Y",
  "while the legal clock depends on"), the semicolon reversal ("Optical images show X;
  radar finds no Y"), and the comma-triad close ("A, B, and C"). Write a dek that is a
  stance, with the one detail that makes the piece unmistakable.
- Do not reprise the recent "AI incident reports need an audit trail" feature's
  measurement-governance frame or its structure. This piece does arithmetic on a dataset;
  it is not an argument for better reporting infrastructure.
- Name the flex sections for this argument; outline the reasoning before naming them;
  land on the conclusion the piece built, not a generic moral.

A table pairing a few headline figures with their denominators/targets likely earns its
place; use it only if it reads faster than prose. Number sources in first-citation order,
carry each `data-nb-kind`, prefer locators. Fill the nb-meta dates/harness/model. Proof
with `--no-check-links` while iterating, then `nb stamp` and the exact `nb check` above
until BLOCK: 0.
