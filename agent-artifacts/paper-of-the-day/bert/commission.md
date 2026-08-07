# Commission: paper-of-the-day/bert

## Why this paper replaces the first pick
The originally commissioned Chinchilla paper is ALREADY PUBLISHED
(paper-of-the-day/chinchilla, 2026-07-22) with the same angle. Paper-of-the-day
is open mode and must not repeat a published slug or topic. This commission
replaces it with an uncovered paper.

## Subject
Devlin, Chang, Lee, Toutanova, "BERT: Pre-training of Deep Bidirectional
Transformers for Language Understanding" (NAACL 2019; arXiv:1810.04805). Focal
paper for the paper template. Confirmed not in the published set (attention,
word2vec, resnet, etc. are covered; BERT is not).

## Angle (a claim that can be rebuilt, with a real public record)
Central claim: deep BIDIRECTIONAL pretraining via masked language modeling
(MLM) lets one pretrained encoder transfer to many tasks with light fine-tuning,
beating left-to-right pretraining (GPT) and shallow feature-based approaches
(ELMo). Rebuild the MLM objective (mask ~15% of tokens; the 80/10/10
mask/random/keep split and WHY) and the pretrain-then-fine-tune recipe.

The public record is the reason to run it and must be weighed:
- RoBERTa (Liu et al. 2019) showed BERT was significantly UNDERTRAINED and that
  the Next Sentence Prediction (NSP) auxiliary objective was unnecessary (even
  mildly harmful) — trained longer, on more data, with bigger batches and no
  NSP, it beat BERT. BERT's own ablation (Section 5.1) already hinted NSP's
  contribution was small: a nice "the paper's own table foreshadowed it."
- ELECTRA (Clark et al. 2020) argued MLM is sample-inefficient (only the ~15%
  masked tokens are supervised) and replaced it with replaced-token detection.
So the verdict: the headline (bidirectional MLM pretraining + fine-tuning
transfer) was the durable, field-defining contribution; BERT's own secondary
claim (NSP helps) did not survive; and MLM's supervision inefficiency was a real
limit that motivated successors. Ground each limb in a cited source.

## Reconstruction requirements (template)
- Set the MLM objective as math (masked-token cross-entropy) and operate on it;
  explain bidirectionality vs the left-to-right factorization it breaks with.
- The quantitative evidence is in TABLES (GLUE test results; the Section-5
  ablations: No-NSP vs BERT-base; BERT-base vs BERT-large; feature-based vs
  fine-tuning) and RoBERTa's comparison table. Bring the comparisons the claim
  turns on into the article as ORIGINAL house charts via nb chart (do NOT lift
  arXiv figure images — arXiv non-exclusive license; the template-mandated
  abstract card is the only verbatim reproduction). Say what each chart settles.
- min_sources 8, prefer primary (BERT, RoBERTa, ELECTRA, the GLUE benchmark
  paper, and the specific tables each claim rests on).

## Boundaries
Focal paper owns its claims; RoBERTa/ELECTRA/GLUE earn space only where they
change the interpretation. Do not drift into a survey of every encoder since.
Distinct from the published attention-is-all-you-need (architecture) and
word2vec (static embeddings): this is about the pretraining objective and
transfer, and the field's re-examination of what in the recipe mattered.

## Template / policy
paper template; abstract card + reconstruction + evidence review + verdict +
sources. production policy: coach low, researcher high, writer medium (capable
models), editor high/inherit REQUIRED. Harness Claude Code, model
claude-opus-4-8 for correspondent roles unless a role records a deviation.

## Neighbors in this run
Six other articles today; only this touches ML research. No overlap.

## Habits not to inherit (recent paper-of-the-day)
- No author roll-call opener; open on the claim or the tension.
- Avoid the "and every later model inherited…" closer and comma-triad deks;
  check recent deks first.
