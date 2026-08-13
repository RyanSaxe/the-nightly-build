# editor review-brief: paper-of-the-day/vision-transformer (editor/01)

Inputs:
- editorial-direction.md, commission.md, and the writer's brief
  (writer/01/brief.md) — at / under the artifact root
- writing-coach/01/voice-guide.md — the register and quoted exemplars
- researcher/01/evidence.md — the evidence record (Numbers + Source assets)
- writer/01/draft-handoff.md — the draft handoff (original-work sentence)
- the article: library/paper-of-the-day/vision-transformer.html
- template context under .nb-context/

Recent-pattern notes (formula check):
- Recent paper pieces (mixture-of-experts, PPO) open on a problem-motivation
  section and close on a "what the field kept / what survives" holdsup section
  plus a verdict note. Confirm this piece's opener and closer are not those molds.
- Heavy nb-math is expected here; check headings are the piece's own nouns, and
  deks/headings are not stamped from the recent record.

This round's focus:
1. Source floor. The proof leaves W-SOURCES-MIN (4 sources vs the series floor of
   8); it is non-blocking because the series is not strict, so this is a quality
   judgment, not an automatic failure. Decide it on the argument: read whether any
   load-bearing claim rests on a source the piece cites as fact without its own
   entry (e.g. the BiT/ResNet baselines the crossover is measured against, the
   JFT-300M / ImageNet-21k datasets, the Transformer encoder the model reuses, or
   the Swin baseline ConvNeXt modernizes against). If such claims are load-bearing
   and uncited, route to the researcher to open those specific primaries and to
   the writer to cite them where the argument uses them. If the four opened papers
   honestly carry every claim the argument rests on and more would be padding,
   approve and record that the warning is accepted rather than padded — do not
   have the writer add citations to sources nobody opened.
2. Inspect both source assets (Figure 3 crossover, Figure 5 compute-vs-accuracy):
   honest crops from the ViT PDF, captions factual and cited, and the argument
   spends what each shows.
3. Audit every data-nb-kind (all marked primary) against the primary/secondary
   test; open every href.
4. Check the reconstruction math (the annotated equation) and the figures against
   the evidence record and the cited primary.
5. Confirm the honest bound is stated: no after-record source retrains a
   ViT-H/14-scale model on ImageNet-1k alone, so the largest-scale half of the
   crossover is confirmed by the original paper but not independently re-tested.

Proof after your edits is the orchestrator's to run (nb stamp + nb check). Route
evidence to the researcher, reporting/redraft/assets to the writer.
