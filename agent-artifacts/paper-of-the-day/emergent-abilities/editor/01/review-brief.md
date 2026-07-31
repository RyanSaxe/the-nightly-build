# Editor brief — paper-of-the-day/emergent-abilities (01)

## Role
Load and follow `skills/editor/SKILL.md`. Fresh-eyes gate. Three ordered reads
(skeptic, cut, reader). Cuts and small prose fixes go directly in the HTML; new
writing past a word/clause returns to the writer; evidence gaps to the researcher.
Approve only with `DONE` and no required change.

## Begin with these exact inputs (under `.nb-work/paper-of-the-day/emergent-abilities/`)
- `agent-artifacts/paper-of-the-day/emergent-abilities/editorial-direction.md`
- `agent-artifacts/paper-of-the-day/emergent-abilities/writer/01/brief.md` (EXACT
  writer brief — check for instruction leakage into prose)
- `agent-artifacts/paper-of-the-day/emergent-abilities/writer/01/draft-handoff.md`
- `agent-artifacts/paper-of-the-day/emergent-abilities/researcher/01/evidence.md`
- `agent-artifacts/paper-of-the-day/emergent-abilities/writing-coach/01/voice-guide.md`
- The article: `library/paper-of-the-day/emergent-abilities.html`

## The three reads (paper template)
1. **Skeptic.** Is the reconstruction of Wei et al.'s claim faithful, and is the
   Schaeffer "mirage" argument represented accurately? Reopen both papers via the
   evidence record. Check specifically: the **abstract is verbatim** (not
   paraphrased) and cited; the metric argument (discontinuous exact-match/
   multiple-choice vs continuous token-edit-distance/Brier) is stated correctly;
   the worked example uses **real named thresholds, not fabricated curve points**
   (the researcher flagged Schaeffer has no numeric table — confirm nothing was
   invented); the map of where the two papers agree/disagree is honest; the
   afterlife (Wei's blog rebuttal, Barak's defense, the 2024/25 follow-ons) is
   fairly used; the verdict separates artifact from real phenomenon without
   overreach. Audit each source's `data-nb-kind` and every `data-nb-locator`.
2. **Cut.** Remove sentences doing no fact/claim/reasoning work; self-grading,
   the "paper's own table already recorded the catch" reveal, the "field has no
   agreed account" stock closer, signposts, instruction leakage, manufactured
   punchlines, hedged not-X-but-Y beyond the ceiling, scaffold headings. 2858
   words is within band but tighten where it drifts.
3. **Reader.** What does the piece give beyond the two papers? Compare with the
   writer's original-work claim. Judge voice vs the guide/house floor. Retest
   headline and dek vs `spec/headlines.md` (no colon machine-tell; dek adds and
   takes a stance).

## After edits
Re-run and confirm still clean:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/paper-of-the-day/emergent-abilities/library/paper-of-the-day/emergent-abilities.html \
  --series paper-of-the-day --library /home/user/library
```
Must remain BLOCK: 0.

## Output (write only this)
`agent-artifacts/paper-of-the-day/emergent-abilities/editor/01/editorial-review.md`
The three reads, every direct change, any required change routed (to whom, why).

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/paper-of-the-day/emergent-abilities/editor/01/editorial-review.md`
  (approve, no required change, proof BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `REQUEST researcher <need>` /
  `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
