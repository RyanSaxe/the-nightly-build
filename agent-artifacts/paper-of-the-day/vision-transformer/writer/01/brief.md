# writer brief: paper-of-the-day/vision-transformer (01)

Inputs:
- editorial-direction.md (house standard, slop, headlines, press voice, paper
  template identity, series prompt) — at the artifact root
- commission.md (the claim to rebuild, the after-record to weigh it against, the
  boundaries) — at the artifact root
- writing-coach/01/voice-guide.md (how this piece should sound)
- researcher/01/evidence.md (the complete set of claims available; use its
  Numbers section exactly; figures named in Source assets)
- the initialized article: library/paper-of-the-day/vision-transformer.html
- template context under .nb-context/ (effective contract, furniture catalogs)

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/paper-of-the-day/vision-transformer/library/paper-of-the-day/vision-transformer.html --series paper-of-the-day --library /home/user/library-checkout

Recent shapes to break (from the commission): recent paper pieces open on a
problem-motivation section and close on a "what the field kept / what survives"
holdsup section plus a verdict note. Use math and figures where the claim turns
on them, but do not build the opener or closer on those molds, and outline the
reasoning before naming sections. The evidence record flags one bound to honor:
no after-record source retrains a ViT-H/14-scale model on ImageNet-1k alone, so
the largest-scale half of the crossover is confirmed by the original paper but
not independently re-tested. Bring in the figures the evidence record names as
source assets via nb asset, only where the argument spends what they show.
