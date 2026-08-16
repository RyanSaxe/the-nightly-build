# Draft handoff: tech-news/2026-08-16 (writer 01)

## Original-work sentence
For each of four selected developments the article names the one thing that
changed in how these systems get built or trusted, and for the two model
releases it demotes the headline benchmarks to what they actually are, the
labs' own unverified figures, stating the verification gap the announcements
leave out.

The work is visible in each item's closing "The change is..." line and in the
self-report caveats on the Qwen and GLM-5.3 items.

## Items selected (4 of 7 candidates)
Chose on significance and refused to pad to six; the weekend produced no major
primary release, so the desk carries the freshest consequential work of 12-14
August.

1. Qwen3.8-27B (single lead, named in the headline) — 27B multimodal model on a
   single GPU via a 3:1 linear-to-full attention interleave.
2. Anthropic text watermarking + C2PA — the most consequential decision;
   provenance moves into the text itself, no opt-out.
3. GLM-5.3 — a large coding gain from post-training on the unchanged GLM-5.2 base.
4. Gladstone/UCSF in vivo CRISPR screen in human T cells — two genes whose
   knockout lifts solid-tumor resistance to CAR-T.

Dropped: the Nvidia 13F/SpaceX item (a passive equity disclosure, not a change
in technical practice, and it would have required an EDGAR verification the
researcher had not done), and the DeepSeek V4-Pro GA (on the do-not-repeat
list).

## Selection cautions honored
- Every benchmark is marked as a lab self-report with the verification gap
  stated: Qwen ("Those are the lab's figures. No independent evaluator had
  posted verified results by 16 August") and GLM-5.3 ("These too are the lab's
  own numbers... analyst judgment").
- Anthropic's own caveat is carried in its words: the mark shows only "likely
  involved" and "cannot distinguish 'Claude wrote this' from 'Claude heavily
  edited this.'"
- No do-not-repeat item reused; DeepSeek V4-Pro left out.
- Headline names the single lead and leads with the concrete result (single-GPU
  27B model); no triad-of-topics.
- Each item's "why it matters" states what changed in the technical picture, not
  that a company shipped.

## Proof result
`./nb check ... --series tech-news --library <scratchpad checkout>` (links on):
BLOCK: 0, WARN: 0. Verdict PUBLISHABLE. `nb stamp` written: words 814,
reading_minutes 4, sources 9. nb-meta dek is identical to the rendered dekline.
No warnings intentionally left.

## Furniture
One stat strip on the lead item (27B dense parameters, 262K to 1M context, 3:1
linear-to-full blocks), each figure cited to the model card in adjacent prose.
Held to one component so the piece reads as a wire brief, not a stack.

## Open evidence question
The single-GPU footprint (~24-28 GB at 8-bit) is a deployment estimate bundled
from the model card and specialist runbook accounts, not a measured benchmark;
I framed it as an estimate at reduced precision. If the editor wants a
hard-measured VRAM figure, none was in the evidence record. Independent
verification of the Qwen and GLM-5.3 scores did not exist at press time, so no
verified number is available to substitute for the self-reports.
