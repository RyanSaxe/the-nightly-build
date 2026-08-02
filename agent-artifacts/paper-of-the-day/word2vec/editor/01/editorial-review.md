# Editorial review: paper-of-the-day/word2vec (editor/01)

## Skeptic

Thesis: word2vec's signature demo (King - Man + Woman ~= Queen) is not word2vec's
own result and does not stand on its own. The demo is credited by word2vec's own
paper to a separate, RNN-based line of work; it only "succeeds" because the three
query words are barred from being the answer, a rule whose removal collapses
accuracy on the actual public vectors; and the broader count-vs-predict question
it is enrolled in remains unresolved. The piece then states a bounded verdict on
what word2vec did (a cheap architecture whose vectors win nearly every practical
benchmark) versus what the demo oversold (that linear offsets are a stable,
general property of the space).

Load-bearing claims tested:

1. **Attribution / "predates" (headline + dek + s1/s3).** Held, with one
   correction. "Efficient Estimation" (s1) attributes the King/Queen offset via
   citation [20] to Mikolov, Yih & Zweig (s3), whose vectors come from an RNNLM,
   the older architecture family word2vec was built to replace. The verbatim [20]
   sentence is quoted accurately and matches the evidence. BUT the draft asserted
   the NAACL paper was "presented five months earlier" than "Efficient
   Estimation." That is backwards: I fetched both primaries — arXiv:1301.3781 v1
   is 16 Jan 2013 (v3 7 Sep 2013), and the NAACL paper is June 2013, i.e. ~5
   months *later*. The demo's precedence is real (word2vec cites the work as prior
   art, so the method existed by Jan 2013; the RNNLM model predates skip-gram),
   but the specific publication-timing claim was false. Cut. The headline/dek/
   verdict survive on the model-lineage-plus-attribution reading, which is what
   the surviving body now supports ("the same family of architecture 'Efficient
   Estimation' was built to replace"; "where the vector-offset method and the
   King/Queen example both originate").

2. **Negative sampling as the softmax-cost fix (s2).** Held. The full-softmax
   cost is stated correctly, negative sampling is motivated by that cost, the toy
   vocabulary is a correct illustration, and the k=5-20 / 2-5 range is quoted from
   the primary. Not overclaimed (hierarchical softmax is simply not the one taught).

3. **3CosAdd, the exclusion rule, and its collapse (s1/s4/s5/s6).** Held, with
   one correction. The exclusion is quoted from word2vec's own paper; 3CosAdd's
   definition, its additive rearrangement, and the London/Baghdad -> Mosul vs Iraq
   / 3CosMul example all match s4. The Levy-Goldberg head-to-head table numbers and
   margins check out, as do the 19,258/19,544 OOV figure and the Nissim 0.71->0.21
   / 0.73->0.45 collapse. **However, the Linzen breakdown was factually wrong and
   geometrically impossible.** The draft read: nearest neighbor to X = King - Man +
   Woman was "Woman... 93%... and Man... 5%. It was never King." Linzen (and the
   geometry) say the subtracted word can never be the answer: nearest is one of the
   two *added* words (Woman 93%, King 5%), never the subtracted word (Man). The
   draft swapped King and Man. Since X = King + Woman - Man points *away* from Man,
   "Man 5%" is impossible and "never King" is wrong. The evidence record confirms
   b=93%, a*=5%, never a (a = the subtracted word). Fixed directly to "King... 5%.
   It was never Man." Writer must re-verify this in proof.

4. **Implicit shifted-PMI factorization (s7).** Held. w.c = PMI - log k is
   correctly stated, correctly caveated as an idealized-optimum result ("holds
   exactly only when the dimension is large enough..."), and the residual fact
   that trained SGNS still beats an exact factorization on analogies (0.627 vs
   0.448 syntactic) is reported with the paper's own conjecture (frequency
   weighting) marked as conjecture, not proof. Not overclaimed.

5. **Count-vs-predict dispute (s8/s4/s9).** Held. Baroni's "thorough and
   resounding victory" (13 of 14) is quoted and scoped; Levy-Goldberg CoNLL is
   presented as running "contrary to" Baroni; and Levy/Goldberg/Dagan 2015 is
   framed as "one lab's account of a dispute they were already one side of," not
   the final word, exactly as the brief required.

6. **Google-News figures as self-report.** Held. The caveat is explicit and
   scoped to every figure attached to the unreleased corpus/vectors.

Display text and data-nb-kind: headline, dek, and all seven section subheads make
claims about the world (none grade the article's method), reconstruct the argument
in order, and avoid the banned reversal/comma-and molds and scaffolding slots. The
dek is two clauses, not a comma triad, and carries no semicolon reversal or
suspended question. All nine sources are genuinely primary (each owns the claim
cited to it); the Levy-authored papers are correctly presented as one lab's
account rather than independent adjudication. No secondary-as-primary and no
"different website = independent author" failures.

The intentional WARN:1 (W-SENTENCE-DENSITY, 44 words) on the verbatim [20]
sentence earns its place: it is the exact sentence carrying the attribution that
is the piece's spine, and splitting it would misquote the primary. The warning
stands.

## Cut

- Cut the signpost/self-reference paragraph "That training trick is what sits
  underneath every skip-gram vector this piece discusses from here on..." Its
  cargo (the later vectors are skip-gram-with-negative-sampling) is re-established
  in the sections that follow, and cutting it lets the section end on its concrete
  payoff sentence.
- Cut "here and in what follows" from the Google-News caveat: "Every accuracy
  figure attached to it" already scopes the caveat universally, so the phrase was
  redundant self-reference.
- Cut "presented five months earlier" (see Skeptic 1).

Worst tell: the self-referential "this piece discusses from here on." Otherwise
the prose holds its register. The two licensed forms are used within their bars:
the single rhetorical question ("So what happens when the vocabulary...runs past a
million words?") appears once, at a genuine pivot, answered in the next sentence;
the sustained four-points spatial image is used to make cosine-vs-Euclidean
checkable and is explicitly retired where it stops explaining ("It stops
explaining why skip-gram's particular arrangement... beats a matrix..."). No
repeated ending shape across sections; endings vary in construction. No prompt
leakage beyond the cut signpost.

Minor, non-blocking (writer's discretion, not required):
- "Consider a large enough vector dimension..." opens with a lecturing verb the
  house standard names; a clean fix needs a small rephrase, so it is the writer's
  to smooth, not an editor cut.
- The nb-stat-strip pairs Linzen's 98% with Nissim's 0.71->0.21 under the Linzen
  paragraph; both numbers are correct and both are cited correctly in prose, but a
  reader may attribute both to Linzen. Optional furniture-clarity touch.
- "roughly a tenth the data" is loose (320M vs the 1.6B run is nearer a fifth);
  hedged, so it stands, but the writer may tighten.

## Reader

What the piece gives beyond its sources: a single cross-checked argument, built
from nine primaries, that the famous demo is (a) credited by word2vec's own paper
to prior RNN work, (b) an artifact of the query-word exclusion — demonstrated to
collapse on the actual public GoogleNews vectors — and (c) embedded in an
unresolved count-vs-predict dispute, resolving into a bounded verdict on what
word2vec actually established. No single cited source states that synthesis. The
draft's original-work sentence claims exactly this reconstruction, and the article
delivers it; both survive the reader pass, so no redraft is owed. The prose sits
closer to the Olah/Alammar/Pavlus exemplars than to a median summary: each
mechanism gets a hand-traceable instance before its name, the spatial image is
carried and retired deliberately, and the verdict cashes out every qualifier
against named evidence.

## Edits

- the-excluded-words: corrected Linzen breakdown from "Man, the other input word,
  in another 5%. It was never King." to "King, the other input word, in another
  5%. It was never Man." (factual/geometric correction, grounded in s5 and the
  evidence record).
- the-demo-before-the-paper: cut "presented five months earlier" from the
  Mikolov/Yih/Zweig attribution sentence (false publication-timing claim).
- scoring-every-word: cut the closing signpost paragraph "That training trick is
  what sits underneath every skip-gram vector this piece discusses from here on..."
- orientation: cut "here and in what follows" from the Google-News caveat.
- Ran `nb stamp`: words 2866 -> 2828, reading_minutes 12, sources 9.

## Required work

None blocking. For the writer's proof pass (owner: writer):
- Re-verify the corrected Linzen breakdown (Woman 93%, King 5%, never Man) against
  s5 during proof, since it is a content correction made by the editor.
- Re-run the full proof (links included) after these cuts; expect BLOCK:0 with the
  one intentional W-SENTENCE-DENSITY warning.

Optional, non-blocking (owner: writer): smooth the "Consider" opener; label or
consolidate the mixed-provenance stat strip; tighten "roughly a tenth."

Optional, non-blocking (owner: researcher): amend the evidence record to store the
"Efficient Estimation" abstract as a verbatim quote for the production trail (the
string is verbatim and was re-verified against arXiv:1301.3781 during this review).

## Decision

approve — after direct cuts, every load-bearing claim holds, the one factual error
(the geometrically impossible Linzen breakdown) and the one false timing claim are
corrected in place, and no new prose is owed; the writer runs the full proof and
re-verifies the corrected breakdown.
