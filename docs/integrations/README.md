# Choose an agent

The Nightly Build works with an agent that can follow repository instructions,
run commands, research the web, and use GitHub. Choose a path by what you want
to do.

## Publish an article now

- [Claude Code](./claude-code.md): work in a local clone from the terminal.
- [Codex](./codex.md): work in a local clone with Codex CLI.
- [ChatGPT Work](./chatgpt-work.md): work in a cloud session with a connected
  GitHub account.

Each path can set up the paper and publish an article through the repository's
Article PR workflow. For the general setup flow, see
[Set up](../getting-started/setup.md).

## Publish on a schedule

- [ChatGPT Work scheduled task](./chatgpt-work.md#schedule-publication): use a
  recurring Work task with GitHub access and a fresh cloud checkout.
- [Claude Code Routine](https://code.claude.com/docs/en/routines): use a
  scheduled cloud routine with the repository and required tools connected.

Both paths read their run instructions from
[`run-scheduled-publication.md`](../../.agents/prompts/run-scheduled-publication.md).
The scheduler prompt should point to that file rather than copy its workflow.
See [Schedule publication](../guides/operate/schedule.md) for the prompt and the
publication choices.
