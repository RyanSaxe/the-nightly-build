# editor review-brief: paper-of-the-day/adversarial-examples (01)

Inputs (paths relative to the workspace root `.nb-work/paper-of-the-day/adversarial-examples/`):
- `agent-artifacts/paper-of-the-day/adversarial-examples/editorial-direction.md`
- `agent-artifacts/paper-of-the-day/adversarial-examples/commission.md`
- `agent-artifacts/paper-of-the-day/adversarial-examples/writer/01/brief.md` — the exact writer brief (check the draft against it for leakage)
- `agent-artifacts/paper-of-the-day/adversarial-examples/writing-coach/01/voice-guide.md`
- `agent-artifacts/paper-of-the-day/adversarial-examples/researcher/01/evidence.md`
- `agent-artifacts/paper-of-the-day/adversarial-examples/writer/01/draft-handoff.md`
- `library/paper-of-the-day/adversarial-examples.html` — the drafted paper article (proof passes at BLOCK: 0, links included), with `asset-1.png` beside it
- `.nb-context/` — effective template contract and furniture catalogs

Output: `agent-artifacts/paper-of-the-day/adversarial-examples/editor/01/editorial-review.md`

## Recent-pattern notes (paper desk, to catch formula)
- The desk's recurring headline/dek mold is "the paper's own proof or measurement leaves out its claim" (batch-norm, GAN, word2vec). Confirm this headline/dek is not that mold.
- The recent GAN piece was built as "theorem versus Algorithm 1"; confirm this piece does not mirror that structure.
- Recent papers close on a stamped "what the paper is right about" heading (nb-holdsup / nb-note-strong). Confirm the closer here is the piece's own weighing.

## This round's focus
- Math correctness is load-bearing. Verify the perturbation is set as `eta = epsilon * sign(w)` (or sign of the input gradient) with the growth term `epsilon * m * n`, and that the annotated equation names epsilon, m, n. The bare `sign(w)` without epsilon would be wrong; confirm it does not appear as the operative form.
- Source asset: inspect `asset-1.png` as a reader. It must retain all three Figure 1 panels, the operators, and the confidences (panda 57.7% -> "gibbon" 99.3%, epsilon=0.007), with a factual cited caption and no unrelated clutter.
- The reframing must be grounded in the paper's own numbers: adversarial error cut to 17.9% but still 81.4% confident when wrong. Verify these against the evidence record. Confirm the linear view's real wins (cheap, gradient-aligned, transferable perturbations; FGSM + adversarial training as the field's start) are conceded before the piece weighs where it fell short.
- Szegedy 2013's prior view must be represented accurately ("low-probability pockets" / discontinuity, quoted in his words), with the "nonlinearity" framing named as partly Goodfellow's construction, not a strawman asserted as Szegedy's position.
- The closing stat strip anchors three CIFAR-10 robust-accuracy figures at eps=8/255 (undefended ~0%, Madry PGD 45.8%, Wang 70.69%). The attacks behind them differ (PGD vs AutoAttack), so this is a decade-scale anchor, not a like-for-like table. Confirm the prose says so and the figures match the evidence record and are presented as a dated checkpoint.
- Audit every `data-nb-kind`: a paper is primary for its own claims and secondary when it characterizes another's.

Open every citation href. Verify display text descriptor by descriptor. Inspect the source asset and the equation furniture as furniture carrying evidence. Edit prose/structure directly; leave the source asset and chart provenance to the writer, and route reporting, evidence, or a redraft. You are the required fresh-eyes editor at high effort; make all three reads.
