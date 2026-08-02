# Editorial review: paper-of-the-day/generative-adversarial-networks (editor/01)

## Skeptic
Skeptic: thesis "the 2014 GAN paper proved a clean equilibrium in the space of
arbitrary functions, named its own failure mode (mode collapse, 'the Helvetica
scenario') without fixing it, and the decade after measured how far training
practice sat from the proof's assumptions"; tested 4 load-bearing claims (the
proof/equations; the paper's own 2014 naming of mode collapse; the
assumptions-broke chain via Arjovsky & Bottou Theorem 2.4; the WGAN/Lucic/
diffusion after-record); broke: **one factual claim.** The Lucic paragraph said
NS-GAN "wins MNIST and CelebA outright." FID is lower-is-better (the article's
own caption says so), and in the article's own Table 2 NS-GAN's CelebA FID is
55.0 — the worst of the three rows; WGAN-GP wins CelebA at 30.0. NS-GAN wins
only MNIST (6.8 outright). Fixed directly by cutting the false "and CelebA"
(the true CIFAR-10 detail and the load-bearing "no row wins all four columns"
point are kept). Everything else survived the break attempt.

### Verified against the primaries (all correct)
- **Abstract anchor**: reproduced verbatim from `researcher/02/evidence.md`,
  character-for-character (single unbroken paragraph, "1/2" as plain text). No
  paraphrase.
- **Equations, each re-derived against researcher/01**: value function Eq. 1;
  D*_G = p_data/(p_data+p_g) (Prop. 1); Theorem 1 quote (global min iff
  p_g=p_data, value -log 4) verbatim; Eq. 6 C(G) = -log 4 + 2·JSD; the
  non-saturating swap (maximize log D(G(z))) with both quoted phrases exact; the
  vanishing-gradient bound ‖∇_θ E[log(1-D(g_θ(z)))]‖₂ < Mε/(1-ε); the
  Earth-Mover distance. Every symbol is built before the line that spends it
  (question → symbol → formula → consequence), and the annotated Eq. 6 legend
  ("floor", "constant from two KL terms", "the real gap") is a fair gloss.
- **Theory-practice gap, per the exact angle**: the paper's OWN Section 6 names
  "the Helvetica scenario" in 2014 (quoted verbatim; framed as "foreseen,
  named, no fix," not "failed to foresee"); Arjovsky & Bottou Theorem 2.2/2.4
  (disjoint-support perfect-but-zero-gradient discriminator, then the bound);
  WGAN's "in no experiment did we see evidence of mode collapse" scoped
  explicitly as an experiments-claim, not a theorem; Lucic kept distinct from
  WGAN ("different questions, neither rebuts the other"); diffusion as
  proportionate context with "arXiv preprint" and no conference asserted.
- **Numbers/names**: -log 4; all Lucic Table 2 FIDs; all Dhariwal & Nichol
  Table 5 FIDs (ADM-G vs BigGAN-deep, all three resolutions) plus the 3.94/3.85
  guided+upsampled figures kept distinct; 25 sampling passes; all eight authors
  in correct order; Université de Montréal.
- **data-nb-kind**: all correct. Sources renumbered in first-citation order
  (GAN 1; tutorial 2; Weng 3; Salimans 4; Arjovsky-Bottou 5; WGAN 6; Lucic 7;
  diffusion 8). All papers `primary`; Lilian Weng's explainer `secondary`.
- **Furniture / render**: three equation blocks, two inline math spans, two
  tables, the Helvetica `nb-note`, and the Verdict `nb-note-strong`. LaTeX
  hand-checked (balanced braces, valid commands, `\htmlClass{nb-mc1..3}`
  matching the engine's documented `trust` syntax) — no real syntax error, so
  the sandbox KaTeX-CDN limitation is not flagged per the brief. No markup fix
  needed.

## Cut
Cut: 4 edits (2 full sentences/clauses removed, 1 signpost phrase, 1 false
label); worst tell: the "this record" self-reference paired with "two sections
back" signposting. Edits made directly:
1. Deleted "That gap is the seam the rest of this record runs along." — a
   self-referential signpost carrying no new fact; the section now ends on the
   sharp antithesis "The proof is about functions; the code that runs it
   optimizes parameters."
2. "NS-GAN is the non-saturating fix this record built two sections back, not a
   later variant." → "NS-GAN is the non-saturating fix, not a later variant."
   (removed self-reference + signpost; the concept name is already established).
3. "On the failure named two sections back, the paper reports one direct
   result:" → "On mode collapse, the paper reports one direct result:" (named
   the established concept in place of the signpost).
4. "The paper does not claim the second, and this record does not either." →
   "The paper does not claim the second." (removed self-reference).
Plus the skeptic-driven factual cut ("and CelebA") above. Headline, dek shape
aside, section headings, and punctuation otherwise hold the floor; earned
contrasts (Lucic vs WGAN "different questions"; "not the discovery of a failure
mode the 2014 paper missed") are real and within ceiling.

## Reader
Reader: this gives me the connective argument no single source performs — the
paper's own admitted crack (the non-saturating objective it swapped for the one
it just proved things about), its own named-but-unfixed failure (Helvetica),
the later theorem that explains *why* a near-optimal discriminator starves the
generator (Arjovsky & Bottou 2.4), the fair-budget null result (Lucic), and
diffusion's displacement, held apart as answers to different questions rather
than flattened into one rebuttal, and closed on a verdict that keeps the proven
result, the unproven assumptions, and the field's actual fixes distinct. Matches
the draft-handoff's original-work sentence. After the cuts, the prose reads
closer to the Goh/Olah/Weng exemplars (motivate-name-formula-consequence pacing,
one name per concept, plain theory/practice boundary) than to a median AI
summary. Headline as largest claim holds against Section 6.

## Required work by owner
**Writer** (one revision, prose + proof):
- **Dek shape.** The dek — "The 2014 paper proved a clean equilibrium in the
  space of functions, and the decade after measured exactly how far training
  practice sat from that space" — reproduces the voice guide's explicit
  do-not-reuse formula "proved X for a setting practice never occupied," the
  same proof-then-scope shape recurring across the recent library (muon,
  selective-state-spaces, alphafold). Recast to a fresh shape; keep it an
  accurate stance (not the banned "N follow-ups disagree"), and do not restate
  the headline. This is new prose, so it returns to the writer.
- **Re-proof.** My cuts changed the word count, so `nb-meta` `words: 2522` is now
  stale. Re-run to BLOCK: 0 and update the measured count (and reading_minutes
  if it shifts):
  `nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`

No researcher work: the evidence records are complete and correct; the one
factual break was a writer misreading of a table already right in the evidence,
fixed here by cut.

Re-proof needed: yes (word count changed by the cuts above).

## Final decision
REQUEST writer — recast the dek off the do-not-reuse "proved X / practice never
occupied" formula and re-run the proof to refresh the now-stale word count. All
substantive claims, equations, numbers, sourcing, and the abstract anchor
verified correct; the one factual error (NS-GAN "wins CelebA") is fixed in place.
