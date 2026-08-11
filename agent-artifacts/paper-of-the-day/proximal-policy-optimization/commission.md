# Commission: paper-of-the-day/proximal-policy-optimization

## Assignment

Reconstruct and weigh one machine-learning paper: John Schulman, Filip Wolski,
Prafulla Dhariwal, Alec Radford, and Oleg Klimov, "Proximal Policy Optimization
Algorithms" (2017, arXiv:1707.06347). Template `paper` (longread, 1800-3400
words, 2-8 flexible sections). Authorized scheduled work from `nb duty`; open
Paper-of-the-Day slot, one article. (An earlier plan for this slot collided with
an already-published article; this is the replacement subject. The batch
normalization slug and the exact fair-use disagreement are already in the
library — do not go near them.)

## Why this paper, and the angle

PPO became the default deep-RL policy-gradient method, and the public record
after publication did what this desk looks for: a controlled reexamination found
that the paper's headline mechanism was not what carried the results. PPO's
stated contribution is the clipped surrogate objective, a cheap way to keep each
policy update inside a trust region without TRPO's constrained optimization.
Engstrom, Ilyas, Santurkar, Tsipras, Janoos, Rudolph, and Madry, "Implementation
Matters in Deep Policy Gradients: A Case Study on PPO and TRPO" (ICLR 2020,
arXiv:2005.12729), and the companion "A Closer Look at Deep Policy Gradients"
(arXiv:1811.02553), showed that a set of unglamorous "code-level optimizations"
(reward/observation normalization, value-function clipping, orthogonal
initialization, learning-rate annealing, advantage normalization, gradient
clipping) account for much of PPO's advantage over TRPO, and that PPO's clipping
does not reliably keep updates within the trust region it was designed to enforce.

The angle is the gap between the mechanism a paper advertises and the mechanism
that does the work: PPO's clipped objective is real and widely used, but the
controlled ablations located much of its measured benefit in the surrounding
implementation. Do not overclaim that PPO "does not work" or was debunked; it is
the field's workhorse. Steelman the clipped-objective account and the paper's own
ablations (it compares clipping to a KL-penalty variant and to no clipping)
before weighing the reexamination, and record where the picture is genuinely
contested (later work and library maintainers dispute how much the code-level
tricks generalize, and PPO's practical dominance is not in question).

## Reconstruction obligations

Rebuild the argument with the paper's own artifacts, not a paraphrase:
- Set the math the reconstruction leans on: the probability ratio r_t(theta), the
  unclipped surrogate, the clipped surrogate objective L^CLIP with its epsilon,
  why the min() of clipped and unclipped is a pessimistic (lower) bound, and how
  generalized advantage estimation supplies the advantages. Explain the actor-
  critic loss actually optimized (policy term, value term, entropy bonus) and the
  multiple-epoch minibatch updates that distinguish PPO from a single gradient
  step.
- Bring in the figures the claim turns on as captured source assets with factual
  captions and prose that says what each settles: candidates are the paper's
  clipping-illustration figure and its continuous-control / Atari comparison
  curves, and the Engstrom et al. ablation figures isolating the code-level
  optimizations and the trust-region-violation measurement. Use `nb asset` only
  for an exact visual from a cited primary or public document whose argument the
  article spends.

## Sources

`min_sources` is 8. Required primaries: the PPO paper (1707.06347), Engstrom et
al. (2005.12729), and the companion analysis (1811.02553). Add the supporting
record: TRPO (Schulman et al. 2015, 1502.05477) for the trust-region baseline PPO
approximates; GAE (1506.02438); and later work on PPO reproducibility or the
"what matters in on-policy RL" line (e.g. Andrychowicz et al. 2020,
2006.05990). Every figure the article reproduces or reasons from is checked
against the owning primary. Cite only what you have read; every URL resolves to
the source's page (arXiv abs pages, not PDF-fetch endpoints; the OpenReview page
for the ICLR paper is acceptable as its own page).

## Required contribution

The reader finishes able to reconstruct PPO's clipped objective and training loop
from memory, to state precisely what the clipping was meant to guarantee and what
the controlled experiments showed it does and does not deliver, and to say which
parts of PPO's measured advantage the reexamination attributed to implementation.
The article puts the paper's own explanation next to the reexamination on the same
reconstructed objective and shows exactly where they part.

## Boundaries with the rest of tonight's edition

No overlap with the news briefs, the tariff-authority argument, the parenting
piece, or the word. Keep this self-contained to PPO and its follow-on record.

## Habits not to inherit

- Recent Paper-of-the-Day headlines run a fixed mold: possessive-plus-appositive
  ("CLIP's robustness came from its data, a cause the paper floated") and negative
  parallelism ("Dropping bidirectionality broke BERT where dropping its sentence
  task did not"). PPO's story is the same shape (advertised mechanism vs. what
  the ablations found), so the headline must break that wording, not restate it in
  the same frame. State the finding in the piece's own nouns.
- Recent openers start cold on a result sentence naming authors and a metric.
  Vary the entry.
- Do not close on a line that grades the paper or the field in the abstract.

## Production record

- Profile: balanced (`press/production.yaml`).
- writing-coach: capable tier (Claude Sonnet), effort low.
- researcher: capable tier (Claude Opus), effort high.
- writer: capable tier (Claude Opus), effort medium.
- editor: inherit (Claude Opus), effort high, required.
- Harness sets reasoning effort at the session level; per-role effort is the
  policy target executed on the closest available runtime setting. No `required`
  model or effort directive applies, so no deviation is owed.
