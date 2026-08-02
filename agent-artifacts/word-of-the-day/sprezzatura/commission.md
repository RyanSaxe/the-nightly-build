# Commission: word-of-the-day/sprezzatura

## Assignment
Tonight's Word of the Day is **sprezzatura**. Write the paper's smallest read:
a precise definition, the documented story of the word's origin, and the
distinction the word preserves that keeps it useful far outside its origin.

## Angle
Sprezzatura was coined as the name for a paradox: the highest art is the art
that hides the effort it took. Baldassare Castiglione invented the term in *Il
libro del cortegiano* (*The Book of the Courtier*, 1528) to name the studied
nonchalance that makes difficult things look effortless, and he coined it as the
cure for its opposite, *affettazione* (affectation). The useful modern sense
carries both halves: the word names concealed effort wherever mastery must look
easy, and it already carries the failure mode Castiglione diagnosed, the visible
strain of trying to look effortless. Trace the coinage, its classical lineage
(the Latin rhetorical ideal of art concealing art), and where the pattern earns
its keep now.

## Intended reader
The house reader (mathematically and technically trained, well-read) meeting an
unusual word. No specialist background assumed. This is an entertaining, exact
short read, not a lexical survey.

## Mode / template
mode: open. template: article (word bands 550-800). The `rs-word-card` furniture
opens the piece (documented in `.nb-context/furniture/press.md`): word,
pronunciation, part of speech, one cited plain-sentence definition. Beyond the
card, no fixed section structure; name flex sections for this piece's argument.

## Contribution required
The piece must give the reader more than a dictionary would: the exact origin
(who coined it, in what text, in what setting, and what he meant), the reason
the coinage was needed (the contrast with *affettazione*), and the transferable
pattern that makes the word worth keeping. It must ground the present sense in
at least one real, cited example of modern use, not assert it.

## Source obligations
- Template floor: **minimum 4 sources**; article template, per-section citation.
- Cite an **authoritative dictionary** (OED and/or Merriam-Webster) for the
  definition, pronunciation, and part of speech. This is a secondary authority
  on present meaning; label honestly.
- The **primary** source for the coinage is Castiglione's own text
  (*Il Cortegiano*, Book I, the passage where Count Lodovico da Canossa
  introduces "una certa sprezzatura"). Use a public-domain edition/translation
  and cite the located passage. Etymology is history, not proof of present
  meaning: keep the origin and the present sense distinct.
- Ground the present sense in a **real, dated, cited** example of modern usage
  (published writing that uses the word in its current sense).
- Every URL must resolve; a paywall/403 is gated, not verified. No unread cites.

## Starting sources (verify and extend; not exhaustive)
- OED / Merriam-Webster "sprezzatura" entries.
- Castiglione, *The Book of the Courtier*, Book I (Hoby 1561; or Opdycke 1901 /
  a public-domain translation on archive.org / Project Gutenberg / a scholarly
  edition). Locate the exact coinage passage and Castiglione's definition, plus
  the *affettazione* contrast.
- Classical lineage: the rhetorical ideal of concealed art (e.g. Cicero on
  hiding artifice; Ovid, *Ars Amatoria*, "ars adeo latet arte sua"). Treat as
  context; verify any quotation against a real edition.
- One modern usage in the effortless-mastery sense (a reputable published
  source, dated).

## Relevant prior coverage (avoid repeating)
Recent Word of the Day: umwelt, apophenia, petrichor, solastalgia, mondegreen,
limerence, quisling, kayfabe, bowdlerize, shibboleth, zugzwang. Sprezzatura is
not an eponym, so avoid the eponym-correction shape used for bowdlerize and
quisling. It shares nothing with these subjects.

## Structures not to inherit
- Openers: recent pieces open on a bare definition-as-claim ("Zugzwang means
  ...") or on "X coined it in YEAR for ...". Do not open on that formula.
- Deks: recent deks are "who did what, when" facts; find this piece's own line.
- Do not close on a reading list or a pointer away from the piece.

## Neighboring articles tonight
current-events, tech-news, paper-of-the-day (ML), investing lesson,
parenting-research. Word of the Day is the standalone short read in Daily
Reading; no overlap of subject or shape with the others.

## Output paths
- Article: `.nb-work/word-of-the-day/sprezzatura/library/word-of-the-day/sprezzatura.html`
- Artifacts under `agent-artifacts/word-of-the-day/sprezzatura/`.

## Harness / model (resolved, balanced profile)
- harness: `claude-code`
- writing-coach: model `claude-sonnet-5`, effort low
- researcher: model `claude-sonnet-5`, effort high
- writer: model `claude-sonnet-5`, effort medium (record this in `nb-meta`)
- editor: model `claude-opus-4-8` (inherit), effort high, required
