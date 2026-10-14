# editor brief: expert-tools/verifiers-rl-environments (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/editorial-direction.md : standing directions
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/commission.md : assignment, boundaries, recent-pattern notes, decisions
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/writer/01/brief.md : the exact writer brief
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/writing-coach/01/voice-guide.md : how the piece sounds
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/researcher/01/evidence.md and /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/researcher/01/nowcast_alfred/ : the claim set and the code that ran
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/writer/01/draft-handoff.md : the writer's handoff
- the article: /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/library/expert-tools/verifiers-rl-environments.html
Output: /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/library/expert-tools/verifiers-rl-environments.html --series expert-tools --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

This round's focus, from the orchestrator:
- The commission's contribution is that someone can build their own RL task
  with verifiers 0.4.0, interface first. Test whether the headline and dek
  carry that contribution. The draft headline and dek lead with the leak
  finding. Decide whether that is the piece's largest defensible claim or
  whether the interface is, and fix the display text either way.
- The word count is 2981 against a 3000 cap that counts code and sources.
  Any addition needs a matching cut. Run ./nb stamp after edits.
- Owner rules: zero em-dashes and zero semicolons in rendered text (the four
  semicolons in the Google Fonts URL in head are template chrome and stay).
  No information about the owner, an employer, a job or a work project.
- The writer flagged one inferred figure (batch size counting rollouts) and
  several marked judgments. Check each against the evidence.
- Every listing must match the code that ran. Recheck a sample line by line.
