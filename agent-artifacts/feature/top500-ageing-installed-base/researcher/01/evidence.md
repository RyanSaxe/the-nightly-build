# Evidence record: feature/top500-ageing-installed-base (researcher 01)

The list files reproduce the scout's figures exactly and support a sustained ageing of the TOP500's entries. In November 2026 the median entry first appeared 6 editions (three years) earlier, against 4 in November 2021 and 1 to 2 in every list from 2012 to 2019. 138 entries first appeared ten or more editions earlier, against 45 in November 2021 and 2 to 36 in 2012–2017. November 2021 was no young baseline. It was the oldest list up to that date, and the rise starts around 2014. The mechanism is turnover. The list always holds 500 entries, so the number of newcomers equals the number of entries pushed off. Since 2020 the bar at No. 500 has risen 5–25% a year, against 30–69% a year in 2011–2019, and survival has changed accordingly: 52–72% of the non-Chinese 2020–2021 cohorts were still listed five years later, against 3–17% of the 2012–2017 cohorts. The evidence is thinner in three places. (1) About half the fall in newcomers since the 2010s is China leaving the list, not a general retreat. Non-Chinese newcomers ran 37–84 per edition in 2015–2019 and 39–54 from June 2022 to June 2026, and the November 2026 non-Chinese count, 27, sits near 2020's 25 and 31, so it is low but not unprecedented on that basis. (2) By performance the list has not aged. Entries first listed within the last two years carry 61% of total Rmax in November 2026, inside the 62–69% range of every November list from 2016 to 2025, and the five-year-plus entries carry 9% and sit mostly in the bottom half (median rank 313). (3) Nothing in the files shows where new compute went. The AI-cluster explanation is the release's inference from Epoch AI ownership data. Epoch measures 8-bit peak capacity, so its growth figure is not comparable with HPL. Next Platform's "pause before Rubin and MI400" reading cannot be tested before the June 2027 list. Every past dip before 2022 rebounded within one to three editions. Since June 2022 newcomers have stayed between 39 and 54 for nine editions and have now fallen to 28.

## Data and reproduction

- Downloaded 68 list files, June 1993 to November 2026, on 2026-11-20 into `.nb-work/feature/top500-ageing-installed-base/data/raw/`. Address pattern: `https://www.top500.org/lists/top500/YYYY/MM/download/TOP500_YYYYMM.xlsx` for June 2020 onward. Earlier lists use `.xls` at the same path (the `.xlsx` path returns 404 before 2020). No login is needed. SHA-256 sums are in `data/raw.sha256`.
- `data/compute.py` (run with `uv run .nb-work/feature/top500-ageing-installed-base/data/compute.py` from the checkout root) writes `data/series.csv` (one row per list, every series below), `data/cohort_survival.csv` and `data/checks.txt`. Its docstring holds the exact definitions. Helpers: `data/newcomers.py` lists the November 2026 newcomers, `data/sites.py` lists hyperscaler and AI-company entries in November 2026, and `data/peek_headers.py` shows each file's columns.
- Saved web pages (untrusted copies, for re-reading only) are in `data/web/`.
- The November 2026 file's server `Last-Modified` is Wed, 18 Nov 2026 03:09:23 GMT, two days after the release. The June 2026 file's is Sun, 28 Jun 2026. Both files were revised after their releases, so every figure here is as of the download on 2026-11-20.

### How "First Appearance" is defined

TOP500 publishes no definition of the "First Appearance" column. Neither the TOP500 Description page nor the Call for Participation mentions it, and the FAQ covers only Linpack. Its meaning is read from the files:

- It holds an edition number (June 1993 = 1, November 2026 = 68), present in every file from June 2012 (edition 39) on. Lists before June 2012 do not have it.
- In every list from November 2016 onward, an entry has a blank "Previous Rank" exactly when First Appearance equals the current edition. Earlier lists have a handful of exceptions: 2012-11, 2013-06, 2014-11 and 2016-06 (4, 1, 1 and 1 entries).
- Upgrades keep it. Across the 1,650 System IDs seen from November 2017 on, no System ID ever carries two First Appearance values. 108 times a System ID's Rmax rose more than 10% between consecutive lists and its First Appearance stayed the same.
- Re-entry keeps it. Two System IDs left and later returned (178083: absent editions 57–60, back from 61 with First Appearance 41; 179399: absent 52–53). Both kept their original value. Re-entry is negligible in count.
- What it cannot catch: a system that is rebuilt or renamed and submitted under a new System ID counts as a newcomer. So "age by First Appearance" measures time since an entry first appeared, not the age of the hardware.
- Cross-check with the documented "Year" field ("Year of installation/last major update", TOP500 Description page). Upgrades reset that field. In November 2026, 139 entries have a Year five or more years before 2026, against 138 by First Appearance, and only 5 of the 138 have a Year of 2022 or later. The two definitions agree.

Age in this record is `N − First Appearance` in editions (one edition = six months). A newcomer has age 0. "Five or more years" means age ≥ 10 editions, which is the definition that reproduces the scout's 138 and 45. A note for the writer: an entry with age 6 has appeared on 7 lists, counting the current one. The scout's "on the list for 6 editions" means six editions since first appearance.

## Sources

```text
URL:         https://www.top500.org/lists/top500/2026/11/download/TOP500_202611.xlsx (and the same path pattern for every list back to June 1993; .xls before June 2020)
Kind:        primary. The TOP500 project publishes the list and owns every field in it.
Establishes: firsthand, for each list, every entry's rank, previous rank, First Appearance, Year, country, segment, Rmax, System ID.
Paraphrase:  500 rows per list, one per system, with a header row; Rmax is in GFlop/s through November 2016 and TFlop/s from June 2017 (column labelled "Rmax [TFlop/s]").
Locators:    sheet "68" (Nov 2026), columns "First Appearance", "Previous Rank", "Year", "Rmax [TFlop/s]", "Country", "System ID". Old files (1993–2011) begin with a blank row on some lists; compute.py handles it.
```

```text
URL:         https://www.top500.org/news/top500-leadership-holds-steady-new-system-turnover-falls-historic-low/
Kind:        primary for the TOP500 project's own statements about the 68th list; secondary for the Epoch AI figures it repeats. No individual byline (dateline Chicago, 16 November 2026).
Establishes: the project's own count of 27 new systems (5.4%), its "lowest ... in the history of the list" claim, No. 500 at 2.857 PF/s (from 2.662), No. 50 from 49.85 to 55.81 PF/s, No. 100 from 21.85 to 22.74 PF/s, total HPL 19.57 EF/s (+4.4%), 291 accelerated systems (58.2%), HANGANG as top newcomer at No. 12 with 342.6 PF/s. It repeats Epoch AI's 2.5x per year, 15 million H100e and 71% figures without a link.
Paraphrase:  The top ten did not change from June. The release says the low turnover does not mean performance stopped growing. It attributes more of the improvement to additions and upgrades below the very top, and offers the shift of hardware into hyperscaler "AI factories" as its suggestion of where new hardware went.
Locators:    sections "Only 27 Systems Are New", "Where the New Hardware Is Going", "Performance Deeper in the List Improved", closing paragraph.
Quote:       "Just 27 systems are new, the lowest number ever recorded by a wide margin."
Quote:       "This suggests that growth has indeed shifted toward AI factories, and from capability systems to capacity systems."
Quote:       "The next shift at the top will therefore depend on when the next generation of large systems and energy-efficient technologies is ready to report measured results."
```

```text
URL:         https://www.top500.org/lists/top500/list/2026/11/
Kind:        primary. The TOP500's live rendering of the 68th list.
Establishes: that the live list, like the downloaded file, includes Horizon (TACC, Dell PowerEdge XE8712, GB200) at No. 24 with Rmax 132.00 PF/s.
Paraphrase:  The live list and the file agree with each other and disagree with the release's 27 newcomers and 19.57 EF/s total.
Locators:    first page of the list, rank 24.
```

```text
URL:         https://top500.org/project/top500_description/
Kind:        primary. The TOP500's own field definitions.
Establishes: "Year - Year of installation/last major update". It has no entry for First Appearance.
Locators:    field list, paragraph beginning "To keep the list as compact as possible".
```

```text
URL:         https://www.top500.org/project/call-for-participation/
Kind:        primary. TOP500 submission rules.
Establishes: the November 2026 deadline for new submissions was 24 October (23:59 PST), and every system reported had to be installed by 1 November. A machine installed later cannot appear until June 2027. That bears on the timing explanation.
Locators:    "Deadlines" paragraph.
```

```text
URL:         https://www.nextplatform.com/hpc/2026/11/16/supercomputer-installs-take-a-dive-in-the-second-half-of-2026/5310221
Kind:        primary for its author's view; secondary for list facts. Timothy Prickett Morgan, "Co-Editor, Co-Founder, The Next Platform", published 16 Nov 2026 18:59 UTC.
Establishes: Prickett Morgan's own reading (roadmap timing, with cloud renting as a worse alternative). It repeats the 27 count and offers his newcomer tallies.
Paraphrase:  He says new HPL-tested installations "stalled" at about half the normal number. He offers two explanations: a shift to renting cloud capacity, and customers not yet ready to test machines built on Nvidia Rubin/Vera or AMD MI400/Venice parts arriving in 2027. He favours the second and adds that networking is stuck at 800 Gb/s ports. He expects "about two dozen extra machines" over the next lists to balance the drop. He adds that the list is skewed by non-submission: large machines often do not submit, and many entries are cloud, telecom and software-company clusters that do not do HPC as their day job. He proposes counting only machines no older than four or five years.
Locators:    paragraphs 3–6 ("But don't freak out just yet" through "We will see as the June 2027..."), paragraph on 264 machines, paragraph on eSurfing Cloud.
Quote:       "It could also just be that companies were not ready to test iron that is being installed now or early in 2027 as Nvidia rolls out its "Rubin" GR200 GPUs and "Vera" CV100 CPUs or AMD rolls out its "Altair" MI400 GPUs and its "Venice" Epyc 9006 processors."
Quote:       "All that said, I still believe the stall is more about roadmap timing – particularly with networking, which is stalled at 800 Gb/sec ports when the world is expecting 1.6 Tb/sec ports – than it is moving workloads to the cloud at the same time there are much better compute engines ramping next year."
Quote:       "To balance things out, I would expect about two dozen extra machines to be installed to cover the drop experienced in the November 2026 rankings. If the June 2027 list is a little light, then the following two lists will have to be above average for things to balance out."
```

```text
URL:         https://epoch.ai/data-insights/ai-computing-capacity-additions-doubling
Kind:        primary. Epoch AI owns the estimate. Data Insight, 29 Oct 2026, by Isabel Juniewicz and Josh You.
Establishes: the release's "2.5 times per year" figure, traced to its owner. Quarterly additions of AI computing capacity, measured in H100-equivalents (H100e) from Epoch's AI Chip Sales median estimates as of 19 October 2026, grew 2.5x per year (90% CI 2.3x to 2.7x, doubling time 9.1 months) over Q1 2024 to Q2 2026. That is down from about 6x in 2023. Year-over-year growth in quarterly additions fell from 2.8x (Q2 2025) to 2.2x (Q2 2026). Epoch notes a possible deceleration that is not statistically significant and "may also reflect a lull between generations", and says Nvidia had recognised no Rubin sales in its fiscal quarter ending July.
Paraphrase:  The quarterly additions table runs from 827,914 H100e (Q1 2024) to 6,327,416 H100e (Q2 2026). Cumulative capacity grew 2.6x from Q2 2025 to Q2 2026.
Locators:    lead paragraph; table "Computing capacity of AI chips sold each quarter by designer"; "Analysis" section.
```

```text
URL:         https://epoch.ai/blog/introducing-the-ai-chip-sales-data-explorer
Kind:        primary. Epoch AI, "Update Jan. 13, 2026", by the Epoch AI team.
Establishes: the release's "15 million H100" figure. Cumulative global AI compute capacity exceeds the equivalent of 15 million Nvidia H100s, "measured using each chip's respective peak specifications in 8-bit operations per second".
Locators:    section "Compute".
```

```text
URL:         https://epoch.ai/data-insights/hyperscalers-control-most-compute
Kind:        primary. Epoch AI Data Insight, 14 Apr 2026, by Luke Emberson, Josh You and Venkat Somala.
Establishes: the release's 71% figure. Amazon, Google, Meta, Microsoft and Oracle hold an estimated 71% of cumulative AI compute as of Q4 2025, in H100e, up from 63% in Q1 2024. The table row gives 70.7% for Q4 2025.
Locators:    lead paragraph; table "Hyperscaler Compute Share by Quarter", rows 2024 Q1 and 2025 Q4.
```

## Contradictions

- **Release versus file: 27 or 28 newcomers.** The release, Next Platform and the scout's source all say 27. The downloaded file and the live list both hold 28 entries with First Appearance 68. The file total is 19,710.6 PF/s (release 19.57 EF/s). Its No. 500 is 2.8676 PF/s (release 2.857), and its total growth on June is 5.2% (release 4.4%). These gaps fit one roughly 132 PF/s entry added after the release text was written: Horizon (TACC) at No. 24, which pushed the old No. 500 (2.857 PF/s) off the list. Removing Horizon and restoring that entry gives 19,710.6 − 132.0 + 2.857 ≈ 19,581 PF/s, close to the release's 19.57 EF/s and 4.5% above June's 18,732.7. No document states that Horizon was added late, so the cause is unconfirmed. Next Platform's own six-list total of "264 machines from June 2024 through November 2026" equals the file counts with 28 (46+54+48+45+43+28) and is one more than its 27 implies. The writer should use one count and say which document owns it.
- **"Historic low" versus China's exit.** TOP500 calls 27 the lowest ever "by a wide margin". The site/year proxy puts every November and June list from 1993 to 2011 at 83 or more, and the First Appearance count since 2012 never went below 39 before now, so the all-entries claim holds. Restricted to non-Chinese entries, though, 27 is close to June 2020 (25) and November 2020 (31). Chinese newcomers ran 33–103 per edition in 2015-11 to 2020-06, most of them in the Industry segment. They have been 0–2 per edition since June 2022, and China's entries fell from 228 (Nov 2019) to 18 (Nov 2026). Much of the 2010s-to-2020s drop in newcomers is that withdrawal.
- **Ageing by count versus ageing by performance.** By count the list has aged steadily. By Rmax it has not: entries first listed within two years hold 61.5% of total Rmax in Nov 2026, against 64.1% in Nov 2021 and 69.4% in Nov 2019. Five-year-plus entries hold 9.0%, against 11.5% in Nov 2021 and 14.2% in Nov 2017. The old entries are mostly small: their rank quartiles are 201, 313 and 428, and the best-placed is No. 9 (Fugaku, First Appearance 55). The working claim that "the TOP500 increasingly measures an ageing installed base" is true of the bottom half and not of the list's capacity.
- **Median plateau.** The median rose from 4 (Nov 2021) to 6 (Nov 2024), then read 6, 5, 5, 6. The mean went 6.10, 6.39, 6.10, 6.01, 6.40. Entries aged ≥6 editions have stayed between 239 and 261 since June 2024. The 2021-to-2026 rise in the median was over by November 2024. What kept rising after that is the five-year-plus tail: 92, 113, 106, 117, 138. Half of the 138 (71) are the June and November 2021 cohorts, which crossed the ten-edition line this year and last.
- **Next Platform's "pause" view against the history.** In its own words: the stall is "more about roadmap timing" and will be balanced by "about two dozen extra machines" in the coming lists. History up to 2021 is on its side. The newcomer low of Nov 2014 (68) was followed by 89, 136 and 154. Nov 2020 (44) was followed by 58 and 70. Since June 2022, though, newcomers have not rebounded above 54 in nine editions: 39, 41, 44, 47, 46, 54, 48, 45, 43, then 28. A rebound from 28 back to the 2022–2026 range would fit the pause view. It would not undo the post-2020 step down, which has held through the Hopper and Blackwell generations. Epoch's own note that the slowing in AI chip additions "may also reflect a lull between generations" supports the timing reading for hardware in general. TOP500's 24 October submission deadline and 1 November installation cutoff mean that hardware installed in late 2026 could not have been listed.
- **"AI clusters that never submit an HPL run."** This overstates the record. Microsoft Azure has eight entries in Nov 2026, including Eagle at No. 7 (561.2 PF/s, First Appearance 62). Nvidia, SoftBank and Nebius also submit. What the file does show: no entry sited at Google, Amazon, Oracle or xAI, and Meta appears only as a 2017 "Facebook" entry at No. 425. The release offers the AI-factory explanation as a suggestion ("This suggests..."). Next Platform offers cloud renting and roadmap timing as competing explanations. No source counts how much AI hardware is HPL-capable and went unsubmitted.
- **Scout's "HPL total growth of 4.4%".** That is the release's figure. The file gives 5.2%. Over twelve months the file gives +31.5%.

## Numbers

All series are in `data/series.csv` (definitions in `compute.py` docstring) and `data/cohort_survival.csv`. One edition = six months. "Non-China" = Country ≠ "China" in that list.

```text
Figure: median age, Nov 2026 = 6 editions; Nov 2021 = 4 editions
Owner:  TOP500 list files (First Appearance), computed in compute.py
Scope:  all 500 entries of each list; age = edition − First Appearance
```

```text
Figure: entries aged ≥10 editions (first listed five or more years earlier), Nov 2026 = 138; Nov 2021 = 45
Owner:  TOP500 list files, computed
Scope:  500 entries; non-China only: 124 vs 41
```

```text
Figure: entries with Year ≥5 years before the list year, Nov 2026 = 139; Nov 2021 = 39
Owner:  TOP500 list files ("Year" = year of installation/last major update), computed
Scope:  500 entries; independent of First Appearance
```

```text
Figure: newcomers, Nov 2026 = 28 in the file (27 per TOP500 release); previous minimum since June 2012 = 39 (June 2022)
Owner:  TOP500 list files (First Appearance = 68); TOP500 release for 27
Scope:  one edition
```

```text
Figure: newcomers per edition by site/year proxy, 1993-11 to 2011-11: minimum 83, median 191, maximum 327
Owner:  TOP500 list files, computed (an entry is new if its normalised Site and Year pair does not appear in the previous list)
Scope:  proxy error against First Appearance across 30 lists 2012–2026: mean +1.0, range −16 to +23
```

```text
Figure: five-year survival (present ten editions after entry), non-China cohorts: 2012-06 to 2017-11 cohorts 3%–17%; 2020-06 72% (18/25), 2020-11 52% (16/31), 2021-06 67% (33/49), 2021-11 54% (33/61)
Owner:  TOP500 list files, computed (cohort_survival.csv)
Scope:  cohort = entries with a given First Appearance; all-country rates: 2012–2017 cohorts 1%–16%, 2020–2021 cohorts 45%–66%
```

```text
Figure: No. 500 Rmax growth year on year (November lists): 2011 +64%, 2012 +50%, 2013 +54%, 2014 +30%, 2015 +35%, 2016 +69%, 2017 +57%, 2018 +59%, 2019 +31%, 2020 +15%, 2021 +25%, 2022 +5%, 2023 +17%, 2024 +15%, 2025 +11%, 2026 +11%
Owner:  TOP500 list files, computed (No. 500 Rmax: 2025-11 2.574 PF/s, 2026-11 2.868 PF/s)
Scope:  entry threshold; total Rmax growth over the same years: 2020 +47.5%, 2021 +25.0%, 2022 +60.2%, 2023 +44.6%, 2024 +66.7%, 2025 +27.9%, 2026 +31.5%
```

```text
Figure: share of total Rmax held by entries first listed within two years (age ≤4), Nov 2026 = 61.5%; Nov 2021 = 64.1%; Nov 2019 = 69.4%; Nov 2016–Nov 2025 range 62.0%–69.4%
Owner:  TOP500 list files, computed
Scope:  sum of Rmax over 500 entries
```

```text
Figure: share of total Rmax held by newcomers, Nov 2026 = 5.1%, the lowest of the 30 lists since June 2012 (previous low 5.5%, June 2023)
Owner:  TOP500 list files, computed (newcomer Rmax 1,000.6 PF/s of 19,710.6)
Scope:  one edition
```

```text
Figure: Chinese entries, Nov 2019 = 228; Nov 2021 = 173; Nov 2026 = 18. Chinese newcomers 2015-11 to 2020-06: 33–103 per edition; June 2022 onward: 0–2
Owner:  TOP500 list files, computed
Scope:  Country = "China"
```

```text
Figure: Epoch AI quarterly AI-compute additions growth = 2.5x per year (90% CI 2.3x–2.7x)
Owner:  Epoch AI, Data Insight 29 Oct 2026 (Juniewicz, You)
Scope:  H100-equivalents (8-bit peak), Q1 2024–Q2 2026, six chip designers; not comparable with FP64 HPL Rmax
```

```text
Figure: five US hyperscalers' share of global AI compute, Q4 2025 = 71% (table: 70.7%), Q1 2024 = 63% (62.5%)
Owner:  Epoch AI, Data Insight 14 Apr 2026 (Emberson, You, Somala)
Scope:  cumulative H100e
```

### Full series, every list with First Appearance (June 2012 – November 2026)

Age in editions. Rmax shares are fractions of the list's total Rmax.

| list | ed | newcomers | of which non-China | median age (ed) | mean age (ed) | non-China median / mean | entries ≥10 ed | of which non-China | entries ≥6 ed | China entries | Rmax share ≥10 ed | Rmax share newcomers | Rmax share ≤4 ed | total Rmax PF | #500 Rmax PF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2012-06 | 39 | 167 | 140 | 1 | 1.76 | 1 / 1.87 | 5 | 5 | 36 | 68 | 0.0031 | 0.321 | 0.9069 | 123.418 | 0.0608 |
| 2012-11 | 40 | 165 | 143 | 1 | 1.88 | 1 / 1.96 | 2 | 2 | 47 | 72 | 0.0011 | 0.2927 | 0.9251 | 162.139 | 0.0764 |
| 2013-06 | 41 | 178 | 140 | 1 | 1.82 | 1 / 1.92 | 5 | 5 | 42 | 66 | 0.0042 | 0.2993 | 0.9148 | 223.654 | 0.0966 |
| 2013-11 | 42 | 129 | 111 | 1 | 2.02 | 1 / 2.1 | 4 | 3 | 44 | 63 | 0.0036 | 0.1386 | 0.8598 | 250.08 | 0.1178 |
| 2014-06 | 43 | 114 | 86 | 2 | 2.33 | 2 / 2.46 | 5 | 4 | 52 | 76 | 0.0042 | 0.1366 | 0.7802 | 273.764 | 0.1337 |
| 2014-11 | 44 | 68 | 64 | 2 | 2.89 | 3 / 2.96 | 9 | 8 | 71 | 61 | 0.0067 | 0.1118 | 0.6789 | 308.851 | 0.1534 |
| 2015-06 | 45 | 89 | 84 | 3 | 3.24 | 3 / 3.22 | 12 | 9 | 96 | 37 | 0.0128 | 0.1838 | 0.6045 | 362.652 | 0.1648 |
| 2015-11 | 46 | 136 | 49 | 2 | 2.99 | 3 / 3.56 | 16 | 13 | 108 | 109 | 0.0265 | 0.1936 | 0.5594 | 417.807 | 0.2063 |
| 2016-06 | 47 | 154 | 82 | 1 | 2.64 | 3 / 3.45 | 16 | 13 | 95 | 168 | 0.0457 | 0.3133 | 0.6556 | 567.353 | 0.2861 |
| 2016-11 | 48 | 113 | 78 | 2 | 2.78 | 3 / 3.36 | 20 | 15 | 91 | 171 | 0.0724 | 0.198 | 0.6782 | 672.112 | 0.3493 |
| 2017-06 | 49 | 112 | 74 | 2 | 2.91 | 2 / 3.31 | 32 | 27 | 87 | 160 | 0.106 | 0.1473 | 0.6805 | 748.372 | 0.4305 |
| 2017-11 | 50 | 137 | 41 | 2 | 2.84 | 2 / 3.77 | 36 | 32 | 79 | 202 | 0.1416 | 0.1528 | 0.671 | 845.121 | 0.5487 |
| 2018-06 | 51 | 133 | 80 | 2 | 2.86 | 3 / 3.7 | 33 | 28 | 91 | 206 | 0.1474 | 0.3669 | 0.7258 | 1210.915 | 0.7156 |
| 2018-11 | 52 | 154 | 51 | 1 | 2.75 | 3 / 3.94 | 34 | 31 | 91 | 227 | 0.133 | 0.19 | 0.6895 | 1414.956 | 0.8748 |
| 2019-06 | 53 | 94 | 49 | 2 | 2.92 | 2 / 3.93 | 34 | 31 | 83 | 220 | 0.1274 | 0.1434 | 0.679 | 1559.575 | 1.021 |
| 2019-11 | 54 | 102 | 37 | 2 | 3.07 | 3 / 4.19 | 34 | 30 | 86 | 228 | 0.1118 | 0.1346 | 0.6938 | 1646.887 | 1.142 |
| 2020-06 | 55 | 58 | 25 | 3 | 3.46 | 3 / 4.47 | 43 | 39 | 84 | 226 | 0.0868 | 0.2964 | 0.7858 | 2206.134 | 1.228 |
| 2020-11 | 56 | 44 | 31 | 3 | 3.91 | 4 / 4.71 | 42 | 39 | 77 | 214 | 0.0848 | 0.0958 | 0.6423 | 2428.762 | 1.3168 |
| 2021-06 | 57 | 58 | 49 | 4 | 4.17 | 4 / 4.6 | 38 | 34 | 121 | 188 | 0.1049 | 0.1679 | 0.6485 | 2786.059 | 1.511 |
| 2021-11 | 58 | 70 | 61 | 4 | 4.38 | 4 / 4.52 | 45 | 41 | 153 | 173 | 0.1147 | 0.1243 | 0.6408 | 3036.862 | 1.6491 |
| 2022-06 | 59 | 39 | 39 | 4 | 4.84 | 3 / 4.71 | 52 | 47 | 172 | 173 | 0.0854 | 0.3266 | 0.7276 | 4403.083 | 1.6491 |
| 2022-11 | 60 | 41 | 39 | 5 | 5.13 | 3 / 4.77 | 50 | 46 | 204 | 162 | 0.0766 | 0.0747 | 0.6204 | 4864.384 | 1.729 |
| 2023-06 | 61 | 44 | 43 | 5 | 5.47 | 4 / 5.06 | 70 | 63 | 221 | 134 | 0.1364 | 0.0548 | 0.6185 | 5239.025 | 1.872 |
| 2023-11 | 62 | 47 | 47 | 5 | 5.73 | 4 / 5.29 | 74 | 66 | 220 | 104 | 0.1102 | 0.262 | 0.6625 | 7031.841 | 2.015 |
| 2024-06 | 63 | 46 | 46 | 5 | 5.96 | 5 / 5.6 | 90 | 75 | 239 | 80 | 0.1045 | 0.1008 | 0.6782 | 8213.337 | 2.1299 |
| 2024-11 | 64 | 54 | 54 | 6 | 6.1 | 5 / 5.73 | 92 | 76 | 261 | 63 | 0.0608 | 0.3001 | 0.6362 | 11723.13 | 2.3102 |
| 2025-06 | 65 | 48 | 48 | 6 | 6.39 | 5 / 6.07 | 113 | 93 | 254 | 47 | 0.0963 | 0.1672 | 0.6705 | 13837.531 | 2.435 |
| 2025-11 | 66 | 45 | 45 | 5 | 6.1 | 5 / 5.78 | 106 | 86 | 243 | 40 | 0.0876 | 0.07 | 0.6938 | 14993.513 | 2.574 |
| 2026-06 | 67 | 43 | 42 | 5 | 6.01 | 5 / 5.72 | 117 | 98 | 240 | 31 | 0.0802 | 0.2128 | 0.6449 | 18732.742 | 2.6615 |
| 2026-11 | 68 | 28 | 27 | 6 | 6.4 | 5 / 6.25 | 138 | 124 | 256 | 18 | 0.0898 | 0.0508 | 0.6146 | 19710.577 | 2.8676 |

Newcomer Rmax shares run higher in June than in November in most years, so compare like editions.

### November lists 1993–2026: proxy newcomers and Year-field age

| November list | proxy newcomers (Site/Year) | First Appearance newcomers | median age by Year (yr) | entries with Year 5+ yr old |
|---|---|---|---|---|
| 1993 | 83 | — | 1 | 28 |
| 1994 | 111 | — | 1 | 15 |
| 1995 | 157 | — | 1 | 8 |
| 1996 | 179 | — | 0 | 4 |
| 1997 | 176 | — | 0 | 8 |
| 1998 | 198 | — | 0 | 6 |
| 1999 | 207 | — | 0 | 8 |
| 2000 | 195 | — | 0 | 4 |
| 2001 | 183 | — | 0 | 7 |
| 2002 | 173 | — | 0 | 9 |
| 2003 | 202 | — | 0 | 5 |
| 2004 | 150 | — | 0 | 5 |
| 2005 | 211 | — | 0 | 2 |
| 2006 | 148 | — | 0 | 3 |
| 2007 | 210 | — | 0 | 3 |
| 2008 | 167 | — | 0 | 1 |
| 2009 | 145 | — | 0 | 0 |
| 2010 | 145 | — | 0 | 1 |
| 2011 | 141 | — | 0 | 5 |
| 2012 | 156 | 165 | 0 | 4 |
| 2013 | 122 | 129 | 0 | 5 |
| 2014 | 78 | 68 | 1 | 9 |
| 2015 | 140 | 136 | 1 | 13 |
| 2016 | 107 | 113 | 1 | 19 |
| 2017 | 139 | 137 | 1 | 34 |
| 2018 | 138 | 154 | 1 | 28 |
| 2019 | 91 | 102 | 1 | 27 |
| 2020 | 45 | 44 | 2 | 35 |
| 2021 | 70 | 70 | 2 | 39 |
| 2022 | 43 | 41 | 2 | 58 |
| 2023 | 50 | 47 | 2 | 78 |
| 2024 | 56 | 54 | 3 | 95 |
| 2025 | 47 | 45 | 3 | 111 |
| 2026 | 29 | 28 | 3 | 139 |

The 1993 row compares with the June 1993 list only. June-list proxy values are in `series.csv`.

### Cohort survival

| cohort (first list) | newcomers | on list 6 ed later | 10 ed later | non-China newcomers | non-China 6 ed later | non-China 10 ed later |
|---|---|---|---|---|---|---|
| 2012-06 | 167 | 35 | 15 | 140 | 34 | 15 |
| 2012-11 | 165 | 35 | 9 | 143 | 35 | 9 |
| 2013-06 | 178 | 17 | 5 | 140 | 16 | 4 |
| 2013-11 | 129 | 19 | 8 | 111 | 18 | 8 |
| 2014-06 | 114 | 17 | 6 | 86 | 15 | 6 |
| 2014-11 | 68 | 13 | 6 | 64 | 12 | 5 |
| 2015-06 | 89 | 27 | 14 | 84 | 26 | 14 |
| 2015-11 | 136 | 17 | 7 | 49 | 11 | 7 |
| 2016-06 | 154 | 12 | 5 | 82 | 10 | 4 |
| 2016-11 | 113 | 18 | 11 | 78 | 18 | 11 |
| 2017-06 | 112 | 12 | 10 | 74 | 11 | 9 |
| 2017-11 | 137 | 5 | 2 | 41 | 5 | 2 |
| 2018-06 | 133 | 58 | 24 | 80 | 47 | 21 |
| 2018-11 | 154 | 45 | 9 | 51 | 26 | 8 |
| 2019-06 | 94 | 40 | 23 | 49 | 16 | 14 |
| 2019-11 | 102 | 64 | 15 | 37 | 14 | 9 |
| 2020-06 | 58 | 53 | 26 | 25 | 22 | 18 |
| 2020-11 | 44 | 37 | 23 | 31 | 24 | 16 |
| 2021-06 | 58 | 51 | 38 | 49 | 42 | 33 |
| 2021-11 | 70 | 56 | 39 | 61 | 47 | 33 |
| 2022-06 | 39 | 24 | — | 39 | 24 | — |
| 2022-11 | 41 | 26 | — | 39 | 24 | — |
| 2023-06 | 44 | 35 | — | 43 | 34 | — |
| 2023-11 | 47 | 41 | — | 47 | 41 | — |

"Non-China 6 ed later" counts cohort members whose Country is not China in the later list. Cohorts from 2024-06 on are too young for a six-edition reading.

### Composition of the 138 five-year-plus entries, November 2026 (from checks.txt)

- By First Appearance: 41:1, 47:1, 48:1, 49:3, 51:6, 52:6, 53:11, 54:10, 55:12, 56:16, 57:32, 58:39.
- By country: United States 45, China 14, Germany 12, France 12, Japan 10, Russia 5, South Korea 4, Brazil 4.
- By segment: Research 44, Industry 42, Academic 33, Vendor 9, Government 8, Others 2.
- Rank quartiles 201, 313.5, 428; best rank 9.

### The mechanism, stated for a diagram

The list has a fixed 500 slots, so each edition's newcomers equal its departures. An entry's Rmax rarely changes, so it leaves when the No. 500 threshold rises past it. An entry that comes in at m times the threshold survives about log(m)/log(1+g) years, where g is the threshold's annual growth. With m = 2, that is 1.5 years at g = 60% (the 2016–2018 pace was 57–69%) and 6.4 years at g = 11.4% (2025 and 2026). This is arithmetic on the definitions, not a TOP500 statement. The threshold series above supplies g.

## Limits

- The files cannot show where new compute went. The AI-factory explanation is the TOP500 release's suggestion built on Epoch AI ownership data. No source counts AI clusters that could run HPL and did not submit.
- Epoch's 2.5x per year measures quarterly additions of 8-bit peak capacity in H100e. It is not comparable with HPL Rmax (FP64, measured), so a chart setting HPL growth against "AI compute growth" sets two different units against each other. I did not convert between them, and no source does.
- First Appearance has no published definition. Its behaviour (kept through upgrades and re-entry, reset by a new System ID) is inferred from the files.
- Why the No. 500 threshold slowed after 2019 is not established by any source read. The candidates are China's exit, fewer mid-sized submissions, and large systems concentrated at the top. The data show only the slowing.
- The cause of the 27-versus-28 discrepancy (Horizon's apparent late addition) is unconfirmed. No document states it.
- Pre-2012 newcomer counts are a proxy calibrated against First Appearance (error −16 to +23 per list). They are good enough to say no list from 1993 to 2011 came near 28. They are not exact counts.
- Whether the November 2026 dip is a pause cannot be settled until the June 2027 list (due at ISC 2027).

## Source assets

```text
Asset: TOP500 release, table of the top five systems (rank, system, site, country, HPL in EF/s), under "The Top 10 Is Completely Unchanged".
Shows: only the unchanged leaders; it carries none of the turnover argument.
Crop:  None needed; prose figures suffice.
```

```text
Asset: Epoch AI Data Insight "New global AI computing capacity is doubling every 9 months", interactive chart and table "Computing capacity of AI chips sold each quarter by designer (H100e)", Q1 2024–Q2 2026.
Shows: the 2.5x per year trend in quarterly additions, by chip designer.
Crop:  the chart renders only with JavaScript; the table values are in the page and can be charted directly with Epoch credited (CC BY). Must retain the H100e unit label.
```

```text
Asset: Next Platform article, two tables of newcomers (six-list summary June 2024–Nov 2026 by architecture; Nov 2026 newcomer feeds and speeds).
Shows: Prickett Morgan's own newcomer tallies by architecture.
Crop:  secondary; not recommended as evidence since the counts come from the list files, which the article's own figures partly contradict (27 vs 264 total).
```

TOP500 list files: None found as a visual. The charts for this piece have to be drawn from `series.csv` and `cohort_survival.csv`. Candidates: newcomers per edition 2012–2026 split China/non-China, with the 1993–2011 proxy as context; cohort survival curves; No. 500 threshold growth against total Rmax growth; age distribution stacked by First Appearance.

## Discarded

```text
https://www.top500.org/resources/frequently-asked-questions/: covers the Linpack benchmark only; no definition of list fields.
https://epoch.ai/data-insights/computing-capacity: an October 2024 insight on leading companies' chip holdings; superseded by the 2026 insights for every figure the release cites.
https://epoch.ai/data/ai-chip-owners: data explorer page (updated May 12, 2026); its figures render only with JavaScript, and the 71% figure is taken from the Data Insight that states it.
https://epoch.ai/gradient-updates/frontier-labs-dont-use-most-ai-compute: an opinion newsletter (Josh You, 20 May 2026) on frontier-lab compute shares, flagged by Epoch as the author's own view; not the source of any release figure.
https://www.top500.org/system/180518/: Horizon's system page; the fetched HTML held only navigation, no dates or list history.
https://the-decoder.com/global-ai-compute-hits-15-million-h100-equivalents-epoch-ai-finds/: secondary retelling of Epoch's January figure; the Epoch post itself is cited.
Web search summaries (TOP500 field definitions, Horizon on the list): no document behind them stated the facts asked; each was checked against the primary pages above.
```
