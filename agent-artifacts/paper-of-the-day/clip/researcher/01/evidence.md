# Evidence record: paper-of-the-day/clip (01)

The evidence supports every load-bearing claim in the commission. The CLIP paper
(Radford et al., 2021) is the primary owner of the contrastive objective, the
zero-shot construction, the exact ImageNet numbers, and the effective-robustness
result, and all of these are verified against the paper's own method section,
Figure 1, Figure 3, Section 3.1, and Section 3.3. The follow-on that isolates the
training-data distribution as the cause of the robustness (Fang et al., 2022) is
verified against its own abstract and experimental design, and it sits inside a
coherent body of work from the same research lineage (Taori et al., 2020; Nguyen
et al., 2022; Cherti et al., 2023) that agrees with it. The record is thin in one
respect the writer must handle carefully: the CLIP paper did **not** claim the
language objective caused the robustness. It explicitly named the large, diverse
pre-training dataset as a candidate explanation and declined to settle the
question. So the after-record refined an open question the paper posed, not a
wrong answer it asserted. The other honest limitation is that the follow-on
isolating data traces largely to one research group (Ludwig Schmidt and
collaborators); it is peer-reviewed and controlled, but not yet independently
reproduced by an unrelated lab, and I found no source that overturns it.

## Sources

```text
URL:         https://arxiv.org/abs/2103.00020
Kind:        primary. Radford et al. author the objective, the models, and every
             CLIP number; they own these claims firsthand.
Establishes: The contrastive objective and its exact form; the zero-shot
             classifier construction; prompt engineering/ensembling; the zero-shot
             ImageNet result; the effective-robustness result and the paper's own
             (hedged) reading of it; the documented model biases.
Paraphrase:  CLIP jointly trains an image encoder and a text encoder on 400M
             web (image, text) pairs to predict which caption goes with which
             image in a batch, using a symmetric cross-entropy loss over scaled
             cosine similarities with a learned temperature. At test time the text
             encoder turns class names into a linear classifier, giving zero-shot
             transfer. Best CLIP (ViT-L/14@336px) reaches 76.2% top-1 zero-shot on
             ImageNet, matching the original ResNet-50 with none of its 1.28M
             labeled examples, and is far more robust to natural distribution
             shift than standard ImageNet models.
Locators:    Abstract; Fig. 1 (p.3, "Summary of our approach"); Sec. 2.3
             (objective) and Fig. 3 (pseudocode, p.5); Sec. 3.1.2 (zero-shot
             construction); Sec. 3.1.3 (Table 1, ImageNet result); Sec. 3.1.4
             (Fig. 4, prompt engineering); Sec. 3.3 and Fig. 13 (robustness);
             Sec. 7.1 and Tables 6-7 (bias).
Quote:       "We optimize a symmetric cross entropy loss over these similarity
             scores." (Sec. 2.3)
             "the temperature parameter which controls the range of the logits in
             the softmax, tau, is directly optimized during training as a
             log-parameterized multiplicative scalar" (Sec. 2.3)
             "While these results show that zero-shot models can be much more
             robust, they do not necessarily mean that supervised learning on
             ImageNet causes a robustness gap. Other details of CLIP, such as its
             large and diverse pre-training dataset or use of natural language
             supervision could also result in much more robust models regardless
             of whether they are zero-shot or fine-tuned." (Sec. 3.3)
```

```text
URL:         https://github.com/openai/CLIP
Kind:        primary. The official OpenAI code and pre-trained weights released
             with the paper; the artifact itself, not a report on it.
Establishes: That the paper shipped runnable code and weights (the loss and the
             encoders as implemented). Supports "we release our code and
             pre-trained model weights" in the abstract.
Paraphrase:  Official OpenAI CLIP repository. Provides pre-trained weights loaded
             via clip.load(), the model/loss implementation under /clip, and
             encode_image / encode_text / tokenize utilities. MIT licensed.
Locators:    Repository root README.
Quote:       (none needed)
```

```text
URL:         https://arxiv.org/abs/2205.01397
Kind:        primary for its own finding. Fang et al. own the controlled
             experiment that isolates the cause of the robustness. It is a
             secondary commentary on CLIP but a primary source for "data
             determines robustness."
Establishes: That among five candidate causes of CLIP's robustness -- training
             set size, training distribution, language supervision at training
             time, language supervision at test time, and the contrastive loss --
             the diverse training distribution is the main cause and the other
             four contribute little to none. Introduces ImageNet-Captions to run
             the controlled comparison.
Paraphrase:  The authors hold the objective and supervision fixed and vary the
             data, and vary the objective/supervision on fixed data. CLIP trained
             on ImageNet-Captions (ImageNet images with their original Flickr
             captions) does not become robust, and standard classifiers trained on
             CLIP's data do gain robustness, so language supervision and the
             contrastive loss are not what confer it. The distribution of the
             pre-training data is.
Locators:    Abstract; the ImageNet-Captions construction and the five-cause
             ablation in the body.
Quote:       "Our experiments show that the more diverse training distribution is
             the main cause for the robustness gains, with the other factors
             contributing little to no robustness."
```

```text
URL:         https://arxiv.org/abs/2007.00644
Kind:        primary for the effective-robustness framework. Taori et al. own the
             definition and the measurement testbed CLIP's Section 3.3 builds on.
Establishes: The definition of effective robustness (accuracy under distribution
             shift above what in-distribution accuracy predicts) versus relative
             robustness (any OOD gain); the 7 natural-shift testbed; and, already
             in 2020, that training on larger and more diverse data was the main
             lever that moved effective robustness while synthetic-shift
             robustness did not transfer.
Paraphrase:  Across 204 ImageNet models in 213 test conditions, robustness to
             synthetic perturbations did not transfer to natural distribution
             shift, and almost no existing technique helped. The one exception
             they found was training on larger, more diverse datasets. This is the
             framework CLIP adopts, and it foreshadows the data explanation before
             CLIP was published.
Locators:    Abstract; effective/relative robustness definitions in the body.
Quote:       "The main exception is training on larger and more diverse datasets,
             which in multiple cases increases robustness, but is still far from
             closing the performance gaps."
```

```text
URL:         https://arxiv.org/abs/2208.05516
Kind:        primary for its own finding (Nguyen et al., 2022). Refines the data
             explanation.
Establishes: That it is the specific composition of the pre-training source, not
             raw diversity or quantity, that determines robustness. No single
             source dominates across all shifts, and mixing sources can dilute the
             robustness of the best individual source rather than improve on it.
Paraphrase:  Using a testbed of six public sources (YFCC, LAION, Conceptual
             Captions, WIT, RedCaps, Shutterstock), the authors show CLIP's
             robustness varies substantially by which data it was trained on, and
             naively combining sources does not help and often hurts. This
             sharpens Fang: "the right distribution," not "more data."
Locators:    Abstract; the six-source testbed and mixing experiments.
Quote:       "we find that the performance of the pre-training data varies
             substantially across distribution shifts ... mixing multiple sources
             does not necessarily yield better models, but rather dilutes the
             robustness of the best individual data source." (as reported in the
             abstract)
```

```text
URL:         https://arxiv.org/abs/2212.07143
Kind:        primary for its own finding (Cherti et al., 2023) and a reproduction
             of CLIP on open data via OpenCLIP.
Establishes: That OpenAI CLIP (trained on WIT) and OpenCLIP (trained on LAION)
             show different downstream scaling despite identical architectures and
             similar recipes, so the training data source, not the objective or
             architecture, shapes what the model does. This is the open
             reproduction the commission asks for.
Paraphrase:  Training CLIP-style models on up to two billion LAION pairs yields
             power-law scaling on zero-shot classification, retrieval, and linear
             probing, but the scaling exponents differ between the OpenAI-data and
             LAION-data models. Same math, different data, different behavior.
Locators:    Abstract; scaling-law results per task.
Quote:       "the training distribution plays a key role in scaling laws as the
             OpenAI and OpenCLIP models exhibit different scaling behavior despite
             identical model architectures and similar training recipes."
```

```text
URL:         https://arxiv.org/abs/2402.07410
Kind:        secondary on CLIP, primary for its own audit (Tu, Deng, Gedeon;
             NeurIPS 2023). Complicates the reliability story.
Establishes: That training-source design strongly shapes CLIP's safety-related
             properties (a second confirmation that data drives behavior), while
             also showing CLIP models are not consistently better-calibrated than
             ImageNet classifiers, contradicting some prior claims. Useful as the
             place the follow-on complicates a clean "CLIP is simply more
             reliable" reading.
Paraphrase:  A comprehensive evaluation of 83 CLIP models and 127 ImageNet
             classifiers across visual-factor resilience, calibration, and anomaly
             detection. Training source has a profound influence on all three;
             CLIP's calibration advantage does not hold up.
Locators:    Abstract; the three-property evaluation.
Quote:       (paraphrase sufficient)
```

```text
URL:         https://arxiv.org/abs/2110.01963
Kind:        primary for its own audit (Birhane, Prabhu, Kahembwe, 2021). Serves
             the data-curation criticism the commission names.
Establishes: That the uncurated web-scale data that gives these models their
             robustness also carries serious harm. Their audit of LAION-400M -- a
             dataset built by parsing Common Crawl image-alt-text pairs and
             filtering them with CLIP itself -- documents pornographic, misogynist,
             racist, and stereotyping content, and argues automated filtering
             (including CLIP's) does not remove it.
Paraphrase:  The same property Fang credits for robustness (broad, uncurated web
             diversity) is the property that lets harmful content through. LAION
             was CLIP-filtered, so CLIP is implicated in the curation, not just a
             beneficiary of the data. The robustness dividend and the harm share
             one root.
Locators:    Abstract; the LAION-400M content audit.
Quote:       "We found that the dataset contains, troublesome and explicit images
             and text pairs of rape, pornography, malign stereotypes, racist and
             ethnic slurs, and other extremely problematic content."
```

## Contradictions

- **The paper's reading versus the after-record -- but not a flat contradiction.**
  CLIP reads its robustness as a benefit of natural-language supervision and
  zero-shot evaluation (Sec. 3.3 intro: a zero-shot model "should not be able to
  exploit spurious correlations ... since it is not trained on that
  distribution"). Fang et al. (2022) show the cause is the data, not the objective
  or the zero-shot protocol. The two do **not** contradict as sharply as the angle
  might want: the CLIP paper explicitly hedged in the same section, naming "its
  large and diverse pre-training dataset" as a candidate cause and writing that
  its results "do not necessarily mean that supervised learning on ImageNet causes
  a robustness gap." The writer must not stage the follow-on as overturning a
  claim CLIP asserted. CLIP posed the question and leaned toward the
  zero-shot/language reading in its intuition; the follow-on answered it against
  that lean. Letting the later critique read as something CLIP conceded, or as
  refuting a confident CLIP claim, would misstate the record.

- **CLIP's own adaptation experiment already cut against the zero-shot reading.**
  Adapting CLIP to ImageNet with an L2-regularized logistic-regression classifier
  raised ImageNet accuracy by 9.2% to 85.4% but did not improve average accuracy
  under distribution shift (it slightly decreased), and per-dataset it fell 4.7%
  on ImageNet-R, 3.8% on ObjectNet, 2.8% on ImageNet Sketch, 1.9% on ImageNet-A
  (Sec. 3.3, Fig. 14). CLIP wrote "We do not have confident answers to these
  questions at this time." So the paper itself supplied evidence that the zero-shot
  protocol was doing less than the intuition suggested.

- **"More data" is too coarse.** Nguyen et al. (2022) show mixing sources can
  dilute robustness, so the correct statement is that the training distribution
  (which source), not sheer size or diversity, determines it. A writer who
  compresses the finding to "CLIP is robust because it trained on more data" will
  overstate what Fang and Nguyen established.

- **The robustness dividend and the data harm share a root.** Fang credits the
  broad, uncurated web distribution for the robustness. Birhane et al. (2021) audit
  LAION-400M -- built from Common Crawl and filtered with CLIP itself -- and find
  pornographic, misogynist, and racist content that automated filtering did not
  remove. This is not a contradiction of the robustness finding; it is its cost.
  A writer crediting "diverse web data" for the robustness should not do so as if
  diversity were free. CLIP's own Sec. 7.1 bias results point the same way from
  inside the paper.

- **Provenance caveat, not a contradiction.** Taori (2020), Fang (2022), Nguyen
  (2022), and Cherti (2023) share authors and a single research lineage. The
  finding is peer-reviewed and rests on controlled experiments, and I found no
  source disputing it, but it is not yet independently reproduced by an unrelated
  group. State the finding as well-supported, and do not dress one lab's coherent
  program as a broad multi-lab consensus.

## Numbers

```text
Figure: 400 million (image, text) pairs (the WIT training set)
Owner:  Radford et al. 2021, Abstract / Sec. 2.2
Scope:  Total pre-training pairs collected from the internet.
```

```text
Figure: N = 32,768 (minibatch size)
Owner:  Radford et al. 2021, Sec. 2.5
Scope:  Batch size for the contrastive loss; the classifier over each batch has N
        classes, with N real pairs and N^2 - N incorrect pairings.
```

```text
Figure: temperature tau initialized to the equivalent of 0.07; logit scaling
        clipped at a maximum of 100
Owner:  Radford et al. 2021, Sec. 2.5
Scope:  The learned temperature is a log-parameterized multiplicative scalar
        (implemented as np.exp(t) in Fig. 3), directly optimized, clipped to
        prevent training instability.
```

```text
Figure: 76.2% zero-shot top-1 on ImageNet (95% top-5)
Owner:  Radford et al. 2021, Sec. 3.1.3, Table 1
Scope:  Best model, ViT-L/14@336px, zero-shot, ImageNet validation, 1000 classes.
        Matches the original ResNet-50; up from Visual N-Grams' 11.5%.
```

```text
Figure: prompt gains -- single "A photo of a {label}." prompt: +1.3% on ImageNet;
        80-prompt ensemble: +3.5% over the single default; together ~5%
Owner:  Radford et al. 2021, Sec. 3.1.4, Fig. 4
Scope:  ImageNet for the +1.3% and +3.5%; Fig. 4 reports ~5 points on average
        across 36 datasets for prompt engineering + ensembling combined, a gain
        comparable to 4x more compute on the contextless baseline.
```

```text
Figure: robustness gap reduced by up to 75%
Owner:  Radford et al. 2021, Sec. 3.3, Fig. 13
Scope:  Zero-shot CLIP vs. standard ImageNet models, averaged over the 7 natural
        distribution-shift datasets; "up to 75%" is the maximum gap reduction.
```

```text
Figure: ResNet-101 makes 5x as many mistakes on natural shifts as on ImageNet val
Owner:  Radford et al. 2021, Sec. 3.3
Scope:  A same-ImageNet-accuracy baseline; motivates the effective-robustness gap.
```

```text
Figure: adaptation trade-off -- +9.2% ImageNet (to 85.4%), avg shift accuracy
        slightly down; per-dataset -4.7% ImageNet-R, -3.8% ObjectNet, -2.8%
        ImageNet Sketch, -1.9% ImageNet-A
Owner:  Radford et al. 2021, Sec. 3.3, Fig. 14
Scope:  L2-regularized logistic regression on CLIP features fit to ImageNet
        training set, vs. the zero-shot classifier. Only ImageNetV2 improved
        meaningfully.
```

```text
Figure: banana-class illustration (Fig. 13 right), ResNet-101 vs zero-shot CLIP
        (ViT-L/14@336px): ImageNet 76.2 / 76.2; ImageNetV2 64.3 / 70.1 (+5.8);
        ImageNet-A 2.7 / 77.1 (+74.4); ImageNet-R 37.7 / 88.9 (+51.2);
        ObjectNet 32.6 / 72.3 (+39.7); ImageNet Sketch 25.2 / 60.2 (+35.0)
Owner:  Radford et al. 2021, Fig. 13 (right panel)
Scope:  Per-class accuracy for "banana," a class shared across 5 of the 7 shift
        datasets, chosen as a visualization. These are illustrative single-class
        figures, NOT the averaged headline result; do not present them as the
        overall robustness numbers.
```

```text
Figure: bias probe -- Black faces classified into a "non-human" category at 14.4%
        vs <=7.6% for every other race group; a "child" label added to the set
        drops young-face misclassification into crime/non-human categories from
        ~30-35% (ages 0-9) to ~2-4%
Owner:  Radford et al. 2021, Sec. 7.1, Tables 6-7
Scope:  Zero-shot CLIP on FairFace images with a label set augmented with 3
        crime-related and 4 non-human categories. Per-cell numbers were read from
        a PDF table extraction; the writer should confirm exact cells against
        Tables 6-7 before quoting any single figure. The robust, safe claim is the
        Black/non-human disparity and the label-set sensitivity, both stated by
        the authors.
```

```text
Figure: five candidate causes ablated; diverse training distribution is the cause
Owner:  Fang et al. 2022, Abstract and body
Scope:  (i) training set size, (ii) training distribution, (iii) language
        supervision at train time, (iv) language supervision at test time,
        (v) contrastive loss. Only (ii) drives robustness.
```

```text
Figure: 204 ImageNet models, 213 test conditions
Owner:  Taori et al. 2020, Abstract
Scope:  The effective-robustness testbed; synthetic-shift robustness did not
        transfer to natural shift; more diverse data was the main exception.
```

## The contrastive objective, for the writer to set as an equation

The paper's own Figure 3 pseudocode (Sec. 2.3, "Numpy-like pseudocode for the
core of an implementation of CLIP"), transcribed verbatim from the source:

```text
# image_encoder - ResNet or Vision Transformer
# text_encoder  - CBOW or Text Transformer
# I[n, h, w, c] - minibatch of aligned images
# T[n, l]       - minibatch of aligned texts
# W_i[d_i, d_e] - learned proj of image to embed
# W_t[d_t, d_e] - learned proj of text to embed
# t             - learned temperature parameter

# extract feature representations of each modality
I_f = image_encoder(I) #[n, d_i]
T_f = text_encoder(T)  #[n, d_t]

# joint multimodal embedding [n, d_e]
I_e = l2_normalize(np.dot(I_f, W_i), axis=1)
T_e = l2_normalize(np.dot(T_f, W_t), axis=1)

# scaled pairwise cosine similarities [n, n]
logits = np.dot(I_e, T_e.T) * np.exp(t)

# symmetric loss function
labels = np.arange(n)
loss_i = cross_entropy_loss(logits, labels, axis=0)
loss_t = cross_entropy_loss(logits, labels, axis=1)
loss   = (loss_i + loss_t)/2
```

In the paper's notation, for a batch of N pairs: the image encoder produces
features I_f, the text encoder produces T_f, each is linearly projected (W_i, W_t)
and L2-normalized into the shared embedding space to give unit vectors I_e, T_e.
The logit matrix is the N x N matrix of pairwise cosine similarities scaled by the
exponentiated learned temperature, logits = (I_e . T_e^T) * exp(t). The correct
pairings are the diagonal (labels = arange(N)). The loss is the average of two
cross-entropies over that matrix: one normalizing over images for each text
(axis 0) and one normalizing over texts for each image (axis 1). This is the
symmetric InfoNCE / multi-class N-pair form. The paper attributes the batch
construction to Sohn (2016) (N-pair loss), Oord et al. (2018) (InfoNCE), and Zhang
et al. (2020) (text-image, medical). Suitable single-equation form for nb-math,
letting s(i,j) be the scaled cosine logit between image i and text j and t the
learned temperature:

  L = -(1/2N) * sum_i [ log( exp(s(i,i)) / sum_j exp(s(i,j)) )
                       + log( exp(s(i,i)) / sum_j exp(s(j,i)) ) ]

## Zero-shot classifier construction, for the writer

From Sec. 3.1.2, verbatim mechanism: "we first compute the feature embedding of
the image and the feature embedding of the set of possible texts by their
respective encoders. The cosine similarity of these embeddings is then calculated,
scaled by a temperature parameter tau, and normalized into a probability
distribution via a softmax." The paper frames this as "a multinomial logistic
regression classifier with L2-normalized inputs, L2-normalized weights, no bias,
and temperature scaling," where the text encoder acts as "a hypernetwork ... which
generates the weights of a linear classifier based on the text specifying the
visual concepts." Each class name is wrapped in a prompt (default "A photo of a
{label}.") and embedded; the embeddings become the classifier's weight vectors.

## Source assets

```text
Asset: Figure 1, "Summary of our approach" (p.3). Three panels: (1) Contrastive
       pre-training -- the N x N image-text similarity matrix with the diagonal as
       the positives; (2) Create dataset classifier from label text -- class names
       in the "A photo of a {object}." template through the text encoder; (3) Use
       for zero-shot prediction -- one image against all class-text embeddings.
Shows: The whole mechanism the article rebuilds: how the objective trains the two
       encoders and how, at test time, label text becomes a classifier. This is
       THE method figure the commission asks for.
Crop:  Keep all three numbered panels and their labels; the argument is that (1)
       and (2)-(3) are the same similarity operation reused. Do not crop to a
       single panel. The "Pepper the aussie pup" caption text may be trimmed; the
       matrix, the encoders, and the prompt template must stay.
```

```text
Asset: Figure 3, "Numpy-like pseudocode for the core of an implementation of CLIP"
       (p.5). The ~15-line pseudocode transcribed above.
Shows: The exact objective -- projection, L2-normalize, scaled cosine logits,
       symmetric cross-entropy. The commission wants the math SET (nb-math), so
       the writer should render the equation rather than reproduce the code image;
       the pseudocode is the source of record to derive it from.
Crop:  n/a -- prefer the typeset equation over a figure crop. If any code is shown,
       it must keep the exp(t) temperature scaling and both axis-0 and axis-1
       cross-entropies (the symmetry is the point).
```

```text
Asset: Figure 13, "Zero-shot CLIP is much more robust to distribution shift than
       standard ImageNet models" (p.15). Left panel: OOD accuracy (avg over 7
       shifts) vs. ImageNet accuracy, with the y=x ideal-robustness line, the
       standard-ImageNet trend, and zero-shot CLIP sitting well above it. Right
       panel: the "banana" per-class visualization comparing ResNet-101 with
       zero-shot CLIP across five shift datasets.
Shows: The effective-robustness claim itself -- CLIP closing the gap that standard
       models leave open. This is THE robustness plot the commission asks for.
Crop:  The LEFT panel is the load-bearing one; keep the y=x line, the fitted
       standard-ImageNet band, and the zero-shot CLIP points, or the "gap" is
       invisible. If the right (banana) panel is included, caption it as a
       single-class illustration so its dramatic +74.4% / +51.2% deltas are not
       mistaken for the averaged result.
```

```text
Asset: Figure 14 (p.15), the per-dataset change from zero-shot when CLIP is
       adapted to ImageNet by logistic regression.
Shows: That fitting ImageNet raises ImageNet/ImageNetV2 accuracy but costs
       accuracy on ImageNet-R, ObjectNet, Sketch, and ImageNet-A -- the paper's
       own evidence complicating the zero-shot reading. Optional but strong
       support for the contradiction section.
Crop:  Keep the per-dataset signed bars and the zero baseline.
```

## Discarded

```text
URL: https://arxiv.org/pdf/2103.00020 : same paper as the abs page; the PDF is the
     transport, the abs page is the source's own address. Text was read from a
     locally decoded copy of this PDF; recorded canonical URL is the abs page.
URL: https://ar5iv.labs.arxiv.org/html/2103.00020 : a rehosted HTML rendering of
     the CLIP paper, used only to cross-check figures; not an independent source
     and not the paper's own address. The abs page is recorded instead.
URL: https://proceedings.mlr.press/v162/fang22a.html : the ICML/PMLR page for Fang
     et al.; same content as the arXiv abs. Kept arXiv as the stable primary; this
     is the peer-reviewed venue of record if the editor prefers it.
URL: https://proceedings.neurips.cc/paper/2020/hash/d8330f857a17c53d217014ee776bfd50-Abstract.html
     : NeurIPS page for Taori et al.; duplicate of the arXiv source.
URL: https://liner.com/review/... and semanticscholar / emergentmind summary pages
     : third-party summaries, secondary retellings with no authorship stake; not
     cited.
```
