# Writer brief — word-of-the-day/shibboleth (02, recast)

## Why this round
The editor's skeptic read found the article overclaims the 42,000: it is the
**whole-conflict Ephraimite toll** (Judges 12:4 has Gilead defeat Ephraim in
battle before the fords test; 12:6 closes the episode with "forty-two thousand …
fell at that time"), **not** the count killed by the shibboleth/sibboleth
pronunciation test. No source splits battle vs. fords deaths. The correction is
verified in `researcher/02/evidence.md`.

## Begin with these exact inputs
- `agent-artifacts/word-of-the-day/shibboleth/researcher/02/evidence.md` (the
  correction: verbatim v.1-6, safe/unsafe recast phrasings)
- `agent-artifacts/word-of-the-day/shibboleth/editor/01/editorial-review.md` (the
  required change and the editor's other reads)
- The current article: `library/word-of-the-day/shibboleth.html` (already has the
  editor's two splice fixes; still BLOCK: 0)
- For unchanged context: `researcher/01/evidence.md`, the voice guide, the
  writer/01 brief.

## Required change (recast only what the correction touches)
1. **Headline.** It currently pins all 42,000 deaths on a mispronounced consonant
   ("A Mispronounced Consonant Cost 42,000 Ephraimites Their Lives"). Rewrite it
   so it does not claim the test alone killed 42,000. Keep it specific and
   committed per `spec/headlines.md` (state a true finding about the word/episode;
   no colon machine-tell; no coiner-opener). The surprise can be the involuntary
   phoneme test itself, or the word's afterlife — but it must be TRUE to the text.
2. **Dek.** Editor flagged "finds"→"notes" and any causal overclaim; make the dek
   add what the headline leaves out and take a stance without misattributing the
   number.
3. **Origin paragraph.** Add the v.4 battle context so the sequence is honest
   (quarrel → Gilead defeats Ephraim in battle → Gilead holds the fords → the
   shibboleth test on fugitives → 42,000 "fell at that time" as the episode's
   total). Phrase 42,000 as the whole-conflict toll; the text gives no fords-only
   count. Use the correction's safe phrasings; avoid its unsafe ones.
4. Leave everything the editor did NOT flag intact (the sh/s mechanism section,
   the Hebrew literal-meaning dispute, the sense-development timeline, the PLOS
   ONE modern use, the IPA pronunciation, source kinds). Do not re-litigate
   settled parts. Keep the piece 550-800 words.

## Proof (run to BLOCK: 0)
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/word-of-the-day/shibboleth/library/word-of-the-day/shibboleth.html \
  --series word-of-the-day --library /home/user/library
```
Update `nb-meta.words` to the measured count if it changed.

## Also write
`agent-artifacts/word-of-the-day/shibboleth/writer/02/draft-handoff.md`: what you
changed (headline, dek, origin paragraph), the corrected framing of 42,000, the
new word count, and the proof result.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/word-of-the-day/shibboleth/writer/02/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work only. Do not tour the repo/archive.
