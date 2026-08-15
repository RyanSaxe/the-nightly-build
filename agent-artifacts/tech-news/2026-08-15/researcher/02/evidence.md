# Evidence record: tech-news/2026-08-15 (researcher/02)

This is a complete replacement record, not a diff. It carries forward the four
items the editor cleared unchanged (IBM/OpenAI, Apple/Alibaba, GPT-5.6-Cyber,
Meta Muse Glimmer) from researcher/01, and rewrites the three items the editor
routed back: the DeepSeek quotation, the Gemini GDPVal-AA figures, and the
science item. All three are now resolved with primary-page evidence read this
session. Short version: (1) the DeepSeek quote is corrected to the source's
actual sentence, with a tighter locator; (2) the Gemini GDPVal-AA figures
survive — they are real and exactly as printed, but they live on a different
Artificial Analysis page than the one cited, and the record now supplies that
page; (3) the science item is replaced. A stronger, fresher, more consequential
candidate exists — a Nature Climate Change paper on Atlantic circulation
collapse, published August 13 and read directly from its own page this session
— and it is recommended over patching the fuel-cell item. The fuel-cell item's
Nature primary was also read directly this time (abstract and metadata, past
the point researcher/01 reached), and is recorded below, corrected, as a
fallback in case the writer and editor prefer to keep it instead.

## Sources

### 1. IBM/OpenAI enterprise partnership

Unchanged from researcher/01; the editor found this item clean. Carried forward
verbatim.

```text
URL:         https://newsroom.ibm.com/2026-08-13-ibm-partners-with-openai-to-accelerate-secure-ai-deployment-for-enterprises-across-core-operations
Kind:        Primary. IBM's own newsroom, dateline Armonk, N.Y., August 13, 2026. IBM is a party to the deal it describes.
Establishes: The partnership's terms as IBM states them: OpenAI models (GPT-5.6) and products (Codex, ChatGPT Work) embedded in IBM Consulting Advantage; a dedicated "OpenAI Practice" staffed by "thousands of consultants and engineers" holding OpenAI Partner Network certifications; IBM joins OpenAI's "Elite" partner tier; three focus areas (legacy-workflow modernization, software development, cybersecurity via the OpenAI Daybreak Cyber Partner Program plus IBM Autonomous Security); named industries (financial services, government, telecom, retail).
Paraphrase: No dollar figures, consultant headcount, or contract length are disclosed anywhere in the release.
Locators:  Full release text (single page, ~600 words); quotes are the final two paragraphs.
Quote:     Andy Baldwin, Global Senior Vice President, IBM Consulting: "The challenge is not access to AI technologies — it's integrating AI securely and at scale into complex enterprise environments and workflows." Denise Dresser, Chief Revenue Officer at OpenAI: "IBM Consulting and OpenAI are helping organizations make that shift, combining deep transformation expertise to deploy AI that is secure, operational, and aligned with real business priorities."
```

```text
URL:         https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/
Kind:        Secondary/independent. TechCrunch has no stake in the deal; reports on it from outside.
Establishes: Same-day independent framing: places the deal inside "competition for corporate AI spending," notes IBM's July 2026 revenue-forecast cut and "weaker-than-expected quarterly results" (context IBM's own release omits), and notes OpenAI has struck comparable enterprise partnerships with Infosys and Tata Consultancy Services.
Paraphrase: Adds business-performance context and competitive framing; does not add new deal terms, since none were disclosed to any outlet.
Locators:  Full article, ~450 words.
Quote:     None recorded; no material quote beyond paraphrase needed.
```

### 2. Apple's China-specific LLM built with Alibaba

Unchanged from researcher/01. Not touched by the editor's review; the
single-origin-sourcing caveat in Contradictions still applies.

```text
URL:         https://finance.yahoo.com/technology/ai/articles/apple-trains-china-specific-ai-140316517.html
Kind:        Secondary, syndicated wire copy. Byline is Reuters; Yahoo Finance is a distribution partner, not the originating newsroom. Reuters itself is outside Apple and Alibaba, but its account rests entirely on three unnamed sources, so treat this as reporting-grade, not company-confirmed fact.
Establishes: Apple built a large language model for the China market with Alibaba Group's help; described as a shift from Apple's earlier reliance on outside partners' models; would make Apple "the first foreign company Beijing has cleared to deploy its own proprietary AI model in China"; Apple Intelligence rollout in China expected "in the coming months" after an iOS update; neither Apple nor Alibaba commented to Reuters.
Paraphrase: No parameter count, benchmark, training-compute figure, or named regulatory approval document is given anywhere in this reporting chain.
Locators:  Full article, ~350 words, dateline August 14, 2026.
Quote:     None material beyond paraphrase; no named Apple or Alibaba spokesperson is quoted.
```

```text
URL:         https://www.macrumors.com/2026/08/14/apple-trained-own-ai-model-for-china/
Kind:        Secondary, but not independent of the above: MacRumors' entire account is attributed to the same Reuters report. Read to check whether it added any reporting of its own; it did not.
Establishes: Nothing not already in the Reuters/Yahoo account. Adds one piece of prior-history context: Apple briefly published, then within a day removed, a support guide describing how to connect Alibaba's Qwen to Siri on Mac.
Paraphrase: Confirms this is a single-origin story republished, not independently corroborated by a second newsroom's own sourcing.
Locators:  Full article, ~400 words.
Quote:     None recorded.
```

```text
URL:         https://www.bloomberg.com/news/articles/2026-07-15/apple-gets-approval-for-alibaba-powered-iphone-ai-tools-in-china
Kind:        Primary-adjacent independent reporting, different claim, one month earlier. Included for the Contradictions section below, not as confirmation of the August 14 claim.
Establishes: On July 15, 2026, Bloomberg reported China's regulators approved Apple Intelligence for iPhones in China, with Alibaba and Baidu named as partners — describing Apple integrating Alibaba's existing Qwen model, not Apple training its own proprietary model.
Paraphrase: This is a materially different claim from the August 14 story (integrating a third party's model vs. training an in-house one with that party's help). See Contradictions.
Locators:  Headline and lede only; full body gated (403 on fetch).
Quote:     None recorded; headline paraphrased above.
```

### 3. DeepSeek V4 Pro reaches general availability — quotation corrected

The first two sources are unchanged from researcher/01. The Digital Applied
entry is rewritten: the Quote field carried a sentence that is not on the page.
I fetched the page fresh this session (a third independent fetch, after the
researcher's original and the editor's two) and pulled the verbatim text
myself.

```text
URL:         https://api-docs.deepseek.com/news/news260813/
Kind:        Primary. DeepSeek's own API documentation/changelog page announcing the GA release.
Establishes: DeepSeek-V4-Pro-0813 moved from preview to general availability on the app, web, and API. States a pricing change takes effect "at 16:00 UTC, Aug 16, 2026," with off-peak rates 50% below peak. Documents "flexible reasoning effort" (low/high/max) and native OpenAI Responses API support "optimized for Codex." References a benchmark comparison table as an embedded image (img/v4_260813_benchmark_table_en.png) whose cell values I could not extract as text.
Paraphrase: The page does not itself state total/active parameter counts or context window in readable text; those figures below are drawn from the secondary sources that read the model card.
Locators:  Full changelog entry, dated August 13, 2026.
Quote:     None extracted; benchmark figures live in an image, not body text.
```

```text
URL:         https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/
Kind:        Secondary/independent.
Establishes: Model specs read off the model card: 1.6 trillion total parameters, 49 billion active per token (Mixture-of-Experts), 1,000,000-token context window, up to 384,000-token output. Reports MIT-licensed open weights.
Paraphrase: Confirms this is the same "0813" build named in DeepSeek's own changelog.
Locators:  Full article.
Quote:     None recorded.
```

```text
URL:         https://www.digitalapplied.com/blog/deepseek-v4-pro-ga-official-release-2026
Kind:        Secondary/independent, and the strongest independent account of the six candidates. Explicitly labels every benchmark figure as vendor-stated and adds original findings DeepSeek did not publish.
Establishes: Using Internet Archive snapshots, the piece bounds the GA release to a roughly 32-hour window (Aug 12-13) and documents that the version string appeared first in DeepSeek's price list, with no separate announcement — a distinct fact from what DeepSeek's own changelog states (Wayback-bounded: absent Aug 12, 03:00 UTC; present Aug 13, 11:10 UTC). Notes the release lacks a published Jinja chat template and that the GA build carries no disclosed parameter count of its own (distinct from the general V4-Pro architecture figures). Reports that accounts using the alias "deepseek-v4-pro" were upgraded in place without a version pin, a compliance-relevant operational detail.
Paraphrase: This is read-and-verified independent skepticism, not a repetition of DeepSeek's claims.
Locators:  Section 03 ("Benchmarks"), subsection "Label every number." Full article; byline dated August 15, 2026.
Quote:     CORRECTED. The verbatim sentence, fetched directly this session: "At the time of writing, no independent reproduction of any GA-specific figure exists — normal for a release this fresh, and still the single most important caveat on the table." (The record's prior Quote field — "None of these columns has yet been replicated by an independent evaluator for the 0813 build." — does not appear anywhere on the page. It has been removed.) A second sentence in the same section, also usable, reads: "every cell in both tables is DeepSeek-stated," describing the rival-model columns as DeepSeek's own reproductions on its own harness, not the rivals' published figures.
```

Benchmark figures as reported by DeepSeek (self-reported; see Numbers section for full detail and the independent-verification caveat above): SWE-bench Verified 80.6%, Terminal-Bench 2.0 67.9%, GPQA Diamond 90.1%, MMLU-Pro 87.5%, LiveCodeBench 93.5%, Codeforces rating 3,206.

### 4. Google ships Gemini 3.7 Flash — GDPVal-AA figures re-sourced

The blog and 9to5google entries are unchanged. The Artificial Analysis entry is
split in two: the Intelligence Index page the article already cites (which
does not carry the GDPVal-AA figures — the editor was right), and the actual
owner of those figures, a separate, dedicated Artificial Analysis leaderboard
page. The figures survive intact; only the citation was wrong.

```text
URL:         https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
Kind:        Primary. Google's own product blog.
Establishes: Released August 13, 2026, three weeks after Gemini 3.6 Flash. Introductory pricing $0.75/1M input tokens and $3.75/1M output tokens through December 31, 2026 (rising to $1.50/$7.50 on January 1, 2027) — Google's own stated half-price-of-launch framing. Availability: Gemini app (Spark tier, AI Pro/Ultra subscription), Google Antigravity, AI Studio, Android Studio, Gemini Enterprise Agent Platform, Gemini Enterprise app.
Paraphrase: Benchmark gains are Google's own evaluations, run on Google's own harness, against Google's own prior model (3.6 Flash) as baseline. See Numbers.
Locators:  Full post.
Quote:     None material beyond the figures recorded in Numbers.
```

```text
URL:         https://9to5google.com/2026/08/13/gemini-3-7-flash-launch/
Kind:        Secondary/independent, but adds framing rather than new testing.
Establishes: Confirms the "three weeks after the last release" cadence claim, and the availability list, independently of Google's post. Does not run its own benchmarks.
Paraphrase: Functions as same-day confirmation of Google's own claims, not independent verification of the numbers.
Locators:  Full article, published 10:00 am PT, August 13, 2026.
Quote:     None recorded.
```

```text
URL:         https://artificialanalysis.ai/models/gemini-3-7-flash
Kind:        Independent third-party benchmark organization. This is the page the article currently cites for the GDPVal-AA figures, and it does not carry them — confirmed by a fresh fetch this session, which found only the Intelligence Index figures below. Still the correct citation for those Intelligence Index figures specifically.
Establishes: Gemini 3.7 Flash (high) scores 56 on Artificial Analysis's own Intelligence Index v4.1.1 (a 9-evaluation composite spanning GDPval-AA v2, Tau3-Banking, Terminal-Bench v2.1, SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, and AA-LCR), ranked 17th of 188 models tested, price-tier median 34. Also on this page: Output Speed 340.1 tokens/sec (#1/188), Cost per Intelligence Index task $0.40, 1.0M-token context window.
Paraphrase: The Intelligence Index score (56) is a composite that includes a GDPval-AA v2 sub-score, but this page does not display that sub-score as a standalone Elo figure, and does not name rival models' GDPVal-AA scores. Confirmed absent on a direct re-fetch: no 1,525, no +103, no Muse Spark/Claude Sonnet 5/GPT-5.6 Terra comparison anywhere on this page.
Locators:  Model page, "Intelligence Index" and headline metrics sections.
Quote:     None recorded.
```

```text
URL:         https://artificialanalysis.ai/evaluations/gdpval-aa
Kind:        Independent third-party benchmark organization, and primary-grade for its own measurement (Artificial Analysis designs, runs, and authors this leaderboard; it is not reporting on someone else's number). This is the page that actually owns the four figures the article prints. New source, supplied to close the editor's routed finding.
Establishes: The GDPval-AA v2 leaderboard, described on the page as testing models on "real-world tasks across 44 occupations and 9 major industries" using 220 tasks developed by OpenAI, with models given shell and web-browsing access in an agentic loop and performance rated by blind pairwise comparison converted to an Elo score anchored to a human baseline of 1,000. Confirmed by direct fetch, exact rows: Gemini 3.7 Flash (high), rank 24, Elo 1,525. Gemini 3.6 Flash (high), rank 36, Elo 1,422 — the difference is exactly 103 points, confirming the article's "+103" figure, though the page does not print the delta as its own stated number; it is arithmetic on two rows I read directly. Muse Spark 1.2 (xhigh), rank 11, Elo 1,628. Claude Sonnet 5 (Adaptive Reasoning, Max Effort), rank 14, Elo 1,598. GPT-5.6 Terra (max), rank 18, Elo 1,578. All five numbers match the article's printed figures exactly.
Paraphrase: This resolves the editor's finding. The figures were never fabricated; they were cited to the wrong Artificial Analysis page. This page is the right one.
Locators:  Full leaderboard table, filtered to the named model rows above. No byline or last-updated date visible on the page.
Quote:     None recorded; figures are tabular, reported verbatim above.
```

Google's own reported benchmark deltas (self-reported, Google's harness, vs. Gemini 3.6 Flash): FrontierCode 1.1 Main 43.6% vs. 34.4%; DeepSWE v1.1 65.3% vs. 49.0%; WebDev Arena Elo 1,588 vs. 1,538; AutomationBench 30.4% vs. 17.0%. (One further figure, transcribed from the fetch as "GDP.pdf" at 34.0% vs. 22.0%, could not be confirmed against a benchmark with that exact name in independent searches — likely a mis-transcription of a benchmark abbreviation; flagged, not used as a clean citation. Do not cite this figure without re-reading the blog post's own image/table directly.)

### 5. OpenAI's GPT-5.6-Cyber reaches "High" cyber capability

Unchanged from researcher/01; the editor found this item clean. Carried
forward verbatim.

```text
URL:         https://deploymentsafety.openai.com/gpt-5-6
Kind:        Primary. OpenAI's own Deployment Safety Hub / system card for the GPT-5.6 model family, which GPT-5.6-Cyber belongs to.
Establishes: OpenAI classifies GPT-5.6 Sol, Terra, and Luna (the base models GPT-5.6-Cyber derives from) as "High," not "Critical," on cybersecurity capability under OpenAI's own Preparedness Framework. States directly: "GPT-5.6 Sol and Terra can find vulnerabilities and pieces of exploits, but in cybersecurity testing they were unable to carry out autonomous, end-to-end attacks against hardened targets." Documents evaluation methods: Cyber Capability Evaluations at three defined thresholds (Informational/High/Critical) plus CVE-Bench, and states external evaluations were run by two named outside organizations — Irregular and the UK AI Safety Institute (UK AISI). States GPT-5.6 Sol's "cyber safeguards block roughly ten times more potentially harmful activity" than the prior generation.
Paraphrase: The High/Critical classification is OpenAI's own governance determination (made under its Preparedness Framework process), informed by — but not made by — the two named external evaluators. This is stronger sourcing than a pure self-report, but it is not an independent regulator's finding.
Locators:  Cybersecurity capability section of the hub page; "External Evaluations for Cyber Capabilities" subsection.
Quote:     "GPT-5.6 Sol and Terra can find vulnerabilities and pieces of exploits, but in cybersecurity testing they were unable to carry out autonomous, end-to-end attacks against hardened targets."
```

```text
URL:         https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/
Kind:        Primary. OpenAI's own announcement blog post for GPT-5.6-Cyber and the expanded Daybreak access program. Gated: returned HTTP 403 to the fetch tool. Recorded as the source's own canonical page per the researcher standard (a 403 is gated, not dead); its content below is reconstructed from search-result excerpts and cross-checked against the deploymentsafety.openai.com page and the independent accounts below, not read directly in full.
Establishes (per excerpts and cross-checked secondary reporting): GPT-5.6-Cyber launched August 10, 2026, built on GPT-5.6 Sol, available through "Daybreak Red," the higher-access tier of an expanded Daybreak program for vetted defenders.
Paraphrase: Treat any figure attributed only to this URL as needing a direct re-read before publication, since I did not read the full page myself.
Locators:  Not directly accessible this session.
Quote:     None taken directly; do not quote this page without re-fetching.
```

```text
URL:         https://www.helpnetsecurity.com/2026/08/11/openai-gpt-5-6-cyber-model/
Kind:        Secondary/independent, but relays OpenAI's claims without outside verification of its own. Read in full to check for independent expert commentary; found none.
Establishes: GPT-5.6-Cyber completed 95% of requests involving exploit chains, authentication bypass, and privilege escalation, versus 1.5% for standard GPT-5.6 (OpenAI's own comparison, on OpenAI's own ExploitGym benchmark). Reports OpenAI's claim that its researchers used the model to find two previously undocumented flaws in Chrome's V8 engine, one later assigned CVE-2026-15903.
Paraphrase: No security researcher, academic, or third party is quoted or cited in this piece; it is a same-day rewrite of OpenAI's announcement.
Locators:  Full article, published August 11, 2026.
Quote:     None recorded.
```

```text
URL:         https://www.tenable.com/cve/CVE-2026-15903
Kind:        Independent — a third-party vulnerability database with no relationship to OpenAI, cataloging Chrome's own disclosure. This is the one piece of GPT-5.6-Cyber's story that is independently, externally confirmable rather than resting on OpenAI's word.
Establishes: CVE-2026-15903 is real and public: an out-of-bounds read/write in V8 in Google Chrome before version 150.0.7871.128, CVSS v3 score 8.8 (High), allowing a remote attacker to execute code inside the sandbox via a crafted HTML page. Published July 20, 2026; updated July 24, 2026.
Paraphrase: This CVE record does not itself credit OpenAI or GPT-5.6-Cyber as the discoverer — that attribution comes only from OpenAI's own reporting and secondary coverage repeating it (see Contradictions). Independent search also found reporting that Chrome's own release notes for 150.0.7871.128 credit the finding to OpenAI's security research, reported July 6 and fixed in the July 16 stable release — meaning the underlying discovery predates GPT-5.6-Cyber's August 10 public launch; OpenAI's announcement is citing a track record built before release, not a post-launch discovery.
Locators:  Full CVE record.
Quote:     "Out of bounds read and write in V8 in Google Chrome prior to 150.0.7871.128 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page."
```

### 6. Meta releases Muse Glimmer 30B under Apache 2.0

Unchanged from researcher/01; the editor found this item clean. Carried
forward verbatim.

```text
URL:         https://huggingface.co/meta-models/Muse-Glimmer-30B
Kind:        Primary. The official weights and model card, hosted by Meta's own organization account on Hugging Face — the artifact itself, not a description of it.
Establishes: Dense causal transformer with a dedicated perception (vision) encoder, ~29.6B parameters including the ~1.8B-parameter ViT-G/14 vision encoder, 52 layers, 131,072+ token context window, Apache 2.0 license, knowledge cutoff January 4, 2026, 202,048-token vocabulary. States a benchmark table: MCP Atlas 75.5, SWE-Bench Pro 51.2, SWE-Bench Verified 76.0, AIME 2026 94.7, GPQA Diamond 83.5, MMMU Pro 74, Charxiv Reasoning 78.8, presented against Gemma4-31B and Qwen3.6-27B.
Paraphrase: All benchmark figures on this page are Meta's own; the card does not identify any external evaluator.
Locators:  Model card, "Benchmarks" table.
Quote:     None recorded; figures are tabular.
```

```text
URL:         https://www.infoq.com/news/2026/08/meta-muse-glimmer/
Kind:        Secondary/independent. Read in full specifically to check for independent testing; confirmed there was none.
Establishes: Confirms release date August 10, 2026 (article published August 14). Names the benchmarks Meta cited (SWE-Bench, DeepSearch QA, τ-Bench, MCP-Atlas) but reproduces no independent numbers of its own. The one concrete figure repeated is Meta's own DFlash speculative-decoding claim: "up to a 3.1x increase in generation throughput" on specified hardware.
Paraphrase: Confirmed directly: "no evidence that [the author] conducted independent benchmarking, consulted external AI researchers, or validated Meta's performance claims through third-party evaluation." This is a press-release rewrite, not an independent check — recorded honestly rather than counted as verification.
Locators:  Full article.
Quote:     None recorded beyond the DFlash figure above.
```

### 7. Science item — REPLACED. AMOC tipping-rate paper (recommended), fuel-cell catalyst (corrected fallback)

The commission's science slot is thin in the fuel-cell item for two compounding
reasons: it is nine days old on the 15th, and the article's own framing
contradicts the primary. I searched specifically for a fresher, more
consequential, resolvably-primary candidate dated August 13-15, and found one:
a Nature Climate Change paper on what actually controls Atlantic Meridional
Overturning Circulation (AMOC) collapse, published August 13, 2026 — same day
as three of the article's other four items. I recommend this as the
replacement. I also went back and read the fuel-cell paper's own page directly
this session (its metadata and abstract, past the login gate that stopped
researcher/01), so the original item is recorded below too, corrected, in case
the writer or editor prefers to keep it instead of swapping the fourth item.

#### 7a. Recommended replacement: AMOC stability depends on the rate of warming, not just its peak

```text
URL:         https://www.nature.com/articles/s41558-026-02730-w
Kind:        Primary. Nature Climate Change, the paper itself. Read directly this session via its own page metadata (title, full author list, and complete abstract are served without a login wall; the typeset full text sits behind the same subscription gate as the fuel-cell paper below — same limitation, disclosed the same way).
Establishes: Published online August 13, 2026. Authors, in order: René M. van Westen (Institute for Marine and Atmospheric Research Utrecht, Utrecht University), Reyk Börner, Henk A. Dijkstra. Title: "Failure to track a stable AMOC state under rapid climate change." The paper's own abstract, quoted in full: "The Atlantic Meridional Overturning Circulation (AMOC), a tipping element of the climate system, currently has an estimated global warming threshold for collapse of +4.0 °C (uncertainty range 1.4-8 °C). However, such a threshold may not be meaningful because AMOC stability depends on the rate of radiative forcing change, not a set temperature. Here we identify an AMOC stabilizing mechanism that operates on timescales slower than present-day warming rates. Slow forcing permits coherent adjustment of surface and interior ocean properties, supported by enhanced evaporation and reduced sea-ice extent, counteracting destabilizing feedbacks. Using a slow CO2 ramp (+0.5 ppm yr-1) climate model simulation, we explicitly demonstrate the AMOC remains stable up to +5.5 °C of global warming. By contrast, under faster CO2 ramps, the AMOC collapses at substantially lower warming levels (+2 °C). Our findings demonstrate rate-induced AMOC tipping and imply that limiting the rate of emissions is critical for reducing the risk of an AMOC collapse."
Paraphrase: The finding overturns a specific, widely cited number (the "+4.0°C collapse threshold") by showing the threshold concept itself doesn't hold — the same climate-model system can stay stable well past +5°C under slow forcing or collapse at +2°C under fast forcing, depending only on the rate of change. That is a change in scientific understanding of a live tipping-point question, not an incremental modeling update.
Locators:  Page metadata (title, author list, abstract) fetched directly from nature.com. Full body text (methods, figures, discussion) is paywalled; not read.
Quote:     Full abstract quoted verbatim above; nothing else quoted, since the full text was not accessible.
```

```text
URL:         https://phys.org/news/2026-08-rapid-atlantic-circulation-2c-slower.html
Kind:        Secondary, but not independent reporting — checked directly and it is a republished Utrecht University press release. Byline: "by Rosa van den Dool, Utrecht University," with an editor's note ("edited by Swati Mestri, reviewed by Robert Egan") and the line "Provided by Utrecht University" at the foot of the piece. All quotes in it are from the paper's own authors (van Westen, Börner, Dijkstra); no outside scientist is quoted. Recording this honestly rather than counting it as independent verification.
Establishes: Restates the paper's abstract in plain language and adds one author quote not in the abstract: van Westen: "Our results show there is not necessarily a fixed temperature beyond which the AMOC inevitably collapses. The stability of the circulation depends on how fast the climate is changing." Also states the critical warming rate found in the paper is around 0.3°C per decade — a pace the world's current emissions trajectory is already approaching.
Paraphrase: Adds no reporting or verification beyond the primary; useful for the plain-language framing and the one added figure (0.3°C/decade), not as a second, independent confirming source.
Locators:  Full article.
Quote:     Quoted above.
```

```text
URL:         (search attempt only — no page fetched) Science Media Centre expert-reaction search
Kind:        n/a — checked and rejected. A Science Media Centre page titled "expert reaction to a modelling study suggesting that AMOC may be resilient to future warming" looked promising but, on fetch, turned out to cover a different, earlier paper (Baker et al., "Continued Atlantic overturning circulation even under climate extremes," Nature, 2025, DOI 10.1038/s41586-024-08544-0), not this one. Not usable; see Discarded.
Establishes: Nothing about this item.
Paraphrase: n/a
Locators:  n/a
Quote:     n/a
```

**Honest limitation on this replacement candidate:** I could not find a genuinely independent journalistic account of this specific paper in this session's search budget — every outlet I found (phys.org, ScienceDaily, ecomagazine.com, Environmental News Network) traces to the same Utrecht University press release, with no outside expert quoted specifically on this paper. This is the same shape of weakness researcher/01 flagged for the Apple/Alibaba item (single-origin, republished, not independently sourced) and, on inspection this session, is also true of the fuel-cell item's own ScienceDaily and phys.org citations below — both are the same Washington University press release, byline "Beth Miller, Washington University in St. Louis," republished on both outlets. Neither science candidate this round clears a strict independent-account bar as cleanly as the AI items do. Between the two, the AMOC paper is still the stronger choice: it is dated to the round's actual cluster (Aug 13, not Aug 6), and its claim is checkable directly against the primary's own abstract rather than resting on a secondary's paraphrase of a claim the primary itself doesn't make (see the fuel-cell item's central problem, below).

#### 7b. Corrected fallback: platinum-sparing fuel-cell catalyst (if the writer keeps this item instead)

```text
URL:         https://www.nature.com/articles/s41565-026-02244-8
Kind:        Primary. Nature Nanotechnology. Read directly this session via page metadata — title, full author list, and complete abstract are accessible without a login wall (researcher/01 only saw the login redirect and did not retrieve these). Full typeset text remains paywalled ("Buy or subscribe" / "Access options" confirmed present on the page); not read.
Establishes: Published online August 6, 2026 — CORRECTED from "Wu et al." First author: Gao, Lei. Senior/corresponding author: Wu, Gang (Washington University in St. Louis). Full author list, in order: Gao, Hwang, Li (Xiaorui), Zheng, Lee, Liu, Wierzbicki, Li (Jialu), Guo, Zhang, Lin, Zhao, Wang, Dun, Wu. Actual title, quoted from the page's own citation metadata: "Radial nanochannel-array carbon enables high-performance intermetallic fuel cell catalysts." The paper's own abstract, quoted in full: "The challenge of designing platinum-based intermetallic catalysts for oxygen-reduction cathodes in fuel cells is to synergistically integrate four critical merits into one catalyst, including fine metal nanoparticles, high ordering degree of intermetallic structure, high Pt content against support and mesopore-rich carbon supports for favourable ionomer dispersion and mass/charge transfers. Here we introduce a radial nanochannel-array carbon sphere (RNCS) support that contains open-through-grooved mesopores with sufficient volume and optimal size. PtCo intermetallic nanoparticles are uniformly assembled into the RNCS to achieve exceptional thermal and electrochemical stability. Annealing at desirable elevated temperatures (>1,000 °C) simultaneously yields highly ordered L10-PtCo intermetallic phases (>80%) and fine particle dispersion (<5 nm), even at a high Pt content of 40 wt%. The RNCS support enables all these merits in a single catalyst due to its ordered mesoporous structures with effective nanoconfinement, and the supported PtCo intermetallic catalyst in membrane electrode assemblies delivered a compelling current density of 2.12 A cm-2 at 0.70 V under heavy-duty vehicle conditions and retained 82.5% performance after a rigorous accelerated stress test of 150,000-voltage cycles."
Paraphrase: CORRECTED CLAIM — the primary does not claim reduced platinum loading. It explicitly keeps loading high (40 wt%, described in the abstract itself as "high Pt content") and states the advance as achieving small, ordered particles and durability *despite* that high loading, not by lowering it. The reduction the abstract and the researcher institution's own quote describe is in precious-metal *use* — via better durability, meaning less catalyst needs replacing over the system's life — not in the *loading percentage* of the catalyst itself. "Reduces platinum loading" is not a defensible paraphrase of this abstract; "keeps high platinum loading durable, cutting long-run platinum consumption through longevity" is.
Locators:  Page metadata (title, author list, abstract) fetched directly from nature.com. Full body text (methods, figures beyond what the abstract states, discussion) is paywalled; not read.
Quote:     Full abstract quoted verbatim above.
```

```text
URL:         https://source.washu.edu/2026/08/platinum-powers-the-future/
Kind:        Secondary, and not independent: this is Washington University's own communications office announcing its own faculty member's (Gang Wu's) paper. Treat as primary-adjacent institutional messaging, not outside verification.
Establishes: Published August 6, 2026. Direct quote from Gang Wu, Elvera and William R. Stuckenberg Professor, McKelvey School of Engineering, Washington University in St. Louis: "Our strategy is using this new carbon nanostructure to synthesize platinum cobalt intermetallic nanoparticles that can reduce precious metal content and enhance activity and stability." Also states the same figures as the primary abstract: sub-5nm particles, >1,000°C annealing, 150,000-cycle test.
Paraphrase: Wu's own quote uses "reduce precious metal content," which is closer to the primary's actual claim (reduced consumption via durability) than the article's "reduces platinum loading" — but it is still the loading percentage that stays high (40 wt%), and this quote should not be read as endorsing a loading-percentage reduction.
Locators:  Full article.
Quote:     Quoted above.
```

```text
URL:         https://phys.org/news/2026-08-carbon-nanostructure-fuel-cell-catalyst.html
Kind:        Secondary, but on closer inspection this session, not independent reporting either: byline "by Beth Miller, Washington University in St. Louis," editor's note ("edited by Swati Mestri, reviewed by Robert Egan"), no outside quote. This is the same Washington University release as the source.washu.edu entry above, republished on phys.org, not a second confirming account. CORRECTED from researcher/01, which described this as "not affiliated with the research team" — the byline shows it is the research team's own institution's writer.
Establishes: Reports the catalyst "retained 85% of its performance after 150,000 harsh voltage cycles, likely equivalent to 25,000 hours of operation," and that nanoparticles stayed under 5 nanometers even after heating to 1,000°C.
Paraphrase: CONTRADICTION FLAGGED. The 85% figure here does not match the primary's own abstract, which states 82.5% after the same 150,000-cycle test. Use the primary's figure (82.5%) if this item runs; the 85% figure traces only to this non-independent secondary and should not be printed as the paper's own number.
Locators:  Full article.
Quote:     None recorded.
```

```text
URL:         https://www.sciencedaily.com/releases/2026/08/260807035140.htm
Kind:        Secondary, not independent: same Washington University release ("Materials provided by Washington University in St. Louis. Original written by Beth Miller") republished a second time on a second aggregator. New source added this round, purely to confirm it is not a distinct confirming account. Do not count phys.org and ScienceDaily as two sources; they are one release republished twice.
Establishes: Nothing beyond the source.washu.edu / phys.org release.
Paraphrase: n/a
Locators:  Full article.
Quote:     None recorded.
```

This candidate is weaker than the recommended replacement on every axis the
commission weighs: it is nine days old on the 15th rather than two; its central
claim required correcting because the article's framing contradicted the
primary; and its only secondary sourcing is one institutional press release
republished across two aggregators, not a genuinely separate account. Keep it
only if the writer and editor decide, for other reasons, that the AMOC
replacement doesn't fit the day's mix.

## Contradictions

- **Fuel-cell item: the article's own framing contradicted its cited primary.**
  "Reduces platinum loading" is not supported; the paper's abstract states a
  high platinum loading (40 wt%) held steady, with the advance being ordered,
  durable, small particles at that high loading, not a lower loading
  percentage. This is now corrected above; flagging here per the researcher
  standard's instruction to record contradictions in full, since a future
  writer could reintroduce the same error from an earlier draft.
- **Fuel-cell item: a numeric contradiction between the primary and its own
  institution's press release.** The Nature Nanotechnology abstract states the
  catalyst "retained 82.5% performance after a rigorous accelerated stress test
  of 150,000-voltage cycles." Washington University's own release (and its
  phys.org/ScienceDaily republications) states "85%." The primary's number
  governs; 82.5% is correct if this item runs.
- **AMOC item and fuel-cell item share a sourcing limitation.** Neither has a
  secondary account that is genuinely independent (outside the study's own
  institution) with its own added reporting or an outside expert's comment.
  Both rest on one university communications-office release, republished
  across science-news aggregators that add no verification of their own. This
  is disclosed for both rather than silently accepted for one and flagged for
  the other.
- **Apple/Alibaba: single-origin sourcing dressed as multiple accounts.** Every
  outlet I read on this story (Yahoo/Reuters, MacRumors, Benzinga,
  MacDailyNews, Japan Times, Seeking Alpha, Foreign Policy Journal) attributes
  the claim to the same Reuters report, which itself rests on three unnamed
  sources. Under the researcher standard, two retellings of one origin count as
  one confirmation, not two. This item does not currently clear the
  two-independent-confirmation bar for an accusation-grade claim, though it is
  not an accusation — it is a business-strategy report, where the standard is
  looser. Flag for the writer regardless: treat it as "Reuters reports," not as
  established fact.
- **Apple/Alibaba: two different claims are being conflated across the
  coverage.** Bloomberg's July 15, 2026 report says China approved Apple
  Intelligence for iPhones with Alibaba and Baidu as named partners — i.e.,
  Apple integrating Alibaba's existing Qwen model. The August 14 Reuters report
  describes something different: Apple training its own proprietary model,
  with Alibaba's help. Keep these distinct.
- **DeepSeek V4 Pro: benchmark table is unverified by design, and the record
  says so.** DeepSeek's own GA announcement and every secondary account agree
  no independent lab has reproduced the 0813 build's benchmark numbers. Not a
  disagreement between sources — a documented absence of verification.
- **Gemini 3.7 Flash: Google's and Artificial Analysis's benchmark suites do
  not overlap**, so there is no direct number-for-number comparison between the
  vendor's self-reported gains and the independent GDPVal-AA/Intelligence Index
  scores. Report them as separate measurements, not as confirming or
  contradicting each other on the same scale.
- **GPT-5.6-Cyber: the Chrome vulnerability finding predates the model's public
  release.** The underlying report-to-fix timeline (reported July 6, fixed July
  16) is roughly a month before GPT-5.6-Cyber's August 10 public launch. Worth
  stating precisely rather than letting "GPT-5.6-Cyber found a Chrome zero-day"
  imply post-launch, third-party use.

## Numbers

```text
Figure: GPT-5.6-Cyber completes 95% of requests involving exploit chains, authentication bypass, and privilege escalation
Owner:  OpenAI (self-reported, on OpenAI's own ExploitGym benchmark)
Scope:  Compared against a 1.5% completion rate OpenAI reports for standard GPT-5.6 on the same task set; no external reproduction found
```

```text
Figure: DeepSeek V4 Pro — 1.6 trillion total parameters, 49 billion active per token, 1,000,000-token context, 384,000-token max output
Owner:  DeepSeek (model card / API docs; parameter figures corroborated by independent secondary reporting reading the same card, not independently measured)
Scope:  Applies to the V4-Pro-0813 GA build specifically
```

```text
Figure: DeepSeek V4 Pro benchmark scores — SWE-bench Verified 80.6%, Terminal-Bench 2.0 67.9%, GPQA Diamond 90.1%, MMLU-Pro 87.5%, LiveCodeBench 93.5%, Codeforces rating 3,206
Owner:  DeepSeek (self-reported, own harness)
Scope:  0813 GA build; zero independent reproduction, per Digital Applied's verified statement: "At the time of writing, no independent reproduction of any GA-specific figure exists"
```

```text
Figure: DeepSeek V4 Pro output pricing rises from a flat $0.87/1M tokens to peak-hour $3.96/1M tokens
Owner:  DeepSeek (own pricing page)
Scope:  Effective 16:00 UTC, August 16, 2026; off-peak rate set at half the peak rate
```

```text
Figure: Gemini 3.7 Flash introductory price $0.75/1M input, $3.75/1M output tokens
Owner:  Google (own blog post)
Scope:  Through December 31, 2026; rises to $1.50/$7.50 on January 1, 2027
```

```text
Figure: Gemini 3.7 Flash benchmark deltas vs. 3.6 Flash — FrontierCode 1.1 Main 43.6% vs. 34.4%; DeepSWE v1.1 65.3% vs. 49.0%; WebDev Arena Elo 1,588 vs. 1,538; AutomationBench 30.4% vs. 17.0%
Owner:  Google (self-reported, own harness, own choice of comparison baseline)
Scope:  Comparison is to Google's own immediately prior model only
```

```text
Figure: Gemini 3.7 Flash (high) scores 56 on Artificial Analysis's Intelligence Index v4.1.1, ranked 17th of 188 models, price-tier median 34
Owner:  Artificial Analysis (independent third-party benchmarking organization)
Scope:  https://artificialanalysis.ai/models/gemini-3-7-flash — confirmed live on this page
```

```text
Figure: Gemini 3.7 Flash (high) scores 1,525 on Artificial Analysis's GDPVal-AA v2 leaderboard (rank 24), a +103 gain over Gemini 3.6 Flash (high, 1,422, rank 36); trails Muse Spark 1.2 (xhigh, 1,628, rank 11), Claude Sonnet 5 (Adaptive Reasoning, Max Effort, 1,598, rank 14), and GPT-5.6 Terra (max, 1,578, rank 18)
Owner:  Artificial Analysis (independent third-party benchmarking organization; primary-grade for its own leaderboard)
Scope:  https://artificialanalysis.ai/evaluations/gdpval-aa — CORRECTED CITATION. All five figures confirmed by direct fetch this session; the +103 is arithmetic on the two Gemini rows, not a number the page states as a delta itself
```

```text
Figure: Muse Glimmer 30B — ~29.6B total parameters (incl. ~1.8B vision encoder), 131,072+ token context window
Owner:  Meta (own Hugging Face model card)
Scope:  Applies to the released BF16/GGUF weights on the meta-models Hugging Face org
```

```text
Figure: Muse Glimmer benchmark scores — MCP Atlas 75.5, SWE-Bench Pro 51.2, SWE-Bench Verified 76.0, AIME 2026 94.7, GPQA Diamond 83.5, MMMU Pro 74, Charxiv Reasoning 78.8
Owner:  Meta (self-reported, own model card)
Scope:  No independent reproduction found; InfoQ explicitly confirmed it ran no benchmarks of its own
```

```text
Figure: Muse Glimmer DFlash speculative-decoding speedup — 3.1x on RTX 5090, 1.8x on M5 Max, 1.5x on M4 Max
Owner:  Meta (self-reported)
Scope:  Hardware-specific; no independent hardware benchmark found
```

```text
Figure: CVE-2026-15903 (Chrome V8 out-of-bounds read/write), CVSS v3 8.8 (High)
Owner:  Independent — Chrome/Chromium's own vulnerability disclosure, catalogued by Tenable's third-party CVE database
Scope:  Affects Chrome versions before 150.0.7871.128; published July 20, 2026, updated July 24; report/fix dates (July 6/July 16) precede GPT-5.6-Cyber's August 10 public launch
```

```text
Figure: IBM/OpenAI — no consultant headcount, dollar figure, or contract term disclosed
Owner:  n/a (absence of a figure, both companies)
Scope:  Confirmed absent in IBM's own release and in TechCrunch's independent read
```

```text
Figure: AMOC collapse threshold is not fixed — stable to +5.5°C global warming under slow CO2 forcing (+0.5 ppm/yr), collapses at +2.0°C under fast forcing; prior single-threshold estimate was +4.0°C (uncertainty range 1.4-8°C)
Owner:  van Westen, Börner, and Dijkstra (Utrecht University), Nature Climate Change — read directly from the paper's own abstract
Scope:  Climate-model simulation result (idealized CO2 ramp scenarios), not an observational measurement or a prediction of which scenario the real world will follow
```

```text
Figure: AMOC critical warming rate approximately 0.3°C per decade
Owner:  Utrecht University's own press release (source.washu.edu-equivalent: source.washu.edu is the fuel-cell item; this figure is from Utrecht's release, republished on phys.org), attributed to the same paper
Scope:  Not found stated as an exact figure in the abstract text itself; treat as the institution's own gloss on the paper pending a full-text read, not yet independently confirmed against the paper's body
```

```text
Figure: Fuel-cell catalyst — 40 wt% platinum loading (kept high, not reduced), sub-5nm particles at >1,000°C, >80% ordered L10-PtCo phase, current density 2.12 A/cm2 at 0.70V under heavy-duty vehicle conditions, 82.5% performance retained after 150,000 voltage cycles
Owner:  Gao, Hwang, Li, Zheng, Lee, Liu, Wierzbicki, Li, Guo, Zhang, Lin, Zhao, Wang, Dun, and Wu (Washington University in St. Louis and collaborators), Nature Nanotechnology — read directly from the paper's own abstract
Scope:  Laboratory cycling test; durability claim, not a field-deployment result. CORRECTED: the 82.5% figure supersedes the 85% figure in researcher/01, which traced only to the non-independent WashU press release, not the primary
```

## Source assets

```text
Asset: DeepSeek's embedded benchmark comparison image (img/v4_260813_benchmark_table_en.png) on the API-docs GA announcement
Shows: The full vendor-reported score table for V4-Pro-0813 against named rival models, in one place
Crop:  Would need the DeepSeek-only row(s) if used; the rival-model columns are DeepSeek's own reproductions of rivals' scores, not the rivals' self-reported numbers, and should not be presented as if independently sourced
```

```text
Asset: Meta's Muse Glimmer 30B benchmark table on the Hugging Face model card, comparing to Gemma4-31B and Qwen3.6-27B
Shows: Relative standing across agentic, coding, multimodal, safety, and reasoning benchmarks in Meta's own testing
Crop:  Label clearly as Meta's self-reported comparison; omit any implication of third-party testing
```

```text
Asset: Artificial Analysis's GDPVal-AA v2 leaderboard table (artificialanalysis.ai/evaluations/gdpval-aa)
Shows: Where Gemini 3.7 Flash actually lands against named rivals on an independently run, cross-vendor agentic-task benchmark — the load-bearing comparison for the Gemini item's headline claim
Crop:  The five named rows (Gemini 3.7 Flash high, Gemini 3.6 Flash high, Muse Spark 1.2 xhigh, Claude Sonnet 5 Max Effort, GPT-5.6 Terra max) are what the item needs; the full ~60-row table is not
```

```text
Asset: OpenAI's Preparedness Framework threshold table on the GPT-5.6 Deployment Safety Hub (Informational/High/Critical, with the External Evaluations subsection naming Irregular and UK AISI)
Shows: How OpenAI's own classification process incorporates named external evaluators, distinguishing this from a bare self-report
Crop:  Keep the threshold definitions and the external-evaluator naming together; do not crop out the evaluator names
```

```text
Asset: None found for the IBM/OpenAI partnership, the Apple/Alibaba report, or the DeepSeek/Gemini text sourcing beyond the tables above.
```

```text
Asset: None found for the AMOC paper (text abstract only; no chart accessible past the paywall this session).
```

```text
Asset: None found for the fuel-cell item beyond the abstract text (figures are behind the same paywall).
```

## Discarded

```text
URL: https://www.sciencemediacentre.org/expert-reaction-to-a-modelling-study-suggesting-that-amoc-may-be-resilient-to-future-warming/ — Looked like independent expert reaction to the AMOC replacement candidate; on fetch, it covers a different, earlier paper (Baker et al. 2025, Nature, DOI 10.1038/s41586-024-08544-0), not the van Westen/Börner/Dijkstra August 13, 2026 paper. Not usable as a source for this item.
```

```text
URL: https://www.sciencedaily.com/releases/2026/07/... (Aalto University superconducting quantum heat engine, republished by ScienceDaily August 14) — Considered as an alternative fresh-science candidate. Rejected: the underlying paper posted July 13, 2026, a month before the round; the August 14 date is only the media republish date, the same staleness problem that sank the fuel-cell item's dating and, before that, the discarded SS-H2 steel story in researcher/01.
```

```text
URL: https://www.nature.com/articles/s41586-026-10845-5 (piezochiral effect) — Considered as an alternative fresh-science candidate: a genuinely new physical effect (mechanical strain inducing chirality in achiral crystals), well-covered, primary-sourced. Rejected on dating only: published online July 29, 2026, over two weeks before the round; no news peg ties it to August 13-15 specifically.
```

```text
URL: Antineutrino "reactor afterglow" study (Double Chooz, Physical Review Letters) — Considered. Rejected on dating: the paper posted August 4, 2026, eleven days before the round; ScienceDaily's August 14 republication is the press date, not the paper's date.
```

```text
URL: https://www.macrumors.com/2026/08/14/apple-trained-own-ai-model-for-china/ — Not discarded as a source (used above), but flagged here too: contributes no reporting independent of the single Reuters origin; do not count as a second confirming source.
```

```text
URL: https://finance.yahoo.com/technology/ai/articles/pony-ai-uber-plan-deployment-102107759.html — Uber/Pony.ai plan to deploy 2,000+ robotaxis across Europe (announced Aug 14). Rejected as a candidate: a commercial fleet-scale-up of an already-existing Level 4 driving stack, not a new technical capability or research result.
```

```text
URL: https://en.wikipedia.org/wiki/Aspera_(spacecraft) and https://rocketlabcorp.com/missions/launches/aspera/ — NASA's Aspera EUV astrophysics smallsat, scheduled to launch August 15, 2026. Rejected: a launch is an event, not yet a research result.
```

```text
URL: (FDA/Moderna mFLUSIVA coverage) — First mRNA flu vaccine FDA approval. Rejected on dating: FDA approval was August 5, 2026, ten days before the round.
```

```text
URL: https://www.forbes.com/sites/jonmarkman/2026/08/11/openai-ships-gpt-56-cyber-its-first-offense-grade-hacking-model/ — Returned HTTP 403 on fetch (gated). Did not use; Help Net Security and the OpenAI primary pages cover the same ground and were read in full.
```

```text
URL: https://www.marktechpost.com/2026/08/10/meta-ai-releases-muse-glimmer/ — Fetch returned empty content this session (possible caching/render issue). Not cited; InfoQ was read in full instead.
```

```text
URL: https://www.bloomberg.com/news/articles/2026-08-13/google-debuts-new-gemini-flash-while-top-ai-model-still-delayed and https://www.axios.com/2026/08/13/google-gemini-37-flash — Both returned HTTP 403 (paywall/gate). Not cited directly; 9to5google and Artificial Analysis cover the independent angle adequately.
```
