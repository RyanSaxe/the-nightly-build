# Editor review-brief: tech-news/2026-08-02 (01)

## Your job
Give this drafted technology `brief` the three ordered reads (skeptic, cut,
reader) and either approve it (`DONE editor`, no required change) or route
numbered repairs. Cuts and small prose fixes go directly in the article; new
prose past a word/clause returns to the writer; evidence gaps to the researcher.

## Begin with these exact inputs
- This brief; `../../editorial-direction.md`; the exact writer brief
  `../../writer/01/brief.md` (for prompt-leakage detection); voice guide
  `../../writing-coach/01/voice-guide.md` (read first); evidence record
  `../../researcher/01/evidence.md`; draft handoff `../../writer/01/draft-handoff.md`;
  article `/home/user/the-nightly-build/.nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html`;
  template context `../../../../.nb-context/`.

## What to check hardest (this brief's risk surface)
- **Per-item sourcing**: each of the 4 items must carry exactly 1 primary and 1+
  independent secondary, with honest `data-nb-kind`. Confirm the writer's
  resolution of Item 1's two-primary conflict (EU Commission FAQ as primary; the
  third-party legal-text mirror as secondary) is right, not relabeled to game the
  count. Item 2's OpenAI primary 403s for automated fetch — verify the writer
  cited only figures a directly-read secondary confirms and attributed the 99.8%
  aligner figure to The Decoder by name.
- **Excluded/attributed claims (verify none slipped in)**: the "1,610→27 seconds"
  HI.SIM figure and the Kush Desai "BREAKING" quote must be ABSENT (unverified).
  The EO 14409 "missed deadline" must be framed as Forkast's reporting as of a
  date, not a flatly established government failure. DeepSeek's "open-weight"
  status must not be asserted as settled (weight-availability unresolved);
  vendor-stated benchmarks labeled as such.
- **Every figure, model/version name, org name, date** in display text and body
  against the owning primary (EU €15M/3%, application date Aug 2; DeepSeek
  Intelligence Index 50 vs 25 median, 284B/13B, pricing; the speedups). A wrong
  number or name in a headline/dek is the costliest error.
- **Brief discipline**: each item is a judgment about why it matters, not a
  recap; no item closes by handing the point back to the reader; the lead is
  chosen by significance (the non-security EU item), not reflex.

## Standards to apply in the cut
Full house prose/punctuation floor. Compare item headlines, the dek, and item
shapes against the recent tech-news library (the AI-security-lead reflex, stacked
AI-safety items, formulaic kickers, hedged-contrast deks). Break any repeated
shape. Cut prompt leakage (selection rules, planning labels, "this brief covers"
self-description).

## Output
Write `editorial-review.md` here with the three required lines, direct edits,
required work by owner, and the final decision. If you edit, note whether a
re-proof is needed
(`nb check .../2026-08-02.html --series tech-news --library /home/user/library`).
Return `DONE editor <path>` only if no redraft is required, else a
`REQUEST writer/researcher <one-sentence>` line.
