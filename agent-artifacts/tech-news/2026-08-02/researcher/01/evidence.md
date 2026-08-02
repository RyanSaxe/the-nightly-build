# Evidence record: tech-news/2026-08-02 (01)

## Overview

The evidence supports a 4-item slate, all AI-central but reached from four
different angles, which satisfies "significance decides the mix" without
forcing a non-AI item the day did not produce. Two items land on the exact
dateline with hard, checkable facts: the EU AI Act's Article 50 transparency
regime takes legal effect on 2026-08-02 itself, and the Trump administration's
Executive Order 14409 deadline for a frontier-AI review framework expired at
2026-08-01 00:00Z with no public deliverable — a clean contrast between a
regulator that hit its date and one that didn't. A third, OpenAI's field
report on coding agents modernizing scientific research software, is dated
2026-08-01 in independent coverage and carries an unusually well-sourced
caveat (agents "couldn't judge whether their own output was scientifically
correct") that keeps it from reading as vendor promotion. The fourth,
DeepSeek-V4-Flash-0731, is a 2026-07-31 official release verified against the
vendor's own changelog and against Artificial Analysis's independent
benchmark run; it is two days off the dateline, which the writer should
weigh against the other three.

Where the record is thin: I could not directly fetch openai.com's primary
report page (persistent 403, likely bot-blocking; confirmed via WebFetch
twice and curl once) — its numbers are triangulated from two independent
outlets that quote it verbatim, not read on the primary page itself. The
EO 14409 "deadline lapsed" claim rests on one directly-read independent
account (Forkast/Yahoo Finance); a second, CNBC's 2026-07-31 story, could not
be fetched (403) and is not cited as a source, only noted as attempted.
Candidates researched and rejected as too stale, too thin, or too promotional
for 2026-08-02 are in Discarded. No item here duplicates the paper-of-the-day
subject (an older ML paper) or the previously-covered items the commission
flagged (Claude/HAWK cryptanalysis, Ruflo RCE, Nvidia-AI-security alliance,
Nvidia-SSI, Kimi K3, the OpenAI-model HuggingFace incident).

Recommended slate and lead order:
1. **EU AI Act Article 50 takes effect** (regulatory; non-security lead)
2. **OpenAI field report on coding agents in scientific computing**
3. **US frontier-AI executive order deadline lapses without deliverables**
4. **DeepSeek-V4-Flash-0731 official release**

---

## Sources

### Item 1: EU AI Act Article 50 transparency obligations take effect 2026-08-02

**Primary — https://artificialintelligenceact.eu/article/50/**
Classification: Primary. This page reproduces the operative legal text of
Regulation (EU) 2024/1689 Article 50 verbatim; the claim (what the law
requires) is owned by the regulation itself, not by this site's commentary.
Establishes firsthand: the exact four obligations (AI-interaction
disclosure; machine-readable marking of GPAI-generated synthetic content;
deployer disclosure of deepfakes; deployer labeling of AI-generated text on
matters of public interest published without human editorial review) and
cites Article 113 for the application date of "2 August 2026."
Verbatim: "Providers shall ensure that AI systems intended to interact
directly with natural persons are designed and developed in such a way that
the natural persons concerned are informed that they are interacting with an
AI system." Locator: Article 50(1) as reproduced on the page; application
date locator: Article 113 cross-reference on the same page.

**Primary — https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act**
Classification: Primary. Official European Commission page (Directorate-
General for Communications Networks, Content and Technology) — the
regulator itself stating its own enforcement position and timeline.
Establishes firsthand: application date "August 2, 2026," a grace period to
"December 2, 2026" for marking/detection obligations on systems already on
the market before the application date, and the penalty ceiling. Verbatim:
"up to 15 million euros or 3% of total worldwide turnover for the preceding
financial year," with proportionality for SMEs. Locator: FAQ answer sections
on application date and on enforcement/penalties.

**Secondary/independent — https://natlawreview.com/article/eu-ai-act-final-guidelines-transparency-obligations-under-article-50**
Classification: Secondary, independent. Client-alert analysis by Sarah
Pearce and Veronica Muratori of K&L Gates LLP, a law firm with no stake in
the regulation's content, published via National Law Review on 2026-08-02
(underlying alert dated 2026-07-28, referencing the Commission's final
Article 50 guidelines published 2026-07-20). Reports on, does not own, the
law. Useful for scope and compliance-practice framing beyond the bare legal
text. Verbatim: "Article 50 is not limited to high-risk AI systems and may
apply to a broad range of AI solutions, including chatbots, generative AI
tools, emotion recognition systems, biometric categorization tools, and
deepfake technologies." Also: "Generic references hidden in terms and
conditions, website footers, or vague labels are unlikely to be sufficient."
Locator: body sections on scope and on compliance recommendations.

---

### Item 2: OpenAI field report — coding agents modernize scientific research software

**Primary — https://openai.com/index/scientific-computing-agentic-ai/**
Classification: Primary (OpenAI's own field report; it owns the claims about
its case studies). Access note: returned HTTP 403 on two WebFetch attempts
and one curl attempt with a browser user-agent — consistent bot-blocking,
not evidence the page is unreachable to human readers. The page's existence
and exact wording are corroborated by two independently-read outlets below
that quote it directly and by several other outlets (Yowox, Milan Tribune)
that link to it as their source. Do not cite page sections I have not
myself read; the numbers below are attributed to the secondary sources that
quote the primary, not to my own reading of openai.com.

**Secondary/independent — https://the-decoder.com/ai-coding-agents-can-modernize-research-software-but-cant-judge-if-the-science-is-right/**
Classification: Secondary, independent. The Decoder (Jonathan Kemper),
published 2026-08-01 — a technology-news outlet with no stake in OpenAI's
report, adding outside sourcing (a METR study, named researcher quotes) not
present in a vendor writeup. Firsthand reporting on: the RustQC 60x speedup,
the rustar-aligner 99.8%-agreement rewrite claim, and independent critical
context. Verbatim, Brent Pedersen (cyvcf2 developer, quoted by the outlet):
"With coding agents, it's quite easy to go fast; for now, to go far in
science, there's still a need for expert guidance, understanding, taste, and
care." Verbatim, Philip Ewels (RustQC lead): agent output can be "eloquent,
convincing, and confidently wrong in ways that are easy to miss." Also
reports: "A METR study found maintainers rejected ~50% of solutions passing
industry benchmarks; curl's bug bounty collapsed under AI-generated noise" —
independent context on agent-generated code more broadly, not specific to
OpenAI's case studies. Locator: body paragraphs on validation and on
external corroborating research.

**Secondary/independent — https://michaelbriancotter.wordpress.com/2026/07/29/openai-report-links-coding-agents-to-faster-science-software-builds/**
Classification: Secondary, independent commentary/aggregation blog,
published 2026-07-29, quoting the primary report directly with pull-quotes.
Establishes firsthand (as read directly): the exact RustQC figures, the
STAR-aligner Rust rewrite detail, and the HI.SIM timing detail. Verbatim:
"cut runtime by 60 times and disk input/output by 25 times" (RustQC, 15
RNA-sequencing QC tools consolidated); "FastQC-Rust (7x faster), Trim Galore
(3x faster)"; on the aligner, "rewriting a 20,000-line aligner by hand isn't
a sensible use of time, but with an agent it becomes weeks of steered work,"
original tool named as STAR, rewritten in Rust, verified by manual review of
"900 of them by eye" (parity percentage not given in this source — see
Contradictions); on HI.SIM, "cut runtime by 31 percent across a
representative test set" with byte-identical output as the acceptance
criterion. Also verbatim on scope and caveat: "eight early coding-agent
projects," "five projects used Codex alone... three cases, or Codex together
with Claude Code," and "agents handled well-scoped implementation requests
capably but couldn't judge whether their own output was scientifically
sound." Locator: full post body (short-form post, no section headers).

---

### Item 3: US frontier-AI executive order (EO 14409) 60-day deadline lapses without deliverables

**Primary — https://www.presidency.ucsb.edu/documents/executive-order-14409-promoting-advanced-artificial-intelligence-innovation-and-security**
Classification: Primary. The American Presidency Project (UC Santa Barbara)
hosts the verbatim text of the signed executive order; the order itself
owns the deadline it sets. (The Federal Register's own page,
https://www.federalregister.gov/documents/2026/06/05/2026-11415/promoting-advanced-artificial-intelligence-innovation-and-security,
is the official government copy but its automated-fetch route redirected to
an anti-bot interstitial and could not be read directly — recorded here as
the canonical citation but not relied on for quotes; the UCSB mirror,
successfully read, carries the same operative text.) Establishes firsthand:
signing date June 2, 2026; Section 3 ("Secure Frontier Model Deployment")
sets a 60-day clock. Verbatim: "Within 60 days of the date of this order,
the Secretary of the Treasury, the Secretary of War, through the Director of
NSA, and the Secretary of Homeland Security, through the Director of CISA
[...]" must build a classified benchmarking process for "covered frontier
models" and a voluntary disclosure framework. Responsible officials also
include the National Cyber Director, the Assistant to the President for
Science and Technology, and the Secretary of Commerce through the NIST
Director. June 2 + 60 days = August 1, 2026. Locator: Section 3 of the
order.

**Secondary/independent — https://finance.yahoo.com/technology/ai/articles/white-house-ai-framework-deadline-002011007.html**
Classification: Secondary, independent. Forkast News (byline Lena Park),
syndicated via Yahoo Finance, published 2026-07-31 — a news outlet reporting
on the administration's inaction, not a party to the order. Establishes
firsthand: as of publication, the three required deliverables (classified
benchmarking process; voluntary frontier-AI disclosure framework; federal
cyber-workforce expansion plan from OPM) were unfulfilled. Verbatim: "There
were no Federal Register notices, no NIST or CISA publications, and no
statements from the Office of Science and Technology Policy (OSTP)." Also
reports the TRAINS program (standardizing jailbreak-severity scoring across
OpenAI, Anthropic, Google, Microsoft, and xAI) remains without a public
status update, and names Anthropic CEO Dario Amodei in connection with
related AI-policy proposals. Locator: full article body (short-form news
piece).

**Attempted, not cited — CNBC, "Trump's AI executive order nears key deadline as regulation debate intensifies," 2026-07-31**, and techtimes.com's 2026-07-24 EO 14409 deadline preview: both returned HTTP 403 on WebFetch and are not used as sources. A WebSearch-tool paraphrase surfaced a claim that White House spokesperson Kush Desai posted "BREAKING: Trump White House to meet a deadline we set for ourselves" — this is **not verified** (I did not read the primary post or the CNBC page myself) and must not be used in the article without independent verification the writer can perform.

---

### Item 4: DeepSeek-V4-Flash-0731 official release

**Primary — https://api-docs.deepseek.com/updates**
Classification: Primary. DeepSeek's own API changelog; the vendor owns the
claim of what it released and when. Establishes firsthand: release date
"2026-07-31"; verbatim: "DeepSeek-V4-Flash-0731 keeps the same model
architecture and size as DeepSeek-V4-Flash-Preview, and was only
re-post-trained." No pricing or weight-publication language appears in this
changelog entry. Locator: the 2026-07-31 dated entry.

**Secondary/independent — https://artificialanalysis.ai/models/deepseek-v4-flash**
Classification: Secondary, independent. Artificial Analysis is a third-party
model-benchmarking organization with no commercial stake in DeepSeek;
it ran its own evaluation rather than reprinting vendor-reported scores.
Establishes firsthand (its own test result): "DeepSeek V4 Flash 0731
(Reasoning, Max Effort) scores 50 on the Artificial Analysis Intelligence
Index" and ranks "#3 / 101" among models in its class, against a stated
"median Intelligence Index score for comparable open-weight models" of 25.
Also independently confirms: "284B" total parameters, "13B" active
(Mixture-of-Experts), release date "July 31, 2026," pricing "$0.14 per 1M"
input tokens / "$0.28 per 1M" output tokens, and cache-hit pricing of
"$0.003(-98%)" per million tokens (ranked #1/101). Locator: model summary
page, Intelligence Index and pricing sections.

**Corroborating, not separately counted — https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731**
Classification: Secondary hosting/mirror, read directly. Confirms MIT
license language ("This repository and the model weights are licensed under
the MIT License") and a vendor-reported benchmark table (Terminal Bench 2.1:
82.7; DeepSWE: 54.4; Cybergym: 76.7; and others) consistent with other
outlets' reporting of the same table. One extraction of this page returned
"304B params" for total size, which conflicts with the 284B figure
independently confirmed above — flagged in Contradictions; treat 284B/13B
as the reliable figure since it is corroborated by three independently-
authored sources (Artificial Analysis, DeepSeek's own changelog structure as
reported by digitalapplied.com, and the vLLM recipe page) against a single
inconsistent extraction of this one page. Do not use this URL as the sole
citation for the parameter count.

**Secondary, read for corroboration only — https://www.digitalapplied.com/blog/deepseek-v4-flash-0731-official-release-agent-benchmarks**
Classification: Secondary, independent. Published 2026-07-31; directly
quotes DeepSeek's own changelog and states plainly the epistemic status of
the benchmark claims. Verbatim: "Every agent-benchmark number is
vendor-stated" and, as of the article's publication, there had been "zero
third-party reproductions." Also states the 0731 checkpoint's weights were
not confirmed published at time of writing ("the 0731 checkpoint itself has
no published weights") — in tension with the Hugging Face repository
existing under that exact model name (see Contradictions). Locator: body
paragraphs on benchmark provenance and on weight availability.

---

## Contradictions

- **EU AI Act penalty figure**: both primary EU sources (artificialintelligenceact.eu
  and the European Commission FAQ) agree exactly — up to €15 million or 3% of
  worldwide turnover — no contradiction found here, noted for completeness
  since it's the one number in Item 1 the argument would lean on.
- **OpenAI report — genome-aligner parity percentage**: The Decoder states
  the Rust rewrite of the aligner ("rustar-aligner") reached "99.8%
  agreement with original." The other directly-read source
  (michaelbriancotter.wordpress.com) describes the same rewrite (names the
  original as STAR, a widely-used genome aligner) but reports the
  verification method ("900 of them by eye") without stating a percentage.
  These are not strictly contradictory — one may simply omit the figure the
  other states — but I could not independently confirm the 99.8% figure
  against the primary page (blocked). Attribute it to The Decoder by name if
  used, not to OpenAI directly.
- **OpenAI report — synthetic-genome/HI.SIM timing**: An earlier WebSearch
  tool paraphrase (not a directly-read source, not cited above) asserted
  HI.SIM runtime fell "from 1,610 seconds to 27 seconds." This figure does
  not appear in either directly-read secondary source; the two sources I
  did read state a 31% runtime cut with byte-identical output. The
  1,610-to-27 figure looks like a hallucinated or misattributed number and
  should not be used.
- **DeepSeek-V4-Flash-0731 total parameters**: 284B total / 13B active is
  corroborated by three independent readings (Artificial Analysis's own
  benchmark page, the digitalapplied.com writeup, and a WebSearch-surfaced
  vLLM recipe page). One direct extraction of the Hugging Face model card
  returned "304B params" instead. Given the 3-to-1 weight of independent
  confirmation and that a WebFetch extraction is a lossy secondhand read of
  the actual page (not the raw HTML), treat 284B/13B as correct and flag
  304B as likely an extraction error rather than a genuine vendor
  discrepancy.
- **DeepSeek-V4-Flash-0731 weight availability**: digitalapplied.com (read
  2026-07-31 vintage) states the 0731 checkpoint "has no published weights,"
  while a Hugging Face repository named exactly
  "deepseek-ai/DeepSeek-V4-Flash-0731" returned a live model card with a
  benchmark table and an MIT license statement when fetched directly. These
  cannot both be fully true; either the weights were published between the
  digitalapplied.com article and my fetch, or digitalapplied.com's claim
  was wrong at the time, or the Hugging Face repository is a placeholder
  populated ahead of actual weight upload. The writer should not assert
  "open-weight release" as settled fact without the writer's own check of
  whether the Hugging Face files tab contains actual weight files, not just
  a card.
- **EO 14409 deadline "missed" claim — source count**: only one directly-
  read independent account (Forkast/Yahoo Finance) supports the specific
  claim that no deliverables appeared. A second candidate (CNBC) could not
  be fetched. This satisfies the brief's "1+ independent secondary" floor
  but falls short of the two-independent-confirmation bar the skill sets
  for accusation-shaped claims; the writer should frame the claim as "no
  public deliverable had appeared as of [date], per Forkast's reporting"
  rather than as an flatly established fact of government failure.
- **Commission's candidate note on the OpenAI/Anthropic "slow AI that writes
  its own code" letter (~2026-07-29)**: this did not independently confirm
  as a distinct, still-live 08-02 story separate from the EO 14409 coverage;
  see Discarded.

---

## Numbers

| Number | Owning primary | Exact reading | Unit | Denominator/base | Period |
|---|---|---|---|---|---|
| EU AI Act Article 50 application date | Regulation (EU) 2024/1689, Art. 113 (via artificialintelligenceact.eu and EC FAQ) | 2 August 2026 | date | — | one-time application date |
| EU AI Act marking-obligation grace period | European Commission Article 50 FAQ | grace period to 2 December 2026 | date | applies to systems already on market before 2 Aug 2026 | four-month grace window |
| EU AI Act penalty ceiling | European Commission Article 50 FAQ | up to €15,000,000 or 3% of total worldwide turnover, whichever higher | euros / % of turnover | preceding financial year's worldwide turnover | annual |
| EO 14409 signing-to-deadline | The American Presidency Project (EO 14409 text) | signed 2026-06-02; "within 60 days" | days | — | 2026-06-02 to 2026-08-01 |
| EO 14409 deliverables status | Forkast/Yahoo Finance, 2026-07-31 | 0 of 3 required deliverables published (classified benchmarking process; voluntary disclosure framework; OPM cyber-workforce plan) | count | 3 required deliverables | as of 2026-07-31 |
| OpenAI report — RustQC speedup | OpenAI report (via michaelbriancotter.wordpress.com, direct quote) | 60x runtime reduction, 25x disk I/O reduction | multiple (×) | RustQC vs. prior tool set (15 consolidated RNA-seq QC tools) | single reported test |
| OpenAI report — FastQC-Rust / Trim Galore speedups | OpenAI report (via michaelbriancotter.wordpress.com) | 7x and 3x respectively | multiple (×) | vs. prior versions | single reported test |
| OpenAI report — aligner rewrite scale | OpenAI report (via michaelbriancotter.wordpress.com) | 20,000 lines rewritten (STAR aligner, C/C++ to Rust) | lines of code | original codebase size | one-time rewrite |
| OpenAI report — aligner parity | OpenAI report (via The Decoder, attribute to outlet) | 99.8% agreement with original | percent | not stated (comparison basis not specified in source read) | single reported test — use with attribution, see Contradictions |
| OpenAI report — HI.SIM speedup | OpenAI report (via michaelbriancotter.wordpress.com) | 31% runtime reduction, byte-identical output | percent | representative test set | single reported test |
| OpenAI report — case study count and tooling | OpenAI report (via michaelbriancotter.wordpress.com and yowox.com, consistent) | 8 case studies total; 5 used Codex alone, 3 used Codex + Claude Code | count | — | — |
| DeepSeek-V4-Flash-0731 parameters | api-docs.deepseek.com/updates (architecture unchanged) + Artificial Analysis (exact figures) | 284B total, 13B active (MoE) | parameters (billions) | — | as of 2026-07-31 release |
| DeepSeek-V4-Flash-0731 Intelligence Index | Artificial Analysis | 50 (vs. median 25 for comparable open-weight models) | index score | Artificial Analysis Intelligence Index scale | as tested, 2026-07-31 vintage |
| DeepSeek-V4-Flash-0731 pricing | Artificial Analysis | $0.14 / 1M input tokens; $0.28 / 1M output tokens; cache-hit $0.003 (−98%) | USD per 1M tokens | — | as of test date |
| DeepSeek-V4-Flash-0731 Terminal Bench 2.1 | Hugging Face model card (vendor-stated, unreproduced per digitalapplied.com) | 82.7 | benchmark score | Terminal Bench 2.1 scale | vendor-reported, no third-party reproduction confirmed |

---

## Source assets

- **EU AI Act Article 50**: a small table of the four transparency
  obligations (who: providers vs. deployers; what: disclose vs. mark) would
  carry the structure better than a paragraph — the Commission FAQ page
  already organizes it this way. Source: digital-strategy.ec.europa.eu FAQ
  page (see Sources, Item 1). A reader can learn which obligation applies to
  which actor at a glance; a crop/table must keep the provider/deployer
  distinction and must not drop the "unless obvious" and "law enforcement"
  exemptions, which change what the rule actually requires.
- **EO 14409 timeline**: a simple timeline (June 2 signing → August 1
  deadline → no deliverable as of July 31/August 1) would show the gap
  visually. Source: dates as established in Item 3's primary and secondary
  entries above. Must retain the exact signing date and the exact 60-day
  language; must not imply a specific hour-of-day beyond "00:00Z" since
  that's what triggered the "lapsed" framing in the one secondary read.
- **OpenAI report benchmark figures**: the four speedup figures (RustQC 60x,
  FastQC-Rust 7x, Trim Galore 3x, HI.SIM 31%) could carry as a small bar
  comparison, but see the Numbers-table caveat on the 99.8% aligner-parity
  figure and the unread primary — a chart should stick to the numbers
  sourced from directly-read secondaries only, and must carry a caption
  noting these are OpenAI's own case-study results, not independently
  reproduced.
- **DeepSeek-V4-Flash-0731**: None found beyond a possible params/pricing
  comparison table against V4-Pro-Preview, which none of my directly-read
  sources provided as a complete side-by-side; do not fabricate one.

---

## Discarded

- **Google DeepMind disbands the AlphaFold team** (Engadget, 2026-07-30;
  The Decoder, 2026-07-29; both read directly) — genuinely interesting but
  all available reporting traces to one Financial Times origin story I could
  not read myself (paywalled, not fetched); Engadget and The Decoder are two
  retellings of one origin and do not count as independent confirmation of
  each other. No independent DeepMind blog post or filing exists as a clean
  primary beyond a brief spokesperson quote relayed through the press.
  Rejected for this dateline: sourcing too thin to clear "1 primary + 1
  independent secondary" honestly, and the underlying event is 3-4 days
  stale relative to 2026-08-02 with no fresher development found.
- **IPMI/BMC password-hash exposure (24,650 servers)** (search snippets from
  The Hacker News, BleepingComputer, Help Net Security, dated 2026-07-28/29)
  — real, credible security research (Lava security researchers), but the
  underlying flaw is CVE-2013-4786, a 2013-vintage bug being re-surveyed,
  not a new vulnerability; the commission specifically cautions against
  another "crypto weakness/RCE" item absent something materially new, and
  the story is 4-5 days stale for 2026-08-02 with no AI/tech-field news hook
  beyond "affects some GPU-provider infrastructure." Not deeply fetched
  beyond search snippets — reject rather than force.
- **OpenAI/Anthropic joint letter on slowing self-improving AI** (~2026-07-29,
  via search snippets referencing techtimes.com coverage) — not independently
  fetched; appears adjacent to the EO 14409 story but is a separate event
  (an industry public letter, not a government deadline) and risks
  duplicating or diluting Item 3. Left out of the slate; the writer could
  fold a single sourced sentence into Item 3 only if they independently
  verify it, which I did not do.
- **Meta business-agent metered pricing (effective 2026-08-01)** (Unite.AI,
  Medianama, TechCrunch search snippets) — real product/business-model
  change, but reads as an incremental monetization change to an existing
  WhatsApp/Messenger product, not a technology development with the
  significance this brief's floor requires; also PR-adjacent (Meta's own Q2
  earnings framing). Not fetched directly. Rejected as promotional/
  incremental per commission guidance.
- **BYD humanoid robot debut** (South China Morning Post, CnEVPost, search
  snippets, 2026-07-27/28/31) — as of the dateline this is still a forward
  announcement ("will debut in August," "in the coming weeks"), not a
  completed 2026-08-01/02 event. No product has actually been shown yet.
  Rejected as not-yet-happened.
- **Latigo Biotherapeutics LTG-001 (Nav1.8 non-opioid pain drug), NEJM,
  2026-07-30** (search snippets, Managed Healthcare Executive, BusinessWire)
  — Phase 2b only, single cosmetic-surgery indication (abdominoplasty), and
  the coverage traces to the company's own BusinessWire announcement of its
  own trial — promotional pattern the commission's floor excludes on its
  own. Not fetched directly. Rejected.
- **Iptacopan / APPLAUSE-IgAN final results** (search snippets) — the actual
  NEJM publication date resolved to 2026-03-29, not late July/August;
  stale for this dateline once checked. Rejected.
- **DeepSeek developing its own inference chip** (Bloomberg/Reuters via
  search snippet, dated to a 2026-07-07 Bloomberg republish) — stale,
  reporting on a months-old Reuters story. Rejected.
- **CVE-2026-55040 (Microsoft SharePoint auth-bypass chain)** — the
  second vulnerability completing the RCE chain was reported as expected at
  "Patch Tuesday, August 2026," which falls on the second Tuesday of the
  month (2026-08-11), not yet occurred as of this brief's dateline.
  Rejected as not-yet-happened.
- **General AI-model-release scans** (Claude Opus 5, 2026-07-24; GPT-5.6
  Luna/Terra, 2026-07-09; Kimi K3, 2026-07-16) — all confirmed stale
  relative to 2026-08-02 and/or already covered in prior tech-news
  editions per the commission's own list. Not pursued further.
