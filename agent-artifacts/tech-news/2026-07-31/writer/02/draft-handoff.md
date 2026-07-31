# Draft handoff — tech-news/2026-07-31 (writer 02, item-2 fix)

## Original work
This round's act: separating two voices the previous draft had blended into
one — DeepMind's self-disclosed numbers and its own carefully hedged
language ("remains challenging," no causal claim) versus TheNextWeb's
independent inference (that hardware explains the split) — so the article
no longer puts a secondary outlet's analysis in the primary's mouth, while
still giving the reader the causal explanation TheNextWeb actually offers,
correctly attributed and correctly cited.

## What changed
File: `.nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html`
(item 2, Gemini Robotics 2 brief item only; items 1, 3, 4 untouched).

**Old wording (round 01):**
> DeepMind traces the split to hardware: Apollo 2's five-fingered,
> 22-joint hand draws the low multi-finger scores, while simpler
> two-fingered grippers on other platforms cluster at 68% to
> 90%.[4] The company's own post states plainly that "multi-finger
> dexterous manipulation remains challenging."[4] ER 2 is available
> through Google AI Studio and, in private preview, the Gemini
> Enterprise Agent Platform. The VLA and on-device models remain
> limited to early-access partners and trusted testers.[4]
> TheNextWeb, reviewing the same release independently, adds that
> the robots "pause to think through moves a person makes without
> a second thought."[5]

**New wording (round 02):**
> The company's own post states plainly that "multi-finger
> dexterous manipulation remains challenging."[4] ER 2 is available
> through Google AI Studio and, in private preview, the Gemini
> Enterprise Agent Platform. The VLA and on-device models remain
> limited to early-access partners and trusted testers.[4]
> TheNextWeb, reviewing the same release independently, traces the
> split to hardware: Apollo 2's five-fingered, 22 degree-of-freedom
> hand draws the low multi-finger scores, while simpler two-fingered
> grippers on other platforms cluster at 74% to 90%. It adds that
> the robots "pause to think through moves a person makes without a
> second thought."[5]

## Corrections applied (per editor 01 + evidence.md)
1. **Attribution** — the hardware-split framing and the gripper-cluster
   comparison are now attributed to TheNextWeb and cited to s5 (secondary),
   not presented as DeepMind's own causal claim under s4. DeepMind's own
   claim is now limited to its own words: the suite split by task, the
   verbatim "remains challenging" hedge, the three-model breakdown, and
   access terms — all still cited to s4 (primary). The two voices no
   longer share one sentence.
2. **Figure** — "68% to 90%" corrected to "74% to 90%," the two-fingered-
   gripper (Franka/Robotiq) range per the evidence record's Numbers table
   (74.2%, 78.9%, 89.6%). Apollo 2's 68.4% Inspire-hand pick-up-from-table
   score is excluded from this range — it is a multi-finger-hand result,
   not a two-fingered-gripper result, and folding it in was the exact
   error the editor flagged.
3. **Spec language** — "22-joint" changed to the primary's own phrase,
   "22 degree-of-freedom."
4. Split the resulting long sentence in two (hardware-split framing /
   pacing quote) to clear a new sentence-density warning the merge
   introduced; no wording changed beyond the split.

Items 1, 3, and 4 were not opened or touched — the editor cleared them.

## Proof result
```
./nb check .nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html \
  --series tech-news --library /home/user/library
```
`BLOCK: 0 / WARN: 0 / verdict: PUBLISHABLE`

No warnings left outstanding.

## Remaining questions
None. The evidence record already carried the correct attribution and
figures; no new researcher or voice-guide question arose in this round.
