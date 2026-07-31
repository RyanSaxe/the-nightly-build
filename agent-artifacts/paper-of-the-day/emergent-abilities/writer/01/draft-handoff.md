# Draft handoff — writer/01 — paper-of-the-day/emergent-abilities

## Article
`.nb-work/paper-of-the-day/emergent-abilities/library/paper-of-the-day/emergent-abilities.html`

No asset files changed (no `nb asset` or `nb chart` used — see rationale below).

## The one act of original work

The article rebuilds Wei et al.'s definition and Schaeffer et al.'s rebuttal
each in full before letting them collide, then draws a precise map of where
they actually agree, where Schaeffer's classification-metric result directly
answers the specific objection Wei et al. raised in their own Section 5.1
(rather than talking past it), and where neither paper's mathematics
resolves the dispute at all (Barak's multi-step compounding gap). It
separates what is demonstrated artifact (the metric-swap effect, shown
concretely on the same GPT-3/InstructGPT outputs under two scoring rules)
from what survives as a real, unresolved practical fact (a deployment stuck
with a discontinuous metric still faces a genuinely unpredictable threshold).
Neither source paper states this separation in these terms; it is the
article's synthesis, not a restatement of either abstract.

## Word / source counts

- Words: 2,858 (band: 1,800–3,400)
- Sources: 10, all read by the researcher and cited; numbered in
  first-citation order (s1 Wei et al. → s10 Havlík)
- Flex sections: 5 (`what-wei-called-emergent`,
  `the-objection-in-the-paper-itself`, `one-task-two-rulers`,
  `the-tasks-called-metric-proof`, `what-a-smoother-curve-doesnt-buy`), last
  one carries the `nb-holdsup` grid and the `nb-note nb-note-strong` Verdict

## Proof

```
./nb check .nb-work/paper-of-the-day/emergent-abilities/library/paper-of-the-day/emergent-abilities.html \
  --series paper-of-the-day --library /home/user/library
```

Result: **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE.**

Warnings encountered and fixed during drafting (none left outstanding):
- 9× `W-SENTENCE-DENSITY` — split each flagged sentence so no clause runs
  past the 40-word floor the check ignores below; verified against the
  engine's own `sentence_density()` helper sentence-by-sentence rather than
  guessing.
- `W-BANNED-TERM 'mechanism'` (4 uses, limit 1 per `press/banned-terms.yaml`)
  — cut to the single use where it is doing real work (Barak's causal claim
  about compounding sub-step probabilities); the other three became "what
  produces it," "effect," and "effect."
- `W-SELF-COUNT` — `nb-meta.words`/`reading_minutes` were placeholders
  (0/0); set to the counted 2,858 words / 13 minutes.

## Editorial decisions worth flagging

- **No chart, no source asset.** The researcher's evidence record is
  explicit that Schaeffer et al.'s central arithmetic demonstration
  (Figure 3) has no underlying numeric table, only qualitative curve shape.
  Per the brief, I built the worked example on the real named quantities
  instead (the 2-digit-multiplication/4-digit-addition task, the
  Accuracy-vs-Token-Edit-Distance metric swap, the "4 or 5 digits" threshold
  language, the BIG-Bench 39-metric / 4-of-39 / >92% figures) and did not
  digitize or invent curve points for a chart.
- **One `nb-table`** does carry real numbers: Wei et al.'s own named
  FLOPs/parameter thresholds for six of their reported abilities, compiled
  from their Figure 2, Figure 3, and Table 1 — all numbers the researcher
  verified directly against the PDF, none estimated.
- The NeurIPS Outstanding Paper award (evidence sources 3–4) is cited once,
  in the orientation section, to establish the rebuttal's standing before
  the reconstruction gets into its argument.
- Kept exactly one hedged not-X-but-Y-style contrast ("the discontinuity
  travels with the scoring rule, not with the model") and stayed under the
  em-dash and banned-terms limits throughout.

## Remaining questions

None. Evidence and voice guide were sufficient to draft and pass proof
without a researcher or writing-coach request.
