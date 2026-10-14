# researcher brief: expert-tools/verifiers-rl-environments (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/editorial-direction.md : the standing directions
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/commission.md : the assignment, the running example and its design
Output: /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Leads from the owner, every one to be re-verified against source before it is
recorded as fact:

1. Install the package in a scratch venv under your scratchpad
   (`uv venv && uv pip install verifiers`) and read site-packages directly.
   Record the exact version installed. The owner reports PyPI verifiers 0.4.0
   is v1-only (`import verifiers.v1 as vf`) and that SingleTurnEnv, ToolEnv,
   MultiTurnEnv and Rubric are gone from the package.
2. Core objects reported: vf.TaskData (frozen pydantic row: prompt,
   system_prompt, network_allow, network_block, timeout, resources, subclassed
   to add hidden fields) -> vf.Task[Data, State, TaskConfig] (async
   setup(trace, runtime), finalize, @vf.reward(weight=..), @vf.metric, @vf.stop,
   classmethod toolsets) -> vf.Taskset[Task, TasksetConfig] with load() (list or
   generator, INFINITE=True for procedural). Views: include, exclude, shuffle,
   skip, take.
3. Reward and metric methods declare needs by parameter name (task, trace,
   runtime). trace.last_reply, trace.num_turns, trace.stop_condition. Rewards
   return a float or a dict of keyed scores. TOML hooks under
   [env.taskset.task.rewards] with fn, weight, priority.
4. @vf.stop takes a typed Request, Response or Trace predicate. @vf.intercept
   rewrites a boundary (environments/web_search_interception in the GitHub repo
   blocks a reward hack).
5. Tools: subclass vf.Toolset[ConfigT, StateT], @vf.tool (docstring is the
   description, name is TOOL_PREFIX_method), async setup() once per server,
   setup_task(task) per task, typed per-rollout state via self.state (a vf.State
   subclass). Served as MCP servers. Task.toolsets per rollout, Taskset.toolsets
   shared per worker. Examples: environments/wiki_search, environments/scratchpad.
6. Action space = harness x toolsets x network policy. Harness ids: bash
   (default), null, claude_code, codex, rlm, mini_swe_agent, terminus_2 etc.
   Default runtime a Prime sandbox, subprocess for debugging.
   TaskData(network_allow=[]) means no egress. Runtime has async read(path) and
   write(path, bytes).
7. CLI: vf-init <name> [-T] [-H], vf-eval <taskset> -n -r -s,
   --env.agent.harness.id, `vf-eval @ config.toml`. Training:
   `prime train config.toml --volume <vol>` with [[orchestrator.train.source]],
   [orchestrator.train.source.env.taskset] id, group_size, batch_size. Prime's
   docs use harness id "default", which the 0.4.0 loader says was renamed
   "bash".
8. ALFRED/FRED API: fred.stlouisfed.org/docs/api/fred/series_observations.html.
   realtime_start, realtime_end, vintage_dates. output_type 4 = initial release
   only. API key required.

Also source:
- Prime Intellect itself: the open RL post-training stack (prime-rl), the
  Environments Hub, Hosted Training, from Prime's own pages.
- The docs-site drift: find a docs page still showing the v0 API, record URL.
- Release history and cadence (PyPI release dates, GitHub releases or tags).
- Rollout cost, group size and reward-noise guidance, and any Prime guidance
  on SFT warm start before RL. Primary documents only for figures.
- One or two primary sources on revisions and real-time data (ALFRED
  documentation, or a Philadelphia Fed real-time dataset page) to support the
  leakage argument.

Most important for the writer: for every class, decorator, method, CLI flag and
TOML key the article could show, record the exact signature or spelling and the
file path and line in site-packages (or repo path at a named commit). If you can,
write a minimal nowcasting-shaped environment against the installed package and
record what imports, constructs and runs locally (vf-eval with the subprocess
runtime and no model call is fine if a model is unavailable). Put that file in
/home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/researcher/01/ beside evidence.md and record exactly what ran.

Do not record anything about the paper owner, their employer or their job.
