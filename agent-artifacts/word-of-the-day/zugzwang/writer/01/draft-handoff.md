# Draft handoff — word-of-the-day/zugzwang (writer, round 01)

## Original work

The piece does what no single source in the evidence record does on its
own: it assembles the corrected origin chronology (the 1858 German coinage
in *Deutsche Schachzeitung*, the overlooked 1894 *Ulster Echo* citation that
predates Emanuel Lasker's 1905 note by eleven years, and the 1929
naturalization into English chess writing via Nimzowitsch's *My System*)
into one corrected timeline that displaces the Lasker-first folklore the
commission itself started from; then it derives the operative test for the
word — whether standing still has stopped being an option, not whether the
remaining options are any good — directly from Nimzowitsch's own account of
what happens inside a zugzwang position, rather than from a stacked list of
dictionary definitions; and it verifies that exact test against two
independently sourced non-chess uses (Freedman on the Russia-Ukraine war,
the Finnish Institute of International Affairs on the same war) instead of
asserting the transfer is valid on the strength of the word alone.

## Files changed

- `library/word-of-the-day/zugzwang.html` — full draft, only file changed.
  No chart or source asset: the evidence record found no verified visual to
  capture (see evidence.md, "Source assets"), so none was added.

## Proof result

`nb check library/word-of-the-day/zugzwang.html --series word-of-the-day --repo /home/user/the-nightly-build`
→ **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE.

Warnings hit and resolved during drafting (none left standing):
- `W-LENGTH-HIGH` (818 words, band is 550–800): fixed by tightening the
  Nimzowitsch paragraph — replaced an over-long full-sentence quotation with
  a short exact-phrase quote ("the necessity of making a move") plus my own
  paraphrase of the surrounding clause. Brought the count to 794.
- `W-SENTENCE-DENSITY` (the same 47-word quoted sentence): resolved by the
  same edit — the quotation no longer runs as one long sentence.
- `W-SELF-COUNT`: `nb-meta.words` and `reading_minutes` were placeholders
  (0); set to the measured 794 words / 4 min, matching the byline.

I also escaped a bare `&` in the Nimzowitsch Google Books source href
(`&pg=PA36` → `&amp;pg=PA36`) for HTML validity; not flagged by `nb check`
but corrected on inspection.

## Notes for the editor

- **1604 Salvio omitted deliberately.** The evidence record confirmed only
  that Salvio's 1604 *Trattato* exists and is digitized, not the specific
  endgame study or that it demonstrates zugzwang (that attribution traces to
  an unread secondary source). Rather than hedge it awkwardly in a
  550–800-word piece, I left it out entirely. Flag if the edition wants it
  restored with a hedge.
- **Word-card pronunciation carries no separate inline citation**, matching
  the furniture's fixed sample shape (only the definition sentence wears a
  `<sup class="nb-cite">`). The IPA is Oxford Learner's Dictionaries'
  (`/ˈzʌɡzwæŋ/, /ˈzuːɡzwæŋ/`), which is cited elsewhere in the piece (source
  5) for its definition. Merriam-Webster's own respelling was not used
  because the evidence record flags it as MW's proprietary system, not
  standard IPA.
- **Heidenfeld's stricter "true zugzwang" test** (contested-questions
  material in the evidence record) is addressed directly in "The
  compulsion, not the choice," including his rejection of the
  Sämisch–Nimzowitsch "Immortal Zugzwang Game" as genuine zugzwang. The
  piece states which definition it follows and why (the sense that
  transfers beyond chess) rather than papering over the disagreement.
- **OED and Etymonline's 1904 date are not cited anywhere** in the piece —
  the evidence record flags 1904 as a stale/erroneous date from the 1989
  print OED that Winter corrects to 1905. The piece uses only 1894 (Ulster
  Echo) and 1905 (Lasker), both page-verified via Winter.
- All 7 sources trace to evidence the researcher opened directly (no
  Wikipedia, no unread JSTOR lead). `min_sources` is 4; the piece carries 7.
- No remaining evidence or voice question.

DONE writer library/word-of-the-day/zugzwang.html
