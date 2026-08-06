# Editorial review: paper-of-the-day/instructgpt (editor/01)

## Skeptic

**Thesis.** The paper's durable object is not the headline ("a 1.3B model
outranks a 175B one") but the KL-regularized preference objective (Eq. 2), which
InstructGPT assembled from an existing lineage rather than invented; that
objective survives two later verdicts — Gao's over-optimization (the β-KL term is
load-bearing) and DPO's closed form (the RL loop is removable, the KL leash is
not) — while the small-beats-large result is real but scope-bound to human
preference on OpenAI's own prompt distribution against a specific baseline.

The four load-bearing claims and how each held:

1. **The headline preference result, stated with its exact reference points.**
   Verified against the evidence record. The article does the precision work the
   brief demanded: the abstract's "1.3B preferred to 175B GPT-3" is kept distinct
   from Figure 1's win-rate curve (measured against the 175B **SFT** model, not
   GPT-3), the table labels the 85±3% (plain) and 71±4% (few-shot) numbers as
   **175B InstructGPT** vs 175B GPT-3, and the metric is framed as preference by
   ~40 labelers at 72.6±1.5% agreement, aligned to "labelers and researchers,"
   with the verbosity confound named. Not framed as capability or truthfulness.
   Held.

2. **InstructGPT assembled and scaled an existing lineage.** Each lineage
   citation genuinely supports the point at the exact sentence that makes it:
   Christiano 2017 at the Bradley-Terry introduction (preference-to-reward on
   Atari/robotics); Ziegler 2019 at the KL penalty (first KL leash on a
   pretrained LM, GPT-2) and reprised for its self-reported heuristic
   exploitation; Stiennon 2020 in the pipeline section (same SFT→RM→PPO+KL a year
   earlier, overlapping team); Schulman 2017 where PPO is named (clipped
   surrogate). None pads the count. Held.

3. **The β-KL term is load-bearing (Gao).** The over-optimization section states
   the mechanism (gold reward rises, peaks, falls in √KL; the closed-form
   R_bon/R_RL fits) and carries Gao's own scope limit (synthetic — a gold RM
   substitutes for humans). Held.

4. **The RL loop is removable (DPO).** The closed-form section derives Eq. 4 → 5
   → 7 correctly and carries DPO's scope limit (off-task: sentiment,
   summarization, single-turn), calling it directional rather than a head-to-head
   win at InstructGPT's task. Held.

**Break found (fixed).** The Verdict block conflated two distinct measurements.
It read "the claim that a small model beat a large one stands only with its
baseline named, 85 ± 3% against a plain 175B GPT-3 and 71 ± 4% against a prompted
one." But per the evidence record those figures are the **175B** InstructGPT vs
175B GPT-3 numbers, not the 1.3B-vs-175B small-model claim; the body's own table
correctly labels them "175B InstructGPT preferred to…". Attached to "a small
model beat a large one," they tell the reader the 1.3B model won 85% of the time,
which is false. This is exactly the abstract/figure conflation the brief and the
evidence record warned against ("Both are real; do not conflate them"). Fixed by
cutting the mis-attributed numeric clause; the correct numbers, correctly
labeled, remain in the small-beats-large table and prose, so nothing true was
lost. The Verdict now reads "…stands only with its baseline named."

**Equations.** All displayed math matches the evidence record's Numbers section
term for term: RM ranking loss (Eq. 1), the PPO+β-KL+γ-ptx objective (Eq. 2), the
KL-regularized objective (DPO Eq. 3 = Eq. 2 with γ=0, with π_ref in the SFT
role), the closed-form optimal policy (Eq. 4) and its Z(x), the reparameterized
reward (Eq. 5), the DPO loss (Eq. 7), the implicit reward r̂_θ, and Gao's
R_bon/R_RL with d=√KL. The Eq. 3 ≡ Eq. 2 identity is legitimate: the article had
already shown the expected log-ratio is the KL divergence, so E[r − β log(π/π_ref)]
= E[r] − β·KL. No math routed back.

**data-nb-kind audit.** All nine sources carry `primary`, and each is primary for
the claim it is cited on (each paper owns its own equations/results; the OpenAI
release is the authoring party's; Saito owns the verbosity-bias claim). No claim
in the piece needs an independent secondary that a primary is masking. Clean.

**Citation hrefs.** Opened all nine Source URLs. Titles and authors confirmed
correct for Stiennon (2009.01325, NeurIPS 2020), Christiano (1706.03741), Ziegler
(1909.08593), Schulman (1707.06347), Saito (2310.10076 — verbosity bias, "GPT-4
prefers longer answers more than humans" confirmed), Gao (2210.10760), Rafailov
(2305.18290), and InstructGPT (2203.02155). The OpenAI page returns HTTP 403
(bot-gated, not dead) at the resolvable `openai.com/index/instruction-following/`,
exactly as the brief predicted, and the paper's abstract owns every number it
carries. Venue strings honor the evidence flags: only Stiennon's NeurIPS 2020 is
printed; all others are year-only. No venue invented. Figure-caption cites
disclose the paper's original figure numbers via `data-nb-note` (article Fig. 1 =
paper Fig. 2; article Fig. 2 = paper Fig. 1), which is honest.

## Cut

Four direct cuts, all removing tells rather than cargo:

- **Verdict conflation** (skeptic finding above): cut the mis-attributed 85/71
  clause.
- **Self-reference / signpost:** "the direct-optimization result *at the end of
  this piece* will exploit" → removed the self-locating phrase; the substantive
  foreshadowing (RM learns only from differences, which DPO exploits) stays.
- **Forward signpost:** "…where the durability of the whole scheme is decided,
  *and the after-record spends most of its effort on it*." — cut the clause that
  narrates the article's own structure.
- **Self-grading meta:** "The result the paper is known for is a preference, *and
  stating it precisely matters as much as stating it*." — cut the throat-clearing;
  the section then demonstrates the precision without announcing it.

**Worst tell:** the Verdict conflation — a prominent furniture block asserting a
number the body itself contradicts.

**Pattern check.** The recent-pattern habits are broken: the piece opens on the
next-token/instruction gap, not a bare quantitative record, and closes on a
falsification condition ("what would change the assessment"), not a "what the
field kept" refrain. Licensed mechanistic contrasts (proof vs measurement, what
DPO removes vs keeps) are within the voice guide's technical-pairing license; the
one rhetorical "not X but Y" (target is not a next-token predictor but a
helpful/honest/harmless model) is earned and within the ceiling. One minor,
non-blocking cadence note: two of eight headings use the comma-"and" two-clause
shape ("The reward model is a proxy, and proxies can be gamed"; "What the claim
was, and what still stands on it") — not a formula at two instances, but worth
watching if the writer touches headings.

The three W-SENTENCE-DENSITY warnings are on the two displayed equations and the
one inline-math derivation sentence, per the handoff — the density heuristic
reading TeX thin-spaces/braces as prose, not genuine run-ons. Confirmed; nothing
to split.

## Reader

Read straight through as the paper's declared reader (ML engineer, comfortable
with set notation): what I get beyond the sources is a way to reason about RLHF
that none of the three papers states about itself — that Eq. 2 is the real,
durable object, and that Gao and DPO are two verdicts on that single objective
(the KL term provably cannot be dropped; the RL loop provably can). That matches
the original-work sentence in writer/01's handoff, and the rl-objective →
overoptimization → closed-form → verdict arc delivers it. The prose sits closer
to the voice-guide exemplars than to a median summary: it choreographs each
display in the announce → show → read-back-a-term beat, presses the durability
verdict through the specific term (β / the KL leash) rather than adjectives, and
weighs each after-record result by what it measured before crediting it.

## Edits

- Verdict: cut ", 85 ± 3% against a plain 175B GPT-3 and 71 ± 4% against a
  prompted one" (mis-attributed the 175B-vs-175B numbers to the 1.3B small-model
  claim).
- Reward-model section: cut "at the end of this piece" from "the direct-
  optimization result … will exploit" (self-reference).
- RL-objective section: cut ", and the after-record spends most of its effort on
  it" (structural signpost).
- Small-beats-large section: cut ", and stating it precisely matters as much as
  stating it" (self-grading meta).
- Ran `nb stamp`: words 3256 → 3214, reading_minutes 14, sources 9.

## Required work

None blocking. Optional, for the writer if the piece is reopened for other
reasons (do not open the loop solely for these):
- The Verdict could re-state baseline-dependence with the correctly-labeled 175B
  numbers, but the body already carries them correctly, so this is polish, not a
  gap.
- Two comma-"and" headings could be varied if headings are touched.

## Decision

approve — the one factual error (the Verdict's abstract/figure conflation) is
fixed by a surgical cut, three tells are cut, and the math, citations,
data-nb-kind labels, source-asset figures, and headline reference-point precision
all verify against the evidence record.
