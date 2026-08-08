# Evidence record: paper-of-the-day/neural-machine-translation-attention (02)

This record supersedes the 01 record for count purposes only: every 01 finding
below is preserved unchanged and still valid, and this round adds the four
predecessor/refinement sources the 02 brief named, reading each firsthand. The
record now holds eight genuinely-read sources. The evidence supports the full
commissioned reconstruction. The focal paper (Bahdanau, Cho, Bengio,
arXiv:1409.0473, ICLR 2015) owns, in its own text and tables, every element the
article turns on. The new sources firm up the predecessor line the paper builds
on (the fixed-vector RNN Encoder-Decoder of Cho et al. 2014 and the seq2seq LSTM
of Sutskever et al. 2014), the exact long-sentence degradation Fig. 2 answers
(Cho, Bahdanau et al. 2014, arXiv:1409.1259), and the immediate refinement of
the mechanism (Luong et al. 2015). One new tension surfaced that revises the 01
framing: the "fixed-vector models degrade on long sentences" motivation is
documented firsthand for the RNN Encoder-Decoder line (Cho 1409.1259), but
Sutskever et al. explicitly claim their reversed-input LSTM "did not have
difficulty on long sentences." The writer must attribute the degradation claim
to the encoder-decoder line specifically, not to all fixed-vector seq2seq, and
note Sutskever's contrary claim. This is recorded in Contradictions.

Where the record is thin (unchanged from 01): the focal paper studies only
English->French WMT'14, one language pair and one architecture, so its
generalization claim is narrow by construction; and the explanation debate was
conducted on later BiLSTM-attention classification/QA models, not on Bahdanau's
translation model itself, so importing it onto the 2015 paper is an analytic
bridge the writer must make explicitly. New thinness: cross-paper BLEU is not
head-to-head. Sutskever's 34.8/36.5 (En-Fr, large-vocab ensemble/rerank),
Cho 1406.1078's 33.87 (En-Fr, SMT feature), and Luong's 20.9/23.0/25.9 (En-De)
each sit in a different setup from Bahdanau's 26.75/28.45 and from each other;
none is a controlled comparison. The two focal figures are described here for
capture; they must be rendered from the primary PDF via `nb asset` (I did not
capture images).

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
URL:         https://arxiv.org/abs/1406.1078
Kind:        primary (for its own claim). Cho, van Merrienboer, Gulcehre,
             Bahdanau, Bougares, Schwenk, Bengio author the RNN Encoder-Decoder,
             the gated hidden unit, and the SMT experiments; they own those
             claims. Secondary relative to Bahdanau 1409.0473, which it precedes
             and which extends it; it is the fixed-vector architecture the focal
             paper fixes.
Establishes: The RNN Encoder-Decoder that Bahdanau's model extends, firsthand:
             an encoder RNN compresses a variable-length source into one
             fixed-length summary vector c, and a decoder RNN generates the
             target conditioned on c. Also the gated hidden unit (reset gate,
             update gate) later called the GRU, and that adding the model's
             phrase-pair conditional probability as a feature improves a
             phrase-based SMT system.
Paraphrase:  Two RNNs are trained jointly to maximize the conditional
             probability of a target sequence given a source sequence. The
             encoder reads the source token by token; its final hidden state is
             a summary c of the whole input (c = tanh(V h^{<N>})). The decoder's
             hidden state is h^{<t>} = f(h^{<t-1>}, y_{t-1}, c), so the SAME
             fixed vector c conditions every output step (this is exactly the
             fixed-length bottleneck Bahdanau replaces with a per-step c_i). The
             gated hidden unit uses a reset gate that lets a unit drop past
             state and an update gate that controls how much past state carries
             forward. Used as an extra feature scoring phrase pairs in Moses,
             it raises BLEU over the baseline.
Locators:    Abstract; Sec. 2.1-2.2 (encoder-decoder, summary c and decoder
             conditioning); Sec. 2.3 "Hidden Unit that Adaptively Remembers and
             Forgets" (reset/update gate equations); Sec. 4 + Table 1 (WMT'14
             En->Fr SMT results). EMNLP 2014.
Quote:       Abstract: "One RNN encodes a sequence of symbols into a
             fixed-length vector representation, and the other decodes the
             representation into another sequence of symbols. The encoder and
             decoder of the proposed model are jointly trained to maximize the
             conditional probability of a target sequence given a source
             sequence."
             Gated unit (Sec. 2.3), equations as printed:
             reset gate   `r_j = sigma([W_r x]_j + [U_r h_{<t-1>}]_j)`
             update gate  `z_j = sigma([W_z x]_j + [U_z h_{<t-1>}]_j)`
             candidate    `h~_j^{<t>} = phi([W x]_j + [U (r . h_{<t-1>})]_j)`
             new state    `h_j^{<t>} = z_j h_j^{<t-1>} + (1 - z_j) h~_j^{<t>}`
             (`.` is elementwise product; `sigma` logistic sigmoid).
```

```text
URL:         https://arxiv.org/abs/1409.3215
Kind:        primary (for its own claim). Sutskever, Vinyals, Le author the
             seq2seq LSTM, the reversed-input finding, and the WMT'14 En->Fr
             results; they own those claims. Secondary relative to Bahdanau: the
             other fixed-vector seq2seq predecessor, not an authority on
             Bahdanau's model.
Establishes: The parallel fixed-vector predecessor firsthand: a multilayer LSTM
             maps the whole input to a single fixed-dimensional vector, and a
             second deep LSTM decodes the target from that vector. The
             reversed-source-order trick. Strong WMT'14 En->Fr BLEU. And,
             importantly for the after-record, an explicit CLAIM that the LSTM
             did NOT struggle on long sentences.
Paraphrase:  End-to-end sequence learning with minimal structural assumptions:
             one LSTM encodes the source into a fixed-length vector, another
             decodes the translation from it. Reversing the word order of the
             source (not the target) markedly improved results by creating many
             short-term source-to-target dependencies that ease optimization.
             On WMT'14 En->Fr the LSTM reaches 34.8 BLEU on the full test set
             (penalized on out-of-vocabulary words); reranking a phrase-based
             system's 1000-best with the LSTM lifts BLEU to 36.5. The authors
             report the LSTM did not have difficulty on long sentences.
Locators:    Abstract; Sec. 1 (reversed input, long-sentence claim); Sec. 3-4
             (model, experiments, BLEU). NeurIPS 2014 (arXiv 1409.3215).
Quote:       Reversed input: "we found that reversing the order of the words in
             all source sentences (but not target sentences) improved the LSTM's
             performance markedly, because doing so introduced many short term
             dependencies between the source and the target sentence which made
             the optimization problem easier."
             BLEU (abstract): "the translations produced by the LSTM achieve a
             BLEU score of 34.8 on the entire test set, where the LSTM's BLEU
             score was penalized on out-of-vocabulary words." / "a phrase-based
             SMT system achieves a BLEU score of 33.3 on the same dataset." /
             "When we used the LSTM to rerank the 1000 hypotheses produced by
             the aforementioned SMT system, its BLEU score increases to 36.5,
             which is close to the previous best result on this task."
             Long sentences: "the LSTM did not have difficulty on long
             sentences."
```

```text
URL:         https://arxiv.org/abs/1409.1259
Kind:        primary (for its own claim). Cho, van Merrienboer, Bahdanau, Bengio
             author it. Same core group as the focal paper (Bahdanau, Cho,
             Bengio all co-authors), published months before 1409.0473. It is
             the diagnostic that motivates Bahdanau's Fig. 2.
Establishes: Firsthand, the exact failure mode the focal paper answers: neural
             machine translation with a fixed-length representation performs
             well on short sentences with known words but degrades RAPIDLY as
             sentence length and the number of unknown words grow. Studied on two
             encoder-decoder models: the RNN Encoder-Decoder (gated units) and a
             newly proposed gated recursive convolutional network (grConv).
Paraphrase:  Both encoder-decoder models compress a variable-length source into
             one fixed-length representation before decoding. Their translation
             quality falls off sharply with longer sources and with more unknown
             words. This is the same-group, pre-Bahdanau documentation of the
             bottleneck; Bahdanau's Fig. 2 (RNNencdec dropping while RNNsearch
             holds) is the direct answer to this degradation curve. The grConv
             additionally recovers grammatical structure automatically, a side
             finding not needed by the article.
Locators:    Abstract; the degradation analysis by length and unknown-word count
             (the paper's quantitative-analysis section, with per-length BLEU
             plots). Eighth Workshop on Syntax, Semantics and Structure in
             Statistical Translation (SSST-8), 2014.
Quote:       Abstract: "The encoder extracts a fixed-length representation from a
             variable-length input sentence, and the decoder generates a correct
             translation from this representation." / "We show that the neural
             machine translation performs relatively well on short sentences
             without unknown words, but its performance degrades rapidly as the
             length of the sentence and the number of unknown words increase."
```

```text
URL:         https://arxiv.org/abs/1508.04025
Kind:        primary (for its own claim). Luong, Pham, Manning author the global
             and local attention variants, the score functions, input feeding,
             and the WMT En->De results. Secondary relative to Bahdanau: the
             immediate refinement of Bahdanau's mechanism, part of the honest
             after-record.
Establishes: Firsthand that attention was refined right away: two attention
             classes (global, always over all source positions; local, over a
             small window per target word), three simpler score functions
             (dot, general, concat), and "input feeding" (feeding the previous
             attentional vector back into the next decoder input). Also a set of
             explicit, named architectural simplifications relative to Bahdanau,
             and competitive-to-SOTA WMT En->De BLEU.
Paraphrase:  Global attention derives the context vector from all encoder hidden
             states; local attention focuses on a subset per target word, either
             local-m (assume roughly monotonic, p_t = t) or local-p (predict an
             alignment position via a small network, then Gaussian-weight around
             it). They score a target hidden state against a source hidden state
             three ways: dot product, a general bilinear form with W_a, or a
             concat form matching Bahdanau's additive shape. Their model is
             simpler than Bahdanau's: it uses the top-layer LSTM hidden states in
             both encoder and decoder (not a concatenation of separate forward
             and backward states) and a shorter computation path
             h_t -> a_t -> c_t -> h~_t -> prediction. Input feeding makes the
             model aware of previous alignment choices. On WMT'14 En->De the best
             single attention model reaches 20.9 BLEU and an 8-model ensemble
             23.0; on WMT'15 En->De an 8-model ensemble reaches 25.9, a new SOTA
             at the time, +1.0 over the prior best NMT + reranker system.
Locators:    Abstract; Sec. 3.1 (global attention + three score functions);
             Sec. 3.2 (local attention, local-m and local-p); Sec. 3.3 (input
             feeding); Sec. 4 + Tables 1-2 (WMT'14 and WMT'15 En->De results).
             EMNLP 2015.
Quote:       Score functions (Sec. 3.1): dot `score(h_t, h_bar_s) = h_t^T
             h_bar_s`; general `score(h_t, h_bar_s) = h_t^T W_a h_bar_s`;
             concat `score(h_t, h_bar_s) = v_a^T tanh(W_a [h_t ; h_bar_s])`.
             Global vs local: the global model considers "all the hidden states
             of the encoder when deriving the context vector"; the local model
             "chooses to focus only on a small subset of the source positions per
             target word." local-p position: `p_t = S . sigmoid(v_p^T tanh(W_p
             h_t))`. SOTA claim: their best system "establishes a new state of
             the art result of 25.9 BLEU," outperforming the best NMT + n-gram
             reranker system by +1.0 BLEU.
```

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

New tension in the predecessor record (02): the "fixed-vector seq2seq degrades
on long sentences" motivation is NOT uniform across predecessors, and the writer
must not overstate it.

- Cho, Bahdanau et al. (1409.1259) document firsthand, for the RNN
  Encoder-Decoder line, that performance "degrades rapidly as the length of the
  sentence and the number of unknown words increase." This is the same group as
  the focal paper and the direct motivation Bahdanau's Fig. 2 answers.
- Sutskever, Vinyals, Le (1409.3215) claim the opposite for their model: "the
  LSTM did not have difficulty on long sentences." Their reversed-input trick
  and larger LSTM are the stated reasons.

These are not strictly contradictory (different architectures: GRU RNN
Encoder-Decoder vs. a deep reversed-input LSTM), but the article must attribute
the long-sentence bottleneck specifically to the RNN Encoder-Decoder line
(Cho 1406.1078 / 1409.1259), which is what Bahdanau's RNNencdec baseline in
Fig. 2 instantiates, and acknowledge Sutskever's contrary result rather than
implying every fixed-vector model collapses on long input. Bahdanau's own
contribution is that RNNsearch removes the fixed vector entirely, so it holds up
regardless of which baseline one starts from.

No contradiction was found in the focal paper's own numbers: Table 1 and the
Fig. 2 narrative are internally consistent (RNNsearch beats RNNencdec at both
30- and 50-word training caps, and the gap widens with sentence length).

## Numbers

All focal BLEU figures below are from Bahdanau et al. Table 1 (test set, WMT'14
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
```

Predecessor and refinement BLEU (02) - context only, NOT head-to-head with
Bahdanau; each sits in a different vocabulary/ensemble/language-pair setup:

```text
Figure: RNN Encoder-Decoder as SMT feature: baseline Moses 33.30 -> 33.87 (test)
        (dev: 30.64 -> 31.20)
Owner:  Cho et al. 2014, arXiv:1406.1078, Table 1 (called "Moses" baseline)
Scope:  WMT'14 En->Fr. Same Moses baseline value (33.30 test) that Bahdanau
        also reports; here the RNN Encoder-Decoder is only a rescoring feature,
        not a standalone translator.

Figure: Seq2seq LSTM = 34.8 BLEU (full WMT'14 En->Fr test set, penalized on
        out-of-vocabulary words); reranking a phrase-based system's 1000-best
        with the LSTM = 36.5; the phrase-based SMT baseline = 33.3
Owner:  Sutskever, Vinyals, Le 2014, arXiv:1409.3215, Abstract / results
Scope:  WMT'14 En->Fr, large-vocabulary deep LSTM (the 34.8 reflects the paper's
        full LSTM system, a different setup from Bahdanau's smaller single
        model; do not compare directly to 26.75/28.45).

Figure: Luong attention (WMT'14 En->De): best single model 20.9 BLEU; ensemble
        of 8 models 23.0 BLEU. WMT'15 En->De: ensemble of 8 = 25.9 BLEU (new
        SOTA at the time, +1.0 over prior best NMT + reranker)
Owner:  Luong, Pham, Manning 2015, arXiv:1508.04025, Tables 1-2 / Abstract
Scope:  English->German (different pair from Bahdanau's En->Fr); use only as
        "attention was refined and pushed to SOTA soon after," never as a
        head-to-head with Bahdanau's En->Fr numbers.

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
if captured. The same-shape degradation for the RNN Encoder-Decoder is
independently documented in Cho et al. 1409.1259 (BLEU falling with length and
unknown-word count).

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

The four 02 predecessor/refinement sources are used for the argument's spine
(fixed-vector bottleneck and the after-record), not as source assets. Their own
figures (e.g. the grConv grammar tree in 1409.1259, Luong's global/local
attention schematic) are not needed by the commissioned reconstruction, which
draws its visual evidence from the focal paper's Fig. 2 and Fig. 3.

## Discarded

```text
None. All eight sources were read firsthand and used: the four 01 sources
(Bahdanau 1409.0473; Vaswani 1706.03762; Jain & Wallace 1902.10186; Wiegreffe &
Pinter 1908.04626) and the four 02 sources the brief named (Cho et al.
1406.1078; Sutskever et al. 1409.3215; Cho, Bahdanau et al. 1409.1259; Luong et
al. 1508.04025). No outside background was substituted for the declared reading;
the 02 brief's named set was the whole menu for this round.
```
