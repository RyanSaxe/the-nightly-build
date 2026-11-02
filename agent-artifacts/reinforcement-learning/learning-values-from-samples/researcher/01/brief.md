# researcher brief: reinforcement-learning/learning-values-from-samples (01)

Inputs:
- editorial-direction.md (one dir up): the full standing editorial standard for this article.
- ../../commission.md: what this lesson teaches and its boundaries.
- Lesson 1 and lesson 2 of this course, already published, readable with
  `nb history --show reinforcement-learning/environments-and-the-rl-problem` and
  `nb history --show reinforcement-learning/finding-optimal-policies` from the repo root
  (the `nb` executable is at /home/user/the-nightly-build/nb).
Output: evidence.md in this directory (/home/user/the-nightly-build/.nb-work/reinforcement-learning/learning-values-from-samples/agent-artifacts/reinforcement-learning/learning-values-from-samples/researcher/01/evidence.md)

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

This is a teaching lesson, not a news piece, so the evidence record is mostly
authoritative definitions, theorems and one real-world case, not breaking events.
Establish, from the owning documents:

1. Monte Carlo prediction for a fixed policy: first-visit and every-visit
   estimators, that both converge to v_pi, the incremental running-mean update,
   and that MC is unbiased and high-variance and needs complete episodes. Owning
   source: Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed.,
   chapter 5. Record exact section/page locators for each claim.
2. TD(0) prediction: the update V(s) <- V(s) + alpha[R + gamma V(s') - V(s)], the
   TD error, that it bootstraps and updates online, and the bias/variance and
   convergence comparison with MC. Owning source: Sutton & Barto chapter 6
   (including the MC-vs-TD discussion and the example comparing them). Exact
   locators.
3. One real-world case for the "Why this matters" opener, with a firsthand source:
   prefer Tesauro's TD-Gammon (Gerald Tesauro, "Temporal Difference Learning and
   TD-Gammon," *Communications of the ACM* 38(3), 1995) — get a specific checkable
   claim (e.g. that it trained by TD on self-play and reached strong play), with a
   locator. If TD-Gammon's text is hard to reach, the dopamine/TD-error result
   (Schultz, Dayan, Montague, "A Neural Substrate of Prediction and Reward,"
   *Science* 275, 1997) is an acceptable alternative. Record whichever you can
   confirm firsthand; note if you could not open one.
4. The papers that introduced the key ideas, for the "Go deeper" band: Sutton's
   1988 TD paper ("Learning to Predict by the Methods of Temporal Differences,"
   *Machine Learning* 3) and the MC/TD chapters above. Say which part to read and
   why.

Record every source with the Sources / Numbers / Limits / Source assets /
Discarded sections the researcher skill specifies. For a teaching piece the
"Numbers" are the few quantities the lesson will state from the code run — but the
code is the writer's to run, so here just note that the running numbers (RMS
error, v(13) estimates, episode counts) come from the committed script, not from a
secondary source, and flag that as a Limit the writer fills by running code.
Classify each source primary/secondary with the reason. Confirm every URL resolves
to the document's own page (a stable publisher or author page for the papers; for
Sutton & Barto, the authors' freely available 2nd-edition PDF is acceptable and
preferred as the citeable location). Report the path and the record's most
important limit.
