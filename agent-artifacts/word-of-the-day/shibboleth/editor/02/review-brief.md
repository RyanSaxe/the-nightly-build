# Editor brief — word-of-the-day/shibboleth (02, confirm recast)

## Role
Load and follow `skills/editor/SKILL.md`. Fresh read of the recast. You approved
everything in 01 except one required change (the 42,000 overclaim). Confirm that
change is resolved and that the recast introduced no new problem, then approve or
route again. Small direct fixes are yours; larger writing returns to the writer.

## What changed since your 01 review
Per `writer/02/draft-handoff.md`, the writer recast the **headline** (now "A
Sound No Ephraimite Could Fake Decided Who Crossed the Jordan Alive"), the
**dek** ("finds"→"notes"; 42,000 framed as the whole-war toll), and the **origin
paragraph** (added the Judges 12:4 battle before the fords; closes "the toll of
the whole war, battle and fords together. The text does not divide it between the
two."). Everything else is unchanged from the version you already cleared.

## Begin with these exact inputs (under `.nb-work/word-of-the-day/shibboleth/`)
- `agent-artifacts/word-of-the-day/shibboleth/editor/01/editorial-review.md` (your
  prior reads and the required change)
- `agent-artifacts/word-of-the-day/shibboleth/researcher/02/evidence.md` (the
  verified correction)
- `agent-artifacts/word-of-the-day/shibboleth/writer/02/draft-handoff.md`
- The article: `library/word-of-the-day/shibboleth.html`

## Focus this read
1. **Required change resolved?** Is the 42,000 now honestly the whole-conflict
   toll, with the v.4 battle context, and does nothing in the piece still pin all
   42,000 on the pronunciation test? Confirm against `researcher/02/evidence.md`.
2. **New headline/dek** against `spec/headlines.md`: does the new headline commit
   to something the piece establishes and avoid the machine tells (no colon
   subtitle; not a coiner-opener; not the bowdlerize "wrong person" reveal)? Is it
   accurate (the sound test decided who crossed alive — true to the fords scene)?
   Does the dek add without restating and take no misattributed number?
3. **No regressions:** the recast did not break the throughline, introduce slop,
   or exceed the word band (now 742, within 550-800).

## Proof
Confirm still clean (re-run if you edit):
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/word-of-the-day/shibboleth/library/word-of-the-day/shibboleth.html \
  --series word-of-the-day --library /home/user/library
```

## Output (write only this)
`agent-artifacts/word-of-the-day/shibboleth/editor/02/editorial-review.md`

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/word-of-the-day/shibboleth/editor/02/editorial-review.md`
  (approve, no required change, BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `REQUEST researcher <need>` /
  `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
