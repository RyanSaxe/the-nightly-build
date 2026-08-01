# Editorial review — paper-of-the-day/grokking (editor, 01)

Three ordered reads at high effort. Sources reopened as an opponent; every
load-bearing figure recomputed; each `data-nb-kind` audited. Final decision at
the end.

## Skeptic

Skeptic: thesis "the 2022 paper documented delayed generalization but supplied
no cause, and the after-record verified a mechanism on only a narrow slice of
the original task while splitting three ways on why weight decay drives the
jump, none confirming the paper's own flat-minima guess"; tested 7 claims;
broke: 1 (a furniture note that internally contradicts the article — cut).

Claims tested and what I did to each:

1. **Abstract is verbatim (critical check).** Reopened the arXiv abstract via
   the HTML page (`arxiv.org/abs/2201.02177`) and independently via the arXiv
   export API (`export.arxiv.org/api/query?id_list=2201.02177`). Both render the
   word with **straight double quotes**: `"grokking"`. The draft (and the
   evidence transcription) used single quotes `'grokking'`. Every other
   character of the abstract matches. **Fixed directly** — the single quotes are
   now double quotes; the abstract is now verbatim.

2. **Venue is not overstated (critical check).** Confirmed the piece does not
   assert a specific workshop/year for the focal paper. The paper card carries
   `arXiv:2201.02177 · 2022` (arXiv posting year, not a claimed venue). The body
   says only "posted to arXiv in January 2022 as a workshop submission" and then
   states the MATH-AI/ICLR-2021 record is "dated a year before that posting, a
   mismatch that stays unresolved." Independently, the arXiv page carries no
   journal-ref and no venue metadata (only a Comments field with correspondence
   and a code link). The venue is genuinely unresolved; the safe phrasing is
   correct and **stands unchanged**. Open item resolved editorially: do not name
   a venue.

3. **Nanda's neuron concentration.** Reopened `arxiv.org/html/2301.05217` §4.3.
   "433 of 512 (84.6%)" with >85% of variance from a single frequency:
   confirmed, and the paper does partition those neurons by the five key
   frequencies, so the draft's "a single one of those five frequencies" is
   supported. No change.

4. **Nanda's ablation losses.** §4.4: removing all non-key frequencies cuts loss
   ~70% to 7.24×10⁻⁸; keeping only the ten key directions cuts it ~50% to
   1.19×10⁻⁷; the direction is a *reduction* (the discarded components were
   noise). All confirmed against the source. Key frequencies k∈{14,35,41,42,52}
   confirmed. No change.

5. **Power's measured quantities.** Checked against the evidence record's
   verbatim readings: <10³ steps to near-perfect train accuracy; ~10⁶ to
   validation; "very little evidence" until 10⁵; +40–50% median steps per 1% of
   data removed near the viable minimum; steps-to-fit stay in the 10³–10⁴ band;
   weight decay "more than halving" the samples needed; decay toward
   initialization less effective than toward the origin. All match. Worked
   example 87 + 61 ≡ 35 (mod 113) recomputed and correct.

6. **The four causal accounts are fair and none is called settled.** Verified
   each against the evidence: Nanda (Fourier/rotation — answers *what the network
   computes*), Omnigrok/Liu (weight-norm Goldilocks band, t ∝ γ⁻¹), Varma
   (circuit efficiency, ungrokking/semi-grokking), Prieto (Softmax Collapse /
   numerical). The piece keeps Nanda's "what" distinct from the three-way "why
   weight decay" dispute, states "Why it does that is not settled," and says the
   record "has not converged." No account is overclaimed as settled. No change.

7. **The scope-gap synthesis (the article's spine).** The claim that the
   mechanistic record covers one operation of twelve, one modulus, one
   architecture — while eleven-twelfths of Power's claim is untested by any
   explanation — is carried correctly in the "What to be careful about" box and
   the verdict, both scoped to the rotation account. Holds.

**Broke (required change, fixed by cutting):** the "Same name, narrower task"
note asserted "Every explanation for grokking published after Power's paper was
tested on addition only, at p = 113, on a one-layer network." This is false and
self-contradicting: Omnigrok (one of the three weight-decay accounts) is
explicitly credited *later in the same article* with reproducing grokking on
image classification, sentiment analysis, and molecule-property prediction — not
addition only. Prieto used an MLP, not a one-layer network; Varma's setup is
unverified in the evidence (abstract-level only). The note used a Nanda cite
(s3 §3) to support a blanket claim about *all* follow-ons. The correctly-scoped
version of this point already appears in the "What to be careful about" box and
the verdict, so I cut the note rather than return it.

**`data-nb-kind` audit.** s1 Power (primary, owns its claims) ✓; s2 MATH-AI page
(primary for the one fact it is cited for — that this workshop page lists the
paper) ✓; s3 Nanda (primary, cited for its own claims) ✓; s5 Liu effective
theory, s6 Omnigrok, s7 Varma, s8 Prieto (each primary for its own claims) ✓.
s4 Barak "Hidden Progress" is labeled **secondary**: it is cited only for its own
sparse-parity finding, which would make "primary" defensible, but the researcher
labeled it secondary/contextual because it owns no grokking claim and only
supplies the progress-measures lineage. The label hides no missing independent
source (it is the more modest choice), so I left it; noting it here for the
record. All eight sources are cited in the body; the openai/grok repo from the
evidence was dropped by the writer as non-load-bearing, correctly.

## Cut

Cut: 3 sentences/blocks (~96 words); worst tell: an early furniture note whose
blanket "every explanation... addition only... one-layer network" contradicted
the article's own later Omnigrok paragraph.

Direct cuts made:

- **Orientation trailing sentence** — "What later researchers found the network
  was actually doing, and how far that finding reaches, took another three years
  and a different research group entirely." A forward signpost ("what follows"),
  and its "three years" collided with the next section's own "A year after
  Power's paper." Cut; the section now lands on the paper's untested-hypothesis
  admission, a harder ending.
- **"Same name, narrower task" note** — cut for the factual/self-contradiction
  reason above.
- **Measurement-section restatement** — "That guess is the only candidate
  explanation the paper offers... and it goes untested inside the paper itself."
  Third restatement of a point already made in the orientation and in the
  blockquote note directly above it; carried no new fact. Cut; the transition
  sentence remains.

Also updated `nb-meta` `words` from 2592 to 2496 to keep the declared count
honest after the cuts (reading_minutes unchanged at 12).

Nothing else met the delete test. Em-dash usage is within the house limit
(the check reports zero banned-term warnings), and I introduced none. No prompt
leakage: the prose never narrates its own contribution or claims to have
fulfilled the brief; the "Verdict" block is required paper-template furniture.
The dek makes a claim about the world (the three-way disagreement), not a grade
of the article's method, and avoids the banned dek molds.

## Reader

Reader: this gives me a clean separation of a measured phenomenon from four
disagreeing accounts of its cause, plus the reviewer's-eye scope audit — that
the after-record verifies a mechanism on one of Power's twelve operations, at a
different modulus, on a smaller network, while the deeper "why weight decay"
question stays open three ways — which no single one of the eight sources states.

This matches the writer's original-work claim in `draft-handoff.md` (the
phenomenon-vs-cause split and the eleven-twelfths-untested scope gap). The prose
sits closer to the voice-guide exemplars (Recht's scoped verdict, Olah/Weng's
teach-by-rebuilding: worked p=113 example, the angle-addition identity taught by
use) than to a median AI summary. Headline retested as the largest claim:
"OpenAI's grokking paper never explained grokking" is defended by the body (the
paper offered only an untested flat-minima guess) and is accurate shorthand
(four of five authors at OpenAI, correspondence to openai.com). No colon
subtitle. Both writer open items resolved: venue phrasing stays non-committal
(confirmed unresolved at source); the two abstract-only sources (s5, s7) are
cited only at abstract-level locators, within their verified scope.

## Required work by owner

None outstanding. The one broken claim was removed by cut; the verbatim defect
was fixed directly.

## Proof

`nb check library/paper-of-the-day/grokking.html --series paper-of-the-day
--repo /home/user/the-nightly-build` → **BLOCK: 0, WARN: 0, PUBLISHABLE**,
re-run after every edit including the final `nb-meta` change.

## Decision

Approve. No redraft required.
