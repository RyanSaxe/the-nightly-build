# Editorial review — tech-news/2026-07-31 (editor 02, confirm item-2 fix)

## Decision
DONE. The one blocking fault I named in round 01 — item 2's false attribution
plus two wrong figures — is fully resolved with no new problem and no regression
to items 1, 3, 4. Proof is BLOCK: 0 / WARN: 0 / PUBLISHABLE. Approve.

## Scope of this read
Round 01 cleared items 1, 3, 4 and required a single change. This is a targeted
confirm of that change against the evidence record and my own round-01 read, not
a fresh full review of the cleared items. I re-checked the three focus questions
in the brief and spot-checked the cleared items for regression.

## Skeptic
The round-01 break was item 2's sentence "DeepMind traces the split to hardware:
… clusters at 68% to 90%," cited to s4 — three stacked faults: a causal claim put
in DeepMind's mouth (the framing is TheNextWeb's), a miscite (s4 should be s5),
a wrong low bound (68% folded in Apollo 2's 68.4% Inspire multi-finger pick, the
exact hand class the sentence blames), and "22-joint" for the primary's "22
degree-of-freedom." I re-broke the rewritten passage on all three axes:

- **Attribution now honest.** The causal hardware-split framing and the
  gripper-cluster comparison sit in a sentence opening "TheNextWeb, reviewing the
  same release independently, traces the split to hardware…," cited to s5
  (secondary). DeepMind's s4 sentences now carry only what DeepMind's post
  actually says: the task-split success numbers, the three-model breakdown, the
  verbatim "multi-finger dexterous manipulation remains challenging" hedge
  (matches evidence, primary read), and the access terms. No causal claim
  survives under s4. The two voices are distinct — the primary reports numbers
  and its own hedge; the secondary supplies the inference. The blended-voice
  fault is gone, which also restores the item's original-work premise.
- **Figures corrected.** "74% to 90%" matches the evidence Numbers table's
  two-fingered-gripper (Franka Duo / Robotiq) cluster — 74.2%, 78.9%, 89.6% —
  rounded to whole percents. Apollo 2's 68.4% Inspire-hand table-pick is now
  correctly excluded; it is a multi-finger result, not the two-fingered-gripper
  class the sentence contrasts. The low bound no longer contradicts the sentence
  it lives in.
- **Spec corrected.** "22-joint" is now "22 degree-of-freedom," the primary's own
  phrasing, exactly as round 01 required — and correct even though the sentence
  is attributed to s5 (TheNextWeb renders it "22-joint"; the article uses the
  more accurate primary term for a true, primary-owned spec inside a paraphrase
  of TheNextWeb's argument, which is what round 01 prescribed, not a new fault).

No regression in the cleared items. Item 1: CVSS 10.0, < 3.16.3 / patched 3.16.3,
233 tools, autopilot-only blocklist, rotate-keys/audit-AgentDB remediation,
Reuven Cohen on record; kinds hold (GHSA primary, Noma + Hacker News
secondaries). Item 3: €10bn/€20bn/€30bn, up to seven sites, 12 Nov 2026 deadline,
early-2027 award, ~€1bn-committed breakdown, Nvidia/AMD/Qualcomm MoUs. Item 4:
4 K, ≤3.5 W, 18-qubit / 54-dot array, distance-5 code, 2×10⁻⁴ / 3×10⁻³ / 9×10⁻⁴,
"order of magnitude," QuTech simultaneous 5-qubit result, 100+/thousands scale
gap. All display text (title, dek, four subheads) unchanged from the round-01
state I cleared. Tested: the three focus claims plus regression spot-checks on
items 1/3/4 — broke: none.

## Cut
0 cuts. The writer split the merged passage into two sentences (hardware-split
framing / pacing quote) to clear a density warning, wording otherwise unchanged;
the split is clean and I leave it. No new prompt leakage, self-grading, or
revelation frame entered with the rewrite. Punctuation clean (the colon after
"traces the split to hardware" introduces the explanation, it does not connect).
Worst tell remains item 1's mild "The flaw itself is not in dispute:" pivot,
which still earns its place separating contested scale figures from undisputed
advisory facts. N = 0; nothing new to trim.

## Reader
Per item I still get the vendor or institution's own claim held apart from what
an independent party confirmed, plus the caveat the headline dropped. The item-2
repair strengthens this: the reader now gets DeepMind's numbers and hedge in one
voice and TheNextWeb's hardware explanation in another, no longer conflated — the
juxtaposition the draft-handoff claims as original work, now actually delivered
rather than faked by borrowing the secondary's analysis under the primary's cite.
The prose sits closer to the voice-guide exemplars than a median AI summary.
Reread as the largest claim, the title/dek still commit to the lead security item
and hold.

## Direct edits made
None. The writer's fix resolved the fault; no cut or ≤-clause repair remained.

## Required work by owner
None. No researcher work (the evidence record already carried the correct
attribution and figures, as noted in round 01). No further writer work.

## Proof
`./nb check .nb-work/tech-news/2026-07-31/library/tech-news/2026-07-31.html
--series tech-news --library /home/user/library` → BLOCK: 0, WARN: 0,
PUBLISHABLE.
