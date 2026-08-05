# Editorial review: word-of-the-day/ultracrepidarian (editor/01)

## Skeptic

Thesis: *ultracrepidarian* names one precise fault — competence in a single
domain spent as though it covered the next — and the word carries that sense
through a documented two-layer origin, from Apelles' cobbler proverb to the
1819 English coinage against William Gifford. The piece stands on four claims:
the definition (card); the Pliny anecdote and its Latin (orientation + note);
the 1819 first-recorded English use against Gifford, with coinage unsettled
(hazlitt-gifford); and the semantic distinction against *dilettante* /
*presumptuous* (overreach). Headline and dek carry claims too.

I opened every citation href as the article prints it. All six resolve and
land on the source's own page, and each supports the sentence it backs:

- **s1 Dictionary.com** — carries both parts-of-speech definitions and, in its
  Example Sentences panel, the verbatim 2023 *Salon* line the overreach section
  quotes ("toss the phrase ultracrepidarian at them because they don't know
  what they're talking about"). The article's bracketed "toss[es]" is an honest
  editorial inflection. Resolves.
- **s2 LacusCurtius (Pliny, Latin)** — §85 reads "ne supra crepidam sutor
  iudicaret, quod et ipsum in proverbium abiit." The note's Latin
  (*Ne supra crepidam sutor iudicaret.*) matches glyph-for-glyph
  (capitalized first word + terminal period for the standalone quotation). The
  primary also fixes Apelles as Greek ("Apelles Cous," of Cos) — load-bearing
  for the finding below.
- **s3 Attalus (Pliny, English)** — "a shoemaker in his criticism must not go
  beyond the sandal," matching the note's gloss.
- **s4 lordbyron.org** — Leigh Hunt's *Examiner* reprint of Hazlitt's Letter,
  carrying "You have been well called an Ultra-Crepidarian critic" verbatim.
  Labeled `primary`; it reproduces Hazlitt's own words, so primary for the
  quotation is defensible.
- **s5 Word Histories** — confirms 1819, *A Letter to William Gifford, Esq.*,
  and that Gifford "served an apprenticeship to a shoemaker." Resolves.
- **s6 Wikipedia** — confirms the Charles Lamb attribution ("might have been
  coined by Charles Lamb instead") and Leigh Hunt's 1823 *Ultra-Crepidarius*.
  Resolves.

Accuracy checks the round called for, all held in the body: the piece says
1819 "fixes the word's first appearance in the printed record, not the moment
anyone invented it," reads Hazlitt's *well called* as an already-applied
epithet, and flags the Lamb proposal — it never says Hazlitt coined it.
Pliny's *supra crepidam* is printed correctly and the pivot names the later
*ultra crepidam* as the reshaped tag English took its prefix from.
Merriam-Webster is absent; the definition rests on the resolving Dictionary.com
page. Baptist News (403) is absent; the modern-use ground is the Salon line via
Dictionary.com. `data-nb-kind` labels are sound.

**The break — the dek.** The dek is factually wrong on two counts, and the dek
is display text (the costliest place to be wrong):
1. "a **Roman** painter's rebuke" — Apelles was Greek, not Roman. The body
   itself says "the most celebrated of the Greeks," and the primary (s2) places
   him at Cos. Pliny was the Roman who recorded it; the rebuke is Apelles' and
   Apelles was Greek. The dek contradicts its own article and its primary.
2. "a cobbler who **fixed** a sandal" — in the anecdote the cobbler *faulted*
   the sandal (a loop missing); the *painter* fixed it, then the cobbler
   presumed to judge the leg. The body has this right ("he pointed out, and the
   painter fixed it"); the dek misattributes the repair.

Both are routed to the writer: the fix requires recasting beyond a clause and
must be synced into the `nb-meta` JSON dek (markup I do not touch) with a
re-proof. Named precisely below so it cannot be reworded around.

Headline reads clean on sourcing (Gifford was apprenticed to a shoemaker;
Hazlitt applied the epithet). One soft note: "had once been a shoemaker"
compresses "served a shoemaker's apprenticeship" (he left the trade for
Oxford). Fair compression, the body carries the precise version, non-blocking.

## Cut

The piece is tight (606 words on arrival) and mostly earns its place: two
scenes each landed by a quoted primary, joined by the one licensed pivot
("Seventeen centuries later, in another language..."), then the licensed
corrected-assumption (dilettante) and the licensed dry closing turn ("anyone
can throw it," which spends the opening scene's own Apelles image). No eponym
opener — it opens on the corrected cobbler, names arriving only where earned.
Dek uses no banned mold. No prompt leakage; the contrasts ("well called, not I
call you"; "not the moment anyone invented it") are earned and load-bearing,
and the dilettante correction is separately licensed.

One cut made: the self-grading signpost "The wording matters." at the head of
the second Hazlitt paragraph. It announced the significance of a point the very
next sentence demonstrates; the demonstration stands alone. I considered
cutting "The distinction still earns its keep" but kept it — it states the
section's actual claim (why the word still earns vocabulary space), which the
template wants and the following sentences substantiate. Ran `nb stamp`:
words=603, still inside the 550-800 band.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not give me: the line the word actually draws. The sources
supply the definition, the anecdote, and the 1819 record separately; none of
them reads the anecdote structurally to separate *ultracrepidarian* (competence
in one place, overspent) from mere presumption or dilettantism. The piece does
— the cobbler was right about the sandal and wrong about the leg — and that is
the draft-handoff's stated original work, delivered. The prose sits with the
voice-guide exemplars, not a median summary: economy is the wit, two quotes
doing their own work back to back. The headline as the largest claim holds on
its sourcing.

## Edits

- Cut "The wording matters." (self-grading signpost) from the second
  hazlitt-gifford paragraph.
- Ran `nb stamp` (words 606 -> 603).

## Required work

- **writer** — Correct the dek's two factual errors and sync both surfaces
  (the `nb-meta` JSON `dek` and the `<p class="nb-dekline">`), then re-proof:
  (a) Apelles was **Greek**, not "a Roman painter"; (b) the cobbler **faulted**
  the sandal — the painter fixed it — so "a cobbler who fixed a sandal" is
  wrong. Blocking: display-text accuracy.
- **writer** — Reconcile the word-card pronunciation to its cited authority.
  Dictionary.com (s1, the card's citation) respells it
  `uhl-truh-krep-i-dair-ee-uhn`; the card prints `/uhl-truh-krep-ih-DAIR-ee-uhn/`,
  inserting an "h" ("krep-ih" for the source's "krep-i") not present in the
  source. Change "krep-ih" to "krep-i" to match glyph-for-glyph (the DAIR
  stress-cap is an acceptable convention for the source's bolded "dair"), or
  drop the respelling. This resolves the writer's open question 1: verified
  against the source, and it does not match as printed. Small, but a sourced
  claim in the card must match its source.

Open question 2 ruled, no action: OED does **not** need to be named. The 1819
first-attestation rests on Word Histories (s5), which resolves and directly
carries both the date and Gifford's shoemaker apprenticeship; the brief
permitted a resolving secondary and the handling is honest.

## Decision

revise — the dek prints two factual errors in display text (Apelles was Greek,
not Roman; the cobbler faulted the sandal, the painter fixed it), and the card
pronunciation does not match its cited source; both belong to the writer and
the body is otherwise accurate, tight, and closer to the voice-guide exemplars
than a summary.
