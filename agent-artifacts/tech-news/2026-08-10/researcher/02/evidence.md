# Evidence record: tech-news/2026-08-10 (researcher 02)

## What this record supports, and where it is thin

Round 01 found two firm items and two marginal ones. This round keeps the two
firm ones and adds three fresh items with primaries I opened, bringing the brief
to **five firm items** and retiring the two marginals. The window is early
August 2026; the strongest developments cluster on 1-6 August rather than the
tight 8-10 window, which is why round 01 read the day as thin.

The five firm items, each with an openable primary:

1. **OpenAI publishes ten new results in mathematics and theoretical computer
   science, with Lean 4 certificates on GitHub** (blog and manuscript dated
   1-2 Aug 2026). Primaries opened: the 253-page manuscript PDF on OpenAI's CDN
   and the `openai/ten-proofs` GitHub repository. The vendor framing ("solved
   ten open problems," model named "Astra," "$2,000" of compute) runs ahead of
   what the manuscript itself claims and what anyone has verified. The manuscript
   names only "an internal OpenAI model," calls the results "advances," and the
   independent record is explicit that reaction is not yet verification. This is
   the item where the commission's "report the number the vendor's chart omits"
   instruction bites hardest.
2. **EU AI Act Article 50 transparency obligations enter application** (2 Aug
   2026). Carried forward from 01, unchanged.
3. **California AI Transparency Act becomes operative** (2 Aug 2026). Carried
   forward from 01, unchanged.
4. **Tesla and SpaceX commit $16.8 billion to "Terafab," a Texas semiconductor
   fab** (6 Aug 2026). Primary opened: the Texas Governor's official release;
   SpaceX's own announcement ran on X.
5. **SK hynix and Sandisk release the first High Bandwidth Flash (HBF) standard
   at FMS 2026** (4 Aug 2026). Primary opened: SK hynix's newsroom.

Two round-01 marginals are **retired, not carried into the selection**: the
NVIDIA/NAVER Korea AI-factory deal (firm primary but dated 24 July, stale for a
10 August brief) and EO 14409's 1 August benchmarking deadline (primary
fetch-gated, deliverable classified and unconfirmable). Their round-01 records
are preserved below under "Retired items" so the writer and editor can see the
prior work and the reason each was displaced. Three fresh firm items displace
both, per the brief's instruction to drop the weakest marginal when firmer items
arrive.

The two commission candidates that broke under round-01 verification stay broken:
no August FDA "autonomous diagnostic AI" class exists, and the August frontier
model releases still have no openable vendor primary. Neither is revived.

---

## Sources — grouped by item

### Item 1 (firm): OpenAI publishes ten results in mathematics and theoretical computer science with machine-checkable Lean proofs, 1-2 August 2026

```text
URL:         https://cdn.openai.com/pdf/ten-proofs-oai.pdf
Kind:        primary — OpenAI's own 253-page manuscript, "Ten Advances in
             Mathematics and Theoretical Computer Science," authored and hosted
             by OpenAI. Opened and read directly (front matter, abstract, table
             of contents, and full-text search of the extracted text).
Establishes: The abstract states the results were "obtained by an internal
             OpenAI model." The ten results, verbatim from the abstract/contents:
             (1) high-dimensional sphere packing — the asymptotic strength of the
             Cohn-Elkies linear program is determined exactly, improving the
             general high-dimensional packing bound; (2) binary and spherical
             codes — classical fixed-distance upper bounds improved by exponential
             factors; (3) non-sofic groups exist — an explicit non-sofic group is
             constructed, answering whether every countable group is sofic;
             (4) Connes's rigidity conjecture — disproved, via infinitely many
             pairwise non-isomorphic property-(T) groups sharing one group von
             Neumann algebra; (5) arithmetic circuit complexity — permanent lower
             bounds; (6) quantum parallel repetition; (7) closest vector problem;
             (8) Ehrhart's volume conjecture; (9) multicolor Ramsey numbers;
             (10) extremal number conjectures (Erdos problems 146 and 180).
             The manuscript does NOT contain the string "Astra," does NOT state a
             "$2,000" compute cost, and frames the work as "advances," not as
             "solving ten open problems."
Paraphrase:  OpenAI's own manuscript attributes the results to an unnamed internal
             model and presents them as ten advances, several of which resolve a
             named open question (non-sofic groups, Connes's conjecture) and
             several of which improve an existing bound.
Locators:    Title page; Abstract (p. ii, items 1-10); Contents (pp. iii-...).
             253 pages as read from the PDF (press reports "249"; treat 253 as the
             read count of this file).
Quote:       "We present a collection of results obtained by an internal OpenAI
             model, spanning mathematics and theoretical computer science."
             "An explicit nonsofic group is constructed, answering the
             longstanding question of whether every countable group is sofic."
```

```text
URL:         https://github.com/openai/ten-proofs
Kind:        primary — OpenAI's own repository of Lean 4 certificates for the ten
             results. Opened and read (README).
Establishes: Repository description: "Lean certificates accompanying ten proofs in
             mathematics and theoretical computer science." It carries Lean 4
             formalizations of all ten results, an Apache-2.0 license, and points
             to the manuscript on openai.com and a separate "reasoning walkthroughs"
             document. The README describes independent proof checking via a tool
             it calls Comparator, and states the build requires Lean 4.32.0,
             mathlib, and Lake. The exact "sorry" count (secondary coverage claims
             zero) was not visible in the README excerpt I read; the presence of
             compiling Lean 4 certificates is what the repository establishes
             firsthand.
Paraphrase:  The formal artifacts are public and machine-checkable: the theorems,
             as stated in Lean, can be verified by anyone who compiles the repo.
             What the repo cannot establish is that each Lean statement faithfully
             encodes the informal theorem it claims to prove.
Locators:    Repository root README; license file (Apache-2.0); ten result
             directories.
Quote:       "Lean certificates accompanying ten proofs in mathematics and
             theoretical computer science."
```

```text
URL:         https://openai.com/index/ten-advances-in-mathematics/
Kind:        primary — OpenAI's announcement blog post, the document that owns the
             "Astra" naming and the "$2,000" cost claim. NOTE: gated — returns HTTP
             403 to an automated fetch; it resolves in a browser. Recorded as the
             source's own page. Its substantive claims were read via the manuscript
             and GitHub primaries above and the independent accounts below; the two
             claims unique to the blog (model name, compute cost) are attributed,
             not independently verified here.
Establishes: Per the blog and wide corroboration, OpenAI used this post to reveal
             that its next major model family is named "Astra," disclosed in the
             post's third paragraph, and put the compute cost of finding all ten
             results at "roughly $2,000." Neither claim appears in the manuscript.
Paraphrase:  The model name and the headline cost figure live only in the
             announcement post, not in the formal manuscript. A headline that
             states "Astra" or "$2,000" as fact is citing the blog, not the proofs.
Locators:    Post body, third paragraph (naming); cost sentence.
Quote:       (primary gated; naming and cost read via secondary — see below)
```

```text
URL:         https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/
Kind:        secondary — independent technical account (Simon Willison), dated
             1 Aug 2026. Reports on the release from outside OpenAI.
Establishes: Independent confirmation that OpenAI released the manuscript, the Lean
             certificates on GitHub, and the reasoning walkthroughs on 1 August
             2026, and that the model behind the results is an internal, unreleased
             system. Used for the date and the shape of the release.
Paraphrase:  A careful independent write-up corroborates the artifacts and the
             1 August date.
Locators:    Post body.
Quote:       —
```

```text
URL:         https://www.understandingai.org/p/openais-milestone-math-breakthrough
Kind:        secondary — independent analysis (Timothy B. Lee, Understanding AI).
             This is the independent check the vendor framing omits.
Establishes: The distinction the announcement blurs: what had happened as of
             publication was reaction, not verification. No named mathematician had
             publicly reported working through any of the ten arguments; outside
             researchers still must compare each natural-language claim, its formal
             Lean statement, and the prior literature, and journal peer review is a
             separate process still to come. Fields Medalist Timothy Gowers called
             it a milestone and said he would have recommended a proof for
             publication in a top journal; Thomas Bloom, who curates the Erdos
             problem catalogue, called the constructions big news. These are named
             expert reactions, not completed verifications.
Paraphrase:  The Lean certificates guarantee the formalized theorems compile; they
             do not guarantee the formal statements match the informal claims, and
             that gap is exactly what no one has yet closed in public. Attribute the
             enthusiasm to Gowers and Bloom by name, and keep reaction and
             verification separate.
Locators:    Body; sections on verification status and expert reaction.
Quote:       "What has happened so far is reaction, not verification."
```

### Item 2 (firm): EU AI Act Article 50 transparency obligations enter application, 2 August 2026

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
Locators:    Library page, "Guidelines on transparency obligations..."; publication
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
             they are interacting with an AI," except where "obvious ... to a natural
             person who is reasonably well-informed, observant and circumspect";
             (b) providers of generative systems must ensure outputs are "marked in
             a machine-readable format and detectable as AI-generated" (text, audio,
             image, video), with "technical standards ... still under development
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
             published a voluntary Code of Practice as a compliance pathway.
Paraphrase:  An independent firm's day-after read matches the Commission's own
             dates and confirms the 2 December 2026 grace period for pre-existing
             generative systems.
Locators:    "The Four Scenarios"; "Transitional Deadline"; publication date 3 Aug
             2026.
Quote:       "Providers have until 2 December 2026 to comply."
```

Independent penalty figure (consistent across firm analyses): non-compliance can
trigger fines up to **EUR 15 million or 3% of worldwide annual turnover**,
whichever is higher. Owner of the penalty is the AI Act itself (Article 99);
treat as context pending a primary reading of Article 99.

### Item 3 (firm): California AI Transparency Act (SB 942, amended by AB 853) becomes operative, 2 August 2026

```text
URL:         https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853
Kind:        primary — the enrolled/chaptered text of AB 853 on the California
             Legislature's own site. Read directly.
Establishes: AB 853 amends Business and Professions Code sections 22757.1, 22757.4,
             22757.6 and adds 22757.3.1, 22757.3.2, 22757.3.3. "Approved by
             Governor October 13, 2025; filed with Secretary of State October 13,
             2025." Principal operative clause: "This chapter shall become operative
             on August 2, 2026." Added obligations phase in later: platform
             provenance detection operative 1 January 2027 (22757.3.1-.3.2),
             capture-device disclosure operative 1 January 2028 (22757.3.3).
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
             1,000,000 monthly visitors or users and ... publicly accessible within"
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
Locators:    Bill nav page, SB 942 (2023-2024 session).
Quote:       —
```

The delay to 2 August was explicitly to line up with the EU: firm analyses report
the amendment moved the operative date "from January 1, 2026, to August 2, 2026,
a move intended to align with the implementation timeline of the European Union's
AI Act." Treat as reported context, corroborated by the shared date.

### Item 4 (firm): Tesla and SpaceX commit $16.8 billion to "Terafab," a Texas semiconductor fab, 6 August 2026

```text
URL:         https://gov.texas.gov/news/post/governor-abbott-announces-spacex-expansion-in-grimes-county
Kind:        primary — the Office of the Texas Governor's official release,
             announcing the state action and the incentive it granted. The state is
             a party with stake (it owns the Texas Enterprise Fund grant). Read
             directly. Dated 6 August 2026.
Establishes: A $16.8 billion first-phase capital investment by Tesla and SpaceX in
             a Grimes County semiconductor facility named Terafab; a $30 million
             Texas Enterprise Fund grant to SpaceX; 3,000 new jobs; roughly
             100 million square feet; chips for AI "on Earth and in space." Carries
             a quote from Elon Musk and from Governor Abbott.
Paraphrase:  The state confirms the project, the headline investment, the jobs, and
             its own $30 million incentive on the record.
Locators:    Release body; investment, grant, jobs, and square-footage figures;
             Abbott and Musk quotes.
Quote:       Musk: "The Terafab is bringing cutting-edge manufacturing to America,
             creating thousands of high-paying jobs."
```

```text
URL:         https://techcrunch.com/2026/08/06/tesla-and-spacex-will-invest-16-8b-to-start-building-terafab-chip-factory-in-texas/
Kind:        secondary — independent US newsroom (TechCrunch), dated 6 August 2026.
Establishes: SpaceX announced the project on 6 August, describing Terafab as built
             for "unprecedented scale and speed," a vertically integrated site
             handling logic, memory, advanced packaging, and testing under one roof,
             with chips intended for Tesla's Optimus robots and Cybercabs and for
             SpaceX's space-based data centers. SpaceX posted a video rendering of a
             single roughly 2.5-mile-long building on X.
Paraphrase:  Independent reporting supplies the technical scope (logic + memory +
             packaging + test, vertically integrated) and the end uses the state
             release does not itemize, and locates SpaceX's own announcement on X.
Locators:    Lede and project-detail paragraphs.
Quote:       "unprecedented scale and speed."
```

```text
URL:         https://electrek.co/2026/08/06/tesla-spacex-terafab-grimes-county-16-8-billion/
Kind:        secondary — independent trade newsroom (Electrek), dated 6 August 2026.
Establishes: Corroborates the $16.8 billion first phase and Grimes County site;
             independent reporting puts potential total investment across future
             phases as high as ~$119 billion, and notes the site draws water from
             the Gibbons Creek Reservoir rather than local groundwater.
Paraphrase:  A second independent account confirms the phase-one figure and adds
             the larger multi-phase ambition the one-line announcement omits.
Locators:    Body; investment and site paragraphs.
Quote:       —
```

### Item 5 (firm): SK hynix and Sandisk release the first High Bandwidth Flash (HBF) standard at FMS 2026, 4 August 2026

```text
URL:         https://news.skhynix.com/en/hbf-at-fms-2026/
Kind:        primary — SK hynix's own newsroom, the co-author of the standard.
             Read directly. Publication date 4 August 2026; FMS 2026 ran 4-6 August
             2026 at the Santa Clara Convention Center.
Establishes: SK hynix and Sandisk unveiled the first standard specification for
             High Bandwidth Flash (HBF), a NAND-based memory layer that sits between
             HBM and SSD. Specification: capacities up to 512GB (8-high and 16-high
             die configurations); three performance grades from 0.4 TB/s to
             3.0 TB/s; UCIe (Universal Chiplet Interconnect Express) as the
             interconnect. The first spec landed roughly six months after the
             consortium launched (February 2026), released through the Open Compute
             Project as an open standard; consortium partners include SK hynix,
             Sandisk, Google, and Tenstorrent. At the same event SK hynix showed a
             375-layer 4D NAND (V10) with 2.5x better power efficiency than the
             prior generation, mass production planned early 2027. Quote from
             Executive Vice President Kim Chun-sung.
Paraphrase:  HBF standardizes a high-capacity, NAND-based tier to relieve the AI
             memory-capacity bottleneck that HBM alone cannot fill, and the first
             cross-vendor spec now exists in the open.
Locators:    Release body; capacity, bandwidth, and interconnect figures; consortium
             list; V10 NAND paragraph; EVP quote.
Quote:       Kim Chun-sung (EVP, SK hynix): "Through HBF, SK hynix will expand the
             boundaries between memory and storage and contribute to building new
             architectures that enhance overall system efficiency."
```

```text
URL:         https://www.hpcwire.com/off-the-wire/sk-hynix-unveils-1st-hbf-standard-specifications-with-sandisk-at-fms-2026/
Kind:        secondary — independent HPC trade newsroom (HPCwire). Reports the same
             release from outside the vendors.
Establishes: Corroborates the first HBF standard, the SK hynix/Sandisk authorship,
             and the positioning of HBF as an HBM-adjacent, NAND-based capacity tier
             for AI workloads.
Paraphrase:  Independent confirmation of the standard and its intent.
Locators:    Body.
Quote:       —
```

```text
URL:         https://www.trendforce.com/news/2026/08/05/news-samsung-expected-to-showcase-zhbm-at-fms-2026-a-next-gen-3d-memory-architecture-with-4x-bandwidth/
Kind:        secondary — independent industry analyst (TrendForce), 5 Aug 2026.
             Used only as context for the competing showcase, not selected as an
             item.
Establishes: At the same FMS 2026, Samsung previewed "zHBM," a next-generation
             stacked-memory concept the company frames as a successor to z-NAND,
             with claimed performance up to ~8x HBM5. This is a roadmap/preview
             claim (a concept product), not a released standard, and is weaker on
             consequence than SK hynix's shipped spec — recorded so the writer does
             not mistake the Samsung preview for a delivered standard.
Paraphrase:  Samsung's zHBM is a competing preview, not a finished specification;
             SK hynix's HBF is the firm development here.
Locators:    Body.
Quote:       —
```

---

## Contradictions

- **OpenAI's framing outruns its own manuscript and the independent record.** The
  announcement blog names the model "Astra" and puts the cost at "roughly $2,000";
  the 253-page manuscript I read does neither — it says "an internal OpenAI model"
  and calls the results "advances," not solved open problems. Several of the ten
  are improved bounds (sphere packing, codes, circuit lower bounds), not the
  resolution of a yes/no question; two are genuine resolutions (a non-sofic group
  is constructed; Connes's rigidity conjecture is disproved). A headline that says
  OpenAI "solved ten open problems" adopts the blog's gloss over the manuscript's
  own word. Attribute "Astra" and "$2,000" to the announcement post, not the
  proofs.

- **For the OpenAI item, verification is the number the vendor omits.** The Lean 4
  certificates make the formalized theorems machine-checkable: compile the repo and
  the stated theorems hold. That guarantee stops at the formal statement. Whether
  each Lean statement faithfully encodes the informal claim, and whether the results
  survive journal peer review, is unsettled: as of the reporting window no named
  mathematician had publicly worked through any of the ten arguments. Timothy
  Gowers and Thomas Bloom offered praise, which is reaction, not verification. The
  vendor's "trustlessly verifiable" framing is true of the formalization and not yet
  true of the mathematics as a whole.

- **EU Article 50: obligation live, standard pending.** The machine-readable
  marking-and-detection duty for AI-generated content is legally in force from 2
  August 2026, yet the technical standard for how to mark is not finalized — the
  Commission offers a voluntary Code of Practice, and pre-existing generative
  systems get until 2 December 2026. Regulator and independent analysis agree on the
  dates; neither claims the standard is settled. A real tension in the primary
  record, not a divergence between accounts.

- **California vs EU scope.** Same operative date, different reach: EU Article 50
  covers chatbots, emotion recognition, deepfakes, and synthetic-content marking for
  all providers; California binds only generative providers above 1,000,000 monthly
  users and adds a public detection-tool duty the EU rule does not. A table is the
  honest way to show the overlap and the gap.

- **Terafab is a capex commitment, not a running fab.** The $16.8 billion is a
  first-phase investment announced 6 August with civil work only beginning; the
  larger ~$119 billion figure is a potential multi-phase total from independent
  reporting, not a committed number. Report it as a commitment and a groundbreaking,
  not as capacity that exists.

- **FMS 2026: SK hynix shipped a spec; Samsung previewed a concept.** SK hynix and
  Sandisk released an actual first HBF standard through the Open Compute Project;
  Samsung's zHBM at the same show is a preview with a claimed ~8x-HBM5 figure and no
  released standard. Do not level the two.

- **The two broken commission candidates remain broken.** No August 2026 FDA
  authorization creates a class of autonomous diagnostic AI (the only true
  autonomous-diagnosis authorization on record is IDx-DR from 2018; the July 2026
  Syncron-E De Novo is assistive ventilator-waveform software). The August frontier
  model releases (Qwen 3.8-Max, Seedance 2.5, Muse Spark 1.2) still have no openable
  vendor primary. Neither is revived. Note that "Astra" here is a research
  announcement of an unreleased model, not a shipped frontier model with a system
  card and benchmarks — it is a different kind of item.

---

## Numbers

```text
Figure: 10 results; 253-page manuscript (press: 249); ~$2,000 compute (blog claim)
Owner:  OpenAI manuscript (results, page count read from PDF); OpenAI blog (cost)
Scope:  Ten advances in math/TCS by "an internal OpenAI model"; cost figure is the
        announcement post's, absent from the manuscript. Verification of the
        informal claims is not yet done in public.
```

```text
Figure: 2 August 2026 — operative date, EU AI Act Article 50 transparency duties
Owner:  Regulation (EU) 2024/1689, Art. 50 / European Commission guidelines
Scope:  Applies to in-scope systems regardless of when placed on market; marking
        obligation for pre-existing generative systems deferred to 2 Dec 2026.
```

```text
Figure: up to EUR 15,000,000 or 3% of worldwide annual turnover — max Art. 50 penalty
Owner:  EU AI Act (Article 99 penalty tiers), reported via legal analyses
Scope:  Whichever is higher; treat as context pending a primary reading of Art. 99.
```

```text
Figure: 2 August 2026 — operative date, California AI Transparency Act
Owner:  Cal. Bus. & Prof. Code Ch. 25, Div. 8 (SB 942 as amended by AB 853)
Scope:  Covered providers = generative-AI systems with >1,000,000 monthly
        visitors/users, publicly accessible in California. Platform duties from
        1 Jan 2027; capture-device duties from 1 Jan 2028.
```

```text
Figure: $16.8 billion first phase; $30 million Texas Enterprise Fund grant;
        3,000 jobs; ~100 million sq ft; up to ~$119 billion across future phases
Owner:  Texas Governor's release ($16.8B, $30M, 3,000, 100M sq ft); Electrek
        (potential ~$119B multi-phase)
Scope:  Grimes County, TX fab "Terafab" (Tesla + SpaceX); phase-one commitment,
        civil work beginning; multi-phase total is potential, not committed.
```

```text
Figure: HBF: up to 512GB per stack; 0.4-3.0 TB/s (three grades); UCIe interconnect;
        375-layer V10 4D NAND at 2.5x power efficiency
Owner:  SK hynix newsroom (HBF spec and V10 NAND figures)
Scope:  First HBF standard specification, released via Open Compute Project;
        consortium SK hynix / Sandisk / Google / Tenstorrent; V10 mass production
        planned early 2027.
```

```text
Figure: ~8x HBM5 performance — Samsung zHBM (context only, not a selected item)
Owner:  Samsung, via TrendForce (5 Aug 2026)
Scope:  A preview/concept at FMS 2026, not a released standard.
```

---

## Source assets

```text
Asset: OpenAI ten-proofs GitHub repository tree (openai/ten-proofs)
Shows: That the formal artifacts are public and auditable — ten result directories,
       Lean 4 certificates, Apache-2.0 license. The visual argument is that the
       proofs are open, which grounds the "machine-checkable" claim honestly.
Crop:  A screenshot of the repo root file tree; retain the directory names and the
       license badge. No decorative rendering.
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
Asset: HBF-in-the-memory-hierarchy comparison (from the SK hynix figures)
Shows: Where HBF sits between HBM and SSD on bandwidth (0.4-3.0 TB/s) and capacity
       (up to 512GB), i.e. the capacity tier HBM cannot reach and the bandwidth SSD
       cannot reach.
Crop:  A small nb-table of bandwidth/capacity by tier beats vendor prose; keep the
       three HBF grades and the UCIe note.
```

No decorative imagery. Where numbers carry an item (transparency thresholds; HBF
grades; Terafab magnitudes), a table is the right furniture; elsewhere prose
suffices.

---

## Retired items (round-01 records preserved; displaced by fresher firm items)

These two were round-01's marginal items. Three fresh firm items now fill the
brief, so neither is selected. Records kept so the decision is auditable.

### Retired A: NAVER, NVIDIA and Brookfield Korea AI-factory expansion — stale (24 July 2026)

```text
URL:         https://nvidianews.nvidia.com/news/naver-nvidia-and-brookfield-to-expand-koreas-national-ai-factory-infrastructure-buildout
Kind:        primary — NVIDIA's own newsroom release, read directly. Dated 24 July
             2026.
Establishes: Proposal to grow the NVIDIA DSX AI-factory deployment at the GAK Sejong
             data center from 55 MW to 200 MW by 2028, NAVER's stated 1 GW long-term
             target, a $1 billion NVIDIA investment into NAVER, and a Brookfield
             nonbinding term sheet for up to $9 billion in project financing. UPI
             (secondary, 27 July) adds the omitted ~4.5% NVIDIA stake, making it
             NAVER's third-largest shareholder.
Reason retired: Firm primary, but dated 24 July — roughly two-plus weeks stale for a
             10 August daily brief, and displaced by three fresher firm items.
Locators:    Release body; MW, dollar, and timeline figures.
Quote:       "expand the initial NVIDIA DSX AI factory buildout ... from 55 megawatts
             to 200 megawatts by 2028."
```

### Retired B: U.S. EO 14409 frontier-model benchmarking deadline — unverifiable (1 August 2026)

```text
URL:         https://www.federalregister.gov/documents/2026/06/05/2026-11415/promoting-advanced-artificial-intelligence-innovation-and-security
Kind:        primary — Federal Register publication of EO 14409. NOTE: fetch-gated
             (302-redirects an automated request to a challenge page); resolves in a
             browser. Could not be read firsthand in round 01.
Establishes: EO 14409, signed 2 June 2026, sets a 60-day (i.e. by 1 August 2026)
             deadline for Treasury/NSA/CISA to develop a classified benchmarking
             process designating "covered frontier models," plus a voluntary 30-day
             pre-release review window. Corroborated by CRS IF13268 and law-firm
             analyses (both also fetch-gated).
Reason retired: The 1 August deliverable is classified and cannot be confirmed to
             have occurred; the primary is fetch-gated. Consequential in principle,
             unverifiable in practice, and displaced by firmer items.
Locators:    FR doc 2026-11415; EO 14409 (per secondary summaries).
Quote:       (primary not read; see caveat)
```

---

## Discarded

```text
URL: https://openai.com/index/ten-advances-in-mathematics/
     — the OpenAI announcement post is NOT discarded (it is Item 1's naming/cost
     primary), but note it 403s to automated fetch; its unique claims ("Astra,"
     "$2,000") are attributed, read via secondary, not verified in the manuscript.
```

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
URL: https://qwenlm.github.io/blog/qwen3.8-max/ ; ByteDance/Volcano Engine Seedance
     2.5 ; Meta Muse Spark 1.2
     — the August frontier/open-weight model releases: no openable vendor primary
     resolves (the Qwen vendor blog 404s; the rest trace to aggregators). Cannot
     verify any benchmark or the omitted independent number. Not usable.
```

```text
URL: https://deploymentsafety.openai.com/gpt-5-6
     — genuine OpenAI system card, but GPT-5.6 shipped 9 July 2026, outside the
     window. Not an August development.
```

```text
URL: https://www.trendforce.com/... (Samsung zHBM) — retained as context under Item 5
     only; not selected as its own item because it is a concept preview, not a
     released standard.
```

```text
URL: aggregators/leaderboards (llm-stats, aireleasetracker, digitalapplied,
     buildfastwithai, coursiv, techjournal, enterprisedna, and similar)
     — no primary authorship over any claim; used only to locate candidates and to
     read the framing of the OpenAI announcement, cited as primary for nothing.
```
