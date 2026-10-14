# Draft handoff: expert-tools/verifiers-rl-environments (writer/02)

Original work: for one point-in-time nowcasting task, the piece ties each route by which the agent can reach the realized value to the verifiers 0.4.0 setting or design choice that closes it, with executed instances. It then uses the PAYEMS revision size against the naive error to choose the scoring vintage. That still holds after this revision.

## Required change resolved

- Training config added at the end of the warm-start section, right after "If the rewards already vary within groups, start with RL", where the training run first appears. The listing is `train.toml`, headed "run with prime train train.toml --volume <name>". It uses only keys from evidence line 545: `[orchestrator] batch_size = 64`, `[orchestrator.train] group_size = 8`, `[[orchestrator.train.source]]`, `...env.taskset` with `id = "nowcast-alfred"` and `closed_egress = true`, `...env.agent.harness id = "bash"`, `...env.agent.runtime type = "prime"`. The runtime type is `prime` (PrimeConfig, the default runtime named in the record) because the article's closing conditions call for an isolating runtime. Model, deployment GPUs and renderer are left out, and the caption says so. Both TOML listings parse with tomllib.
- Caption: assembled from prime-rl at 782b84b and Prime's docs, not executed. Batch and group sizes sit at Prime's floors. Cites 8, 15 and 7.
- A following paragraph says each training source's `env` field is the same verifiers env config that vf-eval reads from eval.toml's `[env]` tables, so one taskset config serves the baseline and the run. Training turns closed_egress back on and moves to prime. I rechecked this in the clone: prime-rl `orchestrator.py` 85-90, `EnvConfig.env: SerializeAsAny[vf.EnvConfig]`, with `name` optional (it defaults to the taskset id, so I left it out).
- Citation choice: I cite source 15 (end-to-end run page), not 22, for the `prime train ... --volume` command and the source env-block shape. Both appear in that page's Step 4. Citing 22 here would have put it ahead of 17 to 21 and forced a renumber. I added "and prime train command" to source 15's locator.
- Source 8 now points at the prime-rl tree root at 782b84b. Its title is "GitHub · prime-rl at 782b84b", and its locator adds `orchestrator.py` lines 85-90, 232 and 343, with rl.toml widened to 17-27. A reader who lands on the old examples/basic href could not reach orchestrator.py.
- Orientation: "the config that ran it" became "the eval config that ran it", and I added "The training config was not run, and nothing was trained", so "The listings come from" stays true.

## Cuts (107 words added, 108 cut net, 2997 to 2996)

- Upload cadence sentence ("Uploads, dev builds included, ran 1 to 5 a month in 2025 and 159 in July 2026"). Source 17 still carries the release-dates sentence.
- "Its signatures are best read from the installed files" and the repeated "as nowcast_alfred pins verifiers==0.4.0" in the drift closer. The first caption already states the pin.
- "whose orchestrator runs each environment in its own subprocess" from the prime-rl introduction.
- "and it requires an API key" from the FRED snapshot sentence.
- "Prime's own architecture notes call subprocess a debugging runtime." Source 11 is still cited in the drift section.
- The third stat (242k, Oct 2024). The noise paragraph already gives 12 against 254.
- "No real key appears" from the eval.toml caption, and "local" before "stub".
- R1-Zero sentence compressed to "DeepSeek-AI's R1-Zero skipped SFT and still learned to reason, with poor readability."
- "The rest is arithmetic."
- The one-task paragraph compressed to "A policy trained on one task learns its realized number. A method is learned only when many tasks, across series and as-of dates, share it."
- "guessing repeatedly in the wrong format" (the topic sentence and the quote both carry format).
- "such as closed_egress" and "config" from the num_rollouts paragraph. The new training paragraph now shows closed_egress in both configs.
- "Prime sets the group floor at 8, with 16 to 32 common, because" became "Prime's group floor exists because". The floor of 8 is already stated in the twelve-tasks paragraph.
- New caption tightened to "Model, deployment GPUs and renderer are omitted."

## Proof

`./nb stamp`: words 2996, sources 22, reading 13 min. `nb check` with links: BLOCK 0, WARN 0, PUBLISHABLE. Rendered text has zero em-dashes and zero semicolons. The one en dash is inside the quoted "10–80%" from Prime's page.

## Open questions

None for evidence. One judgment for the editor: the training listing sets `closed_egress = true` explicitly although it is the default, so that the contrast with eval.toml's `false` shows on the page.
