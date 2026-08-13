# Evidence: tech-news/2026-08-13 (researcher/02, complete record)

This record supersedes researcher/01 for citation purposes; it carries forward
that round's still-valid work and adds this round's four targeted findings. The
evidence now supports four items at full strength, each with a source-owned
primary and at least one independently-opened secondary: an AI-discovered
zero-click Zoom exploit chain (disclosed 2026-08-11), Meta's open-weight,
single-GPU Muse Glimmer agent model — now grounded in Meta's own primary
announcement, closing round 01's gap — (2026-08-10), IBM/Together AI's $240M
Nvidia-backed inference cluster (2026-08-11, now with two independently-opened
secondaries), and a new item: a Nature paper on glucose-responsive engineered
probiotics for diabetes control in mice and monkeys (published online
2026-08-12). The Nvidia $500B-plus AI-compute-financing item is verified as
accurate and internally consistent, but this round's dating check finds it is
the same single event as round 01 recorded (Nvidia's own August 10 MOU release)
and that its substance was fully reported and analyzed across major outlets
before August 12 — Fortune's 08-12 "circular financing" piece and
Tradingpedia's 08-12 write-up both rehash the August 10 announcement rather
than report a new dated action. No 08-13-dated development was found. This
matches the brief's own drop condition ("if it is a repeat of the 08-12
coverage, drop or replace it"), so this record recommends the writer/editor
treat Nvidia's financing platform as a background reference rather than a
standalone item for the 2026-08-13 slate — see Contradictions and the report
below for the full reasoning, since the call is close enough that the
orchestrator may weigh it differently. The probiotics item is scientifically
solid and clearly dated, but its only independently-opened secondary is
Nature's own podcast/news page (editorially separate from the paper's authors,
but same publisher); no outside-Nature press coverage was found within this
round's budget, likely because the paper is very fresh. Exact quantitative
results (magnitude of glycemic control) sit behind Nature's paywall and are not
recorded as numbers here for that reason.

### Sources

Carried forward unchanged from researcher/01 (still valid, still fully
opened): the A Security Zoomsday writeup, Zoom's ZSB-26015 bulletin, the
TechRepublic Zoomsday secondary, Nvidia's own financing-platform release, the
SiliconANGLE Nvidia secondary, the IBM/Together AI newsroom release, the
CloudSEK LiteLLM report (offered to current-events, not this slate), and
Google's DeepMind-reshuffle post (excluded as stale — see Discarded). Full
entries for those are in researcher/01/evidence.md and are not repeated here
except where this round adds to them; nothing about them changed.

```text
URL:         https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
Kind:        Primary — Meta's own research blog (credited to Meta
             Superintelligence Labs), announcing Meta's own model release.
             This closes researcher/01's principal gap: no Meta-owned primary
             had been located and opened as of that round.
Establishes: Muse Glimmer's release by Meta Superintelligence Labs, 30B
             parameters, Apache 2.0 license, that it is trained on Muse
             Spark's outputs via logit distillation (teacher-student
             relationship confirmed in Meta's own words, not just secondary
             inference), hardware envelope (24GB/32GB memory footprint with
             ~4-bit quantization, tested on MacBook M4-Max, M5-Max, and
             RTX-5090), capabilities (agentic task completion, tool use,
             multi-step reasoning, failure recovery, multimodal text+image
             input, scaffold compatibility including OpenClaw, controllable
             reasoning effort, 100+ languages), and specific speculative-
             decoding speedups from Meta's DFlash technique (3.1x on
             RTX-5090, 1.8x on M5-Max, 1.5x on M4-Max).
Paraphrase:  Meta says Glimmer is distilled from its larger, closed Muse
             Spark model to bring near-frontier agentic capability to
             consumer hardware, and reports it outperforming Gemma4-31B and
             Qwen3.6-27B on agentic, coding, multimodal, safety, and
             reasoning benchmarks (Meta's own comparison; no independent
             benchmark re-run found in any source read this round or last).
Locators:    Publication date August 10, 2026, per the fetched page. Sections
             covering model architecture, hardware requirements, benchmark
             comparisons, and the DFlash speedup figures.
Quote:       None recorded beyond the paraphrase above; the page's framing
             language did not surface a load-bearing quote distinct from the
             facts already captured.
```

```text
URL:         https://developer.meta.com/ai/models/muse-glimmer/
Kind:        Primary — Meta's own official developer/model-card page,
             confirmed by Meta branding and links to Meta's own Hugging Face
             and GitHub organization (meta-models).
Establishes: Corroborates model size (30B), license (Apache 2.0), and the
             single-consumer-GPU/Mac deployment claim from Meta's own model
             card, independent of the research-blog framing. Links out to
             Meta's Hugging Face (meta-models/Muse-Glimmer-30B and variants)
             and deployment integrations (Ollama, vLLM, llama.cpp).
Paraphrase:  Positions Glimmer as "an open model built for always-on local
             agents" — Meta's own product framing for the release, distinct
             from Meta Superintelligence Labs' more technical research-blog
             framing.
Locators:    Full page as fetched; no internal date stamp surfaced in the
             fetched text, but content and cross-links are consistent with
             the August 10, 2026 research-blog date above.
Quote:       "An open model built for always-on local agents" — page framing
             line, Meta's own.
```

```text
URL:         https://www.bnnbloomberg.ca/business/2026/08/11/ibm-together-ai-ink-240-million-deal-for-nvidia-powered-ai-inference-cluster/
Kind:        Secondary — wire reporting (Reuters byline, carried by BNN
             Bloomberg), independent of IBM, Together AI, and Nvidia.
             Superseding researcher/01's flag on this source: fully opened
             this round, not search-synthesis only.
Establishes: Independent confirmation of the $240M figure and the Nvidia
             HGX B300 + Spectrum-X hardware; adds specificity not in IBM's
             own release — approximately 2,000 Nvidia Blackwell B300 chips
             in the initial US deployment — and a demand claim from Together
             AI's own chief revenue officer, Kai Mak, that capacity will be
             "sold out at least two to three months ahead of time."
             Independently confirms Together AI's $8.3B valuation as of July
             2026 and that it serves open-source models including DeepSeek,
             MiniMax, and Kimi.
Locators:    Full article body, dated August 11, 2026.
Quote:       "We think this will be sold out at least two to three months
             ahead of time." — Kai Mak, Together AI chief revenue officer.
```

```text
URL:         https://thenextweb.com/news/ibm-together-ai-240m-nvidia-inference-cluster
Kind:        Secondary — independent tech-news analysis (The Next Web,
             byline Cristian Dina), no stake in the deal.
Establishes: Independent confirmation of the $240M figure, hardware, and
             Together AI's reported ~400 trillion tokens/month inference
             volume. Adds competitive-positioning analysis not present in
             IBM's release: frames the deal as IBM competing on
             inference-cost economics rather than raw scale against AWS,
             Microsoft, and Google, and cites Nebius's separate $643M
             acquisition of an inference-optimization team as independent
             market evidence that "shaving cost per token is where the
             margins now live" (the outlet's own framing, not a quote from a
             deal party).
Locators:    Full article body, dated August 11, 2026.
Quote:       None load-bearing beyond the paraphrase above.
```

```text
URL:         https://www.nature.com/articles/s41586-026-10909-6
Kind:        Primary — the research paper itself (Guan, Kong, Gao, Ye et al.,
             East China Normal University Shanghai Key Laboratory of
             Regulatory Biology and Institute of Biomedical Sciences; with
             Shangang Zhao, University of Texas Health Science Center at San
             Antonio), published in Nature. This is the paper that owns the
             finding — the development the commission asks the researcher to
             treat as the article-worthy event in its own right.
Establishes: An engineered, orally-delivered probiotic ("GIFT") carrying a
             synthetic glucose-responsive gene circuit (built on the
             glucose-responsive transcriptional regulator HexR and a
             synthetic promoter) that transiently colonizes the gut and
             expresses a therapeutic transgene (GLP-1) only when blood
             glucose exceeds a threshold. Tested across multiple diabetic
             mouse models (db/db, diet-induced-obese) and in non-human
             primates with type 2 diabetes. Reports glycemic control,
             improved lipid profiles, and attenuated hepatic, renal, and
             colonic diabetic complications with long-term oral dosing.
             States the platform requires no cell transplantation and no
             external signal to control dosing, unlike prior engineered-cell
             approaches.
Paraphrase:  The paper frames its contribution as a "programmable, orally
             deliverable sense-and-respond platform for metabolic therapy
             without transplantation" — its own stated advance over prior
             engineered-cell diabetes therapies that needed either external
             triggering or surgical implantation.
Locators:    Published online August 12, 2026 (per the fetched abstract
             page). Figures 2 through 5 cover db/db mice, DIO mice, and
             non-human primate results respectively, per the fetched table
             of contents; Extended Data Figures 1-10 hold the granular
             metabolic measurements. The full-text numeric results (exact
             glucose/HbA1c magnitudes, animal counts per group, exact study
             duration beyond an approximate 30-day mouse-study window
             visible in figure descriptions) sit behind Nature's paywall and
             were not independently retrieved this round — see Numbers and
             Limitation below. The abstract and bibliographic/author/
             affiliation data are open and were read in full.
Quote:       "a programmable, orally deliverable sense-and-respond platform
             for metabolic therapy without transplantation" — the paper's
             own framing of its advance, from the abstract.
```

```text
URL:         https://www.nature.com/articles/d41586-026-02521-5
Kind:        Secondary — Nature's own news/podcast desk (bylined to Nick
             Petrić Howe and Benjamin Thompson, Nature Podcast hosts), which
             is editorially independent of the research paper's authors and
             has no authorship stake in the finding, though it shares a
             publisher with the primary. Treated as secondary under the
             authorship-and-stake test in the researcher brief, and recorded
             as this item's weaker secondary — see Limitation.
Establishes: Independent (of the paper's authors) confirmation that the
             study tested mice and monkeys and that the probiotic lowered
             elevated blood sugar in those animal trials. Frames it in
             plain-language terms as "a living diabetes treatment."
Paraphrase:  Restates the paper's headline finding for a general-audience
             podcast segment; the fetched page (a podcast-episode landing
             page, segment 00:45-08:03) did not surface independent expert
             commentary distinct from the paper's own framing.
Locators:    Published August 12, 2026, per the fetched page.
Quote:       None beyond "a living diabetes treatment," a descriptive label
             rather than a load-bearing claim.
```

```text
URL:         https://fortune.com/2026/08/12/nvidia-private-capital-deal-circular-financing-ai-boom/
Kind:        Secondary — independent financial-press analysis (Fortune), no
             stake in Nvidia's deal. Opened this round specifically to test
             researcher/01's dating for the Nvidia financing item, per this
             round's brief.
Establishes: That this piece is analysis of, not a new development
             following, the August 10 MOU: it opens by referencing "on
             Monday, Nvidia announced" (August 10, 2026 was a Monday) the
             same six-partner $500B+ arrangement round 01 already recorded.
             Adds an analytical angle — how Apollo, KKR, and peers can
             structure or place debt with retirement and insurance capital
             they manage — and a countervailing view from Morgan Stanley
             analyst Joseph Moore that the structure eases circular-
             financing concern because third-party investors, not Nvidia,
             supply most of the capital.
Paraphrase:  Continues the running commentary on the August 10 announcement;
             introduces no new dollar figure, no new partner, and no new
             dated corporate action.
Locators:    Full article body, dated August 12, 2026.
Quote:       None recorded as load-bearing; the Moore attribution is
             captured under Establishes.
```

```text
URL:         https://www.tradingpedia.com/2026/08/12/nvidia-advances-on-major-ai-financing-drive/
Kind:        Secondary — independent trade-press coverage, no stake in the
             deal. Opened this round for the same dating check.
Establishes: That the one genuinely new fact in this August 12 piece is
             unrelated to the $500B financing-platform item: a separate,
             reported-but-not-yet-primary-confirmed Nvidia investment of up
             to $3 billion in Lancium, a Blackstone-backed power-
             infrastructure company (an initial $2B for roughly 20%
             ownership, a further $1B contingent on milestones). The
             remainder of the piece "rehashes" (its own reporting's
             substance, not new to it) the August 10 financing-platform
             announcement with added analyst commentary from Wells Fargo and
             market context ahead of CPI data.
Paraphrase:  Confirms, by omission, that no new fact about the six-partner
             $500B+ platform itself surfaced on August 12 — only continued
             analysis of the August 10 event, plus an adjacent but distinct
             Lancium transaction this record did not independently verify
             against a primary (no Nvidia- or Lancium-owned release was
             located or opened this round; time did not allow it within this
             gap-filling round's scope).
Locators:    Full article body, dated August 12, 2026.
Quote:       None recorded.
```

### Contradictions

- Carried forward from researcher/01: the DeepMind/Jeff Dean reshuffle dating
  discrepancy (resolved as stale, excluded from slate) and the LiteLLM-breach
  organization-count discrepancy (2,500+ per CloudSEK vs. 2,100+ per an
  unopened Hacker News snippet; item is offered to current-events, not this
  slate, so this is recorded for completeness only).
- New this round: the Nvidia $500B-plus financing-platform item is internally
  consistent and was not contradicted on its facts by any source read. The
  issue this round surfaces is not a factual contradiction but a dating one:
  the brief asked whether this item is a datable 2026-08-13-adjacent
  development or a repeat of coverage that had already fully surfaced by
  2026-08-12. Having opened the August 12 Fortune and Tradingpedia pieces
  specifically to test this, the finding is that both are continued analysis
  of the same August 10 MOU, not new dated actions. Under the brief's own
  instruction ("if it is a repeat of the 08-12 coverage, drop or replace
  it"), this record flags the item as failing that freshness test as a
  standalone item, three days out from the 2026-08-13 dateline with its
  substance unchanged since August 10. It is not in this paper's
  do-not-repeat list (it has not been run by this paper before), which is the
  strongest argument for keeping it; the researcher notes both readings so
  the orchestrator can make the editorial call the commission reserves for
  that role.
- No contradiction found on the Muse Glimmer, IBM/Together AI, or
  glucose-responsive-probiotic figures across the sources read this round.

### Numbers

Carried forward from researcher/01 without change: the Zoomsday timeline
figure, CVE-2026-53413's CVSS score, the Nvidia $500B+ figure and scope, the
IBM $240M/Q1 2027 figure, and the CloudSEK exposure figures. See
researcher/01/evidence.md for those four entries; nothing about them changed
this round except the editorial-freshness question on the Nvidia item, noted
above under Contradictions, not under Numbers, since no number itself is in
dispute.

```text
Figure: 30 billion parameters; single consumer GPU (24GB/32GB memory
        envelope, ~4-bit quantized); Apache 2.0 license
Owner:  Meta (Meta Superintelligence Labs research blog and Meta's own
        developer.meta.com model page, both opened this round)
Scope:  Now owned by a directly-opened Meta primary, closing researcher/01's
        gap, which had this figure sourced to secondary reporting only.
```

```text
Figure: Nvidia HGX B300-based cluster (~2,000 Blackwell B300 chips in the
        initial US deployment); $240 million multi-year deal value; Q1 2027
        target availability
Owner:  IBM (newsroom.ibm.com release) for the deal value and hardware
        family; the ~2,000-chip figure and "sold out two to three months
        ahead" demand claim are owned by BNN Bloomberg/Reuters reporting
        (Kai Mak of Together AI, quoted there) — not independently
        restated in IBM's own release, so attributed to the reporting that
        carries it, not treated as IBM's own figure.
Scope:  Same scope as researcher/01: this is IBM and Together AI's deal
        specifically, not Together AI's separately reported $8.3B valuation
        or 400-trillion-tokens/month volume, which are context, not this
        deal's own figures.
```

```text
Figure: No precise magnitude recorded.
Owner:  Would be owned by Guan et al. (Nature, s41586-026-10909-6), but the
        exact glycemic-control magnitude (e.g., percentage blood-glucose
        reduction, HbA1c change) sits in the paywalled full text and
        Extended Data figures, which this round's fetch could not retrieve.
Scope:  What is confirmed, openly, from the abstract: efficacy shown across
        multiple diabetic mouse models (db/db, diet-induced-obese) and
        non-human primates with type 2 diabetes, with "clear improvements"
        in lipid profiles and attenuated diabetic complications on
        long-term oral dosing — the paper's own qualitative language, not a
        number. If the writer needs a numeric figure for this item, it must
        be independently retrieved from the full text or Source Data files
        before publication; do not estimate or infer one from the abstract.
```

### Source assets

Carried forward from researcher/01 without change: the Zoomsday disclosure-
timeline asset and the Nvidia six-partner AUM-scale asset (the latter's
usefulness is now conditional on whether the Nvidia item runs at all — see
Contradictions).

```text
Asset: Meta's own Glimmer research post reports head-to-head benchmark
       comparisons against Gemma4-31B and Qwen3.6-27B across five
       categories (agentic, coding, multimodal, safety, reasoning), and a
       three-platform DFlash speedup comparison (RTX-5090, M5-Max, M4-Max).
Shows: How Meta itself frames Glimmer's competitive position among
       similarly-sized open models, and the concrete speed gain from its
       speculative-decoding technique on real consumer hardware.
Crop:  A speedup comparison across the three platforms would carry the
       "runs well on hardware you own" argument better than restating the
       memory-footprint prose; omit the full five-category benchmark table,
       which is Meta's own comparison set and not independently verified —
       flag it as Meta-reported if used at all.
```

```text
Asset: The Guan et al. paper's Figures 2-5 (per the fetched table of
       contents) show db/db mouse, DIO mouse, and non-human primate results
       as a progression — the same intervention validated in successively
       more translationally relevant models.
Shows: The mouse-to-primate escalation is itself the evidentiary structure
       of the paper's claim; a reader can see why the authors call this
       sense-and-respond control rather than a single-model proof of
       concept.
Crop:  Not independently confirmed beyond the figure list and captions
       visible in the open abstract page; the writer/editor would need the
       full-text figures themselves (paywalled) before using this as a
       visual asset, not just this record's description of what the table
       of contents lists.
```

### Discarded

Carried forward from researcher/01 without change (DeepMind/Dean reshuffle
sources, Kimi K3 sandbox-escape coverage, DARPA VENOM, the earlier failed
nature.com dcLVA/Alzheimer's fetch, Gemini's 1-billion-user milestone,
Lovable's funding round, and California's suspense-calendar votes — see
researcher/01/evidence.md for the full list and reasons).

```text
URL: https://venturebeat.com/technology/meta-returns-to-open-source-with-muse-glimmer-an-apache-2-0-licensed-30b-parameter-ai-model-optimized-for-agents-available-now — retried this round, again returned HTTP 429 (rate limited). Not opened in either round; do not cite. No longer load-bearing, since Meta's own primary is now open and TechCrunch (researcher/01, fully opened) remains available as the item's independent secondary.
URL: https://developer.nvidia.com/blog/run-local-agentic-ai-workflows-with-metas-muse-glimmer-on-nvidia/ — surfaced in this round's search but not opened; would be Nvidia's own secondary technical coverage of running Glimmer on its hardware, potentially useful context but not needed once Meta's own primary was located, and not verified this round.
URL: https://huggingface.co/blog/muse-glimmer and https://huggingface.co/meta-models/Muse-Glimmer-30B — surfaced but not opened this round; likely a second Meta-owned primary (Hugging Face org "meta-models"), redundant with the two Meta pages already opened and cited above, so not pursued further under this round's time budget.
URL: https://www.tradingpedia.com's Lancium sub-claim (Nvidia's reported up-to-$3B Blackstone/Lancium investment) — read only via the Tradingpedia secondary above; no Nvidia- or Lancium-owned primary located or opened this round. Recorded as a discrete, distinct-from-the-$500B-platform fact, not verified enough to cite as its own item, and not needed for the $500B item's own sourcing either way.
URL: Nature News search results for other August 13, 2026 issue items (spin-qubit device advances across four teams; anelloviruses and long COVID; rainforest insect cataloguing megaproject; lithium-extraction methods) — surfaced via WebSearch snippets only, not opened. The spin-qubit story in particular (https://www.nature.com/articles/d41586-026-02357-z) is a multi-paper News feature rather than a single dated primary result and was not pursued once the glucose-responsive-probiotics single-paper candidate was confirmed and opened; worth a look if the editor wants a second science candidate.
```

## Limitation

This round closed researcher/01's two named gaps that could be closed within
budget: Muse Glimmer now has a directly-opened Meta-owned primary (two, in
fact), and the IBM/Together AI item now has two directly-opened independent
secondaries in place of one search-synthesized one. The science/health item
requested is sourced to a directly-opened primary paper (Guan et al., Nature)
but its only independently-opened secondary is Nature's own podcast page —
editorially arm's-length from the paper's authors but not an outside-Nature
newsroom; no non-Nature press coverage of this specific paper was found within
this round's search budget, most likely because the paper is very fresh
(published online within roughly a day of this research). If the editor
requires a fully outside-publisher secondary before running this item, that
search was not exhausted and could be retried. The paper's precise
quantitative results are paywalled and were not obtained; do not print a
number for this item's effect size without first retrieving it from the full
text. The Nvidia financing item is fully verified as accurate but is flagged,
per this round's specific finding, as failing the brief's own freshness test
for a standalone slate item — the researcher records this plainly rather than
resolving it, since the commission reserves item-selection judgment for the
orchestrator.
