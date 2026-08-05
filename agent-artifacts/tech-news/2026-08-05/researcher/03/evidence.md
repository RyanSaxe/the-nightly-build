# Evidence: tech-news/2026-08-05 (researcher 03)

This is the third evidence pass, working under the orchestrator's authorized SCOPE
RULING that relaxes the window to the daily-wire "this week" scope: developments
from ~Jul 30 through Aug 5, 2026 that are newly consequential and were NOT already
filed in tech-news 2026-07-26 … 2026-08-04. It preserves the round-02 keeper
(Qwen3.8-Max) and its sourcing, confirms the arginine/MHC-I *Cell* keeper with a
newly-located primary-institution press release, and resolves the three open
questions the brief posed: it DROPS DiffusionGemma (the model shipped June 10, so
the Jul-31 arXiv report is documentation of a two-month-old release, not a new
development), DROPS the Nature Physics candidates (Sagnac-superfluid published
~June 26; teleportation July — both pre-window), and adds one genuinely new,
in-window, well-sourced field development the round-02 net missed: **OpenAI's
Astra "Ten Advances in Mathematics" release (Aug 1)** with machine-checkable Lean 4
certificates on GitHub.

Net result: **three fully-buildable, disjoint, in-window items** (Qwen3.8-Max,
Aug 3; OpenAI Astra, Aug 1; arginine/MHC-I, Jul 30), each with an owning primary,
at least one independent secondary, and all URLs resolving to the source's own
page. A fourth strong physics item (atom–quantum-dot two-photon interference,
*Light: Science & Applications*) is fully sourced and disjoint but its PRIMARY
online date is Jul 15 — its Jul-30 news wave is a coordinated press release, not
the publication date — so under a strict reading of the relaxed window it is a
near-miss, offered as a conditional 4th for the orchestrator to rule on. **A clean
4-item set is therefore achievable only if the orchestrator counts the atom–QD
item's Jul-30 press wave as the qualifying event; otherwise the honest buildable
set is 3.**

The evidence for *what OpenAI announced* in Astra is strong and unusually
verifiable (public Lean 4 certificates), but note two limits: the manuscripts were
prepared by humans working with the model, and human peer review of the
mathematics is ongoing — the machine-checkable certificate is the verification, the
"resolves a decade-old open problem" framing is partly OpenAI's. Qwen3.8-Max is
thin exactly where round 02 left it: the benchmark table is vendor-published and
not independently reproduced, and qwen.ai/blog is a JS app the fetcher cannot read.

## Buildable set at a glance

```text
FULLY BUILDABLE, IN-WINDOW, DISJOINT (primary + independent secondary, URLs resolve):
  1. Qwen3.8-Max (Alibaba, Aug 3)          — AI model release
  2. OpenAI Astra "Ten Advances" (Aug 1)   — AI-for-math, verifiable Lean proofs
  3. Arginine / MHC-I translation (Jul 30) — immunology / nutrition (Cell)

CONDITIONAL 4th (fully sourced + disjoint, but primary online date Jul 15):
  4. Atom–quantum-dot two-photon interference (Light: Sci. Appl.) — quantum networking

DROPPED THIS PASS (with reasons, below):
  - DiffusionGemma       — model released Jun 10; Jul-31 arXiv report is not new
  - Nature Physics Sagnac — published ~Jun 26 (pre-window)
  - Nature Physics teleportation — July (pre-window)
  - N-able N-central CVE  — current-events desk (per commission), not filed here
```

## Sources

### Keeper 1: Qwen3.8-Max (Alibaba, Aug 3 2026) — preserved from round 02, re-confirmed

```text
URL:         https://qwen.ai/blog?id=qwen3.8
Kind:        primary (owner) for what Alibaba announced — NOT DIRECTLY READABLE
Establishes: Alibaba/Qwen's official Qwen3.8-Max announcement and benchmark table
Paraphrase:  The owning page for the Qwen3.8-Max claim. URL resolves, but the page
             is a JS app; the fetcher returns only "Qwen" with no body. Every
             Qwen3.8-Max figure below is traced THROUGH secondaries that reproduce
             Alibaba's own table, not read off this page.
Locators:    blog?id=qwen3.8 (JS-gated; body not machine-readable via fetch)
Quote:       (none obtainable from the primary as loaded)
```

```text
URL:         https://siliconangle.com/2026/08/03/alibaba-debuts-qwen3-8-max-model-2-4t-parameters/
Kind:        secondary (independent US tech newsroom) — NEW this pass
Establishes: Aug-3 release; 2.4T total / 95B active MoE; 1M-token context; price
Paraphrase:  Reports Alibaba debuted Qwen3.8-Max on Aug 3 2026: 2.4 trillion
             parameters, 95B active via sparse MoE, 1-million-token context,
             native multimodal, priced at $2 / $6 per million input/output tokens,
             open weights to follow. Independent confirmation of the release, the
             specs, and the pricing.
Locators:    lede + specs paragraphs
Quote:       "2.4 trillion parameters"
```

```text
URL:         https://www.implicator.ai/alibaba-publishes-the-qwen3-8-max-benchmarks-it-withheld-two-weeks-ago/
Kind:        secondary (industry press; independent account) — carried from round 02
Establishes: Aug-3 publication of the benchmark numbers; the preview→release arc
Paraphrase:  Alibaba published benchmark scores for its 2.4T-parameter Qwen3.8-Max
             on Monday (Aug 3 2026), two weeks after claiming at WAIC the model was
             "second only to Claude Fable 5" without releasing any numbers. The
             Aug-3 event is the release of the withheld numbers, not a fresh preview.
Locators:    lede + benchmark-summary section
Quote:       "two weeks after claiming the model was second only to Claude Fable 5
             without releasing any numbers"
```

```text
URL:         https://the-decoder.com/alibabas-open-weight-qwen3-8-max-takes-on-long-horizon-ai-tasks-with-2-4-trillion-parameters/
Kind:        secondary (independent tech outlet) — carried from round 02
Establishes: Specs, positioning, the company autonomous-coding demonstration detail
Paraphrase:  Qwen3.8-Max is 2.4T total / 95B active on the Qwen3.5 architecture,
             aimed at coding/research/professional/multimodal work, Alibaba's first
             Max-scale model slated for open weights. The company-run oh-my-cli
             autonomous run is quantified: ~16 days, 265 commits, 127 pull requests,
             151 issues. Available via QwenCloud; weights due on Hugging Face and
             ModelScope "next week."
Locators:    specs paragraph + autonomous-coding paragraph + availability note
Quote:       "2.4 trillion parameters with 95 billion active"
```

```text
URL:         https://www.neowin.net/news/alibaba-releases-qwen38-max-challenging-gpt-56-sol-and-claude-fable-5-on-ai-benchmarks/
Kind:        secondary (independent tech outlet) — carried from round 02
Establishes: Independent confirmation of the Aug-3 release and the competitive claim
Paraphrase:  Reports the Aug-3 release of Qwen3.8-Max challenging GPT-5.6 Sol and
             Claude Fable 5 on published benchmarks. Confirms the RELEASE and the
             CLAIM, not the numbers.
Locators:    headline + lede
Quote:       (headline) "Alibaba releases Qwen3.8-Max, challenging GPT-5.6 Sol and
             Claude Fable 5 on AI benchmarks"
```

```text
URL:         https://www.bloomberg.com/news/articles/2026-08-03/alibaba-drops-another-china-ai-model-with-breakthrough-performance
Kind:        secondary (reputable US newsroom; paywalled) — carried from round 02
Establishes: Independent confirmation Alibaba shipped Qwen3.8-Max Aug 3
Paraphrase:  Bloomberg reports Alibaba released its largest model, Qwen3.8-Max,
             claiming benchmark scores rivaling Anthropic and ranking above
             Moonshot's Kimi K3. Confirms the RELEASE and CLAIM, not the benchmarks.
Locators:    headline + lede (full text paywalled)
Quote:       (headline) "Alibaba's Qwen3.8-Max AI Model Claims Benchmark Scores
             Rivaling Anthropic"
```

### Keeper 2: OpenAI Astra — "Ten Advances in Mathematics and TCS" (Aug 1 2026) — NEW, buildable

```text
URL:         https://openai.com/index/ten-advances-in-mathematics/
Kind:        primary (owner) — OpenAI's official announcement
Establishes: What OpenAI announced Aug 1: an internal version of its next major
             model, Astra, resolved or made substantial progress on ten long-standing
             open problems across eight fields of math and theoretical CS, with
             machine-checkable Lean 4 certificates published under Apache 2.0.
Paraphrase:  Ten results spanning high-dimensional geometry (sphere-packing upper
             bounds down to the Cohn–Elkies threshold), coding theory (exponentially
             improved bounds on binary and spherical codes), arithmetic circuit
             complexity, group theory (a non-sofic group construction), operator
             algebras (a disproof of Connes's rigidity conjecture, per secondaries),
             quantum complexity (exponential parallel repetition for quantum games),
             lattice cryptography, and extremal combinatorics (resolving Erdős
             problems 146 and 180). Total token cost to find all ten was ~$2,000 at
             Sol API rates. IMPORTANT process caveat, in OpenAI's own words: "The
             arguments were prepared into manuscripts by humans with the same model,
             and afterward, the model formalized each argument in a Lean certificate."
Locators:    announcement body; results list; cost note; process/verification note
Quote:       "The total number of tokens needed to find solutions to these problems
             would cost roughly $2,000 at Sol API rates."
```

```text
URL:         https://github.com/openai/ten-proofs
Kind:        primary (owner) — the machine-checkable artifact itself
Establishes: The verification substrate: public Lean 4 certificate files (Apache
             2.0), a formalization.yaml manifest, a ComparatorChallenges directory
             for independent verification, and links to the manuscript and the
             per-problem reasoning walkthroughs. Repo resolves and builds against
             Lean 4.32.0 + mathlib.
Paraphrase:  Ten Lean 4 formalization files covering sphere packing, quantum games,
             group theory, Ramsey/extremal theory and more, each a machine-checkable
             certificate of correctness. This is why the claim is checkable rather
             than take-our-word: a reader can compile the certificates. The full
             manuscript PDF: https://cdn.openai.com/pdf/ten-proofs-oai.pdf
Locators:    README; lakefile.toml / lean-toolchain; formalization.yaml
Quote:       "Lean certificates accompanying proofs in mathematics and theoretical
             computer science"
```

```text
URL:         https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/
Kind:        secondary (independent tech outlet), Aug 1 2026
Establishes: Independent account of the Aug-1 announcement and an outside-expert
             reaction
Paraphrase:  Reports OpenAI announced its "next major model" Astra by publishing ten
             previously-unsolved math/TCS solutions with Lean 4 machine-checkable
             certificates on GitHub, a 249-page manuscript and a 62-page account of
             how the arguments came together, at ~$2,000 compute. Quotes University
             of Manchester mathematician Thomas Bloom calling the results "big news."
             An independent expert reaction, not a full peer review.
Locators:    lede + expert-reaction paragraph
Quote:       (Thomas Bloom, per the outlet) "big news"
```

```text
URL:         https://qz.com/openai-astra-model-math-problems-lean-proofs-080326
Kind:        secondary (independent US business/tech newsroom)
Establishes: Second independent confirmation of the Aug-1 release, cost, and the
             Lean-proof verification approach
Paraphrase:  Quartz reports OpenAI's Astra model solved ten open math problems for
             roughly $2,000, with machine-checkable Lean proofs published for
             independent verification. Independent confirmation of the development.
Locators:    headline + body
Quote:       (headline) "OpenAI Astra model solves 10 open math problems for $2,000"
```

### Keeper 3: arginine / MHC-I codon-dependent translation (Cell, Jul 30 2026) — buildable

```text
URL:         https://www.cell.com/cell/abstract/S0092-8674(26)00818-4
Kind:        primary (peer-reviewed research paper, Cell) — page GATED (HTTP 403)
Establishes: The owning paper. DOI 10.1016/j.cell.2026.07.020 resolves (302 →
             Elsevier linkinghub). The article's own page returns 403 to the
             fetcher (gated, not dead); recorded as the source's home per policy.
Paraphrase:  Wu Q. et al., "Dietary arginine drives codon-dependent MHC class I
             translation and improves immunity in colon tumorigenesis and
             respiratory viral infection," Cell (2026). In mice, extracellular
             arginine restriction represses specific arginine tRNAs, stalling
             ribosomes on the arginine-rich MHC-I message and cutting antigen
             presentation; the effect is codon-usage dependent (synonymous codon
             mutations abolish it). Arginine restriction worsened influenza and
             SARS-CoV-2 outcomes and increased colon tumorigenesis; raising dietary
             arginine did the reverse.
Locators:    abstract + graphical abstract
Quote:       "codon-dependent MHC class I translation"
```

```text
URL:         https://www.rockefeller.edu/news/40196-amino-acid-arginine-diet-tumor-virus-infection/
Kind:        primary-institution press release (The Rockefeller University), Jul 30 2026
Establishes: The Jul-30 publication date, the full author list, and the affiliation
             — NEW this pass; pins the in-window date via a non-auth route.
Paraphrase:  Press release dated Jul 30 2026 announcing the Cell study. Authors, all
             at The Rockefeller University: Qiushuang Wu (first author, postdoc),
             Lara M. Seydlitz, Vladislav Iakimov, Dennis J. Hsu, Parham Habibzadeh,
             H.-Heinrich Hoffmann, Philip B. Paty, Charles M. Rice, and Sohail F.
             Tavazoie (senior). Wu notes arginine supplementation was "equally
             impactful" preventatively or after infection.
Locators:    release header (date) + author list + findings summary
Quote:       "equally impactful"
```

```text
URL:         https://www.eurekalert.org/news-releases/1138428
Kind:        secondary (press-release distribution) — corroborates Jul-30 timing
Establishes: Independent restatement of the finding and its timing
Paraphrase:  "The amino acid arginine helps the body fight tumors and viral
             infections" — carries the Rockefeller announcement of the Cell study on
             the same Jul-30 timeline. A repetition of the origin, not a second
             origin.
Locators:    headline + body
Quote:       (headline) "The amino acid arginine helps the body fight tumors and
             viral infections"
```

```text
URL:         https://www.sciencenews.org/article/amino-acid-argininine-colon-cancer-diet
Kind:        secondary (independent US science newsroom)
Establishes: Independent lay account of the mechanism and stakes
Paraphrase:  Science News explains the codon-stalling mechanism (ribosomes pause at
             arginine codons when charged tRNA supply falls, slowing MHC-I
             production) and the mouse results in colon cancer and influenza/COVID.
             Independent secondary; adds no new primary numbers.
Locators:    body
Quote:       (title) "How one amino acid might help fight colon cancer and infections"
```

```text
URL:         https://www.technologynetworks.com/applied-sciences/news/dietary-amino-acid-helps-the-body-fight-tumors-and-viral-infections-415256
Kind:        secondary (independent science-news outlet)
Establishes: Additional independent restatement of the result
Paraphrase:  Technology Networks reports the same Cell finding: arginine availability
             shapes MHC-I antigen presentation and thus immune visibility of tumors
             and viruses in mice. Independent secondary.
Locators:    body
Quote:       "Arginine May Improve Cancer Immunity"
```

### Conditional 4th: atom–quantum-dot two-photon interference (Light: Sci. Appl.) — sourced, but primary online date Jul 15

```text
URL:         https://www.nature.com/articles/s41377-026-02399-y
Kind:        primary (peer-reviewed paper, Light: Science & Applications) — GATED
Establishes: The owning paper. DOI 10.1038/s41377-026-02399-y. nature.com redirects
             the fetcher to idp.nature.com auth; the article's own page is recorded
             as its home. PRIMARY ONLINE DATE: Jul 15 2026 (per phys.org's citation).
Paraphrase:  Han Seb Moon (Pusan National University) and Je-Hyung Kim (UNIST) and
             colleagues demonstrate direct two-photon (Hong–Ou–Mandel) interference
             between single photons from two physically dissimilar, independent
             sources — a warm cesium atomic ensemble and an InAs/GaAs semiconductor
             quantum dot — without active spectral or temporal modification. Cesium
             heralded photons at ~917 nm; the QD tuned to 917.48 nm by cooling to
             12.5 K, giving spectral overlap 0.88; HOM visibility 0.65 ± 0.14. A
             building block for modular/hybrid quantum networks that mix emitter
             types.
Locators:    abstract; results (overlap, visibility, wavelength)
Quote:       "two-photon interference between independent atomic and quantum dot
             single-photon sources for hybrid quantum network" (title)
```

```text
URL:         https://phys.org/news/2026-07-cesium-atoms-quantum-dots-generate.html
Kind:        secondary (independent, editorially-reviewed science outlet), Jul 30 2026
Establishes: Independent account; and the date discrepancy that makes this a
             near-miss
Paraphrase:  phys.org (Science X, credited editors, fact-checked) reports the result
             and cites the journal publication date as Jul 15 2026, while the article
             itself and the coordinated press wave (PRNewswire, The Quantum Insider,
             Mirage News, Quantum Computing Report) are dated Jul 30 2026. So the
             DEVELOPMENT (journal publication) is Jul 15; the Jul-30 activity is a
             press-release push, i.e. syndication of a two-week-old paper.
Locators:    dateline + "published July 15, 2026" citation + metrics
Quote:       "published July 15, 2026"
```

## Contradictions

- **Qwen3.8-Max: vendor claim vs independent reproduction (unchanged).** Every
  Qwen3.8-Max headline benchmark is Alibaba's own table on mixed harnesses; no
  independent reproduction surfaced. Primary for "what was announced," vendor-only
  for "whether it is true." Open weights were still NOT on Hugging Face / ModelScope
  and no license was named as of the Aug-5 research window ("due next week").

- **Astra: verifiable certificate vs human-assisted framing.** The strongest fact
  is that the Lean 4 certificates are machine-checkable and public, so correctness
  of the formalized statements can be independently compiled — a materially higher
  bar than a bare capability claim. But OpenAI states the manuscripts were "prepared
  into manuscripts by humans with the same model," so this is human-plus-model
  collaboration, not an unattended solve; and human mathematical peer review of the
  full arguments is ongoing. The independent signal so far is expert reaction
  (Thomas Bloom, Manchester, "big news"), not completed peer review. The writer
  should keep "resolved a decade-old open problem" attributed and distinguish the
  machine-checked certificate from the not-yet-peer-reviewed manuscript.

- **atom–QD interference: development date vs press-wave date.** The paper's journal
  online date is Jul 15 2026 (pre-window); the uniform Jul-30 coverage is a
  coordinated press release, the same re-syndication pattern round 02 flagged for
  ScienceDaily items. Under the relaxed "~Jul 30–Aug 5" window this is a near-miss
  on the primary date, not a clean in-window development. Recorded honestly so the
  orchestrator can rule; not asserted as in-window.

- **"August" science is still mostly re-syndication (round-02 finding holds).**
  This pass re-confirmed that ScienceDaily's Aug 3-5 front page (weight-loss brain
  set-point, aging/ALS molecular switch, Arctic permafrost carbon, proton-assisted
  triplet transfer) traces to older or undated primaries and surfaced no new
  in-window, cleanly-owned, practice-changing result beyond arginine.

## Numbers

```text
Figure: Qwen3.8-Max — 2.4T total parameters / 95B active (MoE); 1M-token context
Owner:  Alibaba/Qwen (qwen.ai/blog?id=qwen3.8; via SiliconANGLE, implicator.ai, the-decoder)
Scope:  model size; active per forward pass. Owner page JS-gated — traced via secondaries.
```
```text
Figure: Qwen3.8-Max — pricing $2 / $6 per million input / output tokens
Owner:  Alibaba (via SiliconANGLE; techstartups roundup)
Scope:  list API pricing at launch
```
```text
Figure: Qwen3.8-Max — released Mon Aug 3 2026; open weights "due next week"; weights
        NOT yet posted and no license named as of Aug 5
Owner:  Alibaba (via implicator.ai, testingcatalog, neowin)
Scope:  release date + open-weights timeline
```
```text
Figure: Qwen3.8-Max — Terminal-Bench 2.1 86.6; SWE-bench Pro 67.7; FrontierSWE 73.5;
        PaperBench 93.0; CoWorkBench 74.8; WideSearch 81.9 (Alibaba's own table)
Owner:  Alibaba's published table (vendor-reported; no independent reproduction)
Scope:  mixed harnesses; NOT a single controlled head-to-head
```
```text
Figure: Astra — 10 open problems across 8 fields; ~$2,000 total token cost at Sol API
        rates; 249-page manuscript + 62-page account + public Lean 4 certificates
Owner:  OpenAI (openai.com/index/ten-advances-in-mathematics/; github.com/openai/ten-proofs)
Scope:  internal Astra model; human-prepared manuscripts, model-formalized certificates
```
```text
Figure: Astra — resolves Erdős problems 146 and 180; non-sofic group construction;
        sphere-packing upper bounds to the Cohn–Elkies threshold; exponential
        parallel repetition for quantum games
Owner:  OpenAI announcement (specific results); verify each against the manuscript PDF
Scope:  per-problem claims; Lean certificate is machine-checkable, manuscript peer
        review ongoing
```
```text
Figure: arginine/MHC-I — Cell, DOI 10.1016/j.cell.2026.07.020, published Jul 30 2026
Owner:  Wu Q. et al., Cell; Rockefeller PR (Jul 30); independent secondaries
Scope:  mouse study; in-window (window opens ~Jul 30)
```
```text
Figure: atom–QD interference — spectral overlap 0.88; HOM visibility 0.65 ± 0.14;
        ~917 nm (Cs) / 917.48 nm (QD at 12.5 K)
Owner:  Moon & Kim et al., Light: Sci. Appl., DOI 10.1038/s41377-026-02399-y
Scope:  primary online date Jul 15 (pre-window); Jul-30 press wave is syndication
```

## Source assets

```text
Asset: Qwen3.8-Max benchmark comparison table (qwen.ai/blog?id=qwen3.8; JS-gated)
Shows: Alibaba's head-to-head positioning vs GPT-5.6 Sol, Claude Fable 5, Opus 4.8
Crop:  If used, retain the "vendor-reported / mixed harness" caveat and label every
       column as Alibaba's own claim; do not present as a neutral leaderboard.
```
```text
Asset: OpenAI ten-proofs GitHub repo tree + a Lean certificate file (github.com/openai/ten-proofs)
Shows: That the correctness claim is machine-checkable — the certificate files and
       the ComparatorChallenges verification directory are the argument's substance.
Crop:  A file-tree screenshot conveys "public, compilable certificates" better than
       prose; keep the Apache-2.0 / Lean-toolchain context, omit decorative chrome.
```
```text
Asset: arginine/MHC-I graphical abstract (cell.com article page; gated)
Shows: The codon-stalling mechanism — ribosome pausing at arginine codons under
       restriction, cutting MHC-I surface presentation.
Crop:  Retain the tRNA-charging → ribosome-stall → reduced-MHC-I chain; omit journal
       furniture.
```

## Discarded (read far enough to reject, with the reason)

```text
URL: https://deepmind.google/models/gemma/diffusiongemma/ + https://www.marktechpost.com/2026/06/10/... + https://gigazine.net/gsc_news/en/20260611-google-ai-diffusiongemma/ — DiffusionGemma the MODEL was released Jun 10 2026 (MarkTechPost, MLQ, GIGAZINE, NVIDIA blog all June). arXiv:2608.00146 (Jul 31) is a technical report documenting a two-month-old release, not a new this-week development. DROPPED (resolves round-02's open question: an independent secondary now exists, but the release date disqualifies it).
```
```text
URL: https://www.nature.com/articles/s41567-026-03349-6 — Nature Physics Sagnac-phonon rotating-superfluid angular momentum (Frómeta Fernández, Del Pace, Hernández-Rajkov et al.). arXiv 2511.02664 journal-ref "Nat. Phys. (2026)"; online publication ~Jun 26 2026 (pre-window). A companion News & Views "Rotation through sound" (s41567-026-03384-3) exists. DROPPED — pre-window.
```
```text
URL: https://www.nature.com/articles/s41567-026-03348-7 — Nature Physics quantum teleportation over a lossy channel (USTC); July coverage, pre-window. DROPPED.
```
```text
URL: https://www.nature.com/articles/s41377-026-02399-y — atom–quantum-dot two-photon interference; strong and disjoint but primary online date Jul 15 (Jul-30 wave is a press release). Logged as the conditional 4th above, not asserted in-window.
```
```text
URL: https://www.cisa.gov/news-events/alerts/2026/08/03/... — N-able N-central CVE-2026-18577 (CISA KEV Aug 3). In-window but the news is active-exploitation + mandated remediation, a public/security CONSEQUENCE the commission routes to current-events; also echoes the Aug-04 Cisco lead. NOT filed here (per brief).
```
```text
URL: https://techtimes.com/articles/321552/20260725/... (FLUX 3, Black Forest Labs) — released Jul 23 2026; pre-window. DROPPED.
```
```text
URL: aireleasetracker.com/latest + llm-stats.com/ai-news — dated model-release scan for Jul 30–Aug 5 returns only DeepSeek-V4-Flash-0731 (Jul 31, already filed 08-03) and Qwen3.8-Max (keeper). GPT-5.6 Luna/Sol (Jul 9), Kimi K3 (Jul 16), Gemini 3.5/3.6 (Jul 21), Claude Opus 5 (Jul 24) — all pre-window or already filed. No other in-window LLM release.
```
```text
URL: AMD Zen 6 (per techstartups Aug-3 roundup) — forthcoming architecture / roadmap detail, product promotion, no shipping field result. Microsoft Xbox price increase (Aug 1) — consumer business, not a field development. Both out of scope.
```
```text
URL: ScienceDaily Aug 3-5 front page (weight-loss brain set-point; aging/ALS molecular switch; Arctic permafrost carbon; proton-assisted triplet transfer between quantum dots) — surfaced via aggregator ordering; owning primaries older/undated; no clean in-window, practice-changing result located beyond arginine. Re-syndication, not filed.
```
```text
URL: BYD humanoid robot "August unveiling"; Xiaomi Robotics-U0; EY quantum hub (Aug 1) — product-promotion / corporate-milestone shapes without an owning field-result primary + independent verification in-window. Not brief-worthy.
```

## Third-pass conclusion (buildable set for the writer / orchestrator)

**Fully buildable, disjoint, in-window (each: owning primary + independent
secondary, all URLs resolve):**

1. **Qwen3.8-Max** (Alibaba, Aug 3) — primary qwen.ai/blog?id=qwen3.8 (JS-gated,
   figures traced via secondaries); independent secondaries SiliconANGLE, Bloomberg,
   Neowin, implicator.ai, the-decoder. AI model release.
2. **OpenAI Astra "Ten Advances in Mathematics and TCS"** (Aug 1) — primary
   openai.com/index/ten-advances-in-mathematics/ + github.com/openai/ten-proofs
   (Lean 4 certificates, resolve and compilable); independent secondaries The
   Decoder, Quartz (plus TechTimes, Forbes, The Next Web, DataCamp). AI-for-math.
3. **Arginine / MHC-I codon-dependent translation** (Cell, Jul 30) — primary
   cell.com article (DOI 10.1016/j.cell.2026.07.020; page gated 403) + Rockefeller
   University press release (Jul 30, author list + date); independent secondaries
   Science News, Technology Networks, Newsweek, Inside Precision Medicine.
   Immunology / nutrition.

**Set size = 3 clean.** These three are disjoint in field (AI model / AI-for-math /
immunology) and each stands alone.

**Conditional 4th:** the atom–quantum-dot two-photon interference paper (*Light:
Science & Applications*, DOI 10.1038/s41377-026-02399-y) is fully sourced (primary +
independent phys.org and others) and disjoint (quantum networking), but its journal
online date is **Jul 15** — the Jul-30 coverage is a coordinated press wave, not the
publication date. If the orchestrator counts the Jul-30 press wave as the qualifying
event (as it effectively does for arginine, whose Cell date is Jul 30), this makes a
clean **4-item** set. Under a strict primary-date reading of the relaxed window, it
falls out and the honest buildable count stays at **3**.

**Is 4+ achievable?** Yes — but conditionally. Three items are unconditionally
in-window and buildable; the fourth depends on the orchestrator's ruling on whether
a Jul-15 primary with a Jul-30 press wave qualifies under the "~Jul 30–Aug 5" scope.
No fifth qualifying item exists this week without further relaxation. Do not pad.

**One verification note for the writer/editor:** `nb history` returns no records in
this checkout (no library attached; `NB_LIBRARY` empty), so I could not re-confirm
the 08-01…08-04 filings from the tool directly. The non-overlap for the Astra item
rests on round-02's explicit enumeration of those editions (which did not include
Astra) and on Astra being an Aug-1 development freshly surfaced this pass. Before
finalizing, confirm Astra was not already run on the 08-01 or 08-02 tech-news front
page.
