# editor review-brief: feature/ai-economy-atlas (editor/01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- voice-guide.md (../../writing-coach/01/voice-guide.md) — read first.
- evidence.md (../../researcher/01/evidence.md) — the claim set the draft must not exceed.
- commission.md (../../commission.md)
- the exact writer brief (../../writer/01/brief.md)
- draft-handoff.md (../../writer/01/draft-handoff.md) — the original-work sentence and three
  flagged open items.
Article under review (read the rendered page, and look at the rendered chart image):
  .nb-work/feature/ai-economy-atlas/library/feature/ai-economy-atlas.html
  (chart source + image: .../library/feature/ai-economy-atlas/chart-1.py + chart-1.png)
Output: ../../editor/01/editorial-review.md
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/ai-economy-atlas/library/feature/ai-economy-atlas.html --series feature --repo /home/user/the-nightly-build

Decide whether this publishes and edit it until it can. Effort: HIGH. Change anything except
the facts; narrow a claim to what the evidence supports, but never invent a figure, alter a
number, or change what a citation is cited for. Where the record and a source you open
disagree, STOP and ask me (the orchestrator).

The spine of the piece is a measurement distinction; test it hard:
- Every ATLAS work "share" must read as a share of conversational-request VOLUME within a
  geography, in the authors' own terms (report Sec 2.3; AI-in-Science fn 14). Confirm the
  draft never lets a share stand as a share of jobs, hours, or task-help.
- Attribution of the headline numbers: the 30% and the per-country multipliers belong to the
  report's Figure 1 / the interactive as PUBLISHED figures; the 20.06% must be labelled the
  public-dataset recomputation; the ~15%/~11.9%/~5% baselines must read as back-calculations.
  Confirm the draft does not present the 30% as independently recomputed.
- "~6.9 hours saved" (self-reported, net) must stay distinct from "~7 hours spent on data
  analysis," and the survey's limits (n=637, unweighted, not representative, selection bias
  over-estimating) must be carried, not buried.
- METR 2025 and Humlum-Vestergaard 2025 are used to BOUND the self-report-to-economic-gain
  inference, not to refute the ATLAS; if METR's Feb-2026 follow-up is cited, it must be fair.
- Open the href of every citation as printed; audit data-nb-kind (the study's own blog is
  secondary to its own data).

Three inherited open items from the writer (you decide each; do not fabricate data):
1. Chart scope. The record has no major-group VOLUME-share series (public files withhold it),
   so a literal volume-vs-saturation chart is not possible from the evidence. The writer built
   a saturation comparison (any use vs intensive use) strictly from the verified series and
   carried the volume-vs-depth contrast in prose. Judge whether the chart earns its place and
   whether its caption is a factual, cited label with the interpretation in prose. If it does
   not earn its place, cut it; do not invent a volume series to "fix" it.
2. It charts 14 of the 22 major groups (only those the record verifies). Fine if the caption
   is honest about the subset; flag if you think the omission misleads.
3. Source 5 was switched to the embed-report-2026 served path (resolves 200) because the
   dataset .zip path 404s; confirm the printed href lands on the owning document and no claim
   changed.

Recent-habit comparison (Feature desk):
- Dek molds to cut: the dependency-clause tail ("whose durability depends on X and Y"), the
  semicolon reversal, the comma-triad close.
- Do not let the piece drift into the recent audit-trail feature's measurement-governance
  frame; this is arithmetic on a dataset.
- Check headings against spec/headlines.md (each a step of the argument in the piece's nouns),
  and the first/last sentence of every section and the article's last sentence for slop.

Last, answer in one sentence what the piece gives beyond its sources, and compare it to the
writer's original-work sentence in draft-handoff.md; if neither survives, it is a redraft.
If you make direct edits and approve, run `nb stamp` and the exact `nb check` above until
BLOCK: 0 yourself. Write editorial-review.md in the required shape and report the decision.
