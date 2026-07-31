# Writer brief — tech-news/2026-07-31 (02, item-2 fix)

## Why this round
The editor found one blocking fault in **item 2 (Gemini Robotics 2)**. The
sentence "DeepMind traces the split to hardware…" attributes a causal claim to
DeepMind that its own post does not make (the post says only that multi-finger
manipulation "remains challenging"). The hardware-split framing is TheNextWeb's,
and two numbers are wrong. The evidence record already carries the correct
attribution and figures. Everything else in the article is clean and the editor
cleared it.

## Begin with these exact inputs
- `agent-artifacts/tech-news/2026-07-31/editor/01/editorial-review.md` (the
  required change)
- `agent-artifacts/tech-news/2026-07-31/researcher/01/evidence.md` (correct
  attribution + figures for item 2)
- The article: `library/tech-news/2026-07-31.html`

## Required change (item 2 only)
Fix the "DeepMind traces the split to hardware…" sentence so that:
1. The **hardware-split framing and the gripper-cluster comparison are attributed
   to TheNextWeb and cited to s5**, not presented as DeepMind's causal claim
   (DeepMind's post says multi-finger manipulation "remains challenging" — nothing
   causal). Keep DeepMind's own claims cited to the DeepMind primary.
2. Correct "**68% to 90%**" to the sourced **74–90%** two-fingered-gripper range
   (the 68.4% figure is Apollo 2's Inspire-hand pick, NOT a two-fingered gripper —
   do not fold it into the gripper range).
3. Change "**22-joint**" to the primary's "**22 degree-of-freedom**."
Or cut the sentence entirely if that reads cleaner. Do not touch the other three
items — the editor cleared them. Keep the two voices (DeepMind's claims vs
TheNextWeb's framing) distinct.

## Proof (run to BLOCK: 0)
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html \
  --series tech-news --library /home/user/library
```
Update measured counts if they changed.

## Also write
`agent-artifacts/tech-news/2026-07-31/writer/02/draft-handoff.md`: the old and new
item-2 wording, the corrected attribution/figures, and the proof result.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/tech-news/2026-07-31/writer/02/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work only. Do not tour the repo/archive.
