# researcher brief: paper-of-the-day/vision-transformer (01)

Inputs:
- editorial-direction.md (citation standard, series territory, declared reader)
  — at the artifact root
- commission.md (the paper, the claim to rebuild, the after-record to weigh it
  against) — at the artifact root

Output: researcher/01/evidence.md

Focus: read the Vision Transformer paper itself (arXiv:2010.11929) in full,
including appendices. Establish the architecture precisely enough to reconstruct
it: patch size and count, the linear patch embedding, the class token and
position embeddings, the standard transformer encoder, and the model sizes
(ViT-B/L/H and the patch variants). Establish the central results with exact
numbers and the datasets they were trained on: the ImageNet accuracies, the
JFT-300M pretraining crossover versus ImageNet-21k and ImageNet-1k, the
compute-versus-accuracy comparison against BiT/ResNet baselines, and the
data-scale figure the crossover claim turns on. Identify the exact figures and
tables that carry the claim, so the writer can bring them in as source assets via
nb asset (name the figure numbers and what each shows). Then read and verify the
after-record: DeiT (Touvron et al. 2021, arXiv:2012.12877) and what accuracy it
reached training on ImageNet alone with distillation; "Do Vision Transformers See
Like Convolutional Neural Networks?" (Raghu et al. 2021, arXiv:2108.08810); and
ConvNeXt (Liu et al. 2022, arXiv:2201.03545) and what it showed about a modernized
pure-CNN versus ViT-style models. For each, record the exact result that bears on
whether the transformer architecture or the training recipe and data scale did the
work. Search for what breaks the commission's reading and record it. Verify every
number against the owning paper.
