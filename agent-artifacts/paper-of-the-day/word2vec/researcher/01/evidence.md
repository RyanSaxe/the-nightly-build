# Evidence: paper-of-the-day/word2vec (researcher/01)

The evidence solidly supports the commissioned angle and adds one finding the
commission did not anticipate. Every mechanism claim is verified against its
owning paper, read in full text (not abstract or secondary summary): the
CBOW/skip-gram architectures and the analogy task in "Efficient Estimation"
(arXiv:1301.3781); negative sampling, subsampling, and phrase vectors in
"Distributed Representations" (arXiv:1310.4546); the shifted-PMI factorization
result in Levy & Goldberg's NeurIPS 2014 paper, including its own stated
qualification (exact only in the large-dimensionality limit, and SGNS still
beats SVD-of-PMI on analogies in practice); the 3CosAdd formula, its
mathematical decomposition, and the explicit exclusion of the query words in
Levy & Goldberg's CoNLL 2014 paper; the ablation that makes the exclusion's
load-bearing role a *measured fact* rather than an inference, in Linzen 2016
(literal, unconstrained 3CosAdd returns one of the input words 98% of the
time); and the implementation-and-framing critique in Nissim, van Noord & van
der Goot 2020, which reproduces the accuracy collapse when the constraint is
lifted (0.71→0.21 for 3CosAdd) on the original Mikolov test set itself. Two
further primaries — Baroni, Dinu & Kruszewski 2014 and Levy, Goldberg & Dagan
2015 — supply the "what word2vec actually established" side of the verdict,
and they disagree with each other in an interesting, checkable way (see
Contradictions).

The one finding beyond the brief: the canonical King − Man + Woman = Queen
example, the demo the whole popular narrative hangs on, is not word2vec's own
result. "Efficient Estimation" states it explicitly, citing Mikolov, Yih &
Zweig 2013 (NAACL) as the source — a paper about **recurrent neural network
language model** embeddings, not CBOW or skip-gram, published five months
before "Efficient Estimation." I read that paper in full; it is where the
vector-offset method, the exclusion-of-query-words framing, and the
King/Queen example itself all originate. This complicates the standard
telling more than the commission's brief anticipated and is worth a
paragraph in the piece.

The record's thinnest point: I could not verify Mikolov et al.'s reported
Google-News-trained accuracy numbers directly, because the proprietary
training corpus and the exact trained vectors are not published; every
accuracy figure below is the number the owning paper itself reports, not an
independent reproduction. This is normal for the era and I flag it explicitly
rather than let it pass as independently confirmed. The two Levy-authored
replication papers (CoNLL 2014, TACL 2015) partially compensate: they retrain
skip-gram themselves on an open corpus (Wikipedia) and get comparable orders
of magnitude, which is the closest this record gets to independent
confirmation of the original numbers.

## Sources

```text
URL:         https://arxiv.org/abs/1301.3781 (v1 Jan 16 2013, latest v3 Sep 7 2013)
Kind:        primary — Mikolov, Chen, Corrado, Dean, "Efficient Estimation of
             Word Representations in Vector Space." Owns the CBOW/skip-gram
             architectures and the Semantic-Syntactic Word Relationship
             analogy test set.
Establishes: (1) CBOW and skip-gram architecture definitions and their
             computational-complexity formulas (Q = N·D + D·log2(V) for CBOW;
             Q = C·(D + D·log2(V)) for skip-gram), removing NNLM/RNNLM's
             nonlinear hidden layer. (2) The analogy-question scoring
             procedure: compute vector X (e.g. biggest − big + small), search
             for the closest word by cosine distance, "we discard the input
             question words during this search" — i.e., the exclusion of
             query words is stated by word2vec's own paper, not invented by a
             later critic. (3) Test set size: 8869 semantic + 10675 syntactic
             = 19544 questions. (4) Training data: Google News corpus, ~6B
             tokens; 1.6B-word training run; vocabulary capped at 1M most
             frequent words. (5) Best reported skip-gram accuracy: 300-dim,
             783M training words → 50.0% semantic / 55.9% syntactic / 53.3%
             total (Table 4); 300-dim, 1.6B words (1 epoch) → 52.2% / 55.1% /
             53.8%; 600-dim, 783M words → 56.7% / 54.5% / 55.5%. Table 3
             (fixed setup, cross-architecture): RNNLM 9/36, NNLM 23/53, CBOW
             24/64, Skip-gram 55/59 (semantic/syntactic %). (6) The
             King−Man+Woman≈Queen example appears in the Introduction
             (subsection "Goals of the Paper"), attributed by citation [20] to
             Mikolov, Yih & Zweig 2013 (NAACL) — this paper does not claim to
             have originated that example.
Paraphrase:  The paper's own contribution is efficiency (cheap architectures
             trained on much more data) and a systematic accuracy benchmark
             on an analogy test set it built; the offset-arithmetic technique
             and its most famous illustration are explicitly sourced to prior
             RNN work.
Locators:    Introduction §1.1 "Goals of the Paper" (King/Queen sentence and
             citation [20]); §3.1–3.2 (CBOW/skip-gram definitions and
             complexity); §4 (Results, opening paragraphs before §4.1) for the
             "we discard the input question words" sentence; Table 3, Table 4.
Quote:       "Using a word offset technique where simple algebraic operations
             are performed on the word vectors, it was shown for example that
             vector('King') − vector('Man') + vector('Woman') results in a
             vector that is closest to the vector representation of the word
             Queen [20]." / "Then, we search in the vector space for the word
             closest to X measured by cosine distance, and use it as the
             answer to the question (we discard the input question words
             during this search)."
```

```text
URL:         https://arxiv.org/abs/1310.4546 (v1 Oct 16 2013)
Kind:        primary — Mikolov, Sutskever, Chen, Corrado, Dean, "Distributed
             Representations of Words and Phrases and their Compositionality"
             (NeurIPS 2013). Owns negative sampling, subsampling, and phrase
             vectors.
Establishes: (1) Negative-sampling objective (Eq. 4): log σ(v'_wO·v_wI) +
             Σ E[log σ(−v'_wi·v_wI)]; recommended k = 5–20 for small corpora,
             k = 2–5 for large ones. Framed explicitly as a simplified
             alternative to Noise Contrastive Estimation: NCE needs sampled
             probabilities, negative sampling needs only samples. (2)
             Subsampling of frequent words (Eq. 5): P(discard) = 1 − √(t/f(w)),
             threshold t ≈ 1e-5. (3) Word-analogy result: NEG-15 with
             subsampling reaches 61% total accuracy on a 692K-word vocabulary
             trained on 1B words (Table 1). (4) Phrase analogy: best model
             (hierarchical softmax, 1000-dim, ~33B words) reaches 72% (Table
             3). (5) Phrase-scoring formula (Eq. 6): score(wi,wj) =
             (count(wi,wj) − δ)/(count(wi)·count(wj)), run over 2–4 passes
             with decreasing threshold. (6) The "Air Canada" example (meanings
             of "Canada" and "Air" don't compose to give "Air Canada") is the
             abstract/introduction's motivating case for phrase detection, not
             a worked example in the results tables — the worked additive-
             compositionality examples given are "Russian + river → Volga
             River" and "German + airlines → airline Lufthansa" (Table 5).
Paraphrase:  This is the paper that actually gives word2vec its practical
             training method (negative sampling) and its scaling advantage
             (subsampling); the celebrated analogy demo is not the focus of
             this paper — it appears as one accuracy table among several,
             framed as a way to show the sampling and subsampling changes
             don't hurt quality while they buy speed.
Locators:    §2 (Hierarchical Softmax vs. Negative Sampling, Eq. 4); §2.2
             (Subsampling, Eq. 5); §4 (Empirical Results, Table 1); §4 Learning
             Phrases (Eq. 6); §5 Additive Compositionality (Table 5).
Quote:       "values of k in the range 5–20 are useful for small training
             datasets, while for large datasets the k can be as small as 2–5."
```

```text
URL:         https://proceedings.neurips.cc/paper_files/paper/2014/hash/b78666971ceae55a8e87efb7cbfd9ad4-Abstract.html
             (PDF: .../file/b78666971ceae55a8e87efb7cbfd9ad4-Paper.pdf)
Kind:        primary — Levy & Goldberg, "Neural Word Embedding as Implicit
             Matrix Factorization" (NeurIPS 2014). Owns the shifted-PMI
             factorization result.
Establishes: (1) The main theorem (§3.1, Eq. 7): for sufficiently large
             embedding dimensionality d — large enough to allow perfect
             reconstruction of the target matrix — SGNS's objective is
             optimized exactly by setting w⃗·c⃗ = PMI(w,c) − log k for every
             (w,c) pair; i.e., SGNS with negative-sampling parameter k is
             implicitly factorizing the word-context matrix M_ij =
             PMI(w_i,c_j) − log k. This is derived by treating each dot
             product as an independent free parameter and solving the
             per-pair objective (Eq. 5) for its optimum — an idealization,
             not a claim about what SGD with a bounded d actually converges
             to. (2) Also shows NCE implicitly factorizes a shifted
             log-conditional-probability matrix (Eq. 8). (3) Empirically: an
             explicit sparse Shifted-PPMI matrix nearly attains the same
             objective value as SGNS and beats it on word-similarity
             correlation tasks (WordSim353, MEN); SVD-of-PPMI beats both on
             similarity but SGNS remains superior on analogy tasks,
             especially the syntactic set (Table 2: SGNS k=15 reaches 0.627 on
             the syntactic analogy set vs. SVD k=1's 0.448). (4) The authors'
             own explanation for SGNS's residual analogy advantage: SGNS
             performs *weighted* matrix factorization (frequent pairs matter
             more), unlike unweighted SVD — a stated conjecture, not proven.
Paraphrase:  The "SGNS factorizes shifted PMI" result is a real, derived
             theorem, but it is a limiting-case/idealized-optimum result: the
             paper itself is explicit that actual trained SGNS vectors (fixed,
             modest d) still outperform an exact factorization of that same
             target matrix on analogies, and it does not fully explain why.
Locators:    §2 (SGNS objective, Eq. 1–2); §3, §3.1 (derivation, Eq. 3–7); §3.2
             (weighted matrix factorization); §5.2 and Table 2 (linguistic task
             results); §6 (Conclusion).
Quote:       "For sufficiently large dimensionality d (i.e. allowing for a
             perfect reconstruction of M), each product w⃗·c⃗ can assume a value
             independently of the others. Under these conditions, we can treat
             the objective ℓ as a function of independent w⃗·c⃗ terms..." /
             "M^SGNS_ij = W_i·C_j = w⃗_i·c⃗_j = PMI(w_i,c_j) − log k."
```

```text
URL:         https://aclanthology.org/W14-1618/  (PDF: .../W14-1618.pdf)
Kind:        primary — Levy & Goldberg, "Linguistic Regularities in Sparse and
             Explicit Word Representations" (CoNLL 2014, Best Paper). Owns the
             3CosAdd formalization and the explicit-vs-neural analogy
             comparison.
Establishes: (1) Formalizes the offset method as 3COSADD (§3.2, Eq. 1):
             argmax_{b*∈V} cos(b*, b−a+a*), "where V is the vocabulary
             excluding the question words b, a and a*" — the exclusion is
             stated as part of the method's definition, attributed to how
             Mikolov et al. actually solved the task. (2) Shows 3CosAdd is
             algebraically equivalent (under unit-normalized vectors) to
             maximizing cos(b*,b) − cos(b*,a) + cos(b*,a*) (Eq. 3): a sum of
             two similarities minus one — "relational similarity... expressed
             as a sum of attributional similarities." (3) Introduces 3COSMUL
             (Eq. 4), a multiplicative variant that fixes a "one term
             dominates" failure mode (worked example: "London:England ::
             Baghdad:?" wrongly answers "Mosul" under 3CosAdd because
             geographic closeness swamps the relational signal; 3CosMul
             recovers "Iraq"). (4) Head-to-head numbers on MSR/GOOGLE/SEMEVAL
             analogy sets, comparing neural (skip-gram, 600-dim, NEG-15,
             Wikipedia ~1.5B tokens) against traditional sparse PPMI vectors
             on the same corpus: 3CosAdd — embedding 53.98/62.70/38.49%,
             explicit 29.04/45.05/38.54%; 3CosMul — embedding 59.09/66.72%,
             explicit 56.83/68.24% (SemEval ~38% for both). (5) Explicit
             vectors are interpretable: intersecting "woman"⊗"queen" surfaces
             features like female pronouns and names of queens, giving a
             literal look at what a "relational aspect" is made of (Table 7).
Paraphrase:  Word2vec's own SemEval/analogy pipeline used PAIR_DIRECTION for
             semantic analogies and 3CosAdd for syntactic ones, a distinction
             "not mentioned in the [Mikolov] paper" but confirmed by Levy &
             Goldberg both empirically and "by corresponding with the
             authors" — a primary-sourced correction to what word2vec's own
             papers say about their own evaluation.
Locators:    §3.2–3.3 (3CosAdd definition, Eq. 1, and reinterpretation, Eq. 3);
             §6 (3CosMul, Eq. 4, London/Baghdad example); Table 1, Table 3
             (head-to-head numbers); §9 (interpretability, Table 7); §11
             (Discussion, contradiction with Baroni et al. 2014 — see
             Contradictions).
Quote:       "arg max_{b*∈V} (cos(b*,b) − cos(b*,a) + cos(b*,a*))... where V is
             the vocabulary excluding the question words b, a and a*." /
             "[This] was not mentioned in the paper, [but] Mikolov et al.
             (2013c) used PAIR_DIRECTION for solving the semantic analogies of
             the SemEval task, and 3COSADD for solving the syntactic analogies.
             This was confirmed both by our independent trials and by
             corresponding with the authors."
```

```text
URL:         https://aclanthology.org/W16-2503/  (PDF: .../W16-2503.pdf)
Kind:        primary — Linzen, "Issues in evaluating semantic spaces using
             word analogies" (RepEval 2016). Owns the ablation that measures
             how load-bearing the exclusion constraint is.
Establishes: (1) A literal, unconstrained implementation of the offset method
             ("VANILLA," no exclusion) fails outright: on Linzen's own trained
             skip-gram spaces, the nearest neighbor of a*−a+b was the input
             word b in 93% of cases and a* in 5% — "it was never a" — leaving
             essentially no headroom for a correct novel answer. (2) Proposes
             baselines that also exclude {a,a*,b} but ignore the offset
             entirely — ONLY-B (nearest neighbor of b alone) and IGNORE-A — and
             shows these often recover much of ADD's (3CosAdd's) accuracy: on
             the "plurals" category ONLY-B alone scores .70 against ADD's
             comparable performance, meaning that category's apparent success
             is largely driven by b and b* already being close neighbors, not
             by consistent offsets. (3) Reversing the analogy direction (same
             offset, opposite query order) drops mean accuracy by −0.11, and
             the size of the drop correlates (Pearson r=.72) with how much the
             offset-blind ONLY-B baseline also drops — evidence that ADD's
             apparent success is entangled with neighborhood structure, not
             purely offset consistency.
Paraphrase:  This is the direct empirical demonstration, on real trained
             word2vec-style (skip-gram + negative sampling) spaces, that the
             exclusion of query words is not a minor implementation detail:
             remove it and the method effectively stops working, because the
             untouched vocabulary search is almost always won by one of the
             three input words.
Locators:    §2 (VANILLA/ADD/ONLY-B/IGNORE-A definitions, Eq. 2–7); §4 Results
             ("Baselines" and "Reversed analogies" paragraphs); §5 Discussion.
Quote:       "When these words were not excluded, the nearest neighbor of
             a*−a+b was b in 93% of the cases and a* in 5% of the cases (it
             was never a)." / "the performance of the offset method when
             applied to the Mikolov et al. (2013a) sets jointly evaluates the
             consistency of the offsets and the probability that b* is the
             nearest neighbor of b."
```

```text
URL:         https://aclanthology.org/2020.cl-2.7/  (PDF: .../2020.cl-2.7.pdf)
Kind:        primary — Nissim, van Noord & van der Goot, "Fair Is Better than
             Sensational: Man Is to Doctor as Woman Is to Doctor"
             (Computational Linguistics 46:2, 2020). Owns the
             implementation/framing critique and its own reproduction of the
             exclusion effect.
Establishes: (1) Independently reproduces Linzen's finding on the standard
             GoogleNews embeddings and the original Mikolov analogy test set:
             lifting the exclusion constraint drops macro-accuracy from 0.71
             to 0.21 for 3CosAdd, and from 0.73 to 0.45 for 3CosMul; in most
             failures the returned answer is simply the second input term B
             (D==B). (2) Points out the constraint is in fact documented in
             Mikolov et al. 2013 and in follow-up work (Linzen 2016; Bolukbasi
             et al. 2016; Goldberg 2017), yet argues it "is not common
             knowledge in the field" — and demonstrates the confusion is
             consequential: famous "bias" analogies such as man:doctor ::
             woman:X can never return "doctor" (the arguably unbiased answer)
             because the code structurally forbids D==B, so the system is
             being penalized for a constraint the querier imposed. (3) Shows
             analogy-detection algorithm choice, vocabulary-size cutoff, and
             threshold parameters (for the Bolukbasi formula) each swing the
             top answer for "man:doctor::woman:X" across "doctors," "nurse,"
             "midwife," "gynecologist," and "woman" (Table 3) — i.e., much of
             what gets reported as a finding about the embedding is actually a
             finding about the analyst's implementation choices.
Paraphrase:  This paper does not dispute that word2vec-style spaces encode
             societal associations; its target is specifically the analogy
             task's reliability as a *measurement instrument*, and it
             corroborates — with its own experiment, on the actual GoogleNews
             vectors — the same brittleness Linzen demonstrated on
             self-trained spaces.
Locators:    §3 (algorithms, Eq. 1–4); §4.1 (constrained vs. unconstrained
             results, Table 1); §4.3 (Table 3, threshold/vocab sensitivity);
             §5 (Final Remarks).
Quote:       "We observe a large drop in macro-accuracy for 3COSADD and
             3COSMUL in the unconstrained setting (from 0.71 to 0.21 and 0.73
             to 0.45, respectively). In most cases, this is because the second
             term is returned as answer (man is to king as woman is to king,
             D == B)."
```

```text
URL:         https://aclanthology.org/Q15-1016/  (PDF: .../Q15-1016.pdf)
Kind:        primary — Levy, Goldberg & Dagan, "Improving Distributional
             Similarity with Lessons Learned from Word Embeddings" (TACL 3,
             2015). Owns the hyperparameter-attribution finding and functions
             as the replication/benchmark source weighing word2vec's
             practical value against count-based alternatives.
Establishes: Directly reframes the "predict beats count" result reported by
             Baroni et al. 2014 (below): once hyperparameters that word2vec
             popularized as defaults (context distribution smoothing,
             dynamically-sized windows, negative-sampling-style corrections)
             are made explicit and ported into the traditional PPMI/SVD
             pipeline, "there is no consistent advantage to one algorithmic
             approach over another" — tuning a single hyperparameter often
             changes performance more than switching between SGNS, SVD, PPMI,
             and GloVe. This is the paper's stated central conclusion, not a
             minor caveat.
Paraphrase:  Word2vec's practical edge over older distributional methods,
             insofar as it existed, is substantially attributable to
             engineering choices bundled into the word2vec tooling
             (smoothing, context handling) rather than to the neural
             prediction objective itself.
Locators:    Abstract; §1 Introduction (paragraphs 3–5, stating the central
             finding and its relation to Levy & Goldberg 2014's implicit-PMI
             result); §2 (method definitions).
Quote:       "We also show that when all methods are allowed to tune a
             similar set of hyperparameters, their performance is largely
             comparable. In fact, there is no consistent advantage to one
             algorithmic approach over another, a result that contradicts the
             claim that embeddings are superior to count-based methods."
```

```text
URL:         https://aclanthology.org/P14-1023/  (PDF: .../P14-1023.pdf)
Kind:        primary — Baroni, Dinu & Kruszewski, "Don't count, predict! A
             systematic comparison of context-counting vs. context-predicting
             semantic vectors" (ACL 2014). Owns the "predict decisively beats
             count" benchmark result that Levy/Goldberg/Dagan 2015 later
             complicates.
Establishes: A large controlled comparison (36 count models × 48 predict/
             word2vec models, same ~2.8B-token corpus) across 14 lexical
             semantics benchmarks (relatedness, synonym detection, concept
             categorization, selectional preference, and the Mikolov analogy
             set). Best-setup predict models beat best-setup count models on
             13 of 14 tasks, often by a wide margin (e.g. analogy "an": 68%
             predict vs. 49% count, best-setup-per-task numbers, Table 2), and
             even the *worst* predict configuration usually beats the *best*
             count configuration. Explicitly frames this as a surprise to
             "seasoned distributional semanticists" who expected the opposite.
Paraphrase:  This is the paper the commission's "replication/benchmark"
             requirement points to: an independent group, not the word2vec
             authors, retrains both families of models on a shared corpus and
             finds skip-gram/CBOW-style representations are the more useful
             general-purpose semantic vectors of 2014 — a genuine practical
             finding, distinct from and prior to the analogy-specific critique.
Locators:    Abstract; §4 Results (Table 2, "best setup on each task" block);
             §5 Conclusion.
Quote:       "The results, to our own surprise, show that the buzz is fully
             justified, as the context-predicting models obtain a thorough and
             resounding victory against their count-based counterparts."
```

```text
URL:         https://aclanthology.org/N13-1090/  (PDF: .../N13-1090.pdf)
Kind:        primary — Mikolov, Yih & Zweig, "Linguistic Regularities in
             Continuous Space Word Representations" (NAACL-HLT 2013). Owns
             the vector-offset method and the King−Man+Woman=Queen example
             itself, on RNNLM vectors, not CBOW/skip-gram.
Establishes: (1) This paper, not "Efficient Estimation," introduces the
             vector-offset method for analogies (§5): compute y = x_b − x_a +
             x_c, find argmax_w cos(x_w, y). (2) The King/Queen example
             appears in this paper's abstract as the illustrative case for
             the "male/female relationship" offset. (3) The vectors tested are
             from a recurrent neural network language model (Mikolov 2010
             RNNLM toolkit), trained on 320M words of Broadcast News data,
             82k vocabulary — a different model family and roughly an order
             of magnitude less data than "Efficient Estimation"'s later
             skip-gram runs. (4) Reported RNN accuracy on its own 8000-question
             syntactic set: up to 39.6% (RNN-1600, composite of several
             dimensionalities); on the SemEval-2012 relational-similarity set,
             RNN vectors beat the prior best system (UTD-NB).
Paraphrase:  The demonstration that made the analogy idea famous predates
             word2vec's architectures. "Efficient Estimation" adopted the
             method and re-ran it, at far larger scale, on its own new
             architectures — meaning skip-gram/CBOW get credit in the popular
             narrative for a demo whose source paper used a different model.
Locators:    Abstract; §5 (The Vector Offset Method); §6 (Experimental
             Results, Tables 2–4).
Quote:       "For example, the male/female relationship is automatically
             learned, and with the induced vector representations, 'King -
             Man + Woman' results in a vector very close to 'Queen.'"
```

## Contradictions

1. **Baroni et al. 2014 vs. Levy & Goldberg 2014 (CoNLL), on whether neural
   embeddings actually beat traditional count vectors.** Baroni et al. report
   a "thorough and resounding victory" for predict (word2vec-style) models
   over count models across nearly all lexical-semantics tasks tested. Levy &
   Goldberg's CoNLL paper, published the same year, explicitly frames its
   analogy result as running counter to that: with 3CosMul, explicit PPMI
   vectors reach 56.83%/68.24% on MSR/GOOGLE against skip-gram's
   59.09%/66.72% — essentially tied — and their Discussion section says so
   in so many words: "contrary to the recent findings of Baroni et al.
   (2014), under certain conditions traditional word similarities induced by
   explicit representations can perform just as well as neural embeddings on
   this task." This is a live disagreement between two 2014 papers, not one
   later correcting the other.

2. **That contradiction is resolved (not just repeated) by Levy, Goldberg &
   Dagan 2015.** The TACL paper argues the Baroni et al. result was itself an
   artifact of unequal hyperparameter tuning between the two model families,
   and that once tuning is matched, "there is no consistent advantage to one
   algorithmic approach over another." I read all three papers directly; the
   2015 paper's account is the more careful one (it controls for the specific
   hyperparameters it names), but it is still one lab's account of a
   three-paper disagreement, not an independent fourth party's adjudication —
   worth stating as such rather than treating 2015 as the final word.

3. **What "the original paper" actually did on its own analogy task is
   itself disputed between the original authors and Levy & Goldberg.** Levy &
   Goldberg's CoNLL paper states Mikolov et al. used PAIR_DIRECTION (not
   3CosAdd) for the semantic-analogy half of their SemEval evaluation, a
   detail "not mentioned in the [original] paper" and confirmed only by
   "corresponding with the authors." Neither 2013 word2vec paper itself
   discloses this. I could not independently verify it beyond Levy &
   Goldberg's say-so (the original authors' side of that correspondence is
   not published), so the article should attribute this claim to Levy &
   Goldberg specifically, not treat it as settled word2vec-paper content.

4. **No contradiction, but a boundary worth being precise about:** Levy &
   Goldberg's NeurIPS "implicit factorization" result is an idealized-optimum
   theorem (exact only for sufficiently large d), and the same paper reports
   that actual SGNS still beats an exact SVD factorization of the same target
   matrix on analogy tasks. The mechanism explains what the *objective's*
   optimum looks like, not fully why trained, dimension-bounded SGNS vectors
   are good at analogies specifically. The paper's own explanation
   (SGNS's frequency-weighting) is offered as a conjecture, not proven.

## Numbers

```text
Figure: 8869 semantic + 10675 syntactic = 19544 analogy questions
Owner:  Mikolov et al. 2013 (arXiv:1301.3781), the "Semantic-Syntactic Word
        Relationship" test set
Scope:  Full test set as released; Levy & Goldberg 2014 (CoNLL) independently
        report the same 19544 total for their "GOOGLE" dataset, cross-
        confirming the count.
```

```text
Figure: Skip-gram, 300-dim, 1.6B training words → 52.2% semantic / 55.1%
        syntactic / 53.8% total accuracy
Owner:  Mikolov et al. 2013 (arXiv:1301.3781), Table 4
Scope:  Google News corpus (~6B tokens, subsampled to 1.6B words for this
        run); vocabulary capped at 1M most frequent words; single epoch.
```

```text
Figure: "we discard the input question words" (Vanilla, unconstrained)
        → nearest neighbor is the input word b in 93% of cases, a* in 5%,
        a in 0% of cases
Owner:  Linzen 2016 (RepEval), measured on Linzen's own skip-gram-with-
        negative-sampling spaces (s2/s5/s10, trained on ukWaC + 2013
        Wikipedia)
Scope:  All 14 Mikolov analogy categories combined, VANILLA condition only
        (no exclusion of a, a*, b from the candidate pool).
```

```text
Figure: 3CosAdd macro-accuracy on GoogleNews embeddings: 0.71 (constrained,
        query words excluded) → 0.21 (unconstrained, query words allowed)
Owner:  Nissim, van Noord & van der Goot 2020, §4.1, Table 1 discussion
Scope:  Full original Mikolov et al. 2013 analogy test set, standard
        pretrained GoogleNews vectors (code.google.com/archive/p/word2vec).
        3CosMul figures for the same comparison: 0.73 → 0.45.
```

```text
Figure: M^SGNS_ij = PMI(w_i, c_j) − log k  (the implicit factorization
        identity)
Owner:  Levy & Goldberg 2014 (NeurIPS), Eq. 7
Scope:  Holds exactly only "for sufficiently large dimensionality d (i.e.
        allowing for a perfect reconstruction of M)" — an idealized-optimum
        condition, not a claim about trained low-dimensional vectors.
```

```text
Figure: 3CosAdd: embedding 62.70% vs. explicit (PPMI) 45.05% on GOOGLE;
        3CosMul: embedding 66.72% vs. explicit 68.24% on GOOGLE (explicit
        edges ahead once the additive objective is replaced)
Owner:  Levy & Goldberg 2014 (CoNLL), Table 1 and Table 3
Scope:  Skip-gram (600-dim, NEG-15, subsampling 1e-5) vs. PPMI, both trained
        on the same ~1.5B-token English Wikipedia corpus; GOOGLE test set
        after removing 286 out-of-vocabulary instances (19258 of 19544
        remain).
```

```text
Figure: Best-setup predict (word2vec) models beat best-setup count models on
        13 of 14 lexical-semantics benchmarks tested, e.g. analogy task "an":
        predict 68% vs. count 49%
Owner:  Baroni, Dinu & Kruszewski 2014, Table 2
Scope:  Shared ~2.8B-token corpus (ukWaC + Wikipedia + BNC); 36 count model
        configurations vs. 48 predict configurations, best-per-task
        comparison.
```

Preserved series (useful if a chart is warranted): Mikolov et al. 2013
(arXiv:1301.3781) Table 4 gives accuracy at three training-data/dimension
combinations (783M words/300-dim; 1.6B words/300-dim; 783M words/600-dim),
enough points to show accuracy rising with data and dimensionality but not
enough for a dense curve — treat any chart built from it as illustrating the
trend the paper reports, not a reconstructed learning curve.

## Source assets

```text
Asset: Levy & Goldberg CoNLL 2014, Table 3 — 3CosAdd vs. 3CosMul, embedding
       vs. explicit representation, on MSR and GOOGLE (4 numbers × 2 methods)
Shows: The size of the gap the exclusion-and-scoring-function choice creates
       between "neural embeddings clearly win" (3CosAdd) and "count-based
       vectors are competitive or ahead" (3CosMul) — the single clearest
       piece of furniture for the "measurement choice, not just data" thread
       of the article.
Crop:  Keep both methods and both datasets together; the comparison is the
       point. Omit SEMEVAL if space is tight — its near-tie result doesn't
       carry new information beyond what MSR/GOOGLE already show.
```

```text
Asset: Nissim et al. 2020, Table 1 — constrained vs. unconstrained top answer
       for three "gender bias" analogy queries (man:doctor::woman:X, etc.),
       across 3CosAdd, 3CosMul, and the Bolukbasi formula
Shows: Concretely, in the article's own worked example, what changes when the
       query-word exclusion is turned off — "doctor" becomes an available
       (and returned) answer once it's no longer structurally forbidden.
Crop:  Needs all three algorithm columns and both constrained/unconstrained
       rows to make the point that the exclusion — not anything about the
       embedding — is what manufactures the "biased" answer in this
       particular famous case.
```

```text
Asset: Linzen 2016, Figure 4 — bar chart of all analogy-scoring functions
       (Vanilla, Add, Only-B, Ignore-A, Add-opposite, Multiply, two reversed
       variants) across all 14 Mikolov categories, on space s5
Shows: How much of "Add"'s (3CosAdd's) apparent success in each category is
       already captured by baselines that ignore the offset entirely —
       category-by-category, not just in aggregate.
Crop:  Dense; if used, a redrawn version isolating 3–4 categories (e.g.
       plurals, where the offset-blind baseline nearly matches Add; and
       common-capitals, where Add's advantage over the baselines is largest)
       would carry the argument better than the full 14-category original.
```

```text
Asset: Mikolov et al. 2013 (arXiv:1301.3781), Table 4 — accuracy vs. training
       corpus size and vector dimensionality for skip-gram
Shows: The scaling relationship that is the paper's actual headline
       contribution (more data and more dimensions, cheaply, beats the older
       architectures) independent of the analogy-scoring controversy.
Crop:  Three rows only; reproduce as-is or as a small bar/line comparison —
       there is no larger series available from within the paper's own
       tables at published resolution.
```

None found beyond the above: the two 2013 word2vec papers do not include
loss curves, embedding-space projections, or other diagrams beyond the
tables already listed; nothing in the NAACL, TACL, or ACL papers offers
additional visual evidence not already captured.

## Discarded

```text
URL: https://levyomer.wordpress.com/2014/09/10/neural-word-embeddings-as-implicit-matrix-factorization/
     — author's blog post, used only to locate a working PDF mirror after the
     stale papers.nips.cc hash returned 404; not used as a citable source.
     The formal citation is the canonical proceedings.neurips.cc URL
     (verified resolving), not the blog.
```
