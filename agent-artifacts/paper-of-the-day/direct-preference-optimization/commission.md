# Commission: paper-of-the-day/direct-preference-optimization

(Replaces a mis-slugged paper: `chinchilla` was already published, so it was
withdrawn. This is a first publication of a fresh paper.)

## Assignment

Reconstruct the central claim of "Direct Preference Optimization: Your Language
Model is Secretly a Reward Model" (Rafailov, Sharma, Mitchell, Manning, Ermon,
Finn; NeurIPS 2023): the standard RLHF pipeline (fit a reward model to human
preferences, then optimize the policy against it with reinforcement learning under
a KL penalty) can be replaced by a single supervised classification loss on
preference pairs, with no explicit reward model and no RL loop. Rebuild the
derivation from the paper's own math and weigh the claim against the public record
that followed.

## Why this paper

DPO reorganized open-model post-training and became a default alignment method,
and it has the after-the-fact record the series wants: extensions and critiques
that let the article test the claim against what happened next (for example Azar
et al.'s IPO on preference-overfitting when the reward model's regularization is
removed; KTO; and analyses of whether offline DPO matches on-policy PPO/RLHF, plus
work on DPO's tendency to push probability mass off-distribution and lower the
likelihood of the preferred response). The Nightly Build's InstructGPT piece
already foreshadowed this result; DPO is its natural successor, not a repeat.

## Reconstruction demands

- Set the math the argument leans on rather than paraphrasing it: the
  KL-constrained reward-maximization objective, its closed-form optimal policy, the
  reparameterization that expresses the reward as a function of the policy and the
  reference policy, and how substituting it into the Bradley-Terry preference model
  cancels the partition function to leave the DPO loss. Show the gradient's meaning
  (it up-weights preferred and down-weights dispreferred responses in proportion to
  how wrongly the implicit reward orders them).
- Bring the figures the claim turns on into the article as captured source assets
  (for example the sentiment-control reward-vs-KL frontier where DPO dominates PPO,
  and the summarization/dialogue win-rate results), with captions and prose that
  say what each settles.
- Weigh the claim: what DPO provably matches in the RLHF objective, where later
  work found it diverges from on-policy RLHF in practice, and what the critiques
  established.
- Source floor: at least 8 sources, the primary paper and its artifacts first.

## Boundaries

Stay a reconstruction and assessment, not a survey of preference-optimization
methods. The reader is an ML engineer: assume transformers and the RLHF/InstructGPT
baseline, and teach the DPO derivation itself.

## Recent-pattern habits to avoid

The series spine is "the paper claimed X; the later record showed Y", which is the
mandate. Vary the dek and headline construction from the recent run (avoid the "a
cause the paper floated and left open" family); commit the finding in this paper's
own terms.

## Neighboring articles this run

Six other articles publish today; none overlaps. Tech News may carry AI news but
this is a 2023 paper reconstruction and will not collide.

## Production policy (balanced profile)

- writing-coach: effort low, model capable. researcher: effort high, model capable.
  writer: effort medium, model capable. editor: effort high, model inherit, required.
- No `required` model or effort directive exists for this series. `capable` resolves
  to the most capable available tier (Opus); the required editor runs on the inherited
  orchestrator model (Opus 4.8). Neither is a trade-down. Effort is production guidance.

## Suggested tags

rlhf, preference-optimization, dpo, alignment, language-models
