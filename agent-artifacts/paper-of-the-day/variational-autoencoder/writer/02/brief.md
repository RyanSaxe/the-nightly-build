# writer brief: paper-of-the-day/variational-autoencoder (02)

Apply the sources item from editor/01/editorial-review.md using the new evidence
(inputs and standard unchanged from writer/01/brief.md; the editor's direct edits
are already in the article and must be preserved).

New sources to cite at existing claim sites:
- researcher/02/evidence.md: Ho, Jain, Abbeel 2020 (DDPM, arXiv:2006.11239) —
  owns the ELBO-to-diffusion forward link the commission named but the draft
  omitted; fold this link into the verdict where the piece gestures at diffusion.
  Paisley, Blei and Jordan 2012 (arXiv:1206.6430) — owns the high-variance
  score-function estimator claim the piece leans on by name; attach it there.
- researcher/03/evidence.md: Doersch 2016 (arXiv:1606.05908) — owns the general
  reparameterization-validity conditions (fixed noise, continuity, no discrete
  latents) behind the gradient-problem section's "no differentiable path through
  the random draw"; cite it at that claim.

Keep beta-VAE (source 5) as the corroborated secondary it is; its primary is
access-blocked, so do not present it as read. Add no new claims or sections beyond
folding in the diffusion forward link the commission asked for.

Number ALL sources in strict first-citation order (renumber as needed), so the
proof does not warn W-CITE-ORDER. Update the nb-meta sources count (from 5 to 8).
The three W-SENTENCE-DENSITY warnings on the equations and the verbatim Bowman
quote are acceptable to leave (the editor concurred). Rerun the full proof (links
included) with `nb stamp` before the final check, until BLOCK: 0 and no
W-CITE-ORDER or W-SOURCES-MIN. Output: writer/02/draft-handoff.md.

Proof: ./nb check --series paper-of-the-day .nb-work/paper-of-the-day/variational-autoencoder/library/paper-of-the-day/variational-autoencoder.html --library /home/user/library-checkout
