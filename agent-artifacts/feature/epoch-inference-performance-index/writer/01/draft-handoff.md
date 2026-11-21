# Draft handoff: feature/epoch-inference-performance-index (writer 01)

Original-work sentence: the article recomputes the H100's four per-model scores from the index author's score matrix to show the 25x is a harmonic-weighted mean of ratios from 8x to 217x (59x geometric), splits the 25x into a 13.6x chip-generation step and a 1.85x rack step, and decomposes the rise in capacity per H100e (0.119 to 0.211) into 95% mix shift.

Proof: `nb check ... --series feature` with links, BLOCK 0, WARN 0, PUBLISHABLE. Words 1192 (band 600-1200, so little headroom).

Open evidence question (correction to the record): evidence.md gives per-model GB300/H100 ratios of 43.5x (GLM-5.2), 166.7x (Kimi K3) and 200x (MAI proxy). Those are 1/0.023, 1/0.006 and 1/0.005, rounded scores. From the unrounded scores in `ipi_sens_score_matrix.csv` (0.022619, 0.006303, 0.004604) the ratios are 44x, 159x and 217x; Qwen 8.0x is unchanged. The article uses the recomputed figures, and the recomputed arithmetic (25.2x) and geometric (59.1x) means match the record. The record's "8x to 200x" range is 8x to 217x here.

Choices the editor may check:
- The 1.85x rack step is 1/0.5407; Epoch's text rounds it to "about 1.9x". The article uses 1.85x.
- "Harmonic mean of the ratios" is my identity (mean of scores = 1/harmonic mean of ratios), not Epoch's wording.
- The FP4 effect (about 1.5x) is my division of SemiAnalysis's "up to" 100x and 65x, flagged as "imply".
- The InferenceX compare page carries an "Unofficial deployment" banner; the citation note says its figures are indicative.
- The Data Insight series appears to treat HGX chips at 5.0 PFLOP/s (record, Limits); not used in the article.
- Not used: scatter of FLOP/s against IPI, geometric-mean rescaling of the series (4.58x to about 4.99x), MLPerf, Nvidia's 50x.
