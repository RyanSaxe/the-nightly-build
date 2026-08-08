# writer brief: word-of-the-day/anosognosia (02)

Inputs:
  ../../editor/01/editorial-review.md       the finding to apply (the pronunciation correction)
  ../../researcher/02/evidence.md           the verified M-W pronunciation
  the article: .nb-work/word-of-the-day/anosognosia/library/word-of-the-day/anosognosia.html
Output: writer/02/draft-handoff.md

Proof: ./nb check .nb-work/word-of-the-day/anosognosia/library/word-of-the-day/anosognosia.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

Single required fix (editor/01): the word card's pronunciation contradicts Merriam-Webster.
Correct the card's pronunciation string to the exact M-W value verified in researcher/02:

  ˌa-nō-ˌsäg-ˈnō-zh(ē-)ə

Only the second syllable changes (nə -> nō, macron); every other character, stress mark,
the (ē-) parenthetical, and the terminal schwa already match. Change nothing else — the
editor already approved the rest and made its own two direct cuts (which stand). Keep
nb-meta harness "claude-code-routine" / model "Opus 4.8". Re-run the full proof to BLOCK: 0.
Note in the handoff exactly what you changed.
