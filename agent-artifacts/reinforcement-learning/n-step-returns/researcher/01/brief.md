# researcher brief: reinforcement-learning/n-step-returns (01)

Inputs:
- ../../editorial-direction.md — standing directions
- ../../commission.md — topic, idea, case and boundaries
- ../../writing-coach/01/voice-guide.md — the series voice (read only for register)
Output: researcher/01/evidence.md (beside this brief)

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

The page will use only a few citations. Gather what it needs:

1. Sutton and Barto, 2nd ed. (http://incompleteideas.net/book/RLbook2020.pdf):
   Section 7.1 in full — the n-step return definition (eq. 7.1), the n-step TD
   update (7.2), the error-reduction property (7.3), the pseudocode box and its
   τ bookkeeping, Example 7.1 and Figure 7.2 (19-state random walk, its setup,
   the n and α values plotted, what the text says about which n is best and
   why). Record printed page numbers. Section 7.2 (n-step SARSA) only enough for
   one pointer sentence. Bibliographical remarks for Chapter 7: who introduced
   n-step returns.
2. Watkins (1989) thesis, "Learning from Delayed Rewards": confirm whether it
   introduces corrected n-step truncated returns, with chapter/page, and a
   stable URL if one exists. Cite only what you open.
3. The random walk's exact values (closed form) and how S&B measure error in
   Fig. 7.2 (RMS over states, averaged over the first 10 episodes and 100
   runs). The writer will rerun it; the record should let the editor check the
   writer's setup matches.
4. Anything credible that complicates "intermediate n is best": e.g. dependence
   on α, on the chain length, on episode count; any S&B exercise (7.3) that asks
   why a smaller walk would change the best n. Record contradictions.
5. For Go deeper: one or two readable pointers (S&B 7.2/7.3 sections, Chapter
   12's λ-return as the averaging of n-step returns, a paper like Hernandez-
   Garcia & Sutton 2019 "Understanding multi-step deep RL" or De Asis et al.
   2018 "Multi-step RL: a unifying algorithm") — confirm each exists, give the
   section worth reading.

Keep the record proportionate: a lesson on a classic method cites little.
