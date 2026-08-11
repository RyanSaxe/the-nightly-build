# Editorial review: paper-of-the-day/proximal-policy-optimization (editor/01)

## Skeptic

Thesis: PPO's clipped objective, the mechanism the paper advertises as its
trust-region enforcer, is not the part that carries PPO's measured advantage;
controlled reexaminations relocate most of that advantage to the surrounding
implementation and show the clip does not hold the ratio region it names, while
PPO's practical dominance stays undisputed. The article stands on four claims,
and I pushed hardest on the two the whole angle rests on.

Claim 1, the reconstruction is faithful to the paper. I checked every equation
against the evidence record's verbatim transcription and the owning papers. The
ratio (Eq. 6 context), L^CPI (Eq. 6), the clipped L^CLIP with the min() and
epsilon = 0.2 (Eq. 7), the TRPO constraint, the KL-penalty variant (Eq. 8), the
combined actor-critic loss with c1/c2 and L^VF = (V - V^targ)^2 (Eq. 9), and the
truncated GAE with delta_t = r_t + gamma V(s_{t+1}) - V(s_t) (Eq. 11-12) all
match the record symbol for symbol. The min()/lower-bound reasoning is stated
correctly and quoted exactly ("a pessimistic estimate (i.e., lower bound)"). The
worked example (r_t = 1.3, band [0.8, 1.2], min keeps 1.2*A_t, gradient zero
past the edge; r_t = 1.1 credited in full) is arithmetically right and is the
Karpathy-style smallest-case the voice guide asks for. Held.

Claim 2, the trust-region finding is about the ratio, not the KL. This is the
load-bearing correction, and it survives exactly. The article says the maximum
ratio runs past 1+epsilon so the clip fails to hold the ratio region, then that
mean KL stays under TRPO's 0.07 bound in the same run, and states outright that
"PPO leaves its trust region" is true of the ratio and false of the KL. The
flattened claim never appears as an assertion; it appears only in quotes, being
corrected. It closes with the record's exact framing: all three methods fail a
ratio region, TRPO holds a mean-KL one nearly by construction. Held.

Claim 3, code-level optimizations outweigh the step choice. Verified against
Engstrom Table 2: PPO/PPO-M/TRPO/TRPO+ and the AAI/ACLI rows all match the
record (Walker2d 3292/2735/2791/3050, AAI 242, ACLI 557; Hopper 2513/2142/2043/
2466, AAI 99, ACLI 421; Humanoid 806/674/586/1030, AAI 224, ACLI 444). The
prose reads the bottom two rows correctly and the 17%/21% Hopper figures match
Sec. 5. PPO-NoClip > PPO-Minimal on all three (2867/2371/831 vs 2735/2142/674)
and edges full PPO on Humanoid (831 vs 806), all matching Table 3. The
footnote-6 containment caveat is present and the article does not upgrade
"clipping unnecessary" past "a tuned no-clip run matches PPO here." Held.

Claim 4, PPO's dominance is undisputed and the paper's own ablation and
Andrychowicz are steelmanned before the reexamination. The article grants
dominance early ("That dominance is not in question here"), devotes a full
section to the paper's Table 1 result ("a genuine result for the clip"), and
gives Andrychowicz its due (PPO loss best on 4 of 5 and on the two hardest,
recommended at clip ~0.25, trust-region behavior shared across losses). The word
"debunked" does not appear; the verdict says the reexaminations "leave that
intact and relocate the credit." Held.

Table 1 (surrogate ablation): the seven displayed rows match the record
(-0.39, 0.76, 0.82, 0.70, 0.68, 0.74, 0.71). It is a representative subset of the
paper's eleven rows; the highest KL variant shown (0.74) is the true maximum KL
score, so the prose claim "the KL variants trail it" is honest against the full
table and nothing is cherry-picked to flatter the clip. No change required.

Display text, checked descriptor by descriptor: the paper card (title, five
authors, OpenAI, arXiv:1707.06347, 2017) is correct; the headline's "most of
PPO's edge" and the dek's "most of its reward margin over TRPO" both track
Engstrom's "most of PPO's gain in cumulative reward over TRPO." Every section
heading is a real step of the argument in the piece's own nouns.

data-nb-kind audit: the six arXiv primaries and two secondaries (Huang blog,
Henderson et al.) match the record's classification. Andrychowicz is cited as a
primary, which the record supports (primary for its own large-scale study).

Citations: I opened all eight printed source-list hrefs. Each resolves to the
source's own arXiv abstract page (or the ICLR Blog Track page for s3), and the
title and authors on each page match the source entry. The two figure cites'
data-nb-url values point at the arXiv PDFs; that is the template's documented
asset-provenance pattern (furniture/template.md), not the citation-URL rule, so
it is correct, and the reader-facing hrefs (#s1, #s6) resolve to the abs pages.

No break found. No claim routed.

## Cut

I ran the sentence-by-sentence slop pass, then the edges out of order, then the
cold-read and the delete test. The prose is unusually clean for a technical
reconstruction; zero sentences failed the slop test outright.

Edge sentences I scrutinized and kept, because each carries a fact or a reasoning
step rather than leaning on its neighbors: "The methods work while the quantities
the theory reasons about behave nothing like the theory expects" (the companion
analysis's actual synthesis, landing the gradient-correlation and 50%-value
facts); "The honest statement is the narrow one" (introduces the specific narrow
claim that follows); the verdict's closing falsification condition (a concrete
study that would move the assessment, not a generic moral); and the pull quote
("The advantage over TRPO happened...not the fact of the advantage"), which is
the Huszár distinction the voice guide asks for and the article's own best line.

Negative-parallelism check: the article's "not X, it is Y" constructions
("The question...is not whether that measurement is real. It is what the
measurement is worth"; "That dominance is not in question here. What is in
question is which part...") each correct a misconception the piece actually
names (that the reexamination denies the clip result; that questioning the
mechanism questions PPO). Earned, not invented. Kept.

Leakage check against the commission, brief, and voice guide: "unglamorous" is
the commission's characterization, but the tricks it labels are genuinely
mundane engineering (reward scaling, gradient clipping, observation
normalization), so it reads as a sourced description rather than a lifted
instruction. No planning labels, selection rules, or assignment-fulfilled claims
survive into the prose.

Formula check against the recent-pattern notes: the headline breaks both the
possessive-plus-appositive mold and the negative-parallelism mold; it is a plain
subject-verb-object finding. The opener starts on a mechanism ("A policy
gradient tells an agent which direction...makes good actions more likely"), not
the recent cold result-plus-metric sentence. Section headings are varied in
construction and none copies a prior piece's comma-and shape.

One cut made, in display text: the dek repeated the headline's exact verb-object
("traced most of [PPO's/its] edge to"). The headline standard bars the dek from
restating the headline, so I rewrote the dek's second clause to "located most of
its reward margin over TRPO in nine unglamorous training tricks" -- distinct
verb, more precise object (reward margin, closer to Engstrom's own wording), and
the concession still leads. Kept both copies (nb-meta and dekline) in sync.

## Reader

Reading straight through as the declared reader (ML-engineering background), what
I have that the sources alone would not give me: PPO's clipped objective and full
training loop rebuilt from the paper's own equations with a worked numeric
example, staged against the two reexaminations on the *same* reconstructed
objective, so the exact seam is visible -- the clip's stated job (hold a ratio
trust region) set beside its measured behavior (ratio violated, KL not), with the
paper's own ablation and an independent large study steelmanned first and the
credit relocated without overclaiming. No single source does that weighing; it is
synthesized across five papers. The draft-handoff's original-work sentence makes
the same claim, and the article delivers it. The prose sits closer to the
voice-guide exemplars than a median summary: Karpathy's smallest-case worked
example, Olah's claim-as-a-question-then-count in the ablation section, and
Huszar's concession-then-limit in the containment caveat and the verdict. The
headline as the largest claim is supported by Engstrom Table 2 and holds.

## Edits

- Rewrote the dek (both nb-meta "dek" and the rendered dekline) from "...traced
  most of its edge over TRPO to nine unglamorous training tricks" to "...located
  most of its reward margin over TRPO in nine unglamorous training tricks," to
  stop the dek restating the headline's verb-object and to tighten "edge" to
  "reward margin."

## Required work

- Orchestrator: none blocking. Equation markup is the sanctioned KaTeX furniture
  (one annotated equation on L^CLIP, within the one-per-article limit); the
  offline KaTeX-load failure noted by the writer is not an article defect and the
  live render-check runs in CI. No equation-markup concern to escalate.
- Writer: none. Source assets and table provenance verified and correct.
- Researcher: none.

## Decision

approve -- the math and the numbers verify against the record and owning papers,
both load-bearing corrections (ratio-vs-KL, advertised-vs-operative with the
paper's ablation and Andrychowicz steelmanned) survive intact, and the one
display-text defect was fixable in place.
