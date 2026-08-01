# Draft handoff — paper-of-the-day/grokking (writer, 01)

## Original work

The evidence record hands over one focal paper (a documented phenomenon
with no explanation, admitted as such in its own appendix) and four
non-redundant follow-on papers that each supply a different candidate
explanation. The one act of original work this draft does to that evidence,
which none of the eight sources does on their own: it separates Power et
al.'s phenomenon from every account of its cause into two distinct claims
with two distinct evidentiary standards — "the delay is real and measured"
(Power, confirmed independently by Nanda's replication) versus "here is why
it happens" (four different, mutually disagreeing answers, none confirming
the original paper's own flat-minima guess) — and then states, as a
reviewer would, exactly which slice of Power's original claim (one
operation of twelve, one modulus of many, one architecture) the mechanistic
record actually covers versus which eleven-twelfths of the original claim
remain untested by any explanation on record. No single source states that
scope gap; it only becomes visible by reading the five mechanistic papers
against Power's own task-family table side by side.

## Article and asset paths changed

- `library/paper-of-the-day/grokking.html` (full draft, written from the
  initialized skeleton; no other files changed; no chart or source asset
  used — the evidence record flagged no real transcribed grokking-curve
  data points and unverified figure images, and the brief bars fabricating
  a curve, so the delayed-generalization curve is described in prose only,
  per Power et al. §3.1 / Fig. 1 numbers).

## Proof result

`nb check library/paper-of-the-day/grokking.html --series paper-of-the-day
--repo /home/user/the-nightly-build` (run from
`.nb-work/paper-of-the-day/grokking/`, with link-checking on):

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

First pass surfaced 10 warnings (8 × W-SENTENCE-DENSITY on run-on
sentences, 1 × W-BANNED-TERM on em-dash count of 7 against the house limit
of 4, 1 × W-PLACEHOLDER on all-caps stat-strip labels that should have been
sentence case — the CSS uppercases them at render time). All ten were
fixed by splitting the flagged sentences, rewriting every em-dash aside as
a period, comma, colon, or parenthetical, and lowering the stat-strip
labels to sentence case. No warnings were left standing. `nb-meta` words
(2,592) and reading_minutes (12) were set from the actual measured count
after the rewrite, not estimated in advance.

The press's own `press/banned-terms.yaml` bans "mechanism"/"mechanisms" to
at most 1 use — a pointed constraint for an article whose spine is
phenomenon-vs-mechanism. The draft uses neither word: "mechanistic" (safe,
not a substring match) and "explanation," "account," "cause," and "causal
story" carry that work throughout, including in the one place the
evidence's own verbatim quote used "mechanisms" (Nanda et al.'s abstract),
which is paraphrased rather than quoted verbatim for that reason.

## Warnings intentionally left standing

None.

## Editorial requests addressed

N/A — this is the first draft (round 01), not a revision.

## Remaining evidence or voice questions

- The evidence record flags the focal paper's venue as unresolved (the
  arXiv listing carries no venue metadata; the one workshop record found
  for it, MATH-AI's ICLR 2021 accepted-papers page, is dated a year before
  the arXiv posting). The draft follows the researcher's recommended safe
  phrasing throughout: the paper card states "arXiv:2201.02177" in place of
  a venue, and the body states the mismatch plainly, cited, without
  asserting a specific workshop or year. If a definitive venue is resolved
  before publication, that sentence in the "Perfect on the training set,
  wrong on everything else" section is the one to revisit.
- Two evidence-flagged sources (Liu et al.'s "Effective Theory" and Varma
  et al.'s "circuit efficiency" paper) were verified by the researcher only
  at the abstract level, not full-text. The draft cites both for
  abstract-level claims only, consistent with that scope; no body-section
  locator is asserted for either.
- No chart or source asset is used. If the editor or a later round wants a
  visual for the headline curve, it would need either a fresh transcription
  of Power et al.'s Figure 1 data points (for `nb chart`, with committed
  provenance) or a direct visual inspection of a captured source asset
  (Power Fig. 1, Nanda Fig. 1 or Fig. 7, Omnigrok Fig. 1, or Prieto Fig. 2
  / Fig. 4) — none of which the evidence record or this round performed.
