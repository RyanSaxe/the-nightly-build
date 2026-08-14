# Evidence record: tech-news/2026-08-14 (01)

The evidence supports a front page built around two items dated exactly 14
August — Z.ai's GLM-5.3 release and the default flip of Claude Code's auto
mode — with a strong health-science result (glucose-responsive probiotics,
Nature, 12 August) and a cross-provider AI-security paper (reasoning-trace
theft, arXiv 10 August, widely reported through 12–14 August) as the next
tier. An inference-speed release (OpenAI's Ultrafast) and a routine model
refresh (Gemini 3.7 Flash) round out the AI-lab news from 13 August. A
battery-materials paper (Science Advances, Cornell, published in the 7–10
August window) is a week old relative to this edition and is included with
that caveat flagged rather than presented as fresh. Two items — Google's
1-billion-MAU milestone for the Gemini app and OpenAI's Daybreak/GPT-5.6-Cyber
expansion — are included only as weak, stale candidates the writer should
likely pass over; both are 3–4 days old and the Daybreak item duplicates
ground the GLM-5.3 cybersecurity benchmarks already cover.

Where the evidence is thin: every AI-lab capability claim below (GLM-5.3's
benchmark table, the Claude Code auto-mode safety study, OpenAI's speed and
GDP-val figures, Google's Gemini 3.7 Flash benchmarks) is self-reported by the
lab that built the product, tested by that lab's own harness and judge
models, and not yet independently reproduced. This is flagged item by item in
Contradictions. The Nature probiotics paper's quantitative efficacy figures
(exact glycaemic and lipid numbers) sit behind Nature's subscriber wall; I
could read the methods, figure legends, extended-data captions, and metadata
in full, and confirm the mechanism and animal models, but could not extract
the headline result numbers from the paywalled results section, and I could
not locate an independent (non-Nature-family) newsroom account of this paper
specifically — that is a real gap, noted in Sources and Discarded. The
reasoning-trace-theft paper has a live figure discrepancy between the arXiv
abstract and a secondary account, recorded in Contradictions. This session's
web-search budget was exhausted before I could locate a second, fully
independent secondary account for two items (probiotics; Gemini 1B MAU); both
limitations are called out where they occur.

## Sources

### 1. GLM-5.3 (Z.ai)

```text
URL:         https://z.ai/blog/glm-5.3
Kind:        Primary — Z.ai's own release announcement for its own model;
             it owns every claim about GLM-5.3's training and benchmark scores.
Establishes: GLM-5.3 shipped 14 August 2026 (page's own Published Time
             metadata: "Fri, 14 Aug 2026 05:17:23 GMT"). Same base model as
             GLM-5.2; all gains came from post-training. Self-reported
             benchmarks: Terminal-Bench 3.0 rose from 4.6 to 28.3; DeepSWE
             v1.1 from 46.2 to 66.9; CyberGym (vulnerability discovery) from
             77.2% to 84.5%, ahead of Mythos 5 (83.8%) and GPT-5.6 Sol
             (83.6%); ExploitBench (exploitation reasoning) more than
             doubled, from 24.4% to 54.4%, while Mythos 5 and GPT-5.6 Sol
             still lead at 78.0% and 76.5%. Working with security teams in
             China since GLM-5.2, the model has been used against real
             codebases and, after expert review, identified 2,436
             vulnerabilities across 269 open-source projects (1,097 rated
             medium-to-high severity), with the oldest flaw dating to 1981
             (45 years old) and an average vulnerability age of 26.6 years.
             Z.ai frames the cyber-capability growth as faster than the
             company expected and explicitly ties the two-week delay before
             releasing open weights to "safety evaluation and hardening."
Locators:    Body text under "Today we are releasing GLM-5.3"; benchmark
             table "Performance across comparison models"; section "Emergent
             Cyber Capability"; section "Getting started with GLM-5.3" /
             "Serve GLM-5.3 Locally" for the two-week open-weight timeline.
Quote:       "What surprised us was how quickly the capability continued to
             develop as training scaled. GLM-5.3 did not simply become
             better at identifying isolated flaws: it began to reason across
             multiple stages of exploitation, forming coherent plans for
             complete exploitation chains."
```

```text
URL:         https://www.unite.ai/z-ai-launches-glm-5-3-with-frontier-coding-and-a-cyber-capability-that-outgrew-its-training/
Kind:        Secondary — Unite.AI reporting on Z.ai's announcement from
             outside the company, with no stake in GLM-5.3's performance.
Establishes: Independently confirms the 14 August 2026 release date (page's
             own Published Time metadata: "2026-08-14T01:47:01-04:00"),
             that weights are not yet public and are promised in about two
             weeks "after safety evaluation and hardening are complete," and
             situates the release against competitors: it "lands days after
             DeepSeek shipped its own flagship V4 Pro out of preview," and
             Z.ai's own comparison table pits GLM-5.3 against DeepSeek-V4
             Pro, Kimi K3, and GPT-5.6 Sol.
Paraphrase:  An outside technology newsroom corroborates the release date,
             the open-weight delay, and the competitive framing, without
             independently re-running any benchmark.
Locators:    Opening paragraph; section "Post-Training on a Bigger Set of
             Work Environments."
```

### 2. Claude Code auto mode becomes the default

```text
URL:         https://claude.com/blog/auto-mode-default-in-claude-code
Kind:        Primary — Anthropic's own announcement of its own product
             change and its own safety study.
Establishes: Auto mode (which routes each tool call through a classifier
             instead of a human-approval prompt, blocking only actions
             "irreversible, destructive, or aimed outside your environment")
             becomes the default for Claude Code Pro, Max, and Team plans
             for new sessions starting 14 August 2026 (page's own dateline:
             "Date August 7, 2026"; body text: "Starting on August 14, new
             sessions on Pro, Max, and Team plans will run in auto mode").
             Anthropic ran a controlled study with 1,053 paid professional
             testers: a single permission prompt was covertly swapped for a
             dangerous command mid-session; human testers caught it 13.6% of
             the time (143 of 1,053) while auto mode blocked it 89% of the
             time (937 of 1,053); head-to-head, auto mode blocked 800
             commands a human tester had approved, and humans blocked only 6
             commands auto mode had allowed. Separately, Anthropic reports
             that in normal usage, "users approve 97% of permission prompts
             in Claude Code," and that among sessions flagged by its safety
             pipeline, manually approved sessions contained a serious
             unintended harm (severity 7+ of 10) more than twice as often as
             auto-mode sessions (6.3% vs 2.4%). Anthropic worked with Apollo
             Research (UK AI-safety org) on adversarial hardening; on a
             held-out attack set the classifier's miss rate fell from 12% to
             7%. Teams using auto mode ship "about 25% more PRs."
Locators:    Opening summary line; paragraph beginning "We're making auto
             mode the default"; section "Auto mode outperforms manual
             permissions on safety"; section "Auto mode prevents more
             harmful actions"; section "Adversarial red-teaming made auto
             mode stronger."
Quote:       "The testers caught the dangerous command just 13.6% of the
             time (143 of 1,053), while auto mode blocked 89% of the same
             commands (937 of 1,053)."
```

```text
URL:         https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/
Kind:        Secondary — TechCrunch reporting on Anthropic's announcement,
             independent newsroom with no stake in the product.
Establishes: Independently corroborates the 14 August rollout date, the
             89%/13.6% figures, and the 97% approval-rate figure, and adds
             an on-record reaction quote from Anthropic's own Claude Code
             lead reacting to the change, plus context that a test version
             of auto mode was first unveiled in March 2026.
Locators:    "Posted: 12:20 PM PDT · August 9, 2026" dateline; body
             paragraphs 2–4.
Quote:       "The team and I use Auto mode exclusively, and have been for
             many months. I couldn't imagine going back to permission
             prompts!" — Boris Cherny, Claude Code lead, quoted from a post
             on X.
```

### 3. GPT-5.6 Sol "Ultrafast" (OpenAI + Cerebras)

```text
URL:         https://openai.com/index/previewing-ultrafast/
Kind:        Primary — OpenAI's own announcement of its own product and its
             own claimed speed figures.
Establishes: OpenAI previewed "Ultrafast," a new API service tier that runs
             GPT-5.6 Sol "up to 14× faster than Standard processing,"
             generating "up to 750 output tokens per second," powered by a
             hardware partnership with Cerebras. Available today only in a
             "limited preview to a select group of customers," expanding "as
             capacity grows." OpenAI frames the significance as decoupling
             speed from model size for the first time at the frontier:
             "Until now, getting real-time speed typically meant choosing a
             smaller or more specialized model." Listed use cases: incident
             response, financial research/security, live customer support,
             commerce, and interactive research loops that previously ran as
             overnight batch jobs.
Locators:    Opening paragraph; section "Powered by Cerebras"; section
             "Availability."
Quote:       "Ultrafast points to progress in a new direction: more useful
             work per second."
```

```text
URL:         https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/
Kind:        Secondary — TechCrunch reporting on OpenAI's announcement,
             independent newsroom.
Establishes: Independently corroborates the 14x/750-tokens-per-second
             figures and the Cerebras partnership and limited-preview
             status; published same day, 13 August 2026 (page's own
             metadata: "2026-08-13T19:22:40+00:00").
Locators:    Headline and first two body paragraphs.
```

### 4. Gemini 3.7 Flash (Google DeepMind) — flagged as incremental

```text
URL:         https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
Kind:        Primary — Google's own release announcement.
Establishes: Google released Gemini 3.7 Flash on 13 August 2026 (page's own
             dateline: "Aug 13, 2026"), "our most intelligent workhorse model
             yet for coding and agents," three weeks after Gemini 3.6 Flash.
             Author: Tulsee Doshi, Senior Director of Product Management,
             Gemini team.
Locators:    Page header/dateline; opening paragraph.
```

```text
URL:         https://venturebeat.com/technology/googles-gemini-3-7-flash-targets-coding-and-agents-with-a-50-introductory-price-cut
Kind:        Secondary — VentureBeat reporting on Google's announcement,
             independent newsroom, includes independent analytical framing
             not present in Google's own post.
Establishes: Confirms release date (13 August 2026, page metadata
             "2026-08-13T18:02:54.407Z") and pricing: $0.75/million input
             and $3.75/million output tokens through year-end 2026 (half the
             standard rate), rising to $1.50/$7.50 on 1 January 2027 — a
             temporary introductory discount, not a permanent price cut.
             Reports Google's own benchmark comparisons show a mixed
             picture: Gemini 3.7 Flash scores 85.8% on Terminal-Bench 2.1
             versus GPT-5.6 Terra's 87.4%, and Terra leads on Terminal-Bench
             3.0 and OSWorld-2.0; Claude Sonnet 5 leads Agent's Last Exam
             desktop/OS tasks at 33.3% versus Gemini 3.7 Flash's 26.3%.
             Cites Artificial Analysis's Intelligence Index score of 56 for
             Gemini 3.7 Flash (up from 52 for 3.6 Flash) against Claude Opus
             5's 63. Cites a SemiAnalysis argument that Google is
             prioritizing cloud-infrastructure revenue over keeping its own
             models at the frontier, and reports 3.5 Pro's release has been
             delayed (Google has not confirmed cancellation).
Locators:    Paragraphs under "unusually short turnaround"; pricing
             paragraph; benchmark-table paragraphs; SemiAnalysis citation
             paragraph near the end.
```

### 5. Glucose-responsive engineered probiotics for diabetes (Nature)

```text
URL:         https://www.nature.com/articles/s41586-026-10909-6
Kind:        Primary — the paper itself; it owns the result.
Establishes: Published online 12 August 2026 (confirmed via the page's own
             "Cite this article" / rights-and-permissions metadata:
             publicationDate "2026-08-12"; formal citation "Guan, N., Kong,
             D., Gao, X. et al. Glucose-responsive probiotics for glycaemic
             modulation in mice and monkeys. Nature (2026).
             https://doi.org/10.1038/s41586-026-10909-6"). Corresponding
             author Haifeng Ye (叶海峰), Shanghai Key Laboratory of
             Regulatory Biology / Biomedical Synthetic Biology Research
             Center, East China Normal University, Shanghai, China; first
             author Ningzi Guan (管宁子), same lab. One co-author (Shangang
             Zhao) is affiliated with UT Health San Antonio. The engineered
             strain is called "GIFT" (probiotic cells carrying a synthetic
             glucose-sensing circuit built on the transcriptional regulator
             HexR, tuned via constitutive-promoter strength, operator-repeat
             number in the glucose-responsive promoter, and ribosome-binding
             site screening); it is engineered to reside temporarily in the
             gut and secrete a therapeutic payload (tested with GLP-1) only
             when glucose exceeds a threshold. Tested in db/db mice,
             diet-induced-obese (DIO) mice, and non-human primates (author
             contributions: "N.G., D.K. and X.G. conducted the therapeutic
             studies in mice and prepared samples for non-human primate
             experiments"). Extended Data figures document long-term daily
             oral dosing (30 days) tracking fasting blood glucose, serum
             GLP-1, plasma insulin, body weight, fat mass, and serum
             triglycerides/total cholesterol, and a head-to-head comparison
             of adverse effects against injected semaglutide.
Locators:    "About this article" / "Cite this article" section (date and
             citation); "Authors and Affiliations" section; "Contributions"
             section; Extended Data Fig. 1 caption (glucose-sensor
             optimization, HexR); Extended Data Fig. 6–7 captions (db/db
             mice, long-term GIFT-GLP-1 effects and complications); Extended
             Data Fig. 9 caption (DIO mice); Extended Data Fig. 10 caption
             (comparison with semaglutide).
Limitation:  The results section itself (the quantitative efficacy figures —
             exact glycaemic control and lipid-profile magnitudes) sits
             behind Nature's subscriber paywall. I read the full metadata,
             methods captions, extended-data legends, references, and
             author list, which is enough to verify the paper is real, dated
             12 August 2026, and does what secondary summaries describe, but
             I could not myself pull the exact headline efficacy numbers
             from the results text. If this item runs, the writer should
             either source a specific efficacy figure from a source with
             full-text access or write around the mechanism and the animal
             models tested rather than citing an unverified magnitude.
```

```text
URL:         https://www.nature.com/articles/d41586-026-02521-5
Kind:        Secondary, with a caveat — this is Nature's own podcast/News
             team (Nick Petrić Howe and Benjamin Thompson) reporting on the
             Guan et al. paper. They are editorially separate from the
             study's authors and have no stake in the result (the
             authorship-and-stake test is met), but they work for the same
             publishing house as the primary journal, which is weaker
             independence than an outside newsroom.
Establishes: Confirms publication date (12 August 2026) and frames the
             result for a lay audience as "genetically modified bacteria
             lower high blood-sugar in animal trials."
Locators:    Episode page header ("12 August 2026"); segment heading "00:45
             A living diabetes treatment."
Limitation:  This session's web-search budget was exhausted before I could
             locate a fully independent (non-Nature) newsroom account of
             this specific paper. Candidate outside articles I found while
             searching (e.g., a site called csnsf.org) turned out to be a
             low-quality repost of this same Nature podcast page, not
             original reporting, and is not fit to cite — see Discarded.
```

### 6. IonNet: AI-screened solid-state battery electrolyte candidates (Science Advances)

```text
URL:         https://www.science.org/doi/10.1126/sciadv.aee4959
Kind:        Primary — the paper itself.
Establishes: "Decoding the chemical space of fast-ion conductors via a
             descriptor-guided transfer learning framework." IonNet, a
             transfer-learning model from a Cornell-led team, was applied to
             ~4,500 stable, perfectly stoichiometric compounds and
             identified 87 candidate fast-ion conductors (FICs, materials
             with ionic conductivity above 1.0×10⁻⁴ S/cm at room
             temperature — the property that matters for solid-state
             battery electrolytes). Expanding to a substituted-composition
             search space of ~5 million compounds (624,460 single-element +
             4,316,850 double-element substitutions), IonNet flagged 62,935
             ("nearly 63,000") additional candidates. Of a further,
             separately screened pool of 154,718 Materials Project
             compounds filtered for stability and electronic-conductivity
             criteria, IonNet flagged 102 promising candidates from the
             remaining 4,583 unique compositions after those filters. The
             authors report each ML prediction takes seconds versus the
             23,000–52,000 CPU-hours a single ab initio molecular-dynamics
             (AIMD) run would need — roughly an eight-order-of-magnitude
             speedup. Twenty top predictions were tested with physics-based
             AIMD simulation; 13 were confirmed as fast-ion conductors. Six
             predicted compounds already have entries in the Inorganic
             Crystalline Structure Database, offered as independent evidence
             the predictions are physically realizable.
Locators:    Abstract; Introduction, paragraph beginning "Here, we proposed
             an attentional TL framework"; Results section discussing the
             154,718-compound Materials Project screen and the
             "approximately eight orders of magnitude speedup"; Results
             section on SES/DES substitution search (624,460 / 4,316,850
             candidates, 11,403 + 51,532 = 62,935 promising hits); Discussion
             section on synthesis feasibility and ICSD entries.
Limitation:  I could not confirm the exact publication date from the page
             content itself (no dateline field rendered in the fetched
             text); secondary sources place it in the 7–10 August 2026
             window, which is a week or more before this edition. If this
             item runs, flag it as a "continuing" item rather than news
             breaking on or immediately before 14 August.
```

```text
URL:         https://interestingengineering.com/energy/cornell-63000-materials-solid-state-batteries
Kind:        Secondary — Interesting Engineering reporting on the paper,
             independent newsroom, published 10 August 2026 (page's own
             metadata: "2026-08-10T18:46:59+00:00").
Establishes: Independently corroborates all four headline figures: ~4,500
             stable compounds screened, 87 candidates from that set, ~5
             million substituted compositions searched, ~63,000 candidates
             from that search, and 20 candidates tested by simulation with
             13 confirmed.
Locators:    Paragraph beginning "The researchers first applied the IonNet
             to roughly 4,500 stable compounds."
```

### 7. Reasoning-trace theft across Anthropic, OpenAI, and Google APIs

```text
URL:         https://arxiv.org/abs/2608.09867
Kind:        Primary — the preprint itself (Panfilov, Schmotz, Shumailov,
             Beurer-Kellner, Schaeffer, Prabhu, Geiping, Andriushchenko;
             ELLIS Institute Tübingen and Max Planck Institute for
             Intelligent Systems, among other affiliations reported
             elsewhere).
Establishes: Submitted 10 August 2026 (page's own submission history: "[v1]
             Mon, 10 Aug 2026 17:24:50 UTC"). Anthropic, OpenAI, and Google
             all return chain-of-thought reasoning to API clients as
             encrypted opaque blocks rather than storing it server-side. The
             paper identifies an architectural flaw: these encrypted blocks
             are interchangeable across sessions, users, and even different
             models within one provider's lineup. The authors replay an
             encrypted trace produced by a strong model into a weaker,
             less-guarded sibling model from the same provider and get the
             weaker model to decode and emit the stronger model's hidden
             reasoning in plaintext — without ever attacking the strong
             model directly. They demonstrate this across all three
             providers named. Beyond IP extraction, they show large-scale
             private-data extraction is possible from reasoning blocks that
             developers unknowingly post publicly: decoding 315,320
             reasoning blocks scraped from public repositories recovered 367
             personally identifiable information (PII) artifacts and 182
             credentials. They also show the flaw can surface content a
             model's visible answer withheld, and can be used to smuggle
             invisible prompt injections inside encrypted blocks. The
             authors followed responsible disclosure and propose
             cryptographic and system-level fixes.
Locators:    Abstract, in full (four numbered attack vectors); submission
             history line for the date.
Quote:       "By injecting an encrypted reasoning trace from a given model
             into a weaker, and less safeguarded model from the same
             provider, we force it to decode and output the trace verbatim
             in plaintext, without ever jailbreaking the more capable model
             directly."
```

```text
URL:         https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html
Kind:        Secondary — The Hacker News reporting on the paper,
             independent outlet, published 13 August 2026 (page's own
             metadata: "Thu, 13 Aug 2026 18:51:16 GMT").
Establishes: Corroborates the 6,708-log, 315,320-block scrape and reports
             that the providers, Microsoft, and Hugging Face were notified,
             and that "the demonstrated attacks stopped working after
             mitigations," with the paper's own reproducibility statement
             saying the main extraction attack is no longer reproducible as
             of August 2026.
Locators:    Paragraph beginning "Across 6,708 public agent trajectories";
             paragraph on disclosure and mitigation status.
```

```text
URL:         https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/
Kind:        Secondary — independent commentator (Simon Willison), no stake
             in any of the three providers named.
Establishes: A concise, accurate restatement of the core mechanism, useful
             as a plain-language gloss; adds no new figures. Notably this
             page's own byline date reads "Fri, 14 Aug 2026," i.e. it
             remained visible/updated in feeds through the 14th, evidence
             the story was still actively circulating on this edition's
             publication day.
Locators:    Single blockquote paragraph.
```

### 8. Gemini app reaches 1 billion monthly active users — weak/stale, flagged

```text
URL:         https://techcrunch.com/2026/08/11/googles-gemini-app-surges-to-one-billion-users/
Kind:        Secondary — TechCrunch reporting on Google CEO Sundar Pichai's
             own announcement (made via a post from the @newsfromgoogle
             account on X on 11 August 2026, which I could not independently
             render — X requires authentication this tool could not
             satisfy). TechCrunch has no stake in the milestone.
Establishes: Pichai announced the Gemini app passed 1 billion monthly
             active users, calling it Google's fastest-growing product and
             the company's 14th product to reach that scale. This followed
             a Q2 2026 earnings call (23 July 2026) at which Google had
             reported "over 950 million monthly users." The article notes
             Gemini's growth keeps pace with ChatGPT, which reached 1
             billion MAU in June 2026 per Reuters (cited within the
             article). 63% of Gemini users engage via voice; the app
             generates more than 150 million images daily (per Google, as
             relayed by TechCrunch).
Locators:    Paragraph beginning "In a significant milestone for Google";
             paragraph on the Q2 2026 earnings-call figure.
Limitation:  I could not open Google/Pichai's own primary post directly
             (X.com fetch was not accessible to this session), so this item
             rests on secondary reporting alone rather than a directly
             verified primary. The underlying event is also three days old
             relative to this edition and is a usage milestone, not a
             technical result — weak fit for "the research itself is the
             development." Recommend the writer drop this item or use it
             only as a one-line note if space allows.
```

## Contradictions

- **Every AI-lab capability and safety claim above is self-reported.**
  GLM-5.3's coding/cyber benchmark table (Source 1) is Z.ai's own harness,
  Z.ai's own judge models, and — by Z.ai's own footnotes — evaluation
  protocols the company designed and tuned (e.g., domain whitelists "to
  prevent the agent from cheating," described entirely in the company's own
  words). No third party has reproduced these numbers; open weights are not
  yet available (promised ~28 August 2026) for anyone to check. Similarly,
  Anthropic's 89%/13.6% auto-mode figure (Source 2) comes from a
  vendor-recruited study Anthropic designed, ran, and graded itself; the
  "6.3% vs 2.4%" production-harm figure comes from Anthropic's own
  internal safety pipeline re-grading its own flagged sessions with an
  Anthropic model as judge. OpenAI's 14x/750-tokens-per-second figures
  (Source 3) and Google's Gemini 3.7 Flash benchmark table (Source 4) are
  likewise self-measured by the lab whose product is being sold. None of
  this means the figures are false; it means none of them have been
  independently reproduced, and the writer should attribute each number to
  the company that made the claim rather than stating it as settled fact.

- **Reasoning-trace theft: primary and secondary disagree on the extraction
  count.** The arXiv abstract itself (Source 7, primary) states the team
  decoded 315,320 reasoning blocks and recovered "367 Personally
  Identifiable Information (PII) artifacts and 182 credentials." The Hacker
  News account (Source 7, secondary) states that after excluding benchmark
  sources, the team "counted 704 distinct privacy artifacts from genuine
  user sessions, including 62 API keys, 33 passwords, 24 access tokens, and
  seven private keys" — a different total and a different credential count
  (62+33+24+7 = 126, not 182) from the same underlying study. This may
  reflect the secondary source citing a subset (post-benchmark-exclusion,
  "genuine user sessions" only) versus the abstract's headline figure, but
  I could not resolve the discrepancy from the abstract alone — the full
  PDF would need to be read to reconcile the two counts. If this item runs,
  cite only the abstract's own numbers (367 PII artifacts, 182 credentials)
  and do not blend the two counts, or flag the discrepancy explicitly.

- **Gemini 3.7 Flash is not uniformly ahead of rivals despite the framing
  of Google's own release post.** VentureBeat's independent read of
  Google's own benchmark table (Source 4, secondary) shows Gemini 3.7 Flash
  trailing GPT-5.6 Terra on Terminal-Bench 2.1 (85.8% vs 87.4%) and on
  Terminal-Bench 3.0 and OSWorld-2.0, and trailing Claude Sonnet 5 on
  Agent's Last Exam desktop/OS tasks (26.3% vs 33.3%). Google's own
  Artificial Analysis Intelligence Index score for the model (56) sits well
  below Claude Opus 5 (63). This cuts against treating the release as a
  leadership claim; it reads more accurately as a price/efficiency play on
  a mid-tier model. A cited outside analysis (SemiAnalysis, relayed by
  VentureBeat) argues Google is deprioritizing frontier-model competition
  in favor of cloud-infrastructure revenue — a contested interpretation
  Google has not confirmed or denied on the record.

- **Coherence risk: three of the eight fresh candidates are security- or
  exploit-flavored** (GLM-5.3's cyber capability, the reasoning-trace-theft
  paper, and the discarded Daybreak/GPT-5.6-Cyber item — see Discarded).
  The commission is explicit that the brief should not lead on another
  agent/harness exploit unless 14 August genuinely warrants it, after three
  straight days led by that genre (08-13 Zoom chain, 08-08 coding-agent
  RCE, 08-07 autonomous-hacking evaluations). None of today's three is a
  disclosed exploit against a real target the way those were: GLM-5.3 is a
  capability release with defensive framing (public disclosure ledger,
  delayed open weights pending "hardening"); the reasoning-trace paper is
  responsibly disclosed academic security research already mitigated by
  the providers; Daybreak/Cyber is a defender-access program. The writer
  should weigh whether running more than one of these, or leading with one,
  risks reading as a fourth straight security-led edition even though the
  substance differs from the prior three days' items.

## Numbers

```text
Figure: GLM-5.3 CyberGym score 84.5% (vs GLM-5.2's 77.2%; GPT-5.6 Sol 83.6%; Mythos 5 83.8%)
Owner:  Z.ai, self-reported (z.ai/blog/glm-5.3)
Scope:  1,507 tasks, single-run Pass@1, evaluated inside Claude Code 2.1.207 harness at max reasoning effort; Z.ai's own domain whitelist applied
```

```text
Figure: GLM-5.3 identified 2,436 vulnerabilities across 269 open-source projects since GLM-5.2 (1,097 rated medium-to-high severity)
Owner:  Z.ai, self-reported, in partnership with unnamed security teams in China
Scope:  Cumulative since GLM-5.2's release, after "expert review, screening, and deduplication"; only 53 of the 2,436 are publicly disclosed as of the blog post, 2,383 remain under embargo
```

```text
Figure: Auto mode caught 89% of dangerous commands (937/1,053) vs 13.6% (143/1,053) for human review
Owner:  Anthropic, self-reported controlled study (claude.com/blog/auto-mode-default-in-claude-code)
Scope:  1,053 paid professional testers in a vendor-run study, single swapped permission prompt per session, test environment not real codebases
```

```text
Figure: GPT-5.6 Sol Ultrafast runs up to 14x faster than Standard, up to 750 output tokens/second
Owner:  OpenAI, self-reported (openai.com/index/previewing-ultrafast/), powered by Cerebras hardware
Scope:  Limited preview availability only, to a select group of customers, as of 13 August 2026
```

```text
Figure: IonNet: 87 fast-ion conductor candidates from ~4,500 stable compounds; 62,935 (~63,000) candidates from ~5,000,000 substituted compositions; 13 of 20 top predictions confirmed by AIMD simulation
Owner:  Cornell-led author team, Science Advances (science.org/doi/10.1126/sciadv.aee4959)
Scope:  Computational screening result; only 20 of the tens of thousands of candidates have been checked against physics-based simulation, and none (as far as the abstract and results discussed) against wet-lab synthesis and conductivity measurement
```

```text
Figure: Reasoning-trace theft: 315,320 reasoning blocks decoded from 6,708 public logs; 367 PII artifacts and 182 credentials recovered (per abstract)
Owner:  Panfilov et al., arXiv:2608.09867 (submitted 10 August 2026)
Scope:  Scraped from publicly posted GitHub/Hugging Face agent trajectory logs; see Contradictions for a conflicting sub-count reported by a secondary source
```

```text
Figure: Gemini app: 1 billion monthly active users, 14th Google product to reach that scale, up from "over 950 million" at the 23 July 2026 earnings call
Owner:  Google / Sundar Pichai, self-reported via X post, relayed by TechCrunch (techcrunch.com/2026/08/11/...)
Scope:  Global monthly active users of the Gemini app specifically, not including Gemini usage embedded in Search's AI Mode or other Google surfaces
```

## Source assets

```text
Asset: GLM-5.3 "Performance across comparison models" benchmark table (z.ai/blog/glm-5.3)
Shows: Every headline figure (coding, cyber, agentic) for GLM-5.3 against GLM-5.2, Kimi K3, DeepSeek-V4 Pro, Qwen3.8-Max, Claude Opus 4.8, Claude Fable 5, and GPT-5.6 Sol in one place
Crop:  Retain the model-name header row and the CyberGym/ExploitBench/ExploitGym rows together if cropping to the cyber story; retain the Terminal-Bench/DeepSWE rows together if cropping to the coding story. Do not crop a single cell out of its row — the comparison to rival models is the point.
```

```text
Asset: Z.ai Security Disclosure Ledger summary tiles (z.ai/blog/glm-5.3, linking to cvd.z.ai): "2,436 FINDINGS TRACKED / 53 PUBLICLY DISCLOSED / 2,383 UNDER EMBARGO / 1,097 CRITICAL & HIGH / 269 OSS PROJECTS / 45 YEARS OF IMPACT"
Shows: The scale and severity distribution of vulnerabilities GLM-5.3 found in real code, and how much of that is still embargoed vs public
Crop:  Keep all six tiles together; the "45 years of impact" and "under embargo" figures are what make this different from a routine benchmark screenshot, and dropping either changes what the asset argues
```

```text
Asset: Anthropic auto-mode blog chart of dangerous-command catch rate by session length ("humans... blocked about 17% of dangerous commands early in a session, dropping to about 5% after 50 or more prior prompts, while auto mode's block rate stayed flat")
Shows: Human vigilance decaying over a session while the classifier's performance does not — the mechanism behind the headline 89%/13.6% gap
Crop:  None found as a rendered chart in the fetched page text; the underlying numbers are in prose. If Anthropic's page has an actual chart image at this location, note that a static screenshot of the 89% vs 13.6% comparison (with sample sizes 937/1,053 and 143/1,053 visible) would carry the finding better than restating it in prose.
```

```text
Asset: IonNet Figure 4 chemical-space screening funnel (science.org/doi/10.1126/sciadv.aee4959, Fig. 4A referenced in Results)
Shows: The funnel from the 154,718-compound Materials Project database down through stability/bandgap filters to the final candidate list, and separately the ~5-million-compound substitution search
Crop:  Keep the funnel's starting and ending counts visible together (154,718 or ~5,000,000 in, tens to tens-of-thousands out) — a crop that keeps only the narrow end loses the scale of the screening claim
```

```text
Asset: VentureBeat's rendered Gemini 3.7 Flash benchmark comparison chart ("Gemini 3.7 benchmark comparison full chart," embedded in the VentureBeat article, credited to Google)
Shows: The same table Google published, laid out for direct visual comparison against GPT-5.6 Terra and Claude Sonnet 5 — including the categories where Gemini 3.7 Flash trails
Crop:  Retain both the categories where Gemini leads and where it trails; a crop showing only Gemini's wins would misrepresent VentureBeat's own point about the "mixed" picture
```

## Discarded

```text
URL: https://csnsf.org/the-probiotic-bacteria-engineered-to-treat-diabetes/ — a Bowen-theory family-therapy nonprofit's blog, not a technology or science newsroom; it is a low-quality repost of the Nature podcast page's own text (Source 5) rather than independent reporting. Rejected as a secondary source.
```

```text
URL: https://openai.com/index/gpt-5-6/ (and adjacent Daybreak/GPT-5.6-Cyber coverage: securityweek.com/openai-unveils-new-cybersecurity-model-gpt-5-6-cyber, thehackernews.com/2026/08/openai-launches-gpt-56-cyber-with.html) — GPT-5.6-Cyber and the Daybreak Blue/Red access tiers shipped 10 August 2026, four days before this edition. Considered as a candidate item; set aside because it is stale relative to 14 August, and because its cybersecurity-capability framing (a model built for authorized offensive security work, reduced refusal rates on exploit-chain tasks) duplicates ground GLM-5.3's CyberGym/ExploitBench comparison already covers in this edition, and would compound the coherence risk noted in Contradictions.
```

```text
URL: https://scitechdaily.com/cornells-breakthrough-could-mean-the-end-of-exploding-batteries/ — fetched while trying to source the IonNet battery item; the rendered content was actually about an unrelated 2024 JACS paper on macrocycle-cage lithium electrolytes, not the IonNet study. Likely a stale cache or mis-indexed page. Discarded in favor of the Cornell Chronicle and Interesting Engineering accounts, which both correctly describe IonNet.
```

```text
URL: https://x.com/newsfromgoogle/status/2087233951031009665 — Google/Pichai's own primary post announcing the 1-billion-MAU milestone. Could not be rendered by this session's fetch tools (X.com requires authentication this tooling does not have). The claim is instead sourced to Source 8's secondary account only; flagged as a limitation there.
```

```text
URL: https://www.techmeme.com/260814/p1 and similar dated Techmeme permalinks — returned HTTP 403 on repeated fetch attempts after an initial successful load of the general river page; used only for headline discovery, not cited as a source for any claim in this record.
```

```text
URL: fusion-energy funding/partnership roundups (Xcimer Energy DOE milestone, Commonwealth Fusion Systems $1B raise, UKAEA-Eni joint venture) — reviewed while searching for a physics candidate; none of these are dated to or freshly advancing around 14 August specifically, and each is a funding/partnership story rather than a technical result. Set aside as not meeting "the research itself is the development."
```

```text
URL: Unitree STAR Market IPO (subscriptions opened 10 August, results due 14 August) — a financial listing event, not a technical result; set aside as outside this brief's scope (product/business milestone, not a development that "changes what a field can do").
```
