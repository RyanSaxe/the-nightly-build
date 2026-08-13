# Evidence record: paper-of-the-day/vision-transformer (researcher/01)

All four papers named in the brief were read in full, including appendices, from
the arXiv PDF (fetched via the paper's own arXiv listing). The architecture,
model-variant table, main results table, and both scale-related figures (data
scale and compute) in the Vision Transformer paper are confirmed with exact
numbers. Each after-record paper yields a specific, checkable result on the
architecture-vs-recipe/scale question. The evidence complicates the
commission's reading in a specific, bounded way: DeiT and ConvNeXt both show
that the ViT paper's own scale claim is real (its numbers hold up) but that its
implicit "only web-scale data gets you there" reading does not hold once
training recipe is treated as a free variable, and ConvNeXt further shows a
non-attention architecture reaches near-parity with ViT-style models when
recipe and scale are held fixed. Raghu et al. is more of a mechanism paper than
a contradiction: it shows the crossover is real at the representation level,
not just the scoreboard level, while also showing what changes as data scales
(the model learns local, CNN-like attention it does not learn without scale).
Thin spots: DeiT's recipe result is demonstrated only at the ViT-Base
parameter count (86M); the brief's largest-model crossover (ViT-H/14 at
88.55%) is not itself contested by any after-record paper here. ConvNeXt is
pretrained on ImageNet-22K (14M images), not JFT-300M (303M), so its 87.8%
result is a near-match at roughly 1/20th the pretraining images, not a
same-dataset architecture ablation against ViT-H.

## Sources

```text
URL:         https://arxiv.org/abs/2010.11929
Kind:        primary — Dosovitskiy et al., "An Image Is Worth 16x16 Words:
             Transformers for Image Recognition at Scale," published as a
             conference paper at ICLR 2021 (banner on p.1 of the PDF); this is
             the paper that owns the ViT architecture and the JFT-300M/
             ImageNet-21k/ImageNet-1k crossover claim.
Establishes: The ViT architecture (patch embedding, class token, position
             embeddings, transformer encoder), the three model sizes and
             patch variants, the ImageNet/ReaL/CIFAR/VTAB accuracy numbers,
             the TPUv3-core-day compute figures, and the two figures (data
             scale, compute-vs-accuracy) the crossover claim rests on.
Paraphrase:  Full text read section by section: Abstract; Introduction;
             Related Work; Method (3.1 Vision Transformer, 3.2 Fine-tuning and
             higher resolution); Experiments (4.1 Setup, 4.2 Comparison to
             state of the art, 4.3 Pre-training data requirements, 4.4 Scaling
             study, 4.5 Inspecting Vision Transformer, 4.6 Self-supervision);
             Conclusion; Appendix A (Multihead self-attention), Appendix B
             (Experiment details), Appendix C (Additional results, Tables 5-6),
             Appendix D (Additional analyses D.1-D.10, Figures 8-14, Tables
             7-9).
Locators:    Abstract p.1; Fig. 1 p.3; Eq. 1-4 p.4; Table 1 p.5; Section 4.1
             p.4; Table 2 and Fig. 2 p.6; Section 4.3, Fig. 3-4 p.7; Section
             4.4, Fig. 5 p.7-8; Appendix C Tables 5-6 p.15; Appendix D.9 p.20.
Quote:       "However, the picture changes if the models are trained on
             larger datasets (14M-300M images). We find that large scale
             training trumps inductive bias." (p.2)
Quote:       "The BiT CNNs outperform ViT on ImageNet, but with the larger
             datasets, ViT overtakes." (p.7, discussing Fig. 3)
Quote:       "ViT uses approximately 2-4x less compute to attain the same
             performance (average over 5 datasets)." (Section 4.4, p.8)
```

```text
URL:         https://arxiv.org/abs/2012.12877
Kind:        primary — Touvron, Cord, Douze, Massa, Sablayrolles, Jégou,
             "Training data-efficient image transformers & distillation
             through attention" (DeiT), Facebook AI / Sorbonne. Primary for
             its own result: the ImageNet-1k-only accuracy DeiT reaches and
             the hard-distillation method that gets it there. (No venue
             banner appears in the arXiv PDF text itself; not asserting a
             conference venue beyond what the paper states.)
Establishes: The exact top-1 accuracy DeiT-B/DeiT-B-distilled reach training
             on ImageNet-1k alone (no JFT-300M, no ImageNet-21k), the training
             compute/time that took, and the explicit comparison DeiT draws
             to ViT's own "insufficient data" framing.
Paraphrase:  Read in full: Abstract through Conclusion, all tables (1-10),
             both figures, and the full reference list. Architecture is
             stated to be identical to ViT-B (Section 5.1: "our architecture
             design is identical to the one proposed by Dosovitskiy et al.
             [15] with no convolutions"); the only differences are training
             recipe (heavy data augmentation: RandAugment, Mixup, CutMix,
             random erasing, stochastic depth, repeated augmentation) and the
             new distillation-token mechanism.
Locators:    Abstract p.1; Section 1 (quotes ViT's "do not generalize well
             when trained on insufficient amounts of data" claim) p.2;
             Section 3 (architecture recap) p.4-6; Section 4 (hard-label
             distillation, Eq. 2-3, distillation token, Fig. 2) p.6-8; Table 1
             p.9 (model variants); Table 3 p.10 (distillation ablation); Table
             5 p.12 (full accuracy/throughput comparison incl. ViT-B/16,
             ViT-L/16); Table 8 p.15 (data-augmentation ablation); "Training
             time" paragraph p.17.
Quote:       "Their paper presented excellent results with transformers
             trained with a large private labelled image dataset (JFT-300M
             [46], 300 millions images). The paper concluded that transformers
             'do not generalize well when trained on insufficient amounts of
             data', and the training of these models involved extensive
             computing resources." (p.2)
Quote:       "Our best model on ImageNet-1k is 85.2% top-1 accuracy outperforms
             the best Vit-B model pretrained on JFT-300M at resolution 384
             (84.15%)." (Section 5.2, p.9)
Quote:       "A typical training of 300 epochs takes 37 hours with 2 nodes or
             53 hours on a single node for the DeiT-B." (Section 6, p.17)
```

```text
URL:         https://arxiv.org/abs/2108.08810
Kind:        primary — Raghu, Unterthiner, Kornblith, Zhang, Dosovitskiy, "Do
             Vision Transformers See Like Convolutional Neural Networks?"
             35th Conference on Neural Information Processing Systems
             (NeurIPS 2021) (banner on p.1). Primary for its own
             representation-similarity findings about ViT vs. ResNet and the
             effect of pretraining-data scale on those representations.
             Co-authored by Dosovitskiy (ViT's own lead author), so it is an
             internal, not outside, re-examination of the original claim.
Establishes: Whether ViT's internal representations look like a CNN's; how
             much of that difference is attributable to self-attention vs.
             skip connections; and — the piece that speaks most directly to
             the commission's crossover claim — how pretraining-data scale
             changes what ViT's early layers learn to do (attend locally or
             not) and how well its higher-layer representations transfer.
Paraphrase:  Read in full: Abstract through Discussion/Conclusion (Sections
             1-9) and Appendices A-H, including all figures and their
             captions.
Locators:    Section 3 (CKA method) p.2-3; Section 4, Fig. 1-2 (representation
             structure) p.3; Section 5, Fig. 3-4 (attention distance, effect
             of scale on locality) p.4; Section 6, Fig. 7-8 (skip connections)
             p.5-6; Section 7, Fig. 9-11 (spatial localization) p.7-8; Section
             8, Fig. 12-13 (effects of scale on transfer learning) p.9-10;
             Appendix C.5/Fig. C.5 (ViT-B/32 exception) p.19.
Quote:       "Interestingly, we see a clear effect of scale on attention. ...
             we see that with not enough data, ViT does not learn to attend
             locally in earlier layers. Together, this suggests that using
             local information early on for image tasks (which is hardcoded
             into CNN architectures) is important for strong performance."
             (Section 5, p.4)
Quote:       "We observe the JFT-300M pretained models achieve much higher
             accuracies even with middle layer representations, with a ~30%
             gap in absolute accuracy to the models pretrained only on
             ImageNet. This suggests that for larger models, the larger
             dataset is especially helpful in learning high quality
             intermediate representations." (Section 8, p.9-10)
```

```text
URL:         https://arxiv.org/abs/2201.03545
Kind:        primary — Liu, Mao, Wu, Feichtenhofer, Darrell, Xie, "A ConvNet
             for the 2020s" (ConvNeXt), Facebook AI Research / UC Berkeley.
             Primary for its own roadmap experiment and resulting model's
             accuracy numbers. (No venue banner appears in the arXiv PDF text
             read; not asserting a conference venue.)
Establishes: How much of the ViT/Swin-vs-ResNet gap is attributable to
             training recipe alone (measured by holding architecture fixed
             and changing only the training procedure); and whether a
             modernized pure-CNN, once given the same recipe and comparable
             macro/micro design choices, matches transformer-style models at
             matched compute and at scale, including under large-scale
             pretraining and on downstream detection/segmentation tasks.
Paraphrase:  Read in full: Abstract through Conclusion (Sections 1-6) and
             Appendices A-G, all tables and figures.
Locators:    Section 1 (introduction, framing quote) p.1-2; Section 2.1
             (training-recipe-only result) p.3; Fig. 2 / Table 10 (full
             roadmap) p.3, p.11; Section 2.2-2.6 (macro/ResNeXt-ify/inverted
             bottleneck/large kernel/micro design steps) p.3-6; Section 3,
             Table 1 (ImageNet-1K/22K results) p.6-7; Section 3.3, Table 2
             (isotropic ConvNeXt vs. ViT) p.7; Section 4, Table 3 (COCO),
             Table 4 (ADE20K) p.8.
Quote:       "However, the effectiveness of such hybrid approaches is still
             largely credited to the intrinsic superiority of Transformers,
             rather than the inherent inductive biases of convolutions."
             (Abstract, p.1)
Quote:       "By itself, this enhanced training recipe increased the
             performance of the ResNet-50 model from 76.1% [1] to 78.8%
             (+2.7%), implying that a significant portion of the performance
             difference between traditional ConvNets and vision Transformers
             may be due to the training techniques." (Section 2.1, p.3)
Quote:       "We observe ConvNeXt can perform generally on par with ViT,
             showing that our ConvNeXt block design is competitive when used
             in non-hierarchical models." (Section 3.3, p.7)
```

## Contradictions

The commission's central claim — "ViT trails CNNs when trained on
ImageNet-sized data and overtakes them only after pretraining on the larger
JFT-300M" — is verified as an accurate statement of what the ViT paper itself
found (Table 2, Figure 3, Figure 4; see Numbers below). It is not
contradicted by any after-record source on its own terms: nobody retrains
ViT-H/14 on ImageNet-1k and beats its JFT-300M number.

What the after-record complicates is the reading the commission's angle draws
from that finding — that the crossover shows something intrinsic to the
transformer architecture that a CNN could not also do. Two specific
findings cut against that broader reading:

1. **DeiT (2012.12877) shows the ViT-B-sized crossover is a recipe artifact,
   not an architecture-and-data-scale-only phenomenon.** ViT's own appendix
   (Table 5 of arXiv:2010.11929) reports ViT-B/16 trained on ImageNet-1k alone
   reaches 77.91% top-1 — the "modest accuracies... below ResNets" result the
   ViT paper itself describes (p.1-2). DeiT uses the *identical* ViT-B
   architecture, trains on ImageNet-1k alone with no external data, and
   reaches 81.8% (Table 3/5), or 83.1% after a 384-resolution fine-tune
   (identical setup to ViT's own fine-tuning practice), or 85.2% with
   hard-label distillation from a convnet teacher (Table 5, best row). That
   85.2% figure exceeds ViT-B/16 pretrained on the full JFT-300M dataset at
   384 resolution (84.15%, both DeiT Section 5.2 and ViT's own Table 5).
   Architecture and evaluation data are held fixed; only training recipe and
   distillation changed. This directly undercuts a reading that only
   web-scale pretraining data can train a competitive ViT at this parameter
   count — DeiT's own framing states this explicitly ("we achieve a strong
   performance without requiring a large training dataset, i.e., with
   Imagenet1k only," p.4). It does **not** speak to whether the same recipe
   substitution would let a from-scratch, ImageNet-1k-only ViT-H/14 match its
   JFT-300M-pretrained 88.55%: DeiT never scales its recipe past the
   86M-parameter Base size.

2. **ConvNeXt (2201.03545) shows a large share of the transformer-vs-CNN gap
   the commission's crossover sits inside was a recipe gap, not an
   architecture gap, and that the residual gap closes with no self-attention
   at all.** Taking an unmodified ResNet-50 and changing nothing but the
   training procedure (AdamW, 300 epochs, Mixup/CutMix/RandAugment/stochastic
   depth/label smoothing — the same family of techniques DeiT introduced)
   raises its ImageNet-1K accuracy from 76.1% to 78.8%, a +2.7-point gain
   attributable to training procedure alone, with zero architectural change
   (Section 2.1). Carrying that recipe forward and then modernizing the
   macro/micro architecture (patchify stem, depthwise convolution, inverted
   bottleneck, 7x7 kernels, GELU, fewer norms, LayerNorm) — introducing no
   attention mechanism anywhere — reaches ConvNeXt-T at 81.97%, beating
   Swin-T's published 81.30% (Table 10; Swin-T is a hierarchical, windowed
   ViT variant, the closest published transformer at matched FLOPs). This
   holds across scale: ConvNeXt-B at 384px beats Swin-B at 384px (85.1% vs.
   84.5%, Table 1), and ConvNeXt-XL pretrained on ImageNet-22K (14M images)
   reaches 87.8% — near ViT-H/14's 88.55% on JFT-300M (303M images), at
   roughly 1/20th the pretraining images, though not the same dataset so not
   a controlled ablation. Most directly on point: ConvNeXt's isotropic
   variant (no hierarchy, no downsampling stages, matched to ViT's own
   non-hierarchical shape) ties ViT-S/B/L almost exactly at matched parameter
   count and FLOPs when trained with the same recipe — 79.7% vs. 79.8%
   (S), 82.0% vs. 81.8% (B), 82.6% vs. 82.6% (L) (Table 2). With
   architecture's most attention-specific feature (self-attention itself)
   removed and recipe/scale held constant, the result is a statistical tie.
   This is the single most direct piece of evidence bearing on "architecture
   vs. recipe/scale" in the after-record: at matched design, recipe, and
   data, self-attention adds approximately nothing over depthwise
   convolution.

3. **Raghu et al. (2108.08810) is not a contradiction of the crossover but a
   mechanism account of it, with one qualification worth recording.** It
   finds the crossover corresponds to a real, measurable representational
   difference: ViT-L/16 and ViT-H/14 pretrained on JFT-300M develop
   higher-quality intermediate-layer representations than the same
   architectures pretrained on ImageNet alone, by roughly 30 points of
   absolute linear-probe accuracy at middle layers (Fig. 13, Section 8) — so
   the crossover is not merely a fine-tuning-time artifact. But the paper
   also shows what data scale is *doing*: without enough pretraining data,
   ViT-L/16 and ViT-H/14's lowest layers fail to learn to attend locally at
   all (Fig. 3 vs. Fig. 4, Section 5) — a property CNNs get for free from
   their architecture. Scale is functioning here largely as a substitute for
   an inductive bias the architecture lacks, which is compatible with the
   commission's crossover claim but complicates a reading of the crossover
   as evidence that self-attention is doing something a convolutional prior
   could not. One qualification: Appendix Figure C.5 shows the smallest
   model tested, ViT-B/32, learns to attend locally even when trained on
   ImageNet alone — the "needs scale to learn locality" finding is
   demonstrated for ViT-L/16 and ViT-H/14, not uniformly across all model
   sizes.

No source in the after-record disputes the ViT paper's own reported numbers
(Table 2, Figure 3, Figure 4) as measurements; the dispute is entirely about
what those measurements are evidence for.

## Numbers

```text
Figure: ViT-H/14 (JFT-300M) — 88.55% ± 0.04 top-1 ImageNet
Owner:  Dosovitskiy et al. 2010.11929, Table 2 / Abstract
Scope:  ImageNet-1k validation set, fine-tuned at 518px after JFT-300M
        pretraining, mean and std over 3 fine-tuning runs; 2.5k
        TPUv3-core-days pretraining compute.

Figure: ViT-H/14 (JFT-300M) — 90.72% ± 0.05 top-1 ImageNet-ReaL,
        94.55% ± 0.04 CIFAR-100, 77.63% ± 0.23 VTAB (19 tasks)
Owner:  Dosovitskiy et al. 2010.11929, Table 2 / Abstract
Scope:  Same pretraining/fine-tuning run as above; VTAB uses 1,000 training
        examples per task across 19 tasks in three groups.

Figure: ViT-L/16 (JFT-300M) — 87.76% ± 0.03 ImageNet; 0.68k TPUv3-core-days
        ViT-L/16 (ImageNet-21k) — 85.30% ± 0.02 ImageNet; 0.23k TPUv3-core-days
        BiT-L / ResNet152x4 (JFT-300M) — 87.54% ± 0.02 ImageNet; 9.9k
        TPUv3-core-days
        Noisy Student / EfficientNet-L2 — 88.4/88.5%* ImageNet; 12.3k
        TPUv3-core-days
Owner:  Dosovitskiy et al. 2010.11929, Table 2
Scope:  Compute is TPUv3 cores (2/chip) x training days; *88.5% is a
        slightly improved number the ViT paper attributes to Touvron et al.
        2020, not to Xie et al.'s original Noisy Student report.

Figure: Pretraining datasets — ImageNet: 1,000 classes, 1.3M images.
        ImageNet-21k: 21,000 classes, 14M images. JFT: 18,000 classes, 303M
        images (called "JFT-300M" elsewhere in the same paper, including its
        own abstract).
Owner:  Dosovitskiy et al. 2010.11929, Section 4.1
Scope:  De-duplicated w.r.t. downstream test sets, following Kolesnikov et
        al. 2020 (BiT).

Figure: ViT dominates the compute/accuracy trade-off by "approximately 2-4x
        less compute to attain the same performance (average over 5
        datasets)" versus ResNets (BiT).
Owner:  Dosovitskiy et al. 2010.11929, Section 4.4 (text accompanying
        Figure 5 / Table 6)
Scope:  Controlled scaling study, all models pretrained on JFT-300M so data
        scale is held fixed; compute measured in exaFLOPs.

Figure: ViT-B/16 trained on ImageNet-1k only (no JFT, no ImageNet-21k) —
        77.91% top-1 ImageNet
Owner:  Dosovitskiy et al. 2010.11929, Appendix C, Table 5
Scope:  Fine-tuned at 384px; this is the "modest accuracies... below
        ResNets" result the paper's own introduction describes for
        mid-sized-data training.

Figure: DeiT-B trained on ImageNet-1k only, no distillation — 81.8% (224px)
        / 83.1% (384px fine-tune)
        DeiT-B with hard-label distillation from a RegNetY-16GF teacher —
        83.4% (224px) / 84.5% (384px)
        DeiT-B distilled, 1000-epoch schedule, 384px — 85.2% (best reported)
Owner:  Touvron et al. 2012.12877, Table 3 and Table 5
Scope:  ImageNet-1k only for both training and evaluation; no external
        pretraining data at any point; 86M parameters, architecture
        identical to ViT-B.

Figure: DeiT-B pretraining takes 53 hours on a single 8-GPU (V100) node (or
        37 hours on 2 nodes); an optional 384px fine-tune adds ~20 hours on
        one 8-GPU node (25 epochs).
Owner:  Touvron et al. 2012.12877, Section 6 ("Training time")
Scope:  DeiT-B specifically; DeiT-S/DeiT-Ti trained "in less than 3 days on
        4 GPU."

Figure: ViT-B/16 pretrained on JFT-300M, fine-tuned at 384px — 84.15%
        top-1 ImageNet
Owner:  Dosovitskiy et al. 2010.11929, Table 5 (Appendix C); independently
        cited by Touvron et al. 2012.12877, Section 5.2
Scope:  This is the JFT-300M number DeiT's distilled 85.2% (ImageNet-1k
        only) is compared against and exceeds.

Figure: ResNet-50, unmodified architecture — 76.1% top-1 ImageNet with
        original training recipe; 78.8% (+2.7 points) with the transformer-
        style training recipe (AdamW, 300 epochs, Mixup/CutMix/RandAugment/
        stochastic depth/label smoothing) and no architecture change
Owner:  Liu et al. 2201.03545, Section 2.1
Scope:  Same ResNet-50 weights/architecture in both rows; only the training
        procedure differs. Used by ConvNeXt as its starting baseline before
        any of the subsequent "modernization" architecture steps.

Figure: ConvNeXt-T (fully modernized pure CNN, recipe-modernized ResNet-50
        lineage) — 81.97% top-1 ImageNet-1K, vs. Swin-T (hierarchical ViT
        variant) — 81.30%, at matched ~4.5 GFLOPs
Owner:  Liu et al. 2201.03545, Table 10 (roadmap) and Table 1 (headline
        comparison, reported as 82.1% there with 3-seed averaging
        differences)
Scope:  ImageNet-1K trained from scratch, no external pretraining data;
        Swin-T number is the published Swin Transformer result.

Figure: Isotropic (non-hierarchical) ConvNeXt vs. ViT at matched parameter
        count/FLOPs: S 79.7% vs. 79.8% (22M params); B 82.0% vs. 81.8%
        (87M params); L 82.6% vs. 82.6% (304-306M params)
Owner:  Liu et al. 2201.03545, Table 2
Scope:  ImageNet-1K, 224px; ViT numbers are DeiT's supervised training
        results for ViT-S/B and MAE's for ViT-L (both improved recipes
        over the original ViT paper's own numbers), so recipe is held
        approximately constant across the comparison.

Figure: ConvNeXt-XL pretrained on ImageNet-22K (14M images), fine-tuned at
        384px — 87.8% top-1 ImageNet-1K
Owner:  Liu et al. 2201.03545, Table 1 / Abstract
Scope:  Pretraining set is ImageNet-22K (14M images), not JFT-300M (303M
        images); compare to ViT-H/14's 88.55% on JFT-300M — a near-match at
        roughly 1/20th the pretraining images, not a same-dataset test.

Figure: JFT-300M-pretrained ViT-L/16 and ViT-H/14 outperform ImageNet-only-
        pretrained versions of the same architectures by "a ~30% gap in
        absolute accuracy" on 10-shot linear probes at middle layers
Owner:  Raghu et al. 2108.08810, Section 8, Figure 13 (left panel)
Scope:  10-shot linear probe accuracy on ImageNet, evaluated at each
        transformer block/layer, both models otherwise identical
        architecture.
```

## Source assets

```text
Asset: Figure 3, Dosovitskiy et al. 2010.11929, p.7 — "Transfer to
       ImageNet." A scatter/line plot of ImageNet top-1 accuracy (y-axis)
       against pretraining dataset (x-axis: ImageNet, ImageNet-21k,
       JFT-300M), for ViT-B/32, ViT-B/16, ViT-L/32, ViT-L/16, ViT-H/14, with
       a shaded region marking the range spanned by BiT ResNets of different
       sizes.
Shows: The exact crossover the commission's central claim turns on: BiT
       ResNets beat ViT on the leftmost (ImageNet) point; larger ViT
       variants overtake the ResNet band as the x-axis moves to
       ImageNet-21k and then JFT-300M. The underlying numbers are in
       Appendix Table 5.
Crop:  Must keep all three x-axis categories and the BiT shaded band
       together; cropping to only two categories or dropping the BiT band
       removes the comparison the claim depends on.

Asset: Figure 5, Dosovitskiy et al. 2010.11929, p.7-8 — "Performance versus
       pre-training compute for different architectures." Two log-x scatter
       plots (Average-5 datasets and ImageNet alone) of transfer accuracy
       against total pretraining compute in exaFLOPs, for ViT, ResNet (BiT),
       and hybrid models.
Shows: The compute-vs-accuracy claim: at matched compute, ViT models sit
       above the ResNet (BiT) curve, and hybrids close part of the gap at
       small budgets but the advantage of hybrids over pure ViT vanishes at
       larger sizes. Underlying numbers are in Appendix Table 6.
Crop:  Must keep both panels (Average-5 and ImageNet) and all three series
       (Transformer/ResNet/Hybrid) with the log-x axis intact; a single-panel
       or single-series crop loses the "hybrid gap vanishes at scale" point.

Asset: Table 2, Dosovitskiy et al. 2010.11929, p.6 — "Comparison with state
       of the art on popular image classification benchmarks." Full numeric
       table: ViT-H/14, ViT-L/16 (JFT and ImageNet-21k), BiT-L, Noisy
       Student, across 7 datasets plus TPUv3-core-days.
Shows: The exact accuracy and compute figures the reconstruction's central
       numbers come from, in one place, with the compute column that
       supports the "lower pretraining compute" half of the commission's
       claim.
Crop:  Keep the full table including the TPUv3-core-days row; the row is
       what supports the compute-efficiency half of the claim and is easy
       to drop if only cropping the accuracy rows.

Asset: Table 1, Dosovitskiy et al. 2010.11929, p.5 — "Details of Vision
       Transformer model variants." Layers, hidden size D, MLP size, heads,
       params for ViT-Base/Large/Huge.
Shows: The exact architecture specification needed to reconstruct the model
       sizes and the patch-size notation (ViT-L/16, ViT-H/14, etc.).
Crop:  Small table; keep intact.

Asset: Figure 1 (throughput/accuracy scatter), Touvron et al. 2012.12877,
       p.2. Plots top-1 ImageNet accuracy against images/sec throughput for
       EfficientNet, ViT, DeiT, and distilled DeiT, all trained on
       ImageNet-1k only.
Shows: ViT-B/ViT-L sitting well below the EfficientNet curve when trained
       on ImageNet-1k only (matching the ViT paper's own 77.9%-scale
       result), and DeiT/DeiT-distilled moving onto or above that curve
       with the same architecture and no external data — the visual form of
       the "recipe, not scale" contradiction.
Crop:  Keep both the ViT points and the DeiT/DeiT-distilled curves together
       with the EfficientNet reference curve; dropping the ViT points
       removes the baseline the improvement is measured against.

Asset: Table 5, Touvron et al. 2012.12877, p.12 — full throughput/accuracy
       comparison table across convnets, ViT-B/16, ViT-L/16, and all DeiT
       variants (with and without distillation, with and without 1000-epoch
       schedule).
Shows: Every DeiT accuracy number cited in this record, in one place,
       alongside the ViT-B/16 and ViT-L/16 rows it is compared against.
Crop:  Full table is dense (28 rows); a usable crop should keep the
       "Transformers" section (ViT-B/16, ViT-L/16, all DeiT rows) together
       rather than splitting DeiT from the ViT rows it is benchmarked
       against.

Asset: Figure 1 and Figure 2, Raghu et al. 2108.08810, p.3 — CKA similarity
       heatmaps for ViT-L/16, ViT-H/14, ResNet-50, ResNet-152 (within-model)
       and ViT-vs-ResNet (cross-model).
Shows: The visual basis for "ViT has more uniform representations across
       layers than ResNet" — a grid-like, high-similarity pattern for ViT
       vs. a staged, blockier pattern for ResNet.
Crop:  Keep at least one within-model pair (e.g., ViT-L/16 and R50) plus the
       cross-model panel together; the cross-model panel is what shows how
       many ResNet layers map to how few ViT layers, the paper's own
       headline reading.

Asset: Figure 3 vs. Figure 4, Raghu et al. 2108.08810, p.4 — attention-head
       mean-distance plots for ViT-L/16 and ViT-H/14, JFT-300M-pretrained
       (Fig. 3) vs. ImageNet-only-pretrained (Fig. 4).
Shows: The direct visual evidence for the "scale teaches ViT to attend
       locally" finding: a mix of local and global heads at low layers with
       JFT-300M pretraining, versus uniformly global attention at low
       layers without it.
Crop:  Must show the two figures side by side (or the same model's two
       panels together) — the finding is entirely in the contrast between
       them, not in either alone.

Asset: Figure 13, Raghu et al. 2108.08810, p.9 — linear-probe test accuracy
       by normalized layer number, JFT-300M vs. ImageNet-only pretraining
       (left panel) and ViT vs. ResNet at various sizes (right panel).
Shows: The ~30-point absolute-accuracy gap in intermediate-layer
       representation quality between JFT-300M and ImageNet-only
       pretraining for the larger ViT models — the clearest single figure
       for "scale changes what the model represents, not just its final
       score."
Crop:  Left panel alone suffices for the data-scale point; keep both ViT-L/16
       and ViT-H/14 curves in both pretraining conditions.

Asset: Figure 2 ("roadmap" bar chart) and Table 10, Liu et al. 2201.03545,
       p.3 and p.11. Sequential bar chart / table walking ResNet-50 through
       each design change (training recipe, macro design, ResNeXt-ify,
       inverted bottleneck, large kernel, micro design) to ConvNeXt-T,
       compared against Swin-T.
Shows: The step-by-step accounting of how much each change contributes,
       with the training-recipe-only step (76.1% -> 78.8%) isolated from
       every subsequent architecture change — the cleanest available
       "recipe alone" measurement in the after-record.
Crop:  Keep the first two rows (original recipe, enhanced recipe) together
       with the final ConvNeXt-T/Swin-T comparison; cropping to only the
       final bars loses the recipe-only step that is the sharpest evidence.

Asset: Table 1, Liu et al. 2201.03545, p.7. Full ImageNet-1K and
       ImageNet-22K-pretrained classification comparison across ConvNeXt,
       Swin, DeiT, RegNet, EfficientNet, EfficientNetV2, and ViT-B/16,
       ViT-L/16 (AugReg-trained).
Shows: ConvNeXt vs. Swin and vs. ViT-B/16, ViT-L/16 at matched or
       comparable scale, including the 87.8% ConvNeXt-XL/ImageNet-22K
       headline result to set against ViT-H/14's 88.55%/JFT-300M.
Crop:  Full table is long; a usable crop should keep the ImageNet-22K
       section intact (it contains the ViT-B/16, ViT-L/16, and ConvNeXt-XL
       rows together) rather than only the ImageNet-1K section.

Asset: Table 2, Liu et al. 2201.03545, p.7 — "Comparing isotropic ConvNeXt
       and ViT." Small table: ViT-S/B/L vs. isotropic ConvNeXt-S/B/L at
       matched params/FLOPs.
Shows: The single cleanest number for the architecture-vs-recipe question:
       with non-hierarchical shape, parameter count, and training recipe
       all held fixed, self-attention (ViT) and depthwise convolution
       (ConvNeXt-iso) land within 0.2 points of each other at every size
       tested.
Crop:  Small table (6 rows); keep intact.
```

## Discarded

None. All four documents named in the brief were opened, read to the end
including appendices, and used; no source was abandoned partway. The one
transport wrinkle worth recording: `arXiv.org`'s WebFetch-rendered text
extraction failed on all four PDFs (returned raw PDF stream data instead of
text), so each PDF was instead downloaded and read directly as a PDF
document; the `arxiv.org/abs/...` page for each paper was separately
confirmed reachable and matching (title, authors, abstract) and is the URL
recorded above as the source's own page, not the `/pdf/` fetch route.
