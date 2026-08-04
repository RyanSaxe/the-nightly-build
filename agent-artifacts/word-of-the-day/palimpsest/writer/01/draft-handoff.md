# Draft handoff: word-of-the-day/palimpsest (01)

## Original work
The piece takes the one physical fact recovered from the Archimedes leaf — an
erased text still legible beneath the writing that overwrote it — and makes it
the argument that joins the word's literal manuscript sense to its modern
extended sense, then grounds that extended sense in the three separate
attestations the evidence records (Merriam-Webster sense 2, De Quincey 1845,
Canadian Geographic 2015) instead of inferring it from the Greek. The evidence
holds those facts apart; the article is the thing that makes them one claim, and
that claim is visible in the closing section and the "sense outgrows the
parchment" turn.

## Proof result
`./nb check ... --series word-of-the-day` with links: **BLOCK: 0, WARN: 0,
verdict PUBLISHABLE.** 684 words (band 550-800), 6 sources (min 4), 3 flex
sections (band 2-5). No warnings left standing.

Note on how BLOCK: 0 was reached: the initial draft renamed the opening section;
the `word` template requires `data-nb-section="orientation"`, so the opening
scene section keeps that label with its own heading. Three W-SENTENCE-DENSITY
warnings were cleared by splitting the sentences (the last, the iron/X-ray
sentence, was a genuine clause pile-up and was split on its merits).

## Open questions
- **Heiberg's given name.** I used "Johan Ludvig Heiberg" (the commission's
  spelling and the historically correct form for the Danish philologist). The
  researcher's evidence paraphrase spells it "John Ludwig Heiberg." Surname is
  uncontested across all sources; only the given name differs, and no source
  quote in evidence.md fixes the spelling. Flagged so the editor's
  check-against-evidence does not read this as a fabrication. If the editor wants
  strict evidence-parity, change to "John Ludwig"; I judged the commission's
  authoritative spelling the right call.
- **Pronunciation.** The `rs-word-card` carries `/ˈpa-ləmp-ˌsest/`. This is
  Merriam-Webster's own pronunciation (the s1 entry that owns the definition and
  etymology), but evidence.md did not separately log the pronunciation string.
  It is uncontested and from the cited authority; flagged only for completeness.
- **"iron-based ink."** Evidence attests "iron" in the original ink (the metal
  the X-ray beam detects), not the specific compound; I wrote "an iron-based ink"
  rather than "iron gall ink" to stay inside the record.
