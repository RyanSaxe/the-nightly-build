# Researcher brief — paper-of-the-day/knowledge-distillation (01)

## Your task
Read and verify the sources for this article and write `evidence.md` in this
directory. The writer and editor use it as the complete, traceable claim set.
Drafting is not your job.

## The assignment
A `paper` reconstruction of **Hinton, Vinyals & Dean, "Distilling the Knowledge
in a Neural Network" (2015, arXiv:1503.02531)**: rebuild the temperature-softmax
/ soft-target ("dark knowledge") mechanism and its MNIST and speech results,
then weigh the claim against the public record — chiefly **Stanton et al., "Does
Knowledge Distillation Really Work?" (NeurIPS 2021, arXiv:2106.05945)**, the
focal counter-evidence, read in full.

## Required primary reading (read the paper, not summaries)
1. Hinton, Vinyals & Dean 2015 — arXiv:1503.02531. Extract, verbatim where it
   earns display: the abstract; the temperature-softmax Eq. (1)
   `q_i = exp(z_i/T) / sum_j exp(z_j/T)`; the definition of soft targets and the
   relative-probabilities-of-wrong-answers idea (BMW / garbage truck / carrot;
   the 2 that is 10^-6 a 3 and 10^-9 a 7); the two-objective training and the
   1/T^2 gradient scaling; "matching logits is a special case" (Eq. 4,
   `~ (z_i - v_i)/(N T^2)`); the MNIST numbers (67 vs 146 vs 74 errors; the
   omitted-3 experiment; 7s/8s-only); Table 1 speech (baseline / 10x ensemble /
   distilled; "more than 80%" transferred); Table 5 soft-targets-as-regularizer
   (3% of data). Note the venue: NIPS 2014 Deep Learning Workshop.
2. Stanton et al. 2021 — arXiv:2106.05945. Extract the fidelity-vs-generalization
   distinction and definitions (Eq. 2 top-1 agreement, Eq. 3 predictive KL); the
   central finding (students fail to match the teacher even with capacity); the
   easy-vs-hard contrast (LeNet-5/MNIST >99% test agreement vs ResNet-56/CIFAR-100
   plateau); augmentation results (MixUp τ=4 best fidelity at 86%; Baseline τ=4
   at 84.5%); the optimization diagnosis (train agreement 78.95% at 300 epochs →
   83.3% at 5k; the λ-initialization basin experiment; Table 1 shared-init
   result); and the four discussion findings.

## Follow-ons to weigh (read the specific cited claim in each)
3. Sanh et al. 2019, DistilBERT — arXiv:1910.01108 (the 40% smaller / 60% faster
   / 97% of GLUE claim).
4. Furlanello et al. 2018, Born-Again Networks — arXiv:1805.04770 (identical-
   capacity student outperforms teacher).
5. Müller, Kornblith & Hinton 2019, "When Does Label Smoothing Help?" —
   arXiv:1906.02629 (a label-smoothed teacher distills worse; logit relational
   info is what distillation needs).
6. Buciluǎ, Caruana & Niculescu-Mizil 2006, "Model Compression" — the origin
   Hinton develops (compressing an ensemble into one small model).
7. Ba & Caruana 2014, "Do Deep Nets Really Need to be Deep?" — arXiv:1312.6184
   (logit matching; shallow mimics reach accuracies training-on-labels could not).
8. Beyer et al. 2022, "A good teacher is patient and consistent" —
   arXiv:2106.05237 (function matching; consistent views; up to ~9600 epochs;
   82.8% ResNet-50 ImageNet — the success that answers Stanton's optimization
   diagnosis).

## Source policy
min_sources 8. Each item above is a primary source: its authors own its claims.
Classify each primary/secondary with a reason. Verify every number against the
paper that owns it. Confirm every URL resolves (arXiv abs pages; the Buciluǎ PDF
at cs.cornell.edu). Search for what breaks the angle — record contradictions
(e.g. Beyer vs Stanton; Born-Again's "failing to match helps").

## Deliver
Evidence record with the standard sections (opening note, Sources,
Contradictions, Numbers, Source assets, Discarded). Flag any figure worth a
chart with its full series. Return `DONE researcher <evidence-path>`.
