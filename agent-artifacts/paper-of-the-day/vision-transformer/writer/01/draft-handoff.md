# Writer handoff: paper-of-the-day/vision-transformer (writer/01)

## Original-work sentence

The article isolates architecture, training recipe, and pretraining scale as
three separate variables inside the ViT-vs-CNN gap by building one synthesis
table from three different papers' controlled comparisons — ConvNeXt's
recipe-only ResNet-50 ablation, DeiT's recipe-only ViT-B ablation, and the
isotropic ConvNeXt/ViT architecture-only tie — that no single source paper
puts side by side, and uses that accounting to show the ViT paper's own
crossover is real as a measurement but does not, by itself, establish
architecture as the variable that needed the data.

## Proof result

Exact brief command, links checked:

```
./nb check .nb-work/paper-of-the-day/vision-transformer/library/paper-of-the-day/vision-transformer.html --series paper-of-the-day --library /home/user/library-checkout
```

Result: `BLOCK: 0`, `WARN: 2`, verdict `PUBLISHABLE`. `nb stamp` has been run
(words=3297, reading_minutes=14, sources=4).

Warnings intentionally left:

- `W-SENTENCE-DENSITY sentence is 49 words with 8 clause joins, punctuation
  score 82` — this is the annotated equation's TeX source (Equation 1's
  `<div class="nb-math-eq">` content: the patch-embedding assembly with four
  `\htmlClass` terms). The furniture contract requires the element's text to
  be literal TeX, and `div` is a sentence-break tag but not a sentence-skip
  tag, so the heuristic reads the equation's semicolons and braces as prose
  punctuation. It is not prose and there is no rewrite that removes the
  warning without breaking the equation.
- `W-SOURCES-MIN 4 sources; series floor is 8` — the evidence record verifies
  exactly four documents (the focal ViT paper plus DeiT, ConvNeXt, and Raghu
  et al., each read in full). The brief and skill require treating the
  evidence record as the only claims available and citing only sources it
  contains; padding to eight would mean citing something the researcher did
  not open. Left as the honest count.

## Open questions

None outstanding. The evidence record's one flagged bound — no after-record
source retrains a ViT-H/14-scale model on ImageNet-1k alone — is stated
explicitly in the body (end of "ViT-B/16 gains 6.24 points…") and again as
the verdict's closing question, rather than left implicit.
