# Editorial review: word-of-the-day/luddite (editor/01)

## Skeptic

Thesis: the Luddites were skilled textile workers who broke machines not out of
fear of the new, but because those machines were being used to cut wages and
destroy their trades; the word later flattened into a slur for anyone who
distrusts technology. Load-bearing claims: (1) Ned Ludd is tradition, not a
documented person; (2) the opposition was to the *use* of machinery to deskill
and underpay, not to machinery as such (the Thompson/Merchant reading); (3) the
state answered with a capital statute, ~12,000 troops, and 17 York executions;
(4) the word's meaning inverted, and the ruling class flattened it deliberately.

I opened all ten citation hrefs exactly as the article prints them. Every one
resolves and lands on the source itself, including s10, whose evidence entry is
`http` but which the article prints and serves at `https`. The `data-nb-kind`
labels hold: Merriam-Webster (s1, definition and first-known-use) and Hansard
(s7, the speech text) are correctly primary; the rest are secondary reporting
from outside the authoring party, correctly labelled. No secondary is dressed as
primary and no independent-source gap is hidden.

Required corrections all hold. The Wellington/Peninsular comparison is gone; the
deployment is stated as "some twelve thousand troops, a figure that traces to
the historian F. O. Darvall" (confirmed against s8, which itself rejects the
Wellington claim). The York count reads as seventeen with the 8-Jan(3, Horsfall)
/16-Jan(14, Rawfolds Mill attack and burglaries) breakdown, each half confirmed
against s9 and s10. The definition and the 1811 opening date rest on
Merriam-Webster (s1); no OED first-use credit appears anywhere, and the OED is
absent from the sources. The present sense is anchored in Merriam-Webster (s1)
and Merchant/TIME (s5); the paywalled NYT "Luddite Club" instance was dropped.

Central distinction: carried correctly as the better-supported reading, not a
neutral given — "The reading now best supported by historians, E. P. Thompson's
and Brian Merchant's after him, is that the Luddites opposed the use of machinery
to cut wages and gut a craft, not machinery itself" (s5). I verified s5 both
quotes the Merchant line verbatim and names E. P. Thompson, so the twin
attribution is sourced, and the evidence record backs Thompson as the reading's
originator. Reasoned and cited, not asserted.

Named-people/date checks: Ned Ludd's status ("led no one, because he had almost
certainly never existed") matches s3's "almost certainly fictional." Byron's
maiden speech, 27 Feb 1812 in the Lords, and the stocking-frame quote are
verbatim in s7; at that date Byron (b. 22 Jan 1788) was indeed twenty-four. The
Act's royal assent (20 March 1812), lapse (1 March 1814), and 1813 transportation
replacement match s6. Horsfall (s9) and Cartwright's Rawfolds Mill (s10) are
correct.

Breaks found and handled:
- **Ned Ludd described as an "apprentice."** Unsupported. The cited s1 calls him
  a "workman"; s3 calls him a "weaver"; neither says apprentice. Fixed directly
  to "workman" (matches s1's etymology exactly: "18th century Leicestershire
  workman who destroyed a knitting frame").
- **"cut in a sheet and sewn to shape so the seams gave."** This cut-up
  mechanism is in no cited source; s4 supports only "cheap, inferior quality
  goods." Cut as an unsupported nonessential detail; "cheaply and badly" survives
  and stays sourced.
- **"forty-pound shears."** The weight is in no source (s4 mentions only the
  shearing frame). Cut "forty-pound"; croppers finishing cloth by hand with
  shears is definitional and sourced by context.
- **Dek attributes the York gallows to the framework knitters.** The framework
  knitters were the Nottingham stocking-frame trade; the York hangings were
  Yorkshire croppers and West Riding Luddites, a distinction the body itself
  draws. This is a display-text error in the most-read line and touches the
  nb-meta JSON, so it routes to the writer (see Required work).

The 1779 date sits in the anecdote sentence cited to s1, which does not carry it;
s3 does, and s3 is cited within the same section, so under the per-section cite
rule the claim is covered. Not blocking.

## Cut

The piece is already lean; most sentences earn their place on a sourced fact or
a reasoning step. Direct cuts removed the two unsourced embellishments above
(cut-up seams, forty-pound shears) and repaired one reflex semicolon (the Act's
lapse and the 1813 replacement are sequential facts about two statutes, so a
period is plainer than the semicolon that joined them).

Earned-contrast count is at but not over ceiling: "were not smashing frames
because frames were new" and "opposed the use of machinery... not machinery
itself" are both real, named misconceptions; the Merchant "not anti-machinery"
line is a quotation, and the closer is a positive statement, not an "X not Y"
mold. No prompt leakage: no planning labels, selection rules, self-grading, or
assignment-fulfilled claims survive into the prose.

Recent-pattern check passed. The opener is scene-first ("Toward the end of 1811,
in the hosiery villages around Nottingham...") — not the banned eponym-reveal
shape, and distinct from the silhouette/quisling/bowdlerize telling. The arc
(name → the machines' purpose → the state's answer with a Hansard note → the
meaning's drift) is not the recent "definition → one scene → spread → the layer
that stayed" outline. Headline carries no colon subtitle; the dek uses none of
the banned molds (no semicolon reversal, suspended question, or comma triad).
Section headings are concrete steps of the argument in the piece's own nouns,
varied in shape. The one `nb-note` (Byron's speech) is deliberate emphasis on
primary evidence, not decoration.

## Reader

Read straight through, the piece hands back exactly what its sources scattered:
the name honours a man who almost certainly never lived; the workers were skilled
and broke machines being used to gut their wages and trades, not machines as
such; the state answered with the gallows and Byron rose against it; and the
ruling class then flattened the word into the insult we still use. That is more
than any one source gives, and it matches the original-work sentence's claim to
join four sources that never meet. The prose sits with the Wilton/Merchant/M-W
exemplars — scene-first compression, dry understatement kept on documented facts,
a flat landing ("What they would not accept was a machine turned against the
trade that fed them") — not a median summary. The headline reads true as the
largest claim: they broke machines they knew how to run.

## Edits

- Ned Ludd descriptor "apprentice" -> "workman" (s1's own term; unsupported before).
- Cut "cut in a sheet and sewn to shape so the seams gave," (unsourced mechanism).
- Cut "forty-pound" before "shears" (unsourced weight).
- Semicolon after "1 March 1814" -> period (reflex-punctuation repair).
- Ran `nb stamp`: words 736 -> 723, sources 10, reading_minutes 3 (still in band).

## Required work

- **writer:** Correct the dek's group attribution. As written it has England
  answer "the framework knitters" with "the gallows at York," but the York
  hangings were of Yorkshire croppers and West Riding Luddites, not the
  Nottingham framework-knitting trade the body carefully distinguishes. Replace
  "the framework knitters" with "the Luddites" (the state answered the whole
  movement with both the statute and the York gallows). Apply the fix in both
  the `nb-dekline` and the `nb-meta` `dek`, then re-stamp and re-run the proof.

## Decision

revise — the article is sourced, cited, and clean after direct cuts, but the
dek pins the York executions on the wrong trade, a display-text error in the
paper's most-read line that only the writer can fix in prose and metadata
together.
