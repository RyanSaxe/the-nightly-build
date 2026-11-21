# Commission: feature/epoch-inference-performance-index

Run date: 2026-11-21. Scheduled duty, open section, no commissions supplied.
Template: article. Strict word band 600–1200, 2–4 flexible sections, at least 5 sources.

## The story

Epoch AI published an Inference Performance Index (IPI) for AI accelerators
(methodology report dated 9 November 2026,
https://epoch.ai/publications/inference-performance-index) and a Data Insight on
18 November 2026 (https://epoch.ai/data-insights/agentic-inference-capacity-growth)
with a CC-BY CSV of installed inference capacity by chip family per quarter. The
headline claim the scouting found: a GB300 delivers roughly 25 times an H100's
per-chip inference capacity on about 2.5 times its 8-bit FLOP/s, so FLOP/s counts
understate how fast inference capacity is growing. Treat every figure here as
unconfirmed until the researcher opens the primary.

Why now: the index and the capacity series are days old, and FLOP/s remains the
unit almost every public compute comparison uses.

## The angle to test

The piece should show readers why per-chip inference throughput and FLOP/s
diverge (memory bandwidth, interconnect / scale-up domain size, low-precision
formats, batch and latency regime), using the IPI's own construction, and what
that divergence does to an estimate of installed inference capacity growth.

Candidate original work, to be confirmed or killed by the evidence:
1. Recompute from the CSV the capacity growth Epoch reports in IPI units against
   FLOP/s units, and show how much of the gap comes from mix shift toward
   Blackwell-generation chips.
2. Test the IPI's sensitivity to its own aggregation choice: the report reportedly
   says an arithmetic mean of its component ratios flatters some chips relative to
   a geometric mean. If the report gives component scores, recompute.

Disconfirming evidence to look for: anything showing the IPI's scenarios are
dominated by one regime (e.g. a single interactive-latency target) or that
vendor benchmark numbers (InferenceMAX/SemiAnalysis, MLPerf Inference) put the
GB300/H100 ratio far from Epoch's. If the 25x/2.5x framing does not survive
the primary, follow what the primary does support.

## Visuals

Each section is built around a visual: e.g. a scatter of FLOP/s against IPI per
chip, a drawing of how the index is computed (the curve, the area ratio, the
averaging), and the capacity series in both units. Charts come from the
researcher's verified series via `nb chart`. Prefer the mechanism drawing to a
plain bar chart where it fits.

## Boundaries

- Do not cover AI-company financing, debt, or compute spend (covered 19 Nov).
  Do not revisit TOP500 (covered 20 Nov); one sentence of contrast at most.
- Five-minute read: open with the finding in two or three sentences.
- Name the organisation and the authors exactly as the report credits them.

## Recent patterns to break

- Recent feature headlines lead with a ratio or count against a second quantity
  ("Supplier orders outweigh credit guarantees nearly four to one", "Oil's drop
  is bigger than ..."). Avoid another "X outweighs/exceeds Y" comparison headline.
- Recent deks chain two clauses of figures joined by "so" or a comma and a
  second figure. Write a different dek shape.
- Section headings in the last two features were all full declarative sentences
  with a date or count ("Commitments passed debt in 2024 and reached 3.5 times
  it by mid-2026"). Vary the construction.

## Neighbours in tonight's edition

The daily brief (news and two technology items) and an RL lesson on reward scale.
The brief must not lead a technology item with Epoch's index; the brief's
researcher is told so.

## Production record

Balanced profile: writing coach capable/low, researcher capable/high, writer
capable/high (series override), editor inherit/high (required). Runtime: capable
tier runs as Sonnet; editor on the orchestrator's model.

## Decisions after drafting

- Per-model GB300/H100 ratios: the writer recomputed from the unrounded score
  matrix (GLM-5.2 44x, Kimi K3 159x, MAI proxy 217x; Qwen 8.0x; means 25.2x
  arithmetic, 59.1x geometric), superseding the evidence record's rounded
  figures. The editor verifies these against Epoch's primary before approval.
- Editor (01) verified the recomputed ratios against Epoch's score matrix and
  corrected two evidence-record errors in the article: SemiAnalysis's 65x at
  116 tok/s/user is tokens per dollar, not throughput; the InferenceX
  "Unofficial deployment" banner is an off-site embedding artifact, so the
  figures are treated as SemiAnalysis's published results. Settled.
