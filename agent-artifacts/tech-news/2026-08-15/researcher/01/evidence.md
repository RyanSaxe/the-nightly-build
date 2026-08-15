# Evidence record: tech-news/2026-08-15 (researcher/01)

The evidence supports six strong, independently confirmed AI-field developments
clustered in the week before August 15, and a seventh, weaker science candidate
for breadth. All six commissioned candidates are real, dated, and each has a
primary source plus at least one independent account: IBM/OpenAI (Aug 13),
Apple/Alibaba's China LLM (Aug 14, reported), DeepSeek V4 Pro (Aug 12-13 GA),
Gemini 3.7 Flash (Aug 13), GPT-5.6-Cyber's High cyber-capability rating (Aug 10),
and Meta's Muse Glimmer 30B (Aug 10). None is dated August 15 itself; the closest
the record gets to the 15th is the DeepSeek V4 Pro pricing change (effective Aug
16, 16:00 UTC) and an independent forensic write-up of the V4 Pro release
published Aug 15. The evidence is thin in two specific ways the writer should
weigh: (1) the Apple/Alibaba item has no company-confirmed primary source at
all — every account, independent-looking or not, traces to one Reuters report
citing three unnamed sources, so it fails a strict two-independent-confirmation
test even though it is widely repeated; and (2) three of the six items (DeepSeek
V4 Pro's benchmark table, Meta's Muse Glimmer benchmark table, and part of
Google's Gemini 3.7 Flash claims) rest on vendor-published benchmark images I
could not read pixel values from — I have the surrounding text and, where an
independent evaluator (Artificial Analysis, for Gemini) ran its own numbers, I
recorded those separately. GPT-5.6-Cyber's headline capability claim is the
best-corroborated of the six: OpenAI's own classification is echoed by two named
external evaluators (Irregular, UK AISI) in the same system-card document, and
one specific outcome it cites (a Chrome V8 vulnerability) is independently
confirmed in Chrome's own CVE record. The hack-back NSPM is excluded throughout,
as commissioned.

## Sources

### 1. IBM/OpenAI enterprise partnership

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

### 3. DeepSeek V4 Pro reaches general availability

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
Establishes: Using Internet Archive snapshots, the piece bounds the GA release to a roughly 32-hour window (Aug 12-13) and documents that the version string appeared first in DeepSeek's price list, with no separate announcement — a distinct fact from what DeepSeek's own changelog states. Explicitly states: "every cell in both tables is DeepSeek-stated" and "no independent reproduction of any GA-specific figure exists" for the 0813 build. Notes the release lacks a published Jinja chat template and that the GA build carries no disclosed parameter count of its own (distinct from the general V4-Pro architecture figures). Reports that accounts using the alias "deepseek-v4-pro" were upgraded in place without a version pin, a compliance-relevant operational detail.
Paraphrase: This is read-and-verified independent skepticism, not a repetition of DeepSeek's claims.
Locators:  Full article; byline dated August 15, 2026.
Quote:     "None of these columns has yet been replicated by an independent evaluator for the 0813 build."
```

Benchmark figures as reported by DeepSeek (self-reported; see Numbers section for full detail and the independent-verification caveat above): SWE-bench Verified 80.6%, Terminal-Bench 2.0 67.9%, GPQA Diamond 90.1%, MMLU-Pro 87.5%, LiveCodeBench 93.5%, Codeforces rating 3,206.

### 4. Google ships Gemini 3.7 Flash

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
Kind:        Independent third-party benchmark organization — the one genuinely independent measurement found for any of the six candidates. Artificial Analysis runs its own evaluation harness and has no stake in Google's results.
Establishes: Gemini 3.7 Flash (high) scores 56 on Artificial Analysis's own Intelligence Index v4.1.1 (a 9-evaluation composite), ranked 17th of 188 models the organization has tested, "well above average among comparable models (median: 34)" in its price tier. On Artificial Analysis's own GDPVal-AA v2 composite, a separate page (via X/Artificial Analysis) put Gemini 3.7 Flash at 1,525, a +103 point gain over 3.6 Flash, trailing Muse Spark 1.2 (1,628), Claude Sonnet 5 (1,598), and GPT-5.6 Terra (1,578).
Paraphrase: These numbers do not match any figure in Google's own blog post (which uses FrontierCode, DeepSWE, WebDev Arena Elo, and AutomationBench, not Intelligence Index or GDPVal-AA) — they are a genuinely separate, independently run measurement, not a re-statement of Google's claims.
Locators:  Model page; last-updated date not shown on the fetched excerpt.
Quote:     None recorded.
```

Google's own reported benchmark deltas (self-reported, Google's harness, vs. Gemini 3.6 Flash): FrontierCode 1.1 Main 43.6% vs. 34.4%; DeepSWE v1.1 65.3% vs. 49.0%; WebDev Arena Elo 1,588 vs. 1,538; AutomationBench 30.4% vs. 17.0%. (One further figure, transcribed from the fetch as "GDP.pdf" at 34.0% vs. 22.0%, could not be confirmed against a benchmark with that exact name in independent searches — likely a mis-transcription of a benchmark abbreviation; flagged, not used as a clean citation. Do not cite this figure without re-reading the blog post's own image/table directly.)

### 5. OpenAI's GPT-5.6-Cyber reaches "High" cyber capability

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

### 7. (Additional, weaker candidate) Platinum-sparing fuel-cell catalyst

```text
URL:         https://www.nature.com/articles/s41565-026-02244-8
Kind:        Primary — the peer-reviewed paper itself (Nature Nanotechnology). Gated: redirected to a Nature login/authorization page on fetch (303 to idp.nature.com). Recorded as the paper's own canonical page per the researcher standard; content below is drawn from the secondary source, not read directly.
Establishes (per DOI and secondary reporting): A nanostructured, porous hollow-carbon-sphere support that lets platinum-cobalt intermetallic fuel-cell catalysts use sharply reduced platinum loading while retaining durability. Published online August 6, 2026. DOI 10.1038/s41565-026-02244-8. Led by Gang Wu's group at Washington University in St. Louis, with Brookhaven National Laboratory, Lawrence Berkeley National Laboratory, Northeastern University, and University of Pittsburgh collaborators.
Paraphrase: I have not read the paper's own text or figures; the specific durability figure below comes only from the secondary account.
Locators:  Not directly accessible this session; DOI resolves in principle to the publisher.
Quote:     None taken; do not quote without re-fetching past the login gate.
```

```text
URL:         https://phys.org/news/2026-08-carbon-nanostructure-fuel-cell-catalyst.html
Kind:        Secondary/independent science-press account, not affiliated with the research team.
Establishes: Reports the catalyst "retained 85% of its performance after 150,000 harsh voltage cycles, likely equivalent to 25,000 hours of operation," and that nanoparticles stayed under 5 nanometers even after heating to 1,000°C.
Paraphrase: Frames the application as making hydrogen fuel cells more viable for data centers and vehicles — this framing is the journalist's, not a quoted claim from the paper.
Locators:  Full article.
Quote:     None recorded.
```

This candidate is weaker than the other six on the commission's own dating standard: the paper posted August 6, nine days before the 15th, and I could not read the primary text directly (gated). It earns a place on the list only because the durability result is a genuine, quantified change in catalyst practice (platinum-loading reduction at retained durability), not a launch or attention story — the writer should weigh whether nine days is still "on or around" the 15th, or cut it.

## Contradictions

- **Apple/Alibaba: single-origin sourcing dressed as multiple accounts.** Every outlet I read on this story (Yahoo/Reuters, MacRumors, Benzinga, MacDailyNews, Japan Times, Seeking Alpha, Foreign Policy Journal) attributes the claim to the same Reuters report, which itself rests on three unnamed sources. Under the researcher standard, two retellings of one origin count as one confirmation, not two. I could not find a second newsroom's own independent sourcing (a distinct Bloomberg, WSJ, or SCMP report with its own named or unnamed sources making the same claim) in this session's search budget. This item does not currently clear the two-independent-confirmation bar for an accusation-grade claim, though it is not an accusation — it is a business-strategy report, where the standard is looser. Flag for the writer regardless: treat it as "Reuters reports," not as established fact, and do not present the "first foreign company approved" framing as independently confirmed.
- **Apple/Alibaba: two different claims are being conflated across the coverage.** Bloomberg's July 15, 2026 report says China approved Apple Intelligence for iPhones with Alibaba and Baidu as named partners — i.e., Apple integrating Alibaba's existing Qwen model, the same arrangement Apple briefly documented in a since-removed support guide (per MacRumors). The August 14 Reuters report describes something different: Apple training its own proprietary model, with Alibaba's help, rather than shipping Alibaba's model directly. Some derivative coverage blurs these two into one continuous story. The writer should keep "integrating a partner's model" (confirmed, July) and "training an in-house model with a partner's help" (reported, single-sourced, August) distinct.
- **DeepSeek V4 Pro: benchmark table is unverified by design, and the record says so.** DeepSeek's own GA announcement and every secondary account I read agree explicitly that no independent lab has reproduced the 0813 build's benchmark numbers. This is not a disagreement between sources — it is a documented absence of verification that the writer should state plainly rather than repeat DeepSeek's figures at face value.
- **Gemini 3.7 Flash: Google's and Artificial Analysis's benchmark suites do not overlap**, so there is no direct number-for-number comparison available between the vendor's self-reported gains and the independent index score. Both are legitimate but not directly reconcilable; report them as separate measurements, not as confirming or contradicting each other on the same scale.
- **GPT-5.6-Cyber: the Chrome vulnerability finding predates the model's public release.** OpenAI's announcement cites the V8 discovery as evidence of the model's real-world capability, but the underlying report-to-fix timeline (reported July 6, fixed July 16, per Chrome's own release notes as found in secondary search) is roughly a month before GPT-5.6-Cyber's August 10 public launch. This does not make the finding false, but it means the capability being cited was demonstrated by an internal/pre-release version, not by any external party using the publicly released model — worth stating precisely rather than letting "GPT-5.6-Cyber found a Chrome zero-day" imply post-launch, third-party use.

## Numbers

```text
Figure: GPT-5.6-Cyber completes 95% of requests involving exploit chains, authentication bypass, and privilege escalation
Owner:  OpenAI (self-reported, on OpenAI's own ExploitGym benchmark)
Scope:  Compared against a 1.5% completion rate OpenAI reports for standard GPT-5.6 on the same task set; no external reproduction found
```

```text
Figure: DeepSeek V4 Pro — 1.6 trillion total parameters, 49 billion active per token, 1,000,000-token context, 384,000-token max output
Owner:  DeepSeek (model card / API docs; parameter figures corroborated by independent secondary reporting reading the same card, not independently measured)
Scope:  Applies to the V4-Pro-0813 GA build specifically; DeepSeek's own GA changelog does not restate the parameter count in readable text
```

```text
Figure: DeepSeek V4 Pro benchmark scores — SWE-bench Verified 80.6%, Terminal-Bench 2.0 67.9%, GPQA Diamond 90.1%, MMLU-Pro 87.5%, LiveCodeBench 93.5%, Codeforces rating 3,206
Owner:  DeepSeek (self-reported, own harness)
Scope:  0813 GA build; explicitly zero independent reproduction as of the sources read; rival-model comparison columns are DeepSeek's own reproductions of rivals' scores, not the rivals' self-reports
```

```text
Figure: DeepSeek V4 Pro output pricing rises from a flat $0.87/1M tokens to peak-hour $3.96/1M tokens
Owner:  DeepSeek (own pricing page)
Scope:  Effective 16:00 UTC, August 16, 2026; off-peak rate set at half the peak rate; input pricing separately listed at $0.435/1M (cache miss) and $0.003625/1M (cache hit)
```

```text
Figure: Gemini 3.7 Flash introductory price $0.75/1M input, $3.75/1M output tokens
Owner:  Google (own blog post)
Scope:  Through December 31, 2026; rises to $1.50/$7.50 on January 1, 2027; Google frames this as half the price of the prior model's launch pricing
```

```text
Figure: Gemini 3.7 Flash benchmark deltas vs. 3.6 Flash — FrontierCode 1.1 Main 43.6% vs. 34.4%; DeepSWE v1.1 65.3% vs. 49.0%; WebDev Arena Elo 1,588 vs. 1,538; AutomationBench 30.4% vs. 17.0%
Owner:  Google (self-reported, own harness, own choice of comparison baseline)
Scope:  Comparison is to Google's own immediately prior model only, not to competing labs' models on these particular benchmarks
```

```text
Figure: Gemini 3.7 Flash (high) scores 56 on Artificial Analysis's Intelligence Index v4.1.1, ranked 17th of 188 models tested; separately, 1,525 on Artificial Analysis's GDPVal-AA v2 (+103 over 3.6 Flash)
Owner:  Artificial Analysis (independent third-party benchmarking organization; not Google)
Scope:  Own composite indices, not directly comparable cell-for-cell to Google's self-reported benchmarks above; GDPVal-AA v2 places it behind Muse Spark 1.2 (1,628), Claude Sonnet 5 (1,598), and GPT-5.6 Terra (1,578)
```

```text
Figure: Muse Glimmer 30B — ~29.6B total parameters (incl. ~1.8B vision encoder), 131,072+ token context window
Owner:  Meta (own Hugging Face model card)
Scope:  Applies to the released BF16/GGUF weights on the meta-models Hugging Face org; no independent parameter audit found
```

```text
Figure: Muse Glimmer benchmark scores — MCP Atlas 75.5, SWE-Bench Pro 51.2, SWE-Bench Verified 76.0, AIME 2026 94.7, GPQA Diamond 83.5, MMMU Pro 74, Charxiv Reasoning 78.8
Owner:  Meta (self-reported, own model card, own comparison to Gemma4-31B and Qwen3.6-27B)
Scope:  No independent reproduction found in any of the sources read; InfoQ explicitly confirmed it ran no benchmarks of its own
```

```text
Figure: Muse Glimmer DFlash speculative-decoding speedup — 3.1x on RTX 5090, 1.8x on M5 Max, 1.5x on M4 Max
Owner:  Meta (self-reported)
Scope:  Hardware-specific; no independent hardware benchmark found to confirm or contradict
```

```text
Figure: CVE-2026-15903 (Chrome V8 out-of-bounds read/write), CVSS v3 8.8 (High)
Owner:  Independent — Chrome/Chromium's own vulnerability disclosure, catalogued by Tenable's third-party CVE database
Scope:  Affects Chrome versions before 150.0.7871.128; published July 20, 2026, updated July 24; discovery credited to OpenAI's security research in Chrome's own release notes per secondary reporting, with report/fix dates (July 6/July 16) preceding GPT-5.6-Cyber's August 10 public launch
```

```text
Figure: IBM/OpenAI — no consultant headcount, dollar figure, or contract term disclosed
Owner:  n/a (absence of a figure, both companies)
Scope:  Confirmed absent in IBM's own release and in TechCrunch's independent read; do not fill in a number the companies did not give
```

```text
Figure: Fuel-cell catalyst retains 85% of performance after 150,000 voltage cycles (~25,000 operating hours)
Owner:  Washington University in St. Louis research team (Gang Wu), per Nature Nanotechnology paper, as relayed by phys.org — I did not read the primary figure myself (gated)
Scope:  Laboratory cycling test; durability claim, not a field-deployment result
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
Asset: Artificial Analysis's Gemini 3.7 Flash Intelligence Index page (chart of the 9-evaluation composite ranked against 188 models)
Shows: Where the model actually lands on an independently run, cross-vendor scale, distinct from Google's own single-model-comparison benchmarks
Crop:  The ranking position and the price-tier median comparison are the load-bearing parts; the full 188-model list is not needed
```

```text
Asset: OpenAI's Preparedness Framework threshold table on the GPT-5.6 Deployment Safety Hub (Informational/High/Critical, with the External Evaluations subsection naming Irregular and UK AISI)
Shows: How OpenAI's own classification process incorporates named external evaluators, distinguishing this from a bare self-report
Crop:  Keep the threshold definitions and the external-evaluator naming together; do not crop out the evaluator names, since that is what separates this from an unverified claim
```

```text
Asset: None found for the IBM/OpenAI partnership (text-only press release) or the Apple/Alibaba report (text-only reporting, no chart or figure in any source read).
```

## Discarded

```text
URL: https://www.sciencedaily.com/releases/2026/08/260811052717.htm — Corrosion-resistant "SS-H2" stainless steel story. Traced to the actual DOI (10.1016/j.mattod.2023.07.022): the underlying paper is from 2023, in Materials Today. This is old research getting a fresh media write-up in August 2026, not a new dated development, so it fails the commission's "developments dated on or around August 15, 2026" requirement outright.
```

```text
URL: https://www.macrumors.com/2026/08/14/apple-trained-own-ai-model-for-china/ — Not discarded as a source (used above), but flagged here too: contributes no reporting independent of the single Reuters origin; do not count as a second confirming source.
```

```text
URL: https://finance.yahoo.com/technology/ai/articles/pony-ai-uber-plan-deployment-102107759.html — Uber/Pony.ai plan to deploy 2,000+ robotaxis across Europe (announced Aug 14). Rejected as a candidate: this is a commercial fleet-scale-up of an already-existing Level 4 driving stack (Pony.ai's), not a new technical capability, benchmark, or research result. Fits the series' express exclusion of "product promotion, incremental releases, and online attention," not "changes technical knowledge or practice."
```

```text
URL: https://en.wikipedia.org/wiki/Aspera_(spacecraft) and https://rocketlabcorp.com/missions/launches/aspera/ — NASA's Aspera EUV astrophysics smallsat, scheduled to launch on a Rocket Lab Electron on August 15, 2026. Rejected: a launch is an event, not yet a research result — the mission has not returned data. Revisit only if a future edition covers its first science return.
```

```text
URL: (FDA/Moderna mFLUSIVA coverage, e.g. https://www.statnews.com/2026/08/05/fda-approves-moderna-mflusiva-first-mrna-flu-vaccine/) — First mRNA flu vaccine FDA approval. Rejected primarily on dating: FDA approval was August 5, 2026, ten days before the 15th, outside "on or around." Also arguably a regulatory/product story more than a new technical result, though the platform-speed argument (antigenic updates in 2-3 months vs. ~6) is a genuine practice change if the writer wants to revisit it against a looser dating standard.
```

```text
URL: https://www.forbes.com/sites/jonmarkman/2026/08/11/openai-ships-gpt-56-cyber-its-first-offense-grade-hacking-model/ — Returned HTTP 403 on fetch (gated). Did not use as a cited source since I could not read it directly this session; Help Net Security and the OpenAI primary pages cover the same ground and were read in full.
```

```text
URL: https://www.marktechpost.com/2026/08/10/meta-ai-releases-muse-glimmer/ — Fetch returned empty content this session (possible caching/render issue). Not cited; InfoQ was read in full instead and covers the same territory.
```

```text
URL: https://www.bloomberg.com/news/articles/2026-08-13/google-debuts-new-gemini-flash-while-top-ai-model-still-delayed and https://www.axios.com/2026/08/13/google-gemini-37-flash — Both returned HTTP 403 (paywall/gate). Not cited directly; 9to5google and Artificial Analysis were read in full and cover the independent angle adequately.
```
