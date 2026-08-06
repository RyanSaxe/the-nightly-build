# ChatGPT Scheduled Tasks

ChatGPT can run The Nightly Build without a persistent checkout when it has
public-web access, a Scheduled Task, and the connected GitHub app. In this
route ChatGPT is the only generative controller. GitHub is durable state and a
deterministic delivery system.

## Owner prerequisites

The owner must do three things before setup can be completed:

1. **Fork the repository.** The paper, its configuration, article branches, and
   published `library` state live in the owner's fork.
2. **Allow GitHub Actions from pull requests in the fork.** Enable Actions under
   **Settings → Actions → General**, permit the repository's required actions,
   and approve the first pull-request workflow when GitHub presents an approval
   gate. The article validator and browser probe must actually run on proposed
   article PRs.
3. **Give ChatGPT GitHub plugin/connector access to the fork.** The connected app
   must be able to read repository and Actions state, create branches and
   commits, open or update PRs, and inspect or rerun failed jobs. Read access
   alone is insufficient.

The setup assistant should ask for only the first unmet prerequisite, verify it,
and then continue. Never ask the owner to paste a token into chat.

## Control boundary

**ChatGPT Scheduled Task owns:**

- deciding conservatively whether an article is due;
- subject selection and repetition checks;
- public-web research and opening every cited source;
- source classification and verification;
- drafting, citations, HTML assembly, and bounded revision;
- article branch and PR creation through the GitHub connector;
- repairs driven by validator evidence on the same PR;
- observing merge, Pages publication, and the canonical public article.

**GitHub Actions owns only:**

- deterministic article validation;
- a fail-closed browser-render probe;
- protected auto-merge after the required check passes;
- exactly one GitHub Pages artifact and deployment path.

Do not add GitHub Models, `actions/ai-inference`, `web-night-shift`,
`bootstrap-first-edition`, or another repository-hosted article-generation
workflow. A second model or scheduler creates a competing control loop and
makes failures ambiguous.

## Repository changes required

A fork using this route needs:

- `WEB_TASK.md` on `main` as the stateless execution contract;
- `AGENTS.md` routing connector-only ChatGPT tasks to that contract instead of
  the checkout-only `nb sync` path;
- the normal protected article PR validator and auto-merge gate;
- one official GitHub Pages publisher;
- no duplicate generation or publication workflow;
- a browser probe that fails when Chrome cannot start, the intended article
  does not load, required article chrome or styles are absent, mobile overflow
  appears, or the page throws an exception.

The current ChatGPT setup path belongs in the user-assistant setup workflow so
an assistant detects its actual capabilities before prescribing commands. A
connector-only runtime must not claim it ran `nb setup`, `nb sync`, `nb duty`,
Python, or any local proof. When bootstrapping is still required, the assistant
must either use an authorized checkout or ask the owner for that one manual
step.

## Setup and verification

1. Inspect the fork before changing it. Preserve any valid `press/`, `library`
   branch, branch protection, Pages site, or existing schedule.
2. Complete and verify the three owner prerequisites above.
3. Bootstrap or repair the publishing boundary with `nb setup` from an
   authorized checkout when needed. Confirm `library`, the required article
   check, protected merge, and the sole Pages publisher exist.
4. Configure GitHub Pages to use **GitHub Actions** as its source. A successful
   workflow is not enough if the public site still returns 404.
5. Keep `WEB_TASK.md` on `main` and remove any GitHub-hosted generation path.
6. Prove the connector write surface with a disposable branch and draft PR.
   Confirm ChatGPT can create the branch and commit, open the PR, read the
   Actions result, close the PR, and clean up the branch.
7. Run one real scheduled edition and require the complete publication gate
   below.

## Scheduled Task prompt

Replace `<owner>/<repo>` with the fork:

> Run the Daily Nightly Build for `<owner>/<repo>`. Perform all subject
> selection, public-web research, source verification, article drafting,
> bounded revision, and pull-request preparation yourself using the connected
> GitHub app and the public web. Read `WEB_TASK.md` from `main` and follow it
> exactly. Do not dispatch, invoke, or rely on GitHub Models,
> `actions/ai-inference`, `web-night-shift`, `bootstrap-first-edition`, or any
> other GitHub-hosted article-generation workflow. GitHub Actions are only the
> independent CI validator, auto-merge gate, and static publisher. If no article
> is due or the evidence is insufficient, publish nothing.

One task runs the entire paper. Cadence and series changes remain repository
state, not copies embedded in the schedule prompt.

## Completion gate

Opening a PR is not completion. ChatGPT may report a successful edition only
when all of these facts hold for the same article:

1. the current PR head SHA passed the required article check;
2. that validated head merged into `library`;
3. the sole Pages publisher succeeded after the merge;
4. the repository Pages site resolves as a workflow deployment;
5. the canonical homepage returns HTTP 200;
6. the exact article URL returns HTTP 200 with matching series, slug, title, and
   date metadata.

A green validator with no merge, a green publisher with a public 404, or a raw
GitHub file URL is not a published article.

## Bounded repair

Repair only blockers reported by the validator or publisher. Make at most three
article-repair commits and at most two infrastructure reruns for one edition.
If the bound is exhausted, preserve the PR, report `BLOCKED` with the machine
evidence, and resume that PR before commissioning another article for the same
series.
