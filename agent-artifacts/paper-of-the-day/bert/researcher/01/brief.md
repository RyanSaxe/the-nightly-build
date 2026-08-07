# researcher brief: paper-of-the-day/bert (01)

Inputs:
  ../../editorial-direction.md  — citation standard, reader, series territory
  ../../commission.md           — the paper, the angle, the public record wanted
Output: researcher/01/evidence.md

Research questions (read the cited passages in the primaries):
- BERT (Devlin et al., arXiv:1810.04805): the MLM objective exactly — the ~15%
  masking rate and the 80/10/10 (mask / random / keep) split and the stated
  reason; Next Sentence Prediction (NSP) definition; model sizes (BERT-base
  110M, BERT-large 340M — verify); the GLUE test numbers the claim turns on
  (BERT-large vs prior SOTA / GPT / ELMo); the Section-5 ablations (No-NSP vs
  BERT-base; effect of model size; feature-based vs fine-tuning on NER).
  Identify by table/section number each table the argument uses (for
  reconstruction as house charts) with honest locators.
- RoBERTa (Liu et al. 2019, arXiv:1907.11692): the exact changes (more data,
  longer training, bigger batches, dynamic masking, DROP NSP, longer sequences)
  and the specific finding that BERT was undertrained and NSP unnecessary; the
  head-to-head numbers vs BERT-large. Quote the NSP conclusion precisely.
- ELECTRA (Clark et al. 2020, arXiv:2003.10555): the argument that MLM supervises
  only the ~15% masked tokens (sample inefficiency) and the replaced-token-
  detection alternative; the compute-efficiency comparison figure/number.
- GLUE (Wang et al. 2018): what the benchmark is, enough to label BERT's result
  honestly.
- Contradictions: BERT's NSP claim vs RoBERTa's refutation; the MLM-efficiency
  critique; any later nuance (e.g. whether NSP-vs-SOP or data confounds the
  RoBERTa comparison). Record who owns each.
min_sources 8, prefer primary. Verify every number against its owning paper;
record honest locators (section/table). Resolve each URL to the paper's own
page (arXiv abs / ACL Anthology). Note: arXiv non-exclusive license — figures
must be RECONSTRUCTED as charts, not lifted; preserve the numeric series the
writer needs for that.
