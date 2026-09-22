# Schedule publication

Set up a recurring task when you want articles to publish without asking for
each one.

## Choose a scheduler

The supported paths are
[ChatGPT Work scheduled tasks](../../integrations/chatgpt-work.md#schedule-publication)
and [Claude Code Routines](https://code.claude.com/docs/en/routines).

For ChatGPT Work, connect GitHub and give the app access to the fork. Create a
scheduled task in Work, then specify the repository, a daily time and timezone,
and whether Article PRs should publish automatically after checks pass or remain
drafts for your review.

For Claude Code Routines, create a cloud routine with the fork, web access, and
the required tools connected. Set the schedule and use the repository prompt
below. Anthropic's [Routines guide](https://code.claude.com/docs/en/routines)
has the current setup instructions.

Both schedulers need to be able to update `main`, fetch `library`, research the
web, run `uv` and repository commands without pausing for input, and push a
branch and open an Article PR against `library`. Check the provider's GitHub
permissions and network settings when creating the task.

## Give the scheduler its instructions

Keep the scheduled prompt short. Point it to the repository-owned workflow:

> Work in The Nightly Build repository `<owner>/<repo>`. Update the checkout to
> the current remote `main` before reading anything. Read
> `.agents/prompts/run-scheduled-publication.md` and follow it in this agent.
> This paragraph is the entire assignment. If that file is missing from
> up-to-date remote `main`, stop and report the missing repository entrypoint.

Choose the publication mode when configuring the task. Automatic publication
lets validated Article PRs merge. Draft-only leaves each Article PR for you to
review. The repository prompt defines how the agent researches, writes, checks,
and submits each article; do not copy those steps into the scheduler prompt.

Each run starts with `nb sync` and `nb duty`. One schedule can serve the whole
paper because each series defines its own cadence. A series with
`cadence: manual` never appears in scheduled work.

## If a run stops

Check the task's run details and the Article PR's `validate` check. For setup,
repository access, or research failures, see
[Troubleshoot setup and scheduling](../../troubleshooting/setup-and-scheduling.md).
The optional [scheduled runtime check](./verify-scheduled-runtime.md) can help
diagnose a new provider environment without publishing an article.

Keep scheduler credentials out of the `library` PR workflow. Article validation
runs on `pull_request` without scheduler secrets. See
[Publishing and security](../../concepts/publishing-and-security.md).
