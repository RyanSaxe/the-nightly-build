# Editorial review — current-events/2026-08-01 (editor/01)

Three ordered reads at high effort on `library/current-events/2026-08-01.html`.
Four items, `brief` template. Government primaries reopened directly (Fed
statement fetched clean; BEA advance-estimate PDF extracted with pdfminer);
every other figure recomputed against the researcher's verified evidence record.

## Skeptic

Thesis: "The day's four most consequential US developments — a hawkish Fed hold,
a DHS rule stripping asylum interviews, a Q2 growth slowdown with split inflation
signals, and a first-of-its-kind parental sentencing — each carrying the number,
caveat, or mechanism the reader's headline dropped."

Tested 12 display/body claims across the four items. Broke three, all fixed:

- **Item 1 (Fed), sentence 3 — unsupported causal link + misattribution.** The
  draft read: the committee's statement "points to inflation kept elevated by
  energy-price shocks tied in part to the Middle East conflict as the reasoning
  three of its own regional presidents cited for wanting rates higher." I reopened
  the FOMC statement (fetched directly, matches the evidence): it makes two
  *separate* claims — inflation "in part reflecting supply shocks... including
  energy," and, distinctly, that elevated *uncertainty* "owes, in part, to the
  conflict in the Middle East." The draft welded energy inflation to the Middle
  East, a causal link the primary does not make. It also attributed a specific
  "cited" reasoning to the three dissenters that the statement never records
  (boilerplate Committee language is not the dissenters' stated rationale), and
  closed on an invented "higher, not lower" contrast (no one sought a cut). An
  unsupported, misattributed, nonessential elaboration. **Cut the whole sentence.**
  The item's "hawkish, not dovish" corrective survives intact in sentences 1–2.

- **Item 3 (GDP), headline — figure that does not check.** Headline claimed the
  print missed forecasts "by half a point." Forecast 2.1% (Fox/LSEG, secondary),
  actual 1.5% (BEA primary, verified from the extracted PDF): 2.1 − 1.5 = 0.6, not
  0.5. **Fixed to "by 0.6 points."**

- **Item 4 (Gray), "27 counts" cited to a source that reports 29.** The 27-count
  figure was cited to [7] AJC, but AJC reports 29 (the evidence flags this
  contradiction and rules 27 reliable via ABC + Fox breakdown + arithmetic
  2+2+18+5=27). A reader checking [7] would find 29. **Moved [7] to back only the
  "first in Georgia" clause (which AJC supports) and left [8] ABC — the source
  that actually reports 27 and "second in the nation" — carrying the count and the
  national-ranking claim.**

Also verified and passed: Fed 9–3 vote, 3.50–3.75% range, three named dissenters
and their Cleveland/Minneapolis/Dallas Reserve-bank titles (not "governors"),
Warsh as chair at eight-and-a-half weeks; DHS 444,724 of 1,434,145 (= 31%),
effective July 28, comment closes Sept 28; GDP 1.5% vs 2.1%, price index 5.7 vs
3.6, PCE 5.1 vs 4.6, core PCE 3.4 vs 4.4 (all confirmed against the extracted BEA
PDF); Gray 15 years vs an 80-year ask, Colt Gray life on 55 counts two days prior,
four dead/seven injured.

**data-nb-kind audit:** s1/s3/s5 primary (Fed statement, Federal Register rule,
BEA release) and s2/s4/s6/s8 secondary (Fox Business ×2, Baltimore Sun/AP, ABC)
all check — each secondary is an outside newsroom, none is the authoring party.
s7 (AJC) is labeled primary; it is a newsroom account, but the researcher's
"primary-by-content" classification is explicit and reasoned (the sentencing
record is not published online; AJC's gavel-to-gavel in-room account is the
closest owner of the court/DA statements), and genuine independent corroboration
exists in s8. The label does not hide a missing independent source, so I accept
it as a disclosed limitation rather than a hidden sourcing failure — noted here,
not blocked.

`Skeptic: thesis "the day's four most consequential US developments, each carrying
the number/caveat/mechanism the headline dropped"; tested 12 claims; broke: Fed
sentence-3 energy↔Middle-East misattribution, GDP headline 0.6≠half, Gray 27-count
cite pointing at the source that says 29 — all fixed.`

## Cut

Ran the delete test sentence by sentence. Direct cuts:

- Item 1 sentence 3 (above): removed entirely.
- Item 2 sentence 3: removed the method-narration opener "Independent reporting
  confirms" — the piece narrating its own sourcing. Recast to report the fact
  directly ("The agency used that same language the day the rule took effect")
  and split its two citations honestly: [4] on the secondary-corroborated
  effective-date language, [3] (the primary rule) on the Sept 28 comment-close,
  which the primary owns and which previously carried only [4].
- Item 2, precision: "average 7.3 years" → "average over 7.3 years" to match the
  primary's "over 7.3 years."

Everything else survived. No stock-revelation frames, no signposts, no
self-grading, no prompt leakage against the writer brief. Headlines are
colon-free with fresh verbs and varied shapes; item order (Fed, DHS, GDP, Courts)
and per-item sentence shapes do not read stamped. Left in place, as legitimate:
item 1's semicolon (split bound to Warsh's own characterization of it) and item 3's
component/analyst semicolon — both join genuinely related independent clauses and
Fox plausibly restates the components, so no forced churn.

`Cut: ~1.1 sentences removed (one full misattributed sentence plus a method-
narration clause); worst tell: the Fed item asserting the dissenters' "cited"
reasoning the primary never records.`

## Reader

Read straight through as the house reader (math/CS, ML-eng, well-read). What the
piece gives beyond the sources: the Fed dissents were *hawkish* under a chair
eight weeks in (not the dovish read a scanner assumes); the DHS rule already binds
up to 445,000 cases two months before the public may comment; Q2's headline
inflation acceleration hides a *cooling* core PCE; and the Georgia sentencing
everyone will file as a national first is, by the judge's own count, the second.
Each is the reason its judgment sentence exists, not a restatement — matching the
writer's original-work claim in draft-handoff.md. Prose sits with the AP/Semafor
exemplars (numbers welded to their nouns, judgment in-clause), not a median AI
summary. Dek names the night's real center of gravity (economic policy) without a
forced through-line or a hedged-contrast mold; headline-level display text now
matches its primaries. Mail-in voting is absent — Opinion owns it, as required.

`Reader: this gives me the hawkish-not-dovish Fed read, the bind-before-comment
DHS gap, the core-PCE-cooling-under-accelerating-headline split, and the
second-not-first sentencing correction — none in the sources' own headlines.`

## Confirmations against the brief

- 4 items, each exactly 1 primary + ≥1 independent secondary; each headline links
  to its primary. ✓
- Mail-in voting executive order not centered (absent). ✓
- Every date/figure re-checked against the primary (Fed + BEA reopened directly).
  ✓
- meta.words updated 577 → 538 (engine `Article.word_count`) after cuts;
  reading_minutes stays 3, byline honest.

## Direct edits made

1. Cut item 1 sentence 3 (unsupported causal link + misattributed dissenter
   reasoning + invented contrast).
2. Item 2: "average 7.3 years" → "average over 7.3 years"; removed "Independent
   reporting confirms"; re-cited effective-date language to [4] and Sept 28
   comment-close to primary [3].
3. Item 3 headline: "half a point" → "0.6 points".
4. Item 4: moved [7] to back "first...in Georgia" only, leaving [8] to carry the
   "second in the nation" and "27 counts" claims (AJC reports 29).
5. nb-meta words 577 → 538.

## Required work by owner

None. No evidence gap or prose redraft remains; all findings were fixable within
editor authority.

## Proof

`nb check library/current-events/2026-08-01.html --series current-events --repo
/home/user/the-nightly-build` → **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**
(re-run after every edit including the word-count update).

## Decision

Approve. No redraft required.
