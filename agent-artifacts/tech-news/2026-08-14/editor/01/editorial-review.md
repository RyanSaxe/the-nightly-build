# Editorial review: tech-news/2026-08-14 (editor/01)

## Skeptic

This is a brief: six items, each a standalone judgment about what moved, so
each item heading and its prose is its own claim. The page-level thesis, carried
by the headline and dek, is that Anthropic flipped Claude Code to auto mode by
default on 14 August on the strength of a study it ran itself. The lead follows
the commission's steer away from a fourth straight security-led edition; it
holds.

Headline and dek, tested together. The headline commits to "catching 800
dangerous commands human reviewers missed"; the primary (opened, confirmed)
gives "auto mode blocked 800 commands that a human approved, while humans blocked
only 6 that auto mode allowed." The dek carries the reciprocal 6 and the caveat
in the same breath — "a study Anthropic designed, ran, and graded itself" — which
is exactly where a self-reported figure's caveat belongs and what this round asks
for. The two head-to-head numbers (800 and 6) are split honestly between headline
and dek rather than the headline taking only the flattering one. The dek makes a
claim about the world, not a grade of the article's method. Both hold.

Self-reported figures, item by item. Every AI-lab capability and safety number
is attributed to the lab that reported it in the same sentence it appears: "In a
study Anthropic designed and ran itself" (item 1), "under evaluation rules Z.ai
designed itself" and a table captioned "Z.ai's self-reported cyber-benchmark
scores" (item 2), "an API tier it says runs" and "OpenAI frames" (item 3), and
Gemini's table read through VentureBeat rather than stated as fact (item 4). None
is laundered into settled fact. This is the round's central risk and the draft
handles it throughout.

The cyber-benchmark table, read cell by cell against the evidence Numbers block:
GLM-5.3 CyberGym 84.5 / ExploitBench 54.4; GPT-5.6 Sol 83.6 / 76.5; Mythos 5 83.8
/ 78.0. Every cell matches. Read as a reader, the table is honest against its own
prose: the surrounding sentences describe a "cyber-capability jump," and the table
shows GLM-5.3 leading on CyberGym but trailing both rivals badly on ExploitBench
(54.4 against 76–78). The item does not hide the half of the picture that cuts
against the framing, and the caption attributes the whole table to Z.ai's own
harness.

The reasoning-trace discrepancy (item 5). The arXiv abstract (opened, confirmed:
367 PII artifacts, 182 credentials from 315,320 blocks) and The Hacker News
(opened, confirmed: 704 privacy artifacts, 62 API keys / 33 passwords / 24 access
tokens / 7 private keys from genuine user sessions) give different totals. The
draft states both, notes the 704-set is the post-benchmark-exclusion "genuine
user sessions" subset, sums the credential components to 126, and writes plainly
that "the two counts do not reconcile in what either outlet published." It weighs
the gap rather than silently picking a number, as the brief required.

IonNet as a continuing item (item 6). The prose dates it "in early August" and
closes by "placing the paper's publication in the week before this edition rather
than on it." It is flagged as continuing, not breaking today, per the evidence's
instruction. Its four headline figures (4,500 → 87; ~5,000,000 → 62,935; 154,718
→ 4,583 → 102; 20 checked, 13 confirmed; ~eight-order-of-magnitude speedup) all
match the evidence.

One break, fixed. Item 2 attributed the "Claude Code 2.1.207 harness"
specifically to the Terminal-Bench and DeepSWE coding scores. The evidence ties
that harness version only to CyberGym (Numbers block, CyberGym scope line); the
Source 1 record documents no harness for the coding benchmarks, and the Z.ai
primary would not render through the fetcher, so I could not confirm the harness
ran suite-wide. The self-reported framing is the essential point and is
independently supported (Contradictions: "protocols the company designed and
tuned"), so I cut the unverified harness-version detail and kept "both scored
under evaluation rules Z.ai designed itself." Nonessential, unsupported detail
removed rather than routed.

Display text, descriptor by descriptor. Item headings check out against the
evidence: GLM-5.3's Terminal-Bench 4.6 → 28.3 is ~sixfold (6.15x); Ultrafast's
"up to 14 times faster" and "without shrinking the model" match OpenAI's
size-decoupling framing; Gemini 3.7 Flash "trails GPT-5.6 Terra and Claude Sonnet
5 on Google's own benchmark table" matches VentureBeat's read; IonNet "nearly
63,000 ... from a 5-million-compound search" matches 62,935 from ~5M. Named
actors, dates, and quantities in headings and prose all trace to their owning
source. Apollo Research is correctly "the UK's" (primary confirms "UK-based");
the 12% → 7% miss rate is on a "held-out attack set" as the evidence states.

Sourcing labels. All six primaries are the owning documents; all six secondaries
are independent newsrooms with no stake. The two writer-flagged source titles
were writer-constructed descriptions rather than literal page titles. I opened
both pages and swapped in the literal titles (see Edits), which is display text a
reader meets and better set exact. Hrefs: arXiv, The Hacker News, and the
Anthropic blog opened and landed on the source with figures confirmed. The Z.ai
blog (JS page), science.org, openai.com, and venturebeat.com returned empty or
403 to the automated fetcher — a known bot-block on those hosts, not evidence the
link fails for a reader; each href is the canonical source address the evidence
record used, and every figure drawn from them cross-checks against that record.

## Cut

A dedicated slop pass against `spec/slop.md`, sentence by sentence and then along
the edges out of order: no individual sentence failed the placeholder test. The
prose is terse wire-service reporting; every edge sentence carries a fact (a
figure, a date, an independent corroboration), so the openers and closers survive
the delete test. No empty conclusions, no decorative "highlighting/underscoring"
clauses, no vague attribution, no self-reference. The one earned negative-parallel
contrast (item 2's "rather than spotting isolated flaws") mirrors the primary's
own "did not simply ... it began to" framing, so it stays.

One repeated pattern, fixed. Four of six items closed on the same construction —
"[Outlet] independently confirmed [figures]" (items 1, 2, 3, 6). Within a single
brief that reads as a stamped closer even though each carries a real corroboration
fact. I varied the two barest instances: item 1 now reads "TechCrunch, an outside
newsroom, reported the same rollout date and study figures," and item 3 now reads
"TechCrunch corroborated the speed figures and the Cerebras partnership the same
day." Items 2 and 6 keep "independently confirmed" because each already carries a
distinguishing clause (the weights-delay caveat; the continuing-status flag), so
two differentiated uses across six items is acceptable variety.

Leakage check against the brief, commission, and voice guide: no planning labels,
selection rules, or "the article fulfilled its assignment" claims survived into
the prose. Headings do not echo the recent front pages (08-13 Zoom chain, 08-12
eclipse, 08-11 Riemann/cyber-model). The probiotics paper that ran 08-13 is
correctly absent. Grammar and punctuation are clean; no em-dash or reflex-mark
repairs needed.

## Reader

Read straight through as the paper's ML-engineer reader: what I have that the
sources alone would not give me is the day's six developments selected and
ranked, with every self-reported lab figure tagged as the lab's own and the one
genuine data conflict (the reasoning-trace counts) held open instead of papered
over. That curation and consistent caveating is the brief's own work, and it
survives; the original-work sentence in the handoff claims the same and matches
what is on the page. The prose sits closer to the voice-guide exemplars than to a
median summary: it states finding and significance in the same breath, anchors
numbers, and keeps each caveat next to its result rather than filed away. The
headline reads as the largest claim and the piece defends it.

## Edits

- Item 2: cut "inside a Claude Code 2.1.207 harness" from the Terminal-Bench /
  DeepSWE sentence; kept "both scored under evaluation rules Z.ai designed
  itself." (Harness version unsupported by the evidence for the coding
  benchmarks.)
- Item 1 closer: "TechCrunch independently confirmed the rollout date and the
  study's headline figures." → "TechCrunch, an outside newsroom, reported the
  same rollout date and study figures." (Break the repeated-closer formula.)
- Item 3 closer: "TechCrunch independently confirmed the speed figures and the
  Cerebras partnership the same day." → "TechCrunch corroborated the speed
  figures and the Cerebras partnership the same day." (Same.)
- Source s9 title: writer's descriptive label → the paper's literal title,
  "Stealing Reasoning Traces from Proprietary LLM APIs" (opened and confirmed).
- Source s10 title: writer's descriptive label → the article's literal
  headline, "OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode
  Stronger Models' Reasoning" (opened and confirmed).

## Required work

None blocking; no new reporting or evidence is needed and the decision is
approve. Two non-blocking notes recorded for routing:

- writer (optional): if the Z.ai benchmark table's own footnote attributes the
  Claude Code 2.1.207 harness to Terminal-Bench and DeepSWE suite-wide (I could
  not render that page), the harness detail I cut from item 2 may be restored.
  Not required; the item is complete without it.
- researcher / orchestrator (process, not this article): the writer caught, and
  the evidence record missed, that the glucose-responsive probiotics paper
  (s41586-026-10909-6) already ran as the 08-13 lead health item. The item was
  correctly dropped, so nothing on this page needs changing; surfaced so the
  researcher checks the recent library before naming a candidate, per the
  handoff's request.

## Decision

approve — the six items are faithful to the evidence, each self-reported figure
is attributed to its lab, the reasoning-trace discrepancy is held open rather
than resolved, the cyber table checks cell by cell and reads honestly, and IonNet
is flagged as continuing; my direct edits resolved the unsupported harness detail,
the two approximate source titles, and the repeated-closer formula, leaving no
publication-blocking work.
