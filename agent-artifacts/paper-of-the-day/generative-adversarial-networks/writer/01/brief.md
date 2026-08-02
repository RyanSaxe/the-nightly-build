# Writer brief: paper-of-the-day/generative-adversarial-networks (01)

## Your job
Draft the `paper` article on Goodfellow et al., "Generative Adversarial Nets"
(2014) — 1800-3400 words — rebuilding its central claim and weighing it against
what practice did, then prove it to `BLOCK: 0`. Draft only from the evidence
record and voice guide.

## Begin with these exact inputs
- This brief; `../../commission.md`; `../../editorial-direction.md`.
- Voice guide: `../../writing-coach/01/voice-guide.md` (reread before drafting).
- Evidence record: `../../researcher/01/evidence.md` (your complete claim set;
  every equation, number, and quotation you use must trace to it).
- Abstract supplement: `../../researcher/02/evidence.md` — the paper's abstract
  recorded **verbatim** for the required abstract anchor (01 remains valid). Quote
  the abstract from here exactly; do not paraphrase or reconstruct it.
- Initialized article:
  `/home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html`
  (edit this file; do not recreate the skeleton).
- Template context: `../../../../.nb-context/` (template-contract.yaml, runtime-
  assets.yaml, furniture/*). Search the furniture catalogs before drafting.

## The argument to build (all verified in the evidence record)
1. **The abstract anchor**: the paper's own words + link up front (template
   requirement). Then rebuild, in the piece's own words:
2. **The game**: value function (Eq. 1); the two players; Algorithm 1 (k=1 in the
   paper's own runs).
3. **The proof**: Proposition 1 (optimal discriminator D*_G = p_data/(p_data+p_g))
   and Theorem 1 (global optimum iff p_g=p_data, value -log 4, C(G) = -log 4 +
   2·JSD(p_data‖p_g)). Build each symbol before the line that needs it. This is a
   proof *in the space of the functions* — flag that assumption; it matters later.
4. **The first crack the paper itself admits**: the non-saturating trick — Eq. 1
   gives G "insufficient gradient" early, so train G to maximize log D(G(z))
   instead. The paper changed the objective it just proved things about, for a
   practical reason.
5. **The failure the paper named and did not fix**: Section 6 names mode collapse
   as "the Helvetica scenario" in 2014. The angle is precise: not "the paper
   failed to foresee it" but "it foresaw it, named it, and offered no fix beyond
   synchronizing D and G." (Confirmed later by Goodfellow's own 2016 tutorial and
   Salimans et al. 2016 on why the discriminator gives no anti-collapse signal.)
6. **Why the proof's assumptions failed in practice**: Arjovsky & Bottou (2017)
   Theorem 2.4 — when supports are disjoint (low-dim manifolds), a perfect
   discriminator exists with (almost everywhere) zero gradient; the JS objective
   gives no usable signal near optimality (the vanishing-gradient bound). WGAN
   (2017) replaces the objective with the Earth-Mover/Wasserstein-1 distance and
   reports no mode collapse *in its experiments* (scope it honestly — an absence-
   of-evidence claim, not a theorem).
7. **What a fair-budget study found**: Lucic et al. (2017) — no tested variant
   "consistently outperforms the non-saturating GAN" on FID once compute and
   tuning are equalized; no model dominates all four datasets (use Table 2). Keep
   distinct from WGAN's contribution: WGAN changed *what is optimized and how
   reliably it is monitored*; Lucic measured *final sample quality*. They answer
   different questions (see Contradictions #2) — do not flatten one into a
   rebuttal of the other.
8. **What happened next (context, proportionate)**: diffusion displaced GANs on
   image FID (Dhariwal & Nichol 2021, Table 5: ADM-G vs BigGAN-deep). Do not
   overstate the venue (arXiv preprint; no conference asserted).
9. **The reviewer's verdict**: what the paper established (an elegant equilibrium
   result and a working method), what it only assumed (an optimal discriminator,
   a game played in function space, not parameter space), and what the field had
   to add. Commit; do not overclaim.

## Furniture (plan with the prose; use only documented components)
- An **equation** block is well-justified for the value function, D*, and the
  Theorem-1 result (the site ships KaTeX for the equation furniture). Build the
  algebra in prose around it; do not drop a wall of symbols.
- A small **table** is well-justified for Lucic et al. Table 2 (the point is the
  *absence* of a dominant row — keep all four dataset columns together). The
  diffusion FID comparison could be a compact table too, if it earns its place.
- **Source asset (optional)**: Figure 1's four-panel schematic is the clearest
  picture of the equilibrium; use `nb asset` from the cited arXiv/ar5iv source
  only if the prose spends what it shows (retain all four panels a-d in order and
  the D/p_data/p_g labels). Lean toward the equation+table doing the work; add
  the figure only if it earns its place. If you build any chart, `nb chart` from
  the evidence record's verified series only, with committed provenance.

## Universal rules
Number sources in first-citation order; carry evidence-record kinds into
`data-nb-kind` (the GAN/WGAN/Arjovsky-Bottou/Lucic/Salimans/tutorial/diffusion
papers are **primary** for their own claims; Lilian Weng's explainer is
**secondary**). Add `data-nb-locator`/`data-nb-url` only where the evidence
supplies it. Keep fixed engine assets, classes, labels, the abstract anchor, and
`Sources` exactly. No article-authored scripts/styles/iframes/forms/external
images. Fill `nb-meta` with real values: series paper-of-the-day, slug
generative-adversarial-networks, template paper, mode open, order null, date
2026-08-02, tags ["research"], measured sources/words, a real dek (a stance, not
"N follow-ups disagree"), harness "claude-code", model "claude-sonnet-5".

## Prove and hand off
Run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`
Treat warnings as revision notes. Use `nb preview` if layout/asset/chart changed
and inspect the render (equations and any figure).

Write `draft-handoff.md` here with the one-sentence original-work statement,
paths changed, proof result and warnings left, and any remaining evidence/voice
questions. Return `DONE writer <draft-handoff-path>` after `BLOCK: 0`, or a
REQUEST/BLOCKED line. Keep content in files.
