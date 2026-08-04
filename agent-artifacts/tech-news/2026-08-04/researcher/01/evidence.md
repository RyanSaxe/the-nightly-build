# Evidence: tech-news/2026-08-04 (researcher 01)

This record assembles **7 candidate items** for the daily brief; the writer selects
and orders the final 4-6. The evidence is strongest for the lead: OpenAI's "Astra"
math result carries a genuine, machine-checkable primary (a public GitHub repo of
Lean 4 proofs plus a manuscript), corroborated by multiple independent outlets. The
non-AI variety pick (the Feinstein human vagus-nerve atlas) is well-figured against
its owning release and a released dataset. Two candidates are deliberately flagged as
weaker: the Cisco FMC zero-day is a ~5-day-old running security story whose figures
are easy to conflate (the *exploited* CVE is not the CVSS-10 one), and the
Google/Anthropic "$200bn finance machine" is Financial Times reporting whose central
figure no single company primary owns and whose news is a market/policy consequence
(current-events overlap). The record is thin where the simulated news field did not
surface fresh, non-AI, on-date primaries: most materials/quantum/fusion/health results
it returned are dated June–July 2026 and are recorded under Discarded with reasons.

Verification honesty: I opened firsthand the GitHub repo (Astra), the Feinstein
release (via an accessible wire mirror), the Tenable/NVD CVE page (Cisco), and the
Epoch AI data page. Several owning primaries returned **HTTP 403** to the fetch tool
(openai.com index pages, science.org, feinstein.northwell.edu). A 403 is *gated, not
dead*; I record each source's own page as the URL and note where I relied on
independent accounts rather than a firsthand read. The writer/editor must open the
gated primaries before publication.

---

## Sources

### Candidate 1 (LEAD) — OpenAI "Astra" solves ten open problems in math and TCS, with machine-checkable Lean proofs

```text
URL:         https://openai.com/index/ten-advances-in-mathematics/
Kind:        primary (owning announcement). OpenAI authored and staked the claim.
             NOTE: returned HTTP 403 to the fetch tool (gated). Contents below are
             corroborated by the GitHub primary and multiple secondaries, not by a
             firsthand read of this page.
Establishes: OpenAI states an internal version of its next model, "Astra," produced
             proofs of ten previously open problems in mathematics and theoretical
             computer science, announced 2026-08-01, with formal Lean proofs released
             publicly.
Paraphrase:  Ten results, each formalized in Lean 4; token cost to generate all ten
             stated at ~$2,000 at OpenAI's "Sol" API rates.
Locators:    Index page + linked manuscript (below).
```

```text
URL:         https://github.com/openai/ten-proofs
Kind:        primary (the machine-checkable artifact). Opened firsthand.
Establishes: A public repo ("Lean certificates accompanying proofs in mathematics and
             theoretical computer science") with 10 Lean 4 files, one per result:
             SpherePacking.lean, MetricCodes.lean, NonSoficGroup.lean,
             ConnesRigidity.lean, Permanent.lean, QuantumParallelRepetition.lean,
             GapCVP.lean, EhrhartVolumeInequality.lean, MulticolorTriangleRamsey.lean,
             CompactnessAndDegeneracy.lean. License Apache-2.0. README: "This
             repository contains Lean 4 formalizations of the results presented in Ten
             advances in mathematics and theoretical computer science by OpenAI."
             Links a main paper (cdn.openai.com/pdf/ten-proofs-oai.pdf) and reasoning
             walkthroughs (cdn.openai.com/pdf/reasoning-walkthroughs.pdf). References
             independent proof-checking via a "Comparator" challenge.
Paraphrase:  Each of the ten claimed results has a corresponding Lean 4 file intended
             to be independently machine-verified.
Locators:    Repo root README + file list; "1 Commit" on main at time of read.
Quote:       "This repository contains Lean 4 formalizations of the results presented
             in Ten advances in mathematics and theoretical computer science by OpenAI."
```

```text
URL:         https://thenextweb.com/news/openai-astra-model-ten-math-proofs-non-sofic-groups
Kind:        secondary (independent account).
Establishes: Independent framing of the announcement; names specific results incl. a
             construction establishing non-sofic groups exist.
Paraphrase:  Confirms the "ten open problems" claim and the non-sofic-groups result as
             a headline example; frames Astra as OpenAI's next model, introduced via
             mathematical discovery rather than benchmarks.
Locators:    Article body.
```

```text
URL:         https://www.techtimes.com/articles/322710/20260802/openais-astra-solves-ten-decade-old-math-problems-machine-checkable-lean-proofs.htm
Kind:        secondary (independent account, 2026-08-02).
Establishes: Lists results: a claimed counterexample to Connes's rigidity conjecture;
             non-sofic groups exist; improved asymptotic upper bounds for
             high-dimensional sphere packing down to the Cohn-Elkies threshold;
             stronger bounds for binary and spherical codes; an n^4/log n formula lower
             bound for the permanent; a superexponential lower bound for multicolor
             Ramsey numbers resolving Erdos problem 183. States 249-page manuscript,
             Apache-2.0 Lean 4 certificates on GitHub, and reports "sorry" count of zero.
Paraphrase:  Each named result maps to a Lean file in the primary repo (e.g.
             ConnesRigidity, NonSoficGroup, SpherePacking, MetricCodes, Permanent,
             MulticolorTriangleRamsey), which cross-corroborates the manuscript claims.
Locators:    Article body.
```

```text
URL:         https://www.forbes.com/sites/jonmarkman/2026/08/03/openais-astra-solved-10-decades-old-math-problems-for-just-2000/
Kind:        secondary (independent account, 2026-08-03).
Establishes: Independent confirmation of the ~$2,000 compute-cost figure and the
             "next model" framing on 2026-08-03, showing the story was live in the
             Aug-4 window.
Paraphrase:  Repeats the cost and capability claims; adds market/industry framing.
Locators:    Article body.
```

### Candidate 2 — OpenAI + academic partners field report: coding agents modernize scientific software (AI-for-science tooling)

```text
URL:         https://openai.com/index/scientific-computing-agentic-ai/
Kind:        primary (owning field report). NOTE: returned HTTP 403 to the fetch tool
             (gated); contents below rest on OpenAI's own X post and independent
             accounts, not a firsthand read of this page.
Establishes: OpenAI field report, "Scientific computing in the age of agentic AI,"
             documenting eight case studies (mostly life sciences) where research
             groups used coding agents (Codex; some with Claude Code) to modernize and
             optimize research software. Published ~2026-07-27/29.
Paraphrase:  Agents took on maintenance, targeted optimization, language migrations,
             and GPU-native redesigns; humans still had to define the scientific
             question and verify correctness.
Locators:    Report body / case studies.
```

```text
URL:         https://x.com/OpenAI/status/2082152074071228702
Kind:        primary (OpenAI's own announcement post). Owner statement.
Establishes: OpenAI's framing: "Coding agents are helping scientists spend more
             time advancing research ... While agents can reliably execute on ambitious
             projects, researchers must still define the scientific questions, verify
             results, and take a stance on long-term ownership."
Paraphrase:  States both the acceleration claim and the human-verification caveat.
Locators:    Post text.
```

```text
URL:         https://the-decoder.com/ai-coding-agents-can-modernize-research-software-but-cant-judge-if-the-science-is-right/
Kind:        secondary (independent account).
Establishes: Independent read of the report's central caveat: agents are "eloquent,
             convincing, and confidently wrong in ways that are easy to miss"; every
             win rested on a human deciding what "correct" means.
Paraphrase:  Confirms the report's two-sided finding (speedups plus a verification
             blind spot).
Locators:    Article body.
```

```text
URL:         https://www.techtimes.com/articles/321880/20260728/ai-agents-rewrote-20000-lines-dead-genomics-code-scientists-still-checked-every-result.htm
Kind:        secondary (independent account, 2026-07-28).
Establishes: Concrete figures: a 60x speedup in RNA-sequencing quality control; a
             from-scratch Rust rewrite of a ~20,000-line C/C++ genome aligner at 99.8%
             parity; a GPU-native redesign cutting synthetic genome generation from
             1,610 s to 27 s per run. Five projects used Codex alone, three used Codex
             + Claude Code.
Paraphrase:  Supplies the load-bearing numbers the primary page (gated) would own.
Locators:    Article body.
```

### Candidate 3 (non-AI variety) — Feinstein Institutes release the first comprehensive human vagus-nerve atlas (REVA) on NIH's SPARC

```text
URL:         https://www.biospace.com/press-releases/feinstein-institutes-unveils-worlds-first-comprehensive-vagus-nerve-map-substantiating-decades-of-leadership-in-bioelectronic-medicine
Kind:        primary content (verbatim wire copy of the owning Northwell/Feinstein
             press release). Opened firsthand. The original owner page
             (feinstein.northwell.edu/...) is 403-gated; this is the same release text.
Establishes: Northwell Health's Feinstein Institutes released (2026-07-27) the "world's
             first" comprehensive human vagus-nerve anatomical atlas from the
             Reconstructing Vagal Anatomy (REVA) project: more than 200,000 individual
             fibers per vagus nerve, across 60 vagus nerves from 30 human donors, built
             over 3 years on a $6.7M NIH grant (awarded Oct 2022), using microCT
             imaging, immunohistochemistry, and ultrasound. Dataset released freely on
             the NIH-supported SPARC platform (sparc.science).
Paraphrase:  Investigators: Stavros Zanos, MD PhD (Associate Professor, Institute of
             Bioelectronic Medicine, co-leader) and Kevin J. Tracey, MD (President and
             CEO, Feinstein Institutes). Clinical significance: knowing which fascicle
             carries which organ's signal could let vagus-nerve-stimulation devices
             target organs precisely and avoid side effects (hoarseness, disrupted
             sleep, cardiac risk).
Locators:    Release body.
Quote:       "more than 200,000 individual fibers" per vagus nerve; "60" nerves; "30"
             donors; project "Reconstructing Vagal Anatomy (REVA)"; "$6.7 million" NIH.
```

```text
URL:         https://www.science.org/content/article/major-highway-human-nervous-system-gets-complete-road-map
Kind:        secondary (independent account, Science/AAAS news, 2026-08-03). NOTE:
             403-gated to the fetch tool; headline and framing confirmed via search
             index. This 2026-08-03 writeup is what puts the atlas in the Aug-4 window.
Establishes: Independent science-press framing of the atlas as a "complete road map"
             of a major nervous-system "highway," pointing to more precise stimulation
             therapies.
Paraphrase:  Confirms timeliness (Aug 3) and clinical framing.
Locators:    Headline + dek.
```

```text
URL:         https://www.genengnews.com/topics/translational-medicine/comprehensive-human-vagus-nerve-map-unveiled/
Kind:        secondary (independent trade account).
Establishes: Independent confirmation of the 200,000-fibers / 60-nerves / 30-donors
             figures and the SPARC release.
Paraphrase:  Cross-checks the release's headline numbers.
Locators:    Article body.
```

### Candidate 4 (flag: current-events overlap) — Financial Times: Google's ~$200bn financing machine for Anthropic, built around TPUs

```text
URL:         https://www.anthropic.com/news/google-broadcom-partnership-compute
Kind:        primary (Anthropic's own announcement). Owner statement for the compute
             deal underlying the FT story. NOTE: not opened firsthand this session;
             recorded from search index — open before use.
Establishes: Anthropic's expanded partnership with Google and Broadcom for "multiple
             gigawatts" of next-generation compute; reporting puts it at ~3.5 GW of TPU
             capacity coming online from 2027; Alphabet investing a further $40bn ($10bn
             immediate, $30bn milestone-contingent) atop earlier stakes.
Paraphrase:  Owns the TPU/gigawatt/investment figures; does NOT itself own the "$200bn
             finance machine" framing.
Locators:    Announcement body.
```

```text
URL:         https://x.com/FT/status/2084494445752258882
Kind:        secondary but the news owner for the "$200bn" framing (FT investigative
             reporting, surfaced 2026-08-04). "Inside Google's $200bn Wall Street
             finance machine for Anthropic."
Establishes: FT reports interconnected contracts totalling ~$200bn to deploy >$150bn
             of AI chips for Anthropic, uniting Google, Broadcom, Apollo, Blackstone,
             Morgan Stanley and crypto-mining firms; based on people involved and
             corporate filings.
Paraphrase:  The $200bn / >$150bn figures are FT-owned reporting synthesized from
             filings and sources, not a single company disclosure. Full article behind
             ft.com paywall; framing confirmed via FT's own post and secondaries.
Locators:    FT post + linked article.
```

```text
URL:         https://www.cnbc.com/2026/04/06/broadcom-agrees-to-expanded-chip-deals-with-google-anthropic.html
Kind:        secondary (independent US newsroom, context).
Establishes: Prior reporting on Broadcom's expanded chip deals with Google and
             Anthropic; grounds the hardware side of the FT story.
Paraphrase:  Background on the Broadcom/TPU supply relationship.
Locators:    Article body.
```

### Candidate 5 (flag: trend/context, not a fresh event) — Epoch AI: leading AI-supercomputer performance doubling ~every 9 months

```text
URL:         https://epoch.ai/data-insights/ai-supercomputers-performance-trend
Kind:        primary (Epoch AI's own dataset/analysis). Opened firsthand.
Establishes: "The computational performance of the leading AI supercomputers has grown
             by 2.5x annually since 2019" (CI 2.4-2.7x), i.e. ~9-month doubling; driven
             by chips-per-cluster up 1.6x/yr and performance-per-chip up 1.6x/yr.
             Dataset: 728 AI supercomputers, 2010-Jan 2025; 57 "leading" systems; peak
             16-bit FLOP/s.
Paraphrase:  A data-insight, not a dated 2026-08 event. The Aug-2 news peg was NYT
             coverage citing Epoch projections; treat as context/furniture, not a
             standalone "moved today" item.
Locators:    Data-insight page.
Quote:       "The computational performance of the leading AI supercomputers has grown
             by 2.5x annually since 2019."
```

```text
URL:         https://epoch.ai/data-insights/ai-chip-production
Kind:        primary (Epoch AI). Related figure.
Establishes: Total AI compute doubling ~every 7 months (~3.3x/yr since 2022); Nvidia
             >60% of total compute; Google and Amazon much of the remainder.
Paraphrase:  A second, faster doubling series for total (not just leading) compute.
Locators:    Data-insight page. NOTE: recorded from search index; open before use.
```

### Candidate 6 (flag: ~5-day-old running story; figure-conflation risk) — Cisco FMC static-credential zero-day actively exploited (CVE-2026-20316)

```text
URL:         https://www.tenable.com/cve/CVE-2026-20316
Kind:        primary-adjacent record (NVD/CVSS data). Opened firsthand. The owning
             primary is Cisco's security advisory for CVE-2026-20316 (cisco.com) plus
             the CISA KEV catalog entry; open those before use.
Establishes: CVE-2026-20316: static-credential vulnerability in the Cisco Secure
             Firewall Management Center (FMC) web interface; unauthenticated remote
             attacker can log in with a low-privilege account. CVSS v3.1 base 5.3
             (AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N). Confirmed exploited in the wild;
             added to CISA KEV 2026-07-29. Description notes it "can be used with other
             Cisco Secure FMC Software vulnerabilities to elevate privileges."
Paraphrase:  Alone it only leaks data (5.3), but it chains with the CVSS-10 auth-bypass
             bugs to reach root. FCEB remediation deadline was 2026-08-01.
Locators:    CVE record.
```

```text
URL:         https://www.bleepingcomputer.com/news/security/cisco-warns-of-fmc-static-credential-flaw-exploited-in-zero-day-attacks/
Kind:        secondary (independent security newsroom, ~2026-07-30).
Establishes: Independent confirmation of active zero-day exploitation of the static-
             credential flaw and Cisco's release of hot fixes for FMC 7.0/7.2/7.4/7.6/
             7.7/10.0 with no workarounds.
Paraphrase:  Corroborates exploitation and the patch situation.
Locators:    Article body.
```

```text
URL:         https://www.vulncheck.com/blog/cisco-fmc-auth-bypass-cve-2026-20079
Kind:        secondary (independent technical analysis).
Establishes: The related CVSS-10.0 auth-bypass CVE-2026-20079 (paired with
             CVE-2026-20131), disclosed March 2026 via a startup process leaving a
             partial csm_processes session that can be upgraded to call CGI scripts and
             reach root. These CVSS-10 bugs were NOT confirmed exploited; the exploited
             one is 20316.
Paraphrase:  Establishes the exact relationship and prevents the common conflation.
Locators:    Blog body.
```

### Candidate 7 (flag: model release; low priority per boundaries) — Alibaba releases Qwen 3.8 Max (open weights)

```text
URL:         (primary not resolved — Qwen model card / qwenlm.github.io blog / Hugging
             Face repo; MUST be located before use)
Kind:        primary would be Alibaba/Qwen's release notes or model card. NOT resolved
             this session.
Establishes: Reported 2026-08-04 release of Qwen 3.8 Max, an open-weights model aimed
             at coding and collaborative use.
Paraphrase:  On-date but a straight model release; recent editions (2026-07-27..08-03)
             already leaned heavily on open-weight releases, so this is the weakest
             candidate and included only for completeness.
Locators:    n/a.
```

```text
URL:         https://llm-stats.com/ai-news
Kind:        secondary (aggregator; cites Latent Space as the account).
Establishes: Logs "Qwen 3.8 Max" release on 2026-08-04 (attributed to Latent Space).
Paraphrase:  Only a secondary sighting; primary still needed.
Locators:    Aug-4 feed entry.
```

---

## Contradictions

- **Cisco CVE conflation (important).** Several secondaries and one search summary
  blur two distinct bugs. The **actively exploited** flaw on CISA KEV (added
  2026-07-29) is **CVE-2026-20316**, a static-credential issue rated only **CVSS 5.3**.
  The **CVSS 10.0** flaws are **CVE-2026-20079** and **CVE-2026-20131**
  (auth-bypass, disclosed March 2026), which Cisco said were **not** confirmed
  exploited. The real story is the *chaining* of the low-score exploited bug into the
  high-score bugs for root. Any headline calling "the CVSS-10 Cisco bug" the one
  "under active exploitation" is wrong.
- **Astra "sorry count = 0".** This zero-unproven-steps claim appears in secondary
  coverage (TechTimes) and matches the manuscript's assertion, but the GitHub README I
  opened did not itself state a sorry count; it points to independent "Comparator"
  checking. Treat "fully verified, zero sorries" as a claim to confirm by running/reading
  the Lean files or the Comparator results, not as established from the repo landing page.
- **Astra + Gowers endorsement.** Coverage repeats that Fields Medalist Timothy Gowers
  said he would recommend "one of the model family's proofs" for Annals of Mathematics.
  The phrasing suggests this may refer to an *earlier* result from the same model line,
  not necessarily one of these ten. Do not attribute a blanket Gowers endorsement of all
  ten results without a firsthand source.
- **Vagus atlas is a dataset release, not a peer-reviewed paper.** The owning primary is
  a press release plus a released SPARC dataset; no journal paper is cited. The
  editorial standard's "open the paper" instruction has no paper to open here; the
  writer should cite the SPARC dataset and the Feinstein release and say plainly that it
  is a data release. Also note the figure is "200,000+ fibers **per** vagus nerve," not
  across all 60.
- **Google/Anthropic $200bn.** The $200bn / >$150bn figures are Financial Times
  reporting from filings and sources; no single company primary states them. Anthropic's
  own release owns only the compute/TPU/gigawatt and $40bn-investment figures.
- **Epoch is not a fresh event.** Its dataset runs only to January 2025; the "doubling"
  figures are standing analysis, surfaced in the Aug-2 news cycle via NYT. It is context,
  not a development that "moved" on Aug 4.

## Overlap flags

- **Non-overlap with current-events (same run).** Several strong Aug-4 items are
  public/policy/market-consequence stories and belong to **current-events, not
  tech-news**: the **Google/Anthropic "$200bn finance machine"** (Candidate 4 — included
  here only for its TPU/compute-technology angle; if current-events takes it, drop it
  here to keep the sets disjoint); **China's stated concern over US frontier-AI offensive
  cyber ("Mythos")**; the **Apple v. OpenAI trade-secret injunction**; **Trump Media's
  paid market-data API and the SEC-probe request**; and the **EU AI Act transparency
  obligations going live (~Aug 2)**. None of these are proposed as standalone tech-news
  candidates except Candidate 4, which is flagged.
- **Non-overlap with paper-of-the-day (2015 ResNet reconstruction).** No candidate here
  is a foundational-paper explainer; all are current developments. The Astra item is a
  new capability result, not a ResNet-style retrospective. No overlap.

## Numbers

```text
Figure: 10 open problems in mathematics/TCS, each with a Lean 4 file
Owner:  github.com/openai/ten-proofs (opened) + openai.com/index/ten-advances-in-mathematics (gated)
Scope:  Ten results claimed proved by an internal "Astra"; announced 2026-08-01.
```
```text
Figure: ~$2,000 compute cost to generate all ten solutions
Owner:  OpenAI (announcement); repeated by Forbes/Markman 2026-08-03, TechTimes
Scope:  Token cost at OpenAI "Sol" API rates; OpenAI's own figure.
```
```text
Figure: 249-page manuscript; Lean 4 certificates; Apache-2.0
Owner:  GitHub repo (opened) + manuscript cdn.openai.com/pdf/ten-proofs-oai.pdf
Scope:  "sorry" count reported as zero by TechTimes — confirm at source.
```
```text
Figure: 8 case studies; 5 used Codex only, 3 used Codex + Claude Code
Owner:  OpenAI "Scientific computing in the age of agentic AI" (gated) + TechTimes
Scope:  Mostly life-sciences research groups.
```
```text
Figure: 60x speedup (RNA-seq QC); ~20,000-line C/C++ aligner rewritten to Rust at 99.8% parity; synthetic-genome generation 1,610s -> 27s
Owner:  OpenAI field report (gated); figures via TechTimes 2026-07-28
Scope:  Individual project results, not a portfolio average.
```
```text
Figure: >200,000 nerve fibers per vagus nerve; 60 nerves; 30 human donors
Owner:  Feinstein Institutes/Northwell release (opened via BioSpace mirror)
Scope:  REVA project; $6.7M NIH grant (awarded Oct 2022); released 2026-07-27 on sparc.science.
```
```text
Figure: ~$200bn interconnected financing; >$150bn of AI chips for Anthropic; ~3.5 GW TPU capacity from 2027; +$40bn Alphabet investment ($10bn now, $30bn milestone-contingent)
Owner:  $200bn/>$150bn = Financial Times reporting; TPU/GW/$40bn = Anthropic release
Scope:  Multi-party contracts (Google, Broadcom, Apollo, Blackstone, Morgan Stanley, crypto miners); surfaced 2026-08-04.
```
```text
Figure: Leading AI-supercomputer performance 2.5x/yr since 2019 (~9-month doubling); chips/cluster 1.6x/yr; perf/chip 1.6x/yr. Total AI compute ~3.3x/yr (~7-month doubling).
Owner:  Epoch AI data-insights (supercomputers page opened; chip-production page via index)
Scope:  728 supercomputers 2010-Jan 2025; 57 "leading"; peak 16-bit FLOP/s.
```
```text
Figure: Cisco FMC CVE-2026-20316 = CVSS 3.1 base 5.3; exploited; CISA KEV added 2026-07-29; FCEB deadline 2026-08-01. Related CVE-2026-20079 / CVE-2026-20131 = CVSS 10.0, disclosed March 2026, not confirmed exploited.
Owner:  NVD/Tenable (opened) + Cisco advisory + CISA KEV
Scope:  FMC releases 7.0/7.2/7.4/7.6/7.7/10.0; hot fixes, no workarounds.
```

## Source assets

```text
Asset: The 10-file Lean directory listing in github.com/openai/ten-proofs
Shows: That each claimed result has a named, machine-checkable artifact (turns "AI
       solved ten problems" from assertion into inspectable objects).
Crop:  Keep the filenames legible; they name the ten problems. Omit repo chrome.
```
```text
Asset: The vagus-nerve 3D fascicle/fiber reconstruction on sparc.science (REVA dataset)
Shows: How fascicles carrying different organs' signals are spatially organized within
       the nerve — the whole point for targeted stimulation.
Crop:  Retain the fascicle organization and a scale reference; omit decorative renders.
```
```text
Asset: Epoch AI's log-linear performance-vs-year chart (leading AI supercomputers)
Shows: The 2.5x/yr (~9-month doubling) trend and its confidence interval, if a chart is
       used at all for the compute-context item.
Crop:  Must keep the log axis label and the fitted line; note the non-linear scale in
       any caption (per spec/charts.md).
```
```text
Asset: Cisco/CISA exploitation-chain diagram (20316 low-priv login -> chain -> 20079/20131 root)
Shows: Why a "5.3" bug is the one being exploited — the chain is the story.
Crop:  n/a (would be built from the advisories; no single ready image confirmed).
```

## Discarded

```text
https://www.sciencedaily.com/releases/2026/03/260313002642.htm — 3D-printed WC-Co tungsten carbide (Hiroshima hot-wire laser): real result but dated Feb-Mar 2026, journal print issue April 2026; not an Aug-4 development.
https://thequantuminsider.com/2026/06/13/microsoft-and-quantinuum-report-on-major-gains-in-quantum-error-correction/ — Microsoft/Quantinuum 800x error-correction gain: published Nature ~2026-06-10; stale.
https://interestingengineering.com/energy/us-laser-nuclear-fusion-achieves-energy-records — NIF 11th ignition (7.9 MJ, gain ~3.8): June 2026; stale and target-level not plant-level; not on-date.
https://www.un.org/independent-international-scientific-panel-ai/en/preliminary-report — UN AI Panel preliminary report: released 2026-07-01, and it is policy/governance -> current-events, not tech-news.
https://www.nejm.org/doi/abs/10.1056/NEJMoa2511778 — CTX310 CRISPR ANGPTL3 Phase 1 (NEJM): data presented AHA Nov 2025; ESC durability update is 2026-08-28 (future). Not an Aug-4 result.
177Lu-edotreotide (ITM-11) COMPETE trial (PFS 23.9 vs 14.1 mo) — real Phase 3 result but presented ENETS/ESMO 2025; not yet in NEJM/Lancet; FDA PDUFA date 2026-08-28. Regulatory-calendar item, not an on-date development.
https://www.nature.com/articles/d41586-026-01686-3 — ESMFold2 open protein-structure atlas: published Nature May 2026; stale.
https://www.sciencedaily.com/releases/2026/05/260527023220.htm — 151 K ambient-pressure superconductor (U. Houston): May 2026; stale.
https://www.scientificamerican.com/article/see-the-first-complete-map-of-a-mammals-peripheral-nervous-system-in/ — Cell (Shi et al., 2025-07-10) whole-MOUSE PNS map: a different, older study than the human vagus atlas; opened and set aside to avoid conflating the two.
https://www.neuralstack.network/ — aggregator of YouTube recaps, funding trackers, and breach roundups; no owning primary for an Aug-4 development.
https://www.buildfastwithai.com/blogs/ai-news-today-august-2-2026 — useful index of Aug-2 stories, but a secondary digest, not a primary; used only to locate candidates.
Ai4 2026 conference (Las Vegas, Aug 4-6; Hinton/Ng/Li) — an event, not a development that moved; no result attached. Excluded.
GenOffice / Genspark open-source office suite (Aug 4) — product launch; excluded per "product promotion" rule.
Apple >$10bn India sales (Aug 4) — business milestone, not a technology development.
```
