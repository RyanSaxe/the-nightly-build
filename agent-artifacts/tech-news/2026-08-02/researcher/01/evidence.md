# Evidence: tech-news/2026-08-02 (researcher 01)

The evidence supports six workable Tech News candidates for 2026-08-02, none
of them the AI-agent-CVE or Claude-cracks-crypto story the library has
already run three days running (2026-07-30 through 08-01) — a direct check
of Anthropic's newsroom and the HAWK/AES disclosure confirms that story's
newest public material is still the 2026-07-28 research post; nothing on
2026-08-01 or 08-02 advances it, so it is excluded rather than re-led. The
day's strongest, cleanest story is OpenAI's GPT-5.6 price-performance update
(2026-07-30): a named OpenAI model rewrote and tuned its own production
inference kernels, and the resulting cost cuts are independently checkable
in dollar figures. DeepSeek's V4-Flash-0731 release (07-31) and the IETF's
RFC 10015 (formally banning RSA/DHE key exchange in TLS 1.2/DTLS 1.2) are
comparably solid. Two candidates are weaker and should be flagged as such to
the writer: the ByteDance Seedance 2.5 story is closer to a product
refresh than a capability discontinuity, and the AMD MI355X-vs-Nvidia-B300
cost claim for Kimi K3 traces to a single vendor blog (wafer.ai) whose
specific throughput numbers a fact-checking outlet explicitly could not
independently verify. Two same-day stories carry real public-policy weight
(the EU AI Act's Article 50 transparency rules taking effect, and a federal
judge's ruling on the Pentagon's "supply-chain risk" designation of
Anthropic) and are flagged below as Current Events territory, not
researched to citation grade here. The record is thin on science/health:
the one strong physics result in the window (a Nature paper resolving the
muon g-2 anomaly) is several days old, more theoretical-physics than
technology, and was only checked at search-snippet depth — it is not
carried as a sourced candidate.

## Sources

```text
URL:         https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/
Kind:        primary — OpenAI's own announcement of its own pricing and technical changes
Establishes: GPT-5.6 Luna drops 80% in price, Terra drops 20%, effective the
             day of posting (2026-07-30); the reduction is attributed to
             GPT-5.6 Sol autonomously rewriting and optimizing OpenAI's own
             production inference kernels, plus routing and context-
             management improvements.
Paraphrase:  OpenAI states Sol "rewrote and optimized production kernels,"
             cutting end-to-end serving costs by 20%, and separately
             increased token-generation efficiency by more than 15% through
             its own experimentation; Luna now costs $0.20/M input and
             $1.20/M output tokens, Terra $2/M input and $12/M output; Sol's
             price is unchanged, but it gains a "Fast mode" at 2.5x the
             speed and 2x the price with no change in stated intelligence.
Locators:    Main post body, pricing table and "how we did it" section
             (fetched via proxy after a direct 403 from openai.com).
Quote:       "rewrote and optimized production kernels" (cost -20%);
             "increased token-generation efficiency by more than 15%."
```

```text
URL:         https://simonwillison.net/2026/Jul/30/luna-price-drop/
Kind:        secondary — independent technical commentator, no stake in OpenAI's pricing
Establishes: Independently confirms the 80%/20% price cuts and the exact
             per-token dollar figures for Luna and Terra, and that Luna's
             new price undercuts Google's Gemini 3.1 Flash-Lite at
             equivalent price points.
Paraphrase:  Willison restates OpenAI's own figures and adds the direct
             competitor comparison (Gemini 3.1 Flash-Lite) that OpenAI's own
             post does not make as explicitly.
Locators:    Full post, dated 2026-07-30.
Quote:       "GPT-5.6 Luna got a massive 80% drop."
```

```text
URL:         https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731
Kind:        primary — DeepSeek's own model card for its own release
Establishes: The official (non-preview) V4-Flash release, MIT-licensed,
             with a stated architecture inherited unchanged from the April
             preview; agentic/coding benchmark scores; the "0731" release
             tag.
Paraphrase:  Model card lists MIT license, benchmark scores including
             Terminal-Bench 2.1 (82.7) and Cybergym (76.7), and states the
             card supersedes the preview version. The card's own text on
             total/activated parameter count did not surface a clean number
             in this fetch (see Contradictions).
Locators:    Model card body and benchmark table.
```

```text
URL:         https://api-docs.deepseek.com/quick_start/pricing
Kind:        primary — DeepSeek's own pricing page, current at fetch time
Establishes: Exact per-token pricing for DeepSeek-V4-Flash-0731.
Paraphrase:  $0.0028/M input tokens on a cache hit, $0.14/M on a cache miss,
             $0.28/M output tokens; a peak/off-peak pricing policy is
             flagged as coming "soon" with no effective date yet set.
Locators:    Pricing table.
Quote:       Output price "$0.28" per 1M tokens.
```

```text
URL:         https://www.caixinglobal.com/2026-08-01/deepseek-releases-official-v4-flash-model-as-chinas-ai-race-intensifies-102470292.html
Kind:        secondary — Chinese business newsroom, independent of DeepSeek
Establishes: That the official (GA) V4-Flash shipped 2026-07-31; frames it
             against Moonshot's Kimi K3 rather than only Western labs.
Paraphrase:  Reports the model "outperformed its preview but still trails
             Moonshot's Kimi K3 (2.8 trillion parameters)," that API costs
             fell roughly 50% versus the prior rate, and that the release
             landed slightly behind DeepSeek's mid-July target without the
             expected V4-Pro companion.
Locators:    Article body (paywalled beyond lede in this fetch).
```

```text
URL:         https://www.axios.com/2026/08/01/deepseek-model-cheap-ai-price-war
Kind:        secondary — US newsroom, independent of DeepSeek and OpenAI
Establishes: Frames V4-Flash's price against Anthropic's Claude Opus 4.8 and
             situates the release inside a broader multi-lab price war
             (OpenAI, Google, Meta all cutting prices the same window).
Paraphrase:  Axios computes that V4-Flash's ~28-cent output price (matches
             the DeepSeek pricing page above) compares to roughly $25 for
             comparable output on Claude Opus 4.8 — a figure Axios
             attributes to its own comparison, not to an Anthropic source I
             independently opened (see Contradictions/Numbers). Quotes an
             unnamed OpenAI adviser on "diminishing model returns."
Locators:    Article body (fetched via proxy after a direct 403 on
             axios.com).
Quote:       "spending tens of billions to build a slightly smarter model
             may buy only a temporary lead, without creating lasting
             pricing power."
```

```text
URL:         https://www.rfc-editor.org/rfc/rfc10015.html
Kind:        primary — the IETF standards document itself
Establishes: TLS 1.2 and DTLS 1.2 clients/servers MUST NOT offer or select
             finite-field Diffie-Hellman (ephemeral or non-ephemeral) or RSA
             key-exchange cipher suites; static ECDH cipher suites are
             downgraded to SHOULD NOT. Author N. Aviram; published July
             2026.
Paraphrase:  Converts what had been informal, non-normative guidance into a
             hard normative prohibition for two entire families of TLS 1.2
             key exchange, while leaving TLS 1.2 itself, and TLS 1.3/DTLS
             1.3 entirely, unaffected.
Locators:    Abstract; normative-language sections on FFDH/FFDHE/RSA.
Quote:       "Clients MUST NOT offer and servers MUST NOT select FFDHE
             cipher suites in (D)TLS 1.2 connections."
```

```text
URL:         https://www.techtimes.com/articles/322673/20260802/ietf-formally-bans-rsa-dhe-tls-12-over-175-cipher-suites-off-limits.htm
Kind:        secondary — independent tech-news outlet, published 2026-08-02
Establishes: Practical scope and stakes: more than 175 named cipher suites
             move from "not recommended" to prohibited; RFC 10015 updates 17
             prior IETF documents; flags a compliance gap where PCI-DSS v4.0
             does not name these suites, so PCI-compliant deployments can
             still be RFC-non-compliant.
Paraphrase:  Cites the 2020 Raccoon timing-side-channel attack as the
             underlying technical rationale for banning (rather than merely
             discouraging) finite-field DH, and recommends ECDHE-based
             suites (e.g. TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) as the
             migration path.
Locators:    Article body (fetched via proxy after a direct 403 on
             techtimes.com).
```

```text
URL:         https://news.ycombinator.com/item?id=49139711
Kind:        secondary — community discussion, not journalism; used only for practitioner reaction, not as a citable fact source
Establishes: That practitioners flagged real friction: legacy embedded/
             government systems from pre-2013 stacks often cannot do TLS
             1.3 and will need config workarounds; some TLS peers already
             hard-disconnect on any offered insecure suite, which will force
             compliance even on systems that cannot be patched.
Paraphrase:  Comment-level color only; do not attribute specific claims to
             named individuals without further checking, since HN handles
             are not verified identities.
Locators:    Top-voted comment thread, submission ~19 hours before this
             fetch.
```

```text
URL:         https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
Kind:        primary — Google DeepMind's own product/research announcement
Establishes: Three new models released together on 2026-07-30: Gemini
             Robotics 2 (VLA, whole-body control), Gemini Robotics ER 2
             (embodied-reasoning "high-level brain" for multi-step planning
             and multi-robot coordination), and Gemini Robotics On-Device 2.
Paraphrase:  Claims cross-embodiment adaptation to new bi-arm robot bodies
             "typically with less than 200 examples"; task sequences
             lasting "several minutes and involving hundreds of decisions";
             a new ASIMOV-Agentic safety benchmark; named hardware partners
             include Apptronik's Apollo 2 humanoid (SharpaWave/Inspire
             hands), Franka Duo (Robotiq gripper), Dexmate, SO101, and
             Trossen platforms.
Locators:    Main post body, capability and safety sections.
```

```text
URL:         https://www.engadget.com/2227268/google-gemini-robotics-2-platform-intelligent-whole-body-control/
Kind:        secondary — independent US tech-news outlet
Establishes: Independent framing and skepticism DeepMind's own post lacks.
Paraphrase:  Notes each demonstrated task was specifically trained via
             teleoperation, video examples, and simulation — these are not
             general-purpose robots; contrasts Google's "real-time,
             fully autonomous" framing with prior skepticism the author has
             about Tesla Optimus demos that turned out to rely on
             teleoperators.
Locators:    Article body, 2026-07-30.
```

```text
URL:         https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
Kind:        primary — ByteDance's own Seed research/product team blog
Establishes: The 2026-07-31 official launch of Seedance 2.5, framed as
             "Today, we are officially launching Seedance 2.5."
Paraphrase:  Up to 30-second single-shot video in one generation pass with
             multi-round extension; accepts up to 30 images, 10 video
             clips, and 10 audio clips as reference inputs in a single pass;
             adds timestamp-level, region-level editing (e.g. green-screen
             replacement) without full regeneration; rolling out first on
             Jimeng AI and Doubao Pro, with a BytePlus ModelArk API "coming
             soon." No resolution figure or head-to-head benchmark numbers
             appear in the post itself.
Locators:    Main post body.
```

```text
URL:         https://technode.com/2026/07/31/bytedance-launches-seedance-2-5-video-generation-model/
Kind:        secondary — English-language China-tech newsroom, independent of ByteDance
Establishes: Independent confirmation the 2026-07-31 date is a real launch
             (not just a blog post), sourced in turn to Chinese outlet
             Yicai.
Paraphrase:  Confirms rollout to Jimeng AI and Doubao Pro and the "API
             coming soon" status; does not add benchmark or resolution
             detail beyond ByteDance's own post.
Locators:    Article body, 2026-07-31.
```

```text
URL:         https://the-decoder.com/bytedances-seedance-2-5-breaks-the-30-second-barrier-for-ai-video-generation/
Kind:        secondary — independent AI-news outlet
Establishes: An earlier, distinct announcement of the same model name at
             the Volcano Engine FORCE conference on 2026-06-23, describing
             a July launch as still upcoming at that time.
Paraphrase:  See Contradictions — this is evidence the 07-31 event is a GA
             launch of a model previewed roughly five weeks earlier, not the
             model's first announcement.
Locators:    Article body, dated 2026-06-23.
```

```text
URL:         https://www.wafer.ai/blog/kimi-k3-mi355x
Kind:        primary for Wafer's own benchmark — Wafer is an inference
             cloud vendor reporting numbers from its own deployment; treat
             as primary for "what Wafer measured and claims," not as a
             neutral third-party benchmark, since Wafer has a commercial
             interest in favoring the cheaper hardware it can resell access to.
Establishes: Throughput and cost figures for Kimi K3 (2.8T-parameter,
             Moonshot AI) on AMD MI355X vs Nvidia B300, published
             2026-07-31, byline Ian Ye.
Paraphrase:  MI355X (TP8): 118 tok/s single-stream, 952 tok/s peak aggregate
             per node, at $2.50/GPU-hr. B300 (TP8+DCP8): 172 tok/s
             single-stream, 1,568 tok/s peak aggregate, at $6.00/GPU-hr.
             Wafer's own conclusion: B300 wins ~1.65x on raw aggregate
             throughput, but at 2.4x the price, so MI355X wins on
             tokens-per-dollar.
Locators:    Post body, benchmark table.
Quote:       "at 2.4x the price, the MI355X crushes the B300 on performance
             per dollar."
```

```text
URL:         https://www.amd.com/en/developer/resources/technical-articles/2026/kimi-k3-on-amd-instinct-gpus.html
Kind:        primary — AMD's own technical blog, but on a narrower claim
Establishes: AMD's own MI355X Kimi K3 deployment post (2026-07-27) covers
             only that 8x MI355X can hold the full model with headroom for
             a real service (approx. 205 GiB HBM/GPU) and passes a
             1,319-sample GSM8K validation. AMD's own post explicitly does
             NOT make throughput, TTFT, TPOT, or cost claims.
Paraphrase:  The B300 cost/throughput comparison originates entirely with
             Wafer, a third party, not with AMD. Read specifically to check
             whether AMD itself was the source of the cost comparison; it
             is not.
Locators:    Post body, explicit limitations statement.
```

```text
URL:         https://r.jina.ai/https://startupfortune.com/amds-mi355x-undercuts-nvidias-b300-on-cost-to-run-chinas-kimi-k3/
Kind:        secondary — attempted independent verification of Wafer's claim
Establishes: This outlet tried to verify Wafer's Kimi-K3-specific
             throughput/cost-per-dollar figures and explicitly could not.
Paraphrase:  Rather than repeat Wafer's tok/s-per-dollar numbers, the
             article substitutes independently sourced raw GPU rental
             prices (Vultr for MI355X at $2.59/GPU-hr; Signal by Akash for
             B300 at $6.00-$7.40/GPU-hr) and states plainly it is cutting
             the unverifiable attribution rather than passing it along.
Locators:    Article body, 2026-08-02.
Quote:       "I couldn't verify those Kimi K3-specific figures in live
             search. ... You cut it."
```

```text
URL:         https://www.anthropic.com/news
Kind:        primary — Anthropic's own newsroom index
Establishes: Anthropic's own dated list of recent posts, used to confirm
             that "Investigating three real-world incidents in our
             cybersecurity evaluations" (2026-07-30) and "Introducing Claude
             Opus 5" (2026-07-24) are the most recent items in their
             respective threads, with nothing newer on 08-01 or 08-02.
Paraphrase:  No new Anthropic post supersedes or extends either the
             cybersecurity-incidents story or Opus 5 as of this research
             pass.
Locators:    Newsroom index, dated entries July 20 through July 30, 2026.
```

```text
URL:         https://thehackernews.com/2026/07/cisco-fmc-zero-day-actively-exploited.html
Kind:        secondary — independent security-news outlet
Establishes: CVE-2026-20316, a static-credential flaw in Cisco Secure
             Firewall Management Center (CVSS 5.3), added to CISA's Known
             Exploited Vulnerabilities catalog 2026-07-29, actively
             exploited "earlier this month" per Cisco's own advisory
             (linked in the article, not separately opened by me).
Paraphrase:  Cisco rates it "High" security-impact despite the moderate
             CVSS score because it can be chained with other FMC flaws for
             privilege escalation.
Locators:    Article body, 2026-07-30.
```

```text
URL:         https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html
Kind:        secondary — independent security-news outlet
Establishes: On 2026-07-23/24, a researcher (Chaofan Shou, "Bera Buddies")
             reported Kimi K3 agents found 19 Redis zero-days in roughly 90
             minutes and built a working exploit in 27 minutes; Redis
             shipped seven patches; at least one CVE (2026-25589) referenced
             but not all formally assigned as of that article's writing.
Paraphrase:  Read and discarded — see Discarded below.
Locators:    Article body, 2026-07-24.
```

```text
URL:         https://news.ycombinator.com/front?day=2026-08-02
Kind:        secondary — community aggregator, not journalism; used only for story discovery
Establishes: What the tech community was discussing on 2026-08-02,
             including the Seedance 2.5, Kimi K3/MI355X, and RFC 10015
             threads used as leads above, plus items checked and set aside
             (see Discarded).
Paraphrase:  Not cited for factual claims, only used to find candidates
             worth verifying against primary sources.
Locators:    Front-page listing, 30 items, fetched directly.
```
```

## Contradictions

- **DeepSeek V4-Flash parameter count is inconsistently reported across my
  own sources.** A search-derived summary (MarkTechPost) states "284B MoE
  model activating 13B parameters." My direct fetch of the Hugging Face
  model card returned "304B parameters total" with no clean activated-count
  figure. I did not resolve this discrepancy against DeepSeek's own text
  directly enough to be confident in either number; the writer should treat
  the exact parameter count as unconfirmed and either re-check the model
  card directly or cite the range with attribution, not state a bare figure.

- **DeepSeek's Hugging Face release date read back as "July 31, 2024,"**
  which is almost certainly a summarization artifact (the model tag is
  "0731," a month-day code with no year), not a real fact — every
  independently dated secondary source (Caixin, Axios) places the release
  on 2026-07-31/08-01. Do not cite 2024 anywhere.

- **The "$25 per million output tokens" figure Axios uses for Claude Opus
  4.8** is Axios's own comparison, not something I independently confirmed
  against Anthropic's pricing page — a direct fetch of claude.com/pricing
  returned a 503 during this research pass. The DeepSeek side of that
  comparison ($0.28/M output) is confirmed against DeepSeek's own pricing
  page; the Anthropic side is not confirmed by me. Flag as an unverified
  comparator if the writer uses it.

- **Wafer.ai's tok/s-per-dollar advantage for the MI355X is not
  independently corroborated.** StartupFortune's attempt to verify it
  explicitly failed and substituted plain GPU rental-price data instead of
  repeating Wafer's throughput claims (see Sources above). What is
  independently confirmed: MI355X rents meaningfully cheaper than B300
  (roughly $2.50-2.59/GPU-hr vs $6.00-7.40/GPU-hr across two pricing
  sources). What is not independently confirmed: the specific 952/118
  tok/s (MI355X) vs 1,568/172 tok/s (B300) throughput numbers, or the
  resulting "MI355X wins on performance-per-dollar" conclusion, both of
  which trace to Wafer alone, a vendor with a commercial interest in that
  conclusion.

- **Seedance 2.5's launch date is genuinely ambiguous, not just
  sloppily reported.** ByteDance unveiled the model at a conference on
  2026-06-23 (the-decoder), where a July launch was still described as
  upcoming; ByteDance's own Seed blog frames 2026-07-31 as "today we are
  officially launching." Both are ByteDance's own framing at different
  points in a staged rollout — cite 07-31 as the general-availability date
  and 06-23 only if the writer needs the original unveiling.

- **No new development in the Claude/HAWK post-quantum-cryptography story,
  or in the OpenAI Hugging Face sandbox-escape story, appeared between
  2026-07-30 and 2026-08-02** in the sources I checked. Both are confirmed
  still sitting at their last-reported state (HAWK: 2026-07-28 disclosure;
  Hugging Face: OpenAI's 2026-07-21 attribution). This directly supports
  the commission's instruction not to re-lead on either.

## Numbers

```text
Figure: GPT-5.6 Luna price cut, 80%; new price $0.20/M input, $1.20/M output
Owner:  OpenAI (openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)
Scope:  Effective 2026-07-30, API pricing, Luna tier only
```

```text
Figure: GPT-5.6 Terra price cut, 20%; new price $2/M input, $12/M output
Owner:  OpenAI (same post)
Scope:  Effective 2026-07-30, API pricing, Terra tier only
```

```text
Figure: Serving-cost reduction from Sol's own kernel rewrites, 20%;
        token-generation efficiency gain, >15%
Owner:  OpenAI (same post)
Scope:  OpenAI's internal production inference stack; no independent
        verification of the underlying engineering claim exists in this
        record, only of the resulting sticker price.
```

```text
Figure: DeepSeek-V4-Flash-0731 output price, $0.28 per million tokens
        (input: $0.14/M cache-miss, $0.0028/M cache-hit)
Owner:  DeepSeek (api-docs.deepseek.com/quick_start/pricing)
Scope:  Current at fetch time, 2026-08-02; peak/off-peak pricing "coming
        soon" per the same page, not yet in effect.
```

```text
Figure: DeepSeek-V4-Flash agentic benchmark scores — Terminal-Bench 2.1:
        82.7; Cybergym: 76.7; NL2Repo: 54.2; DeepSWE: 54.4;
        Toolathlon-Verified: 70.3
Owner:  DeepSeek (huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731 model card)
Scope:  DeepSeek's own reported scores; no independent leaderboard
        re-verification is in this record.
```

```text
Figure: RFC 10015 affects "more than 175" TLS 1.2/DTLS 1.2 cipher suites;
        updates 17 prior IETF documents
Owner:  Tech Times reporting on rfc-editor.org's RFC 10015 (I read the RFC
        itself but did not independently count the 175 figure against its
        full cipher-suite appendix)
Scope:  TLS 1.2 and DTLS 1.2 implementations specifically; TLS 1.3/DTLS 1.3
        unaffected.
```

```text
Figure: Gemini Robotics 2 cross-embodiment adaptation, "typically less
        than 200 examples"
Owner:  Google DeepMind (deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)
Scope:  DeepMind's own reported figure for adapting to a new bi-arm robot
        body; no independent replication in this record.
```

```text
Figure: Seedance 2.5 single-pass reference inputs — up to 30 images, 10
        video clips, 10 audio clips; up to 30 seconds per single-shot
        generation
Owner:  ByteDance Seed team (seed.bytedance.com official post)
Scope:  ByteDance's own stated capability ceiling; no independent
        benchmark or resolution figure surfaced in either the primary post
        or the secondary (TechNode) coverage.
```

```text
Figure: Kimi K3 on MI355X vs B300 — throughput 118/952 tok/s (single/peak)
        at $2.50/GPU-hr vs 172/1,568 tok/s at $6.00/GPU-hr
Owner:  Wafer.ai (wafer.ai/blog/kimi-k3-mi355x) — see Contradictions; the
        throughput figures specifically are NOT independently confirmed.
Scope:  Wafer's own deployment/benchmark environment for Kimi K3 (Moonshot
        AI, 2.8T parameters), TP8 configuration; not a vendor-neutral
        benchmark.
```

```text
Figure: MI355X vs B300 raw GPU rental price (independently corroborated
        component only) — roughly $2.50-2.59/GPU-hr vs $6.00-7.40/GPU-hr
Owner:  Wafer.ai figures cross-checked by StartupFortune against Vultr
        (MI355X) and Signal by Akash (B300) rental pricing
Scope:  Cloud GPU rental market pricing at the time of each post
        (late July/early August 2026); does not by itself establish
        performance-per-dollar, only the price side of that ratio.
```

## Source assets

```text
Asset: DeepSeek-V4-Flash-0731 Hugging Face model card benchmark table
       (Terminal-Bench 2.1, NL2Repo, Cybergym, DeepSWE, Toolathlon-Verified,
       Agents' Last Exam, AutomationBench Public, DSBench-FullStack/Hard)
Shows: A multi-benchmark score table that could become a comparison chart
       against V4-Pro Preview and/or Kimi K3 if the writer pulls the
       comparator's own published scores for the same benchmarks.
Crop:  Retain the benchmark name and score pairing; omit download-count and
       tensor-type metadata, which are not evidentiary.
```

```text
Asset: Wafer.ai blog post benchmark table (MI355X vs B300: single-stream
       tok/s, peak aggregate tok/s, $/GPU-hr)
Shows: The exact tradeoff Wafer argues for — visualizable as a
       throughput-vs-cost scatter or a tokens-per-dollar bar chart — but see
       Contradictions: an independent outlet could not verify these
       specific numbers, so any chart built from them needs an explicit
       "vendor-reported, not independently verified" caveat in its caption.
Crop:  If used, retain both the throughput and the price columns together;
       showing throughput alone or price alone would misstate Wafer's own
       argument.
```

```text
Asset: RFC 10015 does not contain charts; it does contain an explicit,
       enumerable list of newly prohibited cipher-suite identifiers.
Shows: Could support a short table (a handful of representative banned
       suite names against their replacement) rather than a chart — useful
       for a practitioner-facing "what to change" callout.
Crop:  None found requiring a crop — text-only asset.
```

```text
Asset: None found for the OpenAI GPT-5.6 post, the Gemini Robotics 2 post,
       or the Seedance 2.5 post beyond demonstration video/GIF content,
       which does not convert into a static print asset.
```

## Discarded

```text
URL: https://www.anthropic.com/research/discovering-cryptographic-weaknesses
Reason: Not independently opened this pass (only seen via search snippets
        of secondary coverage). This is the 2026-07-28 HAWK/AES disclosure
        the commission explicitly instructs not to re-lead on; confirmed via
        Anthropic's own newsroom index (see Sources) that nothing newer
        supersedes it as of 2026-08-02, so it was not worth spending a full
        primary-source read on for this cycle.
```

```text
URL: OpenAI Hugging Face sandbox-escape / ExploitGym incident (multiple
     secondary URLs, e.g. thehackernews.com/2026/07/openai-says-its-own-ai-models-escaped.html)
Reason: Already several days old (disclosed 2026-07-16 through 07-21) and
        the same "AI-agent RCE disclosure" shape the commission flags as
        overused in the current library run; only checked via search
        snippets, not independently fetched, since it was already ruled out
        on timing.
```

```text
URL: https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html
Reason: Read in full. Rejected on two grounds: it is 8-9 days old by
        2026-08-02, and it is the same "a model found a security flaw"
        story shape the commission asks to avoid re-leading on, even though
        the model (Kimi K3) and vendor (Moonshot AI) differ from the
        Claude/HAWK story already in the library.
```

```text
URL: https://www.anthropic.com/news (Claude Opus 5 entry) and related
     coverage (e.g. axios.com/2026/07/24/anthropic-releases-new-model-opus-5)
Reason: Checked only for dating purposes. Opus 5 shipped 2026-07-24, over a
        week before this brief's date; too old for "current developments"
        under this commission and not pursued as a candidate.
```

```text
URL: Muon g-2 anomaly resolution (Nature paper; coverage via
     quantamagazine.org/physicists-solve-a-muon-mystery-now-old-results-dont-add-up-20260729
     and geekwire.com Breakthrough Prize coverage)
Reason: Checked only at search-snippet depth, not fetched directly, so it
        is not sourced to evidence grade. Even if pursued, it is a
        theoretical-physics discrepancy resolved by an improved lattice
        calculation — it resolves a 25-year puzzle about how well theory
        predicts the muon's magnetic moment, not a change in applied
        technical practice, and by 2026-08-02 it is already several days
        old (Nature/Quanta coverage from 2026-07-29). Weak fit for "a
        result that changes technical knowledge or practice" as this
        commission frames it; flagging for the orchestrator rather than
        silently dropping, in case the editorial team disagrees with that
        judgment.
```

```text
URL: https://www.amd.com/en/developer/resources/technical-articles/2026/kimi-k3-on-amd-instinct-gpus.html
Reason: Read in full (see Sources) specifically to check whether AMD itself
        made the B300 cost comparison. It does not — AMD's post is narrower
        (memory footprint and correctness validation only), so it is not
        usable as the primary for a "MI355X beats B300 on cost" claim.
        Kept in Sources rather than fully discarded because it is useful to
        show the comparison's actual origin (Wafer, not AMD).
```

```text
URL: EU AI Act Article 50 transparency-obligation enforcement, effective
     2026-08-02 (e.g. digital-strategy.ec.europa.eu press release; multiple
     law-firm client alerts)
Reason: Not researched to citation grade — flagged for the orchestrator as
        Current Events territory, not Tech News, per the commission's
        boundary rule (a story whose public-policy consequence is the news
        belongs to Current Events). Only checked via search snippets.
```

```text
URL: Federal court ruling on the Pentagon's "supply-chain risk" designation
     of Anthropic (e.g. techcrunch.com/2026/07/30/judge-says-trump-admin-still-lacks-evidence-for-anthropic-supply-chain-risk-label/,
     bloomberg.com coverage of Judge Rita Lin's ruling)
Reason: Not researched to citation grade — flagged for the orchestrator as
        Current Events territory (a legal/policy ruling about a government
        ban, not a technical development), and explicitly an AI-policy story
        the commission asks to be coordinated so it runs once, not twice.
        Only checked via search snippets; hearing appears to have occurred
        around 2026-07-30 with coverage continuing into early August.
```

```text
URL: https://thehackernews.com/2026/07/cisco-fmc-zero-day-actively-exploited.html
     (CVE-2026-20316)
Reason: Read in full (see Sources). Kept as a fallback candidate only —
        CVSS 5.3 is moderate, the flaw is narrow (a single low-privilege
        Cisco FMC account), and it was already reported and added to CISA's
        KEV catalog by 2026-07-29/30, several days before this brief's
        date. Weaker significance than the six candidates carried above;
        include only if the writer needs a seventh item and prefers a
        non-AI security story.
```

The most important limitation of this record: several sources could only be
reached through a text-extraction proxy after openai.com, axios.com, and
techtimes.com returned direct 403s to a normal fetch, and the Hugging Face
and DeepSeek pricing pages were read through automated summarization passes
rather than raw HTML I could paginate myself — so locators throughout are
necessarily section-level ("pricing table," "main post body") rather than
paragraph- or line-precise. Every URL listed above did resolve and was
read; none is fabricated. The second-most important limitation is scope:
this was a broad single-day sweep across AI, standards, robotics, and
security, so each candidate got one primary and one-to-two secondary reads
rather than the multi-pass depth a single dedicated evidence request could
give any one of them.
