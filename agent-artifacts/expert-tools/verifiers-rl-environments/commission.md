# Commission: expert-tools/verifiers-rl-environments

Series: expert-tools (open mode, manual commission while the series is paused).
Template: article. Bands: 1200 to 3000 words, counted over the whole rendered
article including code listings, tables and the sources list. Minimum 6 sources.
Publication: `nb prepare-pr` without `--hold`. A clean PR auto-merges.

## The assignment

Subject: `verifiers`, the open-source Python package from Prime Intellect for
building reinforcement-learning environments for language-model agents, plus a
short, sourced account of the company's surrounding stack (open RL post-training
stack, Environments Hub, Hosted Training) only as far as it explains where an
environment goes once written.

Contribution: someone who finishes the piece can write their own RL task with
the current `verifiers` release. The interface is the priority: the classes,
the hooks and their signatures, the CLI, and how a training run consumes a
taskset. Every code listing matches the API of the release the researcher
installs and reads, not the docs site or a blog post.

The question it answers: what does a working `verifiers` environment for a
real, non-toy agent task look like, and what has to be true of it before the
reward is worth training on?

## Running example

One environment built up across the whole piece: an RL environment that trains
an LLM agent to do macro nowcasting. The agent hunts for leading indicators
across many economic series, builds features, fits a model, and submits a
forecast that is scored out of sample. Data is point-in-time from ALFRED, the
St. Louis Fed's vintage archive, accessed through the FRED API's real-time
parameters.

Working design, to be adjusted wherever the installed source disagrees:

- A TaskData subclass holds the series id, the as-of date, the target period,
  the hidden realized value and a naive baseline forecast.
- Taskset.load builds many tasks across series and as-of dates.
- Task.setup stages a point-in-time catalog snapshot into the runtime.
- Network egress is closed for the rollout so the live internet, and with it
  future data, is unreachable.
- A Toolset offers catalog search, with a lookup counter in typed per-rollout
  state.
- Reward is improvement over the naive baseline. Absolute error and lookup
  count are metrics, not reward.

The piece must establish, not merely mention:

- How leakage and reward hacking enter this specific task: data revisions
  (first release vs later vintage, so which vintage the score uses), lookahead
  through series published after the as-of date, and the agent finding the
  target value in its sandbox or through a tool. What in the API closes each.
- Why a single problem is search and not RL: the policy needs many tasks.
- Why one forecast window is a noisy reward, and what that implies for group
  size and for the reward definition.
- What a rollout costs (sandbox, tool calls, tokens), sourced where possible.
- Why a supervised warm start comes before RL for a task this long, sourced to
  Prime's own guidance or a primary paper if one exists.
- Maintenance: PyPI release vs docs site drift (v0 API pages vs the v1 package),
  release cadence, and the renamed harness id. Is it maintained well enough to
  trust?

## Boundaries

- No information about the paper owner, their employer, their job, or any work
  project. Present this as a Python package and a company worth knowing. No
  first-person framing about why the owner wants it.
- Owner style rule, stricter than the house spec: no em-dashes and no
  semicolons anywhere in the article (display text, body, captions, code
  comments in listings included).
- Do not invent API surface. Where a listing is illustrative or untested, the
  caption says so and says what it was checked against.
- Do not claim the environment was trained. It was not. Show what is
  checkable: the code shape against the installed package, and anything
  actually executed locally.
- FRED API needs a key. Do not print or require a real key in a listing.

## Prior coverage and recent patterns

`nb history` shows no prior article on verifiers, Prime Intellect, or RL
environments. Related published pieces are paper-of-the-day articles on DPO and
DQN, which this piece must not re-explain.

Recent Expert Tools and Technical pieces to break from:

- Closing section titled "Verdict" in both sqlglot and shadcn-ui. Do not use
  that heading or a verdict-shaped closing paragraph built the same way
  ("Reach for X when ... Reach for Y when ...").
- A dedicated maintenance section titled "Whether the project is here to stay"
  (sqlglot). Do not reuse the phrasing.
- Headlines built as "<Tool> does X, and Y" (sqlglot, grapple-nvim) or with a
  trailing qualifier clause (dbt v2). Avoid the comma-and clause headline.
- Openers that start with a second-person scenario ("You have a working Spark
  query..."). Open on something else.
- Heavy reliance on "I installed / my run" provenance lines is fine where real.

## Decisions log

- Series home: expert-tools, because the owner named it and the subject is a
  niche Python tool that changes an AI-training workflow.
- Harness id: use `bash`, the name in the installed loader, not `default`.
- Model and effort: all roles run in this orchestrator's runtime with the
  same available model. The editor directive (effort high, model inherit,
  required) is honoured. Other stages use the available model at its default
  effort.

## Decisions after researcher/01

- The installed release is verifiers 0.4.0. Every listing follows the
  researcher's Appendix A and the nowcast_alfred package that ran, not the
  owner's original leads where the two differ (async hooks, `task` is the
  TaskData row, intercept examples, network policy semantics, vf-init status).
- Closed egress was not executed. The article describes it from the source,
  says it was read and not run, and says the subprocess runtime refuses it.
  Framework routes (model endpoint, MCP tool URLs) stay reachable under
  `network_allow=[]`, and task setup runs before the policy applies. Teach
  both as part of the leakage argument.
- Leakage through packaging is in scope: a fixture that ships realized values
  inside the environment package reaches the sandbox when toolsets are
  colocated, and the hidden value lands in uploaded traces when push is on.
  The article says what to do about each from the source.
- Supervised warm start: the evidence does not support a rule. Present it as
  a decision with its condition (a base model whose group rewards are all at
  the floor gives RL no signal), cite Prime's prime-rl examples that do SFT
  first and the one that does not, and DeepSeek-R1-Zero as the counter-case.
  Mark it as judgment.
- Rollout cost: use the sandbox rate the record gives and arithmetic the
  reader can check. Do not invent token prices. Say Prime publishes no
  per-rollout figure.
- Reward noise: use the PAYEMS 2024 figures in the record and say they are
  one series over twelve months.
- vf-init: exists in 0.4.0, removed on main two days after release. Show it
  only with that caveat, or skip it. The maintenance discussion uses the
  docs-site pages that still teach v0, the renamed harness id, the vf-eval
  deprecation notice and the Hosted Training config key placement, all dated.
- The ALFRED fixture route (alfredgraph.csv) is not the documented API. The
  article teaches the documented FRED API parameters for building the
  snapshot and may mention the fixture route only as what the test used.
