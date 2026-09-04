# Editor brief

## Inputs

- Read `commission.md`.
- Read the generated `editorial-direction.md`.
- Read `writing-coach/01/voice-guide.md`, `researcher/01/evidence.md`, and `writer/01/draft-handoff.md`.
- Read the writer brief.
- Read the complete initialized article HTML in the library workspace.
- Inspect both local source assets and the built preview if available.

## Output

First read the draft alone as a skeptical reader. Second read it against the evidence and source list. Third read it for structure, deletion, and what the article adds beyond the sources. Edit the article directly where needed, but do not edit the evidence record, source assets, or the commission. Then write `editorial-review.md` with these exact top-level sections: `## Skeptic`, `## Cut`, `## Reader`, `## Edits`, `## Required work`, and `## Decision`.

Verify:

- the focal abstract is verbatim and every external number is scoped to its source’s setup;
- every source URL, source kind, source count, first-citation order, locator, and note is honest;
- the two figures are exact crops, their alt text describes the visible content, and their captions explain what each settles;
- the optimal-cap equation renders as a single annotated equation and the `nb-note-strong` verdict is the only strong note;
- every flex section has an argument-bearing heading and an inline citation;
- the article states partial implementation and all material toy-model assumptions before its verdict;
- optional uses of the press-banned term are removed where the paper’s terminology does not require them;
- headline, dek, header, and metadata agree, with no template placeholders.

## Proof

- Run `nb stamp` after any edit.
- Run the local checker with `--series paper-of-the-day` and `--no-check-links` until `BLOCK: 0`.
- Attempt the link-aware checker again if the environment permits it.
- Rebuild the site and run `nb render-check`; if Chrome is unavailable, record that limitation rather than claiming visual browser verification.
- Approve only after the proof is fresh and the decision is `APPROVE`.
