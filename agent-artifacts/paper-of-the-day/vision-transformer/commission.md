# Commission: paper-of-the-day/vision-transformer

## Subject

Dosovitskiy et al., "An Image Is Worth 16×16 Words: Transformers for Image
Recognition at Scale" (ICLR 2021; arXiv:2010.11929). The central claim to
rebuild: a pure transformer applied to sequences of image patches, with no
convolutional inductive bias, matches or beats the best convolutional networks
on image classification once it is pretrained on enough data, and it does so at
lower pretraining compute. The claim the reconstruction turns on is the
data-scale crossover: ViT trails CNNs when trained on ImageNet-sized data and
overtakes them only after pretraining on the larger JFT-300M.

## Why this paper, now

An open beat, ML-core. The paper reset computer vision onto the transformer and
has the public afterlife the series prizes: a documented record of replication,
criticism, and follow-on that lets the article weigh the claim against what
happened next. That record is the point of the piece, not a coda.

## Angle and boundaries

Rebuild the argument with the paper's own artifacts. Set the patch-embedding and
the standard transformer encoder in real notation rather than paraphrasing them,
and bring in the paper's own figures where the claim turns on them: the accuracy
crossover as pretraining data grows, and the compute-versus-accuracy comparison
with the ResNet (BiT) baselines. Then weigh the claim against the after-record
the researcher verifies: DeiT (Touvron et al. 2021), which reached strong ViT
accuracy trained on ImageNet alone with distillation, undercutting the reading
that only web-scale data can train a ViT; the "do vision transformers see like
convolutional neural networks" analysis (Raghu et al. 2021); and ConvNeXt (Liu
et al. 2022), a modernized pure-CNN that matched ViT-style models, which bears on
whether the transformer architecture or the training recipe and scale did the
work. Land a reviewer's verdict on what the paper established and what the
follow-on reassigned. Steelman the reading the after-record complicates before
weighing it.

## Template and floors

- Template: `paper` (abstract card and link anchored first; flexible sections
  carry the reconstruction and verdict; word band 1800-3400).
- Sources floor: 8. The paper itself is primary for its own claims; each
  after-record paper is primary for its own result. Figures brought in as source
  assets must come from the cited primary via `nb asset`.

## Habits not to inherit

Recent paper pieces (mixture-of-experts, PPO) both open on a
problem-motivation section ("The bill X promised to cut" / "One careless update
can destroy a policy"), run a math-derivation middle, and close on an
nb-holdsup "what the field kept / what survives" section plus an nb-note-strong
verdict. The math middle and figures are appropriate here, but do not build the
opener or the closer on those molds. Vary section headings from those pieces.

## Neighboring articles this run

The library already covers "Attention Is All You Need" (2026-07-27), which frames
transformers on the NLP side and names the state-space counter-case; this piece
takes the architecture into vision and must not reconstruct the NLP transformer
again or reuse that piece's framing. No other article this run touches the
subject.

## Production record

- writing-coach: model sonnet, effort low.
- researcher: model sonnet, effort high.
- writer: model sonnet, effort medium.
- editor: session model (inherit), effort high, required.
