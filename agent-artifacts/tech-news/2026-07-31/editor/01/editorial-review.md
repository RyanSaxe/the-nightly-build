# Editorial review — tech-news/2026-07-31 (editor 01)

## Decision
REQUEST writer. One blocking factual/sourcing error in item 2 (Gemini
Robotics 2). Everything else clears. Proof stands at BLOCK: 0 / WARN: 0 /
PUBLISHABLE, but the failure is a false attribution the proof cannot see, so
publication waits on the fix.

## Skeptic
Thesis: for each of four 30–31 July developments, lead with the independently
verified number and carry the caveat the vendor's own framing dropped. Tested
the four item theses plus the night's title/dek and all four subheads as
claims; reopened the evidence record and, for the one load-bearing point,
DeepMind's primary post directly. Broke: item 2's sentence "DeepMind traces
the split to hardware: Apollo 2's five-fingered, 22-joint hand draws the low
multi-finger scores, while simpler two-fingered grippers on other platforms
cluster at 68% to 90%." Three faults stacked in it:

- **False attribution.** DeepMind's post makes no causal claim; it says only
  that "multi-finger dexterous manipulation remains challenging." The
  hardware-causes-the-split framing and the cross-platform cluster comparison
  are TheNextWeb's (s5), which the evidence record files under the secondary,
  not the primary. The sentence puts the secondary's inference in DeepMind's
  mouth and cites it to s4 — the writer's guess wearing the primary's
  attribution, which the floor bans, and a miscitation (should be s5).
- **Wrong number.** The two-fingered gripper (Franka/Robotiq) cluster is
  74–90% per both the DeepMind table and TheNextWeb. The article's "68%" pulls
  in Apollo 2's 68.4% table-pick, which used Inspire multi-finger hands, not a
  two-fingered gripper — the exact hand class the same sentence blames for the
  low scores.
- **Spec imprecision.** DeepMind's post says "five-fingered, 22
  degree-of-freedom SharpaWave hand"; the article renders it "22-joint."

The rest held. Every figure I spot-checked matches the record: item 1 CVSS
10.0 / <3.16.3 / 233 tools / autopilot-only blocklist (GHSA + Noma); item 2's
92/36/32/40/89.6/76.3 success rates; item 3's €10bn/€20bn/€30bn, seven sites,
12 Nov deadline, €1bn-actually-committed breakdown, non-EU chip MoUs; item 4's
2×10⁻⁴ / 3×10⁻³ / 9×10⁻⁴, 54 dots → 18 EO qubits, ≤3.5 W at 4 K, distance-5
code, QuTech simultaneity and the 100+/thousands scale gap. The
verified-number-before-vendor-framing move holds in all four; every flagged
caveat is carried (multi-finger range, EU funding gap + non-EU silicon, patch
does not undo compromise + vendor-adjacent scale, HRL not sole entrant +
trailing on scale). The unread "100,000 chips per site" figure is correctly
omitted. Item 1's reclassification holds and is honest: GHSA is the sole
`data-nb-kind="primary"`, Noma and The Hacker News are secondaries, Noma is
still cited by name where its "233 tools" and scale figures originate, and The
Hacker News (with maintainer Reuven Cohen on record) is a genuine independent
secondary, so the secondary label hides no missing independent source. All
four items are exactly 1 primary + ≥1 independent secondary with honest kinds.

## Cut
0 cuts made. I did not cut the broken item-2 sentence because the reasoning it
carries (a complex multi-finger hand explains the low scores) is real and
evidence-supported via TheNextWeb; cutting would lose genuine reader value the
sources support. The honest repair is re-attribution plus two number fixes,
which is beyond a clause and belongs to the writer. Worst surviving tell: item
1's "The flaw itself is not in dispute:" — a mild framing pivot, but it earns
its place by separating the contested scale numbers from the undisputed
advisory facts, so it stays. No prompt leakage, no "why it matters"
scaffolding, no closer hands the point back, no manufactured punchline, no
hedged-contrast dek. Punctuation is clean (commas and periods; colons used to
introduce, not to connect). Subhead shapes vary acceptably.

## Reader
This gives me, per item, the vendor or institution's claim held apart from what
an independent party confirmed, plus the one caveat the headline dropped —
juxtapositions no single cited source pre-assembles, which matches the
draft-handoff's stated original work and survives the read. The prose sits
closer to the voice-guide exemplars (number built into the sentence, skepticism
carried by a second figure rather than an adjective) than a median AI summary.
The single exception is the item-2 sentence above, which breaks the piece's own
original-work premise by blending the two voices it is supposed to keep apart —
one more reason it must be fixed rather than shipped. Reread as the largest
claim, the title/dek commit to what the lead item defends; the title's "any
unpatched Ruflo AI agent" leans slightly past the advisory's "default
docker-compose deployment" scope, but the dek's "traces the hole to Ruflo's own
Docker defaults" restores the qualifier, so it stays.

## Direct edits made
None. No cut or ≤-clause fix resolves the item-2 fault without reconstructing
prose, and the rest is clean.

## Required work by owner
- **writer** — Item 2: fix "DeepMind traces the split to hardware…". DeepMind
  makes no such causal claim, so re-attribute the hardware-split framing and the
  gripper-cluster comparison to TheNextWeb and cite s5; correct "68% to 90%" to
  the sourced 74–90% two-fingered-gripper range; change "22-joint" to the
  primary's "22 degree-of-freedom." Or cut the sentence. Re-run the proof to
  BLOCK: 0 after the change.

No researcher work: the evidence record already carries the correct
attribution (the causal split framing under TheNextWeb) and all needed figures.

## Proof
`./nb check … --series tech-news --library /home/user/library` → BLOCK: 0,
WARN: 0, PUBLISHABLE (unchanged; I made no edits). The blocking issue is a
factual attribution the proof does not detect.
