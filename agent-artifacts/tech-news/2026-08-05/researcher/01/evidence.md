# Evidence: tech-news/2026-08-05 (researcher 01)

The strongest, freshest, and most disjoint-from-the-other-desks technology story
for 2026-08-05 is a compressed burst of open-weight frontier model releases in
the first days of August: Alibaba's **Qwen3.8-Max** (Aug 3), Thinking Machines'
**Inkling-Small** open weights (part of the Inkling family), and DeepSeek's
promoted **V4-Flash-0731** checkpoint (Jul 31). The evidence supports *what each
lab announced and claimed* with high confidence, and the general shape of the
week (Chinese and independent labs shipping near-frontier models with open or
soon-open weights, at a fraction of US closed-model price). It is thin exactly
where it matters most: almost every headline benchmark number is **vendor-
published and not independently reproduced**, and for the single most
consequential item (Qwen3.8-Max) the owning primary page (`qwen.ai/blog`) is a
JavaScript-rendered app that the fetcher can only see as the bare word "Qwen," so
its figures are traced through secondaries that faithfully reproduce Alibaba's
own table rather than read off the owner directly. Only DeepSeek carries one
genuinely independent capability signal (Artificial Analysis). Non-model
candidates for Aug 4-5 (a fresh chip launch, a single primary science paper) did
not surface cleanly; the chip and science threads I found are either older or
better owned by current-events. Several adjacent stories are field-shaped but
belong to the other desks this edition (EU AI Act -> opinion; Anthropic
supply-chain ruling and the CareCloud breach -> current-events); they are logged
below as overlaps, not candidates.

## Sources

```text
URL:         https://qwen.ai/blog?id=qwen3.8
Kind:        primary (owner) for what Alibaba announced — BUT NOT DIRECTLY READABLE
Establishes: Alibaba/Qwen's official Qwen3.8-Max announcement and benchmark table
Paraphrase:  This is the owning page for the Qwen3.8-Max claim. The URL resolves,
             but the page is a JS app; the fetcher returns only the string "Qwen"
             with no body. Every Qwen3.8-Max figure below therefore comes THROUGH
             a secondary that reproduces Alibaba's own table, not off this page.
Locators:    blog?id=qwen3.8 (JS-gated; body not machine-readable via fetch)
Quote:       (none obtainable from the primary as loaded)
```

```text
URL:         https://www.marktechpost.com/2026/08/03/alibaba-qwen-releases-qwen3-8-max/
Kind:        secondary (industry press reproducing Alibaba's published table)
Establishes: Qwen3.8-Max specs and the vendor benchmark table, Aug 3 2026
Paraphrase:  Alibaba Qwen released Qwen3.8-Max, a 2.4T-total / 95B-active MoE,
             the most capable Qwen to date; multimodal (text/image/video/docs),
             ~1M-token context (per related coverage). Alibaba's own table reports
             Terminal-Bench 2.1 86.6, SWE-bench Pro 67.7, FrontierSWE 73.5,
             PaperBench 93.0, CoWorkBench 74.8, WideSearch 81.9, positioned near
             GPT-5.6 Sol and Claude Fable 5 / Opus 4.8. Numbers are vendor-reported
             and combine multiple harnesses; not a controlled head-to-head.
Locators:    lead + specs section + benchmark table
Quote:       "The scores are vendor-reported and combine multiple sources and
             harnesses; they should not be read as a single controlled head-to-head."
```

```text
URL:         https://www.testingcatalog.com/qwen-released-qwen3-8-max-with-open-weights-coming-soon/
Kind:        secondary (independent tech outlet)
Establishes: Aug 3 release date; open-weights/license status; autonomous-run demo
Paraphrase:  Qwen3.8-Max announced Aug 3 2026 at 2.4T total / 95B active; open
             weights for Max and a Qwen3.8-27B "scheduled for the following week"
             on Hugging Face and ModelScope, with no license named yet. Cites an
             Alibaba company-run autonomous-coding test (a project "oh-my-cli"
             built over ~16 days) and an e-commerce simulation. Points to
             qwen.ai/blog?id=qwen3.8 as the source.
Locators:    opening + "open weights coming soon" + demo paragraphs
Quote:       "open weights ... scheduled for the following week on Hugging Face and ModelScope"
```

```text
URL:         https://www.bloomberg.com/news/articles/2026-08-03/alibaba-drops-another-china-ai-model-with-breakthrough-performance
Kind:        secondary (reputable US newsroom; independent account, paywalled)
Establishes: Independent confirmation that Alibaba shipped Qwen3.8-Max Aug 3 claiming
             performance rivaling Anthropic
Paraphrase:  Bloomberg reports Alibaba released its largest model, Qwen3.8-Max,
             claiming benchmark scores rivaling Anthropic, ranking above Moonshot's
             Kimi K3. This is independent confirmation of the RELEASE and the CLAIM,
             not an independent reproduction of the benchmarks.
Locators:    headline + lede (full text paywalled)
Quote:       (headline) "Alibaba's Qwen3.8-Max AI Model Claims Benchmark Scores Rivaling Anthropic"
```

```text
URL:         https://huggingface.co/blog/thinkingmachines-inkling
Kind:        primary (Thinking Machines Lab's own HF blog post)
Establishes: Inkling family release, specs, weights repo
Paraphrase:  Thinking Machines Lab released Inkling (975B total / 41B active,
             256-expert decoder-only MoE, 1M context, natively multimodal
             text/image/audio) and a smaller Inkling-Small (276B total / 12B
             active, same architecture, MXFP8/NVFP4 weights). Dated July 15 2026.
             Weights at huggingface.co/thinkingmachines/Inkling (BF16/NVFP4/GGUF).
             Benchmark scores are the lab's own claims vs Gemini/Claude/GPT/DeepSeek.
Locators:    spec section + quantized-variant table + weights link
Quote:       "45 trillion tokens of text, images, audio and video"
```

```text
URL:         https://thinkingmachines.ai/model-card/inkling/
Kind:        primary (Thinking Machines Lab model card)
Establishes: License and Inkling's own-reported evals
Paraphrase:  Inkling model card: Apache 2.0 license; 975B total / 41B active; up to
             1M context; released July 15 2026. Evals reported at effort=0.99:
             AIME 2026 97.1%, SWE-bench Verified 77.6%, GPQA Diamond 87.2%,
             HLE (text only) 29.7%, Global-MMLU-Lite 88.7%, SimpleQA Verified 43.9%.
             The card does not separately state Inkling-Small's parameters or its
             own release date.
Locators:    header (license/params) + evaluations table (effort=0.99)
Quote:       "effort=0.99"
```

```text
URL:         https://thinkingmachines.ai/news/introducing-inkling/
Kind:        primary (Thinking Machines Lab announcement)
Establishes: Positioning/strategy and the Inkling-Small rollout ambiguity
Paraphrase:  Company frames Inkling as "not the strongest model available today,
             open or closed"; the bet is customers fine-tuning it on their own data
             via Tinker (the company's commercial platform) beat generic frontier
             chatbots on their specific work. Page describes Inkling-Small testing
             as "currently finishing" with full weights to follow — i.e., a
             staggered rollout, not a same-day launch.
Locators:    strategy paragraph + Inkling-Small status note
Quote:       "not the strongest model available today, open or closed"
```

```text
URL:         https://www.marktechpost.com/2026/08/02/thinking-machines-lab-releases-inkling-small-276b-open-weights-multimodal-moe-model/
Kind:        secondary (industry press)
Establishes: Reports Inkling-Small full open-weights release ~Aug 2 2026
Paraphrase:  MarkTechPost reports Thinking Machines released Inkling-Small, a 276B
             total / 12B active open-weights MoE, about a quarter the size of
             Inkling (975B/41B). Dates the small-model open-weights availability to
             early August, which conflicts with the July-15 family date on the
             lab's own pages (see Contradictions).
Locators:    headline + first paragraphs (body not machine-readable via fetch;
             specs taken from search-result summary of the same page)
Quote:       (title) "Thinking Machines Lab Releases Inkling-Small: A 276B Total, 12B Active Open Weights Multimodal MoE Model"
```

```text
URL:         https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash
Kind:        primary (DeepSeek model card)
Establishes: The base V4-Flash spec the 0731 build is promoted from
Paraphrase:  DeepSeek-V4-Flash: 284B total / 13B activated MoE; 1M-token context;
             MIT license; FP4 (experts) + FP8 (rest). Card release date April 26
             2026. Card-reported evals: MMLU 88.7 (5-shot), MMLU-Pro 86.4,
             HumanEval 69.5 (pass@1), LiveCodeBench 91.6 (max reasoning),
             LongBench-V2 44.7, SWE-bench Verified 79%. Three effort modes
             (Non-think / Think High / Think Max).
Locators:    model card header + benchmark table
Quote:       "MIT" (license); "284 billion total parameters with 13 billion activated"
```

```text
URL:         https://huggingface.co/blog/ResterChed/deepseek-v4-flash-official-release
Kind:        secondary (community HF blog, NOT DeepSeek-authored)
Establishes: What the Jul 31 "-0731" promoted checkpoint claims to change
Paraphrase:  Describes DeepSeek-V4-Flash-0731 (Jul 31 2026) as a production-candidate
             checkpoint promoted out of the V4 preview line, MIT open weights, same
             284B/13B, 1M in / 384K max out, FP4+FP8, ~166.9 GB on disk. Claims
             large agentic-benchmark jumps over the April preview: Terminal-Bench
             2.1 82.7 (from 61.8), DeepSWE 54.4 (from 7.3), Cybergym 76.7 (from
             38.7). Reports an INDEPENDENT signal: Artificial Analysis put the build
             at 50 on its Intelligence Index, +10 vs the April Flash. Pricing:
             $0.14/M input (cache miss), $0.0028/M (cache hit), $0.28/M output.
             CAUTION: these -0731 figures are from this community post, not confirmed
             on a DeepSeek-authored -0731 model card.
Locators:    benchmark table + "Artificial Analysis" note + pricing block
Quote:       "50 on its Intelligence Index — a 10-point jump over the April Flash"
```

```text
URL:         https://www.theregister.com/systems/2026/07/23/amd-and-cerebras-join-forces-against-nvidias-groq-lpus/
Kind:        secondary (reputable outlet) — LOGGED FOR BREADTH, likely too old
Establishes: AMD-Cerebras disaggregated inference platform (announced Jul 23)
Paraphrase:  AMD tapped Cerebras to build a disaggregated compute platform pairing
             Instinct GPUs with Cerebras SRAM accelerators for ultra-low-latency
             agentic inference, unveiled at Lisa Su's Advancing AI keynote;
             availability via Cerebras Cloud in H2 2026. A systems/chips story, but
             dated Jul 23 — outside the Aug 4-5 window unless a fresh turn appears.
Locators:    lede + availability paragraph
Quote:       "disaggregated compute platform"
```

## Contradictions

- **Inkling-Small release date.** Thinking Machines' own HF blog and model card
  date the Inkling family to **July 15, 2026** and the model card does not list a
  separate Inkling-Small release; the introduction page describes Inkling-Small as
  still "currently finishing" testing with weights to follow. MarkTechPost dates
  the Inkling-Small **open-weights** release to **~Aug 2, 2026**. Most likely
  reconciliation: July 15 was the family announcement / preview, and the small
  model's full open weights landed in early August — but the lab's own pages do
  not state an Aug date, so the "fresh this week" framing rests on the secondary.
  If the writer leads on Inkling-Small as an Aug item, this gap must be stated.

- **DeepSeek V4-Flash date/identity.** DeepSeek's own model card shows **April 26,
  2026** with base evals (HumanEval 69.5, SWE-bench Verified 79%). The Jul 31
  "-0731" build is a *promoted checkpoint of the same 284B/13B model*, not a new
  model, and its headline jumps (Terminal-Bench 2.1 61.8 -> 82.7, DeepSWE 7.3 ->
  54.4) come from a community blog, not a DeepSeek-authored -0731 card. Treat
  "-0731" as a checkpoint refresh whose specific gains are vendor/community-claimed.

- **Qwen3.8-Max: preview vs release.** Coverage split. Alibaba first showed
  Qwen3.8-Max as a **preview** at WAIC Shanghai on **July 19** (qwen3.8-max-preview);
  the **Aug 3** event is reported by some outlets as a full release "with open
  weights coming" and by others as still a shifting preview with weights and
  license not yet posted. As of the research window, weights are **not** on
  Hugging Face and no license is named. The fresh news is the Aug 3 benchmark
  claim and the open-weights promise, not a downloadable frontier model.

- **Benchmark vs independent reproduction (all three models).** Every model above
  reports scores against overlapping suites (Terminal-Bench 2.1, SWE-bench
  Pro/Verified, PaperBench, AIME) but on different harnesses/effort settings and
  with no shared controlled run. The only independent capability signal found is
  Artificial Analysis's Intelligence Index = 50 for DeepSeek-V4-Flash-0731. No
  independent reproduction of Qwen3.8-Max's or Inkling's headline numbers surfaced.

## Numbers

```text
Figure: Qwen3.8-Max — 2.4T total parameters / 95B active (MoE)
Owner:  Alibaba/Qwen (qwen.ai/blog?id=qwen3.8; via MarkTechPost, testingcatalog)
Scope:  model size; active per forward pass. Owner page JS-gated — traced via secondary.
```
```text
Figure: Qwen3.8-Max — Terminal-Bench 2.1 86.6; SWE-bench Pro 67.7; PaperBench 93.0;
        FrontierSWE 73.5; CoWorkBench 74.8; WideSearch 81.9
Owner:  Alibaba's own published table (vendor-reported; no independent reproduction)
Scope:  mixed harnesses; NOT a single controlled head-to-head; open weights not yet out
```
```text
Figure: Qwen3.8-Max — context window ~1,000,000 tokens
Owner:  Alibaba (via secondary coverage; not confirmed on a fetchable primary)
Scope:  input context; flag as unconfirmed-on-owner
```
```text
Figure: Inkling — 975B total / 41B active; Inkling-Small — 276B total / 12B active
Owner:  Thinking Machines Lab (HF blog + model card)
Scope:  MoE, 256 experts; 1M context; Apache 2.0
```
```text
Figure: Inkling — AIME 2026 97.1%; SWE-bench Verified 77.6%; GPQA Diamond 87.2%;
        HLE (text) 29.7%; Global-MMLU-Lite 88.7% (all at effort=0.99)
Owner:  Thinking Machines Lab model card (vendor-reported)
Scope:  effort=0.99 setting; vendor's own evals
```
```text
Figure: DeepSeek-V4-Flash — 284B total / 13B activated; 1M context; MIT
Owner:  DeepSeek model card (April 26 2026)
Scope:  base V4-Flash; -0731 is a promoted checkpoint of the same model
```
```text
Figure: DeepSeek-V4-Flash-0731 — Terminal-Bench 2.1 82.7; DeepSWE 54.4; Cybergym 76.7;
        Artificial Analysis Intelligence Index 50 (+10 vs April)
Owner:  Terminal/DeepSWE/Cybergym = community HF blog (unconfirmed on DeepSeek -0731 card);
        Intelligence Index 50 = Artificial Analysis (independent)
Scope:  agentic suites; only the Intelligence Index figure is independently sourced
```
```text
Figure: DeepSeek-V4-Flash-0731 — $0.14/M input (cache miss), $0.0028/M (cache hit),
        $0.28/M output
Owner:  community HF blog citing DeepSeek pricing (trace to DeepSeek price page before print)
Scope:  per million tokens; cache-hit ~98% discount claim
```

## Source assets

```text
Asset: Qwen3.8-Max benchmark comparison table (on qwen.ai/blog?id=qwen3.8; JS-gated)
Shows: Alibaba's head-to-head positioning vs GPT-5.6 Sol, Claude Fable 5, Opus 4.8
Crop:  If used, must retain the "vendor-reported / mixed harness" caveat and label
       every column as Alibaba's own claim; do not present as a neutral leaderboard.
```
```text
Asset: Inkling quantized-variant / VRAM table (HF blog: BF16 2TB, NVFP4 600GB;
       Inkling-Small BF16 600GB, NVFP4 180GB)
Shows: The concrete hardware cost of running an open 975B vs 276B model — the real
       "what open weights buy you" story a brief reader wants.
Crop:  Keep all four rows so the size/VRAM tradeoff is legible; keep units (GB/TB).
```
```text
Asset: DeepSeek-V4-Flash-0731 preview-vs-0731 delta bars (community HF blog)
Shows: The size of the agentic-benchmark jump between checkpoints.
Crop:  Only usable if relabeled as community/vendor-claimed; the owner (DeepSeek)
       has not published these as a -0731 card, so treat as illustrative, not proof.
```

## Discarded

```text
URL: https://llm-stats.com/llm-updates — aggregator leaderboard; no primary ownership of any figure.
URL: https://benchlm.ai/ , https://pricepertoken.com/news/model-releases — aggregators; numbers not traceable to owners.
URL: https://blog.mean.ceo/... , https://codersera.com/... , https://kie.ai/... , https://coursiv.io/... — SEO/content-farm summaries; several garble dates/params.
URL: https://www.sciencedaily.com/... (hydrogen detonation turbine, Aug 4) — RDE power generation is an ongoing research area, not a single Aug 4-5 primary result; no owning paper dated 08-04/05 confirmed. Not a clean candidate.
URL: https://www.nature.com/nature/articles?year=2026 — no primary research paper dated exactly 08-04/05 confirmed; ghost-ancestor human-DNA and songbird items are ~Jul 31 and were not verified to their owning papers. Science candidate left as a gap, not asserted.
URL: TSMC 2nm / A16 / Arizona capex coverage (fool.com, wccftech, taipeitimes) — manufacturing-capacity and investment news; the "development" is industrial/financial, better owned by current-events; no Aug 4-5 field-level chip result.
```

## Overlaps flagged for the writer (defer to the named desk)

- **EU AI Act GPAI transparency obligations became applicable Aug 2, 2026**
  (AI-disclosure / synthetic-content marking / deepfake labeling). This is the
  **opinion desk's** territory this edition (AI governance). Factual one-line note
  is the ceiling here; the argument is not this brief's.
- **Federal-court ruling that the Trump administration lacked evidence to label
  Anthropic a supply-chain risk**, casting doubt on the government ban. News is a
  **public/policy consequence -> current-events**. Do not file here.
- **CareCloud health-data breach** (hundreds of thousands notified). A public/
  security consequence -> **current-events**. Not a field development.
- **Anthropic hires Tino Cuéllar as Chief Global Affairs Officer (Aug 4)** —
  personnel, not a field development; excluded.
- **No current (this-week) diffusion-model news surfaced**, so there is no clash
  with paper-of-the-day's 2020 DDPM reconstruction.
