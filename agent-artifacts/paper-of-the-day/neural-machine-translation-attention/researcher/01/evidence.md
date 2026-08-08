# Evidence record: paper-of-the-day/neural-machine-translation-attention (01)

The evidence supports the full commissioned reconstruction. The focal paper
(Bahdanau, Cho, Bengio, arXiv:1409.0473, ICLR 2015) owns, in its own text and
tables, every element the article turns on: the additive alignment score
`e_ij = v_a^T tanh(W_a s_{i-1} + U_a h_j)` (Appendix A.1.2), the context vector
`c_i = sum_j alpha_ij h_j` and softmax weights `alpha_ij` (Section 3.1,
Eqs 4-6), the bidirectional encoder (Section 3.2), the BLEU-vs-length curve
(Fig. 2), and the alignment-matrix visualization with the documented
adjective-noun reordering (Fig. 3, French `[European Economic Area]` ->
`[zone economique europeenne]`). All Table 1 BLEU figures are verified against
the paper's own table. The after-record is solid and two-sided: attention
became the whole of the Transformer (Vaswani et al. 2017), and the explanation
dispute is a genuine, still-live disagreement between Jain & Wallace (2019) and
Wiegreffe & Pinter (2019) whose crux (per-instance vs. model-consistent
adversary, and whether "explanation" is defined before it is tested) is
recorded below in Contradictions.

Where the record is thin: the focal paper studies only English->French WMT'14,
one language pair and one architecture (RNN encoder-decoder), so its
generalization claim is narrow by construction; and the explanation debate was
conducted on later BiLSTM-attention *classification/QA* models, not on
Bahdanau's translation model itself, so importing it onto the 2015 paper is an
analytic bridge the writer must make explicitly, not a finding the debate's
authors state about Bahdanau. The two figures are described here for capture;
they must be rendered from the primary PDF via `nb asset` (I did not capture
images).

## Sources

```text
URL:         https://arxiv.org/abs/1409.0473
Kind:        primary. Bahdanau, Cho, and Bengio author the model, the
             experiments, and the figures; they own every claim the article
             rebuilds.
Establishes: The attention/alignment mechanism firsthand: the additive score,
             context vector, softmax alignment weights, bidirectional encoder,
             the BLEU results (Table 1), the BLEU-vs-length behavior (Fig. 2),
             and the alignment-matrix reading (Fig. 3).
Paraphrase:  A fixed-length context vector is a bottleneck in the basic
             encoder-decoder. The model instead computes, at each output step
             i, a context vector c_i as a weighted sum of encoder annotations,
             with weights produced by a small feedforward alignment network
             trained jointly end to end. Soft alignment lets the gradient flow
             through the alignment decision (no latent alignment variable). On
             English->French it reaches performance comparable to a
             phrase-based system and stays robust on long sentences where the
             fixed-vector model degrades.
Locators:    Abstract; Sec. 3.1 (decoder, Eqs 4-6); Sec. 3.2 (BiRNN encoder);
             Sec. 5.1 + Table 1 (quantitative results); Fig. 2 (Sec. 4/5.1);
             Sec. 5.2 "Qualitative Analysis" + Fig. 3; Appendix A.1.2
             (alignment model), Appendix A.2.3 (model size).
Quote:       Abstract (verbatim, for the paper card): "Neural machine
             translation is a recently proposed approach to machine
             translation. Unlike the traditional statistical machine
             translation, the neural machine translation aims at building a
             single neural network that can be jointly tuned to maximize the
             translation performance. The models proposed recently for neural
             machine translation often belong to a family of encoder-decoders
             and consists of an encoder that encodes a source sentence into a
             fixed-length vector from which a decoder generates a translation.
             In this paper, we conjecture that the use of a fixed-length vector
             is a bottleneck in improving the performance of this basic
             encoder-decoder architecture, and propose to extend this by
             allowing a model to automatically (soft-)search for parts of a
             source sentence that are relevant to predicting a target word,
             without having to form these parts as a hard segment explicitly.
             With this new approach, we achieve a translation performance
             comparable to the existing state-of-the-art phrase-based system on
             the task of English-to-French translation. Furthermore,
             qualitative analysis reveals that the (soft-)alignments found by
             the model agree well with our intuition."
             Alignment parametrization (Sec. 3.1): "We parametrize the
             alignment model a as a feedforward neural network which is jointly
             trained with all the other components of the proposed system."
             Encoder annotation (Sec. 3.2): the annotation of word x_j is the
             concatenation of forward and backward hidden states,
             h_j = [h_forward_j ; h_backward_j], so it summarizes the words
             around x_j.
```

Model equations, as they appear (verbatim shape, with honest locators):

- Sec. 3.1, Eq (4): `p(y_i | y_1,...,y_{i-1}, x) = g(y_{i-1}, s_i, c_i)`
- Sec. 3.1 (stated just after Eq 4): `s_i = f(s_{i-1}, y_{i-1}, c_i)`
  (decoder RNN hidden state at step i)
- Sec. 3.1, Eq (5): `c_i = sum_{j=1}^{T_x} alpha_ij h_j`
- Sec. 3.1, Eq (6): `alpha_ij = exp(e_ij) / sum_{k=1}^{T_x} exp(e_ik)`
- Sec. 3.1 (defined immediately below Eq 6): `e_ij = a(s_{i-1}, h_j)`, the
  alignment model scoring how well inputs around position j match output i.
- Appendix A.1.2 (explicit additive form):
  `e_ij = v_a^T tanh(W_a s_{i-1} + U_a h_j)`
  with `v_a in R^{n'}`, `W_a in R^{n' x n}`, `U_a in R^{n' x 2n}`. Because
  `U_a h_j` does not depend on i, it is pre-computed to reduce cost.
- Appendix A.2.3 (model size for the main model): `n = 1000` hidden units
  (encoder each direction and decoder), `n' = 1000` alignment hidden units,
  `m = 620` word-embedding dimension, `l = 500` maxout hidden layer.

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary (for its own claim). Vaswani et al. author the Transformer;
             they own the claim that attention alone suffices. Secondary as
             evidence *about Bahdanau* (it reports the downstream fate of the
             mechanism, does not own Bahdanau's claims).
Establishes: That the content-based attention Bahdanau introduced became the
             sole computational primitive of the architecture that replaced the
             RNN encoder-decoder.
Paraphrase:  The Transformer is "based solely on attention mechanisms,
             dispensing with recurrence and convolutions entirely," and is
             faster to train and higher-quality on WMT'14 En-De and En-Fr.
Locators:    Abstract; NeurIPS 2017.
Quote:       "We propose a new simple network architecture, the Transformer,
             based solely on attention mechanisms, dispensing with recurrence
             and convolutions entirely."
```

```text
URL:         https://arxiv.org/abs/1902.10186
Kind:        primary (for its own claim). Jain & Wallace author the experiments
             and the negative result. Secondary relative to Bahdanau (studies
             later BiLSTM-attention classification/QA models, not the 2015
             translation model).
Establishes: That, on the models they study, attention weights fail two tests a
             faithful explanation would pass.
Paraphrase:  Attention is widely presented as affording transparency, a
             distribution read as the relative importance of inputs. Across
             many NLP tasks the authors find (1) learned attention weights are
             frequently uncorrelated with gradient-based / leave-one-out
             feature-importance measures, and (2) one can construct very
             different ("adversarial") attention distributions that yield
             essentially the same prediction. They conclude standard attention
             does not provide meaningful explanations and should not be treated
             as though it does.
Locators:    Abstract; NAACL 2019. Models: BiLSTM with additive/tanh attention
             over binary classification and QA datasets.
Quote:       "learned attention weights are frequently uncorrelated with
             gradient-based measures of feature importance, and one can identify
             very different attention distributions that nonetheless yield
             equivalent predictions." / "standard attention modules do not
             provide meaningful explanations and should not be treated as though
             they do."
```

```text
URL:         https://arxiv.org/abs/1908.04626
Kind:        primary (for its own claim). Wiegreffe & Pinter author the rebuttal
             experiments. Secondary relative to Bahdanau.
Establishes: That whether attention "is explanation" depends on a prior
             definition and a whole-model experimental design, and that Jain &
             Wallace's adversarial result does not, by itself, disprove
             attention's usefulness for explanation.
Paraphrase:  The claim "attention is not explanation" depends on one's
             definition of explanation and must test all elements of the model.
             They propose four tests: a uniform-weights baseline; a
             variance calibration across random seeds; a frozen-attention
             diagnostic (train with attention held fixed); and an end-to-end
             adversarial-training protocol that produces a single
             model-consistent adversary rather than a free per-instance search.
             Their central finding: even when reliable adversarial distributions
             can be found, they do poorly on the simple diagnostic, so prior
             work does not disprove attention's usefulness for explainability.
Locators:    Abstract; EMNLP 2019.
Quote:       "such a claim depends on one's definition of explanation, and ...
             testing it needs to take into account all elements of the model."
             / "even when reliable adversarial distributions can be found, they
             don't perform well on the simple diagnostic, indicating that prior
             work does not disprove the usefulness of attention mechanisms for
             explainability."
```

## Contradictions

The central dispute is the alignment-as-explanation debate, and both sides are
recorded above. The disagreement is real and specific, not two summaries of one
origin:

- Jain & Wallace (2019) argue attention weights are not a faithful account of
  what drove a prediction, on two grounds: low correlation with gradient/
  leave-one-out importance, and the existence of alternative attention
  distributions giving the same output.
- Wiegreffe & Pinter (2019) do not claim attention *is* faithful; they argue
  Jain & Wallace's method overreaches. Two concrete objections: (1)
  "explanation" is undefined, so the negative test is ill-posed; and (2) Jain &
  Wallace's adversary is searched *per instance*, free to differ example by
  example, whereas a fair test needs a single trained model whose alternative
  attention is consistent across the dataset; under that constraint adversarial
  distributions are harder to find and perform worse on their frozen-attention
  diagnostic. Their title ("not not") is deliberate: attention is not
  established as explanation, but neither is it refuted.

Note the scope mismatch the writer must handle honestly: neither 2019 paper
tests Bahdanau's 2015 translation model. They study later BiLSTM attention on
classification and QA. The debate reframes how to read Bahdanau's Fig. 3
alignment plots (his own framing is that the soft alignments "agree well with
our intuition," a plausibility claim, not a faithfulness proof), but the 2019
authors do not make a claim about the 2015 model. A second, milder tension: the
2015 abstract asserts the alignments "agree well with our intuition," which the
later record recasts as evidence of plausibility, not of the weights being a
causal explanation of the output.

No contradiction was found in the focal paper's own numbers: Table 1 and the
Fig. 2 narrative are internally consistent (RNNsearch beats RNNencdec at both
30- and 50-word training caps, and the gap widens with sentence length).

## Numbers

All BLEU figures below are from Bahdanau et al. Table 1 (test set, WMT'14
English->French), verified against the paper's own table. "All" = full test set
including sentences with words unknown to the model; "No UNK" = restricted to
sentences composed only of known words. The suffix -30 / -50 is the maximum
training sentence length. RNNencdec is the fixed-vector baseline; RNNsearch is
the attention model.

```text
Figure: RNNencdec-30 BLEU = 13.93 (All), 24.19 (No UNK)
Owner:  Bahdanau et al., Table 1
Scope:  WMT'14 En->Fr test set; model trained on sentences up to 30 words

Figure: RNNsearch-30 BLEU = 21.50 (All), 31.44 (No UNK)
Owner:  Bahdanau et al., Table 1
Scope:  same test set; trained up to 30 words

Figure: RNNencdec-50 BLEU = 17.82 (All), 26.71 (No UNK)
Owner:  Bahdanau et al., Table 1
Scope:  same test set; trained up to 50 words

Figure: RNNsearch-50 BLEU = 26.75 (All), 34.16 (No UNK)
Owner:  Bahdanau et al., Table 1
Scope:  same test set; trained up to 50 words

Figure: RNNsearch-50* BLEU = 28.45 (All), 36.15 (No UNK)
Owner:  Bahdanau et al., Table 1
Scope:  same test set; RNNsearch-50 trained much longer, until development-set
        performance stopped improving (Table 1 footnote)

Figure: Moses (phrase-based baseline) BLEU = 33.30 (All), 35.63 (No UNK)
Owner:  Bahdanau et al., Table 1 (baseline they report)
Scope:  same test set. Note: Moses used a separate monolingual corpus for its
        language model in addition to the parallel data; a comparison the paper
        flags. On "No UNK," RNNsearch-50* (36.15) edges Moses (35.63).

Figure: Model size of the main model: n = 1000 hidden units, n' = 1000
        alignment units, m = 620 embedding dim, l = 500 maxout units
Owner:  Bahdanau et al., Appendix A.2.3
Scope:  architecture hyperparameters for the reported RNNsearch/RNNencdec models

Figure: Transformer BLEU (context only, not to be conflated with 2015 numbers):
        28.4 WMT'14 En->De; 41.8 WMT'14 En->Fr single model
Owner:  Vaswani et al. 2017, Abstract
Scope:  different task setup and years of progress later; use only as "what
        happened next," never as a head-to-head with Bahdanau's 26.75/28.45.
```

Fig. 2 (BLEU vs. sentence length) is a full series, not a single number; the
qualitative reading is the evidence: RNNencdec's BLEU drops sharply as source
length grows, while RNNsearch-30 and RNNsearch-50 stay roughly flat, with
RNNsearch-50 holding up even beyond 50-word sentences. Preserve the full curve
if captured.

## Source assets

```text
Asset: Figure 2 (BLEU vs. sentence length). Lives in the "Quantitative
       results" region (Sec. 5.1) of arXiv:1409.0473. A line plot: x-axis =
       source sentence length, y-axis = BLEU on the full test set (includes
       unknown words), with four curves: RNNencdec-30, RNNsearch-30,
       RNNencdec-50, RNNsearch-50.
Shows: The paper's core quantitative claim: the fixed-vector encoder-decoder
       degrades on long sentences while the attention model stays robust. This
       is the visual that settles the "bottleneck" argument.
Crop:  Must retain all four labeled curves, both axis labels, and the legend so
       RNNencdec vs. RNNsearch is unambiguous. Do not crop to a single curve or
       drop the length axis. Caption verbatim: "The BLEU scores of the
       generated translations on the test set with respect to the lengths of
       the sentences. The results are on the full test set which includes
       sentences having unknown words to the models."
       Capture from the primary PDF via `nb asset`; no external image URL.

Asset: Figure 3 (four sample alignment matrices found by RNNsearch-50). Lives
       in the "Qualitative analysis / Alignment" region (Sec. 5.2, figure
       floated near Sec. 4-5) of arXiv:1409.0473. Four grayscale heatmaps;
       x-axis = source English words, y-axis = generated French words; each
       pixel = alignment weight alpha_ij (Eq. 6), 0 black to 1 white.
Shows: That learned soft alignments are largely monotonic (bright near-diagonal)
       but capture real reorderings. Panel (a) contains the documented
       non-monotonic case: [European Economic Area] -> [zone economique
       europeenne], where the model aligns [zone] with [Area] (jumping over
       [European] and [Economic]) then steps back to complete the phrase. This
       is the figure that grounds the "alignment has a linguistic reading"
       claim the explanation debate later contests.
Crop:  Must retain both axis word labels (source and target tokens legible) and
       the grayscale mapping for at least panel (a), since the argument depends
       on reading which target word attends to which source word. If space
       forces one panel, use (a) for the adjective-noun swap; do not crop away
       the axis tick labels. Caption verbatim: "Four sample alignments found by
       RNNsearch-50. The x-axis and y-axis of each plot correspond to the words
       in the source sentence (English) and the generated translation (French),
       respectively. Each pixel shows the weight alpha_ij of the annotation of
       the j-th source word for the i-th target word (see Eq. (6)), in grayscale
       (0: black, 1: white). (a) an arbitrary sentence. (b-d) three randomly
       selected samples among the sentences without any unknown words and of
       length between 10 and 20 words from the test set."
       Capture from the primary PDF via `nb asset`; no external image URL.
```

## Discarded

```text
None. All five declared/consult sources (Bahdanau 1409.0473; Vaswani 1706.03762;
Jain & Wallace 1902.10186; Wiegreffe & Pinter 1908.04626) were read and used.
The exclusive-source policy of the brief was honored: no outside background was
substituted for the primary reading.
```
