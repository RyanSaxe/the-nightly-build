# Writer brief: word-of-the-day/sprezzatura (01)

## Your job
Draft the Word of the Day article on **sprezzatura** (550-800 words), then prove
it to `BLOCK: 0`. Draft only from the evidence record and voice guide.

## Begin with these exact inputs
- This brief.
- `../../commission.md` (angle, obligations).
- `../../editorial-direction.md` (house floor, headline standard, press voice,
  article template identity, series prompt).
- Voice guide: `../../writing-coach/01/voice-guide.md` (reread before drafting).
- Evidence record: `../../researcher/01/evidence.md` (your complete claim set).
- Initialized article: `../../../../library/word-of-the-day/sprezzatura.html`
  (edit this file; do not recreate the skeleton).
- Template context: `../../../../.nb-context/` (template-contract.yaml,
  runtime-assets.yaml, furniture/*). The `rs-word-card` markup is documented in
  `.nb-context/furniture/press.md`.

## The article to write
Open per the voice guide: on the scene or the paradox, NOT on a definition-as-
claim or "coined in YEAR." The `rs-word-card` still comes first as the fixed
entry furniture (word, pronunciation, part of speech, one cited plain-sentence
definition) — but your prose opening after it must earn the meaning through the
scene, not restate the card.

Track one argument across three eras (why the coiner needed the word → the older
idea he drew on → whether the pattern still holds), not three facts in sequence.
Load-bearing beats, all verified in the evidence record:
- The coinage: Castiglione, *Il libro del cortegiano* (*The Book of the
  Courtier*), Book I §26, at the court of Urbino (dialogue set 1507; published
  Venice 1528). Quote the coining line from **Opdycke's 1903 translation**,
  naming the translator in the same sentence: "a certain nonchalance that shall
  conceal design and show that what is done and said is done without effort and
  almost without thought." You may give the Italian "una certa sprezzatura, che
  nasconda l'arte" once. The motive: it is coined as the cure for its opposite,
  **affettazione** (affectation).
- The paradox Castiglione built in himself (§27, the Messer Roberto dancing
  anecdote): studied nonchalance that shows the strain becomes affectation —
  "he is striving with all his might to seem to be taking no thought, and this is
  taking too much thought." This is central, not a footnote.
- Classical lineage (context, not a citation Castiglione makes): the older
  rhetorical ideal that art should hide itself. Cicero, *De Oratore* 2.4
  (Crassus/Antonius concealing their learning) is verified. If you use the Latin
  tag "ars adeo latet arte sua" ("so does art conceal art"), attribute it
  correctly to **Ovid, *Metamorphoses* 10.251-252** — NOT the *Ars Amatoria*
  (the commission's original attribution was wrong; the evidence corrected it).
  Present lineage as lineage; Castiglione never names these sources.
- Present sense (ground it, don't assert): Helen De Cruz, "Sprezzatura and
  Wuwei," *The Philosopher*, Jan 11 2024 — applies the word to lute-performance
  practice and the figure-skating judging system's language rewarding "effortless
  power." Use it as the live modern instance.
- Optional texture: the etymological irony from Treccani — "sprezzatura" comes
  from *sprezzare* ("to disdain, to devalue," from Latin *pretium*, worth), so
  the word for graceful concealment is built from "to devalue." Use only if it
  earns its place.

## Hard constraints from the evidence record
- Do NOT quote Hoby's 1561 wording ("reckelesness"/"disgracing"): unverified.
  You may note the word is usually left untranslated / resists a single English
  gloss (a real, longstanding difficulty), without quoting Hoby.
- Do NOT cite or paraphrase the OED: it was gated (403), nothing from it is
  verified. Use Merriam-Webster as the dictionary authority (definition "studied
  nonchalance : graceful conduct or performance without apparent effort";
  pronunciation /sprāt-tsä-ˈtü-rä/; noun).
- Keep etymology (history) and present meaning distinct, per the series prompt.

## Source kinds (carry into data-nb-kind)
Primary: Castiglione (Opdycke translation / Italian original), Ovid, Cicero,
Louvre (only if the asset is used). Secondary: Merriam-Webster, Treccani,
Britannica, De Cruz. Number sources in first-citation order; add
`data-nb-locator`/`data-nb-url` only where the evidence supplies it.

## Source asset
Optional and lean-toward-skip for this smallest read. The Raphael portrait of
Castiglione (Louvre INV 611) is available if it clearly earns its place (the
portrait's own restraint as an image of the idea). If you use it, capture via
`nb asset` from the cited Louvre record, write a factual cited caption and useful
alt text, and make the prose spend what it shows. If it does not earn its place,
omit it — do not add decoration.

## Furniture / markup
Keep fixed engine assets, body classes, required HTML, and the `Sources` section
exactly as supplied. Use only documented furniture. No article-authored scripts,
styles, iframes, forms, or external images. Fill `nb-meta` with real values:
series word-of-the-day, slug sprezzatura, template article, mode open, order
null, date 2026-08-02, tags ["language","etymology"], measured sources and words,
reading_minutes, a real dek (a stance, not who-did-what-when), harness
"claude-code", model "claude-sonnet-5".

## Prove and hand off
Run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check ../../../../library/word-of-the-day/sprezzatura.html --series word-of-the-day --library /home/user/library`
(use the absolute article path
`/home/user/the-nightly-build/.nb-work/word-of-the-day/sprezzatura/library/word-of-the-day/sprezzatura.html`).
Treat warnings as revision notes: fix or record why left. Use `nb preview` if you
change layout/asset and inspect the render.

Write `draft-handoff.md` here with: the one-sentence original-work statement
(what this piece does to the evidence that the evidence does not do itself);
article/asset paths changed; proof result and any warnings left; remaining
evidence/voice questions. Return `DONE writer <draft-handoff-path>` after
`BLOCK: 0`, or a `REQUEST researcher/writing-coach/orchestrator <one-sentence>`
line if blocked. Keep content in files, not the control message.
