# Evidence: tech-news/2026-08-13 (researcher/03, complete record)

This record supersedes researcher/02 for citation purposes; it carries forward
that round's three verified items unchanged and resolves the two findings the
editor routed in editor/01/editorial-review.md. The writer needs only this
file. Two things changed this round, both closing rather than opening gaps.
First, the Zoomsday platform claim: reopening A Security's own writeup and
TechRepublic's secondary this round finds the primary draws a distinction the
draft's "macOS and Android" line collapses — A Security states the underlying
vulnerability is present on every Zoom client (Windows, Mac, iPhone, Android,
Linux) but states the working exploit chain was specifically confirmed on
four of those (Windows, macOS, iOS, Android); TechRepublic independently
confirms the same four-platform "confirmed" set and does not mention Linux as
tested. Neither source supports "macOS and Android" as the affected or
demonstrated set; that undercounts by two platforms at minimum. Second, the
probiotics item's independent-secondary gap: a genuinely outside-Springer-
Nature, outside-ECNU secondary was located and opened this round — 中国科学报
(China Science Daily), published on the ScienceNet portal, dated August 13,
2026 — which interviews the paper's own lead and first authors but is itself
a state science newspaper with no publisher or authorship stake in the Nature
paper's prominence, and which adds substantial reporting beyond the abstract
(the paper's three-year review history at Nature, a five-week non-human-
primate trial duration, gut-clearance kinetics, and a cost projection). This
resolves the editor's blocking finding under option 1 of the brief: the item
stays, with this source added as its qualifying independent secondary rather
than being replaced. No US-based outlet (Ars Technica, ScienceDaily, STAT,
Endpoints) was found covering this specific paper within this round's
search; that gap is recorded under Discarded and does not block the item,
since the series direction permits non-US reporting that carries important
original reporting, which this source does. Items 1-3 (Zoomsday, Muse
Glimmer, IBM/Together AI) are unchanged from researcher/02 except the
Zoomsday platform-scope correction above; nothing else about their sourcing,
numbers, or contradictions changed this round.

### Sources

```text
URL:         https://a.security/blog/asecurity-zoomsday
Kind:        Primary — A Security is the research team that discovered and
             disclosed the vulnerability chain; this is their own writeup.
             Reopened this round specifically to resolve the platform-scope
             question the editor routed.
Establishes: The technical mechanism of the "Zoomsday" exploit chain, the
             AI-assisted discovery/exploitation methodology (models used,
             prompt count, elapsed time), the CVE-by-CVE breakdown, the full
             disclosure timeline (June 8 discovery to August 11 public
             release), and — the new finding this round — a two-tier
             platform claim: the underlying vulnerability is stated to exist
             on every Zoom client, and the working exploit was confirmed on
             four of those five.
Paraphrase:  A Security says the flaw "is present in every version of Zoom
             on every device and operating system: Windows, Mac, iPhone,
             Android and Linux" (five platforms/devices named), and
             separately says the exploit chain itself "was confirmed on all
             platforms Zoom runs on: Windows, macOS, iOS, and Android" (four
             platforms, Linux not included in this narrower "confirmed"
             claim). The post's own detailed demonstration is on macOS
             ("fired live against a real target, it popped Safari open on
             the victim's Mac"); Android is discussed via a heap-spray
             technique framed as proof-of-hijack rather than a shown live
             pop. iOS and Windows are named in the "confirmed" line but the
             fetched text does not include a platform-specific walkthrough
             for either beyond that line.
Locators:    Vulnerability Details / AI-Assisted Research Methodology /
             Exploitation Chain / Disclosure Timeline sections of the post.
Quote:       "The vulnerability is present in every version of Zoom on every
             device and operating system: Windows, Mac, iPhone, Android and
             Linux." / "It was confirmed on all platforms Zoom runs on:
             Windows, macOS, iOS, and Android." / "the barrier that kept
             these weapons scarce has collapsed, and it won't come back" —
             the framing quote carried from researcher/01, still accurate.
```

```text
URL:         https://www.zoom.com/en/trust/security-bulletin/zsb-26015
Kind:        Primary — Zoom's own security bulletin for the lead CVE in the
             chain; the vendor confirming and patching the flaw it owns.
             Unchanged from researcher/01; not reopened this round, no new
             finding needed from it.
Establishes: CVE-2026-53413's existence, CVSS score (8.3, "High"), affected
             products/versions, fixed versions, and that A Security's Idan
             Levcovich is the credited reporter.
Paraphrase:  A missing bounds check in Zoom's annotator function allows a
             buffer over-write that may let a meeting participant achieve
             remote code execution on another participant's device over the
             network. Fixed in Zoom Workplace before 7.1.5/7.0.6, VDI Client
             before 7.0.11/6.6.16, Zoom Rooms before 7.1.0, Meeting SDK
             before 7.1.0.
Locators:    Bulletin ZSB-26015, Revision 1.0, published August 11, 2026.
Quote:       None needed; figures quoted directly above.
```

```text
URL:         https://www.techrepublic.com/article/news-zoom-zero-click-rce-zoomsday-ai-exploit/
Kind:        Secondary — independent tech-news outlet reporting on A
             Security's and Zoom's material, no authorship stake in either.
             Reopened this round for the platform-scope question.
Establishes: Independent confirmation of the CVE set (53413/53414/53415),
             the AI-assisted timeline claim (<24 hours, <20 prompts), that
             Zoom shipped patches, and — the new finding this round —
             independent confirmation of the same four-platform "confirmed"
             set A Security states, with no mention of Linux as tested.
Paraphrase:  "Researchers confirmed the zero-click remote code execution
             (RCE) exploit against Zoom Client v7.0.5 on Windows, macOS,
             iOS, and Android," and separately frames the risk as "exposing
             risks to Windows, macOS, iOS, and Android users." This is
             independent of A Security's own wording but lands on the same
             four-platform set for "confirmed," not the two the draft names.
Locators:    "Discovery & AI Methodology" and "Significance Commentary"
             sections; the platform line appears in the article's opening
             summary and is repeated in the body.
Quote:       "Researchers confirmed the zero-click remote code execution
             (RCE) exploit against Zoom Client v7.0.5 on Windows, macOS,
             iOS, and Android."
```

```text
URL:         https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
Kind:        Primary — Meta's own research blog (credited to Meta
             Superintelligence Labs), announcing Meta's own model release.
             Unchanged from researcher/02; not reopened this round.
Establishes: Muse Glimmer's release by Meta Superintelligence Labs, 30B
             parameters, Apache 2.0 license, that it is trained on Muse
             Spark's outputs via logit distillation, hardware envelope
             (24GB/32GB memory footprint with ~4-bit quantization, tested on
             MacBook M4-Max, M5-Max, and RTX-5090), capabilities (agentic
             task completion, tool use, multi-step reasoning, failure
             recovery, multimodal text+image input, scaffold compatibility
             including OpenClaw, controllable reasoning effort, 100+
             languages), and DFlash speculative-decoding speedups (3.1x on
             RTX-5090, 1.8x on M5-Max, 1.5x on M4-Max).
Paraphrase:  Meta says Glimmer is distilled from its larger, closed Muse
             Spark model to bring near-frontier agentic capability to
             consumer hardware, and reports it outperforming Gemma4-31B and
             Qwen3.6-27B on agentic, coding, multimodal, safety, and
             reasoning benchmarks (Meta's own comparison; no independent
             benchmark re-run found in any source read).
Locators:    Publication date August 10, 2026, per the fetched page.
             Sections covering model architecture, hardware requirements,
             benchmark comparisons, and the DFlash speedup figures.
Quote:       None recorded beyond the paraphrase above.
```

```text
URL:         https://developer.meta.com/ai/models/muse-glimmer/
Kind:        Primary — Meta's own official developer/model-card page.
             Unchanged from researcher/02; not reopened this round.
Establishes: Corroborates model size (30B), license (Apache 2.0), and the
             single-consumer-GPU/Mac deployment claim from Meta's own model
             card. Links out to Meta's Hugging Face (meta-models/Muse-
             Glimmer-30B and variants) and deployment integrations (Ollama,
             vLLM, llama.cpp).
Paraphrase:  Positions Glimmer as "an open model built for always-on local
             agents."
Locators:    Full page as fetched; content and cross-links are consistent
             with the August 10, 2026 research-blog date above.
Quote:       "An open model built for always-on local agents."
```

```text
URL:         https://techcrunch.com/2026/08/10/metas-new-glimmer-ai-model-offers-a-hint-at-zuckerbergs-personal-intelligence-vision/
Kind:        Secondary — independent tech-news reporting; no authorship
             stake in Meta's model release. Unchanged from researcher/01;
             not reopened this round.
Establishes: Model identity, that it runs on a single consumer GPU on Mac or
             PC, offline-capable, multi-step tool use, 100+ languages, text
             and image input, and that it is an open derivative of Meta's
             closed Muse Spark line.
Paraphrase:  Positions the release as revealing where Meta draws the line
             between the open models it wants the public to run themselves
             and the more capable closed models it keeps proprietary.
Locators:    Full article body, dated August 10, 2026.
Quote:       "Glimmer offers an early indication of where Meta may draw the
             line between the AI it wants people to own themselves and the
             more powerful intelligence that remains under the company's
             control."
```

```text
URL:         https://newsroom.ibm.com/2026-08-11-IBM-and-Together-AI-Sign-Multi-Year-Agreement-to-Scale-Open-Source-AI-Inference-with-NVIDIA-AI-Infrastructure-on-IBM-Cloud
Kind:        Primary — IBM's own newsroom release; IBM and Together AI are
             the parties to the agreement. Unchanged from researcher/01; not
             reopened this round.
Establishes: The $240 million multi-year deal, the hardware (Nvidia HGX B300
             systems, Spectrum-X networking), the Q1 2027 availability
             target, and quotes from IBM Cloud's GM, Together AI's CEO, and
             Nvidia's Senior Director of HPC/AI infrastructure.
Paraphrase:  IBM will build a dedicated large-scale Nvidia-based inference
             cluster on IBM Cloud for Together AI, for production-grade
             open-source model serving for enterprises.
Locators:    Dateline August 11, 2026; body paragraphs and quote block.
Quote:       "AI factories are becoming essential enterprise infrastructure
             — like electricity and telecommunications." — Dion Harris,
             Nvidia.
```

```text
URL:         https://www.bnnbloomberg.ca/business/2026/08/11/ibm-together-ai-ink-240-million-deal-for-nvidia-powered-ai-inference-cluster/
Kind:        Secondary — wire reporting (Reuters byline, carried by BNN
             Bloomberg), independent of IBM, Together AI, and Nvidia.
             Unchanged from researcher/02; not reopened this round.
Establishes: Independent confirmation of the $240M figure and the Nvidia
             HGX B300 + Spectrum-X hardware; ~2,000 Nvidia Blackwell B300
             chips in the initial US deployment; a demand claim from
             Together AI's chief revenue officer, Kai Mak, that capacity
             will be "sold out at least two to three months ahead of time."
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
             byline Cristian Dina), no stake in the deal. Unchanged from
             researcher/02; not reopened this round.
Establishes: Independent confirmation of the $240M figure, hardware, and
             Together AI's reported ~400 trillion tokens/month inference
             volume. Frames the deal as IBM competing on inference-cost
             economics rather than raw scale against AWS, Microsoft, and
             Google, and cites Nebius's separate $643M acquisition of an
             inference-optimization team as independent market evidence.
Locators:    Full article body, dated August 11, 2026.
Quote:       None load-bearing beyond the paraphrase above.
```

```text
URL:         https://www.nature.com/articles/s41586-026-10909-6
Kind:        Primary — the research paper itself (Guan, Kong, Gao, Ye et
             al., East China Normal University Shanghai Key Laboratory of
             Regulatory Biology and Institute of Biomedical Sciences; with
             Shangang Zhao, University of Texas Health Science Center at San
             Antonio), published in Nature. Unchanged from researcher/02;
             not reopened this round beyond confirming the abstract still
             reads as before.
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
             external signal to control dosing.
Paraphrase:  The paper frames its contribution as "a programmable, orally
             deliverable sense-and-respond platform for metabolic therapy
             without transplantation" — its own stated advance over prior
             engineered-cell diabetes therapies that needed either external
             triggering or surgical implantation.
Locators:    Published online August 12, 2026 (per the fetched abstract
             page). Figures 2 through 5 cover db/db mice, DIO mice, and
             non-human primate results respectively, per the fetched table
             of contents; Extended Data Figures 1-10 hold the granular
             metabolic measurements. The full-text numeric results (exact
             glucose/HbA1c magnitudes, animal counts per group) sit behind
             Nature's paywall and were not independently retrieved. The
             abstract and bibliographic/author/affiliation data are open and
             were read in full.
Quote:       "a programmable, orally deliverable sense-and-respond platform
             for metabolic therapy without transplantation" — the paper's
             own framing of its advance, from the abstract.
```

```text
URL:         https://www.nature.com/articles/d41586-026-02521-5
Kind:        Secondary — Nature's own news/podcast desk (bylined to Nick
             Petrić Howe and Benjamin Thompson, Nature Podcast hosts).
             Editorially independent of the paper's authors but shares a
             publisher (Springer Nature) with the primary. Unchanged from
             researcher/02; kept in the record as a second, weaker
             secondary, but per the editor's ruling it does not by itself
             satisfy the independent-account bar — see the China Science
             Daily entry below, which does.
Establishes: Independent (of the paper's authors) confirmation that the
             study tested mice and monkeys and that the probiotic lowered
             elevated blood sugar in those animal trials. Frames it as "a
             living diabetes treatment" for a general-audience podcast
             segment.
Paraphrase:  Restates the paper's headline finding; the fetched page (a
             podcast-episode landing page, segment 00:45-08:03) did not
             surface independent expert commentary distinct from the
             paper's own framing.
Locators:    Published August 12, 2026, per the fetched page.
Quote:       "a living diabetes treatment" — a descriptive label, not a
             load-bearing claim.
```

```text
URL:         https://news.sciencenet.cn/htmlnews/2026/8/569743.shtm
Kind:        Secondary — 中国科学报 (China Science Daily), published on the
             ScienceNet (科学网) portal. This is the round's new finding,
             opened specifically to resolve the editor's blocking sourcing
             gap. It is editorially and financially independent of both
             Springer Nature (the paper's publisher) and East China Normal
             University (the authors' institution) — a state science
             newspaper with no ownership or reputational stake in this
             specific paper's prominence, distinct from Nature's own
             podcast desk. It does interview the paper's lead corresponding
             author (Ye Haifeng) and first author (Guan Ningzi), which is
             ordinary science journalism, not a stake; the stake test is
             publisher/authorship interest, not who was interviewed.
Establishes: Independent confirmation that the paper exists, was published
             in Nature, and covers the same claims as the primary (a
             glucose-responsive, orally-delivered engineered probiotic that
             expresses GLP-1 to control blood sugar). Adds substantial
             reporting not present in the open abstract: the paper's
             submission date to Nature (October 2023) and its two-round,
             roughly-three-year review history (a first review of 4+ months
             ending in an editorial handoff, a second review of 7.5 months
             with three new reviewers); a specific non-human-primate trial
             duration (five weeks, in food-crab/cynomolgus macaques, per the
             fetched translation); gut-colonization kinetics (the engineered
             strain concentrates in the cecum/colon and is undetectable in
             feces within five days of dosing, supporting the paper's
             "transient colonization" claim with a concrete clearance
             window); a safety comparison naming semaglutide by name (no
             allergic reactions, thyroid abnormalities, or hypoglycemic
             events reported in the GIFT-treated group); and a cost
             projection (anticipated retail price roughly half that of
             existing comparable drugs, attributed to the researchers, not
             independently verified by the outlet).
Paraphrase:  Presents the paper as the outcome of a ten-year research
             program, quotes Ye Haifeng's stated hope that "it can become a
             gift for diabetes patients" (直译: "希望它能成为送给糖尿病患者的一份礼物"),
             and quotes Guan Ningzi on the projected price point. Frames the
             work as a Chinese-originated therapeutic advance, not a
             restatement of the paper's own abstract language.
Locators:    Published August 13, 2026, 08:30 local time per the fetched
             page timestamp. Names the DOI (10.1038/s41586-026-10909-6)
             directly. Content as machine-translated from the original
             Chinese by the fetch tool; the two direct quotes above were
             checked against the original Chinese text returned by the
             fetch, not translated independently by this record.
Quote:       "希望它能成为送给糖尿病患者的一份礼物" ("hoping it can become a gift for
             diabetes patients") — Ye Haifeng, corresponding author. "预计其售价也
             比现有同类药物低一半" ("the price is expected to be about half that of
             existing comparable drugs") — Guan Ningzi, first author.
```

### Contradictions

- Resolved this round: the draft's "both macOS and Android clients" line for
  the Zoomsday exploit undercounts what both opened sources state. A
  Security's own writeup makes two distinct claims — the underlying flaw
  exists on five named platforms/clients (Windows, Mac, iPhone, Android,
  Linux), and the working exploit chain was specifically "confirmed on all
  platforms Zoom runs on: Windows, macOS, iOS, and Android" (four). Nothing
  in either opened source narrows "confirmed" or "demonstrated" down to just
  macOS and Android; TechRepublic independently corroborates the same
  four-platform confirmed set. This is now a resolved finding, not an open
  contradiction, but it is recorded here because it corrects
  researcher/01/02's unflagged inheritance of the draft's narrower framing —
  see Numbers below for the platform figure itself.
- No contradiction found between the Nature primary and the two probiotics
  secondaries (Nature Podcast, China Science Daily) on any factual claim;
  the China Science Daily piece adds detail the abstract and the podcast
  segment do not carry (review timeline, trial duration, clearance kinetics,
  cost projection) but does not conflict with either.
- Carried forward from researcher/01/02 for completeness, not part of the
  four-item slate: the DeepMind/Jeff Dean reshuffle dating discrepancy
  (resolved as stale, excluded) and the LiteLLM-breach organization-count
  discrepancy (2,500+ per CloudSEK vs. 2,100+ per an unopened Hacker News
  snippet; that item is offered to current-events, not this slate). The
  Nvidia $500B+ financing-platform item, which researcher/02 found to be a
  repeat of coverage fully surfaced by August 12 rather than a fresh
  2026-08-13 development, is not part of this round's four-item slate
  (editor/01 reviewed exactly four items — Zoomsday, Muse Glimmer,
  IBM/Together AI, probiotics — confirming the orchestrator already resolved
  that call between researcher/02 and this round). It is not re-sourced
  here.

### Numbers

```text
Figure: Zoomsday exploit chain — vulnerability present on 5 platforms/clients
        (Windows, Mac, iPhone, Android, Linux); working exploit chain
        confirmed on 4 of those (Windows, macOS, iOS, Android)
Owner:  A Security (https://a.security/blog/asecurity-zoomsday), the
        vulnerability's discoverer, for both figures. TechRepublic
        independently corroborates the 4-platform "confirmed" figure only;
        it does not address the 5-platform "present in every version"
        claim either way.
Scope:  "Present" describes where the underlying flaw exists in Zoom's
        codebase, per A Security's own client/OS inventory. "Confirmed"
        describes platforms where A Security states it validated a working
        RCE exploit chain, as of the August 11, 2026 public disclosure. The
        post's own detailed walkthrough with a shown live compromise is
        macOS-specific; Windows and iOS appear in the "confirmed" list but
        without an equivalent platform-specific walkthrough in the fetched
        text, and Android's demonstration is described as a heap-spray proof
        rather than an equivalent shown live pop. The writer should not
        collapse this to "macOS and Android" — that is neither the affected
        set nor the confirmed set either source states.
```

```text
Figure: Under 24 hours, fewer than 20 prompts; CVSS 8.3 (High),
        CVE-2026-53413
Owner:  A Security (timeline/prompt count); Zoom
        (https://www.zoom.com/en/trust/security-bulletin/zsb-26015), CVSS
        score.
Scope:  Unchanged from researcher/01; not reverified this round, no new
        finding.
```

```text
Figure: 30 billion parameters; single consumer GPU (24GB/32GB memory
        envelope, ~4-bit quantized); Apache 2.0 license; DFlash speedups
        3.1x (RTX-5090), 1.8x (M5-Max), 1.5x (M4-Max)
Owner:  Meta (Meta Superintelligence Labs research blog and Meta's own
        developer.meta.com model page)
Scope:  Unchanged from researcher/02; not reverified this round.
```

```text
Figure: Nvidia HGX B300-based cluster (~2,000 Blackwell B300 chips in the
        initial US deployment); $240 million multi-year deal value; Q1 2027
        target availability
Owner:  IBM (newsroom.ibm.com release) for the deal value and hardware
        family; the ~2,000-chip figure and "sold out two to three months
        ahead" demand claim are owned by BNN Bloomberg/Reuters reporting.
Scope:  Unchanged from researcher/02; not reverified this round.
```

```text
Figure: No precise glycemic-control magnitude recorded (unchanged).
        New this round, from China Science Daily, not from the primary:
        Nature submission October 2023; first review 4+ months, second
        review 7.5 months with three new reviewers; non-human-primate trial
        duration approximately five weeks; engineered strain undetectable
        in feces within 5 days post-dosing; projected retail price roughly
        50% below existing comparable drugs.
Owner:  The magnitude figure (still missing) would be owned by Guan et al.
        (Nature, s41586-026-10909-6) and sits behind the paywall. The five
        new figures above are owned by China Science Daily's reporting,
        attributed there to the researchers (submission/review timeline,
        trial duration, clearance data) or to Guan Ningzi directly (the
        price projection) — none of these five are independently verified
        against Nature's own editorial records or a company/regulatory
        filing, and the price figure in particular is a researcher
        projection, not a filed or announced price. Attribute to China
        Science Daily's reporting if used, not to the paper itself.
Scope:  The submission/review timeline describes this specific paper's path
        through Nature's editorial process, per the researchers' own account
        to the outlet. The five-week NHP trial duration and five-day
        clearance figure describe the animal-study design as reported by the
        outlet, not independently cross-checked against the paywalled
        Methods section. Do not print the magnitude of glycemic effect
        (percentage blood-glucose reduction, HbA1c change) without
        independently retrieving it from the paywalled full text; none of
        this round's sources supply it.
```

### Source assets

```text
Asset: Meta's own Glimmer research post reports head-to-head benchmark
       comparisons against Gemma4-31B and Qwen3.6-27B across five
       categories, and a three-platform DFlash speedup comparison
       (RTX-5090, M5-Max, M4-Max). Unchanged from researcher/02.
Shows: How Meta itself frames Glimmer's competitive position, and the
       concrete speed gain from its speculative-decoding technique.
Crop:  A speedup comparison across the three platforms would carry the
       argument better than restating memory-footprint prose; the
       five-category benchmark table is Meta's own and unverified — flag it
       as Meta-reported if used.
```

```text
Asset: The Guan et al. paper's Figures 2-5 show db/db mouse, DIO mouse, and
       non-human primate results as a progression. Unchanged from
       researcher/02; still not independently confirmed beyond the table of
       contents and captions visible on the open abstract page.
Shows: The mouse-to-primate escalation is the evidentiary structure of the
       paper's claim.
Crop:  Needs the full-text figures themselves (paywalled) before use as a
       visual asset.
```

```text
Asset: China Science Daily's account of the paper's path to publication — a
       ten-year research arc from a 2016 project launch through an October
       2023 Nature submission to an August 2026 publication, with two
       distinct review rounds of differing length and composition.
Shows: How long and contested this specific result's path through peer
       review was, which is a concrete counterweight to any "just-announced,
       untested" reading of a paper published within roughly a day of this
       research — the finding is fresh to print, not fresh to scrutiny.
Crop:  Only the review-timeline facts as reported (dates, durations, reviewer
       turnover) carry evidentiary weight; the outlet's narrative framing
       ("十年'驯'菌", "a gift for diabetes patients") is color, not evidence,
       and should not be presented as the paper's own language.
```

### Discarded

```text
URL: https://www.venturebeat.com/... (Muse Glimmer, HTTP 429 on repeat) — carried forward from researcher/01/02, still not opened, not needed since Meta's own primary and TechCrunch's secondary are both open.
URL: https://csnsf.org/the-probiotic-bacteria-engineered-to-treat-diabetes/ — surfaced this round in search with a title identical to Nature's own podcast-page headline; not opened, appears to be a content aggregator republishing Nature's own piece rather than independent reporting, so not pursued as a candidate independent secondary.
URL: site:statnews.com / site:sciencedaily.com / site:arstechnica.com / site:endpts.com searches for the Guan et al. probiotics paper — no results returned this round for any of the four named US outlets; the paper appears not to have been picked up by US science press within its first ~24-30 hours, consistent with researcher/02's freshness note. Not a rejection of the item; recorded so the writer/editor knows a US-outlet secondary was sought and not found, and that China Science Daily is being used instead per the series direction's allowance for non-US reporting with original reporting.
URL: https://www.stdaily.com/web/2026-08/13/content_563076.html (科技日报, Science and Technology Daily) and https://finance.sina.com.cn/tech/digi/2026-08-13/doc-ininctav3546774.shtml (Sina Tech) and https://www.163.com articles — surfaced in the same Chinese-language search as the China Science Daily piece, evidently covering the same paper; not opened this round once China Science Daily was confirmed sufficient to resolve the editor's finding. Worth opening if the writer wants a second independent secondary or additional figures, but not needed to clear the four-item floor.
URL: Nature News search results for other August 13, 2026 issue items (spin-qubit device advances across four teams, https://www.nature.com/articles/d41586-026-02357-z; anelloviruses and long COVID; rainforest insect cataloguing megaproject; lithium-extraction methods) — not pursued this round; the brief's own instruction was to prefer resolving the probiotics item's sourcing over pursuing the spin-qubit item, since spin-qubit carries the same single-publisher risk. Not needed once the China Science Daily secondary was confirmed.
```

## Limitation

This round closed both findings the editor routed. The Zoomsday platform
scope is now stated precisely from both opened sources: the underlying flaw
is claimed present on five platforms/clients, the working exploit chain
confirmed on four (Windows, macOS, iOS, Android) — not the two ("macOS and
Android") the draft currently states — with macOS carrying the primary's own
detailed live-compromise walkthrough. The probiotics item's independent-
secondary gap is closed with China Science Daily/ScienceNet, a state science
newspaper independent of Springer Nature and East China Normal University in
authorship and stake, opened and read in full this round, which also
supplies several reporting details (review timeline, trial duration,
clearance kinetics, price projection) not present in either the paper's open
abstract or Nature's own podcast page — these are attributed to the outlet's
reporting, not to the paper itself, and are not independently verified
against a primary record. No US-based outlet coverage of this specific paper
was found within this round's search; if the editor or writer wants one
before print, that search was not exhausted, only unsuccessful within this
round's budget, and the three additional Chinese-language outlets found but
not opened (科技日报, Sina Tech, 163.com) are recorded as unopened leads.
Nothing about items 1-3's sourcing, figures, or contradictions changed this
round beyond the Zoomsday platform correction; the Nvidia financing item
remains outside the four-item slate per researcher/02's finding, carried
forward for completeness only.
