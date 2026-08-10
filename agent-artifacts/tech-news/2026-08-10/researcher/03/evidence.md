# Evidence record: tech-news/2026-08-10 (researcher 03)

## What this record supports, and where it is thin

This is a targeted third-round repair of the lead item (OpenAI math results). It
carries forward the five-item selection and the verified items 2-5 from
researcher/02 unchanged, and fixes the single break the editor routed: the
independent account cited for item 1 was the wrong article about the wrong event.

The break, resolved. There are **two distinct OpenAI math stories** in 2026, and
round-02 conflated them:

- **Story A — the Erdős unit-distance disproof (MAY 2026, OUT of window).** On
  ~20 May 2026 OpenAI announced that an internal reasoning model produced the
  first autonomous disproof of the Erdős unit-distance conjecture, an 80-year-old
  discrete-geometry problem. That result **was verified by human mathematicians**:
  a companion paper by nine mathematicians translated and checked the argument the
  same day, and Will Sawin (Princeton) refined the bound to n^1.014. Kai Williams'
  Understanding AI article, "OpenAI's math breakthrough played to AI's strengths"
  (the URL round-02 cited as s2), is about *this* May event, and it correctly says
  "human mathematicians verified the result." It is not an account of the August
  ten-advances manuscript and does not belong to item 1.

- **Story B — the "Ten Advances" manuscript (1-2 AUGUST 2026, IN window).** This
  is the lead item: OpenAI published ten results in mathematics and theoretical
  computer science, credited to an internal version of its next model family
  "Astra," released as a 249/253-page manuscript, a GitHub repo of Lean 4
  certificates (openai/ten-proofs), and a reasoning-walkthroughs PDF, at a claimed
  ~$2,000 total compute. For this item, the accurate in-window status is: the Lean
  certificates make the formalized theorems machine-checkable (they compile); full
  peer review of the underlying ideas and independent working-through of the
  informal arguments has **not** occurred as of the window. No named mathematician
  is documented as having verified the ten results. The human-verification of
  Story A must not be imported into Story B.

Net effect on the lead item's skeptical framing: **it still holds on the
substance** (peer review pending, no documented human verification of the ten
informal arguments), but it must be **re-sourced and re-worded**. The specific
quote "reaction, not verification" and the named Gowers/Bloom reactions in
round-02 were tied to the misidentified Understanding AI URL and are **not**
carried forward — they cannot be attached to a ten-advances-covering source I
opened. The corrected independent account for item 1 is **Simon Willison's
1 August 2026 post**, which actually covers the ten-advances release and does not
assert human verification.

Where this record is thin: the OpenAI announcement blog (Astra/$2,000) and the
May Erdős primary both 403 to automated fetch and were read via manuscript/GitHub
primaries and independent coverage; the MLQ News "peer review still pending"
account also 403s and is treated as gated corroboration, not read firsthand.

The five firm items, each with an openable primary:

1. **OpenAI publishes ten new results in mathematics and theoretical computer
   science, with Lean 4 certificates on GitHub** (blog and manuscript dated
   1-2 Aug 2026), credited to an internal "Astra" model. Distinct from the May
   Erdős unit-distance disproof.
2. **EU AI Act Article 50 transparency obligations enter application** (2 Aug
   2026). Carried forward from 02, unchanged.
3. **California AI Transparency Act becomes operative** (2 Aug 2026). Carried
   forward from 02, unchanged.
4. **Tesla and SpaceX commit $16.8 billion to "Terafab," a Texas semiconductor
   fab** (6 Aug 2026). Carried forward from 02, unchanged.
5. **SK hynix and Sandisk release the first High Bandwidth Flash (HBF) standard
   at FMS 2026** (4 Aug 2026). Carried forward from 02, unchanged.

The two round-01 marginals (NVIDIA/NAVER, EO 14409) remain retired; the two
broken commission candidates (FDA autonomous-diagnostic class; August frontier
model releases) remain broken. Neither is revived.

---

## Sources — grouped by item

### Item 1 (firm): OpenAI publishes ten results in mathematics and theoretical computer science with machine-checkable Lean proofs, 1-2 August 2026

```text
URL:         https://cdn.openai.com/pdf/ten-proofs-oai.pdf
Kind:        primary — OpenAI's own manuscript, "Ten Advances in Mathematics and
             Theoretical Computer Science," authored and hosted by OpenAI. Opened
             and read directly (front matter, abstract, contents, full-text search).
Establishes: The abstract states the results were "obtained by an internal OpenAI
             model." The ten results, verbatim from the abstract/contents:
             (1) high-dimensional sphere packing — the asymptotic strength of the
             Cohn-Elkies linear program is determined exactly, improving the general
             high-dimensional packing bound (first improvement to the general upper
             bound since 1978, per independent coverage); (2) binary and spherical
             codes — classical fixed-distance upper bounds improved by exponential
             factors; (3) non-sofic groups exist — an explicit non-sofic group is
             constructed, answering whether every countable group is sofic (open
             since Gromov, 1999); (4) Connes's rigidity conjecture — disproved, via
             infinitely many pairwise non-isomorphic property-(T) groups sharing one
             group von Neumann algebra; (5) arithmetic circuit complexity — permanent
             lower bounds; (6) quantum parallel repetition; (7) closest vector
             problem; (8) Ehrhart's volume conjecture; (9) multicolor Ramsey numbers;
             (10) extremal number conjectures (Erdos problems 146 and 180). The
             manuscript does NOT contain the string "Astra," does NOT state a
             "$2,000" compute cost, and frames the work as "advances," not as
             "solving ten open problems." NOTE: item (10)'s "Erdos problems 146 and
             180" are extremal-combinatorics problems and are NOT the Erdos
             unit-distance conjecture of the separate May 2026 event (see
             Contradictions).
Paraphrase:  OpenAI's own manuscript attributes the results to an unnamed internal
             model and presents them as ten advances, several of which resolve a
             named open question (non-sofic groups, Connes's conjecture) and several
             of which improve an existing bound.
Locators:    Title page; Abstract (items 1-10); Contents. 253 pages as read from the
             PDF (press/independent coverage reports "249"; treat 253 as the read
             count of this file).
Quote:       "We present a collection of results obtained by an internal OpenAI
             model, spanning mathematics and theoretical computer science."
             "An explicit nonsofic group is constructed, answering the longstanding
             question of whether every countable group is sofic."
```

```text
URL:         https://github.com/openai/ten-proofs
Kind:        primary — OpenAI's own repository of Lean 4 certificates for the ten
             results. Opened and read (README).
Establishes: Repository description: "Lean certificates accompanying ten proofs in
             mathematics and theoretical computer science." It carries Lean 4
             formalizations of the principal results (one .lean file per result:
             NonSoficGroup.lean, ConnesRigidity.lean, SpherePacking.lean, etc.), an
             Apache-2.0 license, and points to the manuscript on openai.com and a
             separate reasoning-walkthroughs document. Build requires Lean 4.32.0,
             mathlib, and Lake; the model itself formalized each argument, checked
             mechanically by the Lean 4 proof assistant with no human judgment in the
             loop. The exact "sorry" count was not visible in the README excerpt
             read; the presence of compiling Lean 4 certificates is what the
             repository establishes firsthand.
Paraphrase:  The formal artifacts are public and machine-checkable: the theorems, as
             stated in Lean, can be verified by anyone who compiles the repo. What
             the repo cannot establish is that each Lean statement faithfully encodes
             the informal theorem it claims to prove.
Locators:    Repository root README; license file (Apache-2.0); per-result .lean
             files.
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
Establishes: Per the blog and wide corroboration, OpenAI used this post to attribute
             the results to an internal version of its next major model family,
             "Astra," and put the compute cost of finding all ten results at "roughly
             $2,000" at Sol API rates. Neither claim appears in the manuscript.
Paraphrase:  The model name and the headline cost figure live only in the
             announcement post, not in the formal manuscript. A headline that states
             "Astra" or "$2,000" as fact is citing the blog, not the proofs.
Locators:    Post body (naming; cost sentence).
Quote:       (primary gated; naming and cost read via secondary — see below)
```

```text
URL:         https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/
Kind:        secondary — independent technical account by Simon Willison (byline:
             Simon Willison), dated 1 August 2026. Reports on the ten-advances
             release from outside OpenAI. Opened and read directly; URL resolves to
             its own page. THIS is the corrected independent account for item 1 (it
             replaces the misidentified Understanding AI/Erdos URL).
Establishes: Independent confirmation that OpenAI released the ten-advances
             manuscript, the Lean 4 certificates on GitHub (openai/ten-proofs), and
             the reasoning walkthroughs on 1 August 2026; that the work is credited
             to an internal version of "Astra"; and the ~$2,000-per-problem / under-
             $2,000 compute framing. On verification it says only that "the
             openai/ten-proofs repository has Lean 4 formalizations of their
             results" — it does NOT assert that any named mathematician worked
             through the informal arguments, and it references a separate cautionary
             essay on AI in mathematics. It therefore corroborates the release and is
             consistent with "Lean certificates compile; no documented human
             working-through of the informal proofs," without claiming human
             verification.
Paraphrase:  A careful independent write-up corroborates the artifacts, the Astra
             attribution, the cost framing, and the 1 August date, and confirms that
             the public verification is the Lean formalization — not a human check of
             the informal arguments.
Locators:    Post body.
Quote:       "The openai/ten-proofs repository has Lean 4 formalizations of their
             results."
```

```text
URL:         https://mlq.ai/news/openai-publishes-ten-claimed-math-advances-with-formal-peer-review-still-pending/
Kind:        secondary — independent news account (MLQ News) covering the
             ten-advances manuscript, headline "OpenAI publishes ten claimed math
             advances, with formal peer review still pending." NOTE: gated — returns
             HTTP 403 to automated fetch; treated as gated corroboration, not read
             firsthand. Byline not confirmable from the fetch; recorded as MLQ News.
Establishes: (Via the headline and consistent independent coverage of the same
             event.) The in-window verification status of the ten-advances item:
             full peer review of the underlying mathematical ideas and their
             originality has not yet occurred; the mathematical community is still
             working through the 249-page manuscript; the Lean-formalized proofs have
             not yet undergone community scrutiny beyond compiling. Researchers are
             urging caution pending independent verification.
Paraphrase:  Independent coverage of the ten-advances release consistently reports
             that peer review is pending and no independent human verification of the
             informal arguments has been completed in-window — the skeptical framing
             the lead item needs, sourced to the correct event.
Locators:    Headline and body (gated).
Quote:       (gated; framing read via headline and corroborating coverage)
```

Verification status of item 1, stated exactly (what is documented vs not):
- **Documented:** Lean 4 certificates are public and machine-checkable; the
  formalized theorems compile under Lean 4.32.0 + mathlib. As of the window, full
  peer review of the informal mathematical arguments has **not** occurred and no
  named mathematician is on record as having worked through and verified the ten
  results; the community is still reading the manuscript.
- **NOT documented (do not assert):** that humans verified the ten results (that
  belongs to the separate May Erdos event), and equally, any stronger "the math is
  wrong / the Lean statements misencode the informal claims" gap beyond the honest
  point that the Lean guarantee stops at the formal statement.

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
Paraphrase:  The Commission issued its Article 50 guidance thirteen days before the
             obligations applied, and paired it with a voluntary Code of Practice
             rather than a finalized technical marking standard. (20 July to 2 August
             is thirteen days; editor recomputed and corrected the derived count.)
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

Note on the "align with the EU" motive: round-02 carried it as unattributed
reported context; the editor cut it from the draft because neither cited primary
(AB 853 s5) nor CalMatters (s6) owns the claim. It is not asserted here.

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
             independent reporting frames a much larger potential total across future
             expansion phases, and notes the site draws water from the Gibbons Creek
             Reservoir rather than local groundwater. NOTE (editor): the specific
             "$119 billion" multi-phase figure did not surface on opening s9, which
             speaks only of "future expansion phases bringing total investment much
             higher." Treat "$119B" as verify-or-cut for the writer, not confirmed
             here.
Paraphrase:  A second independent account confirms the phase-one figure and the
             multi-phase ambition the one-line announcement omits; the exact
             multi-phase dollar total is not confirmed at this href.
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
             release from outside the vendors. NOTE: returns HTTP 403 to automated
             fetch (bot-block, not a dead link); resolves in a browser. Recorded as
             the source's own page.
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

- **TWO DISTINCT OpenAI math stories — do not reconflate (the lead-item break).**
  There are two separate OpenAI math events in 2026, and round-02 cited the wrong
  one for item 1.
  - *May 2026, OUT of window — Erdos unit-distance disproof.* OpenAI announced
    (~20 May 2026) that an internal reasoning model produced the first autonomous
    disproof of the Erdos unit-distance conjecture (an 80-year-old discrete-geometry
    problem); the counterexample beats the classical threshold by a polynomial
    factor, refined by Will Sawin (Princeton) to n^1.014. This result **was verified
    by human mathematicians**: a companion paper by nine mathematicians translated
    and checked the argument the same day. Kai Williams' Understanding AI piece,
    "OpenAI's math breakthrough played to AI's strengths"
    (https://www.understandingai.org/p/openais-milestone-math-breakthrough), covers
    THIS event and correctly states "human mathematicians verified the result." It
    is NOT about the ten-advances manuscript.
  - *1-2 August 2026, IN window — the ten-advances manuscript (item 1).* A
    different release: ten results across math/TCS credited to an internal "Astra"
    model, with Lean 4 certificates. For this one, only the Lean certificates are
    documented as checked (they compile); full peer review and human working-through
    of the informal arguments have not happened in-window.
  - *Why the confusion is easy and must be blocked:* both events involve
    Erdos-named problems. The ten-advances manuscript's item (10) cites "Erdos
    problems 146 and 180" (extremal combinatorics); the May event is the Erdos
    unit-distance conjecture (discrete geometry). Different problems, different
    events, different verification status. The writer must not attach the May
    event's human verification, the nine-mathematician companion paper, Will Sawin,
    or the Kai Williams quote to the August ten-advances item.

- **Round-02's s2 was misidentified — corrected.** Round-02 recorded the
  Understanding AI URL as "Timothy B. Lee, Understanding AI," quoted "What has
  happened so far is reaction, not verification," and attributed named Gowers/Bloom
  reactions to it. The URL is actually Kai Williams' article about the MAY Erdos
  event; that quote and those named reactions are not established by any
  ten-advances-covering source opened here and are NOT carried into item 1. The
  correct byline for that URL is **Kai Williams** (not Timothy B. Lee).

- **For the ten-advances item, verification is the number the vendor omits — and
  the skeptical framing holds, re-sourced.** The Lean 4 certificates make the
  formalized theorems machine-checkable: compile the repo and the stated theorems
  hold. That guarantee stops at the formal statement — whether each Lean statement
  faithfully encodes the informal claim, and whether the results survive peer
  review, is unsettled. Independent coverage of the ten-advances release
  consistently reports peer review is still pending and no independent human
  verification of the informal arguments has occurred in-window (Simon Willison
  confirms only that Lean formalizations exist; MLQ News headline: "formal peer
  review still pending"). The vendor's "trustlessly verifiable" framing is true of
  the formalization and not yet true of the mathematics as a whole. State it that
  way; do not import the May event's human verification, and do not claim a stronger
  error than "the Lean guarantee stops at the formal statement."

- **OpenAI's framing outruns its own manuscript.** The announcement blog names the
  model "Astra" and puts the cost at "roughly $2,000"; the manuscript I read does
  neither — it says "an internal OpenAI model" and calls the results "advances,"
  not solved open problems. Several of the ten are improved bounds (sphere packing,
  codes, circuit lower bounds), not the resolution of a yes/no question; two are
  genuine resolutions (a non-sofic group is constructed; Connes's rigidity
  conjecture is disproved). Attribute "Astra" and "$2,000" to the announcement
  post, not the proofs.

- **EU Article 50: obligation live, standard pending.** The machine-readable
  marking-and-detection duty for AI-generated content is legally in force from 2
  August 2026, yet the technical standard for how to mark is not finalized — the
  Commission offers a voluntary Code of Practice, and pre-existing generative
  systems get until 2 December 2026. Regulator and independent analysis agree on the
  dates; neither claims the standard is settled.

- **California vs EU scope.** Same operative date, different reach: EU Article 50
  covers chatbots, emotion recognition, deepfakes, and synthetic-content marking for
  all providers; California binds only generative providers above 1,000,000 monthly
  users and adds a public detection-tool duty the EU rule does not.

- **Terafab is a capex commitment, not a running fab.** The $16.8 billion is a
  first-phase investment announced 6 August with civil work only beginning; any
  larger multi-phase figure is potential, not committed (and the specific "$119B"
  did not surface at the Electrek href). Report it as a commitment and a
  groundbreaking, not as capacity that exists.

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
  card and benchmarks.

---

## Numbers

```text
Figure: 10 results; 249/253-page manuscript; ~$2,000 total compute (blog claim)
Owner:  OpenAI manuscript (results; 253 pages read from PDF, 249 in coverage);
        OpenAI blog (Astra name, cost)
Scope:  Ten advances in math/TCS by "an internal OpenAI model" (branded "Astra" in
        the blog); cost figure is the announcement post's (Sol API rates), absent
        from the manuscript. In-window verification: Lean certificates compile;
        peer review of the informal arguments still pending, no documented human
        working-through. (Distinct from the May Erdos unit-distance event, which
        nine mathematicians verified.)
```

```text
Figure: 2 August 2026 — operative date, EU AI Act Article 50 transparency duties
Owner:  Regulation (EU) 2024/1689, Art. 50 / European Commission guidelines
Scope:  Applies to in-scope systems regardless of when placed on market; marking
        obligation for pre-existing generative systems deferred to 2 Dec 2026.
        Guidelines published 20 July 2026 (thirteen days before application).
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
        3,000 jobs; ~100 million sq ft
Owner:  Texas Governor's release ($16.8B, $30M, 3,000, 100M sq ft)
Scope:  Grimes County, TX fab "Terafab" (Tesla + SpaceX); phase-one commitment,
        civil work beginning. Any multi-phase total is potential, not committed
        (specific "$119B" unconfirmed at the Electrek href — verify or cut).
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
Shows: That the formal artifacts are public and auditable — per-result .lean files
       (NonSoficGroup.lean, ConnesRigidity.lean, SpherePacking.lean, ...), Apache-2.0
       license. The visual argument is that the proofs are open and machine-checkable
       — which grounds the "Lean certificates compile" claim honestly, and visibly
       stops short of human verification of the informal arguments.
Crop:  A screenshot of the repo root file tree; retain the directory/file names and
       the license badge. No decorative rendering.
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
URL: https://www.understandingai.org/p/openais-milestone-math-breakthrough
     — "OpenAI's math breakthrough played to AI's strengths," by KAI WILLIAMS
     (May 2026, ~28 May). This is about the MAY Erdos UNIT-DISTANCE disproof, a
     DIFFERENT and OUT-OF-WINDOW OpenAI math event that human mathematicians
     verified (nine-mathematician companion paper; Will Sawin refinement). Round-02
     wrongly used it as the independent verification source for the August
     ten-advances item and misattributed it to Timothy B. Lee with a "reaction, not
     verification" quote it does not carry. Discarded for item 1; the correct
     independent account is Simon Willison's 1 Aug 2026 post.
```

```text
URL: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
     — OpenAI's own announcement of the MAY 2026 Erdos unit-distance disproof
     (403s to automated fetch; resolves in a browser). Primary for the May event,
     NOT for the August ten-advances item. Recorded here so the two events stay
     separate; not cited for item 1.
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
URL: aggregators/SEO blogs (digitalapplied, techwafer, techdogs, reapi, nexforce,
     nerdleveltech, developersdigest, explainx, techtimes, aiweekly, thenextweb,
     datacamp, analyticsinsight, forbes/markman, techjournal, digg, and similar)
     — no primary authorship over any claim; used only to locate candidates and to
     read the framing/verification status of the OpenAI announcements. Cited as
     primary for nothing. MLQ News is recorded above as gated corroboration of the
     "peer review still pending" status only.
```
