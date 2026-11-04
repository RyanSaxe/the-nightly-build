# researcher brief: reinforcement-learning/epsilon-greedy-exploration (01)

Inputs:
- ../../editorial-direction.md (the generated editorial direction)
- ../../commission.md (the assignment and its boundaries)

Output: researcher/01/evidence.md (beside this brief)

Work from these inputs. Do not tour the repository, the Git history or the archive for background.
Where something you need is missing, ask me.

A lesson on a classic method cites little. Gather only what the page will use:
- Sutton and Barto, 2nd ed., Section 5.4 (on-policy MC control without exploring starts, the
  epsilon-soft box and the policy improvement argument for epsilon-soft policies), and where
  epsilon-greedy is first defined (Section 2.2). Record exact page numbers and equation numbers.
- The paper that introduced the GLIE conditions and convergence of on-policy control with decaying
  exploration (Singh, Jaakkola, Littman and Szepesvari, 2000), with the section that states GLIE.
- Any primary source that settles whether first-visit on-policy MC control with a fixed epsilon is
  proven to converge to the best epsilon-soft policy, and under what conditions. If nothing proves
  it, say so in Limits.
- The earliest-use origin of the term "epsilon-greedy" only if a clear primary exists (Watkins 1989
  thesis is a candidate); otherwise record it as not established.
You may read the course's published lessons with `nb history --show reinforcement-learning/<slug>`
to record exactly what they taught and their code file names; that is the one repository read you
need. Record every URL as the document's own page.
