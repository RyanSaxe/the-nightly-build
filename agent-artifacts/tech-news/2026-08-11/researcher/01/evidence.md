# Evidence record: tech-news/2026-08-11 (01)

The Aug 10–11 news cycle was dominated by AI, and the evidence supports four
day-anchored items with verifiable primaries: Meta's open-weight Muse Glimmer
30B (model card and benchmark table read firsthand), OpenAI's GPT-5.6-Cyber and
the two chained Chrome V8 bugs it found (CVE-2026-15903), Anthropic's unreleased
Claude raising the proven lower bound for Riemann zeta zeros on the critical line
from 41.6% to 67.2% (Anthropic's own writeup read firsthand, with a Lean 4
proof), and a USTC/Hefei silicon-photonic chip that built a 4-photon 16-qubit
GHZ state and ran Grover's algorithm at 0.987 identification probability (arXiv
preprint 2608.03012, full text read and every figure confirmed). Two of the four
carry a real handling caveat: OpenAI's own announcement page is gated (HTTP 403),
so its numbers are verified only through secondary reporting that quotes OpenAI,
and every Muse Glimmer benchmark is Meta's own self-report on a benchmark set
Meta chose. The evidence is thin where the commission most wants balance: a
genuinely consequential, day-anchored science or health primary was hard to find.
The strongest non-AI candidates either predate 11 August (the aleniglipron oral
GLP-1 trial is a June result being re-surfaced) or are events rather than
advances (the Long March 7A failure is real but lacks an official primary and
does not clearly change technical knowledge or practice). The photonic-quantum
preprint is the one solid non-AI item. Two much-hyped space stories did not hold
up: the Zhuque-3 second landing attempt has no confirmed outcome, and the widely
repeated claim that the Long March failure postponed it is unverified.

## Sources

### 1. Meta Muse Glimmer 30B (open-weight agentic model)

```text
URL:         https://huggingface.co/meta-models/Muse-Glimmer-30B
Kind:        primary — Meta's own model card and benchmark table on Meta's
             Hugging Face org; Meta owns and reports these numbers
Establishes: the model's size, license, memory envelope, and Meta's full
             self-reported benchmark table against two named competitors
Paraphrase:  Muse Glimmer-30B is a ~29.6B-parameter dense causal transformer
             with a perception encoder, Apache 2.0, 131,072+ context, trained on
             100+ languages, released August 2026. Full precision needs 64GB
             VRAM; a K-Quant-Dynamic build runs in 32GB with 0.2% degradation
             and a K-Quant-17GB build in 24GB with 1.0% degradation. On Meta's
             table it wins about half of 24 benchmarks against Gemma4-31B and
             Qwen3.6-27B and loses the other half.
Locators:    model card header (specs) and the "Benchmarks" comparison table
Quote:       "K-Quant-Dynamic | 32GB VRAM (0.2% degradation)"; table rows incl.
             "SWE-Bench Pro | 51.2 | 36.9 | 50.2" and "GDPVal-AA v2 | 953 | 811
             | 1141" (Glimmer | Gemma4-31B | Qwen3.6-27B)
```

```text
URL:         https://siliconangle.com/2026/08/10/meta-releases-open-source-muse-glimmer-model-30b-parameters/
Kind:        secondary — US technology newsroom reporting on Meta's release
Establishes: independent account of the release date and framing; corroborates
             size and the 4-bit memory reduction
Paraphrase:  Reports an August 10, 2026 release of the 30B model, notes the full
             footprint of "about 55 gigabytes of RAM" cut to "under 20
             gigabytes" via 4-bit quantization, and that Meta claimed Glimmer
             outperformed the comparably sized Gemma4-31B and Qwen3.6-27B "across
             half the benchmarks." Offers no independent benchmark verification.
Locators:    lede and body
Quote:       "outperformed the comparably-sized Gemma4-31B and Qwen3.6-27B across
             half the benchmarks"
```

Note the VRAM discrepancy: the model card (primary) states 64GB full precision,
while Meta's blog framing quoted by secondaries says ~55GB reduced to under 20GB.
Record the model card's figures as owning the claim.

### 2. OpenAI GPT-5.6-Cyber and the Chrome V8 bugs (AI + security)

```text
URL:         https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/
Kind:        primary — OpenAI's own announcement; owns the model claim and the
             vulnerability-discovery claim
Establishes: this is the address where OpenAI's announcement lives; it is the
             primary the article should link
Paraphrase:  Not read firsthand. The page returns HTTP 403 to automated fetch
             (gated, not dead). Its content is corroborated below through
             secondary reporting that quotes OpenAI directly.
Locators:    n/a — not opened
Quote:       none (not opened)
```

```text
URL:         https://the-decoder.com/openai-launches-gpt-5-6-cyber-to-help-defenders-find-vulnerabilities-before-attackers-do/
Kind:        secondary — technology newsroom, quoting OpenAI's figures
Establishes: the specific figures OpenAI reported: the CVE, the completion-rate
             benchmark, and the other disclosed vulnerabilities
Paraphrase:  GPT-5.6-Cyber (built on GPT-5.6 Sol) found two previously unknown
             Chrome V8 bugs that chain to corrupt memory and bypass the V8 heap
             sandbox, assigned CVE-2026-15903. On OpenAI's internal "Advanced
             Cybersecurity Completion Rate" it answered 95% of sensitive
             security queries, vs GPT-5.5-Cyber 57.3%, GPT-5.6 Sol 1.5%, and
             Daybreak Blue 2%. It also found at least five bugs in a popular
             mobile OS. Rated "High" but not "Critical" under OpenAI's
             Preparedness Framework. Access is gated behind Daybreak Red
             (identity verification, monitoring, legal declarations; hardware
             security keys mandatory from Sept 1, 2026). Article dated Aug 10.
Locators:    body, benchmark paragraph and "Chrome" paragraph
Quote:       "assigned CVE-2026-15903"; "95% ... compared to GPT-5.5-Cyber's
             57.3%, standard GPT-5.6 Sol at 1.5%, and Daybreak Blue's 2%"
```

```text
URL:         https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/
Kind:        secondary — US newsroom (TechCrunch)
Establishes: an independent US account that the launch happened and who the
             early partners are; does NOT carry the CVE or benchmark figures
Paraphrase:  Reports the Daybreak expansion and names trusted partners
             (Accenture, IBM, CrowdStrike, Cloudflare, and others). Contains no
             CVE, no V8 detail, and no 95% figure.
Locators:    body
Quote:       partners listed as "Accenture, IBM, Crowdstrike, Cloudflare, and
             others"
```

Handling caveat: the CVE and the completion-rate numbers originate from OpenAI's
own account. The V8 fix/CVE was not confirmed against a Google/Chrome primary in
this pass. Treat the "two chained V8 bugs" and the 95% as OpenAI's claim,
verified only as far as OpenAI's own reporting.

### 3. Anthropic — Claude raises the Riemann zeta critical-line lower bound

```text
URL:         https://www.anthropic.com/research/riemann-zeta
Kind:        primary — Anthropic's own research writeup; owns the claim
Establishes: the bound improvement, the compute used, the human verification,
             the Lean proof, and Anthropic's explicit limitation
Paraphrase:  An unreleased research version of Claude increased the proven lower
             bound for the fraction of Riemann zeta zeros satisfying the
             hypothesis from 41.6% to 67.2%. The run used 31 million output
             tokens across two sessions and about 60 Claude subagents. Anthropic
             mathematicians Levent Alpöge and Ralph Furman verified it; external
             experts Brian Conrey and Dan Goldston examined it. Claude produced a
             formally verifiable (Lean) proof. Anthropic states it does not
             expect these techniques to prove the full hypothesis.
Locators:    result summary and methods/limitations paragraphs
Quote:       "We don't expect that the techniques Claude used will lead to
             proving the Riemann hypothesis."
```

```text
URL:         https://cryptobriefing.com/claude-riemann-zeta-lower-bound-67-percent/
Kind:        secondary — independent outlet reporting Anthropic's announcement
Establishes: independent corroboration of the two bound figures and the "largest
             improvement in the history of the problem" framing and the caveat
Paraphrase:  Dated August 10, 2026. Confirms 41.6% -> 67.2% (a 25.6-point gain),
             frames it as the single largest improvement to this bound, and
             states plainly it is not a proof of the full hypothesis (which needs
             100% and a Clay Millennium Prize). Does not carry the token or
             subagent counts.
Locators:    body
Quote:       "the single largest improvement to this particular bound in the
             history of the problem"
```

This item develops the AI-does-frontier-math thread the desk already covered
(OpenAI Astra/Lean proofs, 08-04 and 08-10): a different lab, a different open
problem, again with a machine-checkable Lean certificate. A stronger US-newsroom
secondary than Crypto Briefing likely exists and would be preferable if the
writer runs this.

### 4. USTC / Hefei photonic chip — 4-photon 16-qubit GHZ state, Grover at 0.987

```text
URL:         https://arxiv.org/abs/2608.03012
Kind:        primary — the preprint itself; owns every measured figure
Establishes: title, authorship, submission date, and the claimed advances
Paraphrase:  "On-chip generation of multi-qubit graph states with high-
             dimensional encoded single photons." Authors incl. Lan-Tian Feng,
             Guo-Ping Guo, Guang-Can Guo, Xi-Feng Ren (USTC quantum-photonics
             group). Submitted August 4, 2026. Demonstrates on-chip GHZ and
             cluster graph states and a Grover search on a single-photon cluster
             state.
Locators:    abstract and metadata
Quote:       title as above
```

```text
URL:         https://arxiv.org/html/2608.03012
Kind:        primary — full text of the same preprint (figures read firsthand)
Establishes: the exact measured quantities
Paraphrase:  Four spiral silicon waveguides act as photon-pair sources; a
             4-photon GHZ state is built, then each photon encodes four qubits to
             reach a 4-photon 16-qubit GHZ state. Genuine 10-qubit entanglement
             is confirmed at >11 sigma, stated as the largest entangled state
             demonstrated so far on a photonic chip. The 4-qubit single-photon
             cluster state reaches fidelity 0.991(0.004); the 4-qubit GHZ
             fidelity 0.961(0.003) is called the highest for 4-qubit states on an
             integrated optical chip. Grover search over four targets reaches
             average identification probability 0.987(0.003). The 10-qubit GHZ
             brightness is 0.154 Hz, versus an infeasible 1.1e-15 Hz for
             classical dual-rail encoding.
Locators:    results sections (GHZ generation; cluster state; Grover)
Quote:       "a 4-photon 16-qubit GHZ state is achieved"; "confirms the genuine
             10-qubit entanglement, which is the largest entangled state
             demonstrated so far in photonic chips"; "the average identification
             probability of 0.987(0.003) is achieved"
```

```text
URL:         https://thequantuminsider.com/2026/08/10/sizhen-chip-multi-qubit-photonic-quantum-states-silicon-chip/
Kind:        secondary — quantum-industry outlet; independent account
Establishes: the commercial actor behind the work and the arXiv identifier;
             corroborates the headline figures
Paraphrase:  Attributes the chip to "Hefei Sizhen Chip Technology Co., Ltd.," a
             USTC spinout, links arXiv 2608.03012, and repeats the 4-photon
             16-qubit GHZ, 10-qubit witnessed entanglement, and 0.987 Grover
             figures. The company frames it as a path toward million-qubit
             optical quantum computing.
Locators:    body
Quote:       company named as "Hefei Sizhen Chip Technology Co., Ltd."
```

Name discrepancy to resolve before print: this outlet and the preprint context
give the company as "Sizhen Chip," while other coverage (Pandaily, SecondTalent)
calls it "Guizhen Chip." The arXiv author list carries the academic names, not a
company affiliation I could read. Use the company name only if the writer can
confirm the correct transliteration from the company's own page; the science is
attributable to the USTC group regardless.

### 5. Long March 7A launch failure (marginal — event, not advance)

```text
URL:         https://spacenews.com/chinese-long-march-7a-rocket-explodes-shortly-after-liftoff/
Kind:        secondary — space-industry newsroom; independent account
Establishes: that a Long March 7A failed shortly after liftoff, with payload,
             timing, and flight-history context
Paraphrase:  A Long March 7A carrying the Zhongxing-4B military communications
             satellite exploded roughly 85 seconds after liftoff from Wenchang,
             Hainan, at about 12:00 UTC on August 10, 2026. It was China's 56th
             orbital launch attempt of 2026 and the fourth failure. The 7A first
             flew in March 2020, also a failure; its most recent prior flight was
             a Tianlian-3 launch in late July 2026. As of reporting, Chinese
             authorities had not officially reported the failure. The article
             notes the second Zhuque-3 was scheduled to launch later Aug. 10 but
             records no confirmed link to this failure.
Locators:    body
Quote:       "exploded around 85 seconds into the flight"; "Chinese authorities
             had yet to report the incident as of time of reporting"
```

Two cautions on this item. First, there is no primary yet: no official Xinhua or
CASC failure statement had been issued when SpaceNews reported, so the failure
rests on observer footage and independent reporting, not an owning source. Second,
a launch failure is an event, not a change in technical knowledge or practice,
so it sits at the edge of this desk's remit and overlaps what a general news desk
would cover. Runnable only if the writer can add an official primary and justify
the significance; otherwise it just clears the bar at best.

## Contradictions

- **Zhuque-3 second landing attempt — no confirmed outcome.** Pre-launch
  coverage (Space.com, AIAA, NASASpaceflight) targeted liftoff and a booster
  landing for ~23:45 UTC Aug 10 / 07:45 Beijing Aug 11. One aggregator claimed
  the Long March 7A failure postponed it; SpaceNews, reporting around the same
  window, still listed Zhuque-3 as "scheduled to launch later Aug. 10" and drew
  no link. No source I opened records whether Zhuque-3 flew, landed, or slipped.
  Treat the outcome as unknown and do not assert the postponement causation.
- **Muse Glimmer memory footprint.** Model card (primary): 64GB full precision.
  Meta blog framing via secondaries: ~55GB reduced to under 20GB. Both are
  Meta's; the model card owns the number.
- **Long March 7A date framing.** SpaceNews times the failure at ~12:00 UTC
  Aug 10 (evening Beijing Aug 10 / still Aug 10 US). Some outlets headline it
  "Aug 11" on Beijing local framing. Same event; state the UTC time.
- **Company name Sizhen vs Guizhen** (see item 4).
- No source contradicts the core figures of items 1–4 as recorded; the Meta and
  OpenAI numbers are self-reported, which is a sourcing limit, not a
  contradiction.

## Numbers

```text
Figure: 67.2% (up from 41.6%) — proven lower bound, fraction of Riemann zeta
        zeros satisfying the hypothesis
Owner:  Anthropic (anthropic.com/research/riemann-zeta)
Scope:  a proven analytic lower bound, not a probability; full proof would need
        100%. Produced by an unreleased Claude; 31M output tokens, 2 sessions,
        ~60 subagents; Lean-verified; human-checked by 4 named mathematicians
```

```text
Figure: 0.987(0.003) — average Grover-search identification probability
Owner:  arXiv 2608.03012 (USTC / Hefei group)
Scope:  averaged over four target items, single-photon 4-qubit cluster state, on
        a room-temperature silicon-on-insulator photonic chip
```

```text
Figure: 4-photon 16-qubit GHZ state; genuine 10-qubit entanglement at >11 sigma
Owner:  arXiv 2608.03012
Scope:  each of 4 photons encodes 4 qubits; 10-qubit witnessed entanglement is
        stated as the largest yet on a photonic chip; brightness 0.154 Hz
```

```text
Figure: 95% advanced-cybersecurity completion rate (vs 57.3% / 1.5% / 2%)
Owner:  OpenAI (reported via the-decoder; OpenAI page gated)
Scope:  OpenAI internal "Advanced Cybersecurity Completion Rate" benchmark;
        comparators GPT-5.5-Cyber, GPT-5.6 Sol, Daybreak Blue
```

```text
Figure: two Chrome V8 vulnerabilities, CVE-2026-15903
Owner:  OpenAI (reported via the-decoder); Chrome/Google primary not checked
Scope:  chained to corrupt memory and bypass the V8 heap sandbox
```

```text
Figure: 30B params; 64GB full precision, 32GB (0.2% degrade), 24GB (1.0% degrade)
Owner:  Meta (Hugging Face model card)
Scope:  ~29.6B incl. vision encoder; Apache 2.0; 131,072+ context; 100+ languages
```

```text
Figure: Muse Glimmer wins ~half of 24 benchmarks; notable losses — GDPVal-AA v2
        953 vs 1141 (Qwen), OSWorld-Verified 65.9 vs 75.6 (Qwen), TerminalBench
        2.1 51.7 vs 60.7 (Qwen), GPQA Diamond 83.5 vs 85.7 (Gemma)
Owner:  Meta (model card table); self-reported on Meta's chosen benchmark set
Scope:  vs Gemma4-31B and Qwen3.6-27B; the "wins" (e.g. SWE-Bench Pro 51.2,
        AIME 2026 94.7, MCP Atlas 75.5, IFBench 77.0) are the fine print an item
        should carry alongside the wins
```

```text
Figure: Long March 7A failed ~85s after liftoff; 56th Chinese orbital attempt of
        2026, 4th failure; payload Zhongxing-4B
Owner:  SpaceNews (secondary); no official primary issued as of reporting
Scope:  ~12:00 UTC Aug 10 2026, Wenchang; 7A debuted (and failed) March 2020
```

## Source assets

```text
Asset: Muse Glimmer benchmark comparison table (model card, "Benchmarks" section)
Shows: exactly where the 30B model wins and loses against Gemma4-31B and
       Qwen3.6-27B — the split that turns "beats models its size" into a claim a
       reader can check
Crop:  must retain the competitor columns and the rows where Glimmer loses
       (GDPVal-AA v2, OSWorld, TerminalBench, GPQA); omitting them would
       misrepresent a self-report as a sweep
```

```text
Asset: fidelity / density-matrix and Grover-outcome figures in arXiv 2608.03012
       (results sections)
Shows: the measured 4-qubit GHZ fidelity 0.961(0.003), cluster-state fidelity
       0.991(0.004), and the Grover identification probabilities per target
Crop:  keep the numerical fidelity/probability labels and error bars; a decorative
       chip photograph without the measurement panels would carry no argument
```

```text
Asset: OpenAI "Advanced Cybersecurity Completion Rate" bar chart (announcement)
Shows: the 95% vs 57.3% vs 1.5% vs 2% gap that sizes the capability jump
Crop:  n/a — the primary page is gated and was not opened; do not reproduce a
       chart no one on this desk has seen. Cite the numbers as text instead.
```

```text
Asset: Riemann bound — None found worth reproducing. The result is a single pair
       of numbers (41.6% -> 67.2%); a chart would decorate, not inform. The Lean
       repository and manuscript are the artifacts, better linked than depicted.
```

## Discarded

```text
URL: https://www.nature.com/articles/s41591-026-04476-6 — aleniglipron oral GLP-1
     phase 2b (ACCESS): real Nature Medicine result but published/announced early
     June 2026 (Structure Therapeutics, June 5). The Aug 10 ScienceDaily item is
     a re-surfacing, not a new development. Also a figure conflict (up to 11.3%
     in the trial vs "up to 12.1%" in some coverage). Not day-anchored to 08-11.
```

```text
URL: https://www.therobotreport.com/x-square-robot-debuts-foundation-model-embodied-ai-100m-series-a/ —
     wrong/older piece (Sept 2025 Wall-OSS + Series A+); does not cover the Aug
     2026 HOST framework. The HOST claim (62% success from a 29s human video)
     appears only in Pandaily and a project page I could not open cleanly;
     unverified. A lead, not a citable item this pass.
```

```text
URL: https://pandaily.com/x-square-robot-host-29-second-skill-learning-video-aug2026 —
     fetch returned only the headline; figures (62%, robustness deltas) not
     confirmed from an opened page. Unverified lead.
```

```text
URL: https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model —
     Meta's own launch blog (would be a fine primary) but returns HTTP 403 to
     fetch; superseded here by the model card, which carries the numbers.
```

```text
URL: https://www.cnn.com/2026/08/11/china/china-long-march-rocket-failure-intl-hnk —
     returns HTTP 451; could not open. Long March covered via SpaceNews instead.
```

```text
URL: https://www.digitalapplied.com/blog/ai-model-releases-august-2026-tracker,
     https://techstartups.com/2026/08/10/..., https://aiweekly.co/ai-news-today,
     https://www.secondtalent.com/news/ai/, https://www.buildfastwithai.com/... —
     aggregators used only to surface candidates and dates, not cited for facts.
     Several early-August items they list (Astra 08-01, Alpamayo 2 Super 08-04/05,
     AMD–Taalas 08-06, DARPA VENOM F-16 July, DeepMind leadership change 08-08)
     are stale for an 08-11 brief and/or already covered.
```

```text
URL: Qwen3.8-Max / Qwen3.8-27B open weights — Alibaba promised weights "week of
     10 August" on Hugging Face/ModelScope; as of the 11th nothing had shipped
     and no license was named. A non-event, not a development. Note only if a
     later brief needs the thread.
```
