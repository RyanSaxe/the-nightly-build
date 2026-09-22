# Set up your paper

Fork this repository with **Copy the main branch only** checked. Then choose one
of these setup paths.

## Use a terminal

Sign in to GitHub from `gh` with an account that owns the fork. Clone the fork
and open it in Claude Code or Codex. The agent can run setup for you, or you can
run `./nb setup` yourself before asking for an article.

With `gh`, `./nb setup` creates the default press and `library` branch, seeds
the publishing workflows, and enables Actions, Pages, and repository auto-merge.
It also tries to protect `library` with the `validate` check. If your GitHub
account cannot make a setting, setup prints its link and tells you what to
change.

## Use ChatGPT Work

Connect GitHub in ChatGPT Work and authorize the account or organization that
owns the fork. Give the app access to the fork and permission to push branches
and open pull requests. Before asking for an article, enable Actions from the
fork's Actions tab if GitHub prompts you. Under Settings, Pages, set Source to
GitHub Actions.

Without `gh`, `./nb setup` creates and pushes the git configuration, but cannot
change or read repository settings. It lists Pages and Actions under "Still to
do" even if you already enabled them. If either setting is missing, follow its
GitHub link. Protecting `library` behind the `validate` check is recommended.

## Ask for your first article

> Help me set up my Nightly Build paper in `<owner>/<repo>` and write my first
> article about `<topic>`. Follow the repository's instructions.

`./nb setup` requires `git`, `uv`, and Python 3.10 or newer. An agent can
install or use these in its own environment. You do not need to paste a GitHub
token into chat.

The default press includes Dispatches for articles you request and News Brief
and Feature for scheduled publication. The site appears after Pages is enabled
and the first article merges. See [Your first article](./first-article.md) for
the publication flow and [Schedule publication](../guides/operate/schedule.md)
to set up a recurring run.
