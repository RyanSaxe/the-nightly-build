# Editorial review: reinforcement-learning/n-step-returns (editor/01)

## Correct

Thesis from the draft alone: an n-step TD target adds n real rewards to the
estimate n moves later, so n = 1 is TD(0) and n past the episode is Monte Carlo,
and on the 19-state walk over the first 10 episodes a middle n beats both ends
when each method gets its own best step size. Claims under it:

1. The n-step return and update (eqs. 7.1, 7.2) and their two endpoints. Held.
   Checked against pp. 143-144 of the 2020 PDF. `checks/pseudocode.py` reran:
   `nstep_td` matches the p. 144 box to 0.0 and equals every-visit constant-step
   Monte Carlo at n = ∞.
2. With fixed estimates, the n-step correction is the first n TD errors. Held.
   I reworked the derivation line by line. The Fig. 1 instance (δ5 = +1, error 1
   when t + n ≥ 6) is right. Monte Carlo's correction is the discounted sum, and
   the page now says "discounted".
3. The target for time t is complete at t + n, and the tail needs n late
   updates. Held. The page said the move completes "τ = t + 1 − n in the code",
   but the code has no t. It now says the move from t to t + 1 completes the
   target for τ = t + 1 − n. "Their targets run past the end" was wrong for the
   first late time, whose target reaches the end exactly, and now reads "reach
   the end". The same fault in the Fig. 1 walkthrough is fixed.
4. n = 4 has the lowest error at its own best step size: 0.26 against 0.34 and
   0.49. Held. All five printed commands, run exactly as printed with `uv run`
   from listings extracted from the page, match the printed output byte for byte
   (about 5 s each, 38 s for the 100-episode run). Every number in the prose and
   both charts matches that output. Fig. 2 and Fig. 3 coordinates are within
   0.13 px of the printed values. Seed offsets 1000, 2000 and 3000 keep n = 4
   lowest (0.257 to 0.259). `integer_n.py` gives n = 3, 4 and 5 within 0.002 of
   each other on both seed sets.
5. The mechanism: short targets carry the outcome back slowly, and noise in long
   targets forces a small step. Held within its scope. Sutton and Barto (p. 145)
   report that intermediate n worked best and give no reason, which matches the
   page. `--expected` removes target noise, and then α = 1 is best for every n
   and the error falls as n grows. I reran it at seed offset 1000 and the result
   is the same. `--size 5` and `--episodes 100 --first 91` both put TD(0) first,
   at offset 0 and at offset 1000. `start_exact.py` supports problem 2's answer:
   TD(0) is lowest at every step size, and each n does best at the smallest one.

Headline. "Four-step" is defensible. The claim compares n = 4 with the two
ends, it holds on four seed sets by margins of 0.08 and 0.22, and it does not
claim four is uniquely best. The body says n = 3 and n = 5 do as well, and the
book's figure also uses n = 4. "A random walk" was not defensible, because the
page's own `--size 5` run is a random walk on which TD(0) beats n = 4. The
headline now names the 19-state walk. This narrows the claim to what the record
supports. It does not cover for thin reporting.

Citations. Every printed href was opened. The RLbook2020 PDF over http returns
200, and pages 164, 165, 166, 167 and 310 open on printed pp. 142, 143, 144,
145 and 288 as the locators say. The Watkins scan returns 200, and PDF p. 93
shows the corrected n-step truncated return and the γⁿK bound on printed p. 86.
online.lisp over http returns 200. It sets start state 9 (zero-based), α =
exp(alog) for alog from −5 to 0, and n doubling to 512, which matches the page.
arXiv 1901.07510 returns 200. Section 4.2 says the 20-step version of each
algorithm did better on initial and overall performance, so the Go deeper row
now says "agents" rather than "an agent". The MIT Press page returns 403 to curl
and to WebFetch, which is a bot wall. Eight published lessons use the same href.
All three `data-nb-kind="primary"` labels hold. s1 and s3 share an author, and
the page never presents them as independent.

incompleteideas.net. All inline `data-nb-url` values and band links were
already http. Setting s3's Sources href to http blocks the proof
(B-SOURCES-FORM: a Sources href must be https). I reported this, and the
orchestrator decided that s3 keeps the https href and that its note names the
http address with no mention of certificates. The note now does that. The https
href still fails TLS from this sandbox, so a reader who clicks the Sources entry
itself may not reach the file. The inline "Open cited passage" link and the
note both give the working address.

## Reads well

Cut:

- "Because the explanation is the lesson's own," as the opening of the
  `--expected` paragraph. It came from the briefing: the commission's research
  decision calls any mechanism "the lesson's own claim". The paragraph now
  opens on what the run tests. The earlier sentence saying Sutton and Barto give
  no reason already sets the test up.
- "Each curve falls to a lowest point and rises again." It describes the shape
  the caption and Fig. 2 already show, and it pushed the result out of the
  paragraph's first sentence.
- "n = 4 sits between." It said nothing. It is replaced by what Fig. 3 shows
  for n = 4.
- "A claim that one n learns fastest compares each n at its own best step
  size." The sentence read as a general rule. It now says what the comparison
  above did.
- The off-policy pointer sentence and its Background row. It ended the delay
  section on a topic that section does not cover, and the main idea does not
  need it. I cut it as a whole idea to bring the count under 2,200, as the
  template asks. The commission allowed the sentence but did not require it.
- The takeaway's scope clause, added in my first pass, came out again for
  length. The scope sentence stays in the body.

Rewritten:

- The Why card's third part ("You can then work an n-step target by hand, write
  …, and explain …") repeated the importance-sampling lesson's "you can work out
  … by hand, prove …, and find …". It now follows a different pattern and names
  this lesson's episode and run.
- The step-size section opened on "The experiment", a referent nobody had
  introduced. It now opens on the question the section answers: which n learns
  fastest.
- "Information" and "the outcome" named one thing. The page now says "the
  outcome" throughout, including the section heading and its id.
- The body opener "The walk has 19 states" leaned on the Why card for "the
  walk". It now reads "This lesson's random walk".
- The output paragraph now gives the reason only states 1 to 4 moved: every
  earlier target read an estimate that was still 0.
- "The same states update at the same times" became "in the same order", which
  is what `expected_td` does.
- The heading "At its own best step size, n = 4 has the lowest error" opened
  the same way as two recent headings ("At ε = 0.5 …", "At cell 13 …"). It now
  leads with the finding.
- The dek dropped "19-state", which the headline now carries, and keeps the
  conditions and the 0.022 step.

The draft held the guide's register: one step per sentence, a hand-worked case
before the general equation, and the purpose stated before each derivation. I
found nothing borrowed from the voice guide's quoted passages.

## The experience

Prose on the rendered page: **2,176 words**. That covers both cards, headings,
captions, legend text, the details summary and note, and the problems with their
answers. It leaves out the headline and dek (49 words), equations, code, printed
output, SVG text, the reading bands and the sources. "n = 4" counts as three
words. I counted with Playwright on the `nb preview` build.

I checked the page at 390 px and 1280 px in light and dark. Nothing overflows
(scrollWidth equals the viewport). The Fig. 1 column divider was drawn at a
slant and is now vertical. Fig. 3's tick labels used a hyphen for minus and now
use "−". No labels overlap and no arrows fall short. Fig. 3's panel text is
small at desktop width but legible.

The page gives more than its sources. It reproduces Figure 7.2 from code a
reader can run, explains the win the book leaves unexplained, removes target
noise to test half of that explanation, and shows the cases where TD(0) wins
instead. This matches the original-work sentence in `draft-handoff.md`.

## Edits

- Headline, `<title>` and nb-meta title: "a random walk" became "a 19-state random walk".
- Dek, in the page and nb-meta: rewritten without "19-state"; "force its step size down to 0.022" became "holds its best step size to 0.022"; "ten" became "10".
- Why card: rewrote the third part.
- Orientation: "The walk has 19 states" became "This lesson's random walk has 19 states".
- Orientation: "three moves run past the end" became "the episode ends within three moves".
- first-n-td-errors: added "discounted" to Monte Carlo's sum of TD errors.
- delay: rewrote the τ sentence without "in the code"; "run past the end" became "reach the end".
- delay: rewrote the nstep.py output paragraph (left end, states 1 to 4, why).
- delay: cut the off-policy pointer sentence.
- Background band: removed the importance-sampling row and renumbered.
- step-size: heading became "n = 4 has the lowest error at its own best step size".
- step-size: rewrote the opening sentence (question, Figure 7.2, Sutton's code) and "where the RMS…" became "which puts the RMS… at".
- step-size: cut "Each curve falls to a lowest point and rises again."
- step-size: rewrote the closing sentence.
- Section id and label: `information-and-noise` became `outcome-and-noise`; heading "moves information slowly" became "carries the outcome back slowly".
- outcome-and-noise: "n = 4 sits between" became a sentence on what Fig. 3 shows; "+1 or −1" became "a return of +1 or −1".
- outcome-and-noise: cut "Because the explanation is the lesson's own"; "same times" became "same order".
- outcome-and-noise: rewrote the last sentence of the `--expected` paragraph and the opener of the scope paragraph to say "the outcome".
- Takeaway: rewrote the TD-error sentence ("its correction is the first n of the TD errors that sum to Monte Carlo's correction").
- Go deeper 02: "where it has an intermediate best value" became "where an intermediate λ does best".
- Go deeper 04: "a DQN-style agent" became "DQN-style agents".
- Source s3 note: replaced the certificate sentence with the http address readers can open. The href stays https, per the orchestrator.
- Fig. 1: made the column divider vertical.
- Fig. 3: changed "-1" tick labels to "−1".
- Ran `nb stamp`.

## Decision

approve. The argument holds, every number reproduces from the printed listings,
and the remaining work is the reader check the template requires.
