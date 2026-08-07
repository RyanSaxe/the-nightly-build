# Evidence record: paper-of-the-day/bert (01)

The record supports all three limbs of the commissioned verdict from primary
sources. The durable contribution — deep bidirectional masked-LM pretraining
plus light fine-tuning, transferring across many tasks and beating left-to-right
(GPT) and feature-based (ELMo) approaches — is documented in BERT's own Table 1
and Section 5 ablations, verified numeral by numeral. NSP's secondary claim did
NOT survive: RoBERTa's controlled Table 2 shows removing the NSP loss matches or
slightly improves downstream results, ALBERT shows a plain NSP objective sits at
random-guess (52.0%) on sentence-order, and BERT's own Table 5 already showed
NSP's contribution was small. MLM's supervision inefficiency is documented as a
real limit in ELECTRA: only the ~15% masked tokens are supervised, and
replaced-token detection over all tokens reaches comparable GLUE at under a
quarter of the compute. The record is thin/entangled in exactly one place, and
it matters: RoBERTa's "NSP unnecessary" finding is confounded with a
simultaneous input-format change (SEGMENT-PAIR vs FULL/DOC-SENTENCES) and, in
its headline model, with four other changes at once; only Table 2 isolates it on
matched data. Cross-paper GLUE numbers also mix TEST/leaderboard (BERT Table 1)
with DEV (all ablations, RoBERTa Table 5, ELECTRA) — the writer must label which
is which and never compare across the line. All figure images must be
RECONSTRUCTED as house charts (arXiv non-exclusive license); the numeric series
below are preserved for that. The only verbatim reproduction the template allows
is the abstract card.

## Sources

```text
URL:         https://aclanthology.org/N19-1423/  (canonical; arXiv:1810.04805 v2, 24 May 2019)
Kind:        primary — the focal paper; owns the MLM objective, NSP, model sizes, and all BERT tables.
Establishes: Deep bidirectional MLM pretraining + fine-tuning; the 15% / 80-10-10 masking recipe and its stated reason; NSP; BERT-BASE/LARGE sizes; the GLUE and Section-5 ablation results.
Paraphrase:  BERT pretrains a deep Transformer ENCODER to condition jointly on left and right context "in all layers" by predicting randomly masked tokens (MLM), plus a next-sentence-prediction auxiliary task; the same pretrained weights fine-tune with one added output layer to state-of-the-art on eleven NLP tasks, pushing the GLUE score to 80.5%.
Locators:    Abstract; Sec 3.1 "Task #1: Masked LM"; Sec 3.1 "Task #2: Next Sentence Prediction"; Sec 3 "Model Architecture" (sizes); Table 1 (GLUE test); Table 5 (Sec 5.1 ablation); Table 6 (Sec 5.2 size); Table 7 (Sec 5.3 feature-based NER). Authors: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. Venue: NAACL-HLT 2019, pp. 4171-4186, Best Long Paper.
Quote:       Masking reason — "To mitigate this, we do not always replace 'masked' words with the actual [MASK] token" because [MASK] never appears during fine-tuning, which would otherwise create a pretrain/fine-tune mismatch. NSP — "50% of the time B is the actual next sentence that follows A (labeled as IsNext), and 50% of the time it is a random sentence from the corpus (labeled as NotNext)."
```

```text
URL:         https://arxiv.org/abs/1907.11692  (arXiv-only, submitted 26 Jul 2019; never went to a venue)
Kind:        primary — owns the replication study; the authority for "BERT was undertrained" and "NSP unnecessary."
Establishes: BERT was significantly undertrained; with more data, longer training, larger batches, dynamic masking, no NSP, and longer sequences it matches or exceeds every model published after BERT; removing the NSP loss matches or slightly improves downstream performance.
Paraphrase:  A careful replication finds hyperparameters and data scale, not architecture, drive most reported gains after BERT. RoBERTa's recipe: dynamic masking (mask pattern regenerated each epoch, not fixed once), FULL-SENTENCES / DOC-SENTENCES inputs with the NSP loss dropped, batch size 8K, 160GB of text (vs BERT's 16GB), byte-level BPE with a 50K vocabulary, and up to 500K steps. The controlled input-format ablation (Table 2) is what isolates the NSP finding on matched data.
Locators:    Abstract; Sec 3.2 (data: 16GB vs 160GB; batches; byte-level BPE 50K); Sec 4.1 Table 1 (static vs dynamic masking); Sec 4.2 Table 2 (input format / NSP); Sec 4.4 Table 4 (more data + longer training); Sec 5 Table 5 (GLUE dev vs BERT-Large / XLNet-Large). Authors: Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov.
Quote:       "We find that BERT was significantly undertrained, and can match or exceed the performance of every model published after it." On NSP — "we find that removing the NSP loss matches or slightly improves downstream task performance." On masking — "dynamic masking is comparable or slightly better than static masking."
```

```text
URL:         https://arxiv.org/abs/2003.10555  (ICLR 2020)
Kind:        primary — owns the MLM sample-inefficiency argument and the replaced-token-detection alternative.
Establishes: MLM supervises only the ~15% masked subset per example (sample-inefficient); replaced token detection (RTD) is defined over ALL input tokens, so it learns more per example and is more compute-efficient; RTD reaches comparable or better GLUE than BERT/GPT/RoBERTa/XLNet at far less compute.
Paraphrase:  ELECTRA replaces [MASK]-and-reconstruct with a discriminator that labels every token as original or replaced, where the replacements come from a small generator. Because the loss is over all tokens rather than the 15% masked ones, the same compute buys stronger representations. A one-GPU/4-day ELECTRA-Small beats GPT (trained with ~30x more compute) on GLUE; ELECTRA-Large matches RoBERTa/XLNet at under a quarter of their compute and beats them at equal compute.
Locators:    Abstract; Introduction ("the network only learns from 15% of the tokens per example"; "the model learns from ALL input tokens instead of just the small masked-out subset"); Figure 1 (GLUE score vs pre-train FLOPs); Table 1 (small/base + FLOPs); Table 2 (large models + FLOPs). Authors: Kevin Clark, Minh-Thang Luong, Quoc V. Le, Christopher D. Manning.
Quote:       "A key advantage of our discriminative task is that the model learns from all input tokens instead of just the small masked-out subset, making it more computationally efficient." And: "using less than 1/4 of the compute to train ELECTRA-400K as it did to train RoBERTa and XLNet."
```

```text
URL:         https://arxiv.org/abs/1804.07461  (ICLR 2019)
Kind:        primary — owns the GLUE benchmark definition; secondary to BERT's result.
Establishes: What GLUE is, so BERT's "80.5 GLUE score" can be labeled honestly.
Paraphrase:  GLUE is a collection of nine English natural-language-understanding tasks reported as a single macro-average (equal weight per task): MNLI, QQP, QNLI, SST-2, CoLA, STS-B, MRPC, RTE, WNLI. It is model-agnostic and rewards knowledge shared across tasks; at release, transfer/multi-task systems did not substantially beat per-task training.
Locators:    Abstract; task table (Sec 2 / Table 1). Authors: Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, Samuel R. Bowman.
Quote:       —
```

```text
URL:         https://arxiv.org/abs/1909.11942  (ALBERT; ICLR 2020)
Kind:        primary — owns the NSP-conflation argument and the SOP alternative; changes the interpretation of RoBERTa's NSP result.
Establishes: A diagnosis of WHY NSP was weak (distinct from RoBERTa's "just drop it"): NSP conflates topic prediction with coherence prediction, topic is the easier signal and overlaps with what MLM already learns, so a plain NSP head sits near random on true coherence. Sentence-order prediction (SOP) — same two consecutive segments, positive in order and negative when swapped — targets coherence alone and helps multi-sentence downstream tasks.
Paraphrase:  Because NSP's negatives come from different documents, they differ in BOTH topic and coherence; the model can win by spotting topic shifts, which MLM already supplies. Swap in SOP (order-only) and the intrinsic coherence signal rises sharply while downstream multi-sentence tasks improve.
Locators:    Abstract ("a self-supervised loss that focuses on modeling inter-sentence coherence"); Sec 3.1 "Inter-sentence coherence loss"; Sec 4.6 Table 5 (SOP vs NSP intrinsic + downstream). Authors: Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut.
Quote:       "NSP conflates topic prediction and coherence prediction in a single task"; topic prediction "is easier to learn compared to coherence prediction, and also overlaps more with what is learned using the MLM loss." Intrinsic: an NSP-trained head reaches only 52.0% on the SOP task (near random), while an SOP-trained head reaches 86.5% on SOP and still 78.9% on NSP.
```

```text
URL:         https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf  (OpenAI, 2018; the paper's own home; text extracted from mirror https://www.cs.ubc.ca/~amuham01/LING530/papers/radford2018improving.pdf because the CDN PDF returned as binary to the fetcher)
Kind:        primary — "OpenAI GPT," the left-to-right baseline BERT is defined against; owns the autoregressive LM objective.
Establishes: The left-to-right factorization BERT breaks with; the same pretrain-then-fine-tune shape (BERT's contribution is bidirectionality, not the transfer recipe itself, which GPT already used).
Paraphrase:  GPT pretrains a multi-layer Transformer DECODER as a standard language model, each token conditioned only on the k PREVIOUS tokens, then fine-tunes per task with a task-specific head and input transformations. It improved SOTA on 9 of 12 tasks. This is the unidirectional model BERT's Table 1 (GPT 75.1 avg) and Table 5 ("LTR & No NSP") sit against.
Locators:    Abstract; Sec 3.1 "Unsupervised pre-training," Eq. 1: L1(U) = sum_i log P(u_i | u_{i-k},...,u_{i-1}; Theta), "multi-layer Transformer decoder." Authors: Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever.
Quote:       "we use a standard language modeling objective to maximize the following likelihood: L1(U) = sum_i log P(u_i | u_{i-k}, ..., u_{i-1}; Theta)" — left context only.
```

```text
URL:         https://arxiv.org/abs/1802.05365  (ELMo; NAACL 2018)
Kind:        primary — the feature-based / shallow-bidirectional baseline BERT is defined against.
Establishes: The "feature-based" contrast and the "shallow" bidirectionality BERT claims to improve on; grounds BERT Table 7 (feature-based vs fine-tuning).
Paraphrase:  ELMo derives contextual word vectors from a pretrained biLSTM language model and feeds them, frozen, into task-specific models (feature-based use, not fine-tuning). Its bidirectionality is a shallow concatenation of an independently trained left-to-right and a right-to-left LM, not joint conditioning in every layer — the exact gap BERT's MLM closes.
Locators:    Abstract; the biLM is a concatenation of independent forward/backward LSTMs. Authors: Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer.
Quote:       "Our word vectors are learned functions of the internal states of a deep bidirectional language model (biLM), which is pre-trained on a large text corpus."
```

```text
URL:         https://arxiv.org/abs/1906.08237  (XLNet; NeurIPS 2019)
Kind:        primary — the architecture rival RoBERTa reframes; owns the permutation-LM alternative.
Establishes: The "architecture, not training" claim that RoBERTa pushes back on. XLNet argued a better OBJECTIVE (permutation LM, no [MASK]) beats BERT on 20 tasks; RoBERTa then showed a well-trained BERT matches/exceeds XLNet, relocating the gain to training scale. This is the core "source of recent improvements" tension.
Paraphrase:  XLNet keeps autoregressive factorization but maximizes likelihood over all permutations of token order, so each position sees bidirectional context without a [MASK] token, removing BERT's pretrain/fine-tune discrepancy; it reports beating BERT on 20 tasks. RoBERTa Table 5 and ELECTRA Table 2 later benchmark against it.
Locators:    Abstract. Authors: Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Ruslan Salakhutdinov, Quoc V. Le.
Quote:       "relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy"; "under comparable experiment settings, XLNet outperforms BERT on 20 tasks, often by a large margin."
```

## Contradictions

- BERT's NSP claim vs RoBERTa's refutation. BERT (Table 5, Sec 5.1) reports
  that removing NSP hurts: MNLI-m 84.4 -> 83.9, QNLI 88.4 -> 84.9, MRPC 86.7 ->
  86.5, SST-2 92.7 -> 92.6, SQuAD F1 88.5 -> 87.9, and concludes NSP helps.
  RoBERTa (Table 2) reports that dropping the NSP loss matches or slightly
  improves. THE CONFOUND, owned by RoBERTa: BERT's "No NSP" ablation kept the
  SEGMENT-PAIR input (two concatenated segments) and only removed the loss,
  whereas RoBERTa's gain appears only when it ALSO switches to FULL-SENTENCES /
  DOC-SENTENCES (a single contiguous span, no segment pairing). In RoBERTa
  Table 2, SENTENCE-PAIR+NSP (short single-sentence pairs) is the worst row,
  and DOC-SENTENCES (no NSP, contiguous) is the best. So the honest reading is
  "the NSP loss is unnecessary once the input format is fixed," not "NSP does
  nothing in BERT's own setup." The writer should not present these as a flat
  contradiction.

- Data / multi-change confound in RoBERTa's HEADLINE model. RoBERTa's flagship
  result changes at least five things at once (10x data, 8K batch, longer
  training, dynamic masking, no NSP). Only the controlled ablations on matched
  data — Table 1 (masking), Table 2 (NSP/input format), Table 4 (isolating data
  and steps) — attribute effects to individual choices. Cite Table 2 for the
  NSP claim, not the headline GLUE table.

- Mechanism disagreement, NSP vs SOP. RoBERTa's remedy is to delete the
  auxiliary sentence objective; ALBERT's is to REPLACE it with a coherence-only
  objective (SOP) and shows that helps multi-sentence tasks. Both agree BERT's
  NSP as specified was weak; they disagree on whether any inter-sentence
  objective is worth keeping. Owners: RoBERTa (drop it) and ALBERT (fix it).

- Architecture vs training, the "source of gains" dispute. XLNet claimed a new
  objective (permutation LM, no [MASK]) was why it beat BERT on 20 tasks.
  RoBERTa (abstract: "raise questions about the source of recently reported
  improvements") showed a well-trained BERT matches or exceeds XLNet (Table 5:
  RoBERTa 90.2 MNLI vs XLNet 89.8 vs BERT-LARGE 86.6), relocating much of the
  reported gain from architecture to training scale. Owners: XLNet (Yang et al.)
  vs RoBERTa (Liu et al.). This is the strongest external support for "BERT's
  recipe was undertrained, not out-designed."

- Dev vs test mismatch across the record. BERT Table 1 is TEST/leaderboard
  (GLUE score 80.5, WNLI included via the leaderboard). BERT's Table 1
  "Average" column (82.1 for BERT-LARGE) EXCLUDES WNLI, so it is not the same
  number as the 80.5 leaderboard score — they are different aggregations, not a
  discrepancy. All Section-5 ablations, RoBERTa Table 5, and ELECTRA Tables 1-2
  are DEV. Never compare a dev number in one paper to a test number in another.

## Numbers

BERT — model sizes (Sec 3, "Model Architecture"):
```text
Figure: BERT-BASE = L 12, H 768, A 12, 110M parameters
Owner:  Devlin et al. 2019
Scope:  Transformer encoder; matched to OpenAI GPT size for comparison
```
```text
Figure: BERT-LARGE = L 24, H 1024, A 16, 340M parameters
Owner:  Devlin et al. 2019
Scope:  Transformer encoder
```

BERT — MLM recipe (Sec 3.1, "Task #1: Masked LM"):
```text
Figure: 15% of WordPiece tokens masked at random; of those, 80% -> [MASK], 10% -> random token, 10% -> unchanged
Owner:  Devlin et al. 2019
Scope:  per training sequence; the 80/10/10 split mitigates the pretrain/fine-tune [MASK] mismatch
```

BERT — Table 1 (GLUE TEST set; leaderboard):
```text
Figure: GLUE score (leaderboard): BERT-LARGE 80.5; OpenAI GPT 72.8; prior SOTA improvement +7.7 pts absolute
Owner:  Devlin et al. 2019, Table 1 + Abstract
Scope:  9-task macro-average, test server (WNLI included on leaderboard)
```
```text
Figure: Table 1 "Average" column (WNLI excluded): BERT-LARGE 82.1, BERT-BASE 79.6, OpenAI GPT 75.1, Prior SOTA 74.0
Owner:  Devlin et al. 2019, Table 1
Scope:  8-task average as printed in the paper (differs from the 80.5 leaderboard aggregation)
```
```text
Figure: MNLI-m/mm test: BERT-LARGE 86.7/85.9, BERT-BASE 84.6/83.4, OpenAI GPT 82.1/81.4, Prior SOTA 80.6/80.1
Owner:  Devlin et al. 2019, Table 1
Scope:  MNLI matched/mismatched accuracy, test set
```

BERT — Table 5 (Sec 5.1 ablation, DEV accuracies; SQuAD = F1):
```text
Series (MNLI-m, QNLI, MRPC, SST-2, SQuAD):
  BERT-BASE      84.4, 88.4, 86.7, 92.7, 88.5
  No NSP         83.9, 84.9, 86.5, 92.6, 87.9
  LTR & No NSP   82.1, 84.3, 77.5, 92.1, 77.8
  + BiLSTM       82.1, 84.1, 75.7, 91.6, 84.9
Owner:  Devlin et al. 2019, Table 5
Scope:  DEV; "LTR & No NSP" is a left-to-right LM (GPT-like); largest NSP effect is QNLI (88.4->84.9)
```

BERT — Table 6 (Sec 5.2 model size; DEV; LM = held-out perplexity):
```text
Series (#L, #H, #A -> LM ppl, MNLI-m, MRPC, SST-2):
  3,  768, 12 -> 5.84, 77.9, 79.8, 88.4
  6,  768,  3 -> 5.24, 80.6, 82.2, 90.7
  6,  768, 12 -> 4.68, 81.9, 84.8, 91.3
  12, 768, 12 -> 3.99, 84.4, 86.7, 92.9
  12,1024, 16 -> 3.54, 85.7, 86.9, 93.3
  24,1024, 16 -> 3.23, 86.6, 87.8, 93.7
Owner:  Devlin et al. 2019, Table 6
Scope:  DEV accuracy; bigger model helps even tiny MRPC/SST-2 tasks
```

BERT — Table 7 (Sec 5.3 feature-based, CoNLL-2003 NER, Dev F1):
```text
Series (CoNLL-2003 NER Dev F1):
  Fine-tuning BERT-LARGE                 96.6
  Fine-tuning BERT-BASE                  96.4
  Feature-based (BERT-BASE):
    Embeddings only                      91.0
    Second-to-Last Hidden                95.6
    Last Hidden                          94.9
    Weighted Sum Last Four Hidden        95.9
    Concat Last Four Hidden              96.1
    Weighted Sum All 12 Layers           95.5
Owner:  Devlin et al. 2019, Table 7
Scope:  DEV F1; best feature-based (Concat Last Four, 96.1) trails fine-tuning (96.4) by only ~0.3
```

RoBERTa — Table 1 (static vs dynamic masking, DEV; SQuAD 2.0 F1):
```text
Series (SQuAD 2.0 F1, MNLI-m, SST-2):
  reference (BERT re-eval) 76.3, 84.3, 92.8
  static                   78.3, 84.3, 92.5
  dynamic                  78.7, 84.0, 92.9
Owner:  Liu et al. 2019, Table 1
Scope:  DEV; dynamic comparable-to-slightly-better
```

RoBERTa — Table 2 (input format / NSP, DEV; SQuAD 1.1/2.0 F1):
```text
Series (SQuAD1.1/2.0 F1, MNLI-m, SST-2, RACE):
  SEGMENT-PAIR + NSP   90.4/78.7, 84.0, 92.9, 64.2
  SENTENCE-PAIR + NSP  88.7/76.2, 82.9, 92.1, 63.0
  FULL-SENTENCES       90.4/79.1, 84.7, 92.5, 64.8
  DOC-SENTENCES        90.6/79.7, 84.7, 92.7, 65.6
Owner:  Liu et al. 2019, Table 2
Scope:  DEV; the two no-NSP rows (FULL/DOC-SENTENCES) match or beat the NSP rows
```

RoBERTa — Table 4 (more data + longer training, DEV; SQuAD 2.0 F1):
```text
Series (SQuAD 2.0 F1, MNLI-m, SST-2):
  Books+Wiki, 100K steps        87.3, 89.0, 95.3
  +additional data, 100K steps  87.7, 89.3, 95.6
  +pretrain to 300K steps       88.7, 90.0, 96.1
  +pretrain to 500K steps       89.4, 90.2, 96.4
Owner:  Liu et al. 2019, Table 4
Scope:  DEV; monotonic gains from data then from training length (the "undertrained" evidence)
```

RoBERTa — Table 5 (GLUE DEV, single-task):
```text
Series (MNLI, QNLI, QQP, RTE, SST, MRPC, CoLA, STS):
  BERT-LARGE   86.6, 92.3, 91.3, 70.4, 93.2, 88.0, 60.6, 90.0
  XLNet-LARGE  89.8, 93.9, 91.8, 83.8, 95.6, 89.2, 63.6, 91.8
  RoBERTa      90.2, 94.7, 92.2, 86.6, 96.4, 90.9, 68.0, 92.4
Owner:  Liu et al. 2019, Table 5
Scope:  DEV; RoBERTa beats BERT-LARGE on every task, largest on RTE (70.4->86.6) and CoLA (60.6->68.0)
```

RoBERTa — data scale:
```text
Figure: pretraining text = 16GB (BERT: BookCorpus + Wikipedia) vs 160GB (RoBERTa, five corpora); batch 8K; byte-level BPE vocab 50K
Owner:  Liu et al. 2019, Sec 3.2
Scope:  RoBERTa uses ~10x the text
```

ELECTRA — Table 1 (small/base, GLUE DEV + train FLOPs):
```text
Series (GLUE dev score; approx train FLOPs):
  ELMo            71.2
  GPT (reimpl.)   78.8
  BERT-Small      75.1   (~1.4e18 FLOPs)
  ELECTRA-Small   79.9   (~1.4e18 FLOPs; 1 GPU, 4 days)
  ELECTRA-Base    85.1   (exceeds BERT-LARGE's 84.0 per Table 1)
Owner:  Clark et al. 2020, Table 1
Scope:  DEV; ELECTRA-Small +4.8 over BERT-Small and +1.1 over GPT at equal/less compute
```

ELECTRA — Table 2 (large, GLUE DEV + train FLOPs):
```text
Series (GLUE dev score; train FLOPs):
  BERT-LARGE     ~84.0
  RoBERTa-100K   ~89.0   (~6.4e20 FLOPs, ~0.9x)
  RoBERTa-500K   88.9    (~3.2e21 FLOPs, ~4.5x)
  XLNet-LARGE    ~89.1   (~3.9e21 FLOPs, ~5.4x)
  ELECTRA-400K   89.0    (7.1e20 FLOPs, 1x baseline)
  ELECTRA-1.75M  89.5    (~3.1e21 FLOPs)
Owner:  Clark et al. 2020, Table 2
Scope:  DEV; ELECTRA-400K matches RoBERTa/XLNet at <1/4 their compute; ELECTRA-1.75M tops them
```

ALBERT — SOP vs NSP (intrinsic, Table 5):
```text
Figure: NSP-trained head on SOP task = 52.0% (near random); SOP-trained head = 86.5% on SOP and 78.9% on NSP
Owner:  Lan et al. 2020, Sec 4.6 / Table 5
Scope:  intrinsic probe; downstream SOP gains ~ +1% SQuAD1.1, +2% SQuAD2.0, +1.7% RACE
```

## Source assets

All figures below must be RECONSTRUCTED as house charts via `nb chart` — arXiv's
non-exclusive license forbids lifting the images. The numeric series above are
preserved so each can be rebuilt. The only verbatim reproduction is the abstract
card (template-mandated).

```text
Asset: BERT Table 1, the GLUE test row block (Devlin et al. 2019).
Shows: One pretrained encoder beats OpenAI GPT (left-to-right) and prior SOTA across 8-9 tasks; this is the durable "bidirectional transfer" evidence.
Crop:  Reconstruct as a grouped bar chart of the Average column (Prior SOTA 74.0, GPT 75.1, BERT-BASE 79.6, BERT-LARGE 82.1) or a per-task panel; caption must state TEST set and that 80.5 is the leaderboard aggregation, distinct from the 82.1 printed average.
```
```text
Asset: BERT Table 5, Section 5.1 pre-training-task ablation (Devlin et al. 2019).
Shows: "the paper's own table foreshadowed it" — dropping NSP costs little, while going left-to-right (LTR & No NSP) collapses MRPC and SQuAD, isolating bidirectionality as the load-bearing choice.
Crop:  Reconstruct as a slope/bar chart, BERT-BASE vs No NSP vs LTR&No NSP across the five tasks; keep SQuAD (88.5 -> 87.9 -> 77.8) which makes the LTR collapse visible.
```
```text
Asset: BERT Table 6, Section 5.2 model-size ablation (Devlin et al. 2019).
Shows: Monotonic downstream gains with size even on small-data tasks; the scaling premise the successors inherit.
Crop:  Reconstruct as a line chart, parameters/#L on x, MNLI-m/MRPC/SST-2 on y; annotate LM perplexity falling 5.84 -> 3.23.
```
```text
Asset: BERT Table 7, Section 5.3 feature-based NER (Devlin et al. 2019).
Shows: Even frozen features (Concat Last Four, 96.1) nearly match fine-tuning (96.4), a point about representation quality, not just the fine-tune head.
Crop:  Reconstruct as a horizontal bar chart of Dev F1; keep the fine-tuning reference line at 96.4.
```
```text
Asset: RoBERTa Table 2, input-format/NSP ablation (Liu et al. 2019).
Shows: The controlled refutation of NSP — no-NSP FULL/DOC-SENTENCES match or beat the NSP rows; SENTENCE-PAIR+NSP is worst, which is the input-format confound made visible.
Crop:  Reconstruct as a grouped bar chart across SQuAD2.0/MNLI/SST/RACE; retain all four rows so the format effect is not hidden.
```
```text
Asset: RoBERTa Table 4, data + training-length ablation (Liu et al. 2019).
Shows: The "BERT was undertrained" evidence — gains keep coming from more data and then more steps at fixed architecture.
Crop:  Reconstruct as a line chart with steps on x (100K->500K) and SQuAD2.0/MNLI/SST on y.
```
```text
Asset: RoBERTa Table 5, GLUE dev vs BERT-LARGE and XLNet (Liu et al. 2019).
Shows: A well-trained BERT recipe beats BERT-LARGE on every task, largest on RTE and CoLA.
Crop:  Reconstruct as a per-task delta chart (RoBERTa minus BERT-LARGE); label DEV.
```
```text
Asset: ELECTRA Figure 1, GLUE score vs pre-training FLOPs (Clark et al. 2020).
Shows: Replaced-token detection sits above MLM at every compute budget; the single clearest picture of MLM's sample inefficiency.
Crop:  Reconstruct as a log-x scatter/line (FLOPs) vs GLUE, plotting the Table 1-2 points (ELECTRA-Small 79.9 @1.4e18; ELECTRA-400K 89.0 @7.1e20; ELECTRA-1.75M 89.5 @3.1e21; RoBERTa-500K 88.9 @3.2e21; BERT-Small 75.1 @1.4e18); keep the log FLOPs axis and note it.
```

## Discarded

```text
URL: https://arxiv.org/html/1907.11692v1 — 404 (no arXiv HTML build for this paper); used ar5iv rendering instead. Not a source, an access note.
URL: https://arxiv.org/html/2003.10555v1 — 404 (no arXiv HTML build); used ar5iv rendering. Access note, not a source.
```
