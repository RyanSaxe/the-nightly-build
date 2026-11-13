# Draft handoff: feature/cloudflare-quepaxa (writer 01)

## Original work

The article draws the QuePaxa paper's round and hedging delay beside a Raft
election timeout, then sets Raft's stall, the paper's crash-to-progress gap and
Cloudflare's evaluation run side by side as two failure shapes, with each figure
labelled by what it measures and who measured or derived it. Neither source does
this alone. The sentence still holds for the final draft: Figs. 1 and 3 and the
timeout table carry it.

## Proof

`nb check ... --series feature --repo /home/user/the-nightly-build` (links
checked): BLOCK 0, WARN 0, verdict PUBLISHABLE. Stamped at 1,185 words, 5
minutes and 8 sources. The hard ceiling is 1,200 words and every rendered word
counts, including SVG labels, captions, the table and the sources list. Any
words an editor adds have to be cut somewhere else.

I looked at every visual in `nb preview` through Playwright (system Chrome), at
390 px and 1280 px, in the light and dark themes. Nothing overlaps and the page
does not scroll sideways. On a phone the table scrolls inside its own wrapper,
as the runtime intends. Cloudflare's chart (Fig. 2) is a light image and stays
light in the dark theme.

## Where I departed from the commission, and why

- **The 65% was a descent, not a plateau.** The revised angle says the rate
  "held near 65% for the 53 s". The record's chart readings show steps: about
  94%, then 89% until about 15:00:58, then 69%, and about 64% only from about
  15:01:13 to 15:01:25. So the prose says the rate "stepped down to about 65%"
  over the 53 seconds. Fig. 3 draws a descending line, and the dek says
  "bottomed near 65%". The closing line says "at most about a third" of the
  rate, not a third for 53 seconds.
- **The 1/2 bound appears without the "50% chance" clause.** I cut that clause
  for length. The bound is stated as a worst-case floor for the leaderless
  rounds that come after round 1.
- **I did not interpret two things on Cloudflare's chart.** Phase 0 still made
  about 97% of decisions for about 40 s after the failure marker, and the rate
  overshot to about 108% afterwards. The record lists both as unexplained, and I
  cut them for length. The prose does name the gap between the 33% line and the
  measured rate, and lists the evaluation's unknowns.

## Asset capture

`nb asset image` received a 403 from blog.cloudflare.com: Cloudflare blocks
Python's default urllib client. I downloaded the exact file the record names,
`01M73MN2G9VJ180TS373QNGVJJ.png` at 1999x1150, with curl. I then ran it through
`nb asset image file://...` so the helper normalized it as usual. The file is
the same source image, uncropped, because the whole chart is evidence and has no
clutter around it.

## Open questions

1. "A Raft cluster ... commits nothing for roughly an election timeout and then
   runs at full speed." The first half quotes the Raft paper (§5.6). The phrase
   "full speed" is the revised angle's description of the Raft shape, and no
   cited measurement of a recovery rate supports it. Fig. 3 labels the Raft
   panel as a schematic. Tell me whether the editor wants the phrase softened.
2. Fig. 1 draws proposer 3 "seeing progress" and staying idle, which follows
   §5.2 (a later proposer acts only if it has seen no progress). It is a
   schematic, not a trace from either source.
