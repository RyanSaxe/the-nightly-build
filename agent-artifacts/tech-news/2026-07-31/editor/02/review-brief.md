# Editor brief — tech-news/2026-07-31 (02, confirm item-2 fix)

## Role
Load and follow `skills/editor/SKILL.md`. You cleared items 1, 3, 4 in round 01
and required one change: item 2 misattributed a causal claim to DeepMind and had
two wrong figures. Confirm the writer's fix resolves it with no new problem, then
approve or route again.

## What changed since 01
Per `writer/02/draft-handoff.md`: item 2's hardware-split framing and
gripper-cluster comparison are now attributed to TheNextWeb (cite s5); DeepMind's
claims are limited to what its post says (s4, no causal claim); "68% to 90%" →
"74% to 90%" (Apollo 2's 68.4% Inspire-hand pick excluded); "22-joint" → "22
degree-of-freedom." Items 1, 3, 4 untouched.

## Begin with these exact inputs
- `agent-artifacts/tech-news/2026-07-31/editor/01/editorial-review.md`
- `agent-artifacts/tech-news/2026-07-31/writer/02/draft-handoff.md`
- `agent-artifacts/tech-news/2026-07-31/researcher/01/evidence.md`
- The article: `library/tech-news/2026-07-31.html`

## Focus this read
1. Is the causal/hardware-split framing now correctly TheNextWeb's (s5), with
   DeepMind's cite (s4) carrying only what DeepMind actually claims? The two
   voices kept distinct?
2. Are the figures now correct (74–90% two-finger-gripper range; 22
   degree-of-freedom), matching the evidence record?
3. No regression to items 1, 3, 4.

## Proof
Confirm clean:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html \
  --series tech-news --library /home/user/library
```

## Output
`agent-artifacts/tech-news/2026-07-31/editor/02/editorial-review.md`

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/tech-news/2026-07-31/editor/02/editorial-review.md`
  (approve, no required change, BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `REQUEST researcher <need>` /
  `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
