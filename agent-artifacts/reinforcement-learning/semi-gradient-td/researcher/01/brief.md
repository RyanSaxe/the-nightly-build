# researcher brief: reinforcement-learning/semi-gradient-td (01)

Inputs:
- ../../editorial-direction.md — standing directions, including the series prompt
- ../../commission.md — topic, the one idea, case, boundaries
Output: researcher/01/evidence.md (beside this brief)

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Ask for only what the page will use: a classic-method lesson cites little.
Needed: Sutton and Barto 2nd ed. Chapter 9 passages with page numbers — the VE
objective (eq. 9.1), the SGD/gradient MC update (9.4-9.7), semi-gradient TD(0)
and why it is "semi" (Section 9.3), Example 9.1's exact rules (jump range,
termination rule for out-of-range jumps, start state, aggregation), the linear
TD fixed point and bound (Section 9.4, eqs. 9.12-9.14), and Figure 9.1/9.2
descriptions with step sizes and episode counts used. Find the paper that
introduced linear TD's convergence result (Tsitsiklis and Van Roy 1997) and
record the section/theorem. Locate Sutton's own code for Example 9.1 if it exists
(as the previous lesson used his Lisp for Example 7.1) and record its exact
conventions. Record 2-4 Go-deeper candidates with the exact part to read.
