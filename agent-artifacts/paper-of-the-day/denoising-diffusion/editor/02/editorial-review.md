# Editorial review: paper-of-the-day/denoising-diffusion (editor/02)

Focused confirmation read of writer/03 against the two items editor/01 routed.
Not a re-review: the thesis, math, numbers, sourcing, and verdict were cleared
in editor/01 and I did not reopen settled ground or raise a new standard. I
confirmed the two required fixes resolved and that nothing else moved.

## Skeptic

Both items were writer-owned honesty/cadence fixes, not claim breaks, so the
skeptic pass here is a targeted check that the repairs are factual and that no
new claim entered.

Asset-2 watermark. I read asset-2.png with Read: the LSUN Church grid is
unchanged and uncropped, and the top-left cell carries a legible "shutterstock"
mark with the string "www.shutterstock.com 193883335" beneath it. The caption
(Fig. 2) now records that fact plainly — "The top-left sample carries a legible
'www.shutterstock.com 193883335' watermark, present in the paper's own Figure
3." The number matches the image character-for-character, and the caption stays
a factual cited label pointing at Figure 3, FID=7.89. The interpretation — that
this is training-data memorization — sits where interpretation belongs, in one
what-it-measured prose sentence ("One of those Church samples reproduces a
stock-photo watermark from the training set intact, a visible instance of the
training-data memorization these models can exhibit at this resolution"). One
sentence, in prose, not in the caption. The asset was not recropped, which is
correct: the watermark is inside the paper's own figure and cannot be removed.
The editor/01 honesty gap is closed exactly as scoped.

Verdict heading. The heading is now "A training recipe the whole field kept," a
plain noun phrase that no longer mirrors the comma-and shape of "Strong
samples, a likelihood that lost, and a cost left unnamed." The two headings no
longer read as one stamped cadence. The recipe-not-model point still stands in
the body ("That is a training recipe, not a model family. The recipe is what
the field kept"), so nothing was lost in the trim, and no new formula or
displayed equation was introduced by the reshape.

Spot-check of hrefs: arXiv/abs/2006.11239 (DDPM), 2011.13456 (Score-SDE), and
2102.09672 (Improved DDPM) each return 200 and land on the abs page the source
list prints. No PDF endpoints.

## Cut

No cut needed. I read the two sentences writer/03 added. The prose memorization
sentence is a single appositive clause, roughly thirty words, not a run-on. The
new caption watermark clause is short and factual. The caption's compound
sentence ("The grid is the paper's evidence for the parity claim, and the
figure caption is where that number lives") joins two independent clauses with
a comma and "and," which is correct coordination, not a splice. No new prose
tell, no leakage, no new "not X" contrast — the reshape actually thinned one.

## Reader

Unchanged from editor/01's reader pass and re-confirmed: the piece still
delivers the original-work sentence (the mean-vs-noise fork and the discarded
weight, defended by the 13.51-vs-3.17 ablation rather than by algebra), and the
verdict still earns its split. The two fixes only sharpened honesty — a reader
who now spots the watermark is met by the caption instead of left with an
unexplained stock-photo mark in images labeled "generated."

## Nothing-else-changed check

- Equations: all nine display equations and the L_simple legend are intact and
  unchanged.
- Numbers: 3.17 / 9.46, the 13.51 ablation, 25.32 / 8.87, 7.89, 4.90, 3.75 vs
  3.70, T=1000, 2.20 all present and unchanged.
- Asset-1 (Algorithm 1/2 boxes) and its caption: unchanged.
- Citations: nine primary arXiv abs sources, unchanged; kinds intact.
- editor/01 cut ("and stating it that way is not a demotion"): still absent; the
  verdict body reads as editor/01 left it.
- nb-meta counts: words 2750, reading_minutes 12, sources 9 — consistent with
  the writer's stamp after the two added sentences.
- 5 WARN: per the writer's re-proof (BLOCK 0, WARN 5, PUBLISHABLE), the five
  remaining W-SENTENCE-DENSITY warnings are the same display-equation LaTeX
  false-positives (Eq. 4, 5, 6-7, 12, 14) inside non-skipped nb-math-eq divs.
  The two added prose sentences introduced no new warning; no genuine prose
  run-on hides among the five.

## Edits

None. No direct cut made, so `nb stamp` was not run.

## Required work

None. Both editor/01 items are resolved and nothing new broke.

## Decision

approve — the asset-2 caption now carries a brief factual watermark note with
the memorization reading confined to one prose sentence and the asset uncropped,
the verdict heading is varied so the two comma-and headings no longer share a
stamped shape with the recipe-not-model point preserved in the body, and the
equations, numbers, asset-1, citations, editor/01 cut, and the five justified
equation-LaTeX warnings are all intact.
