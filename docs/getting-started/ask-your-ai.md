# Ask your AI

Use an agent that can run commands and work with your GitHub fork. You can use a
coding agent in a terminal, such as Claude Code or Codex, or use ChatGPT Work
with GitHub connected. See [Agent integrations](../integrations/README.md) for
the product-specific steps.

## 1. Fork the repository

On GitHub, fork this repository with **Copy the main branch only** checked.

## 2. Connect an agent to your fork

- In a terminal, sign in to GitHub with `gh`, clone your fork, and open the
  checkout in your coding agent.
- In ChatGPT Work, connect GitHub and allow access to your fork. Enable
  workflows in the fork's Actions tab if they are disabled. Under Settings,
  Pages, set Source to GitHub Actions.

## 3. Ask for an article

Name your fork and topic in this request:

> Help me set up my Nightly Build paper in `<owner>/<repo>` and write my first
> article about `<topic>`. Follow the repository's instructions.

The agent runs `./nb setup` if the paper is not configured, then creates the
article PR. A clean PR publishes after GitHub's `validate` check passes. Add
"let me read it first" if you want a draft PR to review before it publishes.

For more about setup, see [Set up](./setup.md). For scheduling, see
[Schedule publication](../guides/operate/schedule.md).
