# Claude Code, from fork to first article

Written from a run on 2026-09-18 against a fresh fork, in a terminal with `gh`
signed in.

## What you need

Claude Code in a terminal. `gh auth status` succeeds for an account that
administers the fork. `git`, `uv`, and Python 3.10 or newer on the machine.

## The run

1. Fork with **Copy the main branch only** and clone it, or let Claude Code do
   both:
   `gh repo fork the-nightly-build/the-nightly-build --default-branch-only --clone`.
2. Open the checkout in Claude Code and say:

   > Help me set up my Nightly Build paper and write my first article about
   > `<topic>`. Follow the repository's instructions.

3. Setup. It runs `./nb setup`, which printed, in order: the repository, the
   scaffolded `press/`, a valid configuration, the pushed `library` branch, the
   seeded workflows, Pages enabled, Actions enabled, auto-merge enabled,
   `library` protected, "The presses are ready", and the site URL. Nothing was
   asked of the owner. The scaffold is pushed to `main` as part of setup.
4. The article. The writing coach and researcher ran together, then the writer,
   then the editor. `nb prepare-pr` opened the pull request through `gh`. The
   `validate` check passed in 24 seconds and the auto-merge job in 8, the deploy
   dispatched on `main` built and deployed, and the article was live at
   `library/dispatches/<slug>.html` under the site URL. About 45 minutes of
   agent time, nearly all of it the four roles, with the writer and editor on a
   smaller model under the economy profile.
5. Hold, if you want it. Add "let me read it first" to your request and the pull
   request opens as a draft. In the same rehearsal, the draft was validated and
   left unmerged; pressing "Ready for review" ran the check again, merged, and
   deployed.

## Where things are

Your site at `https://<owner>.github.io/<repo>/`, printed by setup. Each article
at `library/<series>/<slug>.html` on the `library` branch, its production record
beside it under `agent-artifacts/<series>/<slug>/`, and the pull request that
published it in the fork's history.

## If something stops

A warning from setup about Pages or Actions names the setting and its URL; make
it and re-run `./nb setup`. A pull request that shows no `validate` check means
workflows are disabled: enable them on the Actions tab, then close and reopen
the PR.
[Troubleshoot setup and scheduling](../troubleshooting/setup-and-scheduling.md)
covers the rest.
