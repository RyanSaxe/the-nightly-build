# ChatGPT connector-only publication task

This file is the execution contract for a ChatGPT Scheduled Task that has the
public web and a connected GitHub app but no persistent checkout or shell.
Checkout-based scheduled agents use `.agents/prompts/run-scheduled-publication.md`
instead.

## Authority and limits

- Read `AGENTS.md`, the configured `press/`, `spec/editorial.md`,
  `spec/headlines.md`, the effective series and template files, and the current
  publication state before producing anything.
- ChatGPT is the only generative runtime in this route. It performs selection,
  research, verification, drafting, revision, article assembly, and bounded
  repairs itself.
- Do not invoke GitHub Models, `actions/ai-inference`, `web-night-shift`,
  `bootstrap-first-edition`, or any other GitHub-hosted generation workflow.
- GitHub Actions only validate, run the browser gate, auto-merge validated
  content, and publish the static site.
- Never claim to have run `nb`, `uv`, Python, a local browser, or any shell
  command. CI supplies executable proof.
- Never push directly to `main` or `library`. Article work lands through a
  branch and pull request targeting `library`.
- During an article run, modify only the article bundle allowed by the current
  engine and template. Do not modify workflows, engine code, `press/`, specs,
  templates, or site assets.

## Durable state

Reconstruct every run from GitHub. Read:

- current `main` configuration;
- current `library` contents and recent article metadata;
- open article PRs and their current head SHAs;
- validator comments and Actions results;
- recently merged article PRs;
- Pages publisher results and the canonical public site.

An open or failed article PR for a series takes priority over commissioning a
new article for that series. A merged article whose public publication is still
missing takes priority over new work.

## Determine due work

Infer due work conservatively from the current series configuration and the
published `library` state. Respect cadence, paused/completed/manual modes, time
zone, and the latest published date for each series.

Process at most one due article per series. When the repository state does not
establish that an article is due, publish nothing. Do not use uncertainty as a
reason to create filler.

## Select and research

For each due series:

1. Read recent titles, subjects, source sets, and article dates to avoid
   repetition.
2. Select a subject inside the configured beat because the evidence changed,
   the mechanism matters, and the consequences justify a complete article.
3. Research before drafting. Open every source that will be cited.
4. Prefer the record that owns each load-bearing claim. Use genuinely
   independent reporting or analysis for context where the series requires it.
5. Classify sources by authorship and stake, not by domain or file type.
6. Verify the printed source URL lands on the source itself, not merely a fetch
   transport or cached endpoint.
7. Meet the configured source floor and source-kind constraints. If the evidence
   is insufficient, publish nothing.

## Draft the article bundle

Follow the effective series prompt, template, furniture, editorial, headline,
metadata, source-order, citation, asset, active-content, and word-band rules.
Use the same article and PR structure that the checkout-based orchestrator would
produce, but do not invent local artifacts or command results.

Create exactly one article branch from the current `library` head. Commit only
the permitted article bundle and open one ready-for-review PR targeting
`library`. Keep the PR body consistent with the article metadata and include the
required task, process, voice, research, and consulted-source records.

Record the PR number, article path, current head SHA, title, series, slug, date,
and canonical Pages base URL before entering the closure loop.

## Closure and repair loop

Opening a PR is not completion.

1. Observe the required validator for the current PR head SHA. Queued and
   in-progress runs are unfinished.
2. If validation fails, read the validator comment and failed job logs. Repair
   only the observed blockers on the same branch and keep the PR record aligned
   with the article.
3. Make at most three article-repair commits for one edition. Do not weaken a
   gate or rewrite unrelated sections.
4. If a job failed only because of a runner, network, checkout, cache, or GitHub
   service fault, rerun the failed job. Make at most two infrastructure reruns
   for one workflow attempt.
5. After the required check passes, verify that the same validated head merges
   into `library`. Do not manually merge a head whose successful check cannot be
   tied to that SHA.
6. Observe the sole GitHub Pages publisher after merge. Rerun only transient
   infrastructure failures within the same retry bound.
7. Verify the public result independently at the canonical GitHub Pages site.

If repair bounds are exhausted, preserve the PR, report `BLOCKED` with the
machine evidence, and resume it on the next task run before creating another
article for that series.

## Publication gate

Report a successful publication only when all six facts hold for the same
article:

1. the current PR head SHA passed the required article check;
2. that validated head merged into `library`;
3. the sole Pages publisher succeeded after that merge;
4. the Pages site resolves as a workflow deployment;
5. the canonical homepage returns HTTP 200;
6. the exact article URL returns HTTP 200 and contains matching series, slug,
   title, and date metadata.

Raw GitHub content, an Actions artifact, a workflow summary, a PR URL, or a
green publisher paired with a public 404 is not publication.

## Final result

Return one of:

- `PUBLISHED` with the canonical article URL and PR number;
- `NOT DUE` when no series requires work;
- `NO ARTICLE` when research could not satisfy the evidence contract;
- `BLOCKED` with the preserved PR and exact machine or permission evidence.
