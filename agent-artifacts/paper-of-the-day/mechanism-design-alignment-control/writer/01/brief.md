# Writer brief

## Inputs

- Read `commission.md`.
- Read the generated `editorial-direction.md`.
- Read `writing-coach/01/voice-guide.md`.
- Read `researcher/01/evidence.md`.
- Read the initialized file at `library/paper-of-the-day/mechanism-design-alignment-control.html`.
- Inspect `asset-1.png` and `asset-2.png` in the article bundle.

## Output

Edit the initialized HTML in place. Preserve the paper template, paper card, relative theme links, and fixed `abstract`, `orientation`, and `sources` sections. Add six flex sections following the commissioned reconstruction. Write `draft-handoff.md` in this directory after the HTML is complete.

Use source entries `s1` through `s10` in first-citation order. Every citation that carries an argument must point to a source entry and, when the claim is specific to a passage, include `data-nb-locator`, `data-nb-url`, and `data-nb-note`. Keep `data-nb-kind="primary"` or `"secondary"` on each source link. Use the focal paper for theorem statements and the external sources only for the contextual claims they establish.

The paper card must reproduce the focal abstract verbatim. The title and dek in the `<title>`, `nb-meta`, header, and paper metadata must agree. Set the article date to `2026-09-04`, use the commissioned headline and dek, and use tags `mechanism-design`, `ai-safety`, `alignment`, `sandbagging`, `evaluations`, and `control`. Set `harness` to `codex-nightly-build` and `model` to `gpt-5` unless the proof harness requires a different literal. Let `nb stamp` fill the final word and reading-minute counts.

Include:

- Figure 1 as `<figure class="nb-figure">` with a precise alt, a caption describing the directional evidence relation, and a focal-paper citation located at `Fig. 1 · p. 12`.
- One annotated `<figure class="nb-math">` for `ā* = 1 − sqrt(b̄² + σ²) = 1 − sqrt(E[b²])`, with a three-item legend explaining the symbols and the model’s condition (INT).
- Figure 8 as `<figure class="nb-figure">` with a precise alt, a caption identifying its three panels and illustrative frontier, and a focal-paper citation located at `Fig. 8 · p. 35`.
- At most one `nb-note-strong` note, labeled `Verdict`, in the final flex section. It must state the evidence-backed article verdict and its limits. Use ordinary paragraphs and at most one definition note elsewhere if helpful.

Do not use a chart script for the source figures. Do not add claims, numbers, quotes, or source URLs absent from `evidence.md`. Avoid the recent series’ repeated “What holds up” structure and avoid a generic “background” heading. Target about 2,300–3,000 words including the abstract card.

## Proof

- Run `./nb stamp .nb-work/paper-of-the-day/mechanism-design-alignment-control/library/paper-of-the-day/mechanism-design-alignment-control.html`.
- Run `./nb check .nb-work/paper-of-the-day/mechanism-design-alignment-control/library/paper-of-the-day/mechanism-design-alignment-control.html --repo . --library ../the-nightly-build-library --no-check-links` and resolve every blocker.
- Run the link-aware check before handoff if the network permits.
- In `draft-handoff.md`, record the exact original-work sentence, the stamp/check result, the section list, the asset list, and any remaining editorial uncertainty. State explicitly that the headline/dek/metadata agree.
