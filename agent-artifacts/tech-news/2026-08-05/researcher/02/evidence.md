# Evidence: tech-news/2026-08-05 (researcher 02)

This is a second evidence pass. The writer found that two of the three round-01
spine items — **DeepSeek-V4-Flash-0731** and **Inkling-Small** — were already
published as full items in `tech-news/2026-08-03`, so they cannot be re-filed as
new. This pass preserves the one round-01 survivor (**Qwen3.8-Max**, Aug 3, and
strengthens its sourcing) and casts a deliberately wide net for at least three
more genuinely-new, in-window, disjoint field developments.

The central finding of this pass is a negative one, and it is load-bearing for
the orchestrator's scope decision: **under a strict "developments dated ~Aug 3-5,
2026" window, fewer than three additional qualifying items exist.** Qwen3.8-Max
(Aug 3) is the only clean, in-window, field-changing, cleanly-owned development
that is disjoint from the 08-01…08-04 editions and from the other desks. The one
other unambiguously in-window item, the N-able N-central CVE (CISA KEV Aug 3), is
an active-exploitation incident that the commission routes to current-events and
that echoes the Aug-04 Cisco security lead. **Every science/health candidate that
surfaces as "August" via ScienceDaily or Nature subject-page ordering traces to an
owning primary dated weeks to months earlier** (HPV gum April; ruptoblasts June;
tungsten-carbide Feb/April; EPS8 Sept 2025; jumping-gene May 7; arginine/MHC-I
Jul 30; the Nature Physics superfluid and teleportation papers June/July). The
in-window arXiv listings (cs.LG/cs.CL, Aug 3 IDs `2608.000xx`) are incremental
method papers with no independent secondary. A near-miss exists just outside the
window on Jul 30-31 (arginine/MHC-I in *Cell*; DiffusionGemma), listed below so
the orchestrator can rule on whether to relax the window to the normal "this week"
wire scope. The exact list of venues and dates checked is in **Second-pass
conclusion**.

The evidence for **what Alibaba announced** in Qwen3.8-Max is strong (multiple
independent newsrooms reproduce the same Aug-3 release, specs, and open-weights
timeline). It is thin exactly where round 01 was thin: the benchmark table is
vendor-published and not independently reproduced, and the owning page
(`qwen.ai/blog`) is still a JavaScript app the fetcher cannot read, so its figures
are traced through secondaries that reproduce Alibaba's own table.

## Round-01 items excluded this pass (already published)

- **DeepSeek-V4-Flash-0731** — filed as a full item in `tech-news/2026-08-03`
  ("DeepSeek's V4-Flash-0731 posts frontier-adjacent coding scores at cents per
  million tokens"), and again as an Open-Models item in `tech-news/2026-08-02`
  ("DeepSeek's V4-Flash exits preview at half its old price"). Excluded.
- **Inkling-Small** — filed as a full item in `tech-news/2026-08-03` ("Thinking
  Machines' Inkling-Small beats its larger teacher on five of six benchmarks").
  Excluded.
- **Qwen3.8-Max** — NOT previously filed. Preserved below as the one keeper.

## Sources

### Keeper: Qwen3.8-Max (Alibaba, Aug 3 2026) — preserved and re-sourced

```text
URL:         https://qwen.ai/blog?id=qwen3.8
Kind:        primary (owner) for what Alibaba announced — NOT DIRECTLY READABLE
Establishes: Alibaba/Qwen's official Qwen3.8-Max announcement and benchmark table
Paraphrase:  The owning page for the Qwen3.8-Max claim. The URL resolves, but the
             page is a JS app; the fetcher returns only the string "Qwen" with no
             body (unchanged from round 01). Every Qwen3.8-Max figure below is
             therefore traced THROUGH secondaries that reproduce Alibaba's own
             table, not read off this page.
Locators:    blog?id=qwen3.8 (JS-gated; body not machine-readable via fetch)
Quote:       (none obtainable from the primary as loaded)
```

```text
URL:         https://www.implicator.ai/alibaba-publishes-the-qwen3-8-max-benchmarks-it-withheld-two-weeks-ago/
Kind:        secondary (industry press; independent account)
Establishes: Aug-3 publication of the benchmark numbers; the preview→release arc
Paraphrase:  Alibaba published benchmark scores for its 2.4T-parameter Qwen3.8-Max
             on Monday (Aug 3 2026), two weeks after claiming at WAIC the model was
             "second only to Claude Fable 5" without releasing any numbers. The
             scores show it broadly competitive with OpenAI and Anthropic models,
             ahead on several coding/multimodal/engineering benchmarks and trailing
             on some general-purpose reasoning tests. NEW this pass: fixes the
             preview-vs-release ambiguity round 01 flagged — the Aug-3 event is the
             release of the withheld numbers, not a fresh preview.
Locators:    lede + benchmark-summary section
Quote:       "two weeks after claiming the model was second only to Claude Fable 5
             without releasing any numbers"
```

```text
URL:         https://the-decoder.com/alibabas-open-weight-qwen3-8-max-takes-on-long-horizon-ai-tasks-with-2-4-trillion-parameters/
Kind:        secondary (independent tech outlet)
Establishes: Specs, positioning, and the autonomous-coding demonstration detail
Paraphrase:  Qwen3.8-Max is 2.4T total / 95B active, built on the Qwen3.5
             architecture, aimed at coding, research, professional and multimodal
             work, and positioned as Alibaba's first Max-scale model slated for
             open weights. NEW this pass: the company-run oh-my-cli autonomous-run
             is quantified — ~16 days producing 265 commits, 127 pull requests, and
             151 issues. Available now via QwenCloud; weights "due on Hugging Face
             and ModelScope next week."
Locators:    specs paragraph + autonomous-coding paragraph + availability note
Quote:       "2.4 trillion parameters with 95 billion active"
```

```text
URL:         https://www.neowin.net/news/alibaba-releases-qwen38-max-challenging-gpt-56-sol-and-claude-fable-5-on-ai-benchmarks/
Kind:        secondary (independent tech outlet)
Establishes: Independent confirmation of the Aug-3 release and the competitive claim
Paraphrase:  Reports the Aug-3 release of Qwen3.8-Max challenging GPT-5.6 Sol and
             Claude Fable 5 on published benchmarks. Independent confirmation of the
             RELEASE and the CLAIM, not of the numbers.
Locators:    headline + lede
Quote:       (headline) "Alibaba releases Qwen3.8-Max, challenging GPT-5.6 Sol and
             Claude Fable 5 on AI benchmarks"
```

```text
URL:         https://www.testingcatalog.com/qwen-released-qwen3-8-max-with-open-weights-coming-soon/
Kind:        secondary (independent tech outlet) — carried from round 01
Establishes: Aug-3 release date; open-weights timeline; license still unnamed
Paraphrase:  Qwen3.8-Max announced Aug 3 2026 at 2.4T total / 95B active; open
             weights for Max (and a smaller Qwen3.8 variant) scheduled "the
             following week" on Hugging Face and ModelScope, with no license named
             yet. Points to qwen.ai/blog?id=qwen3.8 as the source.
Locators:    opening + "open weights coming soon" paragraphs
Quote:       "open weights ... scheduled for the following week on Hugging Face and
             ModelScope"
```

```text
URL:         https://www.bloomberg.com/news/articles/2026-08-03/alibaba-drops-another-china-ai-model-with-breakthrough-performance
Kind:        secondary (reputable US newsroom; paywalled) — carried from round 01
Establishes: Independent confirmation Alibaba shipped Qwen3.8-Max Aug 3
Paraphrase:  Bloomberg reports Alibaba released its largest model, Qwen3.8-Max,
             claiming benchmark scores rivaling Anthropic and ranking above
             Moonshot's Kimi K3. Independent confirmation of the RELEASE and CLAIM,
             not a reproduction of the benchmarks.
Locators:    headline + lede (full text paywalled)
Quote:       (headline) "Alibaba's Qwen3.8-Max AI Model Claims Benchmark Scores
             Rivaling Anthropic"
```

### New in-window item (contested desk fit): N-able N-central CVE-2026-18577

```text
URL:         https://www.cisa.gov/news-events/alerts/2026/08/03/cisa-adds-one-known-exploited-vulnerability-catalog
Kind:        primary (US CISA Known Exploited Vulnerabilities action)
Establishes: The one clean, unambiguously Aug-3 field-adjacent security event
Paraphrase:  On Aug 3 2026 CISA added CVE-2026-18577, an N-able N-central
             authentication-bypass flaw, to its Known Exploited Vulnerabilities
             catalog. N-able reports exploitation in the wild since Aug 1 2026;
             the flaw is an incomplete-patch regression of CVE-2026-18556, lets an
             attacker bypass authentication and take over N-central servers, then
             abuse the built-in Take Control feature to pivot into managed
             endpoints (cloudflared deployed for persistence). CVSS 8.2. Fixed in
             N-central 2026.3.1.7 (shipped Aug 2); FCEB agencies directed to patch
             by Aug 6.
Locators:    CISA alert body + KEV entry
Quote:       (KEV) "N-able N-central Authentication Bypass Vulnerability"
DESK NOTE:   The news here is active exploitation and mandated remediation — a
             public/security CONSEQUENCE, which the commission routes to
             current-events. It also echoes the Aug-04 Cisco FMC security lead.
             Logged as in-window, but a poor fit for a disjoint tech-news field
             brief. Independent secondaries: Rapid7, BleepingComputer, The Hacker
             News, securityaffairs (all early Aug 2026).
```

### Near-miss (just outside window; strong primary): arginine / MHC-I translation

```text
URL:         https://www.cell.com/cell/abstract/S0092-8674(26)00818-4
Kind:        primary (peer-reviewed research paper, Cell)
Establishes: A genuine field result, but dated JUL 30 2026 — outside Aug 3-5
Paraphrase:  Wu Q. et al., "Dietary arginine drives codon-dependent MHC class I
             translation and improves immunity in colon tumorigenesis and
             respiratory viral infection," Cell (2026), DOI
             10.1016/j.cell.2026.07.020, published Jul 30 2026. In mice, a
             high-arginine diet reduced colon tumors and improved outcomes in
             influenza and SARS-CoV-2 infection; arginine starvation stalls the
             ribosome on the arginine-rich MHC-I message, cutting antigen
             presentation and immune surveillance. Mechanistically novel and
             disjoint from every filed item; NOT previously filed. Multiple
             independent secondaries (Science News, Newsweek, Technology Networks,
             News-Medical). Disqualifier for THIS brief: Jul 30, not Aug 3-5;
             ScienceDaily's Aug-3 re-post is syndication, not the development date.
Locators:    abstract + graphical abstract
Quote:       "codon-dependent MHC class I translation"
```

### Near-miss (just outside window; no independent secondary): DiffusionGemma

```text
URL:         https://arxiv.org/abs/2608.00146
Kind:        primary (arXiv technical report)
Establishes: A disjoint-shape AI development, but dated JUL 31 2026 and unverified
Paraphrase:  "DiffusionGemma Technical Report" (DiffusionGemma Team, 43 authors;
             no institutional affiliation stated in the abstract, though the Gemma
             lineage implies Google). Submitted Jul 31 2026. A discrete-diffusion
             language model that refines blocks of 256 tokens in parallel to avoid
             sequential decoding, claiming ~1,500 output tokens/sec on a single
             NVIDIA H100 — "substantially faster than AR models." Disjoint in shape
             from Qwen (diffusion vs autoregressive MoE). Disqualifiers for THIS
             brief: dated Jul 31 (pre-window); NO independent secondary found;
             affiliation unconfirmed; the throughput figure is the authors' own.
             A current-week diffusion item would not clash with paper-of-the-day
             (that desk reconstructs the 2020 DDPM paper), but this one is not
             clean enough to hand the writer.
Locators:    abstract
Quote:       "iteratively refines blocks of 256 tokens in parallel"
```

## Contradictions

- **Qwen3.8-Max: preview vs release (resolved this pass).** Round 01 left this
  split. implicator.ai resolves it: Alibaba first claimed Qwen3.8-Max at WAIC
  ("second only to Claude Fable 5") *without numbers*; the Aug-3 event is the
  publication of those withheld benchmarks and the open-weights promise. As of the
  Aug-5 research window, weights are still NOT on Hugging Face or ModelScope ("due
  next week") and no license is named. The Aug-3 news is the benchmark claim plus
  the open-weights commitment, not a downloadable frontier model.

- **Qwen3.8-Max: vendor claim vs independent reproduction (unchanged).** Every
  Qwen3.8-Max headline figure is Alibaba's own table on mixed harnesses; no
  independent reproduction surfaced. Treat all benchmark numbers as vendor-reported
  for "whether it is true," primary only for "what was announced."

- **"August" science is mostly re-syndication (the pass's key methodological
  finding).** ScienceDaily's Aug 3-5 front page and Nature's physics/biology
  subject-page "recent" ordering both surface items whose OWNING primaries are
  weeks-to-months old. Verified disqualifying dates: HPV chewing gum (Daniell,
  Penn, *Scientific Reports*) ≈ April 2026; ruptoblasts/exploding immune cells
  (Rosental & Wang, *Cell*) ≈ June 2026; 3D-printed WC-Co (Hiroshima, *Int. J.
  Refractory Metals*) Feb/April 2026; EPS8 aging protein (*Nature Aging*) Sept 3
  2025; jumping-gene circular-intron RNA (*Scientific Reports*) May 7 2026;
  arginine/MHC-I (*Cell*) Jul 30 2026; Nature Physics teleportation-over-lossy-
  channel (phys.org coverage July 2026) and the Sagnac-phonon superfluid paper
  (arXiv preprint 2511.02664, Nov 2025; Nature online date unverifiable — see
  Discarded). None of these is an Aug 3-5 development.

## Numbers

```text
Figure: Qwen3.8-Max — 2.4T total parameters / 95B active (MoE), Qwen3.5 architecture
Owner:  Alibaba/Qwen (qwen.ai/blog?id=qwen3.8; via implicator.ai, the-decoder, testingcatalog)
Scope:  model size; active per forward pass. Owner page JS-gated — traced via secondaries.
```
```text
Figure: Qwen3.8-Max — released Mon Aug 3 2026; open weights "due next week" on HF/ModelScope
Owner:  Alibaba (via implicator.ai, testingcatalog, neowin); weights NOT yet posted as of Aug 5
Scope:  release date + open-weights timeline; license unnamed
```
```text
Figure: Qwen3.8-Max — oh-my-cli autonomous run: ~16 days, 265 commits, 127 PRs, 151 issues
Owner:  Alibaba company-run test (via the-decoder); vendor demonstration, not independent
Scope:  single company-run agentic coding demo
```
```text
Figure: Qwen3.8-Max — Terminal-Bench 2.1 86.6; SWE-bench Pro 67.7; PaperBench 93.0;
        FrontierSWE 73.5; CoWorkBench 74.8; WideSearch 81.9 (round-01 table, unchanged)
Owner:  Alibaba's own published table (vendor-reported; no independent reproduction)
Scope:  mixed harnesses; NOT a single controlled head-to-head; open weights not yet out
```
```text
Figure: N-able N-central CVE-2026-18577 — CVSS 8.2; exploited in the wild since Aug 1;
        added to CISA KEV Aug 3; fixed in 2026.3.1.7; FCEB deadline Aug 6
Owner:  CISA (KEV) + N-able advisory; secondaries Rapid7, BleepingComputer
Scope:  in-window security event, but current-events-shaped (see desk note)
```
```text
Figure: (near-miss) arginine/MHC-I — Cell, DOI 10.1016/j.cell.2026.07.020, published Jul 30
Owner:  Wu Q. et al., Cell; multiple independent secondaries
Scope:  mouse study; OUT of Aug 3-5 window
```
```text
Figure: (near-miss) DiffusionGemma — ~1,500 output tokens/sec on one H100; 256-token blocks
Owner:  DiffusionGemma Team, arXiv:2608.00146, submitted Jul 31; vendor-claimed, no secondary
Scope:  OUT of window; unverified
```

## Source assets

```text
Asset: Qwen3.8-Max benchmark comparison table (qwen.ai/blog?id=qwen3.8; JS-gated)
Shows: Alibaba's head-to-head positioning vs GPT-5.6 Sol, Claude Fable 5, Opus 4.8
Crop:  If used, retain the "vendor-reported / mixed harness" caveat and label every
       column as Alibaba's own claim; do not present as a neutral leaderboard.
```
```text
Asset: CISA KEV catalog entry for CVE-2026-18577 (cisa.gov, Aug 3 2026)
Shows: The date and mandated-remediation status of the one clean in-window security event
Crop:  Only if the writer files the security item; keep the "active exploitation /
       incomplete patch of CVE-2026-18556" framing.
```

## Discarded (read far enough to reject, with the reason)

```text
URL: https://www.sciencedaily.com/releases/2026/08/260803080917.htm — HPV chewing gum 93%; owning primary (Daniell, Penn, Scientific Reports) is ~April 2026. Re-syndication, not an Aug 3-5 development.
URL: https://www.eurekalert.org/news-releases/1130267 — ruptoblasts / exploding immune cells (Rosental & Wang, Cell); owning primary ~June 2026. Out of window.
URL: https://www.sciencedaily.com/releases/2026/08/260801094053.htm — 3D-printed tungsten-carbide-cobalt (Hiroshima, Int. J. Refractory Metals); Feb/April 2026 primary. Out of window.
URL: https://www.nature.com/articles/s43587-025-00943-w — EPS8 aging protein (Nature Aging); published Sept 3 2025. Old.
URL: https://www.pnas.org/doi/10.1073/pnas.2517741122 and https://www.nature.com/articles/s41567-026-03332-1 — Trichoplax cilia folding; June 2026. Out of window.
URL: https://www.cell.com/cell/abstract/S0092-8674(26)00818-4 — arginine/MHC-I; Cell, Jul 30 2026. Strong but pre-window (logged as near-miss above).
URL: https://arxiv.org/abs/2608.00146 — DiffusionGemma; Jul 31 2026, no independent secondary (logged as near-miss above).
URL: https://www.nature.com/articles/s41567-026-03348-7 — quantum teleportation over lossy channel (USTC); phys.org coverage dated July 2026 → published July, not Aug 3-5.
URL: https://www.nature.com/articles/s41567-026-03349-6 — Sagnac-phonon rotating-superfluid angular momentum; arXiv preprint 2511.02664 (Nov 2025); Nature online "Published:" date could not be read (nature.com redirects fetch to idp.nature.com auth), so an Aug 3-5 date could NOT be confirmed. Not asserted.
URL: arxiv.org/list/cs.LG/2026-08 and cs.CL/2026-08 (Aug-3 IDs 2608.00019, .00129, .00220, .00632, .00859, .00036) — incremental method papers (distillation compression, KAN sparsification, verifier reshaping, long-doc benchmark). In-window but no field-changing headline result and no independent secondary. Not brief-worthy.
URL: MLPerf Inference v6.0 (mlcommons.org, April 2026); AMD MI355X 1M tok/s (early July); Arm AGI CPU (March); AMD Advancing AI / MI455X (Jul 23); Marvell FMS 2026 showcase (Aug 4-6 trade-show, product promotion) — no in-window chip/systems field result.
URL: Google DeepMind WeatherNext 2 / AlphaProof — not new this week (AlphaProof IMO result was July).
URL: Wired/Irregular "OpenAI model exploited a website after a security lab gave it internet access" (Aug 4) — same incident class as the Anthropic cyber-eval story already filed on 08-03; an incident, routes to current-events.
URL: N-able N-central CVE-2026-18577 (Aug 3) — in-window but current-events-shaped and echoes the Aug-04 Cisco lead (logged above, not recommended as a field item).
```

## Second-pass conclusion (scope decision for the orchestrator)

**A disjoint 4-6 item brief is NOT reliably buildable under a strict "Aug 3-5,
2026, field-development" reading.** After a wide search I have exactly one clean
keeper — **Qwen3.8-Max (Aug 3)** — plus one contested in-window item (**N-able
CVE**, better owned by current-events). That is not enough for the `brief` band.

Venues checked (dates found in parentheses):
- `nb history` full text for tech-news 08-01, 08-02, 08-03, 08-04 — enumerated
  every filed item; DeepSeek-V4-Flash-0731 and Inkling-Small confirmed already
  filed (08-03); Kimi K3, GPT-5.6 Sol serving, Gemini Robotics 2, IETF TLS RFC,
  Claude/HAWK crypto, HRL quantum EC, and the Deramiocel Phase-3 health item all
  already filed (08-01/08-02).
- arXiv cs.LG/2026-08 and cs.CL/2026-08 new listings (Aug-3 submissions) —
  incremental only.
- ScienceDaily front page, 16 items dated Aug 3-5 — all re-syndications of
  April→July 2026 (and one Sept 2025) primaries.
- Nature and Nature Physics subject/issue pages — superfluid (Nov-2025 preprint,
  Nature date unverifiable), teleportation (July), Trichoplax (June).
- Chips/systems (MLCommons, AMD, Arm, Marvell) — April→July, or Aug trade-show
  promotion.
- Security (CISA KEV, N-able, Cisco) — only N-able is in-window, and it is
  current-events-shaped.
- Google DeepMind, and AI-lab research blogs — nothing new and field-changing in
  window.

**Options for the orchestrator, in order of cleanliness:**
1. **Relax the window to the normal "this week" wire scope (~Jul 30-Aug 5).** This
   admits **arginine/MHC-I in *Cell* (Jul 30)** — a strong, well-sourced, disjoint
   immunology/nutrition result that was NOT previously filed — and, more weakly,
   **DiffusionGemma (Jul 31)**, a diffusion-LM technical report disjoint in shape
   from Qwen but lacking an independent secondary. Even so, that reaches only
   Qwen + arginine as clean items (2), plus DiffusionGemma and the N-able CVE as
   contested/weak items (making 3-4 with caveats). A genuinely disjoint 4-item set
   under this relaxation would be: Qwen3.8-Max (AI model), arginine/MHC-I (health),
   DiffusionGemma (AI systems/inference, if a secondary is accepted or found), and
   the N-able CVE (security, if the current-events boundary is waived for it).
2. **Reduce the item count** for this date if the band allows a floor below 4.
3. **Accept the vendor technical report and/or the current-events-leaning security
   item** to reach 4, with the caveats recorded above.

My recommendation: pursue option 1 with the arginine/MHC-I *Cell* paper as the
second clean spine item, and commission a targeted third pass to (a) find an
independent secondary for DiffusionGemma or confirm its affiliation, and (b)
confirm the Nature Physics Sagnac-superfluid paper's exact online-publication date
via a non-fetch-blocked mirror (e.g., the DOI landing or a physics-news secondary),
since if that date is Aug 3-5 it would add a genuinely in-window, disjoint physics
item.
