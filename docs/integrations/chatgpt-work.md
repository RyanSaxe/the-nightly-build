# ChatGPT Work, from fork to first article

Written from a run on 2026-09-18 against a fresh fork, with no terminal.

## What you need

ChatGPT Work with its GitHub connector authorized for the account or
organization that owns the fork. The connector must be able to push branches and
open pull requests, and the session must be able to run commands in its sandbox
and reach the web for research. You never paste a token.

## The run

1. Fork in the browser with **Copy the main branch only**.
2. Make the two settings only an owner can. On the fork's Actions tab, enable
   workflows if GitHub asks; a fork made from the browser may ask, and the one
   in this run, made with `gh`, did not. Under Settings, Pages, set Source to
   GitHub Actions.
3. In ChatGPT Work, name the fork so the GitHub connector opens it:

   > Help me set up my Nightly Build paper in `<owner>/<repo>` and write my
   > first article about `<topic>`. Follow the repository's instructions.

4. What happened. `nb setup` without `gh` scaffolded `press/`, created and
   seeded `library`, and listed the Pages and Actions settings under "Still to
   do": it cannot read them back, so it lists them even when they are made. The
   scaffold reached `main`. In this run the assistant pushed it, and setup does
   that itself now. The assistant produced the article, and the pull request
   against `library` opened under the owner's identity. The `validate` check
   passed and the auto-merge job merged it 41 seconds after it opened; the
   deploy dispatched on `main` built and deployed; the article was live. From
   the pushed press to the merged pull request took four minutes, and the whole
   run fit inside an hour. The assistant reports the site URL, which is
   `https://<owner>.github.io/<repo>/`.
5. Later, if you want it: protect `library` under Settings, Branches, with a
   rule that requires the `validate` status check. It was left unprotected in
   this run and auto-merge still worked; the rule keeps a future scheduled
   identity from merging past the check.

## Where things are

Your site at `https://<owner>.github.io/<repo>/`, printed by setup. Each article
at `library/<series>/<slug>.html` on the `library` branch, its production record
beside it under `agent-artifacts/<series>/<slug>/`, and the pull request that
published it in the fork's history.

## If something stops

If setup lists a setting under "Still to do" that you have already made, nothing
is wrong: without `gh` it cannot read settings back. A pull request with no
`validate` check means workflows are disabled: enable them on the Actions tab,
then close and reopen the PR. A pull request the connector could not open
arrives as a printed handoff with the base, head, title, and body; open it from
the pushed branch on GitHub.
[Troubleshoot setup and scheduling](../troubleshooting/setup-and-scheduling.md)
covers the rest.
