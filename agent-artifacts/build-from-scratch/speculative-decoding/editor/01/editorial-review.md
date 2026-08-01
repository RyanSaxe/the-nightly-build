# Editorial review — build-from-scratch/speculative-decoding (editor, round 01)

Three ordered reads at high effort, plus the brief's critical technical checks
(accept/reject rule vs. the papers, a fresh re-run of the committed script,
`data-nb-kind` audit, active-content check). Decision at the end.

## Skeptic

Skeptic: thesis "speculative decoding's speedup does not come from trusting the
draft; it comes from a specific rejection-sampling rule — accept `x` with
probability `min(1, p(x)/q(x))`, resample the normalized residual
`norm(max(0, p−q))` on rejection — that provably reproduces the target's exact
distribution, demonstrated by a from-scratch, fully enumerable implementation";
tested 5 claims; broke: none central. Two numeric slips fixed directly (below).

Claims tested and how they held:

1. **The accept/reject rule and residual.** Verified in BOTH the code and the
   article's equation against both founding papers. Code (`speculative_step`):
   `ratio = min(1.0, p_dists[i][x] / q_dists[i][x])`, accept on
   `rng.random() <= ratio`, resample `residual_dist = norm(max(0, p − q))` on
   the first rejection, bonus token from `p_dists[gamma]` when all accepted —
   exactly Leviathan et al. Algorithm 1. Article Fig. 2:
   `Pr(accept x) = min(1, p(x)/q(x))`, `p'(x) = norm(max(0, p(x)−q(x)))` —
   matches the papers and the code. The verbatim Leviathan quote and the Chen
   et al. letter-swap note (q=target, p=draft) match the evidence record word
   for word. The `1−β` cancellation prose matches Appendix A.1 / Theorem 1.
2. **Empirical exactness.** RE-RAN `speculative_decoding.py` myself; stdout is
   byte-identical to the committed `run_output.txt` (seeded, `random.seed(1729)`).
   Every number quoted in the prose and all four tables is a real output:
   single-token max |diff| 0.00146, joint two-token TV distance 0.01523 over
   all 324 pairs, the five-row α/tokens-per-step table, and the α≈0.726 /
   2.92-tokens result at w=0. Nothing invented.
3. **Acceptance rate governs speedup.** β = Σ min(p,q), α = E[β],
   E[#tokens] = (1−α^(γ+1))/(1−α), speedup needs α>c — all match Leviathan
   §3.1–3.3 (Eq. 1, Thm 3.8, Cor 3.9) as transcribed in the evidence.
4. **Real-model α figures.** α≈0.20 (bigram/T5-XXL), 0.88–0.89 (6M/97M),
   0.74–0.75 (LaMDA 8B/137B): all match evidence entries #3–#5.
5. **Follow-on systems keep the same test.** Medusa 2.2x+/2.3–3.6x, EAGLE
   2.7–3.5x, Draft & Verify ≤1.99x, Lookahead ≤1.8x (4x multi-GPU-specific),
   PyTorch gpt-fast 2x vs 1.3x, vLLM ≤1.5x/2.8x at low QPS reversing to
   1.4–1.8x slowdown at high QPS: every quote and number matches the evidence,
   including the workload/regime qualifiers.

Display text verified descriptor by descriptor: title, dek, all seven flex
subheads. Headline "A rejection rule keeps speculative decoding's output exact"
is the largest claim, defended, no colon/question/triad. Dek supplies method
(two hand-built character models, 200,000 draws) plus the second finding
(tokens surviving as the draft improves); no banned hedged-contrast mold.

**Two numeric slips found and fixed directly (correct value at hand):**
- "That sits inside the 2X-3X range Leviathan et al. measured" — the number it
  cites, the computed 3.381× speedup, is above 3× and does not sit inside a
  2–3× band. Changed "sits inside" → "sits just above." Honest and preserves
  the point (the toy's projection lands in real-scale territory).
- "tracks the formula within 0.009 throughout" — the largest measured deviation
  is 0.0091 (w=0.30, 3.4152 vs 3.4061), which exceeds 0.009. Changed to
  "within 0.01."

`data-nb-kind` audit: all 8 sources labeled `primary`. Correct — each is the
party that owns the claim it is cited for (the two founding papers for the
algorithm/proof; the four follow-on papers, PyTorch, and vLLM each for their
own measured speedup). Matches the evidence record's classifications.

Active content: no authored live scripts. The only `<script>` tags are the
JSON `#nb-meta` payload and the fixed engine `nb.js` asset; the code is a
rendered `<pre><code>` listing. No inline event handlers. Confirmed clean.

## Cut

Cut: 2 sentences/phrases; worst tell: the orientation's closing signpost "The
rest of this piece builds it, then checks it against two hundred thousand
draws" — a where-the-piece-will-go preview, redundant with the dek's "two
hundred thousand times." Removed; the paragraph now closes stronger on
"...small enough to run to completion in a few hundred lines of Python." Also
trimmed the internal self-reference "from the sections above" in "None of this
is a flaw in the proof from the sections above." The rest of the piece is
disciplined: each `nb-code` block carries an argument, run output is reported
as plain data, the accept/reject rule is earned in prose before it is named,
and no em-dash reflex survives (0 em-dashes). Voiced lines ("The table above is
that proof, run") carry cargo and stay.

## Reader

Reader: this gives me a runnable, fully enumerable instantiation of the
exactness proof — two explicit distributions I can see in full, the
draft-then-verify loop built against them, and committed numbers showing the
`min(1,p/q)`+residual sampler reproduces the target distribution and how
acceptance rate converts to tokens-per-call as the draft improves. The papers
prove this symbolically; none hands over a running artifact with its own
measured match. That is exactly the original-work claim in `draft-handoff.md`,
and it survives. Prose sits with the Annotated-Transformer / Norvig exemplars
(code and empirical closure carry the argument), not a median AI summary.
Headline reread as the largest claim: true and defended.

## Proof

Split the flagged 59-word run-on (the math-heavy Leviathan verbatim quote,
punctuation score 35) into two sentences, each under the checker's 40-word
evaluation floor, keeping both quote fragments verbatim ("keeping it if
q(x) ≤ p(x)." / "reject the sample with probability... instead."). Updated
`nb-meta` words 3764 → 3746 to match the recount after cuts (reading_minutes 19
and sources 8 unchanged).

`nb check ... --series build-from-scratch` → **BLOCK: 0, WARN: 0**, verdict
PUBLISHABLE.

## Direct edits made

1. Split the 59-word Leviathan quote sentence into two (clears
   W-SENTENCE-DENSITY).
2. Cut the orientation signpost sentence.
3. Trimmed "from the sections above."
4. "sits inside the 2X-3X range" → "sits just above the 2X-3X range."
5. "within 0.009 throughout" → "within 0.01 throughout."
6. `nb-meta` words 3764 → 3746.

## Required work by owner

None. No researcher or writer redraft required.

## Decision

Approve. BLOCK: 0, WARN: 0. All numbers re-verified against a fresh run; the
accept/reject rule matches both papers in code and equation; sources correctly
classified; no active content.
