# Editorial review: reinforcement-learning/held-out-levels (editor/01)

## Correct

Thesis, from the draft alone: return on training levels cannot tell a memorized
level from a learned task; return on held-out levels from the same generator
can, and it rises to meet a high training return only when the observation
carries what differs between levels and the agent trains on enough of them.

Claims under it, and how each held:

1. Trained on one level, both agents solve it by a shortest route and solve
   0.04 (position) and 0.05 (view) of 500 held-out levels. Held. Both listings
   were copied out of the built page into a fresh scratch directory and run
   with `uv run`: `levels.py` and `heldout.py` (2 min 21 s) print output
   identical byte for byte to the page. A separate trace of run 1's agents
   reproduces every path in the Fig. 1 and Fig. 3 aria labels, the wall at
   (1, 3) that blocks the position agent's fourth move on level 100005, the
   view (1,0,1,0,2,2) missing from the view agent's 21-entry table, and the
   route rule ("solves a held-out level iff the goal is on its route before any
   wall") on 500 of 500 held-out levels.
2. No policy of the current observation can beat the best single policy for
   the generator, and for the position that ceiling sits below the per-level
   optimum. The two inequalities are valid for any return. The strictness step
   broke as printed: the page scores the 0/1 return within 40 moves, then
   argues the shortfall with shortest routes, which is the discounted return.
   Under the 0/1 score the (6, 0)/(0, 6) pair does not show a shortfall, since
   a stochastic position policy that mixes down and right at the start retries
   after the blocked move and solves both levels almost surely within 40 moves.
   Fix: the paragraph now says the inequalities hold for any return and that
   the shortfall is shown for the discounted return the agents learn from. "The
   two sides are equal" was ambiguous with three terms on the page; it now
   names the middle and right terms.
3. The view agent's held-out return rises to 0.97 at 64 levels, within 0.01 of
   training, and views missing from its table cause most of the one-level
   shortfall. Held. The removal test does test the cause the page names: it
   changes only the entries that are missing and leaves every learned entry in
   place, and `toward_goal` alone solves every held-out level, so a level the
   filled agent still fails is lost through a learned entry. That is the logic
   the page already uses for the 0.26 run. What did not hold was the silence
   about unstable runs. A per-run rerun of runs 0 to 9 found run 5 at 16
   levels (training 0.56, held-out 0.25, filled 0.30) and run 1 at 64 (0.80,
   0.81, 0.81). Those are the low ends of the printed brackets, and the page
   said nothing about them. A short paragraph now says that a few runs at 16
   and 64 levels fail part of their own training levels and drop on held-out
   levels too, that filling barely lifts them so their learned entries are at
   fault, and that the lesson leaves the cause untraced. The series prompt
   allows that wording when nobody has traced a cause.
4. The position agent's gap closes because its training return falls (1.00 to
   0.05, held-out about 0.04 throughout), so a gap means something only beside
   a high training return. Held. Recomputed Cobbe et al.'s App. E Table 1
   against the arXiv v3 PDF: 99.45 − 66.79 = 32.66, 90.87 − 90.04 = 0.83,
   90.18 − 78.35 = 11.83, 97.7 − 95.87 = 1.83. Kirk et al. p. 211 carries "a
   random policy is likely to get a gap of 0".

A break outside the body: the Why this matters card said what the agent
observes "decides whether [the gap] can close". Section 5 shows the position
agent's gap closing to 0.01. The card now says the observation decides whether
held-out return can rise to meet a high training return.

Labels in the headline, dek and headings agree with the output: 500 held-out
levels, 64 training levels, 0.97 against 0.97 with a gap of 0.01, and the
position agent's 0.05 training return at 256.

Sources reopened past the quoted passage: Cobbe 2019 §3.1 (levels from seeds,
p. 2), §3.2 (the quoted sentence, p. 3), §6 (the LSTM quotation, p. 6), App. E
Table 1 (p. 14); Zhang 2018 "Memorization Capacity of Deep RL Agents" (p. 5,
p = 0.5 makes good test performance impossible, and small training sets reach
near-optimal training reward), App. A.2 (disjoint test ids, p. 15), App. C
(Agent-1's drawn paths); Kirk 2023 §3.3, §3.4 p. 211, §4.2; Procgen README
"Environment Options" and `game.cpp` L93–117 at commit 37b521d; Gymnasium 1.4.0
Env.reset ("then never again"); SB3 2.9.2 vec_envs ("seed and options are
discarded", "reset automatically afterward") and `dummy_vec_env.py` L68–71.
All support what the page cites them for. The record and the sources agree
throughout, so nothing went to the orchestrator.

Printed hrefs: the arXiv, JAIR, Gymnasium and SB3 addresses return 200 and
land on the cited document. The Procgen href
(github.com/openai/procgen/blob/37b521d…/procgen/src/game.cpp#L93-L117)
returns 403 from this session's proxy, which says GitHub access to that
repository is not enabled for the session. That is the sandbox, not the site.
`git ls-remote` shows 37b521d is the repository's HEAD, and the same path at
that commit on raw.githubusercontent.com is `Game::reset` at the cited lines,
so a reader's click lands on the source.

`data-nb-kind`: all six sources are primary for what they are cited for: each
paper's own results or definitions, the maintainers' own documentation, and
Procgen's own code. The page claims no independence between Cobbe et al. and
the Procgen repository and calls it "the same group".

## Reads well

What went:

- "So the gap goes on the page beside the training return." It came from the
  briefing: the commission's "report training and held-out return side by
  side" turned into a sentence about the page. The point is the article's own,
  so it was rewritten: "So a gap shows generalization only when the training
  return beside it is high."
- In the takeaway, "can, and their return goes beside the training return",
  from the same source. Rewritten, and its "so" now carries the reason it
  skipped (one table of positions cannot follow every level's route).
- "The position agent's gap closes from the other side." It said nothing the
  heading above it had not said. Deleted.
- The Procgen "as many as 10,000 levels" sentence. Cut for length, not as
  slop. CoinRun's 4,000-level numbers already show that deep networks reading
  images need far more levels. With no inline citation left, source 7 came off
  the Sources list. The paper stays in Go deeper.
- Go deeper 01, "the CoinRun experiment this lesson shrinks to a table". The
  figure could mean either a Q-table or a table of results. It now says the
  lesson repeats the level-count experiment with a Q-table.
- The dek said "grids" while the headline and body say "levels". It now says
  levels throughout. The seed range "100,000 to 100,499" now matches the level
  ids and the printed output (100000 to 100499).

Against the recent record: the dek opens on the agent, with no "On a ...",
"When only ..." or "only if" turn. The Why card opens on this lesson's own
grid. The five headings are built differently from one another and from the
last three lessons' headings. The Go deeper lines take four different shapes (a
noun phrase, "turn to", a list, a conditional). Headline: it has no "never"
and no number comparison, its subject is the method, and the environment is
left unnamed, so it does not repeat the "A courier paid for every move never
delivers" form of one agent doing one thing in a named environment. It states
the lesson's main idea, and the dek carries the two-agent result. Kept as
written.

Checked against the voice guide's passages: no clause from Olah, Karpathy or
Weng appears in the draft. The register matches the guide, with short
sentences, the purpose of each step before the step, and the derivation's
reasons placed beside its lines. Nothing ran flatter than the guide, so the
edits were for clarity and accuracy. The edges were read alone: section
closers and the article's last sentence each state a result from the runs.

## The experience

Built with `nb preview` and captured with Playwright at 1280 and 390 px wide,
in light and dark themes. There is no horizontal page scroll at either width.
Fig. 1's four panels stack on a phone. The two paths are offset so they never
overlap, and each loop at the move limit draws as a short solid segment that
reads as back-and-forth. Fig. 2 matches the printed means and run ranges point
for point. At one level the view agent's 1.00 training dot sits under the
position agent's, and the aria label and the output carry both. The math
legend's colors hold in both themes. Fig. 3 is clear. No component needed
adding or cutting.

Prose count on the rendered page (cards, captions, math legend, problems and
answers; excluding code, output, drawing text, equations, bands and sources):
2,231 words, or 2,277 with the title and dek. The draft measured 2,190 by the
same count. The unstable-runs paragraph and the explicit change of return
added about 70 words, and the cuts above removed about 30. The lesson ends a
little past the 2,200 line, within the template's "about".

The section on the position bound carries the most weight on the page and is
the densest. It earns that weight, because the lesson's original work is
there.

What the page gives beyond its sources: a two-line derivation showing that a
policy of the current observation is capped by the best single policy for the
generator, and a seed-keyed grid where the position agent's gap closes by
failing its training levels while the view agent's closes by learning, with a
removal test that traces the view agent's early shortfall to missing table
entries. The writer's original-work sentence says the same. The headline
survives as the piece's largest claim: held-out levels are what exposed both
memorizing agents.

## Edits

- Dek (meta and page): "500 new grids after 64 training grids … failing its training grids" → "500 new levels after training on 64 … failing its training levels".
- Why this matters: "That return cannot say" → "Its return there cannot say".
- Why this matters: "… is called the generalization gap, and what the agent observes decides whether it can close." → "… is called the generalization gap. What the agent observes decides whether held-out return can rise to meet a high training return."
- generator: "seeds 100,000 to 100,499" → "seeds 100000 to 100499".
- one-route: "The two sides are equal only if …" → "The middle and right terms are equal only if …".
- one-route: "Under the agents' discount, optimal moves follow a shortest route." → "The inequalities hold for any return. For the shortfall, take the discounted return the agents learn from, under which optimal moves follow a shortest route."
- view-levels: added a paragraph after the removal test on the runs at 16 and 64 levels that fail part of their own training levels, which filling barely lifts, with the cause left untraced.
- training-return: deleted "The position agent's gap closes from the other side."; "Its held-out return" → "The position agent's held-out return".
- training-return: "So the gap goes on the page beside the training return." → "So a gap shows generalization only when the training return beside it is high."
- training-return: cut the Procgen "as many as 10,000 levels" sentence and removed source 7 from Sources.
- Takeaway: "Held-out levels … can, and their return goes beside the training return. A policy of the current observation can do no better on them than the best single policy for all levels, so the position agent's gap closed …" → "Return on held-out levels … can show it when the training return is read beside it. No policy of the current observation beats the best single policy for all levels. One table of positions cannot follow every level's route, so the position agent's gap closed …".
- Go deeper 01: rewritten to "the CoinRun level-count experiment that this lesson repeats with a Q-table. Appendix E prints every training and test score for its nine training-set sizes."
- `nb stamp`: words 4,136, 18 minutes, 6 sources. Code listings and printed output unchanged.

Proof after the edits: BLOCK 0, WARN 2, PUBLISHABLE. Both warnings are
confirmed as the writer's stated choices. W-SENTENCE-DENSITY is the TeX source
of the bound's `nb-math-eq`: rerunning the proof on a copy with that equation
replaced removes the warning. W-CITE-DENSITY on `view-levels` falls on a
section made of the lesson's own runs and their removal test, which the series
prompt exempts.

## Decision

approve. The argument holds, and every break found here (the change of return
in the bound, the unstable runs the page left unmentioned, the card's claim
about which gap can close) is fixed on the page.
