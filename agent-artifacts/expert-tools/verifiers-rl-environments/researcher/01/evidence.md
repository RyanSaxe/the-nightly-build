# Evidence record: expert-tools/verifiers-rl-environments (researcher 01)

The installed release is verifiers 0.4.0 (PyPI, uploaded 2026-10-12, MIT), read directly in site-packages and run locally. The owner's API leads hold up with five corrections that change listings: reward and metric methods must be `async def` (a plain `def` raises TypeError), the `task` parameter a reward receives is the `TaskData` row and not the `Task`, `network_allow=[]` means "framework routes only" and is refused outright on the subprocess runtime, `environments/web_search_interception` uses `@vf.stop` and not `@vf.intercept`, and `vf-init` (with `-T`/`-H`) exists in 0.4.0 but was deleted on main on 2026-10-14 and is absent from the 0.4.1.dev18 wheel already on PyPI. A minimal nowcasting environment built on real ALFRED vintages imports, loads, stages its point-in-time catalog, serves an MCP toolset, round-trips typed per-rollout state and scores end to end under `vf-eval` with the `null` harness, the subprocess runtime and a canned local model endpoint. Nothing was trained and no real model was called. The evidence is thin on four things: closed egress could not be executed locally (no Docker daemon, no Prime account), Prime publishes no per-rollout cost figure, Prime's warm-start guidance is example READMEs and not a stated rule, and the reward-noise argument rests on one series over twelve months.

## Sources

```text
URL:         https://pypi.org/project/verifiers/0.4.0/  (installed with `uv pip install verifiers` into a scratch venv, Python 3.13)
Kind:        primary. The package Prime Intellect publishes owns its own API.
Establishes: every signature in Appendix A, firsthand, read at site-packages/verifiers/v1/...
Paraphrase:  The package root carries only __version__ and a `v1` subpackage. The whole stack lives in verifiers.v1. No SingleTurnEnv, ToolEnv, MultiTurnEnv, Rubric, Environment or load_environment exists on either `verifiers` or `verifiers.v1` (checked with hasattr). Console scripts: vf-debug, vf-eval, vf-gepa, vf-init, vf-replay, vf-validate (verifiers-0.4.0.dist-info/entry_points.txt).
Locators:    verifiers/__init__.py:1 (docstring), verifiers/v1/__init__.py:1-393 (exports), entry_points.txt
Quote:       none needed. The root docstring (verifiers/__init__.py:1) names `import verifiers.v1 as vf` as the import.
```

```text
URL:         https://github.com/PrimeIntellect-ai/verifiers at tag v0.4.0 = commit 6e69354ffe1b445603b493b722d0ecffbca6686d (2026-10-12). Main read at 269ff7b4725958908437324ece8c7e96c72356df (2026-10-14).
Kind:        primary. Prime's own repository, docs and example environments.
Establishes: the v1 docs as shipped with 0.4.0, the example environments, tag dates, the v0 removal and the post-release vf-init removal.
Paraphrase:  docs/overview.md says v1 is what environments should target and that the legacy v0 stack has been removed. docs/v1/tasksets.md documents vf-init, the Task/TaskData/Taskset split, views, INFINITE, toolsets and TOML-plugged hooks. docs/v1/architecture.md says subprocess is for debugging and that the interception server can rewrite tool responses or server-side web search results to block reward hacks. docs/v1/env.md documents an isolated-verifier env that scores in a fresh box. docs/v1/evaluation.md documents vf-eval, TOML configs and that push is on by default. Commit 66a606493 (2026-08-31, PR #2480) "feat!: remove the legacy (v0) stack". Commit c2b706ca6 (2026-10-14, PR #2843) "remove vf-init": deletes the console script, cli/init.py and configs/cli/init.py and the scaffolding docs.
Locators:    docs/overview.md:7. docs/v1/tasksets.md:5-25 (vf-init), 39-73 (addition example), 113-145 (identity, select), 147-169 (infinite), 171-201 (toolsets), 268-290 (TOML hooks). docs/v1/architecture.md:11 (subprocess), 19-27 (interception). docs/v1/env.md:23-86 (isolated verifier). docs/v1/evaluation.md:11-28 (TOML), 49-52 (push). docs/v1/getting_started.md:12-16. environments/scratchpad, wiki_search, web_search_interception, bash_interception, interception (all at v0.4.0).
Quote:       none needed
```

```text
URL:         https://github.com/PrimeIntellect-ai/verifiers/tree/v0.4.0/environments/web_search_interception
Kind:        primary.
Establishes: what this example actually does, which contradicts owner lead 4.
Paraphrase:  WebSearchInterceptionTask has one `@vf.stop` method `stop_on_result(self, response: vf.Response) -> bool` that reads url_citation annotations on the buffered provider response and returns True when a cited URL contains "openai.com". Its reward is `float(trace.stop_condition == "stop_on_result")`. There is no @vf.intercept in the file and git history shows it never had one (added 96f146874, 2026-08-11). README: "uses `@vf.stop` when the search material contains a chosen phrase".
Locators:    web_search_interception/taskset.py:6-22
Quote:       none needed
```

```text
URL:         https://github.com/PrimeIntellect-ai/verifiers/tree/v0.4.0/environments/bash_interception and .../environments/interception
Kind:        primary.
Establishes: the real @vf.intercept examples.
Paraphrase:  bash_interception: `@vf.stop def stop_bash(self, response: vf.Response) -> bool` blocks a proposed bash call before the harness sees it. `@vf.intercept def rewrite_git(self, request: vf.Request) -> vf.Request | None` replaces the pending tool result with "This request is blocked. You should answer with something." so the command never runs and the rollout continues. interception: `@vf.intercept(priority=10)` deterministic rewrite of a Response, an async judge-based intercept, and a metric-only intercept that returns None. A stop's function name becomes trace.stop_condition.
Locators:    bash_interception/taskset.py:24-76. interception/taskset.py:99-148
Quote:       none needed
```

```text
URL:         https://github.com/PrimeIntellect-ai/verifiers/tree/v0.4.0/environments/scratchpad and .../wiki_search
Kind:        primary.
Establishes: toolset patterns owner lead 5 named.
Paraphrase:  scratchpad: `class ScratchpadState(vf.State): slot: str = ""`, `class ScratchpadToolset(vf.Toolset[ScratchpadToolsetConfig, ScratchpadState])` with TOOL_PREFIX "scratchpad", an async setup() paid once per worker and a @vf.tool that writes self.state. Declared on Taskset.toolsets, so one server process per worker, with per-rollout isolation through self.state. The task is `vf.Task[ScratchpadTaskData, ScratchpadState]` and caps turns with `@vf.stop async def done(self, trace) -> bool: return trace.num_turns >= 4`. wiki_search: `WikiSearchToolset(vf.Toolset[vf.SharedToolsetConfig])`, TOOL_PREFIX "wiki", builds a chroma index in setup(), tools search_pages/view_sections/read_section, model sees wiki_search_pages etc. Grading is a plugged judge in WikiSearchTaskConfig.judges.
Locators:    scratchpad/taskset.py:30-65, scratchpad/servers/scratchpad.py:16-41. wiki_search/taskset.py:27-66, wiki_search/servers/wiki.py:72-160
Quote:       none needed
```

```text
URL:         https://pypi.org/pypi/verifiers/json (rendered history at https://pypi.org/project/verifiers/#history)
Kind:        primary. The registry record of uploads.
Establishes: release dates and cadence.
Paraphrase:  606 uploads with files. Final releases: 0.0.0 2025-01-28, 0.1.0 2025-06-05 ... 0.1.14 2026-05-07, 0.2.0 2026-07-10, 0.2.1 2026-07-20, 0.3.0 2026-08-07, 0.3.1 2026-08-24, 0.4.0 2026-10-12. Between 0.3.1 and 0.4.0 there are dev builds up to 0.3.2.dev210 (2026-10-12). After 0.4.0: 0.4.1.dev1 (2026-10-13) to 0.4.1.dev18 (2026-10-14). requires_python ">=3.11,<3.15". Monthly upload counts in Numbers.
Locators:    JSON fields releases[*][0].upload_time
Quote:       none needed
```

```text
URL:         https://files.pythonhosted.org/packages/4e/1e/374bb8b48e79a156764c7ece7584db7e72106852726dbd3542e410eb1cd6/verifiers-0.4.1.dev18-py3-none-any.whl
Kind:        primary.
Establishes: that the next release line already lacks vf-init.
Paraphrase:  entry_points.txt lists vf-debug, vf-eval, vf-gepa, vf-replay, vf-validate. No vf-init. No verifiers/v1/cli/init.py in the wheel. Uploaded 2026-10-14T21:22:17.
Locators:    verifiers-0.4.1.dev18.dist-info/entry_points.txt
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/hosted-training/environment-model
Kind:        primary. Prime's own docs site.
Establishes: docs-site drift. This page still teaches the v0 API.
Paraphrase:  Describes environments as dataset + harness + rubric, lists "Legacy (Verifiers v0)" and "Verifiers v1" styles as both supported by Hosted Training, then documents the v0 type hierarchy (Environment, MultiTurnEnv, SingleTurnEnv, ToolEnv, StatefulToolEnv) with `import verifiers as vf`, `vf.SingleTurnEnv(..., rubric=vf.Rubric(funcs=[...]))`, `vf.ToolEnv(...)` and `def load_environment(...)`. It calls the harness "the built-in `default` harness, or an agent harness such as `bash` or `codex`", which treats default and bash as two different harnesses. Neither import works in 0.4.0.
Locators:    "Legacy and Verifiers v1 environment configs" section, then "The Type Hierarchy" (SingleTurnEnv, MultiTurnEnv, ToolEnv, StatefulToolEnv subsections, "Entry point")
Quote:       "the built-in `default` harness, or an agent harness such as `bash` or `codex`"
```

```text
URL:         https://docs.primeintellect.ai/guides/recipes
Kind:        primary.
Establishes: a second v0 page, plus Prime's suggested starting configs.
Paraphrase:  Every recipe's code uses `import verifiers as vf`, `def load_environment(...) -> vf.Environment`, `vf.SingleTurnEnv`, `vf.Rubric`, a `vf.MultiTurnEnv` subclass and `vf.ToolEnv`. Suggested starting points: math, 4B-class instruct, max_steps 200, batch_size 256, group_size 8, max_completion_tokens 1024. Code, 30B-A3B-class, 300/256/16/2048. Game, 4B-class, 100/128/8/256. Tool use, 30B-A3B-class, 200/256/16/1024. Mixed, flagship MoE, 500/512/16/2048.
Locators:    "Math reasoning" (Environment type: SingleTurnEnv with MathRubric), "Code generation", "Multi-turn games" (MultiTurnEnv), "Tool use" (ToolEnv or MCPEnv), each "Suggested starting point" line
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/guides/search-agents
Kind:        primary.
Establishes: a third v0 page.
Paraphrase:  The patent-search environment "is implemented using the verifiers library as a ToolEnv" with `from verifiers import ToolEnv` and `class PatentEnv(ToolEnv)`. It links github.com/willccbb/verifiers.
Locators:    patent search environment section
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/tutorials-environments/create
Kind:        primary.
Establishes: Prime has flagged at least one v0 page itself.
Paraphrase:  Banner says the page describes the verifiers v0 workflow (load_environment, vf-eval), v0 is deprecated and listed as Legacy on the Hub, build on v1 instead, and `prime env push` works the same way.
Locators:    Note at top of page
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/tutorials-environments/environments
Kind:        primary.
Establishes: Environments Hub description and v1 migration status.
Paraphrase:  "The Hub is moving to verifiers v1." v0 environments carry a Legacy tag and still install, but v0 is being retired. New environments should target v1. `prime env push` lists a push as v1 or legacy from the package's verifiers requirement, `--runtime v0|v1` overrides it. Environment Actions (automated checks on push) have been removed. The Hub is a community registry that doubles as a Python package registry. Environments declare dependencies in pyproject.toml and ship as wheels. It links a v0-to-v1 migration guide at skills/create-environments/SKILL.md on verifiers main, a path that no longer exists on main after PR #2843 (skills/ now holds only release at 269ff7b).
Locators:    top Note, "About", "Motivation"
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/platform-overview
Kind:        primary.
Establishes: Prime's own account of the stack.
Paraphrase:  Prime Intellect describes itself as "an open research platform for post-training" that unifies the Environments Hub, Hosted Training and Hosted Evaluations. Model Factory is the training side, built on open-source prime-rl, covering Hosted Training (on-demand, billed per GPU-hour, full-parameter RL and SFT) and dedicated clusters. The earlier shared LoRA service is retired. prime-rl runs trainer, inference and orchestrator. verifiers is "the environment framework".
Locators:    intro, "Core Concepts", "Model Factory", "Architecture", "Key Libraries"
Quote:       "Prime Intellect is an open research platform for post-training."
```

```text
URL:         https://docs.primeintellect.ai/prime-rl/overview
Kind:        primary.
Establishes: what prime-rl is and how it consumes verifiers environments.
Paraphrase:  prime-rl is a framework for large-scale asynchronous RL of LLMs, three processes: vLLM inference, a CPU orchestrator that "owns the data plane across many verifiers training and eval environments" with each env in an isolated subprocess and a pool of env workers, and an FSDP2 trainer. Quick run trains an SFT-warmed Qwen3-0.6B on reverse-text.
Locators:    "Architecture", "Quick Run"
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/prime-rl/training
Kind:        primary.
Establishes: Prime's group-size and batch-size guidance.
Paraphrase:  Rules of thumb: batch size at least 64 (64 is the floor, 128 to 512 for quick ablations, production often 1024+). Group size at least 8, 16 to 32 common, because if all rollouts in a group succeed or all fail "the within-group advantage collapses to zero and the trainer learns nothing from that task". orchestrator.train.group_size is "Rollouts generated per task". max_off_policy_steps default 8. GRPO is the default algorithm. Also documents an `sft` entrypoint and describes the workflow as "SFT -> RL -> SFT".
Locators:    "Rules of Thumb" (Batch size, Group size bullets), "Useful Knobs" table, "SFT Trainer"
Quote:       "if all rollouts in a group succeed or all fail, the within-group advantage collapses to zero and the trainer learns nothing from that task"
```

```text
URL:         https://docs.primeintellect.ai/prime-rl/algorithms
Kind:        primary.
Establishes: what group_size=1 does.
Paraphrase:  A group-relative algorithm with group_size = 1 produces all-zero advantages. The empty batch is caught at runtime (orchestrator warns and skips), not at config time. max_rl normalizes the centered reward by the group mean. rae needs no sibling rollouts.
Locators:    paragraph after the algorithm table ("Component compatibility is validated at config time ...")
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/hosted-training/getting-started
Kind:        primary.
Establishes: the Hosted Training config shape and command.
Paraphrase:  On-demand training is beta, request access. `prime train configs/full-ft.toml --volume research`. Checkpointing off by default, without a volume and a [ckpt] block a run leaves no model. Example config uses model PrimeIntellect/Qwen3-0.6B-Reverse-Text-SFT, [deployment] num_train_gpus/num_infer_gpus, [orchestrator] batch_size = 64 and group_size = 8, [[orchestrator.train.source]] name, [orchestrator.train.source.env.taskset] id, [orchestrator.train.source.env.agent.harness] id = "null", [orchestrator.train.source.env.agent.runtime] type = "subprocess", [orchestrator.renderer] name = "prime-qwen3".
Locators:    "4. Launch a run"
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/hosted-training/end-to-end-run
Kind:        primary.
Establishes: Prime still documents harness id "default" for training, the baseline-reward band, and a v0-era output layout.
Paraphrase:  Config sets [orchestrator.train.source.env.agent.harness] id = "default" and says bare harness ids such as "default" resolve through the installed runtime package. Tip: a good training environment has a baseline reward between roughly 10 and 80 percent. 0 percent after many attempts means too hard, 80 percent or more means too easy. group_size sits under [orchestrator.train] here. The baseline step says results land in outputs/evals/ as metadata.json and results.jsonl, which is not what vf-eval 0.4.0 writes (it writes <output_dir>/<run>/traces.jsonl plus configs/ and logs/).
Locators:    "Step 2: Run a Baseline Evaluation" (Tip), "Step 4" config listing and "key fields" list, sentence beginning "Taskset and harness ids can be bare runtime ids"
Quote:       "A good training environment should have a baseline reward between roughly 10–80%."
```

```text
URL:         https://github.com/PrimeIntellect-ai/prime-rl at commit 782b84be89d28cd9d3903803d446a01301ccd414 (2026-10-14)
Kind:        primary.
Establishes: SFT warm start in Prime's own examples, and the canonical group_size key.
Paraphrase:  examples/basic/wordle/README.md: baseline Qwen3-1.7B scored an average reward of about 0.2 over 20x3 rollouts, mostly from format and partial rewards, with a 0 percent win rate, "repeatedly submitting guesses in the wrong format", so they run an SFT warmup "to learn the format of the environment" on willcb/V3-wordle before multi-turn RL (100 steps, 32x16 rollouts, batch 512, context 4096). examples/basic/reverse-text/README.md: "SFT warmup to learn the skill of text reversal" then a quick RL run. docs list alphabet-sort as "Multi-turn LoRA RL without SFT warmup". Every examples/basic/*/rl.toml puts group_size under [orchestrator.train]. In packages/prime-rl-configs/src/prime_rl/configs/orchestrator.py, OrchestratorConfig (line 469) has batch_size but no group_size field. group_size lives on TrainConfig (line 343), TrainSourceConfig (232) and eval configs. Configs subclass pydantic_config.BaseConfig, whose model_config is {'extra': 'forbid'}.
Locators:    examples/basic/wordle/README.md:3, 35, 71. examples/basic/reverse-text/README.md:3. examples/basic/wordle/rl.toml:17-27. orchestrator.py:232, 343, 469-521, 678-683. prime_rl/utils/config.py:6
Quote:       wordle README:35 "Let's do some SFT warmup to get the model to learn the format of the environment."
```

```text
URL:         https://docs.primeintellect.ai/sandboxes/overview
Kind:        primary.
Establishes: the only published sandbox cost figure.
Paraphrase:  Sandboxes bill while running. Rates valid through December 22, 2026: CPU $0.02 per vCPU-hour, memory $0.0125 per GiB-hour, disk $0.0002 per GiB-hour. Example: 1 vCPU, 2 GiB RAM, 5 GiB disk costs $0.046 per hour. Image and checkpoint storage $0.10 per GiB-month. Account caps include 4,096 total vCPUs and 102,400 sandbox creations per hour.
Locators:    "Pricing" section, limits tables
Quote:       none needed
```

```text
URL:         https://docs.primeintellect.ai/hosted-training/billing and https://docs.primeintellect.ai/traces/pricing-and-settings
Kind:        primary.
Establishes: training and trace charges.
Paraphrase:  Hosted Training bills per GPU-hour at a rate shown only by `prime train models`, prorated to the second, meter from pods Ready to terminal state. Queueing and image pull are not billed. Traces: $1 per GiB ingested, $0.10 per GiB-month stored, separate from training.
Locators:    billing "What gets billed". traces pricing table
Quote:       none needed
```

```text
URL:         https://fred.stlouisfed.org/docs/api/fred/series_observations.html
Kind:        primary. The St. Louis Fed owns the FRED/ALFRED API.
Establishes: the real-time parameters and output types.
Paraphrase:  realtime_start and realtime_end are optional YYYY-MM-DD dates defaulting to today. output_type 1 = Observations by Real-Time Period, 2 = by Vintage Date all observations, 3 = by Vintage Date new and revised only, 4 = Observations, Initial Release Only. vintage_dates is a comma-separated list of dates that downloads data as it existed on those dates, used instead of a real-time period, capped at 2000 vintage dates for json. An api_key is required. A live request without one returned HTTP 400 "Variable api_key is not set."
Locators:    "Parameters": realtime_start, realtime_end, output_type, vintage_dates
Quote:       "4 = Observations, Initial Release Only"
```

```text
URL:         https://fred.stlouisfed.org/docs/api/fred/realtime_period.html
Kind:        primary.
Establishes: what "as of" means in ALFRED.
Paraphrase:  The real-time period marks when facts were true or when information was known until it changed. Observation values can be revised. The default real-time period is today ("FRED mode"). ALFRED users change it to retrieve what was known in a past period. The period is closed at both ends.
Locators:    "Introduction"
Quote:       "The real-time period marks when facts were true or when information was known until it changed."
```

```text
URL:         https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=PAYEMS&vintage_date=YYYY-MM-DD
Kind:        primary data (St. Louis Fed). Recorded deliberately: it is the endpoint the example environment's build script fetched, without an API key.
Establishes: the PAYEMS revision series in Numbers and the point-in-time snapshots in the fixture.
Paraphrase:  Returns one CSV column named <SERIES>_<served vintage>, the vintage in force on the requested date. Vintage 2024-02-01 ends at 2023-12-01 = 157232. Vintage 2024-02-02 adds 2024-01-01 = 157700 and revises December to 157347. Requests on 2026-10-13 and 2026-10-14 were served vintages labelled 20261012 and 20261013.
Locators:    CSV header and rows. Fetched 2026-10-14
Quote:       none needed
```

```text
URL:         https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/real-time-data-set-for-macroeconomists
Kind:        primary. The Philadelphia Fed owns the dataset.
Establishes: an independent point-in-time archive and its first/second/third-release product.
Paraphrase:  The dataset "consists of vintages, or snapshots, of time series of major macroeconomic variables" for verifying results, analysing policy or forecasting, updated at the end of each month. Downloads offer complete vintage history, or only first-, second- and third-release values for selected variables. Preferred citation: Croushore and Stark, "A Real-Time Data Set for Macroeconomists," Journal of Econometrics 105 (November 2001), pp. 111-30.
Locators:    page body under "Real-Time Data Set for Macroeconomists", "Historical Data", "Background Reading"
Quote:       "The real-time data set consists of vintages, or snapshots, of time series of major macroeconomic variables."
```

```text
URL:         https://arxiv.org/abs/2501.12948 (read at https://arxiv.org/html/2501.12948v1)
Kind:        primary. DeepSeek-AI's own report.
Establishes: a published rationale for supervised data before RL, and the counterexample.
Paraphrase:  Section 2.3.1 Cold Start: to prevent the early unstable cold-start phase of RL from the base model, DeepSeek-R1 fine-tunes on thousands of long chain-of-thought examples as the initial RL actor, with readability as a named advantage. The same paper's DeepSeek-R1-Zero applies RL to the base model with no SFT and reports strong reasoning, at the cost of poor readability and language mixing (abstract).
Locators:    abstract, section 2.2 (R1-Zero), section 2.3.1
Quote:       "to prevent the early unstable cold start phase of RL training from the base model, for DeepSeek-R1 we construct and collect a small amount of long CoT data to fine-tune the model as the initial RL actor"
```

## Contradictions

Against the owner's leads:

- Lead 4. `environments/web_search_interception` does not use `@vf.intercept`. It is a `@vf.stop` on a typed `vf.Response` that ends the rollout when a native web-search citation contains a blocked domain, and its reward checks `trace.stop_condition == "stop_on_result"`. The intercept examples are `bash_interception` (rewrites a pending tool result so a command never runs) and `interception`. The docs architecture page does say the interception server can rewrite web search results to block reward hacks, which is probably where the lead came from.
- Lead 6. `TaskData(network_allow=[])` is not "no egress". `NetworkPolicyConfig` turns an empty allowlist into allow=[], block=["*"], described as "framework-only" (configs/runtime.py:57-77). The interception endpoint and the MCP tool URLs stay reachable (rollout.py:322 passes them to prepare_execution). It also requires a policy-capable runtime (docker, podman, prime, modal, e2b). On subprocess the rollout fails with "task 0 requires a network policy, but the subprocess runtime does not support framework-aware policies" (utils/compile.py:45-55). Executed: vf-debug crashed with that ValueError, and vf-eval recorded it as an EnvError on the episode while still exiting 0. The policy is applied after task setup (rollout.py:262-322), so Task.setup itself runs with open egress.
- Lead 3. Reward and metric methods must be coroutines. `invoke_all` passes each result to `asyncio.gather` (utils/decorators.py:41-45), and a sync function's float raises "TypeError: An asyncio.Future, a coroutine or an awaitable is required" (executed). Stops and intercepts may be sync or async (session.py:66-69). The `task` parameter is `self.data`, the TaskData row (task.py:227), not the Task.
- Lead 7. vf-init with -T/-H is real in 0.4.0, but PR #2843 removed it on 2026-10-14 and the 0.4.1.dev18 wheel on PyPI has no vf-init. A listing that tells readers to run vf-init is correct for 0.4.0 only. vf-eval 0.4.0 also prints on every run: "vf-eval will be deprecated - move to prime-rl's `uv run eval`" (cli/eval/hint.py:1-5).
- Lead 7, training config. Hosted Training getting-started puts `group_size = 8` under `[orchestrator]`. Every prime-rl example and the end-to-end page put it under `[orchestrator.train]`, OrchestratorConfig has no group_size field, and the config base forbids extra keys. The getting-started key is probably rejected. Not executed, no Hosted Training access.
- Lead 2. TaskData has more fields than listed (idx, id, name, description, image, workdir, agent_user, skills, artifacts, artifact_max_bytes). `Taskset` also has `select(SelectConfig)`.

Within Prime's documentation:

- docs.primeintellect.ai/verifiers/overview says the v0 stack "has been removed", while hosted-training/environment-model, guides/recipes and guides/search-agents still teach v0 classes with no banner. tutorials-environments/create carries a v0 banner.
- hosted-training/environment-model treats `default` and `bash` as different harnesses. The 0.4.0 loader says `default` "was renamed to `bash`" (utils/loaders.py:80-84). Executed: `vf-eval nowcast-alfred --env.agent.harness.id default --dry-run` printed exactly that rename message.
- The Hub page's migration-guide link points at skills/create-environments/SKILL.md on main, removed by PR #2843.
- prime-rl/training says group size 8 is the floor. The algorithms page says rae needs no siblings and group_size = 1 is fine there, so the floor is specific to group-relative algorithms such as the default grpo.

Against the commission's angle:

- "A supervised warm start comes before RL for a task this long" is supported only as Prime practice in two example READMEs (wordle, reverse-text), driven by format failures at baseline, and Prime's own alphabet-sort example runs RL without warmup. DeepSeek-R1 motivates cold-start SFT by stability and readability, and the same paper's R1-Zero is RL from the base model without SFT. Prime publishes no rule tied to task length.
- The working design's "Task.setup stages a point-in-time catalog snapshot" and "a Toolset offers catalog search" both work, but the toolset does not run inside the agent's box by default. ToolsetConfig defaults to colocated=False and runtime=SubprocessConfig() (mcp/toolset.py:16-19), so the tool server runs on the env-worker host with whatever network and files that host has. If colocated=True or a non-subprocess toolset runtime is chosen, verifiers installs the toolset's whole package (wheel or source project) into that runtime under <workdir>/.vf-src and .vf-venv (mcp/launch.py:237-296, 355). Any answer data shipped inside the package then sits in the agent's box.
- The subprocess runtime gives no isolation. Executed: a vf-debug command running in the subprocess "box" read `"realized_first": 353.0` out of the installed package's fixture file. The architecture doc already calls subprocess a debugging runtime.
- Hidden TaskData fields are not secret from the platform. The realized value rides on every trace (trace.task.data in traces.jsonl, verified), and vf-eval uploads runs to Prime by default (configs/cli/eval.py:116, push: bool = True).

## Numbers

```text
Figure: verifiers 0.4.0, uploaded 2026-10-12
Owner:  PyPI JSON for verifiers
Scope:  final release, installed version for this record
```

```text
Figure: final-release dates 0.2.0 2026-07-10, 0.2.1 2026-07-20, 0.3.0 2026-08-07, 0.3.1 2026-08-24, 0.4.0 2026-10-12
Owner:  PyPI JSON for verifiers (git tags agree: v0.2.0 2026-07-10 ... v0.4.0 2026-10-12)
Scope:  minor/patch releases since the 0.2 line
```

```text
Figure: 606 PyPI uploads with files in total. Monthly uploads 2026: Jan 6, Feb 7, Mar 4, Apr 14, May 19, Jun 82, Jul 159, Aug 116, Sep 134, Oct 44 (to 2026-10-14)
Owner:  PyPI JSON for verifiers
Scope:  all versions including .dev and .post. 2025 months ran 1 to 5 per month
```

```text
Figure: 447 commits by 35 distinct author names between 2026-07-14 and 2026-10-14. 210 commits between v0.3.1 and v0.4.0
Owner:  git log of PrimeIntellect-ai/verifiers (full clone)
Scope:  default branch. Author names, not deduplicated identities
```

```text
Figure: v0 stack removed 2026-08-31 (PR #2480), first absent in release 0.4.0. vf-init removed 2026-10-14 (PR #2843), absent in 0.4.1.dev18
Owner:  verifiers git history and the 0.4.1.dev18 wheel
Scope:  v0.3.1 still ships the legacy package (singleturn env file present in tag tree)
```

```text
Figure: default Prime sandbox for a verifiers agent: 1.0 CPU, 2.0 GB memory, 5.0 GB disk, image python:3.11-slim, idle_timeout 3600 s. First use of an image triggers an auto-build of about 10 minutes
Owner:  site-packages/verifiers/v1/runtimes/prime.py:77-102 (AgentConfig.runtime default PrimeConfig, configs/agent.py:34)
Scope:  per rollout box, unless the task or CLI overrides
```

```text
Figure: $0.046 per hour for 1 vCPU, 2 GiB RAM, 5 GiB disk (CPU $0.02/vCPU-h, memory $0.0125/GiB-h, disk $0.0002/GiB-h)
Owner:  docs.primeintellect.ai/sandboxes/overview, Pricing
Scope:  launch rates valid through 2026-12-22. Matches the verifiers default box exactly
```

```text
Figure: trace ingestion $1 per GiB, storage $0.10 per GiB-month
Owner:  docs.primeintellect.ai/traces/pricing-and-settings
Scope:  separate from training. vf-eval pushes by default
```

```text
Figure: group size at least 8, 16 to 32 common. Batch size at least 64, 128 to 512 for ablations, 1024+ in production
Owner:  docs.primeintellect.ai/prime-rl/training, Rules of Thumb
Scope:  group-relative algorithms (grpo default)
```

```text
Figure: good baseline reward roughly 10 to 80 percent
Owner:  docs.primeintellect.ai/hosted-training/end-to-end-run, Step 2 Tip
Scope:  pre-training eval of the base model on the environment
```

```text
Figure: wordle baseline average reward about 0.2, win rate 0 percent, over 20 x 3 rollouts. RL after SFT: 100 steps, 32 x 16 rollouts, batch 512, context 4096
Owner:  prime-rl examples/basic/wordle/README.md:35, 71
Scope:  Qwen3-1.7B, 20 held-out words
```

```text
Figure: PAYEMS monthly change, thousands of jobs, 2024, first release vs ALFRED vintage served on 2026-10-14 (labelled 20261013), and the naive forecast (previous month's change as known at month end)
Owner:  ALFRED (St. Louis Fed), PAYEMS vintages via alfredgraph.csv. Source data: BLS Current Employment Statistics
Scope:  reference months Jan to Dec 2024. First-release vintage in brackets

month    first  latest  revision  naive  |naive - first|  first-release vintage
2024-01   353    175     -178      216     137            2024-02-02
2024-02   275    206      -69      353      78            2024-03-08
2024-03   303    228      -75      275      28            2024-04-05
2024-04   175     64     -111      303     128            2024-05-03
2024-05   272     78     -194      175      97            2024-06-07
2024-06   206     87     -119      272      66            2024-07-05
2024-07   114     53      -61      206      92            2024-08-02
2024-08   142      9     -133      114      28            2024-09-06
2024-09   254    155      -99      142     112            2024-10-04
2024-10    12     33      +21      254     242            2024-11-01
2024-11   227    134      -93       12     215            2024-12-06
2024-12   256    237      -19      227      29            2025-01-10

Mean absolute revision first to latest: 97.7. Mean absolute naive error against first release: 104.3.
```

```text
Figure: PAYEMS level for 2024-01 (thousands): 157700 at vintage 2024-02-02, 157533 at 2024-03-08, 157560 at 2024-04-05, 157049 at 2025-02-07 and 2025-09-05, 157032 at 2026-10-13. December 2023 was 157232 at vintage 2024-02-01 and 157347 at 2024-02-02
Owner:  ALFRED PAYEMS vintages
Scope:  levels, not changes. Shows that the release of month m also revises m-1
```

```text
Figure: local stage timings with the null harness on the subprocess runtime and a canned endpoint: setup 12.7 to 14.6 s on the first run (uv installs the chat program), 5.4 s on a later run. Agent stage 3.2 to 6.3 s
Owner:  this record's local runs (traces.jsonl timing fields)
Scope:  no real model, no sandbox. Not a cost estimate for a real rollout
```

## Limits

- Closed egress was not executed. No Docker daemon in this container and no Prime account. The code path that enforces it was read (rollout.py:322, runtimes/docker/egress.py, configs/runtime.py), and its refusal on subprocess was executed.
- No real model was called and nothing was trained. The end-to-end run used a canned OpenAI-compatible endpoint that issues one `catalog_observations` tool call then answers "FORECAST: 200".
- The bash harness (the default) was not run. Only `null` was. The `null` harness has SUPPORTS_MCP=True and EXECUTES_CODE=False, so it cannot fit a model. The commission's "agent fits a model" needs bash or another code-executing harness.
- Prime publishes no per-rollout cost, token-price or tool-call-cost figure. Only the sandbox hourly rate, trace storage, and GPU-hour billing whose rates are in the CLI. Any per-rollout dollar figure in the article would be the writer's arithmetic on the sandbox rate.
- Prime gives no stated rule that SFT must precede RL for long tasks. The support is two example READMEs, with a third Prime example that skips warmup.
- No primary source quantifies reward noise for a single forecast window or recommends a group size for noisy continuous rewards. The PAYEMS table is one series over twelve months.
- The claim that `[orchestrator] group_size` is rejected by Hosted Training is inferred from prime-rl source, not executed.
- GitHub API access (stars, releases page, issue counts) was refused in this session. Maintenance figures come from PyPI and a full git clone.
- The migration-guide link on the Hub page could not be fetched (HTTP 403 through the proxy). Its absence is established from the git tree at 269ff7b.
- The alfredgraph.csv endpoint is not part of the documented FRED API. Its behaviour (column named by served vintage) is observed, not documented.

## Source assets

```text
Asset: docs.primeintellect.ai/hosted-training/environment-model, the "Type Hierarchy" code blocks showing vf.SingleTurnEnv(..., rubric=vf.Rubric(...)) and vf.ToolEnv
Shows: the docs site still teaching an API the installed package does not contain
Crop:  keep the page title and one v0 code block in frame together with the "default harness" sentence
```

```text
Asset: docs.primeintellect.ai/hosted-training/end-to-end-run, Step 4 config listing with id = "default"
Shows: a training config that uses the harness id 0.4.0 renamed
Crop:  keep the [orchestrator.train.source.env.agent.harness] table and its id line
```

```text
Asset: none on the verifiers v1 doc pages (text and code only)
Shows: n/a
Crop:  n/a
```

```text
Asset: docs.primeintellect.ai/prime-rl/overview, architecture diagram (mintcdn prime-rl/assets/architecture.png)
Shows: inference, orchestrator, trainer and where verifiers env workers sit
Crop:  keep all three process boxes and the env-worker label
```

```text
Asset: the PAYEMS 2024 table in Numbers (first release vs latest vs naive)
Shows: the vintage choice moves the target about as far as a naive forecast misses it. A grouped bar or dot chart per month works
Crop:  n/a, chart from the table, caption cites ALFRED PAYEMS vintages
```

```text
Asset: ALFRED series page for PAYEMS (https://alfred.stlouisfed.org/series?seid=PAYEMS) vintage chart
Shows: overlapping vintages of the same months
Crop:  not inspected visually in this session, verify before use
```

```text
Asset: FRED API series_observations page, output_type parameter block
Shows: the four output types including "Initial Release Only"
Crop:  keep the output_type list and the vintage_dates description
```

```text
Asset: Philadelphia Fed RTDSM page: None found beyond text links
Shows: n/a
Crop:  n/a
```

```text
Asset: DeepSeek-R1 paper: no figure needed. Section 2.3.1 text only
Shows: n/a
Crop:  n/a
```

## Discarded

```text
https://docs.primeintellect.ai/guides/rl-training: an agent-driven walkthrough (calendar scheduling) that mentions the v0 "StatefulToolEnv pattern" and an RL config of bs 128 with 8 rollouts per group in a prompt to an agent, not guidance. Superseded by prime-rl/training for group size.
https://docs.primeintellect.ai/hosted-training/full-finetuning and hosted-sft and models: read for dispatch knobs. Nothing the article needs beyond getting-started and billing.
https://docs.primeintellect.ai/faq: nothing on verifiers or environments that the primaries above do not cover.
https://docs.primeintellect.ai/verifiers/v1/tasksets (docs site copy): matches the v0.4.0 repo docs. Cited via the repo at the tag instead, which is pinned.
https://api.stlouisfed.org/fred/series/observations without a key: HTTP 400, used only to confirm the key requirement.
```

## Appendix A: interface record (verifiers 0.4.0, site-packages/verifiers/v1/)

Import: `import verifiers.v1 as vf`. Line numbers are in the installed files.

TaskData and Task, `task.py`:

```text
81   class TaskData(BaseModel):  model_config = ConfigDict(frozen=True)
84   idx: int | None = None            (set automatically from load() position)
86   id: str | None = None             88 name   90 description
93   prompt: str | Messages | None = None
95   system_prompt: str | None = None
98   image: str | None = None          100 workdir    102 agent_user
107  skills: list[SkillSource]
110  network_allow: list[str] = Field(default_factory=lambda: ["*"])
114  network_block: list[str] = Field(default_factory=list)
119  artifacts: list[Artifact]         124 artifact_max_bytes
127  timeout: TaskTimeout = TaskTimeout()     (66: setup, agent, finalize, scoring, seconds)
128  resources: TaskResources = TaskResources()  (51: cpu, memory GB, gpu "A100:2", disk GB)
131  prompt_text property
148  class Task(Generic[DataT, StateT, ConfigT]):
149  NEEDS_CONTAINER: ClassVar[bool] = False
152  def __init__(self, data: DataT, config: ConfigT | None = None)
163  key property (defaults to content hash, override for durable ids)
181  def runtime_env(self) -> dict[str, str]   (live-only process env, not traced)
185  async def setup(self, trace: Trace, runtime: Runtime) -> None
188  async def finalize(self, trace: Trace, runtime: Runtime) -> None
191  async def stage_verifier(self, trace: Trace, runtime: Runtime) -> None
195  async def validate(self, runtime: Runtime) -> bool | None
213  async def score(self, trace, runtime=None)   (227: available = {"task": self.data, "trace": trace}, plus "runtime")
266  reward weight read from fn._vf_weight. Mapping results record each key as its own reward
299  def hooks(self, attr) merges decorated methods with config-plugged functions, sorted by -priority then name
320  @classmethod def toolsets(cls, config: ConfigT) -> list[Toolset]   (per rollout)
```

State, `state.py`: `9 class State(BaseModel)` with `artifacts: dict[str, bytes | None]`. `15 StateT = TypeVar("StateT", bound=State, default=State)`. rollout.py:127 builds `trace.state` from the Task's State type.

Taskset, `taskset.py`:

```text
49   class Taskset(ABC, Generic[TaskT, TasksetConfigT]):
50   INFINITE: bool = False
60   def __init__(self, config: TasksetConfigT)
66   @abstractmethod def load(self) -> Iterable[TaskT]
88   def include(self, **match) -> Self      (idx ranges as strings "0:100", ids, keys, names)
106  def exclude(self, **match) -> Self
118  def shuffle(self, seed: int = 0) -> Self   (raises on an unbounded view)
139  def skip(self, num_tasks: int) -> Self
143  def take(self, num_tasks: int) -> Self
149  def select(self, config: SelectConfig) -> Self   (fixed order include, exclude, shuffle, skip, limit)
180  @classmethod def toolsets(cls, config: TasksetConfigT) -> list[Toolset]   (one instance per env worker)
```

Decorators, `utils/decorators.py`:

```text
78   def tool(func=None, name: str | None = None)        docstring becomes the description
89   def stop(func=None, priority: int = 0)              "Stop when a typed `Request`, `Response`, or `Trace` predicate returns true."
99   def intercept(func=None, priority: int = 0)         return a replacement or None
109  def metric(func=None, priority: int = 0)            declares needs by name: task, trace, runtime
124  def reward(func=None, weight: float = 1.0, priority: int = 0)   float or keyed scores
29   invoke() matches parameters by name, and by type annotation when types are available
41   invoke_all() uses asyncio.gather, so rewards and metrics must be async
```

Hook boundaries, `session.py:50-63`: a stop needs exactly one Request, Response or Trace parameter, an intercept exactly one Request or Response. `session.py:66-69` awaits only if the result is awaitable.

Toolsets, `mcp/toolset.py` and `mcp/server.py`:

```text
toolset.py:16  class ToolsetConfig(BaseConfig): colocated: bool = False, runtime: RuntimeConfig = SubprocessConfig(), url: str | None = None
toolset.py:22  class SharedToolsetConfig(BaseConfig): runtime = SubprocessConfig(), url = None
toolset.py:27  class Toolset(ServerBase[ConfigT, StateT])   registers every @vf.tool on an MCP server
server.py:132  TOOL_PREFIX: ClassVar[str | None] = ""   (empty: snake-cased class name. None: bare tool names)
server.py:146  state property (per-call, pulled from and pushed to the rollout's trace.state)
server.py:257  async def setup(self) -> None        (task-agnostic, once per server process)
server.py:260  async def setup_task(self, task) -> None   ("taskset-scoped servers skip this hook")
server.py:350  @classmethod def run(cls)   (module entry: `if __name__ == "__main__": MyToolset.run()`)
server.py:341-347  a Toolset must parameterize its config, e.g. Toolset[MyConfig], or run() raises TypeError
harnesses/utils/mcp.py:151  model-facing name = f"{server_name}_{tool.name}"
```

Trace, `trace.py`: `407 rewards: dict[str, Reward | None]`, `410 metrics: dict[str, float | None]`, `416 state: StateT` (excluded from serialization), `426 stop_condition: str | None`, `473 reward` (sum of score x weight), `617 num_turns` (sampled nodes), `650 last_reply` (root reply else last assistant message, stripped). `135 class Reward(score, weight)`.

Runtime, `runtimes/base.py`: `214 async def run(self, argv: list[str], env: dict[str, str]) -> ProgramResult`, `360 async def read(self, path: str, max_bytes: int | None = None) -> bytes`, `408 async def write(self, path: str, data: bytes) -> None`, `415 prepare_setup`, `423 prepare_execution(routes)`. Subprocess resolves paths against its workdir with `Path / path`, so a relative path stays in `~/.cache/verifiers/runtimes/subprocess/<name>/` and an absolute path writes to the host (runtimes/subprocess.py:168-193).

Runtime configs: `SubprocessConfig` type "subprocess" (runtimes/subprocess.py:32, no network policy). `PrimeConfig(NetworkPolicyConfig)` type "prime" (runtimes/prime.py:77). `DockerConfig`, `PodmanConfig` (runtimes/docker/__init__.py:42, 46), `ModalConfig` (modal.py:76), `E2BConfig` (e2b.py:142), `ApptainerConfig` (apptainer.py:27, no egress policy per docs). `NetworkPolicyConfig` allow/block (configs/runtime.py:57-77).

Agent and env configs: `configs/agent.py:31 class AgentConfig`: `harness` (None = taskset default), `34 runtime: RuntimeConfig = PrimeConfig()`, `45 max_turns`, `47-52 max_input/output/total_tokens`, `54 timeout: TimeoutConfig` (setup, rollout, finalize, scoring), `57 network_notice: bool = True` (adds "External network access is disabled." to the prompt, rollout.py:329-332). `envs/single_agent/env.py:15 SingleAgentEnvConfig.agent: AgentConfig`, hence `--env.agent.*`.

Task and taskset configs: `configs/task.py:11 DecoratedFunctionConfig(fn: str | None, priority: int | None)`, `24 RewardFunctionConfig(+ weight: FiniteFloat | None)`, `31 TaskConfig(judges, stops, metrics, rewards)`. `configs/taskset.py:12 SharedTasksetConfig(task: TaskConfig, system_prompt: Path | None)`, `23 TasksetConfig(id: ID = "")`.

Loaders, `utils/loaders.py`: a taskset is an installed package whose `__all__` exports exactly one Taskset subclass (99-125). Harness ids are module names under verifiers.v1.harnesses, `-` maps to `_` (70-74). `80-84` the `default` rename message. `153-160 default_harness_id` returns "bash" unless the taskset package exports its own Harness. Built-in harness ids in 0.4.0: bash, browser_use, claude_code, codex, hermes_agent, kimi_code, mini_swe_agent, null, openclaw, pi, prime_agent, rlm, terminus_2. SUPPORTS_MCP is False for mini_swe_agent and terminus_2, True for the rest.

CLI, `configs/cli/eval.py` (vf-eval): `82 model` default "deepseek/deepseek-v4-flash" (alias -m). `86 client` (base_url default https://api.pinference.ai/api/v1, api_key_var PRIME_API_KEY, configs/client.py:48-49). `91 num_rollouts` default 1, aliases group_size, rollouts_per_example, r. `99 max_concurrent` 128 (-c). `107 dry_run`. `116 push: bool = True` (--no-push). `120 output_dir` "outputs" (-o). `configs/select.py:114 shuffle` (-s), `117 limit` (-n). Config file form: `vf-eval @ config.toml`. vf-init (`configs/cli/init.py`): `name`, `path` "./environments" (-p), `add_tool` (-T), `add_harness` (-H), `force`. vf-debug: runs setup then one `--command` or `--script-path`, default runtime PrimeConfig. vf-validate: model-free validation via Task.validate.

TOML keys verified by a passing `vf-eval @ eval.toml --dry-run` and a full run: top-level `model`, `num_rollouts`, `push`, `[select] limit`, `[client] base_url, api_key_var`, `[env.taskset] id` plus taskset config fields, `[env.taskset.task.rewards] beats_baseline = { weight = 1.0 }`, `[env.agent.harness] id`, `[env.agent.runtime] type`.

Training keys (prime-rl at 782b84b and Prime docs, not executed): `prime train <config.toml> --volume <name>`, `[deployment] num_train_gpus, num_infer_gpus`, `[orchestrator] batch_size`, `[orchestrator.train] group_size`, `[orchestrator.train.sampling] max_completion_tokens`, `[[orchestrator.train.source]] name, ratio, group_size`, `[orchestrator.train.source.env.taskset] id`, `[orchestrator.train.source.env.agent.harness] id`, `[orchestrator.train.source.env.agent.runtime] type`, `[orchestrator.renderer] name`, `[ckpt]`, `[model] name`.

## Appendix B: local execution record

All files are beside this record in researcher/01/. Package `nowcast_alfred/` (pyproject pins verifiers==0.4.0), `build_fixture.py`, `eval.toml`, `stub_model.py`. Python 3.13, verifiers 0.4.0, run on 2026-10-14.

1. `python3 build_fixture.py 2026-10-14` fetched PAYEMS, UNRATE, ICSA and INDPRO from alfredgraph.csv at each 2024 month-end vintage, found each month's first-release vintage by probing forward day by day, and wrote `nowcast_alfred/nowcast_alfred/data/fixture.json` (166,139 bytes, 12 tasks). An assert confirmed no snapshot contains its own reference month.
2. `uv pip install -e nowcast_alfred`, then in Python: `vf.load_taskset(NowcastConfig(id="nowcast-alfred"))` loaded 12 tasks. `task_type()` NowcastTask, `data_type()` NowcastData, INFINITE False. Views `include(idx=["0:12"]).exclude(ids=[...]).shuffle(seed=0).skip(1).take(3)` returned three months. `hooks("reward")` = [beats_baseline], `hooks("metric")` = [abs_error, abs_error_latest, lookups]. Task.toolsets gave CatalogToolset with server_name "catalog". `vf.default_harness_id("nowcast-alfred")` = "bash".
3. `vf-debug nowcast-alfred --runtime.type subprocess -n 1 --command 'ls catalog'` with closed egress (the default) raised ValueError "task 0 requires a network policy, but the subprocess runtime does not support framework-aware policies".
4. Same with `--taskset.closed-egress false -n 2` and a command that printed the working directory, listed catalog/ and tailed catalog/PAYEMS.csv: ok=True. Setup wrote catalog/ICSA.csv, INDPRO.csv, PAYEMS.csv, UNRATE.csv into the runtime workdir. For as_of 2024-02-29 the last PAYEMS rows were 2023-12-01 157347.0 and 2024-01-01 157700.0, the first-release values.
5. Leak check, same flags, command grep on the installed fixture path: stdout `"realized_first": 353.0`. The subprocess runtime can read the answer.
6. `vf-eval nowcast-alfred -m stub/model -n 3 -r 2 --env.agent.harness.id null --env.agent.runtime.type subprocess --env.taskset.closed-egress false --client.base-url http://127.0.0.1:8765/v1 --client.api-key-var STUB_KEY --no-push --no-rich` against stub_model.py: 6 traces, stop_condition agent_completed, tools advertised to the model as catalog_observations and catalog_search. Rewards with a constant forecast of 200: Jan -0.098, Feb +0.018, Mar -0.610. Identical within each group of 2 because the stub is deterministic.
7. With the stub changed to call catalog_observations once before answering, `-n 2 -r 1`: each trace has 2 turns, `lookups` metric 1.0 (the toolset's CatalogState counter reached trace.state through the interception /state channel), and the tool result for as_of 2024-02-29 ended at 2024-01-01 157700.0.
8. `vf-eval @ eval.toml --dry-run` validated. The full run produced 6 traces with the same rewards and lookups 1.0. `--env.agent.harness.id default --dry-run` printed the rename-to-bash message.
9. Closed egress under vf-eval on subprocess: the episode carries EnvError with the same ValueError, rewards empty, process exit 0.
10. Every vf-eval run logged "vf-eval will be deprecated - move to prime-rl's `uv run eval`".

Not run: bash harness, docker/prime runtime, closed egress enforcement, any real model, vf-validate, training.
