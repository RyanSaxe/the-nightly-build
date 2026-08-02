# Editorial review: paper-of-the-day/generative-adversarial-networks (editor/02)

Focused re-read of the round-02 dek recast and intactness. The round-01 body
findings stand: abstract verbatim, all equations/theorems, all numbers/names,
`data-nb-kind`, and the theory-practice framing were verified correct in
`editor/01/editorial-review.md` and are unchanged. One new break this round, in
the recast dek itself.

## Skeptic
Skeptic: thesis unchanged from round 01 (the paper proved a clean function-space
equilibrium, named its own failure mode without fixing it, and the decade after
measured how far practice sat from the proof's assumptions); re-tested the dek as
a claim; broke: **the dek misdates its own subject.** New dek: "A fair-budget
study a decade later found that none of the fixes proposed since consistently
outperforms the non-saturating loss the paper itself patched in when its proven
objective wouldn't train." The only fair-budget study in the piece is Lucic et
al., "Are GANs Created Equal?" (source 7, 2017) — three years after the 2014
paper, not a decade. The body is precise about timing elsewhere ("Seven years
after the paper" for diffusion, 2021), and the declared reader knows the Lucic
study's date, so "a decade later" is a wrong date in the single most visible line
the paper prints. Everything the dek asserts about content is true (Lucic's
fair-budget conclusion, the non-saturating loss the paper patched in); only the
interval is false. This is prose in display text carried in both `nb-meta` `dek`
and the `.nb-dekline`, so the fix — and keeping the two in sync — returns to the
writer.

### Dek shape (the round-01 required item): cleared
- Off the banned "proved X for a setting practice never occupied" mold: it opens
  on a finding, not a proof, and does not scope a proof against a setting.
- Not a close cousin: no semicolon reversal, no suspended question, no
  three-clause comma triad (`spec/headlines.md` molds all absent).
- Not an effect-size hook and not an "N follow-ups disagree" line: one specific
  sourced finding, no magnitude, no list of disagreeing parties.
- Not a restated headline: the headline is the paper naming mode collapse and
  not fixing it; the dek adds the later fact that the paper's own patch still
  hasn't been consistently beaten. Different fact.
- `nb-meta` `dek` and the rendered dekline are character-identical.

### Intactness confirmed
- All four round-01 direct cuts hold ("this record ... runs along" gone;
  "this record built two sections back" gone; "On mode collapse ..."; "The paper
  does not claim the second."; false "and CelebA" gone, NS-GAN "wins MNIST
  outright" stands).
- Abstract reproduced verbatim (first and last sentences confirmed against
  `researcher/02`).
- Value function, D*, and the annotated Eq. 6 / JSD block present and unchanged;
  both tables (Lucic Table 2 FIDs; Dhariwal & Nichol Table 5 ADM-G vs BigGAN-deep)
  present and unchanged.

## Cut
Cut: 1 this round; worst tell: a fourth "this record" self-reference I missed in
round 01. Deleted the sentence "The paper is careful about its own scope: it is
an arXiv preprint, and this record does not assert a conference beyond that." —
it narrated the article's own sourcing choice (self-reference the floor bans) and
carried no load-bearing fact; source 8 remains cited twice more in the same
paragraph, and the "no conference venue asserted" requirement is satisfied by the
piece simply not asserting one. The paragraph now opens cleanly on the diffusion
model's best configuration.

## Reader
Reader: unchanged from round 01 — the piece still gives me the connective
argument no single source performs (the paper's own admitted crack, its
named-but-unfixed failure, the later vanishing-gradient theorem, the fair-budget
null result, diffusion's displacement, held distinct through to the verdict). The
dek date error does not touch the body's synthesis.

## Required work by owner
**Writer** (dek prose + re-proof):
- Fix the dek's false interval. The fair-budget study (Lucic et al.) is 2017,
  three years after the 2014 paper, not "a decade later"; recast the temporal
  phrasing to be accurate (drop the interval, or say "three years later" / "years
  later"), keeping it off the banned mold and identical in `nb-meta` and the
  dekline.
- Re-proof. My round-02 cut above changed the prose again, so `nb-meta`
  `words: 2468` is now stale; re-run to BLOCK: 0 and refresh the count:
  `nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`

Re-proof needed: yes (dek fix plus my one cut both change the counted prose).

## Final decision
REQUEST writer — the dek recast clears the banned mold but misdates the
fair-budget study ("a decade later" for Lucic 2017); fix the interval, keep both
dek locations in sync, and re-proof to refresh the word count. All else verified
intact and correct.
