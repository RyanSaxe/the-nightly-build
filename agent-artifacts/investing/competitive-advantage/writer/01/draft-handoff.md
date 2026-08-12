# Draft handoff: investing/competitive-advantage (01)

## Original work

The article turns the evidence's scattered figures and quotations into a single
priced variable: it runs Copart and Crocs through one economic-profit model with
return and growth held equal by construction, so the advantage period alone
moves the modeled value from $690 to about $2,130, and then names that same
buried variable inside the DCF terminal value the course already taught. The
evidence supplies the levels, the fade record, and the taxonomy separately; the
article is where the fade rate, not the headline return, becomes the thing the
reader learns to price.

## Final proof

Command run (links included):

    ./nb check .nb-work/investing/competitive-advantage/library/investing/competitive-advantage.html --series investing --library /home/user/library-checkout

Result: `BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE. Stamped words 2194 (band
1200-2200), reading 10 min, sources 8 (all primary). No warning left standing.

Preview built cleanly with the draft merged (`nb preview`); the annotated
equation, both tables, and the Buffett note render into the built article.

## Warnings intentionally left

None. Earlier iterations carried W-LENGTH-HIGH and three W-SENTENCE-DENSITY
warnings; all were resolved by trimming to band and splitting the long
sentences (including the Copart verbatim-quote sentence's framing and the
Porter barriers-to-entry list).

## Notes for the editor

- The worked "same ROIC, same growth, different fade" comparison is stated
  in-text as a deliberate construction, not a claim the two firms are identical:
  Copart earns roughly 30% and Crocs roughly 27% (FY2024, pre-write-down) in
  different industries, so the piece holds both at an illustrative 30% return,
  6% growth, and $1,000 of capital and varies only the advantage period. The
  $1,000 and 6% are labeled illustrative; the return levels cite the filings.
- Mauboussin's Exhibit 34 numbers are presented as CFROI (named as a cash-based
  cousin of the accounting return the course has used), not relabeled ROIC, per
  the evidence record's contradiction note.
- Mean reversion is framed as a wide-variance tendency, not a schedule
  ("Gravity is not a timetable"), and the moat-identification humility (Dexter
  Shoe; Crocs looking like a fortress at its 2007 peak) is carried explicitly.
- The two prior lessons (value-of-growth, discounted-cash-flow) are linked in
  the Background band and their results paraphrased as course continuity, not
  added to the numbered source list. This follows the library convention
  (sibling lessons appear in Background; numbered sources are the eight external
  primaries). If the editor prefers the terminal-value recap to carry an inline
  cite, the DCF lesson would need to be admitted as a source, which the
  data-nb-source HTTPS rule does not accommodate for a repo-relative link.

## Open questions

None blocking. The evidence record fully supported the round's focus; no
researcher request is needed.
