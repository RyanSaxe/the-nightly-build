# Writer brief — word-of-the-day/bowdlerize (invocation 01)

## Inputs (begin here)
- `editorial-direction.md` (governing stack)
- `commission.md` (the assignment)
- `writing-coach/01/voice-guide.md` (reread before drafting)
- `researcher/01/evidence.md` (the complete claim set; do not add claims)
- Article skeleton: `library/word-of-the-day/bowdlerize.html`
- `.nb-context/` (template contract, runtime assets, furniture catalogs)
- This brief.

## Outputs (write only these)
- `library/word-of-the-day/bowdlerize.html`
- `writer/01/draft-handoff.md`

## The article
- Template `article`, series word-of-the-day, mode `open`, order null, date 2026-07-30.
- Hard word band **550–800**. Write tight; the paper's shortest read.
- Open with the `rs-word-card` (press furniture): word, part of speech, pronunciation,
  one-sentence stand-alone definition, cited to Merriam-Webster (S-MW).
- Required anchor sections: `orientation` and `sources`. Then 2–6 flex sections you
  name for the argument; the last flex is the conclusion. Each section carries a
  citation (cite_rule per-section).
- Reasoning order: (orientation) the 1807 anonymous *Family Shakespeare* and its stated
  aim → (flex) Harriet did the expurgation, Thomas took credit in the 1818 London
  edition, the surname became a verb → (flex) the present sense, grounded in the 2023
  Puffin/Roald Dahl case (text altered, still sold under the author's name) → (flex,
  conclusion) the distinction the word preserves: bowdlerize vs. abridge / censor /
  redact. End on the distinction, not a moral or a pointer onward.

## Sourcing
- Six sources, numbered in first-citation order, kinds carried from the evidence
  record: S-MW primary, S-FOL secondary, S-FS(Wikipedia) secondary, S-ETY primary,
  S-DB secondary, S-CJ secondary. min_sources 4 satisfied.
- Keep etymology (history) distinct from the present sense (a separate claim).
- OED is NOT cited: its entry was gated (403) and could not be read; Merriam-Webster
  and the Online Etymology Dictionary carry definition/etymology instead (see evidence
  record's note). Do not cite unread sources.
- Handle the recorded contradiction: first-attestation year is disputed (MW 1826,
  etymonline 1836). Say the verb formed within a decade of Bowdler's 1825 death; do
  not fix a single year.

## Constraints
- Preserve fixed engine assets, `<body class="nb-article">`, required classes/labels,
  the `<h2>Sources</h2>` chrome. Replace every placeholder/caps run. No active content.
- Banned-term ceilings: em-dash ≤4 (aim 0–1), leverage ≤1, load-bearing 0, mechanism
  ≤1. No colon-subtitle headline, no "X is not Y; it is Z" reflex, no banned dek molds
  (semicolon reversal, suspended question, comma triad).
- Fill `nb-meta` with measured values (sources, words), harness `claude-code`, model
  `claude-opus-4-8`.

## Proof (run to BLOCK: 0)
```
export PATH="/root/.local/bin:$PATH"
./nb check .nb-work/word-of-the-day/bowdlerize/library/word-of-the-day/bowdlerize.html --series word-of-the-day --repo . --library ../library
```
(run from repo root /home/user/the-nightly-build). Treat WARN as revision notes.

## Original work
Record in `draft-handoff.md` the one act of original work: what the article does to the
evidence that the evidence does not do itself.
