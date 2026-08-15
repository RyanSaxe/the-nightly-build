# writer brief: paper-of-the-day/variational-autoencoder (01)

Inputs:
- editorial-direction.md — house/press/series standard, declared reader
- commission.md — the focal paper, the reconstruction, the after-record, and the
  "Habits to break"
- writing-coach/01/voice-guide.md — how this reconstruction should sound
- researcher/01/evidence.md — the confirmed equations with locators, the
  verbatim abstract, the figure inventory, and the recorded gaps
- the initialized article at
  .nb-work/paper-of-the-day/variational-autoencoder/library/paper-of-the-day/variational-autoencoder.html
  and its contract under
  .nb-work/paper-of-the-day/variational-autoencoder/.nb-context/

Output: writer/01/draft-handoff.md

Proof: ./nb check --series paper-of-the-day .nb-work/paper-of-the-day/variational-autoencoder/library/paper-of-the-day/variational-autoencoder.html --library /home/user/library-checkout

This round's focus: rebuild the argument and set the math. The `abstract` section
carries the paper card and the verbatim abstract from the evidence record. Set
the ELBO as the single annotated `nb-math` equation and the reparameterized
estimator in `nb-math`, with honest locators to the paper's own equation numbers.
Honor the evidence's corrections exactly: there is no reparameterization
schematic figure in the paper, so if you use a source asset, use Figure 1 (the
graphical model) or Figure 4 (the 2D learned manifold, Appendix A), captured from
the paper with a factual cited caption and only where the argument spends what it
shows. Use beta-VAE only for the general disentanglement point, without an
equation-level citation, since the researcher could not open the primary; lean on
Bowman et al. 2016 (posterior collapse, which directly complicates the paper's
own Figure 2 caption) and Burda et al. 2016 (IWAE) for the after-record. A
minimal reparameterized sampler in `nb-code` is optional; the equation and figure
are the priority. State the reviewer's verdict in prose before Sources, not in a
boxed `nb-note-strong` callout, and do not copy the vision-transformer piece's
numeric-finding heading formula wholesale.
