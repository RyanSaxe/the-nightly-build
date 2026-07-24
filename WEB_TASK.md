# ChatGPT Scheduled Task night shift

This file is the execution contract for a ChatGPT Scheduled Task that has access
to the public web and a connected GitHub app, but does not retain a repository
checkout or run shell commands. `PROTOCOL.md` remains the editorial authority;
this file adapts that protocol to a stateless, connector-only runtime.

## Execution boundary

- The ChatGPT Scheduled Task is both the scheduler and the authoring runtime. It
  performs subject selection, public-web research, source verification, article
  drafting, bounded revision, HTML assembly, and pull-request preparation.
- Do not invoke GitHub Models, `actions/ai-inference`, or any GitHub-hosted
  article-generation cron or workflow. GitHub Actions do not author content.
- GitHub Actions are the independent proof and render probe, the auto-merge gate,
  and the static publisher after a valid article PR is opened.
- Git is durable memory. Reconstruct state from `main`, `library`, article PRs,
  bot comments, labels, and CI on every run.
- Never claim to have run `uv`, Python, `engine/check.py`, or any other shell
  command. The protected repository check supplies that machine evidence.
- Never push directly to `main` or `library`, never merge an article PR, and
  never modify engine, workflow, template, press, or site-asset files during an
  article run.

## Run loop

1. Resolve the repository named by the Scheduled Task. Read this file,
   `AGENTS.md`, `PROTOCOL.md`, the house editorial and headline specifications,
   `press/`, the configured series, and each effective template needed tonight.
2. Inspect open and recently merged article PRs before commissioning work.
   - Repair an existing open PR before creating another for the same series.
   - If a merged article already satisfies today's cadence, do not duplicate it.
   - Treat the latest bot-authored editor comment and CI state as authoritative.
3. Determine due work conservatively from the series configuration and the
   published `library` state. At most one article per due series may be proposed.
   When the stateless runtime cannot establish that an article is due, skip it.
4. For an open failed PR, update its existing branch and production record from
   the editor findings. Make at most two repair commits in one run. If it remains
   blocked, leave it open and report the unresolved findings; do not commission a
   replacement article in the same run.
5. For new work, read recent article titles and metadata to avoid repetition.
   Select a subject inside the series beat because the evidence changed, the
   mechanism matters, and the consequences justify a complete article.
6. Research before drafting. Open every cited source. Prefer the record that owns
   each load-bearing claim and use genuinely independent reporting or analysis for
   context. Meet the configured source floor and source-kind bands. A skipped
   article is preferable to unsupported synthesis.
7. Build exactly the article bundle permitted by `PROTOCOL.md`, normally one HTML
   file at `library/<series>/<slug>.html`. Follow the effective template,
   metadata, source-order, citation, active-content, word-band, and production
   record rules. The Scheduled Task owns all prose and reasoning; GitHub does not.
8. Create a branch from the current `library` head, commit only the article bundle,
   and open one ready-for-review PR targeting `library`. Use the required title
   and PR-body structure: matching `nb-meta`, Task, Process, Voice brief,
   Research, and Also consulted.
9. Stop after opening or repairing the PR. Do not claim publication. The protected
   GitHub check validates and render-probes the proposal; auto-merge and the
   publisher handle a successful result. The next Scheduled Task run reconstructs
   the outcome from GitHub.

## Hard gates before opening a PR

- The branch is based on the current `library` head and changes only the permitted
  article bundle.
- Metadata, title, dek, source count, word count, date, and rendered content agree.
- Every required and flex section is present and cited as the template requires.
- Sources appear in first-cite order and satisfy the configured primary and
  independent-secondary composition.
- Every factual claim is supported by a source actually opened during this run;
  quotations, numbers, dates, names, and URLs are never invented.
- The HTML contains no executable content beyond the shipped engine runtime and
  no external images, iframes, forms, event handlers, or unsafe URLs.
- The PR body preserves a complete, honest production record and states when the
  runtime used a single context rather than isolated roles.

## Setup-agent obligations

A setup agent using this route must:

1. Confirm the fork is connected to ChatGPT's GitHub app with permission to read
   repository state, create branches and commits, and open or update PRs.
2. Prove that exact write surface with a disposable branch and draft PR, then
   close the PR and remove or reset the disposable branch.
3. Create one daily ChatGPT Scheduled Task for the whole paper using the prompt
   below. Do not create a second GitHub generation schedule.
4. Remove any previously installed GitHub Models generation workflow or cron.
   Keep only repository CI, auto-merge, reporting, and static publishing.
5. Run the task once immediately when the product exposes that control, then
   verify the resulting PR and published URL rather than merely asserting success.

## Scheduled Task prompt

Replace `<repo>` with the fork's `owner/name` value and use this as the complete
Scheduled Task instruction:

> Run the Daily Nightly Build for `<repo>`. Perform all subject selection,
> public-web research, source verification, article drafting, bounded revision,
> and pull-request preparation yourself using the connected GitHub app and the
> public web. Read `WEB_TASK.md` from `main` and follow it exactly. Do not
> dispatch, invoke, or rely on GitHub Models, `actions/ai-inference`, or any
> GitHub-hosted article-generation workflow. GitHub Actions are only the
> independent CI validator, auto-merge gate, and static publisher. If no article
> is due or the evidence is insufficient, publish nothing.
