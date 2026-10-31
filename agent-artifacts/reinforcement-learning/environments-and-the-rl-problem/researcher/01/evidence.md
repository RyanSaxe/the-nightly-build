# Evidence record: environments and the RL problem (researcher 01)

Every definition and equation the lesson needs is pinned to a passage in a document I opened, with a printed page or slide number and, for Sutton and Barto, an equation number. Sutton and Barto (2nd edition) owns the finite MDP, the dynamics function p(s',r|s,a), the discounted return, v_pi, q_pi, the Bellman equation for v_pi, and iterative policy evaluation. Three things are thin. First, Sutton and Barto never numbers the Bellman equation for q_pi (it is Exercise 3.17, p. 61, and Exercise 4.3, p. 76), so q_pi's equation is pinned to Silver and Spinning Up instead. Second, Sutton and Barto never writes the matrix solve v_pi = (I - gamma P_pi)^{-1} r_pi and states convergence of iterative policy evaluation without proof or rate, so those come from Silver (lectures 2 and 3) and Szepesvari (Fact 1 and Appendix A). Third, no cited proof covers gamma = 1 episodic tasks, so the lesson's contraction claim is safe only for gamma < 1. The sources disagree on notation in five places that matter, listed under Contradictions with a recommended single convention.

Page convention: Sutton and Barto locators are printed page numbers. The PDF page is the printed page plus 22 (printed p. 59 is PDF page 81). Szepesvari's PDF page equals its printed page. Silver's locators are slide numbers, which equal PDF page numbers in the files below (the slides carry no printed number).

## Sources

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (landing page: http://incompleteideas.net/book/the-book-2nd.html)
Kind:        primary. Richard S. Sutton and Andrew G. Barto wrote the definitions and fixed the notation the lesson uses.
             The PDF is the second printing (2020) of the 2nd edition, MIT Press 2018. The copyright page releases it under
             CC BY-NC-ND 2.0, so it is the free authorized copy. Both URLs returned HTTP 200 (checked 2026-10-31); the PDF is
             548 pages, 73 MB, and I read it as text and rendered pages 53, 59, 60 and 77 as images to check glyphs.
Establishes: firsthand, the finite MDP and dynamics function, the Markov property as a condition on the state, the return and
             discount rate, policies, v_pi and q_pi, the Bellman equation for v_pi, the linear-system remark, and iterative
             policy evaluation with its stopping rule. Does not establish the matrix form, a contraction proof, or a numbered
             Bellman equation for q_pi.
Paraphrase:  Agent and environment interact at discrete steps t = 0,1,2,...; the agent sees S_t, picks A_t, and one step later
             receives R_{t+1} and S_{t+1}, giving the trajectory S0,A0,R1,S1,A1,R2,... In a finite MDP the sets of states, actions
             and rewards are finite, and the joint distribution of (S_t, R_t) given the preceding state and action is the
             function p(s',r|s,a). The Markov property is a restriction on the state: it must carry whatever about the past
             matters for the future. The return is the discounted sum of future rewards; for gamma < 1 it is finite when rewards
             are bounded; gamma = 0 is myopic and gamma near 1 is farsighted. A policy maps states to action probabilities.
             v_pi(s) and q_pi(s,a) are expected returns from s, or from s with first action a, then following pi. v_pi satisfies
             a recursion over successor states (3.14). With known dynamics that recursion is a system of |S| linear equations in
             |S| unknowns, and treating it as an update rule gives iterative policy evaluation.
Locators:    Chapter 3 "Finite Markov Decision Processes".
             3.1 The Agent-Environment Interface, pp. 47-52: Figure 3.1 (p. 48); trajectory (3.1) and dynamics p (3.2) (p. 48);
               footnote 4 on reward timing (p. 48); normalization (3.3), the Markov-property paragraph, p(s'|s,a) (3.4), r(s,a)
               (3.5), r(s,a,s') (3.6) and "we usually use the four-argument p function" (all p. 49).
             3.2 Goals and Rewards, pp. 53-54: reward hypothesis and the maze example with reward -1 per step "to escape as
               quickly as possible" (p. 53). This is the passage that supports the lesson's step-reward design.
             3.3 Returns and Episodes, pp. 54-55: finite-horizon return (3.7) (p. 54); discounted return (3.8), the
               gamma < 1 convergence sentence, gamma = 0 and gamma -> 1, the recursion (3.9), and the constant-reward sum (3.10)
               (all p. 55).
             3.4 Unified Notation, pp. 57-58: absorbing-state convention for terminal states and the unified return (3.11) (p. 57).
             3.5 Policies and Value Functions, pp. 58-60: policy definition and v_pi (3.12), q_pi (3.13) (p. 58); Bellman equation
               for v_pi (3.14) and its backup diagram (p. 59); "v_pi is the unique solution to its Bellman equation" and
               Example 3.5 (5x5 gridworld, gamma = 0.9, solved "by solving the system of linear equations (3.14)") with
               Figure 3.2 (p. 60). Exercises 3.12-3.14 (pp. 58, 60) and 3.17-3.19 (pp. 61-62).
             Chapter 4 "Dynamic Programming", 4.1 Policy Evaluation (Prediction), pp. 74-76: (4.3) and (4.4) restate the v_pi
               recursion; "existence and uniqueness of v_pi are guaranteed as long as either gamma < 1 or eventual termination is
               guaranteed" and "(4.4) is a system of |S| simultaneous linear equations in |S| unknowns" (p. 74); update rule (4.5)
               and "v_k = v_pi is a fixed point" (p. 74); two-array versus in-place sweeps and the Iterative Policy Evaluation
               pseudocode box with threshold theta (p. 75); Example 4.1, a 4x4 gridworld with reward -1 and gamma = 1 (p. 76);
               Figure 4.1 with the value tables for k = 0, 1, 2, 3, 10, infinity (p. 77); Exercise 4.3 asks for the action-value
               analogues of (4.3)-(4.5) (p. 76).
             Section 10.4 "Deprecating the Discounted Setting", pp. 253-254 (caveat on gamma, see Contradictions).
Quote:       "This is best viewed as a restriction not on the decision process, but on the state." (p. 49). The wording matters
             because the lesson states the Markov property in plain words.
             "We use R_{t+1} instead of R_t to denote the reward due to A_t because it emphasizes that the next reward and next
             state, R_{t+1} and S_{t+1}, are jointly determined. Unfortunately, both conventions are widely used in the
             literature." (footnote 4, p. 48).
             "Clearly, v_k = v_pi is a fixed point for this update rule... Indeed, the sequence {v_k} can be shown in general
             to converge to v_pi as k -> infinity under the same conditions that guarantee the existence of v_pi." (p. 74).
             The book asserts this and does not prove it.
```

```text
URL:         https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-2-mdp.pdf
             (course page: https://davidstarsilver.wordpress.com/teaching/ ; the older address
             https://davidsilver.uk/teaching/ redirects there)
Kind:        primary for what it states. David Silver wrote these slides, "Lecture 2: Markov Decision Processes" (57 slides).
             It is lecture material, not the origin of the underlying mathematics, so it owns its notation and its
             "Bellman expectation equation" naming and nothing earlier. Fetched, HTTP 200, 835 KB.
Establishes: firsthand, the MDP as the tuple <S,A,P,R,gamma>, the induced Markov reward process for a fixed policy, the
             Bellman expectation equations for v_pi and q_pi in both one-step forms, and the matrix solve. Repeats S&B on
             the Markov property and the return.
Paraphrase:  A state S_t is Markov iff P[S_{t+1}|S_t] = P[S_{t+1}|S_1,...,S_t]. An MDP is <S,A,P,R,gamma> with
             P^a_{ss'} = P[S_{t+1}=s'|S_t=s,A_t=a], R^a_s = E[R_{t+1}|S_t=s,A_t=a], gamma in [0,1]. Fixing pi induces
             P^pi_{s,s'} = sum_a pi(a|s) P^a_{ss'} and R^pi_s = sum_a pi(a|s) R^a_s. The Bellman expectation equation in
             matrix form is v_pi = R^pi + gamma P^pi v_pi with direct solution v_pi = (I - gamma P^pi)^{-1} R^pi.
             Direct solution costs O(n^3), so it is practical only for small problems.
Locators:    slide 4 (Markov property); slide 12 (return G_t, gamma in [0,1], "myopic" and "far-sighted"); slide 13 ("Why
             discount?" list); slide 22 (matrix form for an MRP, v = R + gamma P v); slide 23 (v = (I - gamma P)^{-1} R, O(n^3));
             slide 24 (MDP tuple); slide 26 (policy); slide 27 (P^pi, R^pi); slide 28 (v_pi, q_pi); slides 31-32
             (v_pi in terms of q_pi, q_pi in terms of v_pi); slide 33 (Bellman expectation equation for v_pi); slide 34 (Bellman
             expectation equation for q_pi); slide 36 (matrix form for the induced MRP and the solve).
Quote:       none needed.
```

```text
URL:         https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-3-planning-by-dynamic-programming-.pdf
Kind:        primary for what it states. David Silver, "Lecture 3: Planning by Dynamic Programming" (42 slides). Fetched,
             HTTP 200, 824 KB. Same standing as lecture 2.
Establishes: firsthand, iterative policy evaluation as a matrix iteration, the infinity-norm contraction proof for the Bellman
             expectation operator, and the conclusion that iterative policy evaluation converges to v_pi. This is the only
             place in the set that gives the contraction argument for gamma < 1 in the exact form the lesson needs.
Paraphrase:  v_{k+1}(s) = sum_a pi(a|s)(R^a_s + gamma sum_{s'} P^a_{ss'} v_k(s')), equivalently v^{k+1} = R^pi + gamma P^pi v^k,
             synchronous (every state updated from the old vector). Distance between value functions is the infinity-norm
             max_s |u(s) - v(s)|. The operator T^pi(v) = R^pi + gamma P^pi v satisfies ||T^pi(u) - T^pi(v)||_inf <= gamma ||u - v||_inf.
             By the contraction mapping theorem T^pi has a unique fixed point at a linear rate gamma. v_pi is a fixed point by the
             Bellman expectation equation, so iterative policy evaluation converges to v_pi.
Locators:    slide 7 (iterative policy evaluation statement); slide 8 (one-step form and matrix form v^{k+1} = R^pi + gamma P^pi v^k);
             slide 36 (value function space); slide 37 (infinity-norm); slide 38 (T^pi is a gamma-contraction, the three-line
             inequality); slide 39 (contraction mapping theorem, stated without proof); slide 40 (convergence of iterative policy
             evaluation).
Quote:       none needed.
```

```text
URL:         https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf
Kind:        primary for the proofs it contains. Csaba Szepesvari, "Algorithms for Reinforcement Learning" (Synthesis
             Lectures on AI and ML, Morgan and Claypool). The file is the author's draft of the lecture (title page dated
             June 9, 2009, last updated March 12, 2019), 98 pages, hosted on his University of Alberta page. Fetched, HTTP 200,
             1.6 MB. Cite it as the draft, not as the published book, because I did not open the published edition. The theorem
             itself belongs to Banach; this is a textbook exposition with proof.
Establishes: firsthand, the Bellman operator T^pi for a policy, the compact form r^pi + gamma P^pi V^pi = V^pi, the statement that
             for 0 < gamma < 1 T^pi is a maximum-norm contraction with a unique fixed point, Banach's fixed-point theorem with a
             geometric rate and a full proof, and a short proof that T^pi is a gamma-contraction in the sup norm.
Paraphrase:  The MDP is (X, A, P0) where P0 is the joint kernel of (next state, reward): (X_{t+1}, R_{t+1}) ~ P0(.|X_t,A_t).
             Return is sum_t gamma^t R_{t+1}. For a deterministic stationary policy, V^pi(x) = r(x,pi(x)) + gamma sum_y P(x,pi(x),y)
             V^pi(y) (9), which is T^pi V^pi = V^pi (10), and for finite state spaces r^pi + gamma P^pi V^pi = V^pi (11). The
             system is linear and T^pi is affine. Banach: a contraction on a Banach space has a unique fixed point, and iterating
             from any v_0 converges with ||v_n - v|| <= gamma^n ||v_0 - v||. The proof that ||T^pi U - T^pi V||_inf <= gamma
             ||U - V||_inf uses that each row of P^pi sums to 1.
Locators:    Section 2.2 "Markov Decision Processes", p. 9, equation (1) and the discounted return. Section 2.3 "Value functions",
             p. 13 equation (7) (V^pi), p. 14 (Q^pi), p. 15 Fact 1 with equations (9), (10), (11), p. 16 Fact 3 (Q^pi is the unique fixed
             point of an operator, equation (14), which is written for a deterministic policy with Q(y,pi(y))). Appendix A.1, p. 77 Theorem 1 (Banach's fixed-point theorem) with proof; Appendix A.2 "Application to
             MDPs", p. 79, the T^pi contraction argument and "by Banach's fixed-point theorem will converge to V^pi at a geometric rate".
Quote:       none needed.
```

```text
URL:         https://spinningup.openai.com/en/latest/spinningup/rl_intro.html
             (anchors: #reward-and-return, #value-functions, #bellman-equations, #optional-formalism)
Kind:        secondary. OpenAI's "Part 1: Key Concepts in RL" (copyright 2018, OpenAI) is a teaching summary written from outside
             the authors who defined the framework. It restates Sutton and Barto style material for deep RL readers and owns none
             of it. Fetched, HTTP 200. Equations on the page are SVG images; I read them from the image alt text in the HTML.
Establishes: repeats the return, value functions and Bellman equations in deep-RL notation, and independently supplies the Bellman
             equation for Q^pi in one line, which Sutton and Barto leaves as an exercise. Gives a plain-language reason for gamma.
Paraphrase:  Reward r_t = R(s_t,a_t,s_{t+1}); infinite-horizon discounted return R(tau) = sum_{t=0}^inf gamma^t r_t with
             gamma in (0,1). "Cash now is better than cash later" and, mathematically, the undiscounted infinite sum may not
             converge. V^pi(s) = E[R(tau) | s_0 = s], Q^pi(s,a) = E[R(tau) | s_0 = s, a_0 = a]. Bellman equations for the on-policy
             functions:
               V^pi(s)   = E_{a~pi, s'~P}[ r(s,a) + gamma V^pi(s') ]
               Q^pi(s,a) = E_{s'~P}[ r(s,a) + gamma E_{a'~pi}[ Q^pi(s',a') ] ]
             An MDP is the 5-tuple <S, A, R, P, rho_0> (states, actions, reward function R: S x A x S -> reals, transition
             probability P: S x A -> distributions over S, starting-state distribution). The Markov property is stated as
             "transitions only depend on the most recent state and action, and no prior history."
Locators:    section "Reward and Return" (discounted return and the "Why would we ever want a discount factor" paragraph); section
             "Value Functions"; section "Bellman Equations"; section "(Optional) Formalism" at the end of the page.
Quote:       "Mathematically: an infinite-horizon sum of rewards may not converge to a finite value, and is hard to deal with in
             equations. But with a discount factor and under reasonable conditions, the infinite sum converges." The wording is
             hedged ("under reasonable conditions"), which is the only reason to quote it.
```

## Contradictions

Notation clashes the writer must resolve before drafting. Each is a real difference in the primary documents. The recommended convention follows the list.

1. Reward timing. Sutton and Barto index the reward for action A_t as R_{t+1} (trajectory (3.1), return (3.8), footnote 4, p. 48), and Silver (slides 12, 24) and Szepesvari (Section 2.2, p. 9) match. Spinning Up writes r_t = R(s_t,a_t,s_{t+1}), which is the same number under a different subscript, and sums from t = 0, so its return sum_{t>=0} gamma^t r_t is Sutton and Barto's G_t with the index shifted. The commission writes G_t = sum_k gamma^k R_{t+k+1}, which is Sutton and Barto's form. Within Sutton and Barto itself, (3.2) conditions R_t and S_t on S_{t-1}, A_{t-1}, while the trajectory and returns use R_{t+1}. Both are the same convention seen from the next step, but a reader moving from (3.2) to (3.8) sees t shift by one.
2. The environment's primitive. Sutton and Barto use one four-argument function p(s',r|s,a) (3.2) and derive p(s'|s,a) (3.4) and r(s,a) (3.5) from it. Silver uses a transition matrix P^a_{ss'} and an expected-reward function R^a_s. Szepesvari uses a joint kernel P0 and also writes P(x,a,y) and r(x,a). Spinning Up uses P(s'|s,a) and a reward function R(s,a,s'). The commission's tuple (S, A, P, R, gamma) is Silver's. Sutton and Barto never writes a tuple, and writes "we usually use the four-argument p function (3.2), but each of these other notations are also occasionally convenient" (p. 49).
3. What is in the tuple. Silver puts gamma in the tuple. Spinning Up's 5-tuple has the starting-state distribution rho_0 and no gamma. Szepesvari's MDP is (X, A, P0) with gamma outside. Sutton and Barto has no tuple. The commission's (S, A, P, R, gamma) is a choice among these and should be stated as the lesson's own definition with p as the source primitive.
4. Symbol collisions. Sutton and Barto's script R is the set of rewards and R_t a random variable, and lowercase r is both a summation variable and the function r(s,a) (3.5). If the lesson names the reward array R (as the commission's tuple does), it collides with the set R. Spinning Up's R(tau) names the return and R(s,a,s') the reward function on the same page. Szepesvari writes states as X_t, x, y.
5. Name of the equation. Sutton and Barto calls (3.14) "the Bellman equation for v_pi" (p. 59) and "Bellman optimality equation" for the max version. "Bellman expectation equation" is Silver's name (slides 31-36). Szepesvari writes "the Bellman equation for V^pi". The commission says "Bellman expectation equation". That name is Silver's, and the lesson should say Sutton and Barto's plain name for it once.
6. Spinning Up is internally loose. Its reward is R(s,a,s') but its Bellman equations contain r(s,a) inside an expectation over s'. That is ambiguous for rewards that depend on s'. Do not copy its form. Use it for the shape of the q equation only.
7. Scope of the Bellman equation for q_pi. Sutton and Barto states no numbered equation for it (Exercises 3.17 and 4.3, solutions not in the book; the book's solutions page says it is "currently incomplete"). The only openable statements are Silver slide 34, Spinning Up, and Szepesvari equation (14) (which is in operator form with Q(y,pi(y)), for deterministic pi, and is not the sum over a' of pi). Silver slide 34 is the closest match to what the lesson will derive.
8. Range of gamma. Sutton and Barto and Silver allow 0 <= gamma <= 1 (the book permits gamma = 1 when termination is guaranteed, p. 74; Silver slide 13 says undiscounted is possible if all sequences terminate). Spinning Up requires gamma in (0,1). Szepesvari's contraction statement and Silver's contraction proof need gamma < 1 (the proof's factor is gamma, so at gamma = 1 it proves nothing). So the contraction argument covers gamma < 1 only. Sutton and Barto's convergence sentence for gamma = 1 with guaranteed termination (p. 74) is unproved in the book and none of the other documents proves it.
9. A caveat on "why discount". The commission gives two reasons (convergence, preference for sooner reward). Sutton and Barto gives convergence for bounded rewards and the "present value" reading (p. 55). Silver lists more (slide 13): uncertainty about the future, interest on money, animal and human behaviour, and that undiscounted is fine when all sequences terminate. Sutton and Barto Section 10.4 (pp. 253-254) argues that with function approximation in continuing tasks gamma "has no effect on the problem formulation" and discounting has no role in defining the control problem. That caveat does not touch a tabular gridworld, so the lesson can state the two reasons without it, but a claim that discounting is "required" would be wrong.
10. Terminal states. Sutton and Barto treats the terminal state as part of S+ with value 0, and unifies by an absorbing state that pays 0 (Section 3.4, p. 57). Its own gridworld Example 4.1 solves for the nonterminal states only, S = {1,...,14} (p. 76). The matrix solve in the lesson needs the same choice: either drop the terminal state and use the substochastic matrix on nonterminal states, or keep an absorbing row with reward 0. Silver's matrix formulas (slides 23, 36) assume no terminal state and do not say how to handle one.
11. A step the source skips. Sutton and Barto's derivation of (3.14) (p. 59) replaces E_pi[G_{t+1} | S_{t+1} = s'] with v_pi(s') in its third line, and conditions only on S_{t+1} where the preceding line has conditioned on S_t, A_t and R_{t+1} as well. The Markov property is what licenses that replacement, and the book does not say so at that line. The commission asks for the derivation "in full", so the writer has to supply this step. No source in the set does.

Recommended convention, one choice to stay in:

- Time and reward: Sutton and Barto. S_0, A_0, R_1, S_1,... and G_t = sum_{k>=0} gamma^k R_{t+k+1} (3.8), with the recursion G_t = R_{t+1} + gamma G_{t+1} (3.9).
- Environment primitive: p(s',r|s,a) (3.2), with p(s'|s,a) (3.4) and r(s,a) (3.5) derived from it. Then define the arrays P[s,a,s'] = p(s'|s,a) and R[s,a] = r(s,a) in one sentence, and state that this is how the commission's (S, A, P, R, gamma) relates to Sutton and Barto.
- Policy-induced quantities: P_pi[s,s'] = sum_a pi(a|s) p(s'|s,a) and r_pi[s] = sum_a pi(a|s) r(s,a), following Silver slide 27 and Szepesvari equation (11). Sutton and Barto defines neither. Say they are defined here.
- Name the equation "Bellman equation for v_pi" and, once, note that it is also called the Bellman expectation equation.

## Numbers

No empirical figures are needed. These are the equations the lesson renders, in each source's own form. `.=` is the source's dotted-equals "defined as". Sutton and Barto symbols: S states, A actions, R the finite reward set, pi policy, E_pi expectation under pi.

Idea 1 and 2: interaction and the finite MDP

```text
Figure: (3.1)  S0, A0, R1, S1, A1, R2, S2, A2, R3, ...
Owner:  Sutton and Barto, p. 48
Scope:  t = 0,1,2,...; R_{t+1} is the reward that follows A_t.

Figure: (3.2)  p(s',r|s,a) .= Pr{ S_t = s', R_t = r | S_{t-1} = s, A_{t-1} = a },  for all s',s in S, r in R, a in A(s)
Owner:  Sutton and Barto, p. 48. Domain: p : S x R x S x A -> [0,1].
Scope:  the dynamics function; the book calls it the dynamics of the MDP.

Figure: (3.3)  sum_{s' in S} sum_{r in R} p(s',r|s,a) = 1,  for all s in S, a in A(s)
Owner:  Sutton and Barto, p. 49.
Scope:  for each (s,a), p is a probability distribution. Exercise 3.5 (p. 55) says the episodic case needs a small modification.

Figure: (3.4)  p(s'|s,a) .= Pr{S_t = s' | S_{t-1} = s, A_{t-1} = a} = sum_{r in R} p(s',r|s,a)
Figure: (3.5)  r(s,a)   .= E[R_t | S_{t-1} = s, A_{t-1} = a] = sum_{r in R} r sum_{s' in S} p(s',r|s,a)
Figure: (3.6)  r(s,a,s') .= E[R_t | S_{t-1}=s, A_{t-1}=a, S_t=s'] = sum_{r in R} r p(s',r|s,a)/p(s'|s,a)
Owner:  Sutton and Barto, p. 49.
Scope:  derived quantities; (3.4) and (3.5) are the array entries P[s,a,s'] and R[s,a] in the recommended convention.

Figure: Markov property, stated in words: the probabilities of S_t and R_t "depend on the immediately preceding state and action,
        S_{t-1} and A_{t-1}, and, given them, not at all on earlier states and actions"
Owner:  Sutton and Barto, p. 49 (a restriction on the state). Also Silver slide 4: P[S_{t+1}|S_t] = P[S_{t+1}|S_1,...,S_t].
Scope:  holds for the state, not as a separate assumption about the process.
```

Idea 3: return and discount

```text
Figure: (3.8)  G_t .= R_{t+1} + gamma R_{t+2} + gamma^2 R_{t+3} + ... = sum_{k=0}^{inf} gamma^k R_{t+k+1},   0 <= gamma <= 1
Owner:  Sutton and Barto, p. 55. Silver slide 12 is the same with gamma in [0,1].
Scope:  gamma < 1 gives a finite sum when {R_k} is bounded; gamma = 0 maximizes only R_{t+1}; gamma -> 1 weights the future more.

Figure: (3.9)  G_t = R_{t+1} + gamma G_{t+1},   for all t < T, with G_T = 0
Owner:  Sutton and Barto, p. 55.
Scope:  the recursion the Bellman derivation uses.

Figure: (3.10) G_t = sum_{k=0}^{inf} gamma^k = 1/(1 - gamma),  for constant reward +1 and gamma < 1
Owner:  Sutton and Barto, p. 55.
Scope:  the bound R_max/(1-gamma) for bounded rewards follows from it; the book states only the constant-reward case.

Figure: (3.11) G_t .= sum_{k=t+1}^{T} gamma^{k-t-1} R_k,   T = inf or gamma = 1 allowed, not both
Owner:  Sutton and Barto, p. 57.
Scope:  the episodic and continuing unified form; terminal state as absorbing state with reward 0.
```

Idea 4: policy, value functions, Bellman equation

```text
Figure: policy: pi(a|s) is the probability that A_t = a if S_t = s
Owner:  Sutton and Barto, p. 58.
Scope:  "a mapping from states to probabilities of selecting each possible action". Silver slide 26 gives pi(a|s) = P[A_t = a | S_t = s].

Figure: (3.12) v_pi(s) .= E_pi[G_t | S_t = s] = E_pi[ sum_{k=0}^{inf} gamma^k R_{t+k+1} | S_t = s ],  for all s in S
Figure: (3.13) q_pi(s,a) .= E_pi[G_t | S_t = s, A_t = a] = E_pi[ sum_{k=0}^{inf} gamma^k R_{t+k+1} | S_t = s, A_t = a ]
Owner:  Sutton and Barto, p. 58. "the value of the terminal state, if any, is always zero".
Scope:  t is any time step; E_pi means the agent follows pi.

Figure: (3.14) v_pi(s) = sum_a pi(a|s) sum_{s',r} p(s',r|s,a) [ r + gamma v_pi(s') ],  for all s in S
        derivation lines on p. 59: v_pi(s) .= E_pi[G_t|S_t=s] = E_pi[R_{t+1} + gamma G_{t+1} | S_t=s] (by (3.9))
        = sum_a pi(a|s) sum_{s'} sum_r p(s',r|s,a) [ r + gamma E_pi[G_{t+1}|S_{t+1}=s'] ] = (3.14)
Owner:  Sutton and Barto, p. 59, called "the Bellman equation for v_pi". Restated as (4.3) and (4.4) on p. 74. (4.3) is the expectation
        form: v_pi(s) = E_pi[R_{t+1} + gamma v_pi(S_{t+1}) | S_t = s].
Scope:  s' ranges over S (S+ for episodic); a over A(s); r over R. For gamma < 1, or termination guaranteed under pi, v_pi exists and is
        unique (p. 74).

Figure: Bellman equation for v_pi in terms of q_pi (Silver slide 31):  v_pi(s) = sum_{a in A} pi(a|s) q_pi(s,a)
Figure: q_pi in terms of v_pi (Silver slide 32):                        q_pi(s,a) = R^a_s + gamma sum_{s'} P^a_{ss'} v_pi(s')
Figure: Bellman expectation equation for q_pi (Silver slide 34):
        q_pi(s,a) = R^a_s + gamma sum_{s' in S} P^a_{ss'} sum_{a' in A} pi(a'|s') q_pi(s',a')
Figure: Spinning Up Bellman equation for Q^pi:  Q^pi(s,a) = E_{s'~P}[ r(s,a) + gamma E_{a'~pi}[Q^pi(s',a')] ]
Owner:  Silver lecture 2, slides 31, 32, 34; Spinning Up, "Bellman Equations". Sutton and Barto leaves this as Exercise 3.17 (p. 61, with the q_pi
        backup diagram) and Exercises 3.13 (p. 58) and 3.19 (p. 62), and Exercise 4.3 (p. 76).
Scope:  no numbered Sutton and Barto equation exists for q_pi. In the p-notation the equation the writer derives would read
        q_pi(s,a) = sum_{s',r} p(s',r|s,a) [ r + gamma sum_{a'} pi(a'|s') q_pi(s',a') ]. That line is my transcription of the exercise's
        answer under Sutton and Barto's own notation, not a printed equation, so the writer's derivation is what the editor checks it against
        using Silver slide 34 as the printed form.
```

Matrix solve and iterative policy evaluation

```text
Figure: Silver lecture 2 slide 36:  v_pi = R^pi + gamma P^pi v_pi,   with direct solution  v_pi = (I - gamma P^pi)^{-1} R^pi
        slide 22-23 (MRP): v = R + gamma P v, (I - gamma P) v = R, v = (I - gamma P)^{-1} R, computational complexity O(n^3) for n states
Figure: Szepesvari (11):  r^pi + gamma P^pi V^pi = V^pi   (finite state space; (10) T^pi V^pi = V^pi, T^pi affine linear)
Owner:  Silver lecture 2, slides 22, 23, 36; Szepesvari, Section 2.3, p. 15. Sutton and Barto never writes the matrix form: it says (4.4) is "a system of |S|
        simultaneous linear equations in |S| unknowns" and "in principle, its solution is a straightforward, if tedious, computation" (p. 74), and Example 3.5
        says the Figure 3.2 values were "computed by solving the system of linear equations (3.14)" (p. 60).
Scope:  P^pi is |S| x |S| row-stochastic; R^pi is |S|-dimensional. Invertibility of (I - gamma P^pi) for gamma < 1 is not stated in Silver or Sutton and
        Barto. It follows from uniqueness of the fixed point of the affine operator T^pi (Szepesvari, p. 15 and Appendix A.2). That inference is mine.

Figure: (4.5)  v_{k+1}(s) .= E_pi[R_{t+1} + gamma v_k(S_{t+1}) | S_t = s] = sum_a pi(a|s) sum_{s',r} p(s',r|s,a) [ r + gamma v_k(s') ],  for all s in S
Owner:  Sutton and Barto, p. 74. v_0 arbitrary except terminal value 0. Pseudocode box, p. 75, stops when delta = max_s |v_new(s) - v_old(s)| < theta.
        Matrix form: Silver lecture 3, slide 8, v^{k+1} = R^pi + gamma P^pi v^k.
Scope:  the two-array (synchronous) version computes the matrix iteration exactly; Sutton and Barto's box is the in-place version, which "also converges
        to v_pi; in fact, it usually converges faster" (p. 75). The writer should say which one the code runs.

Figure: contraction: T^pi(v) = R^pi + gamma P^pi v;  ||T^pi(u) - T^pi(v)||_inf <= gamma ||u - v||_inf,  ||u - v||_inf = max_s |u(s) - v(s)|
Owner:  Silver lecture 3, slide 38 (proof), slide 39 (theorem: unique fixed point at linear rate gamma), slide 40 (consequence for iterative policy
        evaluation). Szepesvari Appendix A.2, p. 79 (same argument, uses that rows of P^pi sum to 1); Theorem 1, p. 77: ||v_n - v|| <= gamma^n ||v_0 - v||.
Scope:  gamma < 1 only. The contraction is in the infinity-norm, not any other norm. For gamma = 1 with termination, see Limits.
```

Known-answer checks the writer can run their code against. The tables are printed in Sutton and Barto. The recomputation is mine, run with numpy in a scratch script, and agrees with both printed tables to the printed digits.

```text
Figure: Figure 3.2 (right), 5x5 gridworld with special cells A and B, gamma = 0.9, equiprobable random policy, v_pi rows top to bottom:
        3.3 8.8 4.4 5.3 1.5 / 1.5 3.0 2.3 1.9 0.5 / 0.1 0.7 0.7 0.4 -0.4 / -1.0 -0.4 -0.4 -0.6 -1.2 / -1.9 -1.3 -1.2 -1.4 -2.0
Owner:  Sutton and Barto, Example 3.5 and Figure 3.2, p. 60. Rules (p. 60): off-grid moves leave the cell unchanged with reward -1; from A all actions give +10 and go
        to A'; from B all actions give +5 and go to B'; other moves give 0. The drawing on p. 60 (left panel) puts A in the top row second cell, B in the top row fourth cell, A' in the bottom row
        second cell and B' in the middle row fourth cell, and the recomputed table matched the printed one with those positions. The PDF's text layer also carries
        a stray "Figure 3.5" caption on that page, but the rendered figure is captioned Figure 3.2.
Scope:  one decimal place. My direct solve (I - gamma P_pi)^{-1} r_pi reproduced the table; iterating v <- r_pi + gamma P_pi v from zero for 400 sweeps matched the
        direct solve to 1e-15.

Figure: Figure 4.1, k = infinity, 4x4 gridworld, terminal cells top-left and bottom-right, reward -1 on every transition, gamma = 1, equiprobable random policy:
        0.0 -14. -20. -22. / -14. -18. -20. -20. / -20. -20. -18. -14. / -22. -20. -14. 0.0
        and k = 1, 2, 3 rows: k=1 all -1.0 (terminal 0.0); k=2 -1.7 and -2.0; k=3 -2.4, -2.9, -3.0
Owner:  Sutton and Barto, Example 4.1 (p. 76) and Figure 4.1 (p. 77), "rounded to two significant digits".
Scope:  my recomputation gives the same k = infinity table exactly (integers) and k = 2 entries of -1.75, which Sutton and Barto prints as -1.7. Use the exact value
        -1.75 in the lesson's own output and do not claim a mismatch. The spectral radius of the substochastic matrix on the 14 nonterminal states is 0.9468 (my
        computation, not a sourced figure), which is why I - P is invertible here even at gamma = 1.
```

## Limits

- The matrix solve and the contraction proof are not in Sutton and Barto. Silver and Szepesvari supply them, and both are lecture or draft text I read in full at the cited slides and pages. I did not open Bertsekas (the brief offered it) or the published Morgan and Claypool edition of Szepesvari. A page cite to either would be invented.
- Banach (1922), Bellman (1957) and Denardo (1967), who own the underlying theorem and the equation, I did not open. Do not credit them by page. Sutton and Barto's Chapter 3 Bibliographical and Historical Remarks (printed p. 71) say Bellman (1957a) popularized the Bellman optimality equation and mention Denardo's (1967) treatment of dynamic programming through contraction mappings. I read only that pointer.
- No source in the set proves that iterative policy evaluation converges for gamma = 1 with termination, and Silver's and Szepesvari's contraction arguments need gamma < 1. If the lesson's gridworld uses gamma < 1 (Example 3.5 uses 0.9) every cited argument applies. If it uses gamma = 1 episodic, the convergence rests on Sutton and Barto's unproved sentence at p. 74, and the lesson should say so or prove it.
- Invertibility of (I - gamma P_pi) as a stated fact is in none of the sources. It follows from the unique fixed point of the affine operator T^pi (Szepesvari p. 15 and Appendix A.2), and the writer must derive it (a one-line argument from the contraction) rather than cite a page.
- The Bellman equation for q_pi has no numbered Sutton and Barto equation. It can be cited to Silver slide 34 and Spinning Up, and cross-checked against Szepesvari's operator form (14), but not to a Sutton and Barto equation number.
- The derivation the writer is asked for ((3.14) from the definition) is the lesson's own work. Sutton and Barto's version skips the conditional-independence step (Contradictions, item 11), and no other source in the set writes it out.
- I did not run the writer's gridworld. The two checks above use Sutton and Barto's grids, not the lesson's. The lesson's numbers must come from the lesson's code.
- The lesson's claim that a reward of -1 per step "makes the agent prefer short paths" is supported by Sutton and Barto's maze example (p. 53) as a reward-design example. The book does not prove it for a particular policy, and the lesson evaluates a fixed policy, so it should state the preference as a property of the return, not of the evaluation.
- Spinning Up is a web page and can change. I recorded its text on 2026-10-31 from the page at revision shown in its footer (038665d6).

## Source assets

```text
Asset: Sutton and Barto Figure 3.1, "The agent-environment interaction in a Markov decision process" (p. 48): agent box on top, environment box below,
       arrows for state S_t and reward R_t into the agent, action A_t out, and a second arrow pair labelled R_{t+1}, S_{t+1}.
Shows: the timing: reward R_{t+1} and state S_{t+1} arrive together one step after A_t.
Crop:  keep the S_t, R_t, A_t labels and the R_{t+1}, S_{t+1} feedback arrow; omit the surrounding text. The lesson commissions its own SVG of this loop, so use this only as the reference.

Asset: Sutton and Barto backup diagram for v_pi (p. 59, beside (3.14)) and the q_pi backup diagram (p. 61, with Exercise 3.17).
Shows: the two-level tree (state, then action nodes weighted by pi, then reward and next state) that equation (3.14) sums over.
Crop:  keep the open and solid circles and the labels pi, a, p, r, s'; omit the surrounding exercise text.

Asset: Sutton and Barto Figure 3.2 (p. 60): the 5x5 special-reward grid (left) and the state-value grid (right) for gamma = 0.9.
Shows: what a v_pi table looks like on a gridworld and why values near the lower edge are negative under the random policy.
Crop:  keep both panels and the A, B, A', B' markers and the +10, +5 labels; omit the caption's trailing text.

Asset: Sutton and Barto Figure 4.1 (p. 77): value tables for k = 0, 1, 2, 3, 10, infinity on the 4x4 grid, left column only.
Shows: iterative policy evaluation converging sweep by sweep, which is the picture the lesson's heatmap and its second method would reproduce for the lesson's own grid.
Crop:  keep the left column of value tables and the k labels; omit the right column of greedy-policy arrows, which belongs to policy improvement, a later lesson.

Asset: Silver lecture 2 slide 34 (Bellman expectation equation for q_pi, with its backup diagram) and slide 36 (matrix form).
Shows: the q_pi equation and the matrix solve in one notation, for checking the lesson's rendered symbols.
Crop:  keep the equation and diagram. I found no reuse licence on Silver's slides, so cite and redraw rather than capture.
```

## Discarded

```text
https://davidsilver.uk/wp-content/uploads/2020/03/MDP.pdf: 404, an address I guessed; it is not Silver's document location.
https://davidsilver.uk/wp-content/uploads/2020/03/DP.pdf: 404, same reason.
http://incompleteideas.net/book/RLbook2020trimmed.pdf: not opened; it is the trimmed-margin variant of the same book, and printed page numbers match the file I used, so I cite only the untrimmed file.
https://drive.google.com/open?id=1V9jAShWpccLvByv5S1DuOzo6GVvzd4LV (cited-literature collection on the S&B page): not opened, it is a bulk link to third-party papers and not a source for any claim here.
http://incompleteideas.net/book/errata.html: read for errata touching pp. 47-77. The relevant items are p. 54 (typo "aining"), p. 58 Exercise 3.11 (S_t should be S_t = s) and p. 80 (V(terminal)=0 in the policy-iteration box). None changes an equation I cite. Not a source for any claim.
```
