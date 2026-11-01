# Voice guide: feature/jepsen-particledb

No exemplar passage is quoted, so no page was fetched. The register is the one
Jepsen reports use: the claim in the vendor's words, then the test, then the
result, with no adjective between them. The sample sentences below are
illustrations written for this guide. Their facts come from the commission and
must be re-checked against the Jepsen report before reuse.

## The register in one rule

Every sentence reports a claim, a test, or a result about ParticleDB. If a
sentence would still read correctly with "ParticleDB" swapped for another
product, cut it. This is the slop test applied to the whole piece.

## Moves

1. **Claim, then measurement.** Quote the vendor's words in quotation marks
   and name where they appear. Then give what Jepsen observed, with the
   version and mode. Example shape: Orkes documents the default `occ` mode as
   "Jepsen-safe". Jepsen found it lost committed writes.
2. **Flat verbs.** Jepsen "found", "observed", "could not check". Orkes
   "advertises", "documents", "says". Never "admits", "claims" as a sneer,
   "exposes", "debunks", or "fails to deliver".
3. **Define, then name.** Put the plain-words definition in the clause where
   the anomaly first appears, then the standard name, then use only that name.
   Example shape: a transaction overwrites another's update because both read
   the same old value, which is Lost Update. Do the same for read skew (A5A),
   G-single, aborted read (G1a), and a stale read under strict
   serializability. Do not switch to "lost write" for Lost Update later. Keep
   "lost committed write" for the `occ` finding only if the report uses it for
   a different failure, and say which.
4. **Point at cells.** The matrix carries the finding. Prose says how to read
   it ("each row is one advertised guarantee, each right-hand cell is the
   anomaly Jepsen recorded against it") and what the reader should then check
   in the diagram. It does not repeat cell contents in sentences.
5. **Numbers as given.** 96 issues, versions 1.1.4 through 1.1.18.11.rc-22,
   "159K TPS". No rounding, no "dozens". Say once that these were single-node
   tests.
6. **Attribute and bound.** The 1.1.19-rc.13 resolution claim is Orkes's,
   attributed by name, and Jepsen did not test that build. Say both in one
   short passage and leave it. The TLA+ row says the claim could not be
   checked because no specification was available. It does not say the claim
   is false.
7. **Disclose once, early, plainly.** Orkes funded the analysis. One sentence,
   no apology and no defence. Do not add that funding does not affect results
   unless the report says so, and then attribute it.

## Things to avoid here

- **Generalizing.** No sentence about databases, vendors, benchmarks,
  marketing, or the industry. Test the first and last sentence of every
  section and of the piece hardest. End on a result or on what the matrix
  shows, not on a lesson.
- **Antithesis.** "Not a verdict on Orkes but a method" is the tempting
  one. If the fairness point is needed, state what the report did: it tested
  named versions in named modes.
- **Intent and motive.** Never say Orkes knew, hid, or hoped. Never write that
  anything "hinted" or "implied". Stay with the documented wording and the
  measured behaviour.
- **Intensifiers and verdict words.** No "alarming", "startling", "damning",
  "surprisingly", "shockingly". The reader draws the size of the gap from
  `WHERE 4 = 5` matching the row with primary key 5.
- **Rhythm devices.** No triads picked for cadence, no run of sentences
  opening alike, no "the catch is". The matrix has six rows, so list six when
  listing, and none when not listing.
- **Headings.** Do not open any with "What". Make each a step of the
  argument in the piece's nouns, and build them with different shapes, with
  no repeated "X, and Y" pattern. Headline: a declarative finding with the
  specific number, built differently from the recent ones. Dek: no "only
  as X" or "only in one Y" twist.
- **Self-reference.** No "this piece", "below", "as the table shows". Say what
  Jepsen found, and let the figure sit next to it.

## Calibration pair

Too loud: "ParticleDB's marketing collapses under Jepsen's testing, with the
default mode shedding committed data."

On register: "Orkes documents `occ` as 'Jepsen-safe'. In Jepsen's tests the
default `occ` mode lost committed writes."

The second names the vendor, quotes the claim, names the mode, and states the
result in six plain words. It also passes the placeholder test, since remove
the nouns and nothing is left.

## Reader

CS and ML graduates who build production systems. They know transactions,
locks, and replication. They do not carry Adya's taxonomy. Give a definition
once, in a clause, and keep going.
