# Evidence record: daily-brief/2026-11-12 (researcher 01)

The record supports six items. Four rest on the document that owns the claim:
the Federal Register text of USDA's SNAP proposal, the Justice Department's
indictment release, Google's Decisions API post, and the e-means paper on arXiv
with its project page. The Word of the Day rests on Merriam-Webster and a Harvard
Crimson report printed the morning after the 1924 prize was announced. The
Mississippi Senate result rests on AP's report through PBS, with NBC News for
the concession and the Senate count. No certified vote total was found. The thin
points: the Mississippi margin exists only as unofficial reported counts that
differ by a few hundred votes; the indictment release does not say whether two
of the three defendants are in custody; every Gemini Decision 1 and e-means
performance figure is reported by its authors, with no independent check; and
the e-means paper went up on 6 November, six days before this edition. The
feature commission's topic was not in my inputs, so I could not check either
technology item against it. The Nvidia board story is the runner-up most likely
to need a swap: as of this record no outcome had been announced, and if one
comes before drafting it outranks the indictment.

## Selection

Prior coverage checked with `nb history --series daily-brief` (4 to 11
November) and `nb history <term>` for each candidate.

### Word of the Day: scofflaw

- Why: a coinage with a datable birth and named coiners. Delcevare King ran a
  $200 contest for a word to shame drinkers who broke Prohibition, and the
  judges announced on the night of 15 January 1924 that two Massachusetts
  entrants, Henry Irving Dale and Kate L. Butler, had sent in "scofflaw"
  independently. It comes from law and Prohibition, a different field from the
  last eight words (psychology/ethology, burlesque, scholarship, literature,
  philosophy, anthropology, politics). `nb history scofflaw`: no coverage in any
  series. Following the orchestrator's instruction, it is not grawlix or
  spoiler.
- Risk: more well-read Americans will know this word than knew phatic or
  sphexish. Its story is the reason to pick it.
- Runners-up:
  - snowclone (noun): coined on Language Log in January 2004 by the economist
    Glen Whitman, after Geoffrey Pullum asked readers to name the "Eskimos have N
    words for snow" kind of reusable cliché template. `nb history snowclone`: no
    coverage. I did not open its primaries.
  - tachyon (noun): Gerald Feinberg's 1967 Physical Review paper on
    faster-than-light particles. `nb history tachyon`: no coverage. The story is
    thinner. Primaries not opened.
- Rejected after `nb history`: petrichor (the-word, 19 July), mondegreen
  (word-of-the-day, 26 July), bafflegab (daily-brief, 1 November). Also already
  used: boondoggle, gerrymander, maverick, boycott, serendipity.

### News 1 (suggested lead): USDA proposes cutting SNAP categorical eligibility

- Why: the largest consequence in the window. USDA's own estimate is that 6.3
  million people in 3.2 million households would lose SNAP benefits once the
  rule reaches full effect in FY 2029, with $44.649 billion less in federal
  benefit spending over FY 2027 to 2031. It was published 10 November, the
  comment period closes 10 December, and the source is the Federal Register text
  itself. Not covered before (`nb history SNAP`: no news coverage).
- Runners-up: the Nvidia board's meeting on whether to remove Jensen Huang (see
  News 3); a unanimous appeals-court panel ruling on 10 November that the
  administration illegally fired the head of Voice of America (NYT via Just
  Security; not opened).

### News 2: Scott Colom defeats Sen. Cindy Hyde-Smith in Mississippi

- Why: AP called the race on 11 November after eight days of counting
  affidavit and absentee ballots. NBC reports that Democrats will hold at least
  55 Senate seats and that Alaska is the only Senate race still uncalled. Colom
  will be the first Black senator from Mississippi since Reconstruction. The
  4 November brief reported seven Democratic Senate gains and did not mention
  Mississippi (`nb history Colom`, `nb history Mississippi`: no coverage).
- Runners-up: Jim Jordan elected House Republican leader for January 2027,
  beating Steve Scalise by 33 votes (Axios via Just Security, 10 November; not
  opened); a federal judge refusing to dismiss Trump's defamation suit against
  the BBC (Politico via Just Security, 11 November; not opened).

### News 3: Three Iran-backed operatives indicted over nearly 20 attacks and a plot at RAF Fairford

- Why: an eight-count superseding indictment unsealed 10 November in the
  Southern District of New York. It ties the IRGC and Kata'ib Hizballah to the
  spring 2026 attacks on Jewish targets in Europe and to a September plot
  against a British base where US forces were stationed, during the Iran war.
  The release is the primary. Not covered before (`nb history Iran-backed`,
  `nb history Kata'ib`: nothing on this case).
- Runner-up, possible swap: Nvidia. Reuters, the WSJ and CNBC report that the
  board met late on 11 November to decide whether to remove Huang, after the
  NYT reported a second relationship, this one with Kimberly Powell, Nvidia's
  vice president of health care. The board's investigation was the 9 November
  item. The new development is the meeting and its sourcing. It rests on
  anonymous sources, and no outcome had been announced as of this record:
  nothing on Nvidia's newsroom after the 10 November statement, and no 8-K on
  EDGAR since 6 November. If the board announces a decision before drafting,
  this outranks the indictment. Nvidia's own release puts Q3 results on 17
  November.

### Technology 1: Google's Gemini Decisions API scores options in one pass

- Why: released 11 November, a capability that changes how a system builder can
  wire routing, tool choice and policy checks. Gemini Decision 1 scores a
  closed set of options in one forward pass and returns calibrated
  probabilities. It generates no text, and output tokens are not billed. The
  post is the primary. `nb history "Decisions API"`: no coverage.
- Runners-up: Meta's Muse Ember 1.0 (9 November, research.meta.ai), a small
  hosted model priced at $0.10/$0.50 per million input/output tokens, all
  benchmarks self-reported and several "Meta internal evaluation"; AWS Emulator
  (github.com/aws/aws-emulator), a CC0-licensed local emulator of AWS APIs. Its
  page gives no release date and its Releases section is empty, so I could not
  date it to the window.

### Technology 2: e-means replaces Lloyd's k-means in a tenth of the epochs

- Why: a research result for the audience's own tools, with the code shipped
  in Faiss as `faiss.contrib.e_means`. Meta FAIR and ENPC authors replace Lloyd
  iterations with mini-batch exponential-moving-average updates and fix the
  batch size and decay rate from fitted scaling laws, with no sweep. They report
  beating Lloyd's 25-epoch loss in 1.4 to 2.6 epochs. Posted to arXiv on 6
  November and on the Hacker News front page on 9 November.
  `nb history e-means`: no coverage.
- Caveat: six days old. If the orchestrator holds "last few days" tighter, swap
  in Muse Ember (9 November).
- Runner-up: Amazon's Strands Decider post (10 November, strandsagents.com),
  which says Amazon saves "millions" by replacing Sonnet 4.6. Not opened. Its
  scoring-model premise also overlaps the Decisions API item.

## Sources

### Word of the Day

```text
URL:         https://www.merriam-webster.com/dictionary/scofflaw
Kind:        secondary (reference dictionary; it reports the word's history and did not take part in the contest). It is the standard owner of the definition and pronunciation.
Establishes: part of speech (noun), pronunciation \ˈskäf-ˌlȯ, ˈskȯf-\, definition "a contemptuous law violator", first known use 1924, formation from the verb scoff and the noun law. Repeats the contest story: King, a wealthy Massachusetts Prohibitionist, wanted a word to shame lawless drinkers; Henry Dale and Kate Butler split the $200 prize; critics mocked the word at first; it widened to cover anyone who breaks any law.
Paraphrase:  as above.
Locators:    headword entry; "First Known Use"; "Etymology"; the word-history note below the definition.
Quote:       "a contemptuous law violator" (definition text, wording as reported by fetch)
```

```text
URL:         https://www.thecrimson.com/article/1924/1/16/scofilaw-will-make-lawless-drinker-cringe/
Kind:        primary for the timing and terms of the award: a contemporary report printed the morning after the judges announced it, carrying the contest's figures. (King was a Harvard graduate, class of 1895, so the paper had a reason to follow him; it is not the sponsor.)
Establishes: the announcement came on the night of 15 January 1924 ("made last night by the judges"); over 25,000 words from 6,234 people; the term "occurred to two individuals", so the $200 was divided between Henry Irving Dale of Andover and Miss Kate L. Butler of Fields Corner; King at once opened a second $200 contest for the five best 100-word statements of why an illegal drinker should be called a "scofflaw", closing 31 January.
Paraphrase:  as above. The piece opens with a mock dictionary entry: "Scofflaw, n. One who drinks liquor made or obtained illegally."
Locators:    paragraphs 1 to 4 under the dek "Delcevare King '95 Now Offers Another $200 Prize..."
Quote:       "From among over 25,000 words submitted by 6234 people, the winning term was chosen, according to the announcement of the award made last night by the judges."
Quote:       "an epithet of bitter opprobrium applicable to a lawless drinker"
Note:        the headline misprints the word as "SCOFILAW". The body spells it "Scofflaw". Do not copy the headline spelling.
```

```text
URL:         https://www.thecrimson.com/article/1924/2/16/scofflaw-prize-essayist-got-training-at/
Kind:        primary (contemporary report of the second contest's result). Optional extra color.
Establishes: Harold Bisbee, Harvard class of 1900, won the $100-in-gold first prize in the essay contest. His essay was made public on 16 February 1924.
Locators:    paragraphs 1 and 2.
Quote:       "The willingness with which obedience responds to enforcement is the acid test of true democracy" (from Bisbee's essay, as the Crimson quotes it)
```

```text
URL:         https://www.thecrimson.com/article/1924/1/29/fine-says-delcevare-king-of-advocate/
Kind:        primary (contemporary interview quote from King).
Establishes: the Harvard Advocate answered with its own contest for a word stigmatizing the Drys. King welcomed it ("That's fine! Let us turn on the light and get people thinking!") and offered no word for the "Anti-scofflaw".
Locators:    paragraphs 1 to 3.
```

### News 1: SNAP categorical eligibility

```text
URL:         https://www.federalregister.gov/documents/2026/11/10/2026-22936/supplemental-nutrition-assistance-program-reforming-categorical-eligibility
             (PDF of record: https://www.govinfo.gov/content/pkg/FR-2026-11-10/pdf/2026-22936.pdf)
Kind:        primary. USDA's own proposed rule in the Federal Register, and USDA owns the impact estimates.
Establishes: Proposed rule, "Supplemental Nutrition Assistance Program: Reforming Categorical Eligibility", from the Agriculture Department's Food and Nutrition Administration (agency name as the Federal Register lists it), 91 FR, No. 216, Tuesday 10 November 2026, starting page 72454, docket FNA-2026-0661, RIN 0584-AF10. Comments close 10 December 2026. Today households are categorically eligible for SNAP if they receive TANF-funded cash or non-cash/in-kind benefits ("broad-based categorical eligibility", BBCE). The proposal limits categorical eligibility to households receiving TANF "assistance" as defined at 45 CFR 260.31. Impact estimates: 16.9% of participating SNAP households (17.6% of participants) would lose benefits because their income or resources exceed the federal statutory limits, which is 3.2 million households containing 6.3 million individuals in FY 2029, the first year of full effect; federal SNAP benefit spending falls about $44.649 billion over FY 2027 to 2031; about 1.78 million children would lose categorical eligibility for free school meals, though about 97% would remain eligible on income: about 1.66 million would still get free meals, 93,000 would move to reduced-price and 28,000 would pay full price. The preamble recalls the 2019 attempt (84 FR 35570), which the Biden administration withdrew on 10 June 2021 (86 FR 30795).
Paraphrase:  as above. USDA's justification: in FY 2024, 11.5% of participating households (2.5 million households, 5.4 million people) had resources above the SNAP limit, and 5.4% (1.2 million households, 2.0 million people) had incomes above the federal gross or net limits. The preamble also cites millionaires receiving SNAP.
Locators:    Summary/abstract; "Background" section; Regulatory Impact Analysis summary, end of page 72459 in the PDF (6.3 million, $44.649 billion); school-meals paragraph at the top of page 72460; FY 2024 shares in the "Background" discussion of BBCE.
Quote:       "This represents 3.2 million households containing 6.3 million individuals in FY 2029, the first year the proposed rule is expected to reach its full effects."
```

### News 2: Mississippi Senate

```text
URL:         https://www.pbs.org/newshour/politics/scott-colom-wins-senate-election-in-mississippi
Kind:        secondary. An AP report (Bill Barrow and Sophie Bates, Jackson, Miss.) republished by PBS NewsHour, 11 November 2026, 6:01 p.m. EST. AP's race call is the standard US call, but the vote count belongs to Mississippi's election officials, and no certified total was found.
Establishes: AP called the race on Wednesday 11 November for Democrat Scott Colom, 43, a local prosecutor, over Republican Sen. Cindy Hyde-Smith, 67, after a prolonged count of absentee and provisional (affidavit) ballots. Colom would be Mississippi's first Black US senator since Reconstruction. The last Democrat elected to this seat was elected in 1947, a segregationist.
Paraphrase:  as above. Colom campaigned on the economy, beef prices, the Iran war, tariffs and Hyde-Smith's record.
Locators:    paragraphs 1 to 4. The fetched page gave no vote totals.
```

```text
URL:         https://www.nbcnews.com/politics/2026-election/scott-colom-mississippi-senate-election-win-democrat-hyde-smith-rcna605729
Kind:        secondary (NBC News report, 11 November 2026, 5:59 p.m. EST). Used for the concession and the Senate count, which the AP piece does not give.
Establishes: NBC projected Colom the winner. Hyde-Smith conceded in a video Wednesday evening and, per Colom's campaign, by phone. Democrats will hold at least 55 Senate seats next year. Alaska is the only Senate race still uncalled. Colom will be the first Democrat Mississippi has elected to the Senate since 1982.
Quote:       Hyde-Smith: "While this is not the outcome we worked for or hoped for, I respect the decision of Mississippi voters."
Quote:       Colom: "We were never a lost cause. We were a betrayed cause."
```

```text
URL:         https://www.yahoo.com/news/politics/article/mississippi-senate-results-scott-colom-narrowly-defeats-cindy-hyde-smith-flipping-another-seat-for-democrats-in-midterm-elections-232119638.html
Kind:        secondary (Yahoo News, Andrew Romano, updated 12 November 05:17 UTC). Only for the AP percentages, which the PBS copy lacked.
Establishes: per AP figures, Colom 49.2%, Hyde-Smith 48.7%. At the end of election night the two were 65 votes apart. In Alaska, with 84% counted, Democrat Mary Peltola led Republican Sen. Dan Sullivan 48.9% to 47.3% (AP figures).
```

### News 3: Iran-backed operatives indictment

```text
URL:         https://www.justice.gov/opa/pr/three-iranian-backed-operatives-indicted-their-roles-nearly-20-terrorist-attacks-and
Kind:        primary for what the government charges (DOJ Office of Public Affairs, Tuesday 10 November 2026). The facts are allegations: DOJ is a party to the case.
Establishes: an eight-count superseding indictment unsealed 10 November (SDNY) charges Mohammad Baqer Saad Dawood al-Saadi, 32, a dual Iranian-Iraqi national; Mohsen Mohajeri, 48, an Iranian national and IRGC operative; and Mohammad Ali al-Hassani, 35, an Iraqi national, with terrorism offenses in support of Kata'ib Hizballah and the IRGC, both designated foreign terrorist organizations. Alleged: involvement in nearly 20 attacks and attempted attacks in Europe and the US, among them 18 spring-2026 attacks claimed in Europe under the front name Harakat Ashab al-Yamin al-Islamiya (HAYI), seven of them in the UK, including arsons, explosives and a near-fatal stabbing in London of two Jewish men, one a dual US-British citizen; and an attempt by al-Saadi to target a Manhattan synagogue. Most recently, al-Hassani allegedly directed a plot at RAF Fairford in September 2026, while US forces were stationed there: surveillance paid for on 22 August, vans disguised with fuel-delivery and pool-supply decals, and on 26 September three vans, some carrying fuel barrels, sent toward the base. At least two met a security roadblock. UK police recovered the vans and arrested the occupants early on 27 September. Al-Saadi, arrested abroad on or about 1 May and held in New York awaiting trial on charges brought in May, allegedly passed coded messages to the others through family phone calls ("give him money so we can do it", 24 September).
Paraphrase:  as above. Al-Hassani and Mohajeri were "in Iran at the time" of the Fairford plot. The release does not say whether either is in custody.
Locators:    lead paragraph; "According to the allegations..." section; the Fairford paragraphs dated Aug. 22, Sept. 26 and Sept. 27; the paragraph on al-Saadi's jail calls; the age and citizenship paragraph near the end.
Quote:       Attorney General Todd Blanche: "Anyone who plans a terrorist plot on a military base housing American servicemembers will be prosecuted by the United States government."
Note:        FBI Director Kash Patel's quote in the release calls the base "RAF Fairfield". The release's own text and every other passage say RAF Fairford. Do not quote Patel's sentence without that correction.
```

### Technology 1: Gemini Decisions API

```text
URL:         https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
Kind:        primary. Google's own announcement of its own product, so every performance figure is self-reported.
Establishes: dated 11 November 2026. A new Gemini API endpoint, the Decisions API, powered by a new model, Gemini Decision 1 (gemini-decision-1), for closed-set decisions: tool selection, policy checks, model routing, context grading. One multimodal input (text, images, audio, video, PDFs; up to 256K tokens) plus up to 1,000 independent questions per request, of three types: yes/no with a probability, multiple choice (2 to 255 options), and ordered rubric scoring, each answer with a 0-to-1 confidence. Priced at $0.10 per million input tokens with no output tokens billed; a no-cost tier in AI Studio; Google Cloud support "coming soon"; integrations rolling out through OpenRouter, LangChain, Vercel, LiteLLM and others.
Paraphrase:  as above. Google claims median model compute of 50 to 100 ms and 150 to 250 ms end to end, nearly flat from 1 to 100 questions, for contexts up to 16K tokens; the lowest calibration error on its own suite (routing, reasoning, ranking, multimodal); and "nearly 5x" lower cost than Gemini 3.5 Flash-Lite with the Interactions API on that suite.
Locators:    opening paragraph; "Strong performance and calibration" section; pricing and availability sections.
Quote:       "Rather than generating answer text token by token, Gemini Decision 1 scores your candidate options in a single forward pass, returning probabilities and confidence scores in 150-250 ms end-to-end latency at $0.10 per 1M input tokens with zero output tokens billed."
```

### Technology 2: e-means

```text
URL:         https://arxiv.org/abs/2611.09501
Kind:        primary (the authors' paper). Results are self-reported and not yet peer reviewed, as far as the listing shows.
Establishes: "e-means: outperforming k-means (in one-tenth the epochs)", by Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy, Hugo Touvron, David Picard, Matthijs Douze and Hervé Jégou, submitted 6 November 2026 14:22 UTC. Method: mini-batch updates with an exponential moving average replace Lloyd iterations, with scaling laws for how decay rate and batch size affect final loss, which gives a formula for both and no hyperparameter sweep. Claims: beats Lloyd's 25-epoch loss in 1.4 to 2.6 epochs across many embedding datasets, which is 10 to 45x GPU wall-clock speedups over state-of-the-art k-means implementations; often beats k-means++; partitions DINO10B (10 billion DINO embeddings) into 16 million clusters in 2.5 epochs, below Lloyd's loss at 25 epochs.
Locators:    abstract; comments field (code and website links).
Quote:       "On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations."
```

```text
URL:         https://e-means.github.io/
Kind:        primary (the authors' project page). Used for the implementation detail and baselines.
Establishes: shipped in Faiss as faiss.contrib.e_means. Components: new initialization, cosine-scheduled step decay, a finalization stage, dead-cluster revival. Baselines: 10 to 45x end-to-end against Flash-KMeans on GPU and 8 to 15x against Faiss on CPU. On 11 VIBE embedding datasets it matches Lloyd's 25-epoch test error in 1.6 to 2.4 epochs. The authors moved to moving averages because gradient-descent centroid updates were unstable at large learning rates.
Locators:    headline claim; results figures; "dead clusters" ablation (DEEP, 1M vectors, k = 16,384: 47 dead clusters with proportional split, 2,343 with EnCodec-style resampling, 4,313 with revival off).
Quote:       "e-means delivers a ~10× speedup in both epochs and wall-clock time while achieving lower loss."
Note:        Faiss code path https://github.com/facebookresearch/faiss/tree/main/contrib/e_means returned 403 to my fetch (gated, not confirmed dead). Cite the arXiv abstract for claims.
```

### Runner-up records (opened, not selected)

```text
URL:         https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board
Kind:        primary (Nvidia board statement, 10 November 2026).
Establishes: the independent directors retained former acting SDNY US Attorney Joon H. Kim and Wachtell, Lipton, Rosen & Katz for the investigation announced on Sunday 8 November. As of this record, no later statement is on the newsroom.
```

```text
URL:         https://nvidianews.nvidia.com/news/a-message-to-our-company
Kind:        primary (Huang's 8 November email to staff, published by Nvidia).
Establishes: Huang's admission ("I was unfaithful to my wife") and his support for the board's investigation. Already covered on 9 November.
```

```text
URL:         https://www.france24.com/en/technology/20261112-nvidia-board-to-decide-whether-to-oust-longtime-ceo-jensen-huang
Kind:        secondary (France 24 with Reuters, 12 November).
Establishes: repeats Reuters's single source that the board met late on 11 November to decide whether to oust Huang; the WSJ report that it was preparing to; the NYT report of a relationship with Kimberly Powell, VP of health care, citing five people who worked at the company, which Reuters could not verify. Shares fell more than 8% in extended trading. Under the bylaws a majority of directors can remove Huang "with or without cause"; 10 of 11 directors are independent; Huang owns about 3.6% of the stock.
```

```text
URL:         https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html
Kind:        secondary (CNBC, 11 November 5:06 p.m. ET). 403 to curl, read via WebFetch: gated, not dead.
Establishes: CNBC confirmed late Wednesday that the board was meeting. Shares fell more than 9% after hours. No outcome reported.
```

```text
URL:         https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873
Kind:        primary.
Establishes: Q3 FY2027 results call on Tuesday 17 November 2026, 2 p.m. PT.
```

```text
URL:         https://research.meta.ai/blog/muse-ember
Kind:        primary (Meta's announcement; self-reported benchmarks).
Establishes: Muse Ember 1.0, 9 November 2026, via Muse Code, the Meta Model API, Google Cloud and Oracle Cloud; $0.10/$0.50 per million input/output tokens up to 200K-token prompts; 1M context. No parameter count or license stated. Several benchmarks are "Meta internal evaluation". It trails Claude Haiku 5.5 on FrontierCode 2.0-AA (27.2% against 34.9%).
```

```text
URL:         https://github.com/aws/aws-emulator
Kind:        primary (AWS's repository).
Establishes: "a local emulator of the AWS APIs" for testing without an AWS account, CC0-1.0, telemetry on by default, "does not take PRs", not for production or security testing. No release or date on the page.
```

```text
URL:         https://www.justsecurity.org/164111/early-edition-november-11-2026/
Kind:        secondary (news digest). Used only to scan the 10 to 11 November news. Cited for nothing.
```

## Contradictions

- e-means epoch range: the arXiv abstract says Lloyd's 25-epoch loss is beaten
  in "1.4 to 2.6 epochs" across embedding datasets. The project page says "1.2
  to 3" epochs in one figure and "1.6 to 2.4" on 11 VIBE datasets. These are
  different dataset sets. Use the abstract's 1.4 to 2.6 and its "10-45x" GPU
  figure.
- Mississippi margin: CNBC reported a 4,404-vote lead at 2:30 p.m. on 11
  November, and MS NOW reported 4,669 the same day (both from search summaries;
  not opened). Neither is certified. Use AP's percentages (49.2% to 48.7%), not
  a vote margin.
- "First Democrat" claims: AP says the last Democrat elected to this seat was
  elected in 1947. NBC says Colom is the first Democrat Mississippi has elected
  to the Senate since 1982. They agree: one is the seat, the other the state.
  Do not swap them.
- Nvidia earnings date: NBC (search summary) gave 20 November. Nvidia's own
  release says 17 November. Nvidia owns it.
- RAF "Fairfield" in the FBI Director's quote against "Fairford" everywhere else
  in the same DOJ release (see the source note).
- Against the SNAP rule's framing: USDA's own impact analysis says about 97% of
  the 1.78 million children losing categorical school-meal eligibility stay
  eligible on income. That cuts against any line saying 1.78 million children
  lose free meals. Per USDA, 28,000 would pay full price.
- I looked for a contradiction of the indictment's core allegations. Iran
  denies involvement (BBC via Just Security; not opened), and al-Saadi has
  pleaded not guilty to the earlier May charges (search summary). Nothing
  disputes the facts the DOJ filed. The allegations are untested.

## Numbers

```text
Figure: 6.3 million individuals in 3.2 million households would lose SNAP
Owner:  USDA proposed rule, 91 FR (10 Nov 2026), RIA summary, p. 72459
Scope:  FY 2029, first year of full effect; 16.9% of participating households, 17.6% of participants

Figure: $44.649 billion reduction in federal SNAP benefit spending
Owner:  same
Scope:  five years, FY 2027 to FY 2031

Figure: 1.78 million children lose categorical free-meal eligibility; ~97% keep income eligibility; 28,000 would pay full price
Owner:  same, p. 72460
Scope:  school meals programs, rule at full effect

Figure: comment deadline 10 December 2026
Owner:  Federal Register document 2026-22936

Figure: Colom 49.2%, Hyde-Smith 48.7%
Owner:  AP figures (as reported by Yahoo News); the official count belongs to Mississippi election officials, not certified
Scope:  3 November 2026 general election, count as of AP's call on 11 November

Figure: Democrats at least 55 Senate seats next year; Alaska the only uncalled Senate race
Owner:  NBC News, 11 November
Scope:  119th to 120th Congress transition, as of 11 November evening

Figure: eight counts; three defendants; nearly 20 attacks and attempted attacks; 18 HAYI-claimed attacks in Europe in spring 2026, 7 in the UK
Owner:  DOJ release, 10 November
Scope:  allegations in the superseding indictment

Figure: up to 1,000 questions per request; 256K-token input; 2 to 255 choices; $0.10 per 1M input tokens, 0 output tokens billed; 150 to 250 ms end to end
Owner:  Google, 11 November (self-reported)
Scope:  latency figures apply to contexts up to 16K tokens

Figure: 1.4 to 2.6 epochs to beat Lloyd's 25-epoch loss; 10 to 45x GPU wall-clock speedup; DINO10B to 16 million clusters in 2.5 epochs
Owner:  Bessa et al., arXiv:2611.09501 (self-reported)
Scope:  "a wide array of embeddings datasets"; speedup against "state-of-the-art k-means implementations" (the project page names Flash-KMeans on GPU)

Figure: over 25,000 words from 6,234 people; $200 prize split two ways
Owner:  Harvard Crimson, 16 January 1924, reporting the judges' announcement
Scope:  King's 1923 to 1924 contest
```

## Limits

- No certified Mississippi vote total or exact margin. Only AP's percentages
  and two conflicting unofficial leads.
- The DOJ release does not say whether Mohajeri and al-Hassani are in custody.
  It says only that both were in Iran at the time of the Fairford plot. The
  writer must not say all three are held.
- No independent check of any Gemini Decision 1 latency, calibration or cost
  claim, or of the e-means speedups. Both must be attributed to their authors.
- e-means was posted on 6 November, six days old. That is within "the last
  few days" only on a loose reading.
- The feature's topic was not in my inputs, so I could not confirm that
  neither technology item overlaps it. Neither overlaps the deadly-triad
  lesson.
- Nvidia's board outcome was unknown at the time of this record. If it lands,
  the News 3 slot should be reconsidered.
- I could not open the Boston Herald's January 1924 announcement (cited in
  secondary accounts as the 16 January paper) or a Chronicling America scan;
  the loc.gov search is behind a Cloudflare challenge. The Crimson's
  same-morning report stands in for it. Merriam-Webster's "first known use
  1924" fits it.
- The Word of the Day's first sentence in the series form needs a definition.
  Merriam-Webster's is "a contemptuous law violator". The 1924 sense was
  narrower: one who drinks illegal liquor (the Crimson's mock entry).

## Source assets

```text
Asset: DOJ release images: a 2024 photo of al-Saadi before machine guns and a US map with a redacted "legitimate targets" list; an April video still of al-Hassani and Mohajeri planning; a still of the London synagogue attack video
Shows: the government's own exhibits for the allegations
Crop:  not recommended for a three-minute brief. If used, keep DOJ's redactions and caption it as a government exhibit of allegations.
```

```text
Asset: Federal Register PDF, p. 72459, the Regulatory Impact Analysis summary paragraph
Shows: USDA's own 6.3 million / $44.649 billion estimate in print
Crop:  keep the full sentence with "FY 2029, the first year..." so the time scope travels with the number
```

```text
Asset: e-means project page, the loss-against-epochs plot comparing e-means with Lloyd
Shows: the crossing point where e-means passes Lloyd's 25-epoch loss within about two epochs
Crop:  keep the axes, the legend and the Lloyd 25-epoch reference
```

Gemini Decisions API post: None found beyond product graphics and a vendor
benchmark chart with no methodology. Merriam-Webster, the Crimson, AP/PBS and
NBC: None found.

## Discarded

- https://www.justsecurity.org/164111/early-edition-november-11-2026/: digest used for scanning only; each item goes to its own source.
- https://www.pbs.org/newshour/show/november-11-2026-pbs-news-hour-full-episode: segment list only, no reporting text.
- Hegseth impeachment (House referral, 10 and 11 November): covered on 11 November. No new development found.
- Nvidia board meeting (WSJ, Reuters, CNBC, France 24): held as runner-up. Unresolved, anonymous sourcing.
- AWS Emulator (github.com/aws/aws-emulator): no release date on the page, so I could not place it in the window.
- Muse Ember (research.meta.ai/blog/muse-ember): held as runner-up. Self-reported, several internal-only evaluations.
- AlphaProof Code and Claude Fable/Mythos 5.2 (Hacker News, 9 and 10 November): covered on 11 and 10 November.
- Tim Peters's death (discuss.python.org, 11 November): an obituary, not a technology development under the series rules.
- petrichor, mondegreen, bafflegab: previously used, per `nb history`.
