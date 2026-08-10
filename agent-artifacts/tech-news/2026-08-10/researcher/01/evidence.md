# Evidence record: tech-news/2026-08-10 (researcher 01)

## What this record supports, and where it is thin

The verifiable story of this window is governance, not a model or a device. Two
separate AI-transparency regimes switched on together on **2 August 2026**: the
European Union's AI Act Article 50 and California's AI Transparency Act. Both are
backed by primary text I read (the European Commission's own transparency
guidelines and the regulation; California's chaptered bill on the legislature's
site). Both carry a real, checkable tension: the marking-and-detection obligation
for AI-generated content is legally in force while the technical standard for
*how* to mark is not finalized. That pairing — an obligation live, its standard
still pending — is the firmest and freshest thing on the board.

Two of the commission's flagged candidates do **not** survive primary
verification for this window, and the writer must not lead on either:

- **The "new FDA class of autonomous diagnostic AI" candidate is unsupported.**
  No FDA authorization from August 2026 creates a class of AI that makes a
  diagnostic call without a physician. The only 2026 De Novo I could find from
  the vicinity is Syncron-E (a ventilator-waveform tool that *assists*
  respiratory therapists, July 2026), and the only true autonomous-diagnosis
  authorization on record remains IDx-DR from **2018**. Details in Contradictions
  and Discarded.
- **The "new frontier model with agentic-reasoning claims" candidate is out of
  window or unverifiable.** The last frontier release with a genuine vendor
  system card, GPT-5.6 (Sol/Terra/Luna), shipped **9 July 2026** — a month early.
  The August open-weight releases circulating (Qwen 3.8-Max, Seedance 2.5, Muse
  Spark 1.2) have **no openable vendor primary**; the Qwen vendor blog 404s and
  the rest trace only to aggregators. I could not verify a benchmark or its
  omitted independent number against a primary, because no primary resolves.

Two further items have real primaries but are marginal: the NVIDIA/NAVER/Brookfield
Korea AI-factory expansion (firm primary, but dated 24 July, roughly two weeks
stale) and U.S. Executive Order 14409's 1 August frontier-model benchmarking
deadline (consequential, but the primary is fetch-gated and the deliverable is
classified, so I could not confirm firsthand that anything happened on the date).

Net: the brief has **two firm items** (EU Article 50; California AI Transparency
Act), both dated 2 August, plus **two marginal-but-sourced items** (Korea AI
factory; EO 14409). This is a thin day for genuinely new, high-consequence,
primary-verifiable developments, and the honest lead is the transparency shift.

---

## Sources — grouped by item

### Item 1 (firm): EU AI Act Article 50 transparency obligations enter application, 2 August 2026

```text
URL:         https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
Kind:        primary — the European Commission (the regulator) publishing its own
             official guidelines interpreting Article 50. Authorship and stake sit
             with the body that enforces the rule.
Establishes: The Commission published transparency guidelines on 20 July 2026,
             stating the Article 50 obligations "commence on 2 August 2026" and
             directing providers/deployers to comply "in a consistent, effective,
             proportionate and uniform manner." Points to a separate Guidelines on
             Transparency of AI-Generated Content, an Article 50 Q&A, and a
             voluntary Code of Practice on marking AI-generated content.
Paraphrase:  The Commission issued its Article 50 guidance twelve days before the
             obligations applied, and paired it with a voluntary Code of Practice
             rather than a finalized technical marking standard.
Locators:    Library page, "Guidelines on transparency obligations…"; publication
             date 20 July 2026.
Quote:       "ensure compliance with the transparency obligations under Article 50
             of the AI Act in a consistent, effective, proportionate and uniform
             manner."
```

```text
URL:         https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
Kind:        primary — the regulation's own consolidated text, Regulation (EU)
             2024/1689 (the AI Act), owner of Article 50.
Establishes: Article 50 is the transparency provision. Recorded here as the
             regulation's home page. NOTE: this URL renders via JavaScript and
             returns only a shell to an automated fetch; it resolves normally in a
             browser. The substantive Article 50 text below was read from the
             Commission guidelines above and the readable mirror immediately below.
Paraphrase:  Article 50 of Regulation (EU) 2024/1689 sets the transparency duties
             that apply from 2 August 2026.
Locators:    CELEX 32024R1689, Article 50.
Quote:       (text read via the two sources adjacent, not this shell)
```

```text
URL:         https://artificialintelligenceact.eu/transparency-rules-article-50/
Kind:        secondary — a readable compilation of the Article 50 text and recitals
             (the Future of Life Institute's AI Act explorer). Used to read the
             operative wording; not the owner of the rule.
Establishes: The four obligations in force from 2 August 2026:
             (a) providers must design interactive systems so "users are informed
             they are interacting with an AI," except where "obvious … to a natural
             person who is reasonably well-informed, observant and circumspect";
             (b) providers of generative systems must ensure outputs are "marked in
             a machine-readable format and detectable as AI-generated" (text, audio,
             image, video), with "technical standards … still under development
             through the Code of Practice";
             (c) deployers must inform people subject to emotion-recognition or
             biometric-categorization systems;
             (d) deployers must label deepfakes, with carve-outs for "clearly
             fantastical" and artistic/satirical works, and must disclose
             AI-generated public-interest text unless it had "human review or
             editorial control."
Paraphrase:  The marking obligation is legally live while its technical standard is
             not finalized — the Code of Practice is the interim pathway.
Locators:    "Provider Obligations" and "Deployer Obligations" sections; effective
             date box.
Quote:       "marked in a machine-readable format and detectable as AI-generated";
             "practical implementation details are still being finalised ahead of
             August 2026."
```

```text
URL:         https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026
Kind:        secondary — independent legal analysis (Cooley LLP), dated 3 August
             2026, the day after the rules took effect. Reports on the rule from
             outside the regulator.
Establishes: Confirms the four Article 50 scenarios and the transitional deadline:
             providers of generative systems "already on the market" have "until 2
             December 2026" for the marking/detection obligation; all other
             obligations applied immediately on 2 August 2026. Notes the Commission
             published a voluntary Code of Practice as a compliance pathway. Does
             not itself flag a Commission failure, but corroborates the unfinalized
             standard.
Paraphrase:  An independent firm's day-after read matches the Commission's own
             dates and confirms the 2 December 2026 grace period for pre-existing
             generative systems.
Locators:    "The Four Scenarios"; "Transitional Deadline"; publication date 3 Aug
             2026.
Quote:       "Providers have until 2 December 2026 to comply."
```

Independent penalty figure (from the search-surfaced firm analyses, consistent
across Cooley/Sidley coverage): non-compliance can trigger fines up to **€15
million or 3% of worldwide annual turnover**, whichever is higher. Owner of the
penalty is the AI Act itself (Article 99); treat as context, not a verified
primary reading, until the writer confirms against the regulation's Article 99.

### Item 2 (firm): California AI Transparency Act (SB 942, amended by AB 853) becomes operative, 2 August 2026

```text
URL:         https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853
Kind:        primary — the enrolled/chaptered text of AB 853 on the California
             Legislature's own site. Read directly.
Establishes: AB 853 amends Business and Professions Code §§ 22757.1, 22757.4,
             22757.6 and adds §§ 22757.3.1, 22757.3.2, 22757.3.3. "Approved by
             Governor October 13, 2025; filed with Secretary of State October 13,
             2025." Principal operative clause: "This chapter shall become operative
             on August 2, 2026." Added obligations phase in later: platform
             provenance detection operative 1 January 2027 (§§ 22757.3.1–.3.2),
             capture-device disclosure operative 1 January 2028 (§ 22757.3.3).
Paraphrase:  AB 853 moved the Act's operative date to 2 August 2026 (from the
             original 1 January 2026) and layered on later platform and
             capture-device duties.
Locators:    Bill text, amending clause and operative-date section; approval line.
Quote:       "This chapter shall become operative on August 2, 2026."
```

```text
URL:         https://calmatters.digitaldemocracy.org/bills/ca_202520260ab853
Kind:        secondary — CalMatters Digital Democracy bill tracker; quotes the bill
             and summarizes scope. Independent of the legislature.
Establishes: Covered providers are creators of a generative AI system with "over
             1,000,000 monthly visitors or users and … publicly accessible within"
             California. Duties: maintain a free AI-detection tool; offer a manifest
             (visible) disclosure option for AI-generated/altered image, video, or
             audio; and apply latent (embedded) provenance disclosures that are
             "permanent or extraordinarily difficult to remove, to the extent it is
             technically feasible." AB 853 adds AI-hosting-platform and
             capture-device obligations. Chaptered 13 Oct 2025 (Ch. 674, Stats.
             2025). SB 942 originally signed 19 Sept 2024.
Paraphrase:  California's rule targets the largest consumer generative-AI providers
             and pairs a public detection tool with visible-plus-embedded content
             labeling — a narrower, provider-focused cousin of EU Article 50.
Locators:    "Impact on SB 942"; "Key Disclosure Requirements & Thresholds";
             signing/chaptered dates.
Quote:       "over 1,000,000 monthly visitors or users and is publicly accessible
             within"; "permanent or extraordinarily difficult to remove, to the
             extent it is technically feasible."
```

```text
URL:         https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942
Kind:        primary — SB 942, the original Act (adds Ch. 25 to Div. 8 of the
             Business and Professions Code). Recorded as the parent statute's home;
             page resolves (JS-rendered).
Establishes: The original California AI Transparency Act, approved by the Governor
             19 September 2024, later amended and delayed by AB 853.
Paraphrase:  SB 942 is the base statute; AB 853 is the operative amendment.
Locators:    Bill nav page, SB 942 (2023–2024 session).
Quote:       —
```

The delay to 2 August was explicitly to line up with the EU: the amendment moved
the operative date "from January 1, 2026, to August 2, 2026, a move intended to
align with the implementation timeline of the European Union's AI Act" (firm
analyses; treat as reported context, corroborated by the shared date).

### Item 3 (marginal — firm primary, stale by ~2 weeks): NAVER, NVIDIA and Brookfield expand Korea's national AI-factory buildout

```text
URL:         https://nvidianews.nvidia.com/news/naver-nvidia-and-brookfield-to-expand-koreas-national-ai-factory-infrastructure-buildout
Kind:        primary — NVIDIA's own newsroom release, read directly. Dated 24 July
             2026.
Establishes: The parties propose to grow the NVIDIA DSX AI-factory deployment at
             the GAK Sejong data center from 55 MW to 200 MW by 2028, with NAVER's
             stated long-term target of 1 gigawatt. NVIDIA plans a $1 billion
             investment into NAVER Corp; Brookfield signed a nonbinding term sheet
             for up to $9 billion in project financing; NAVER funds the remainder.
             A Korea AI-agent platform launch is slated for H2 2026. Named:
             Haejin Lee, "founder and chairman of NAVER"; Jensen Huang, "founder and
             CEO of NVIDIA"; Sikander Rashid, "global head of AI infrastructure at
             Brookfield."
Paraphrase:  A sovereign-AI infrastructure deal that more than triples an announced
             buildout and gives a U.S. chipmaker an equity position in a Korean
             internet company — but it is two-plus weeks old relative to 10 August.
Locators:    Release body; MW, dollar, and timeline figures; executive quotes.
Quote:       "expand the initial NVIDIA DSX AI factory buildout … from 55 megawatts
             to 200 megawatts by 2028."
```

```text
URL:         https://www.upi.com/Top_News/World-News/2026/07/27/nvidia-naver-ai-factories/7831785195985/
Kind:        secondary — UPI wire report (27 July 2026), independent of the parties.
Establishes: Adds the figure the NVIDIA release omits: the proposed $1 billion buys
             NVIDIA "a stake of about 4.5%, making it Naver's third-largest
             shareholder," and the investment is conditioned on NAVER "securing at
             least $9 billion in committed project financing separate from Nvidia's
             investment."
Paraphrase:  Independent reporting supplies the equity-stake percentage and the
             financing condition the vendor release leaves out.
Locators:    Lede and financing paragraphs.
Quote:       "a stake of about 4.5%, making it Naver's third-largest shareholder."
```

### Item 4 (marginal — primary fetch-gated, deliverable unverifiable): U.S. EO 14409 frontier-model cyber-benchmarking deadline, 1 August 2026

```text
URL:         https://www.federalregister.gov/documents/2026/06/05/2026-11415/promoting-advanced-artificial-intelligence-innovation-and-security
Kind:        primary — the Federal Register publication of Executive Order 14409,
             "Promoting Advanced Artificial Intelligence Innovation and Security."
             NOTE: fetch-gated — the URL 302-redirects an automated request to a
             challenge page (unblock.federalregister.gov); it resolves in a browser.
             I could NOT read the primary firsthand. Details below come from the
             three independent secondary accounts that cite this document.
Establishes: EO 14409, signed 2 June 2026, published 5 June 2026. Within 60 days
             (i.e. by 1 August 2026), Treasury, NSA, and CISA — with the National
             Cyber Director, OSTP, and NIST — must develop a classified benchmarking
             process to designate "covered frontier models" by cyber capability, and
             the order sets a voluntary 30-day pre-release review window for
             developers before models reach trusted partners.
Paraphrase:  A U.S. federal deadline for defining which frontier models count as
             cyber-relevant fell on 1 August, but the deliverable is classified and
             cannot be confirmed to have occurred.
Locators:    FR doc 2026-11415; EO 14409; §§ on covered frontier models and
             benchmarking (per secondary summaries).
Quote:       (primary not read; see caveat)
```

```text
URL:         https://www.congress.gov/crs-product/IF13268
Kind:        secondary — Congressional Research Service explainer of EO 14409
             ("Controlling Advanced Artificial Intelligence"). Authoritative but not
             the order itself. NOTE: returned HTTP 403 to automated fetch; resolves
             in a browser. Details taken from the search-surfaced summary.
Establishes: Corroborates the 60-day / 1 August 2026 classified-benchmarking
             deadline and the voluntary early-access review, and that the order
             directs agencies to harden federal infrastructure against AI-enabled
             cyber risk.
Paraphrase:  A congressional-research summary independently describes the same
             deadline and mechanism.
Locators:    IF13268, "Key Deadlines" discussion.
Quote:       —
```

```text
URL:         https://www.nortonrosefulbright.com/en/knowledge/publications/900af3cf/executive-order-establishes-voluntary-early-access-framework-to-frontier-ai-models
Kind:        secondary — law-firm analysis, independent, describing the voluntary
             early-access framework in EO 14409. Read via search summary only.
Establishes: Confirms the voluntary pre-release government review window for
             frontier AI models under the order.
Paraphrase:  A third independent account of the same order and mechanism.
Locators:    Publication body.
Quote:       —
```

---

## Contradictions

- **The FDA "autonomous diagnostic AI" candidate does not exist for this window.**
  The commission calls it a strong candidate. It is not supported by any primary I
  could find. Searches of fda.gov, the Federal Register, and general coverage
  return: (a) IDx-DR, the first and still-cited autonomous AI diagnostic, De Novo
  authorized in **2018**; (b) a July 2026 De Novo for Syncron-E by a firm named
  "Autonomous Healthcare" — but that is ventilator-waveform analysis software that
  *supports* respiratory therapists, explicitly assistive, not an autonomous
  diagnostic call without a physician; and (c) an FDA press item that on inspection
  is dated **6 May 2026** and concerns the FDA's *internal* AI tool (Elsa 4.0), not
  any device authorization. Multiple 2026 sources state plainly that no authorized
  generative AI devices and no autonomous AI prescription services have been
  cleared. The candidate as briefed should be dropped, not reported.

- **The "new frontier model" candidate is out of window or has no primary.** The
  most recent frontier release with a genuine, openable vendor system card is
  GPT-5.6 (Sol/Terra/Luna) on deploymentsafety.openai.com, dated **9 July 2026** —
  not this window. The August open-weight candidates (Qwen 3.8-Max "week of 10
  August," Seedance 2.5, Muse Spark 1.2) resolve only to aggregator pages; the
  Qwen vendor blog URL 404s. Because no vendor primary resolves, I could not verify
  any benchmark claim or supply the omitted independent number the commission asks
  for. Do not present an August model release as verified.

- **EU Article 50: obligation live, standard pending.** The machine-readable
  marking-and-detection duty for AI-generated content is legally in force from 2
  August 2026, yet the technical standard for how to mark is not finalized — the
  Commission offers a *voluntary* Code of Practice, and pre-existing generative
  systems get until 2 December 2026. Regulator (Commission guidelines) and
  independent analysis (Cooley) agree on the dates; neither claims the standard is
  settled. This is a real tension in the primary record, not a divergence between
  accounts.

- **NVIDIA/NAVER: equity stake omitted by the vendor.** NVIDIA's own release states
  the $1 billion investment but not the resulting stake. UPI supplies it: "about
  4.5%," making NVIDIA NAVER's third-largest shareholder, plus the $9 billion
  financing condition. Vendor account is silent where the independent account is
  specific.

- **Date drift in secondary reporting on the Korea deal.** UPI dates the story 27
  July; the NVIDIA primary carries 24 July. Use the primary's date (24 July).

---

## Numbers

```text
Figure: 2 August 2026 — operative date, EU AI Act Article 50 transparency duties
Owner:  Regulation (EU) 2024/1689, Art. 50 / European Commission guidelines
Scope:  Applies to in-scope systems regardless of when placed on market; marking
        obligation for pre-existing generative systems deferred to 2 Dec 2026.
```

```text
Figure: 2 August 2026 — operative date, California AI Transparency Act
Owner:  Cal. Bus. & Prof. Code Ch. 25, Div. 8 (SB 942 as amended by AB 853)
Scope:  Covered providers = generative-AI systems with >1,000,000 monthly
        visitors/users, publicly accessible in California. Platform duties from
        1 Jan 2027; capture-device duties from 1 Jan 2028.
```

```text
Figure: up to €15,000,000 or 3% of worldwide annual turnover — max Art. 50-adjacent penalty
Owner:  EU AI Act (Article 99 penalty tiers), reported via legal analyses
Scope:  Whichever is higher; treat as context pending a primary reading of Art. 99.
```

```text
Figure: US $5,000 per violation — California civil penalty
Owner:  California AI Transparency Act (per reported analyses of the statute)
Scope:  Each day treated as a discrete violation; confirm against Cal. B&P Code.
```

```text
Figure: 55 MW -> 200 MW by 2028; 1 GW long-term target
Owner:  NVIDIA newsroom release, 24 July 2026 (GAK Sejong / DSX AI factory)
Scope:  Proposed expansion of a single Korean national AI-factory deployment.
```

```text
Figure: US $1,000,000,000 NVIDIA investment in NAVER; ~4.5% stake; up to US $9B Brookfield financing
Owner:  $1B and $9B from NVIDIA release; 4.5% stake from UPI (vendor omits it)
Scope:  Investment conditioned on NAVER securing >=$9B committed project financing.
```

```text
Figure: 1 August 2026 (60 days from 2 June signing) — EO 14409 benchmarking deadline
Owner:  Executive Order 14409 (Fed. Reg. doc 2026-11415), via CRS IF13268
Scope:  Deadline for Treasury/NSA/CISA to build a classified process designating
        "covered frontier models"; deliverable classified and unverified.
```

Reference only (NOT for use — no primary resolved): GPT-5.6 system card (9 July
2026, deploymentsafety.openai.com) reports GPT-5.6 Sol "makes slightly fewer
factual errors than GPT-5.5" and GPT-Red prompt-injection scores of 1.000
(connectors) and 0.910 (search/function-calling) for Sol. Out of window; listed
so the writer does not mistake an August model claim for this.

---

## Source assets

```text
Asset: European Commission timeline graphic of AI Act application dates
       (on digital-strategy.ec.europa.eu factpages / quick-facts pages)
Shows: How 2 August 2026 sits in the Act's staged rollout (2024 entry into force,
       Feb 2025 prohibitions, Aug 2025 GPAI, Aug 2026 transparency + high-risk).
Crop:  Must retain the 2 August 2026 marker and the label distinguishing the
       marking-obligation grace period to 2 December 2026; omit unrelated 2027 rows
       only if the caption states the timeline continues.
```

```text
Asset: Side-by-side of the two transparency regimes (EU Art. 50 vs California Act)
       — constructed from the primaries, not lifted from a source.
Shows: The overlap and the gap: EU covers chatbots, emotion recognition, deepfakes,
       and synthetic-content marking for all providers; California targets only
       >1M-user generative providers with a detection tool plus manifest/latent
       labels. Same date, different scope.
Crop:  A table (nb-table) is the honest form here; keep thresholds and effective
       dates, drop marketing gloss.
```

```text
Asset: NVIDIA release figure of the GAK Sejong DSX AI-factory buildout
Shows: The 55 MW -> 200 MW -> 1 GW scale of the proposed expansion.
Crop:  Retain the megawatt figures and the 2028 date; this is a comparison of
       magnitudes, so a small nb-table beats the vendor's prose.
```

No decorative imagery. Where numbers carry an item (transparency thresholds; the
Korea megawatts), a table is the right furniture; elsewhere prose suffices.

---

## Discarded

```text
URL: https://www.fda.gov/news-events/press-announcements/fda-expands-ai-capabilities-and-completes-data-platform-consolidation
     — dated 6 May 2026 and about FDA's internal tool Elsa 4.0, not a device
     authorization. Does not support the autonomous-diagnostic-AI candidate.
```

```text
URL: https://www.prnewswire.com/news-releases/autonomous-healthcare-receives-fda-de-novo-marketing-authorization-for-syncron-e-...-302823832.html
     — real July 2026 De Novo, but Syncron-E is assistive ventilator-waveform
     software supporting respiratory therapists, not an autonomous diagnostic
     system operating without a physician. Wrong shape for the candidate.
```

```text
URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6550188/
     — the IDx-DR pivotal trial; the real autonomous-diagnosis milestone, but from
     2018. Historical context only; not a 2026 development.
```

```text
URL: https://qwenlm.github.io/blog/qwen3.8-max/
     — HTTP 404. No vendor primary for "Qwen 3.8-Max." The release is attested only
     by aggregators (yottalabs, developersdigest, ofox, warp2search). Unverifiable;
     cannot supply the omitted benchmark number the commission requires.
```

```text
URL: https://deploymentsafety.openai.com/gpt-5-6
     — genuine OpenAI system card, but GPT-5.6 shipped 9 July 2026, outside the
     window. Kept in Numbers as a reference so no August model claim borrows it.
```

```text
URL: https://www.hedra.com/models/video/bytedance/seedance-25 (and related)
     — Seedance 2.5 API opened ~7 August 2026 per aggregators, but no openable
     ByteDance/Volcano Engine primary resolved. Cannot verify; a video-model
     product launch is also weak on consequence for this brief.
```

```text
URL: https://www.nature.com/articles/s41591-025-03832-2
     — rentosertib (AI-designed drug, idiopathic pulmonary fibrosis) Phase 2a. Real
     and consequential, but a 2025 Nature Medicine result, not an 8-10 Aug 2026
     development.
```

```text
URL: https://etcjournal.com/2026/08/01/... ; aireleasetracker.com ; jobsecuritymeter.com ;
     benchlm.ai ; digitalapplied.com ; promptzone.com
     — aggregators/leaderboards with no primary authorship over any claim; used
     only to locate candidates, cited for nothing.
```
</content>
</invoke>
