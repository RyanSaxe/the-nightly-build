# Editor brief — word-of-the-day/shibboleth (01)

## Role
Load and follow `skills/editor/SKILL.md`. You are the fresh-eyes gate. Give the
drafted article the three ordered reads (skeptic, cut, reader). Make cuts and
small prose fixes directly in the HTML; anything past a word or clause of NEW
writing returns to the writer; evidence gaps return to the researcher. Approve
only with an editor `DONE` and no required change.

## Begin with these exact inputs (under `.nb-work/word-of-the-day/shibboleth/`)
- `agent-artifacts/word-of-the-day/shibboleth/editorial-direction.md`
- `agent-artifacts/word-of-the-day/shibboleth/writer/01/brief.md` (the EXACT writer
  brief — check for instruction leakage into the prose)
- `agent-artifacts/word-of-the-day/shibboleth/writer/01/draft-handoff.md`
- `agent-artifacts/word-of-the-day/shibboleth/researcher/01/evidence.md`
- `agent-artifacts/word-of-the-day/shibboleth/writing-coach/01/voice-guide.md`
- The article: `library/word-of-the-day/shibboleth.html`

## The three reads
1. **Skeptic.** Test the thesis (a shibboleth is an *involuntary, identity-bound*
   test, distinct from a chosen password) and every claim it rests on. Reopen the
   sources in the evidence record as needed: is the Judges 12 account accurate; is
   the 42,000 figure honestly caveated (Judges is the only record); is the
   Hebrew literal-meaning dispute presented without picking a winner; is the
   sense-development timeline honest (do not collapse "entered English" and
   "became figurative"); is the pronunciation IPA (not MW respelling mislabeled);
   is the modern PLOS ONE use real and correctly represented; are the discarded
   NYT/arXiv items correctly absent. Audit each source's `data-nb-kind`.
2. **Cut.** Remove any sentence with no fact, claim, or reasoning work:
   self-grading, stock reveals, signposts, instruction leakage, manufactured
   punchlines, hedged not-X-but-Y beyond the ceiling, scaffold headings. It is a
   550-800 word piece; every sentence earns its place.
3. **Reader.** What does the piece give beyond its sources? Compare with the
   writer's original-work claim in draft-handoff. Judge the voice against the
   guide and the house floor. Retest the headline and dek against `spec/headlines.md`
   (no colon machine-tell; dek adds, doesn't restate; no coiner-opener; not the
   bowdlerize "wrong person" reveal or quisling eponym framing).

## After edits
Re-run the proof and confirm it still passes:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/word-of-the-day/shibboleth/library/word-of-the-day/shibboleth.html \
  --series word-of-the-day --library /home/user/library
```
Must remain BLOCK: 0.

## Output (write only this)
`agent-artifacts/word-of-the-day/shibboleth/editor/01/editorial-review.md`
Record the three reads, every change you made directly, and any required change
you are routing back (to whom and why). If you approve, say so explicitly.

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/word-of-the-day/shibboleth/editor/01/editorial-review.md`
  — ONLY if you approve with no required change (article publishable as-is after
  your direct edits, proof still BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` /
  `REQUEST researcher <need>` / `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
