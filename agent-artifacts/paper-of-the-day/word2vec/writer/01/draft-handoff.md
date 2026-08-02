# Draft handoff: paper-of-the-day/word2vec (writer/01)

## Original work

The article reconstructs, as one continuous argument no single cited source
states together: that word2vec's linear-analogy result cannot be separated
from a specific measurement choice (3CosAdd's exclusion of the query words,
a rule word2vec's own paper states but never names); that the King−Man+Woman
demo which sells that result originates in an earlier RNN paper the 2013
word2vec papers only cite in passing; and, weighing that reconstruction
against Levy & Goldberg's implicit-PMI-factorization theorem and the
three-way Baroni/Levy-Goldberg/Levy-Goldberg-Dagan predict-vs-count dispute,
a bounded verdict on exactly what word2vec itself established (a cheap
architecture whose vectors won nearly every independent benchmark tried
against them) versus what its most famous demo oversold (that linear offsets
are a stable, general property of the space, rather than an artifact of one
scoring rule on one excluded set on one test). The verdict note in the
closing section states this explicitly, cashing out each qualifier against
the specific evidence it rests on, per the voice guide's directive.

## Proof result

Final command (links included):

```
./nb check .nb-work/paper-of-the-day/word2vec/library/paper-of-the-day/word2vec.html \
  --series paper-of-the-day \
  --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout
```

Result: `BLOCK: 0`, `WARN: 1`, verdict `PUBLISHABLE`. All 9 source URLs
resolve. `nb stamp` ran clean: words=2866, reading_minutes=12, sources=9.

Warning intentionally left:

- `W-SENTENCE-DENSITY`, 44 words / 1 clause join, on the sentence quoting
  "Efficient Estimation" verbatim ("Using a word offset technique where
  simple algebraic operations are performed on the word vectors...results in
  a vector that is closest to the vector representation of the word
  Queen."). This is the paper's own sentence, presented as a direct
  quotation in the section reconstructing the King/Queen demo's origin.
  Splitting or rewording it to satisfy the density heuristic would misquote
  the primary source, so it stands as written.

## Open questions

None blocking. Two judgment calls worth the editor's attention, both
resolved in the draft but not forced by the evidence:

- The abstract card anchors on "Efficient Estimation of Word Representations
  in Vector Space" as the sole focal paper (per the paper template's
  single-paper identity), with "Distributed Representations of Words and
  Phrases..." folded in as the source for negative sampling in its own
  section rather than given a second paper card. The commission frames this
  as a two-paper story; I judged the template's one-paper-card convention
  controlling and let the companion paper carry its own section instead.
- The abstract paragraph text (verbatim block, source #1) was verified
  directly against the arXiv abstract page rather than against a locator
  already sitting in the researcher's evidence record, since the evidence
  record establishes the paper as read in full but doesn't quote the
  abstract verbatim. Flagging this in case the editor wants the researcher
  artifact amended to carry that exact string for the record.
