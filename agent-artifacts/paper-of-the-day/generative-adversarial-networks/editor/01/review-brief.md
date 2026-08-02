# Editor review-brief: paper-of-the-day/generative-adversarial-networks (01)

## Your job
Give this drafted `paper` article the three ordered reads (skeptic, cut, reader)
and either approve it (`DONE editor`, no required change) or route numbered
repairs. Cuts/small fixes go directly; new prose past a word/clause returns to
the writer; evidence gaps to the researcher; equation/table/markup fixes return
to the writer.

## Begin with these exact inputs
- This brief; `../../editorial-direction.md`; the exact writer brief
  `../../writer/01/brief.md` (prompt-leakage detection); voice guide
  `../../writing-coach/01/voice-guide.md` (read first); evidence records
  `../../researcher/01/evidence.md` AND `../../researcher/02/evidence.md` (the
  verbatim abstract); draft handoff `../../writer/01/draft-handoff.md`;
  article `/home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html`;
  template context `../../../../.nb-context/`.

## What to check hardest (this article's risk surface)
- **The abstract anchor** must reproduce the paper's abstract **verbatim** exactly
  as recorded in `researcher/02/evidence.md` — check character fidelity, no
  paraphrase.
- **Every equation and theorem re-derived against the primary** (researcher/01):
  the value function V(D,G); Proposition 1 D*_G = p_data/(p_data+p_g); Theorem 1
  (global optimum iff p_g=p_data, value -log 4, C(G) = -log 4 + 2·JSD); the
  non-saturating fix (maximize log D(G(z))). Confirm the algebra is right and each
  symbol is built before the line that needs it.
- **The theory-practice-gap claims, precisely**: the paper's OWN Section 6 names
  mode collapse "the Helvetica scenario" (2014) — the angle is "foreseen, named,
  no fix," not "failed to foresee." Arjovsky & Bottou Theorem 2.4 (vanishing
  gradient when supports disjoint / D near-optimal). WGAN's Earth-Mover objective;
  its "no mode collapse" claim scoped as an experiments-claim, not a theorem.
  Lucic et al.: "no variant consistently outperforms the non-saturating GAN" under
  a fair budget — kept DISTINCT from WGAN's contribution (they answer different
  questions; do not flatten into a rebuttal). Dhariwal & Nichol diffusion FID as
  proportionate context; no conference venue asserted.
- **Numbers/names**: -log 4; the Lucic Table 2 FIDs; the diffusion FIDs; all
  eight authors/affiliations; every `data-nb-kind` (the papers primary for their
  own claims; Lilian Weng's explainer secondary).
- **Furniture**: equation block and the two tables must render honestly (the
  writer reports inspecting them and fixing a phone-width overflow — spot-check
  the render if you can; markup fixes return to the writer). The KaTeX CDN could
  not be visually confirmed in the sandbox (proxy limitation) — LaTeX was
  hand-verified against the engine's documented `\htmlClass` syntax; flag only if
  you find a real syntax error, not the sandbox limitation.

## Standards to apply in the cut
Full house prose/punctuation floor. Compare opener, dek, and headings against the
recent paper library (the one-line-paradox headline + "N follow-ups disagree"
dek; the "proved X for a setting practice never occupied" opener-as-formula).
Break any repeated shape. Cut prompt leakage and self-grading; the subject is the
paper, never the experience of reading about it.

## Output
Write `editorial-review.md` here with the three required lines, direct edits,
required work by owner, final decision. If you edit prose, note whether a re-proof
is needed
(`nb check .../generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`).
Return `DONE editor <path>` only if no redraft is required, else a
`REQUEST writer/researcher <one-sentence>` line.
