# writer brief: expert-tools/verifiers-rl-environments (02)

Inputs:
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/writer/01/brief.md : the original brief, still in force
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/editor/01/editorial-review.md : the approved review. Its edits are settled work.
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/researcher/01/evidence.md : especially lines 137-175 and 545 (training keys)
- the article as the editor left it:
  /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/library/expert-tools/verifiers-rl-environments.html
Output: /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/writer/02/draft-handoff.md and the edited article
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/library/expert-tools/verifiers-rl-environments.html --series expert-tools --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

One required change. The commission names "how a training run consumes a
taskset" as part of the interface, and the article never shows the training
config. Add a short TOML listing for `prime train <config.toml> --volume
<name>` that trains nowcast-alfred, built only from keys the evidence records
(line 545): [[orchestrator.train.source]] with its
[orchestrator.train.source.env.taskset] id and taskset fields,
[orchestrator.train.source.env.agent.harness] id = "bash",
[orchestrator.train.source.env.agent.runtime] type, [orchestrator] batch_size,
[orchestrator.train] group_size. Show that the source's env block is the same
env block vf-eval reads in eval.toml, so one taskset config serves eval and
training. Caption: assembled from prime-rl at 782b84b and Prime's docs, not
executed. Do not use a runtime type the evidence does not name, and leave out
keys (model name, deployment GPUs, renderer) you cannot ground, or mark them.

Place it where it teaches best, likely beside the eval.toml listing or in the
warm-start section where the training run first appears. The word cap is
3000 including code and sources, and the article is at 2997. Cut at least as
many words as you add, from the prose that teaches least. Keep every owner
rule: no em-dashes, no semicolons, nothing about the owner or any employer or
job. Run ./nb stamp and the proof with links until BLOCK: 0.
