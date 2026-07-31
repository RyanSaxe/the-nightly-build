# Editorial review — editor/01 — paper-of-the-day/emergent-abilities

Article: `library/paper-of-the-day/emergent-abilities.html`
Proof after edits: **BLOCK: 0, WARN: 0, PUBLISHABLE.**

## Skeptic

Thesis: "emergent ability" as Wei et al. named it conflated two things that
were never separated at the time — a real capability that improves with scale,
and an artifact where a discontinuous scoring rule turns a smooth improvement
into a cliff on the page; Schaeffer et al. demonstrated the artifact concretely,
which retires reading Wei's curves as evidence of a sudden internal change,
while a real residue survives (the unpredictable scale at which a deployment's
own metric crosses usefulness, plus the multi-step compounding gap neither
paper's math covers).

Tested 5 load-bearing claims; broke: none.

- **Abstract, verbatim.** Diffed the paper card's abstract character-for-character
  against the evidence record's PDF-extracted block: exact match, including the
  hedged final clause the researcher specifically flagged ("raises the question
  of whether additional scaling could potentially further expand"). Not
  paraphrased. Cited to s1.
- **Metric argument.** Multiple Choice Grade (1 if correct option has highest
  probability), Exact String Match, Token Edit Distance, and Brier Score are each
  defined exactly as the evidence taxonomy states; the discontinuous-vs-continuous
  split is correct. The claim that the discontinuity "travels with the scoring
  rule, not with the model" is earned by the same-outputs re-scoring, not asserted.
- **Worked example — real thresholds, no fabrication.** The example uses the
  named task (2-shot 2-digit multiplication / 4-digit addition on
  InstructGPT/GPT-3), the verbatim "4 or 5 digits" threshold language, and the
  verbatim "smoothly, continuously and predictably improves" result. The article
  states outright that these are figures, not a per-model table, and that no exact
  percentages exist in the source text — matching the researcher's honest flag.
  No digitized curve points were invented. The Wei-threshold table carries only
  the FLOPs/parameter figures the evidence Numbers table verified against the PDF.
- **Agreement/disagreement map, honest.** The pivot — Wei's Section 5.1 calls the
  metric explanation "incomplete" *because* classification tasks (Fig. 2D–H) also
  jump, and Schaeffer's >92%/Multiple-Choice-Grade result cuts exactly that seam —
  is represented faithfully to both papers. Schaeffer's own Discussion
  self-limitation is quoted; Barak's compounding-substeps gap is correctly marked
  as unresolved by either side's math; Wei's blog rebuttal is used as a values
  disagreement about which metric counts, not a concession.
- **Verdict separates artifact from phenomenon without overreach.** It commits
  (does not retreat to "both sides have a point"), and the residue it keeps is the
  precise one the evidence supports.
- **Sourcing.** Every `data-nb-kind` matches the evidence record (s1–s7 primary,
  s8–s10 secondary; the article renumbers by first-citation order, which is
  internally consistent). Every quote checked verbatim against the record; every
  number matches its owning primary.

## Cut

Cut 2 sentences' worth of non-reporting language (~24 words); worst tell: a
method-signpost in the orientation closer.

- Orientation closer: removed ", and reconstructing the argument means starting
  with the number before either side gets to interpret it" (method self-narration)
  and changed "what the reader should conclude from it" to "what to conclude from
  it" (removes the audience mention the floor bans). The load-bearing claim — the
  two papers agree on the datum and disagree on its interpretation — is preserved.
- One-task-two-rulers section: "What is stated in words, and what this
  reconstruction relies on, is the qualitative result…" → "What is stated in words
  is the qualitative result…" (removes the "this reconstruction" self-reference;
  the fact is untouched).

Nothing else met the delete test. The `nb-holdsup` grid and the `nb-note` verdict
both carry the article's core artifact-vs-real map and are earned furniture, not a
block stack. The not-X contrasts ("travels with the scoring rule, not with the
model"; "a calculator that is usually close is not a calculator") are within the
ceiling and both correct real misreadings.

## Reader

This gives me the one thing neither abstract does: a clean split between the
demonstrated artifact (identical GPT-3/InstructGPT outputs scoring a cliff under
Accuracy and a slope under Token Edit Distance) and the real residue (a deployment
stuck with a discontinuous metric still faces an unpredictable threshold, and
multi-step compounding sits outside both papers' math), plus the exact map of
where Schaeffer's classification-metric result answers Wei's own Section 5.1
objection rather than talking past it. That matches the draft-handoff's stated act
of original work, and it is present in the piece. The prose reads as a reviewer
adjudicating a dispute — closer to the voice-guide exemplars than a median AI
summary. The headline states the finding with no colon tell; the dek adds the
named authors, the rebuttal framing, and a stance.

## Minor observation (not blocking, not routed)

Table row "MMLU, 57-topic average | Chinchilla | 3–5×10²³ FLOPs (70B–280B
params)": the evidence attributes that FLOPs band to GPT-3/Gopher/Chinchilla
across 70B–280B, so naming Chinchilla (a 70B model) alongside a range topping out
at 280B is a slight over-specification. It is not false (Chinchilla does cross
MMLU in that FLOPs band) and lives in a supporting body table, not display text.
Left as the writer built it from the evidence rather than assign an unverified
Chinchilla-specific parameter figure.

## Decision

Approve. No redraft required. Proof BLOCK: 0.
