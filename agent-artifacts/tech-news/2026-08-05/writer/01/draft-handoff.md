# Draft handoff: tech-news/2026-08-05 (writer 01)

## Status: BLOCKED before drafting — needs an orchestrator/researcher decision

I did not draft the article or run `nb stamp`/`nb check`, because the evidence
cannot honestly fill a band-compliant `brief` (template floor is 4 items, per
`.nb-context/template-contract.yaml` `bands.items: [4, 6]`). The blocker is a
continuity collision the evidence record did not flag, which I found by running
the specific history check the commission asked for.

## What I found (verified via `nb history` against the run's library checkout)

The brief names the spine as three model items — **Qwen3.8-Max**,
**Inkling-Small**, **DeepSeek-V4-Flash-0731**. Two of the three were already
published as full items **yesterday**, in `tech-news/2026-08-03`, off the same
primaries and secondaries in this evidence record:

- **DeepSeek-V4-Flash-0731** — 08-03 item "DeepSeek's V4-Flash-0731 posts
  frontier-adjacent coding scores at cents per million tokens." Same facts (MIT,
  284B/13B, 1M context, $0.14/M in · $0.28/M out, Terminal-Bench, the Artificial
  Analysis signal). Same sources (DeepSeek HF card, ResterChed HF blog,
  MarkTechPost). The evidence supplies **no post-08-03 development**.
- **Inkling-Small** — 08-03 item "Thinking Machines' Inkling-Small beats its
  larger teacher on five of six benchmarks." Same facts (276B/12B, Apache 2.0,
  256 experts, HLE/SWE-bench Verified 80.2 vs 77.6/GPQA/IFBench, AIME 95.5 vs
  97.1). Same sources (TML model card, MarkTechPost). **No post-08-03
  development** in the evidence.

The commission's boundary is explicit: "Do not re-file an already-covered
release/result as new." Re-filing either as a new 08-05 item would violate it,
and the template's "say so and build on it" license needs an actual development
to build on, which the evidence does not supply for either.

That leaves exactly **one** genuinely-new, uncovered, source-clearing field
development for 08-05:

- **Qwen3.8-Max** (Alibaba, Aug 3). Primary = `qwen.ai/blog?id=qwen3.8` (owner,
  JS-gated). Independent secondary = Bloomberg (confirms the *release* and the
  *claim* of rivaling Anthropic), plus MarkTechPost/testingcatalog reproducing
  Alibaba's own table. It clears the per-item source rule (1 primary + ≥1
  independent secondary). Note: the benchmarks are **vendor-only, with no
  independent reproduction** (per evidence Contradictions) — they would be
  attributed to Alibaba's table, never printed as fact. Its own history: the
  July 19 WAIC *preview* was noted in `the-wire/2026-07-21`; the Aug 3 benchmark
  table and open-weights promise is the new turn to build on.

No other qualifying item exists in the evidence. The researcher's own lede says
the non-model Aug 4-5 candidates (a fresh chip launch, a single primary science
paper) "did not surface cleanly." AMD-Cerebras is dated Jul 23 and flagged "too
old." Everything else is discarded (aggregators) or deferred to other desks
(EU AI Act → opinion; Anthropic supply-chain ruling and CareCloud → current-events).

**Net: 1 fileable new item vs. a template floor of 4.** I cannot reach a
band-compliant, honest brief without either re-filing two already-covered stories
as new (commission-forbidden) or padding/inventing items (standard-forbidden), so
I stopped rather than write around the hole.

## Decision needed, and its owner

One of the following, none of which is the writer's to make:

1. **Researcher (new artifact):** supply at least three additional
   genuinely-new, shelf-uncovered Aug 4-5 field developments (model, chip,
   systems, or scientific result), each clearing 1 primary + ≥1 independent
   secondary, so a 4-item brief can be built around Qwen3.8-Max. This is the
   clean fix; the current evidence set is effectively exhausted by the 08-03
   edition.

2. **Orchestrator/commission:** re-scope this edition. Either confirm the brief
   is meant as a "surge develops" build-on piece led by Qwen3.8-Max (and rule on
   whether, and how, the 08-03 DeepSeek/Inkling items may be *referenced* as
   established context without being re-filed as new items) — noting the 4-item
   band floor is a hard proof gate that a build-on framing alone does not
   satisfy — or authorize a different template/band for a single-development day.

## Original-work sentence (would apply if Qwen3.8-Max is filed)

Reading Alibaba's own Aug 3 table beside Bloomberg's confirmation-of-claim, the
piece would separate what Alibaba *announced* (a 2.4T/95B model it says rivals
Anthropic) from what is *independently established* (only that it shipped and
made the claim — no benchmark has been independently reproduced), and place that
gap where the numbers are rather than in a trailing caveat.

## Proof result

None. No article was drafted, so `nb stamp` and `nb check` were not run. A 1-item
article cannot reach `BLOCK: 0` against the `[4, 6]` band regardless.

## Open evidence/voice questions for the orchestrator

- The primary open question is the item count above (decision needed).
- Voice/sourcing note if Qwen3.8-Max proceeds: with benchmarks vendor-only and
  no independent reproduction, the interval-anchored-figure and magnitude-
  conversion licenses have little to bite on for this item (no published margins,
  no independent delta). The honest item is mostly attribution discipline plus
  the marked-inference license — worth confirming that a Qwen-led piece is not
  expected to carry converted-ratio devices it has no independent numbers for.
