# Draft handoff — knowledge-distillation (writer 01)

Production: single-context, no isolation. The harness exposed no child-agent
spawn tool, so the correspondent ran writing-coach, researcher, writer, and
editor as numbered roles in one context, each following its SKILL.md, with every
artifact preserved. Degraded isolation, full chain.

## Original-work sentence
The article reads the 2015 paper's own success as the exact quantity a 2021
study measured and found missing — it recasts "dark knowledge transfers" as the
testable claim "the student matches the teacher's distribution," then shows the
two papers agree on the machinery and disagree only on whether ordinary training
can solve it, landing the reader on when distillation moves a distribution
versus when it merely ships a smaller working model.

The work visible in the piece that the sources do not do themselves: the
sources are read against each other, not summarized. Hinton's MNIST/speech wins
are reframed as fidelity claims; Stanton's fidelity gap is placed beside them as
the same quantity re-measured; Born-Again is shown to be evidence *for* low
fidelity (Stanton's own reading), not against it; Müller is used as the
mechanistic confirmation that closes the loop back to 2015; Beyer is the price
tag on Stanton's diagnosis. The single chart isolates the article's spine (toy
task reaches ~99% agreement, modern task plateaus mid-80s) from Stanton's
multi-panel figures.

## Article and asset paths changed
- `library/paper-of-the-day/knowledge-distillation.html` (authored from the
  initialized skeleton; abstract card, orientation, five flex sections, sources).
- `library/paper-of-the-day/knowledge-distillation/chart-1.py` and `chart-1.png`
  (student–teacher top-1 agreement across three settings; data from Stanton [4],
  Figs. 2–3; rendered via `nb chart`, left margin widened and re-rendered so the
  category labels are fully legible; inspected).

## Furniture used, and why
- One annotated KaTeX equation: the temperature softmax (Eq. 1), the design the
  whole reconstruction turns on; T and the logits colored and named in the
  legend.
- One captioned KaTeX equation: the high-temperature gradient limit (Eq. 4),
  carrying the "matching logits is a special case" reasoning that ties Ba &
  Caruana [3] to the temperature knob.
- One `nb-table`: the speech results (baseline / 10× ensemble / distilled),
  three rows of short numbers that read better as a table than in prose.
- One `nb-figure` chart (above).
- One `nb-note nb-note-strong` Verdict (the single strong note allowed), landing
  the practitioner takeaway.
- No pull quote: the house floor's ban on manufactured punchlines made every
  candidate read as self-grading, so none was promoted.

## Proof result
`./nb check … --series paper-of-the-day --repo . --library ../library`
→ **BLOCK: 0, WARN: 0, PUBLISHABLE.**
Cleared en route: the orientation anchor (skeleton renamed back to
`data-nb-section="orientation"`); five W-SENTENCE-DENSITY warnings (long
sentences split, one semicolon chain removed in favor of periods, per the voice
guide's short-sentence rule). Word/source self-counts carry no warning
(measured ≈2434 words, 8 sources; nb-meta set to match). All eight source URLs
are arXiv abstract pages or the author-hosted Buciluǎ PDF, each confirmed to
resolve; `--check-links` is on by default in the proof.

## Source kinds
All eight sources are `primary`: each authoring team owns the results cited.
There is no secondary reporting, which is correct for a paper reconstruction
that argues from the papers themselves; the evidence record records this reason.

## Remaining questions
None open. Two items flagged for the editor's judgment rather than as gaps:
(1) the chart plots LeNet/MNIST at 99 and ResNet/CIFAR at mid-80s, two different
tasks by design — the caption states this so the contrast is not read as a
single controlled sweep; (2) "around 85%" in the verdict is a deliberate round
of Stanton's several mid-80s fidelity readings (84.5–86% test agreement), not a
single reported figure — the body gives the exact numbers with locators.
