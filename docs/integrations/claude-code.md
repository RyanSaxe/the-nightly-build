# Use Claude Code

Claude Code can set up a local paper and publish articles from a local clone. It
can also run unattended with
[Claude Code Routines](https://code.claude.com/docs/en/routines).

## Publish an article now

Install Claude Code, Git, `uv`, and Python 3.10 or newer. Authenticate `gh` with
an account that can administer the GitHub fork.

Fork this repository, clone your fork, and open the clone in Claude Code. Ask:

> Help me set up my Nightly Build paper and publish my first article about
> `<topic>`. Follow the repository's instructions. Let me review the article
> before it publishes.

The assistant runs `./nb setup` when the paper needs setup, then follows the
article workflow. The request to review first makes the Article PR a draft. To
publish without a review hold, omit that sentence.

## Schedule publication

Create a cloud Routine and give it access to the fork, web research, GitHub, and
the tools required by the scheduled prompt. Set its schedule and use this
prompt:

> Work in The Nightly Build repository `<owner>/<repo>`. Update the checkout to
> the current remote `main` before reading anything. Read
> `.agents/prompts/run-scheduled-publication.md` and follow it in this agent.
> This paragraph is the entire assignment. If that file is missing from
> up-to-date remote `main`, stop and report the missing repository entrypoint.

Choose whether the routine may publish automatically or should stop with a draft
PR for review. For current Routine setup steps and limits, see
[Claude Code's Routines guide](https://code.claude.com/docs/en/routines).

## After publication

Your site is `https://<owner>.github.io/<repo>/`. The assistant reports the
published article and its URL when the workflow completes. If GitHub does not
start the `validate` check on an Article PR, enable Actions for the fork and
close and reopen the PR.

For setup problems, see
[Troubleshoot setup and scheduling](../troubleshooting/setup-and-scheduling.md).
