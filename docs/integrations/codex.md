# Use Codex

Use Codex CLI from a local clone to set up a paper and publish articles through
the repository's Article PR workflow.

## Publish an article now

Install Codex CLI, Git, `gh`, `uv`, and Python 3.10 or newer. Authenticate `gh`
with an account that can administer the GitHub fork.

Fork this repository, clone your fork, and open the clone in Codex. Ask:

> Help me set up my Nightly Build paper and publish my first article about
> `<topic>`. Follow the repository's instructions. Let me review the article
> before it publishes.

The assistant runs `./nb setup` when the paper needs setup, then follows the
article workflow. The request to review first makes the Article PR a draft. To
publish without a review hold, omit that sentence.

For unattended publication, use a
[ChatGPT Work scheduled task or Claude Code Routine](../guides/operate/schedule.md).
The scheduled workflow itself lives in
`.agents/prompts/run-scheduled-publication.md`.

## After publication

Your site is `https://<owner>.github.io/<repo>/`. The assistant reports the
published article and its URL when the workflow completes. If GitHub does not
start the `validate` check on an Article PR, enable Actions for the fork and
close and reopen the PR.

For setup problems, see
[Troubleshoot setup and scheduling](../troubleshooting/setup-and-scheduling.md).
