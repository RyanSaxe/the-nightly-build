# researcher brief: paper-of-the-day/adversarial-examples (01)

Inputs:
- `agent-artifacts/paper-of-the-day/adversarial-examples/commission.md` — the paper, the reconstruction targets, the public record to weigh, and the source floor
- `agent-artifacts/paper-of-the-day/adversarial-examples/editorial-direction.md` — citation standard, series territory, declared reader

Output: `agent-artifacts/paper-of-the-day/adversarial-examples/researcher/01/evidence.md`

Read the paper (arXiv:1412.6572) in full, then the record around it. Deliver:
- The exact statements the reconstruction needs: the linear explanation of why a
  max-norm-bounded perturbation moves an activation by an amount that grows with
  input dimension, with the paper's own expression and locator; the fast
  gradient sign method equation; the numbers in Figure 1 (the perturbation size,
  the two labels, the confidence) and the adversarial-training objective. Set
  these down precisely enough for the writer to reproduce the math.
- The Figure 1 panel (panda to gibbon) as a candidate source asset: name exactly
  where it lives in the paper and what a crop must retain (the clean image, the
  perturbation, the adversarial image, and their labels and confidences).
- The public record that weighs the linear claim: Szegedy et al. 2013's original
  framing; Madry et al. 2018 (PGD adversarial training); Athalye et al. 2018
  (obfuscated gradients) and Carlini and Wagner 2017 (breaking defenses); Ilyas
  et al. 2019 (non-robust features); Tsipras et al. 2019 (robustness-accuracy
  tension); and one current benchmark or survey of where robustness stands.
  For each, record what it establishes firsthand and the figure or result that
  matters, with locator.
- Contradictions: where later work disagrees with the linear explanation, and
  where it confirms parts of it (cheapness, transferability). Record both in
  full so the editor can test the verdict.

Classify every source primary or secondary (a paper is primary for its own
claims, secondary when it characterizes another's). Confirm every arXiv URL
resolves to the paper's abstract page. Verify every number against the paper
that owns it.
