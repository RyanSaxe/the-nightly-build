# Commission: paper-of-the-day/word2vec

## Assignment

The Paper of the Day, on the `paper` template. Authorized by the scheduled `nb
duty` result (open section; choose a paper; do not repeat a published slug). Slug
`word2vec`.

## The paper and why it qualifies

Mikolov et al., "Efficient Estimation of Word Representations in Vector Space"
(2013), and its companion "Distributed Representations of Words and Phrases and
their Compositionality" (2013) — the word2vec papers. The famous result is the
linear analogy: vector("king") − vector("man") + vector("woman") lands near
vector("queen"). The paper qualifies because it has a rich public record *after*
publication that recontextualizes the central claim:

- Levy & Goldberg showed skip-gram with negative sampling is implicitly
  factorizing a shifted PMI matrix (a mechanism the original paper did not give).
- Later analyses (e.g. Linzen; Nissim, van Noord & van der Goot, "Fair is
  Better than Sensational") showed the celebrated analogy arithmetic depends on
  excluding the input words from the answer set and is weaker/more selective than
  the demo implies — the "abstract set aside" story this desk favors.

Reconstructing the analogy claim clarifies an active question: what do embedding
"directions" actually encode, and how much of the analogy result was a
measurement choice. This is squarely in ML/NLP, the desk's center.

## Angle and required contribution

Rebuild the central claim — that word2vec learns a vector space where linear
offsets capture analogical relations — and weigh it against what happened next.
The article should reconstruct *how* the analogy is actually evaluated
(3CosAdd, and the exclusion of the query words), report Levy & Goldberg's
implicit-matrix-factorization result as the mechanism the original paper left
implicit, and present the critiques that show the analogy result is narrower than
its demo. Reach a defensible verdict on what word2vec genuinely established
(cheap, useful distributed representations that scaled) versus what the famous
analogy demo oversold. Keep the reader who knows ML but not this specific
literature able to follow every step; define NLP-specific terms (negative
sampling, PMI, 3CosAdd) where they first appear.

## Boundaries and neighbors

The same edition runs a Tech News brief that may touch AI. Keep this piece a
retrospective reconstruction of the 2013 paper and its follow-on record; do not
drift into current-day news. Do not repeat any earlier Paper-of-the-Day angle
(recent: grokking, emergent-abilities, knowledge-distillation, LoRA,
chain-of-thought, attention, resnet, adam, batch-norm, lottery-ticket,
chinchilla) — word2vec is distinct (representation learning / NLP), so the risk
is structural repetition, not topical.

## Recent shapes to break

The paper desk's recent deks and headlines follow a strong, now-recognizable
formula: "Paper X's own result was really about Y," a single sharp reversal
(e.g. "Rescoring the same GPT-3 outputs turns a leap into a slope"; "A distilled
network inherits its teacher's accuracy, not its predictions"). The underlying
"the reckoning recontextualizes the paper" shape is the series identity, but the
*sentence mold* is repeating. Find a headline true to word2vec that does not
reuse the "not X, but Y" or the em-dash-reversal cadence the last several used.
Vary the section headings from any prior paper-desk outline.

## Source policy

Template floor: `min_sources: 8`. Primary sources own the claims: the two 2013
word2vec papers, Levy & Goldberg (2014), the analogy-critique papers, and any
replication/benchmark used. Cite only passages actually read. Contested figures
need the primary that owns them.

## Production (models and effort)

Balanced profile. Roles and models this run assigns:

- writing-coach: capable → `sonnet`, effort low (not required)
- researcher: capable → `sonnet`, effort high (not required)
- writer: capable → `sonnet`, effort medium (not required)
- editor: inherit → `opus`, effort high, **required**

Runtime caveat: isolated children run at their model's default reasoning effort;
effort is not separately tunable. Model per role is the honored lever; the
required editor runs on `opus`.

## Original work

The reconstruction-and-verdict: rebuilding how the analogy is actually measured
and weighing the paper's famous claim against the implicit-matrix-factorization
mechanism and the analogy critiques, to say precisely what word2vec established
and what the demo oversold.
