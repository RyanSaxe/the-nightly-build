# writer brief: feature/thomson-reuters-ross-appeal (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — angle, boundaries, the original work owed
- voice-guide.md (../../writing-coach/01/voice-guide.md)
- evidence.md (../../researcher/01/evidence.md) — the complete claim set; do not go beyond it
- recent-patterns.md (../../recent-patterns.md) — recent feature openers/deks/headings to break
- Template contract + furniture: ../../../../.nb-context/template-contract.yaml and
  ../../../../.nb-context/furniture/engine.md and press.md (rs-docket lives here)

Output:
- The article HTML (edit in place):
  .nb-work/feature/thomson-reuters-ross-appeal/library/feature/thomson-reuters-ross-appeal.html
- ./draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/thomson-reuters-ross-appeal/library/feature/thomson-reuters-ross-appeal.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive
for background. Where something you need is missing (a fact the evidence record does
not carry, or an ambiguity in the voice guide), ask me — do not invent.

This piece's job (confirm or sharpen, then state it in draft-handoff.md): separate
what the Third Circuit actually HELD in Thomson Reuters v. ROSS from the "AI training
is not fair use" headline. READ THE "Orchestrator decision (after researcher/01)"
section at the bottom of commission.md FIRST — it corrects the spine against the
opinion the researcher read in full. The accurate spine:
- The loss turns on a NECESSITY distinction from the software intermediate-copying
  cases (Sega/Sony/Google v. Oracle): ROSS did not need the copyrighted headnotes
  because the judicial opinions were free. The opinion does NOT cabin those cases to
  "non-generative AI" — do not write that.
- Factors 1, 3, 4 ran against ROSS; factor 2 slightly for ROSS. The court moved
  factor 3 against ROSS, reversing the district court, without flagging the change —
  a strong, underreported element.
- The licensing-market-for-training-data harm is thin (one of three factor-4
  findings, ~two sentences, no license/price cited). Report it as thin.
- Generative AI appears only in footnote 7, which sets the DOJ/OpenAI concerns aside
  as "do not apply here." Report exactly that; mark any broader "it reserved the
  question" reading as your own clearly-labeled inference, not the opinion's words.
Use the exact filing date Sept. 29, 2026, docket No. 25-2153, and the panel from the
evidence record.

Specifics:
- Set nb-meta correctly: series `feature`, slug `thomson-reuters-ross-appeal`, mode
  `open`, date `2026-10-04`, template `article`. Fill harness and model. The nb-meta
  `dek` must be identical to the rendered dekline. Run `nb stamp` for counts.
- Use the `rs-docket` furniture to carry the standing case facts (parties, court ·
  docket no., stage, question, stakes) from the evidence record. A table contrasting
  how the fair-use factors were treated may earn its place — only if it shows more
  than prose.
- Be fair to ROSS: state its fair-use argument in recognizable terms before taking
  it apart. Define every legal term at first use (headnote, the four fair-use
  factors, transformative use, intermediate copying, interlocutory appeal).
- Headline/dek per spec/headlines.md: a defensible claim, no colon-subtitle, no
  comma-triad or semicolon-reversal dek; make it this piece's own, not the recent
  molds in recent-patterns.md.
- Every display-text fact (names, court, docket, dates, factor outcomes) checked
  against the evidence record, attributed to the owner (the opinion), not coverage.
- Iterate with `nb check --no-check-links` then run the full proof with links until
  BLOCK: 0. Then write draft-handoff.md (original-work sentence; proof result + any
  intentional warning; any open question).

Report the handoff path and any warning you left.
