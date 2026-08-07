# writer brief: paper-of-the-day/bert (01)

Inputs:
  ../../editorial-direction.md            — house/press/template/series standard
  ../../commission.md                     — the paper, the angle, the verdict
  ../../writing-coach/01/voice-guide.md   — craft (reviewer cross-examining tables)
  ../../researcher/01/evidence.md         — the complete claim set; cite only this
  ../../../../library/paper-of-the-day/bert.html   — the initialized article
  ../../../../.nb-context/                 — effective template contract + furniture
Output: writer/01/draft-handoff.md
Proof:  ./nb check .nb-work/paper-of-the-day/bert/library/paper-of-the-day/bert.html --series paper-of-the-day --library /home/user/library-checkout

Framing precision the evidence record enforces (a wrong version here is a false
central claim):
- The NSP "unnecessary" claim is ENTANGLED. BERT's own No-NSP ablation (Table 5)
  kept the SEGMENT-PAIR input and dropped only the loss; RoBERTa's gain appears
  only once it ALSO switches to FULL/DOC-SENTENCES inputs. Cite RoBERTa TABLE 2
  (matched-data isolation) for the NSP claim — not the five-changes-at-once
  headline model. Support the convergence with ALBERT (a plain NSP head scores
  52.0%, chance, on sentence-order) and BERT's own Table 5 (NSP's largest effect
  is only QNLI 88.4→84.9).
- Bidirectional MLM is load-bearing: the "LTR & No-NSP" ablation collapses
  (MRPC 86.7→77.5, SQuAD 88.5→77.8) — use it to isolate bidirectionality.
- MLM inefficiency is real: ELECTRA supervises all tokens vs MLM's ~15% and
  reaches comparable GLUE at under 1/4 the compute (ELECTRA-400K 89.0 vs
  RoBERTa-500K 88.9). XLNet-vs-RoBERTa supports "undertrained, not out-designed."
- NUMBER HYGIENE: never compare BERT's TEST/leaderboard numbers (Table 1, 80.5)
  to DEV numbers used elsewhere; Table 1's printed "Average" 82.1 excludes WNLI
  and is not the 80.5 leaderboard score. Keep dev and test separate and labeled.

Figures / source assets (licensing): arXiv non-exclusive license — do NOT lift
figure images. RECONSTRUCT the comparisons the claim turns on as ORIGINAL house
charts via nb chart from the evidence's preserved series (the LTR&No-NSP ablation
collapse; the NSP convergence; the ELECTRA GLUE-vs-FLOPs efficiency curve).
Inspect each rendered chart; cite the data source in the caption. The abstract
card reproduces the paper's abstract verbatim per the template contract; every-
thing else is your own reconstruction and order.

Craft (voice guide): set the MLM objective inline and operate on it (why masking
breaks the left-to-right factorization); put each table "on trial" as a claim
under test with the competing hypothesis named; use the "the paper's own Table 5
foreshadowed it" move for NSP. Verdict before Sources: bidirectional MLM transfer
was the durable contribution; the NSP claim did not survive; MLM's ~15%-supervision
inefficiency was a real limit that motivated successors. Habits to break: no
author roll-call opener; avoid the "every later model inherited…" closer and
comma-triad deks.
