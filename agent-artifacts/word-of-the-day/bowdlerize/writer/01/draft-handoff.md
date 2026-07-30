# Draft handoff — word-of-the-day/bowdlerize (writer invocation 01)

Production: single-context, no isolation.

## Original work
The article isolates one precise sense of *bowdlerize* the dictionaries leave
implicit and the eponym's own story dramatizes: the edit that alters a text while
continuing to present it as the author's own work. It then uses that sense as a test,
setting the word against abridge, censor, and redact by a single property (whether the
change is visible to the reader), and grounds the whole distinction in a documented
modern case (Puffin's 2023 Roald Dahl editions, still sold under Dahl's name). The
sources define, date, and narrate; the article turns them into a usable line the reader
can apply.

## Paths changed
- `library/word-of-the-day/bowdlerize.html` (authored from skeleton).
- No assets. No charts.

## Proof
- Command: `./nb check .nb-work/word-of-the-day/bowdlerize/library/word-of-the-day/bowdlerize.html --series word-of-the-day --repo . --library ../library`
- Result: `BLOCK: 0  WARN: 0  verdict: PUBLISHABLE`.
- Measured by the engine: word_count 620 (band 550–800), sources 6 (min 4). nb-meta
  updated to these measured values; reading_minutes 3.
- No warnings left standing.

## Source kinds carried
S-MW primary (s1), S-FOL secondary (s2), S-FS/Wikipedia secondary (s3), S-ETY primary
(s4), S-DB secondary (s5), S-CJ secondary (s6). Numbered in first-citation order.

## Decisions and open questions
- **OED not cited.** The commission named the OED, but its online entry returned 403
  to every fetcher and could not be read; per "cite only what you have read," it is
  omitted. Merriam-Webster (s1) and the Online Etymology Dictionary (s4) carry
  definition and etymology instead. Flagged for the editor.
- **Disputed first-use year** (MW 1826 vs etymonline 1836) handled in prose as "within
  a decade of Thomas's death in 1825," which both readings satisfy; no single year
  asserted.
- **1807 location**: the scholarly body reading (Bath first edition, later London
  re-release) is used; the article does not repeat Wikipedia's conflicting infobox
  publisher.
- **Furniture**: the `rs-word-card` is the opening furniture. No table was added for the
  abridge/censor/redact distinction because I lack cited dictionary definitions for
  censor and redact; forcing a table would have put uncited cells on the page. The
  distinction is carried in cited prose instead. Editor may reassess.
- No remaining evidence or voice questions.
