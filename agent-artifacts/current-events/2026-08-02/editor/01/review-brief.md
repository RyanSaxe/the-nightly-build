# Editor review-brief: current-events/2026-08-02 (01)

## Your job
Give this drafted US news `brief` the three ordered reads (skeptic, cut, reader)
and either approve it (`DONE editor`, no required change) or route numbered
repairs. Cuts/small fixes go directly in the article; new prose past a
word/clause returns to the writer; evidence gaps to the researcher.

## Begin with these exact inputs
- This brief; `../../editorial-direction.md`; the exact writer brief
  `../../writer/01/brief.md` (prompt-leakage detection); voice guide
  `../../writing-coach/01/voice-guide.md` (read first); evidence record
  `../../researcher/01/evidence.md`; draft handoff `../../writer/01/draft-handoff.md`;
  article `/home/user/the-nightly-build/.nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html`;
  template context `../../../../.nb-context/`.

## What to check hardest (this brief's risk surface)
- **The writer flagged a source-kind judgment call — audit it in your skeptic +
  kind read.** The brief template caps each item at exactly 1 primary. Items 1
  and 3 had two primary-type documents. The writer kept one as `primary` and
  dropped or re-tagged the other. Scrutinize item 3 especially: the elimination-
  status determination is OWNED by PAHO (the certifying body; "CDC does not
  itself declare elimination status"), while CDC owns the case data. Confirm the
  item's central claim is attributed to the body that actually owns it and that
  the `data-nb-kind` labels are honest, not chosen to satisfy the geometry. If a
  wrong kind hides a missing independent source, that is a sourcing failure to
  route back.
- **Iran (item 1)**: the "deal"/pause must read as Trump's own unconfirmed claim
  — no Iranian/Israeli confirmation exists in any independent account. Check the
  prose does not state the deal as fact, and carries the skeptical caveat (Hormuz
  previously claimed open "despite evidence to the contrary").
- **TPS (item 2)**: the Aug 1 order text was gated/unread — must be attributed to
  court reporting (Fox + a second independent), not asserted as a document read.
  Names/titles exact: Judge Allison D. Burroughs (D. Mass.); Sec. Kristi Noem;
  *Mullin v. Doe*; the 1,082 figure.
- **Display text descriptor by descriptor**: every name, title, place, date, and
  number in the headline/dek/subheads against the owning primary (the four
  coalition orgs and their leaders' exact titles; measles 2,371/37/94%,
  95.2%→92.5%; the region-vs-US Nov 2025 vs Nov 2026 distinction). A wrong title
  in display text is the costliest error the paper prints.
- **Brief discipline**: each item a judgment about why it matters; no
  reader-handoff closers; the Iran thread advances the paper's 07-30 coverage
  (says what changed) without re-explaining.

## Standards to apply in the cut
Full house prose/punctuation floor. Compare item headlines, the dek, and item
shapes against the recent current-events library (macro/Fed lead reflex,
formulaic kickers, hedged-contrast/comma-triad deks). Cut prompt leakage
(selection rules, "most consequential," planning labels).

## Output
Write `editorial-review.md` here with the three required lines, direct edits,
required work by owner, and the final decision. If you edit, note whether a
re-proof is needed
(`nb check .../2026-08-02.html --series current-events --library /home/user/library`).
Return `DONE editor <path>` only if no redraft is required, else a
`REQUEST writer/researcher <one-sentence>` line.
