# Commission: reinforcement-learning/semi-gradient-td

Run: scheduled edition 2026-11-11. Template: lesson. Voice guide pinned by the series (writing-coach/01, written by nb start-article).

## Where the course stands
Published, in order: environments-and-the-rl-problem, finding-optimal-policies, learning-values-from-samples, action-values-from-samples, epsilon-greedy-exploration, sarsa-and-q-learning, termination-and-truncation, checking-a-custom-environment, training-an-off-the-shelf-agent, off-policy-importance-sampling, n-step-returns (2026-11-10). Stage 1 is complete. Stage 2 has taught everything through n-step returns. The next stage-2 topic is function approximation with semi-gradient updates; the deadly triad follows in a later lesson and is out of scope here beyond a one-sentence pointer at most.

## Topic and the one idea
Topic: function approximation with semi-gradient updates, for prediction.
The one idea: when a state's value is a parameterized function v̂(s, w), learning becomes stochastic gradient descent on squared error against a target. Monte Carlo's target does not depend on w, so its update is a true gradient step and converges to the weights that minimize the state-weighted value error. TD's target contains v̂(S', w), and the semi-gradient update ignores that dependence, so it is not a gradient of any fixed objective; with linear features under on-policy sampling it still converges, to a different point (the TD fixed point), whose error is bounded relative to the best achievable. The lesson derives the update from the objective and shows on a run where the two methods' solutions differ.

Required by the lesson: define the parameterized value function, feature vector, the on-policy state distribution μ and the mean squared value error objective VE(w); derive the gradient MC update and the semi-gradient TD(0) update; explain what "semi" drops; state linear TD's fixed point w_TD = A⁻¹b and the bound on its error (Sutton and Barto eq. 9.14, cite it; derivation of the bound is a side result and gets no derivation). State aggregation is the first feature construction and is a special case of linear features; the writer may mention that a table is linear with one-hot features.

## Case to start from
Sutton and Barto's 1000-state random walk (Example 9.1): an extension of the 19-state walk from n-step-returns (link that lesson for the original rules). States 1-1000, start at 500, each step jumps uniformly to one of the 100 states on either side, ends at −1/+1 off the edges with probability mass of out-of-range jumps going to termination. State aggregation into 10 groups of 100. Gradient MC vs semi-gradient TD(0). Show what was learned: the staircase approximation against the true value curve, and the on-policy distribution μ that decides where each step is accurate. Verify the true values by an exact solve (the course taught exact solves in lesson 1).

The writer chooses the experiments, the causes to test, and the page structure, within the series prompt's limit of two experimental results and its checks (fresh seeds, removal test on the page for any causal claim).

## Boundaries
- Prediction only. No control with function approximation, no tile coding beyond a pointer, no neural nets, no deadly triad divergence example (next lesson's).
- No reliance on RL ideas the course has not taught. Taught: MDPs, Bellman equations, value/policy iteration, Gymnasium contract, MC and TD(0) prediction, TD error, action values, GPI, ε-greedy, SARSA, Q-learning, termination vs truncation, env checker, SB3 PPO as a library call, importance sampling, n-step TD.
- Gradient descent, SGD and least squares are background (press/editorial.md audience) and need no teaching.

## Neighbouring articles this run
daily-brief/2026-11-11 (news) and feature/covid-test-negative-sequelae (epidemiology, PNAS long-COVID claims study). No overlap.

## Recent-pattern notes (for writer and editor)
- Last five headlines are all "<method/object> <verb> <result> on/than <case>" with a number or comparison: "Four-step TD learns a 19-state random walk faster than TD(0) or Monte Carlo", "Importance sampling values a policy from episodes another policy played", "PPO's greedy arrows outscore...", "Gymnasium's environment checker passes a grid with a backward slip". Build this headline differently.
- Recent deks open with a qualifying clause then a number ("Over the first 10 episodes, with each method at its best step size, ..."; "Scaling each return by ... makes the average unbiased, but on Sutton and Barto's one-state loop ..."). The "X, but on Sutton and Barto's ..." dek and "Of five ... runs, ..." are spent.
- Recurring phrasings: "at its best step size", "Sutton and Barto use this walk to compare", "the case the explanation fits worst". The takeaway of n-step-returns restated every section in sequence; don't make the takeaway a section-by-section recap.
- Recent section headings are full-sentence findings ("n = 4 has the lowest error at its own best step size", "Small n carries the outcome back slowly and large n needs a small step"). Fine as a form, but avoid the "X and Y" two-clause heading pattern repeating across the piece.
- Last lessons leaned almost wholly on Sutton and Barto as the source. That remains appropriate for a classic method; additionally link Tsitsiklis and Van Roy (1997) for linear TD convergence where the lesson states it.

## Production record
Researcher, writer and editor run as subagents on the orchestrator's model with effort xhigh, as the series requires. The writing-coach stage is satisfied by the pinned voice guide. No deviation.

## Decisions after research (orchestrator, 2026-11-11)
- The bound: cite eq. 9.14 as the result for discounted continuing tasks and say plainly it does not cover this undiscounted episodic walk. Report the walk's measured ratio of the TD fixed point's VE to the minimum VE from the lesson's own computation. Do not present 1/(1−γ) as this walk's bound and do not print the unsourced 122× figure.
- Attribution: Tsitsiklis and Van Roy (1997) is linked for linear TD's convergence and error bound in the discounted continuing case. Do not say they proved it for episodic tasks. Dayan (1992) may be named for the first general linear-feature convergence result as the book credits it.
- "Semi": the page may say the semi-gradient update is not true gradient descent (book p. 202). The stronger claim, that no fixed objective has it as its gradient, goes in only if the lesson shows it (expected update α(b − Aw) with A not symmetric on this walk, printed by the lesson's code); otherwise leave it out.
- Do not claim μ sets the accuracy across groups. Within a group, Monte Carlo's weight follows μ (book p. 204); that is the claim the evidence supports.
- The lopsided TD staircase around state 500 has no sourced explanation. If the writer reports it, either test an explanation by the series' removal-test rule or say in a sentence that it is not explained here.
- Figure 9.2-left's step size (0.0002) comes only from Sutton's code comment; attribute it so.
- Writer queries (01), decided: keep the https incompleteideas.net links the researcher opened, with the http address in the source note; do not switch to the unopened MIT Press page. Metadata order 12 is correct (n-step-returns is 11). The cut "not the gradient of any objective" derivation stays out; the page uses the book's sourced wording.
