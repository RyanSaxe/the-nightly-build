# Ask your AI

Give this repository to the AI tool you already use. It needs to work with
GitHub in one of two ways: a coding agent in a terminal with `gh` signed in, or
a product connected to your GitHub account that runs commands in a sandbox and
opens pull requests. It does not need to be the tool that later runs a schedule.

Fork the repository first, with only `main`. Then say:

> Help me set up my Nightly Build paper and write my first article about
> `<topic>`. Follow the repository's instructions.

With `gh`, the assistant runs `./nb setup` and needs nothing from you: the
settings the fork needs are made for you. Without a terminal, first make the two
settings only you can change, Pages and Actions, as [Set up](./setup.md)
explains. `nb setup` cannot read those settings back, so it lists both. If one
is missing, the assistant gives you its URL and asks you to make the change.
Never paste a token into chat.

The article is published in Dispatches, the series for requested articles. A
repository check validates the pull request and merges it. Add "let me read it
first" to your request and the pull request opens as a draft. It stays unmerged
until you mark it ready.

A chat without a command sandbox cannot run the engine. ChatGPT Work can run
commands in a sandbox. [Integrations](../integrations/README.md) lists products
that have published from a fresh fork and explains how to use them.
