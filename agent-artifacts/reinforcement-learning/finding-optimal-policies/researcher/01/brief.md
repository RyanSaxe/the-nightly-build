# researcher brief: reinforcement-learning/finding-optimal-policies (01)

Inputs:
- `../../editorial-direction.md` — the full standing editorial standard.
- `../../commission.md` — what this lesson teaches (the short list of ideas) and the finding it must support.
Output: `evidence.md` (write it beside this brief).

Work from these inputs. Do not tour the repository or the archive. Where
something you need is missing, ask me (the orchestrator).

This lesson is mathematics plus runnable code on a fixed 4×4 grid, so the
research job is not news-gathering but pinning every idea to its source with a
precise anchor and confirming the math is stated correctly. For each item below,
open the source, find the exact passage, and record the section, page or
equation number so a reader lands on the words, not a homepage. Never fabricate
or decorate a citation. If a claim cannot be sourced to a passage you actually
read, say so.

Gather and anchor:

1. **Policy improvement theorem** — its exact statement and the one-step
   argument. Primary: Sutton & Barto, *Reinforcement Learning: An Introduction*,
   2nd ed., section 4.2 (give the printed page range and the theorem/equation
   numbers). Record the precise inequality `v_{π'}(s) ≥ v_π(s)` for all s and the
   greedy construction `π'(s) = argmax_a q_π(s,a)`.
2. **Action value `q_π(s,a)`** — its definition and one-step relation to `v_π`.
   Sutton & Barto ch. 3 (the `q_π` definition) and ch. 4. Give equation numbers.
3. **Policy iteration** — the evaluate/improve loop and why it terminates in
   finitely many steps. Sutton & Barto §4.3. Primary attribution for the
   algorithm's origin: Ronald A. Howard, *Dynamic Programming and Markov
   Processes* (1960) — confirm the book and the chapter where policy iteration
   (the "policy-improvement routine" / value-determination operation) is
   introduced; give a page or chapter anchor and a stable URL if one exists.
4. **Bellman optimality equation** (`v_*` and `q_*`) — exact form with the `max`
   over actions. Sutton & Barto §3.6 (equation numbers). Primary: Richard
   Bellman, *A Markovian Decision Process* (1957, Journal of Mathematics and
   Mechanics) — reuse the source lesson 1 already cited; give the section/page
   where the optimality recurrence appears.
5. **Value iteration** and its convergence as a contraction — Sutton & Barto
   §4.4, plus one analysis reference for the max-norm contraction of the
   optimality operator and the non-expansion of `max` (Bertsekas, *Abstract
   Dynamic Programming* — the source lesson 1 used — or Puterman, *Markov
   Decision Processes*). Give the precise result/section.
6. **A real case for "Why this matters"** that is verifiable and connects to the
   course. Preferred: the reading of expert iteration / AlphaZero's
   self-play-plus-network loop as policy iteration (policy improvement by search,
   policy evaluation by the network). Confirm a citable source that makes this
   connection explicitly — e.g. Silver et al., *Mastering the game of Go without
   human knowledge* (AlphaGo Zero, 2017) or *A general reinforcement learning
   algorithm…* (AlphaZero, 2018), and/or Anthony, Tian, Barber, *Thinking Fast
   and Slow with Deep Learning and Tree Search* (2017), which names policy
   iteration directly. Give the passage. If instead you anchor on Howard's own
   documented application, give that passage. Report what the source actually
   says; do not overstate the equivalence.

Also record, for the writer's convenience (not as citations): the standard
arithmetic facts this lesson will compute on the grid, so the writer can check
the code's output against them where a hand computation is feasible (e.g. a
single action value at a cell from lesson 1's `v_π`).

Keep `evidence.md` organized by the numbered items above. For each: the claim in
one line, the source with a precise anchor, a short verbatim quote where wording
matters (with the URL and retrieval date), and a note on anything disputed or
easy to overstate. Meet `spec/slop.md` in your own prose.
