# Use ChatGPT Work

ChatGPT Work can set up a paper and publish an article from a cloud session. Its
scheduled tasks can run from a fresh cloud checkout without your computer
running.

## Connect GitHub

Connect the GitHub app to ChatGPT and authorize the account or organization that
owns your fork. Allow access to the fork and the actions the workflow needs,
including pushing branches and opening pull requests. Workspace administrators
may need to enable the app or its write actions. See OpenAI's guides to
[connect GitHub](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)
and [connected apps](https://help.openai.com/en/articles/11487775).

## Publish an article now

Create a fork of this repository, then start a Work conversation and name the
fork as `<owner>/<repo>`. Ask:

> Help me set up my Nightly Build paper in `<owner>/<repo>` and publish my first
> article about `<topic>`. Follow the repository's instructions. Let me review
> the article before it publishes.

Work uses a cloud checkout to run setup and the article workflow. The request to
review first makes the Article PR a draft. To publish without a review hold,
omit that sentence.

## Schedule publication

Create a recurring scheduled task in ChatGPT Work. Name your fork, choose a
daily time and timezone, and say whether the task may publish after checks pass
or should leave a draft PR for you. For example:

> Schedule The Nightly Build in `<owner>/<repo>` every day at 5:00 AM Eastern.
> Follow the repository's scheduled publication instructions. Open a draft PR
> for review instead of publishing automatically.

Replace the repository name and schedule with yours. If you want automatic
publication, say so explicitly. The task instructions should direct Work to
start from the current `main` and follow
`.agents/prompts/run-scheduled-publication.md`. That file is the source of truth
for the run. See [Schedule publication](../guides/operate/schedule.md) for the
full prompt.

Review the scheduled task and its GitHub permissions before saving it. You can
inspect task runs in ChatGPT's Scheduled view. OpenAI's
[scheduled tasks guide](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)
covers task setup and availability.

## After publication

Your site is `https://<owner>.github.io/<repo>/`. The assistant reports the
published article and its URL when the workflow completes. If GitHub does not
start the `validate` check on an Article PR, enable Actions for the fork and
close and reopen the PR.

For setup problems, see
[Troubleshoot setup and scheduling](../troubleshooting/setup-and-scheduling.md).
