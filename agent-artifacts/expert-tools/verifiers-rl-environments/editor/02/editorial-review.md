# Editorial review: expert-tools/verifiers-rl-environments (editor/02)

## Correct

The thesis is unchanged from round 01. A working verifiers 0.4.0 environment
for payroll nowcasting is four classes and a few async hooks, and its reward is
not worth training on until four routes to the hidden answer are closed and a
baseline eval shows rewards that differ within groups. The round adds one claim
under it: a training run consumes the taskset through the same verifiers env
block that vf-eval reads, so one taskset config serves the baseline and the run.

The train.toml listing, key by key against evidence line 545 and prime-rl at
782b84b (the local clone, which `git ls-remote` shows is main HEAD on the
public remote):

- `[orchestrator] batch_size`: `OrchestratorConfig.batch_size`, orchestrator.py
  line 521, "Samples to train on per step". Held.
- `[orchestrator.train] group_size`: `TrainConfig.group_size`, line 343, which
  every source inherits unless it sets its own (`inherit_group_defaults`, lines
  292-330). The source's own field defaults to 1, so the inheritance is what
  makes 8 reach the source. 64 divides by 8, which the validator at lines
  680-683 requires. Held.
- `[[orchestrator.train.source]]` with no `name`: `EnvConfig.name` defaults to
  the taskset id (line 95). Held.
- `[orchestrator.train.source.env.taskset] id, closed_egress`,
  `...env.agent.harness id = "bash"`, `...env.agent.runtime type = "prime"`:
  `EnvConfig.env` is `SerializeAsAny[vf.EnvConfig]` resolved through
  `vf.resolve_env_field` (lines 85-105). vf-eval's own config declares the
  identical field and resolver in verifiers 0.4.0 (`configs/cli/eval.py` line
  76 and 133). I fed both listings' env blocks to the installed 0.4.0
  `resolve_env_config`. Each resolved to `SingleAgentEnvConfig` with a
  `NowcastConfig` taskset. eval.toml gave closed_egress False, the null harness
  and subprocess. train.toml gave closed_egress True, `BashHarnessConfig` and
  prime. `"prime"` is the `PrimeConfig` literal in `runtimes/prime.py` line 78,
  and the evidence names PrimeConfig as the default runtime. The writer's claim
  that one env config serves both held, and it held one step further than the
  writer tested, since the training env block validates against the installed
  package.
- The structure matches Prime's end-to-end run page, Step 4, key for key.

One break in the listing. Prime's end-to-end page says checkpointing is off by
default, "with no `[ckpt]` block nothing is written", and its Run Size
Guidelines repeat that without `[ckpt]` and `--volume` the run saves nothing.
The listing printed `--volume <name>` in its head and no `[ckpt]`, so a reader
who filled in the model and GPUs would train and keep no weights. `[ckpt]` is
in evidence line 545 and is a top-level field of `RLConfig` (rl.py line 202). I
added it to the listing and one caption sentence saying why.

Source 15's locator said the `prime train` command sits in Step 4. It sits in
Step 5 ("Launch the Training Run"). I corrected the locator and added the key
fields list and Run Size Guidelines, which carry the `[ckpt]` point.

The env-block sentence cited only source 8, which covers prime-rl's side. The
vf-eval side is `configs/cli/eval.py` line 76 in the package, so the sentence
now cites 3 as well, and source 3's locator widens from 82-120 to 76-120.

Source 8's new href. GitHub refuses this session through the proxy (403). The
commit is main HEAD of PrimeIntellect-ai/prime-rl on the public remote, so the
tree URL at that full SHA lands on the repository at the cited commit, and
from there a reader reaches every path in the locator. I rechecked the
locator's lines in the clone: orchestrator.py 85 opens `EnvConfig` and 89 is
the `env` field, 232 and 343 are the two `group_size` fields, and the three
README line 3s and wordle README line 71 say what the article cites them for.
The `nb check` link pass reported nothing against it.

The writer's judgment on `closed_egress = true` set explicitly at its default:
kept. The contrast with eval.toml's `false` is the point of the paragraph after
it.

The cuts, checked against the claims they served. The cadence sentence, the
API-key clause, the third stat and the subprocess-as-debugging-runtime
sentence each removed support for nothing the article still says. The last
one left source 11's locator pointing at `docs/v1/architecture.md` line 11,
which no sentence now uses, so I removed that path from the locator. The
compressed R1-Zero sentence still matches the R1 abstract (no SFT, reasoning
emerged, poor readability). The compressed group-floor sentence had become
"when every rollout in a group succeeds or fails", which is true of every
group. The source says all succeed or all fail. Fixed.

## Reads well

What went or changed:

- "A method is learned only when many tasks, across series and as-of dates,
  share it." "Across series and as-of dates" is the commission's working-design
  clause for Taskset.load, taken whole. The point is the article's own, so I
  rewrote it: "only when it has to serve many series and as-of dates".
- "DeepSeek-AI's R1-Zero" right after "DeepSeek-AI fine-tuned R1" repeated the
  name. Now "R1-Zero".
- "The reverse-text example also starts with SFT, and the alphabet-sort example
  runs RL without it" trimmed to the two example names, since the sentence
  before names them as Prime's examples.
- "Each training source's env field is the same verifiers env config that
  vf-eval reads" lost its "that".

The new paragraph after train.toml passes the placeholder test. It names the
field, the two configs and the two settings that change. I left the one-line
maintenance paragraph. The writer cut its second sentence for room, and the
judgment still stands on the drift table above it.

## The experience

The commission's interface list ended at the CLI. The training run now
appears where the warm-start decision sends the reader ("start with RL"), as a
config whose env block the reader has already seen in eval.toml. The page now
shows the whole path from Taskset to `prime train`, and a reader who copies the
listing keeps the weights. The section heading still names only the warm start.
I left it, since the listing follows from that decision.

Beyond its sources, the piece still ties each route to the hidden answer to
the verifiers setting that closes it, with executed instances, and picks the
scoring vintage from the revision size against the naive miss. The training
listing adds a smaller thing no single source shows. eval.toml and train.toml
side by side make the same env block change in two settings and nothing else.
The handoff's original-work sentence agrees.

## Edits

- train.toml listing: added `[ckpt]` as the first table.
- train.toml caption: added "Without [ckpt] the volume gets no weights."
- Env-block paragraph: "Each training source's ... that vf-eval reads" became "A training source's ... vf-eval reads", and the sentence now cites 3 before 8.
- Group-floor sentence: "when every rollout in a group succeeds or fails" became "when a group's rollouts all succeed or all fail,".
- One-task paragraph: "only when many tasks, across series and as-of dates, share it" became "only when it has to serve many series and as-of dates".
- Warm start: "The reverse-text example also starts with SFT, and the alphabet-sort example runs RL without it" became "Reverse-text also starts with SFT, and alphabet-sort runs RL without it".
- Warm start: "DeepSeek-AI's R1-Zero" became "R1-Zero".
- Source 3 locator: `configs/cli/eval.py 82-120` became `76-120`.
- Source 11 locator: removed `docs/v1/architecture.md line 11`.
- Source 15 locator: now "Step 2 Tip, Step 4 config listing and key fields, Step 5 prime train command, Run Size Guidelines".
- Proof: `nb stamp` gives words 2999, sources 22, reading 13 min. `nb check --check-links` gives BLOCK 0, WARN 0, PUBLISHABLE. Rendered text, meta and title have zero em-dashes and zero semicolons. The one en dash is inside Prime's quoted "10–80%". Nothing in the piece concerns the owner, an employer, a job or a work project.

## Decision

approve. The training listing matches prime-rl at 782b84b and its env block
validates against verifiers 0.4.0. The one break, a run that would save no
weights, was fixed inside the record.
