# researcher brief: reinforcement-learning/environments-and-the-rl-problem (01)

Inputs:
- `../../editorial-direction.md`
- `../../commission.md`
Output: `evidence.md` in this folder (`researcher/01/`)

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

This is lesson 1 of an RL course. The material is standard and settled, so your
job is less to break an angle than to pin every definition and equation to the
canonical source with an exact locator, so the writer cites a passage and not a
homepage, and the editor can reopen it.

Pin these to primary sources with exact chapter/section/page or equation number:
1. The finite Markov decision process: the formal tuple, the agent-environment
   interaction, and the Markov property. The canonical source is Sutton & Barto,
   *Reinforcement Learning: An Introduction*, 2nd edition (the free authorized
   PDF). Record the exact sections (the finite-MDP chapter), the dynamics
   function p(s',r | s,a), and page/equation numbers.
2. The discounted return and the discount factor gamma: the definition and the
   reason gamma < 1 is used. Sutton & Barto, same chapter. Record equation
   numbers.
3. Policies, state-value v_pi and action-value q_pi, and the Bellman expectation
   equations for both. Sutton & Barto, the value-functions sections. Record the
   exact equation numbers for the Bellman expectation equations.
4. The linear-algebra solution of policy evaluation, v_pi = (I - gamma P_pi)^{-1}
   r_pi, and iterative policy evaluation as a fixed-point iteration. Record where
   this is stated (Sutton & Barto's dynamic-programming chapter, or a standard
   reference such as Bertsekas, or David Silver's lecture notes). Give the
   contraction/convergence fact with its source.

Then record at least one strong modern secondary teaching reference for the
reader (OpenAI Spinning Up "Key Concepts in RL", or David Silver's course) with
a URL that resolves, classified as secondary, for the Background/Go-deeper bands
and for cross-checking notation.

Notes specific to this lesson:
- The writer will DERIVE the Bellman equation and WRITE and RUN gridworld code;
  the derivation and the code's numbers are the lesson's own work, not something
  you supply. You supply the authoritative statements and locators they are
  checked against, and you flag any notation clash between sources (for example
  reward timing R_{t+1} vs R_t, or p(s',r|s,a) vs separate P and R) so the writer
  picks one convention and stays in it.
- In Numbers, you do not need empirical figures; instead record the canonical
  equations (return, Bellman expectation for v_pi and q_pi, the matrix solve) in
  the source's own form with the locator, so the writer's rendered math can be
  checked symbol by symbol.
- min_sources 4. Confirm every URL resolves (the S&B PDF, the Spinning Up page,
  etc.). Record the address where each document lives.

Report the path and whether every equation the lesson needs is pinned to a
locator a reader can open.
