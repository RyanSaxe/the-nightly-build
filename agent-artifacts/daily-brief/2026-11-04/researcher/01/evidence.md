# Evidence: daily-brief/2026-11-04 (researcher 01)

The record supports all six items. For the Senate, the AP call is confirmed only through outlets
that carry AP's own wording or AP's data feed. The AP pages themselves (apnews.com live page and
articles) returned 403 to this environment and are recorded as gated. AP had called the Senate for
Democrats by about 11:40 p.m. ET on 3 November. As of 06:22 UTC on 4 November it had not called the
House. NBC News projected the House for Democrats at 10:08 p.m. ET. NPR, from its own tally of AP
race calls, says Democrats hold both chambers. The House figures were moving by several seats every
ten minutes during research, so the writer must print a stated time and the editor should expect
them to be stale. The second news item (Missouri's Proposition A) rests on an AP call reported by St.
Louis Public Radio, not on the Secretary of State's canvass. The third (Israel aid) is Trump's claim
on Fox & Friends; nobody in Israel or the White House confirmed it, and every report notes that
Congress appropriates the money. The word's coinage is documented, but two sources credit
different people. The two technology items are primary documents from their authors. Neither is a
single big-company deal, hack or benchmark. The feature desk's topic had not arrived when I chose
them, so I list two alternates.

## Item choices

- **Word: psephology.** It is a coinage with a documented story and a named Oxford circle behind it.
  It names the study of elections on the morning after the midterms, and few US readers know it.
  Considered: kakistocracy (dropped because it reads as a partisan jab the day after an election),
  scofflaw (1924 contest coinage, better known), factoid (Mailer, too familiar to this audience).
  None of the four has run in the archive (`nb history` returned no matches).
- **News 1: control of Congress.** The commission requires it. Attribute every call to the desk
  that made it.
- **News 2: Missouri voters reject Proposition A.** This is the first referendum defeat of a
  map that Trump pushed for mid-decade, and it decides the lines for the 2028 House elections. That
  gives it national weight under the commission's bar for state results. Amendment 3 (the abortion
  ban) failed on the same ballot and fits in one clause. It is a new development on a story the brief
  last ran on 28 September (Supreme Court stay). Chosen over the Supreme Court argument in *St. Mary
  Catholic Parish v. Roy*, which was only an argument (no decision) and would bring back the
  court-led pattern the commission wants broken.
- **News 3: Trump says US aid to Israel will stop at the end of 2026.** This is a stated reversal of
  a $3.8 billion-a-year commitment, made on 3 November, and the brief has not covered it. Chosen over
  Greenland's ratification of the trilateral security deal, which is concrete but smaller for a US
  reader. The Iran strikes of 2 November are a running story the 3 November brief already covered,
  and I found no new development since then.
- **Tech 1: Hugging Face's Model Integration Contracts, and the UMT5 bug they caught.** An
  audience that trains with Transformers can act on this. HF says a change that turned on SDPA for T5
  let UMT5's decoder see future tokens from 30 July to 28 September 2026. Anyone who fine-tuned UMT5
  on main or a release in that window should check. It is a testing method plus a disclosed
  regression. It is not a deal, a hack or a benchmark.
- **Tech 2: StateBench (Allen Institute for AI, NYU, TTIC).** A research result with a proof and a
  benchmark that separates kinds of state tracking. Directly trained Gated DeltaNet and hybrid
  models generalize far past their training length, transformers never learn the hardest level, and
  four frontier models fall to chance on the harder levels at long inputs. It is a benchmark, but
  it is an academic one covering several companies' models, not one company's launch.
- **Spare news: Greenland's parliament approves the US-Denmark-Greenland security agreement**
  (3 November, 16-0 with seven abstentions).
- **Spare tech 1: NVIDIA open-sources Attribution**, a rule-based tool that traces distributed
  training failures to a root cause (blog 2 November).
- **Spare tech 2: Cloudflare's targeted DNS zone builds** halve change-to-edge delay and cut peak
  memory 85% (blog 2 November). Not ML. Use it only if both ML items fail.

Rejected tech candidates (possible feature topics, or not usable): Binance's $6.3 billion security
issue (single-company hack, and dated 30 October); DoorDash's $17 billion Instacart offer
(single-company deal, 29 October); OpenAI's LifeVal (single-company benchmark); Simon Willison's
post on Qwen 3.8 interpreting model weights (too close to the 3 November GPT-6 Astra item); vLLM
0.33.0 (released to PyPI 2 November 10:12 UTC, but its release notes live on GitHub, which is
blocked here, so I could not establish what changed); Ray 2.60.0 (PyPI 4 November 01:59 UTC, same
problem).

## Sources

### Word of the Day

```text
URL:         https://www.merriam-webster.com/dictionary/psephology
Kind:        primary for definition, pronunciation and first-use date (the dictionary owns its entry)
Establishes: noun; "the scientific study of elections"; pronunciation sē-ˈfä-lə-jē; etymology from
             Greek psēphos "pebble, ballot, vote", from the ancient Greek use of pebbles in voting;
             first known use 1952. Also psephologist (sē-ˈfä-lə-jist), psephological.
Paraphrase:  The word-history note says the pebble root suited the work of election analysts because
             Greeks voted with pebbles, and compares ballot, from Italian ballotta, "little ball".
             It names psephomancy, "divination by pebbles", as a relative.
Locators:    headword block; "Did you know?" note; Etymology; First Known Use. Accessed 4 Nov 2026.
```

```text
URL:         https://www.nuffield.ox.ac.uk/people/sites/the-david-butler-archive/psephology/
Kind:        primary for the Nuffield College account (the college whose fellows coined and spread
             the word; it has an institutional stake in the story)
Establishes: 'Psephology' "started out as an academic joke suggested to R.B. McCallum — but it
             caught on." First use in this sense was by McCallum in Oxford Magazine in 1951,
             reviewing the 1950 Nuffield election study. David Butler was the first to use it in a
             book, The British General Election of 1951 (published 1952). On a 1952 US tour Butler
             "found himself overwhelmed by journalists asking about the new word."
Paraphrase:  As above. It names McCallum and Alison Readman as authors of the first Nuffield
             election study (1947). Athenians voted with differently coloured pebbles.
Locators:    page body, paragraphs 1-3.
Quote:       "'Psephology' started out as an academic joke suggested to R.B. McCallum — but it caught on."
```

```text
URL:         https://en.wikipedia.org/wiki/Psephology (raw wikitext checked)
Kind:        secondary (tertiary); used only to locate Butler's own account
Establishes: Repeats that W. F. R. Hardie (1902-1990) coined the term in 1948 when his friend R. B.
             McCallum asked for a word. It cites David Butler, "British Psephology 1945-2001:
             Reflections on the Nuffield Election Histories", ch. 15 in Still More Adventures with
             Britannia, ed. Wm. Roger Louis (2003), p. 250.
Paraphrase:  Repetition only. I could not open the Butler chapter (Google Books preview showed no text;
             the Books API returned 429).
Locators:    lead paragraph, ref "butler".
```

```text
URL:         https://www.timeshighereducation.com/news/sultans-of-swing/92835.article
Kind:        secondary (a Times Higher Education feature about Butler and Nuffield)
Establishes: Says Butler "popularised the term psephology coined by McCallum". It reports Butler's
             regret over the word "as suggesting something occult and separate", in quotation marks
             attributed to Butler.
Paraphrase:  As above. It credits McCallum, not Hardie.
Locators:    paragraphs 3-4.
```

### News 1: control of Congress

```text
URL:         https://www.pbs.org/newshour/politics/democrats-take-control-of-the-senate-after-winning-key-midterm-races
Kind:        primary for AP's own words (AP story, byline Associated Press, hosted by PBS; AP is the
             race-calling desk)
Establishes: "WASHINGTON (AP) — Democrats have retaken control of the U.S. Senate". "The House
             remains too early to call, but Democrats have already flipped seven seats". Senate wins
             named: Turek over Rep. Ashley Hinson (Iowa), Adam Hamilton over Sen. Roger Marshall
             (Kansas), James Talarico over Ken Paxton (Texas), Annie Andrews over Darline Graham
             (South Carolina), Sherrod Brown over Sen. Jon Husted (Ohio), Roy Cooper (open North
             Carolina seat). Ossoff held Georgia; Pappas won New Hampshire. "Democrats need a net gain
             of three seats" for a House majority.
Paraphrase:  As above. AP calls the result a "decisive rebuke" in its own voice.
Locators:    paragraphs 1-2, 6-8. datePublished 2026-11-03T23:40:42-05:00, dateModified 23:46:18-05:00
             (= 04:46 UTC 4 Nov). Retrieved 06:09 UTC 4 Nov.
```

```text
URL:         https://www.foxnews.com/elections/2026/midterm-results/house
             (also .../midterm-results/senate)
Kind:        primary for AP's call tally as AP's data feed (the page states "Source: The Associated
             Press" and its race-call ticker reads "AP calls ..."). It is Fox's rendering of AP data,
             so a writer can cite it as "AP calls, as tallied on". It is not Fox's own decision desk.
Establishes: The embedded balance-of-power data (Nuxt payload) at three retrievals, listed under
             Numbers. Senate: Democrats are flagged winner. House: neither party is flagged winner.
             The six uncalled Senate races are Alaska (Peltola D v. Sullivan R), Louisiana (Letlow R
             v. Davis D), Michigan (El-Sayed D v. Rogers R), Mississippi (Colom D v. Hyde-Smith R),
             Montana (Alme R v. Bodnar I) and Nebraska (Ricketts R v. Osborn, nonparty).
Paraphrase:  Senate counts are split into seats not up (D 34, R 31) and seats won this year.
Locators:    __NUXT_DATA__ "bop.congress" object; race list "called": false. Newest timestamp in the
             payload at final retrieval: 2026-11-04T06:21:07Z.
```

```text
URL:         https://www.nbcnews.com/politics/2026-election/democrats-house-control-midterm-election-wins-trump-check-rcna603397
Kind:        primary for NBC News's own projection (NBC News Decision Desk owns it)
Establishes: "Democrats won control of the House of Representatives with what could be their largest
             majority in nearly two decades, NBC News projects". Its model estimates "approximately
             255 House seats", "an estimate that could still tick up or down by a few seats". NBC
             also projects the Senate for Democrats. Jeffries is expected to be sworn in on 3 January
             as the first Black speaker.
Paraphrase:  The projection rests on a model of past and current vote counts, without polling
             (results page). Lists GOP incumbents defeated: Fitzpatrick, Mackenzie, Bresnahan, Perry
             (PA), Kiggans and Wittman (VA), Kean (NJ), Spartz (IN), Evans (CO), Hudson (NC; chair of
             the House GOP campaign arm).
Locators:    datePublished 2026-11-04T03:08:31Z (10:08 p.m. EST 3 Nov); updated 05:44:45Z.
             Paragraphs 1-6. Retrieved 06:11 UTC.
```

```text
URL:         https://www.nbcnews.com/politics/2026-elections/house-results
Kind:        primary for NBC's seat estimate
Establishes: "Democrats are poised to win at least 255 seats"; "our estimate indicates Democrats will
             ultimately wind up with a 75-seat majority". Embedded data: House D 255 / R 180,
             flips 28 (model estimate, not calls); Senate D 53 / R 41, D net gain 7.
Locators:    page header "Updated: 1:11 AM ET"; __NEXT_DATA__ globalMarqueeInfo.balanceOfPower.
             Retrieved 06:11 UTC.
```

```text
URL:         https://www.nbcnews.com/politics/2026-election/democrats-capture-full-control-congress-nbc-news-projects-fueled-victo-rcna607042
Kind:        primary for NBC's Senate projection; secondary for everything else
Establishes: "Democrats have captured full control of Congress, NBC News projects". "Not since 2006
             has the minority party flipped control of both chambers on a single night."
Locators:    published 11:24 p.m. EST 3 Nov, updated 12:49 a.m. EST 4 Nov; paragraphs 3-5, 15.
```

```text
URL:         https://www.npr.org/2026/11/03/g-s1-149526/2026-midterms-congress-balance-of-power
Kind:        secondary on the calls (NPR's analysis of AP calls; NPR is not the calling desk)
Establishes: "Democrats have cemented control of both chambers of Congress, according to an NPR
             analysis based on a tally of race calls by The Associated Press." Republicans began the
             year with a 53-47 Senate majority. Quotes Thune's X post and Rep. Robert Garcia's
             "LAWYER UP."
Locators:    dateModified 2026-11-04T01:02:35-05:00 (06:02 UTC). Paragraphs 1-4, 11.
```

```text
URL:         https://www.yahoo.com/news/politics/live/midterms-2026-live-updates-election-day-voters-head-to-the-polls-as-democrats-look-to-flip-gop-control-of-the-house-and-senate-110000715.html
Kind:        secondary (Yahoo News live blog relaying AP calls)
Establishes: As of 6:03 AM UTC 4 Nov the headline reads "Democrats win control of the Senate, with
             House still undecided". Pre-election House: GOP 218, Democrats 214. Gives AP call times:
             Ohio Senate (Brown) 11:10 p.m. ET, Texas Senate (Talarico) 11:03 p.m., Kansas Senate
             (Hamilton) 11:24 p.m. Says Darline Graham was appointed in July to her late brother
             Lindsey Graham's seat. Troy Jackson beat Susan Collins in Maine.
Locators:    header block; featured entry 04:41 UTC; entries for each race. Retrieved 06:09 and 06:22 UTC.
```

### News 2: Missouri Proposition A and Amendment 3

```text
URL:         https://www.kcur.org/politics-elections-and-government/2026-11-03/missouri-proposition-a-election-results-redistricting
Kind:        secondary (St. Louis Public Radio story by Jason Rosenbaum, run by KCUR) reporting AP's call
Establishes: Missourians rejected the map approved "at the behest of President Donald Trump",
             which aimed to unseat Rep. Emanuel Cleaver. It "was losing 62% to 38%, according to the
             Associated Press which called the race at 9:59 p.m." (Central). The 2025 lines therefore
             "will not go into effect for the 2028 election". Missouri was the second state after
             Texas to redraw on Trump's request. The 2022 map governed November 2026 after US and
             Missouri Supreme Court rulings. Amendment 6, also passed, bars the legislature from
             overriding a referendum result. Republicans may try to redraw again in 2027 or 2028.
Paraphrase:  As above. Quotes Richard von Glahn, executive director of People Not Politicians.
Locators:    paragraphs 1-3, 5-7, 13-14. The page's JSON timestamps (published "23:08Z") do not
             reconcile with a 9:59 p.m. Central call (03:59 UTC). Treat them as local time
             mislabelled and do not rely on them.
```

```text
URL:         https://www.kcur.org/2026-11-03/missouri-amendment-3-abortion-legal
Kind:        secondary (STLPR, Sarah Kellogg) reporting AP's call
Establishes: Voters rejected Amendment 3, which would have banned most abortions, with exceptions for
             rape and incest to 12 weeks. AP called it with "no" above 55%. The 2024 amendment that
             ended the ban passed with 51.6%. Amendment 3 would also have written the ban on
             gender-affirming care for minors into the constitution.
Locators:    paragraphs 1-6, 15-17.
```

### News 3: Trump on US aid to Israel

```text
URL:         https://www.foxnews.com/politics/trump-says-israel-stop-receiving-4b-us-aid-years-end-can-still-buy-weapons
Kind:        primary for what Trump said (Fox News's report of its own Fox & Friends interview;
             byline Eric Mack; Reuters contributed)
Establishes: "We were giving them $4 billion – we are – but it gets cut off at the end of the year";
             "They don't need it"; "I was approached by Bibi Netanyahu, and we've been talking about
             it for a couple of years"; "They can buy whatever they want." No White House or Israeli
             statement in the article.
Locators:    published 8:46 a.m. EST 3 Nov, updated 10:58 a.m. Read via WebFetch, because the article
             body is not in static HTML.
```

```text
URL:         https://www.cnn.com/2026/11/03/politics/trump-us-aid-israel
Kind:        secondary (context, and a second record of the quotes)
Establishes: The US provides $3.8 billion of military aid a year under a 10-year memorandum of
             understanding that began in 2018 and expires in 2028. Congress appropriates the funding.
             Former officials doubted follow-through. Trump said he "reached an agreement" with
             Netanyahu. Asked whether it was military aid or cash: "Any way you want to define it...
             You can consider it barter." Gadi Eisenkot and Yair Golan (Israeli opposition) attacked
             Netanyahu over it. In May the US and Israel began formal talks on a successor MOU.
Locators:    published 9:21 a.m. ET, updated 3:01 p.m. ET 3 Nov; paragraphs 1-4, 6, 13-17.
```

```text
URL:         https://www.aljazeera.com/news/2026/11/3/trump-announces-that-us-will-stop-paying-israel-after-year-end
Kind:        secondary
Establishes: Fuller quote from Fox & Friends: "we made a deal months ago that we're stopping... by
             the end of this year we won't be paying Israel. Now, we'll help Israel if they need it."
             State Department gave no immediate comment. An analyst quoted expects military assistance
             to be phased out "during 2027. But not by the end of 2026."
Locators:    paragraphs 2-4, 6-8. Modified 21:32 UTC 3 Nov.
```

```text
URL:         https://www.pbs.org/newshour/world/trump-says-u-s-will-stop-giving-4-billion-in-aid-to-israel-next-year
Kind:        secondary (AP, Ben Finley)
Establishes: AP frames it as the US stopping "$4 billion in aid each year to Israel in 2027". Same
             quotes. "There was no immediate comment from Netanyahu's office."
Locators:    published 9:28 a.m. EST 3 Nov; paragraphs 1-5.
```

### Spare news: Greenland

```text
URL:         https://www.pbs.org/newshour/world/greenland-approves-trilateral-deal-with-denmark-and-u-s-following-pressure-from-trump
Kind:        secondary (AP: James Brooks, Stefanie Dazio, Kostya Manenkov); the parliament's own record
             was not opened
Establishes: Greenland's lawmakers voted 16-0, with seven abstentions, in Nuuk on 3 November to
             approve the security agreement with Denmark and the US. It paves the way for more US
             bases while Greenland stays under Danish control. Trump, Frederiksen and Nielsen signed
             it in September at the UN General Assembly. Danish lawmakers debate it later in
             November. It enters into force when Denmark's parliamentary processes are complete.
             State Department: "another major victory for American national security."
Locators:    published 19:21 EST 3 Nov; paragraphs 1-4, 10, 13-15, 17.
```

### Technology 1: Transformers Model Integration Contracts

```text
URL:         https://huggingface.co/blog/transformers-mic
Kind:        primary (Hugging Face's account of its own library and CI; author Tarek Ziadé)
Establishes: On 30 July 2026 Transformers enabled PyTorch SDPA for T5, and "as a side effect, UMT5's
             decoder could attend to future tokens. During training, it could peek at the answer it
             was supposed to predict. Nothing crashed, and the bug stayed in main for almost two
             months." It was fixed on 28 September. A small UMT5 fixture (66 MB, against 1,227 MB for
             the source checkpoint) flagged it on every replayed commit. Label log-probabilities
             differed from baseline by 1.22, and training loss by about 0.20. Running only eager
             attention missed the bug. A Model Integration Contract has three parts: a shrunk
             fixture, a runnable usage path and human-reviewed baselines. Llama 4 Scout shrinks from
             108.6B to 44.7M parameters. On CPU the T5 contract's runner step took 13.4 s. The test
             suite has 88,000+ CPU tests on main and 200,000+ GPU tests daily, across 750+ model
             types. As of 1 November 2026 the MIC CI job reports without blocking PRs. On Whisper,
             random-weight fixtures caught 18 of 24 injected faults and overfit fixtures caught all
             24; both missed an assisted-decoding bug. CLI: tmic; package transformers-mic.
Paraphrase:  As above. HF says the open questions are real-PR catch rate, false alarms and review cost.
Locators:    datePublished 2026-11-03; opening paragraphs 1-2; "Introducing Model Integration
             Contracts"; the replay paragraph ("We replayed frozen MICs over five months..."); "How
             models are shrunk"; the Whisper section; closing section ("As of November 1, 2026").
             Retrieved 06:17 UTC 4 Nov.
Quote:       "As a side effect, UMT5's decoder could attend to future tokens." (the exact wording is
             the disclosure)
```

### Technology 2: StateBench

```text
URL:         https://arxiv.org/abs/2611.03094
Kind:        primary (the authors' paper)
Establishes: "A Fine-Grained Hierarchy and Benchmark for State Tracking in Language Models", Jackson
             Petty, William Merrill, Ashish Sabharwal (Allen Institute for AI; Petty also NYU, Merrill
             also Toyota Technological Institute at Chicago). v1 submitted Mon 2 Nov 2026 13:12 UTC.
             It defines four levels (r-trivial, aperiodic, soluble, general finite) from the
             Krohn-Rhodes decomposition. It proves that Gated DeltaNet with positive eigenvalues
             expresses all aperiodic problems, and that the class of problems transformers are
             thought to length-generalize on does not contain all aperiodic ones. Pretrained and
             frontier models do not robustly solve even soluble state tracking.
Locators:    abstract; §1 (paragraph beginning "Motivated by these theoretical results"); §6, Figure 6
             and the paragraph "Frontier models struggle on long-horizon hard state tracking"; §7.
             PDF arxiv.org/pdf/2611.03094v1 read in full text.
Quote:       Figure 6 paragraph: frontier models "fall to at-chance accuracy on soluble and finite
             state-tracking problems when inputs reach between 10K 64K tokens."
```

```text
URL:         https://huggingface.co/blog/allenai/statebench
Kind:        primary (Ai2's own announcement; byline Kyle Wiggers)
Establishes: 275M-parameter models were trained from scratch on up to 256 assignments and tested to
             64,000 (250 times). Gated DeltaNet and hybrids generalized "almost perfectly" on
             r-trivial, aperiodic and soluble problems. Transformers "never learned general finite
             problems". Frontier models (Gemini 3.8 Flash, Claude Opus 5.5, GPT-6 Sol and Luna) did
             well on the easy levels and dropped "to 13% or lower on the longest general finite
             problems". Pretrained Olmo 3 7B and Olmo Hybrid were at chance on general finite.
             Problem format mattered: small models were near ceiling on RULER-style r-trivial
             problems and near chance on the same problems framed as spreadsheet edits.
Locators:    datePublished 2026-11-03T17:15Z; "What we found" > "Pretrained models" and "Models
             trained directly on the task". Links: tech report (redirects to the arXiv page above),
             data huggingface.co/datasets/allenai/state-bench, code github.com/allenai/state-bench
             (not opened; GitHub blocked here).
```

### Spare tech

```text
URL:         https://developer.nvidia.com/blog/diagnose-distributed-ai-workload-failures-with-nvidia-attribution/
Kind:        primary (NVIDIA on its own tool; author Elizabeth Goodman)
Establishes: NVIDIA Attribution is described as open source. It correlates workload-scoped logs,
             metrics, telemetry and scheduler state into a diagnosis (outcome, root cause, affected
             nodes, symptoms, evidence trail) using deterministic rules. Its two components are a
             REST Attribution Service and a Python Attribution Blueprint, with Slurm, Kueue, Loki,
             Kubernetes pod log and PromQL connectors. NVIDIA says it analyzes "millions of workloads
             each week across hundreds of thousands of GPUs". In the worked example an NVLink
             XID 149 on one node is the root cause and NCCL errors on other ranks are kept as symptoms.
Locators:    datePublished 2026-11-02T23:39:34Z; summary bullets; "Turn workload evidence into one
             diagnosis". The repository link and licence were not verified (GitHub blocked).
```

```text
URL:         https://blog.cloudflare.com/dns-targeted-zone-builds/
Kind:        primary (Cloudflare on its own pipeline)
Establishes: The Zone Builder now gets about 700 DNS record changes per second, against about 250 in
             2022. Some zones exceed 20 million records. A targeted build planner plus a scheduler
             cut peak memory by 85% and halved the time from DNS change to Quicksilver write.
Locators:    datePublished 2026-11-02T14:00Z; paragraphs 1, 5.
```

## Contradictions

- **Is the House decided?** AP: not called. The PBS-hosted AP story (04:46 UTC) says "too early to
  call". The AP data on Fox shows no House winner at 06:21 UTC, and Yahoo's headline at 06:03 UTC
  says "House still undecided". NBC projected the House for Democrats at 10:08 p.m. ET. NPR says
  "Democrats have cemented control of both chambers... according to an NPR analysis based on a tally
  of race calls by The Associated Press", which is NPR's inference, not an AP call. Fox News's own
  headline list reads "Democrat seize House control" (Fox's decision desk, not opened). Write the
  House as projected by NBC (and others) and not yet called by AP, with the time.
- **Senate flips: six or seven.** NPR (06:02 UTC) lists six (NC, SC, OH, TX, KS, IA). NBC's story
  says "six Republican-held seats" and then names seven states including Maine. NBC's data and the
  AP data both show a Democratic net gain of 7. The Maine call (Troy Jackson over Susan Collins) came
  after NPR's list. Use seven, from the data.
- **House flips.** The AP story at 04:46 UTC says seven. The AP-sourced tally at 06:21 UTC shows a
  Democratic gain of 24. NBC's model estimates 28. Different times and different methods
  (calls against model). Do not mix them.
- **Israel aid timing.** Trump: "cut off at the end of the year"; "by the end of this year we won't
  be paying Israel." AP: aid stops "in 2027" (the same thing in other words). An analyst quoted by Al
  Jazeera expects a phase-out "during 2027. But not by the end of 2026." CNN: the MOU runs to 2028
  and Congress appropriates. Nobody in Israel confirmed the "deal". Netanyahu said before the
  Israeli election that the aid would end, on no stated timeline.
- **Who coined psephology.** Nuffield College: an "academic joke suggested to R.B. McCallum", with
  first use by McCallum in Oxford Magazine in 1951. Wikipedia, citing Butler's 2003 chapter: coined in
  1948 by W. F. R. Hardie at McCallum's request (not verified at source). Times Higher Education:
  "coined by McCallum". Merriam-Webster: first known use 1952 (Butler's book). Safe wording: the word
  came out of McCallum's Oxford circle as a joke, McCallum first printed it in 1951, and Butler's 1952
  book spread it. Name Hardie only as Butler's attribution.
- **StateBench frontier floor.** The Ai2 blog says accuracy fell "to 13% or lower" on the longest
  general finite problems. The paper says "at-chance accuracy on soluble and finite" problems between
  10K and 64K tokens, and "near-zero performance on the hardest problems" (§1). Figure 6 carries no
  printed values in the text layer. Use the paper's wording, or attribute the 13% to the blog.
- **StateBench: transformers on easy levels.** The blog says transformers "learned the easier levels
  but degraded on longer sequences". The paper says directly trained transformers "fail to generalize
  on r-trivial data". Both describe failure to length-generalize. Prefer the paper.
- Against the commission: nothing found that breaks it. AP's House call is the one hole, covered
  above.

## Numbers

Election figures, with retrieval time. The AP-sourced tallies are AP data as rendered on
foxnews.com (see Sources).

```text
Figure: Senate, AP: Democrats 53, Republicans 41, 6 uncalled (AK, LA, MI, MS, MT, NE); D flagged winner
Owner:  AP (data feed on foxnews.com/elections/2026/midterm-results/senate and /house)
Scope:  100 seats; 34 D and 31 R not up in 2026; D won 19 of 35 contests called, R won 10; D net +7.
        Identical at 06:09:47, 06:21:38 and 06:22:58 UTC 4 Nov. The D 53 appears to include
        independents Sanders and King, who caucus with Democrats (the data shows "Oth" 0; inference).
```

```text
Figure: House, AP calls, series: 06:09:47 UTC D 209, R 125, 101 uncalled -> 06:21:38 UTC D 214,
        R 126, 95 uncalled -> 06:22:58 UTC D 215, R 126, 94 uncalled. D net gain 24. No winner.
Owner:  AP (data feed on foxnews.com/elections/2026/midterm-results/house; newest payload stamp
        06:21:07Z at final retrieval)
Scope:  435 seats; 218 for a majority. At 06:22 UTC Democrats needed 3 more called seats.
```

```text
Figure: House majority threshold 218; Democrats needed a net gain of 3; pre-election GOP 218, Dem 214
Owner:  AP story (PBS-hosted) for the net gain of 3; Yahoo News for the pre-election split
Scope:  pre-election House as of 3 November 2026
```

```text
Figure: NBC projection, about 255 Democratic House seats ("could still tick up or down by a few"),
        a 75-seat majority, 28 flips
Owner:  NBC News Decision Desk model (nbcnews.com house-results, updated 1:11 a.m. ET)
Scope:  model estimate of the final seat count, not race calls. Projection made 10:08 p.m. ET 3 Nov.
```

```text
Figure: AP Senate control call, before midnight ET 3 Nov; the AP story was published 11:40 p.m. ET
Owner:  AP (story timestamp on PBS); Yahoo's "before the clock struck midnight" line
Scope:  the exact AP call minute was not established
```

```text
Figure: Pre-election Senate 53 R, 45 D, 2 independents caucusing with D; D needed net +4
Owner:  Yahoo News live blog; NPR (53-47)
Scope:  Senate as of 3 November 2026
```

```text
Figure: Missouri Proposition A losing 62% to 38% when AP called it at 9:59 p.m. Central
Owner:  AP, via STLPR/KCUR
Scope:  partial count at the call; certified totals not obtained
```

```text
Figure: Missouri Amendment 3, "no" above 55% at the AP call; 2024 amendment passed with 51.6%
Owner:  AP via STLPR/KCUR (2026); STLPR for the 2024 figure
Scope:  partial 2026 count at the call
```

```text
Figure: US military aid to Israel, $3.8 billion a year under the 10-year MOU from 2018 to 2028;
        Trump's figure is "$4 billion"
Owner:  CNN for the MOU figure (the MOU text itself was not opened); Fox & Friends for Trump's words
Scope:  annual
```

```text
Figure: UMT5 bug window, 30 July to 28 September 2026; log-prob gap 1.22; loss gap about 0.20;
        fixture 66 MB against 1,227 MB; T5 contract CPU step 13.4 s; Llama 4 Scout 108.6B -> 44.7M
        parameters; Whisper injected faults 18/24 (random) against 24/24 (overfit)
Owner:  Hugging Face blog
Scope:  HF's replay over five months of Transformers commits; the Whisper faults are synthetic
```

```text
Figure: StateBench, trained on up to 256 assignments and tested to 64,000 (250 times); frontier
        models at chance at 10K-64K tokens on soluble and general finite problems
Owner:  Petty, Merrill, Sabharwal, arXiv 2611.03094 (Ai2 blog for "13% or lower")
Scope:  275M-parameter direct-training models; four frontier models evaluated generatively
```

```text
Figure: Greenland parliament vote, 16-0 with 7 abstentions
Owner:  AP via PBS (the Inatsisartut record was not opened)
Scope:  3 November 2026 vote in Nuuk
```

## Limits

- I could not open AP's own pages (apnews.com live page and articles returned 403; the results hub
  renders client-side). Every AP call here comes from an AP story hosted by PBS or from AP's data as
  rendered on foxnews.com.
- AP's House call: not made as of 06:22:58 UTC 4 Nov. Democrats were 3 called seats short and the
  count was moving fast. The writer must state the time, and the editor should expect the figures to
  be stale.
- The exact minute of AP's Senate control call was not established (it was before midnight ET; the
  AP story was published at 11:40 p.m. ET).
- CNN's and CBS's House projections appear only in search summaries. I did not open them, so cite
  NBC.
- Missouri results come from AP calls as reported by STLPR. I did not open the Secretary of State's
  canvass.
- Israel aid: only Trump's word establishes an agreement with Netanyahu. There is no Israeli or White
  House confirmation, and I did not open the MOU text.
- Psephology: Butler's 2003 chapter naming Hardie was not opened, so the inventor is attributed and
  not settled.
- Transformers MIC: I did not check HF's account of the UMT5 bug against the Transformers commit
  history (GitHub blocked). The account is HF's own, about its own library, and so primary.
- StateBench: Figure 6 has no printed values. I did not open the code or data repositories.
- vLLM 0.33.0 and Ray 2.60.0 release contents could not be established (GitHub blocked).
- I never received the feature desk's topic. Swap a technology item for an alternate if it overlaps.

## Source assets

```text
Asset: Figure 6 of arXiv 2611.03094 (§6, p. 9): four panels (r-trivial, aperiodic, soluble,
       general finite), accuracy against input length (log scale, 1K-64K tokens) for
       claude-opus-5-5, gemini-3.8-flash, gpt-6-luna and gpt-6-sol
Shows: accuracy stays high on the first two levels and collapses on the last two as inputs lengthen
Crop:  keep all four panels, the log-scale x-axis label and the legend; keep the caption's Wilson
       interval note
```

```text
Asset: AP balance-of-power data (foxnews.com House and Senate results pages, "Source: The Associated
       Press")
Shows: called seats against uncalled seats per party
Crop:  a capture is time-stamped by nature; any capture must show the page's time. A series table
       (Numbers) is safer than an image.
```

The Nuffield page, the Merriam-Webster entry, the KCUR/STLPR stories, the Fox/CNN/Al Jazeera aid
stories, the HF MIC post (no figure examined), the NVIDIA and Cloudflare posts and the PBS Greenland
story: None found that carries the argument better than prose.

## Discarded

```text
https://apnews.com/live/midterm-election-2026: gated (403); AP wording taken from the PBS-hosted AP story
https://apnews.com/projects/elections-2026/: reachable but renders results client-side; no figures in HTML
https://www.cnbc.com/2026/11/03/midterm-elections-2026-live-updates.html: gated (403)
https://www.axios.com/2026/11/03/election-day-midterm-trump-democrats-republicans: gated (403)
https://www.bls.gov/news.release/jolts.nr0.htm: gated (403); September JOLTS not pursued
https://www.pbs.org/newshour/world/u-s-launches-new-attacks-on-iranian-targets-days-after-netanyahu-pressed-trump-for-more-strikes: running story, no development after 3 Nov
https://www.pbs.org/newshour/economy/binance-flags-potential-security-issue-says-approximately-6-3-billion-impacted: single-company hack, dated 30 Oct
https://www.pbs.org/newshour/economy/doordash-offers-17-billion-for-instacart-in-what-would-be-big-grocery-delivery-consolidation: single-company deal, dated 29 Oct
https://www.pbs.org/newshour/science/anthropic-says-risks-for-investors-include-blowback-from-runaway-ai: dated 27 Oct; single company
https://www.cbsnews.com/news/supreme-court-st-mary-catholic-parish-v-roy-colorado-preschool/ (search summary only): an argument, not a decision; court-led pattern
https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/: too close to the 3 Nov GPT-6 Astra weight-editing item
https://openai.com/index/lifeval: single-company benchmark
https://pypi.org/project/vllm/0.33.0/: release confirmed (2 Nov) but notes unreachable
https://pypi.org/project/ray/2.60.0/: release confirmed (4 Nov) but notes unreachable
https://vllm.ai/blog: no dated posts in the 2-4 Nov window found
https://www.kcur.org/politics-elections-and-government/2026-11-03/missouri-election-results-2026-november-amendments-proposition-congress: index page only; the two linked stories are used instead
```
