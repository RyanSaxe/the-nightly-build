# Draft handoff: feature/mlperf-grpo-post-training (writer 01)

## Original work

The article sets the rules' earliest-evaluation formula, ⌈2.5 + 3,840/GBS⌉, beside the stopping step of all 87 scored runs and 24 reference runs. That shows each v6.1 GRPO minute is the wall time of a fixed number of GRPO steps with the whole loop on the clock. It then recomputes NVIDIA's same-chip, same-backend scaling series in accelerator-minutes and checks the three vendor headline comparisons against the official rows for what each leaves free.

## Proof

`nb check ... --series feature --repo /home/user/the-nightly-build`, links included: BLOCK 0, WARN 0, verdict PUBLISHABLE. Stamped at 1,193 words (band 600–1,200), 11 sources, 5 min.

Warnings left on purpose: none.

Visuals: Fig. 1 (inline SVG of the timed loop), two tables, and Fig. 2 (`chart-1.py` → `chart-1.png`). Captured with Playwright after `nb preview` at 390 px and 1,280 px, in light and dark. Neither width scrolls the page horizontally. The vendor-claims table scrolls inside its own wrapper on a phone, as the runtime intends. Because the chart renderer exports at a fixed 1,200 px layout, I set the chart fonts to 22–24 so labels stay legible at phone width. They look large on a desktop.

## Display text checked

- Headline "stops every clock at the earliest step allowed": all 87 scored runs stopped at samples_count 5,120 (GBS 512) or 6,912 (GBS 1,152), the first eligible checkpoint (evidence, training_results_v6.1 entry).
- Dek: 87 runs, Qwen3.5-397B, 0.69 pass@4 and first allowed checkpoint all come from the record. "Fixed quota" is per batch size. The TPU entry's different quota appears in the body and in two tables. The nb-meta dek and the dekline are identical.
- Subheads: "Sixteen times the GPUs for a threefold speedup" is GB300 vLLM 64 → 1,024 GPUs, 42.48/13.78 = 3.08 (6.1-0035, 6.1-0031).
- Recent habits avoided: no "X averages/reveals N of M" headline, no person-plus-contrast dek, and the opening states the finding first.

## Open evidence questions

- Accelerator-minutes in the Numbers section do not all equal the rounded score × count. For example, 13.78 × 1,024 = 14,110.7 against the record's 14,113, and 10.44 × 1,024 = 10,690.6 against 10,696. I used the record's figures exactly and never wrote a product the reader would recompute differently. The researcher should confirm whether they came from unrounded minutes.
- I left two contradictions out of the prose because neither carries the argument. The README's "140 to 160 minutes" reference runtime is not the same quantity as a score. NVIDIA's "22,500 concurrent RL environments" is a capability claim. The editor may want one sentence on the first.
- The SVG says "Apptainer box" so the text fits the panel. The record says container.
