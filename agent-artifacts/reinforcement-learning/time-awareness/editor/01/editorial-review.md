# Editorial review: reinforcement-learning/time-awareness (editor/01)

## Correct

Thesis, from the draft alone: when a time limit belongs to the task, the moves
left are part of the state, so the agent has to observe them and the last move
is a termination. Four claims carry it.

1. On the four-move task, cell 5's best move is left with one or two moves left
   and up with three or four, and cell 10 mirrors it. Held. I extracted both
   listings from the page, ran them with the printed files of the earlier lessons
   (each identical to the library copy), and got the printed output byte for
   byte. I checked the hand calculation (up: 0.8 to cell 1, 0.1 to cell 4, 0.1
   to the pit at 6, so −2.9; left slips only to 1 or 9, so −1.0) against
   gridworld.py. Value iteration's fourth sweep at cell 13 is −3.439 in
   finding-optimal-policies' printed trace, so the page's −3.44 links back to
   that lesson correctly. figures.py regenerates both SVGs identical to the
   page. A full print of the best-move sets agrees with every arrow and every
   "any" in Fig. 1, and the anti-diagonal symmetry claim holds.
2. A pair with no moves left is terminal, and Gymnasium's own wrappers still
   call the fourth move truncated. Held. Pardo et al. Eq. (4) stops "at all
   terminations" (p. 4047). The 1.4.0 tutorial counts "a time-limit inherent to
   the environment" as termination. stateful_observation.py's `__init__` raises
   the quoted ValueError without an inner TimeLimit, and its `step` returns
   `super().step`. checks1.py reproduces the Box space, the elapsed count and
   the ValueError.
3. With the pair observed, Q-learning reaches the optimal 0.66 in every run.
   With the cell alone it earns 0.20 to 0.35 and is wrong at cell 5, cell 10 or
   both. Held. Unrounded, all five time-aware runs score 0.6641, the optimum,
   and none of them makes a suboptimal greedy move at any (cell, moves left)
   pair. I reran the handoff's seeds.py on unused seeds 5 to 9: time-aware 0.66
   in every run, cell-only 0.20 to 0.38, and every cell-only run takes the
   one-or-two-moves-left move at cell 5, cell 10 or both, losing 2.40 to 2.52
   from that start. checks3.py: forcing up at 5 and right at 10 leaves a loss
   of 0.131 in all ten seeds. p2.py backs Problem 2: a zero start matches
   terminated, and a start of 5 drops the return to −0.03.
4. The cell-only runs learn, entry for entry, the table termination-and-
   truncation's mistaken loop learned. Held. The listing prints True. As an
   independent check, the mean over runs of each cell's largest cell-only
   estimate reproduces that lesson's "cut treated as terminal" grid to two
   decimals in all 16 cells. The settings match too (ε 0.5, 100,000 episodes,
   seeds 0 to 4).

Breaks and fixes, none of which changes a claim:

- The Hopper locator gave pp. 4049–4050. The photo-finish behaviour is in
  Section 2.4 on p. 4048, the fall on p. 4049 and Fig. 5 on p. 4050. I
  corrected the locator.
- The Go deeper row said Harada's risky move "pays only at the last moment".
  Harada says it is optimal to make it only then (p. 578). I reworded the row
  to match.
- The Go deeper row gave Section 2 as pp. 4047–4048. It runs to p. 4049, so I
  corrected the range.
- "Are close enough that four of the five runs choose left" claimed a cause the
  numbers do not show, because closeness does not produce a 4–1 split. On
  seeds 5 to 9 the split is 3–2. I rewrote the sentence to state the split and
  why either choice loses.
- "The next section puts up at −0.86" pointed at a section that never prints
  those values. They come from backward induction and are printed in the run
  output. I reworded the pointer.

Citations. I opened every printed href. PMLR (s1), the PDF, the four Farama
pages (s3, s5, s6, s7, with every anchor present), the AAAI scan (s8) and the
sb3-contrib page all return the source. PyPI (s4) serves a JavaScript client
challenge to scripted clients. PyPI's JSON API confirms 1.4.0, uploaded
2026-10-05, as the latest release. The MIT Press page (s2) returns 403 to curl
and to WebFetch, and so does the site root, so this is a block on scripted
clients and not a dead page. I could not confirm it from here. The ISBN is the
second edition's, termination-and-truncation prints the same href, and the
proof's link check passes it. All eight `data-nb-kind="primary"` labels hold
under the researcher's test. Each source is the authors' or maintainers' own
document for what it is cited for. s3 is cited only for Gymnasium's own flag
definition, which is the use the record calls primary. The page treats none of
the four Farama pages as independent of another.

## Reads well

What went:

- "But here the environment's own rule creates the missing part" came from the
  commission's boundary line ("a hidden variable the environment's own rule
  creates"). The point is the article's own, so I rewrote it in the article's
  terms: the missing part is the count of moves, which exists only because the
  task has a four-move rule.
- "The start of the recursion, v_0 = 0, also decides the flags" has an equation
  deciding something. I folded the fact into the next sentence: the pair's
  value is v_0 = 0, like the goal and the pit.
- "The Markov property asks the state to carry..." has a property asking. It
  now reads "A state with the Markov property carries...".
- "Cells 2 and 7 check that account" followed the random-ending paragraph, but
  the check tests where the losses fall. I made it one sentence inside the
  results paragraph and deleted the standalone paragraph.
- "A time-unaware agent" relied on a term the body no longer defines after the
  cut below. It now reads "an agent that can't see the time left".

No sentence failed the placeholder test outright. I found no clause borrowed
from the Olah, Karpathy or Weng passages. Against the recent record, the
headline does not lead with an agent plus a number, "settle" and "the
course's grid" are absent, the dek is one sentence with no comma-and join,
the body opens on a rule change and not on "Start the agent in cell N", and
no heading opens with "The" or uses the "averages over" form.

What I lifted: the Fig. 2 paragraph now ends on why no single entry can be
right ("Either move is wrong for two of the four numbers of moves left"). The
takeaway's last sentence now separates this lesson's fix from the earlier one:
the target was right and the observation lacked the moves left. The register
is already close to the guide's: short sentences, the purpose of each step
before the step.

## The experience

I built the page with `nb preview` and read it at 390 px in the light theme.
The equations render, and Fig. 1 and Fig. 2 are legible at phone width. Both
figures are byte-identical to the versions the writer checked in both themes
at 390 px and 900 px, and both match the printed output. Fig. 1 had one
unexplained mark, the two-way tie at cell 9 with four moves left, so the
caption now says two arrows mark two best moves.

The page gained focus in the backward-induction section. I cut the paragraph
that restated Pardo et al.'s v_π(s, T − t) notation and re-named the term
time-aware. Its symbols never return, the card already names the term, and the
section now ends on the frame-stacking contrast. The takeaway is down to about
100 words.

Prose, counted on the rendered page per the lesson identity (cards, captions,
equation legends, problems and answers, headings; no code, output, math, SVG
text, bands or sources): 2,139 words with the headline and dek, 2,103
without. The draft had 2,157. `nb stamp` now reads 3,892 words, 17 minutes.

What it gives beyond its sources: on a grid the reader already knows, it
computes the time-indexed values exactly. It shows a cell whose best move flips
at three moves left. It then shows that a correctly flagged cell-only learner
reproduces, entry for entry, an earlier lesson's mistaken table, so the same
wrong numbers need the observation fixed, not the target. That matches the
handoff's original-work sentence. The headline's claim, that cell 5's best move
with one move left points away from the goal, is what the hand calculation
shows.

## Edits

- Why this matters: Hopper locator changed to "Section 2.4, p. 4048; end of Section 2, p. 4049; Fig. 5, p. 4050".
- Why this matters: "The Markov property asks the state to carry" became "A state with the Markov property carries".
- Orientation: "and the next section puts up at" became "Backward induction, the method of the next section, puts up at".
- Fig. 1 caption: added "and two arrows mark two".
- Backward induction: replaced the commission-worded clause with "Here the missing part is the count of moves, which exists only because the task has a four-move rule."
- Backward induction: cut the paragraph on Pardo et al.'s v_π(s, T − t) notation and the term time-aware, removing two s1 cites (Eq. (3), Section 1).
- Terminal pairs: merged "The start of the recursion ... decides the flags" into "so its value is v_0 = 0 in every cell".
- s6 locator: "step, which returns ObservationWrapper.step unchanged".
- Runs: added "Cells 2 and 7, whose best move into the goal is the same with any number of moves left, lose nothing in any run." to the results paragraph and deleted the standalone cells 2 and 7 paragraph.
- Runs, Fig. 2 paragraph: replaced the causal "close enough that" sentence with the split and "Either move is wrong for two of the four numbers of moves left."
- Runs: "a time-unaware agent" became "an agent that can't see the time left".
- Takeaway: dropped "starting from v_0 = 0" and "and the target stops there", and rewrote the last two sentences.
- Go deeper, Pardo: Section 2 page range changed to pp. 4047–4049.
- Go deeper, Harada: "pays only at the last moment" became "is worth making only at the last moment".
- Ran `nb stamp` (words 3,929 to 3,892). Code, printed output and both SVGs are unchanged.

Reruns: four_moves.py and moves_left.py as printed (byte-identical output),
figures.py (identical SVGs), and from the handoff's checks seeds.py 5 10 0.5,
checks1.py, checks3.py and p2.py. All agree with the page.

Open for the orchestrator: the MIT Press href (s2) could not be opened from
this session. Please confirm it in a browser. If it fails, the authors' book
page is the fallback, but its https address failed TLS here, and the proof
requires https.

## Decision

approve. Every claim held on rerun and on new seeds, and the edits correct
locators, wording and one unsupported causal sentence without touching the
argument.
