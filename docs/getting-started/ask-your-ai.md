# Ask your AI

Give this repository to the AI tool you already use. It needs to work with
GitHub in one of two ways: a coding agent in a terminal with `gh` signed in, or
a product connected to your GitHub account that runs commands in a sandbox and
opens pull requests. It does not need to be the tool that later runs a schedule.

Fork the repository first, with only `main`. Then say:

> Help me set up my Nightly Build paper and write my first article about
> `<topic>`. Follow the repository's instructions.

With `gh`, the assistant runs `./nb setup` and needs nothing from you: the
settings the fork needs are made for you. Without a terminal, make the two
settings only you can make first, Pages and Actions, as [Set up](./setup.md)
shows; `nb setup` cannot read them back and lists both anyway, and if one is
missing the assistant gives it to you as one action with its URL. Never paste a
token into chat.

The article goes into Dispatches, the series every paper keeps for what you ask
for, and publishes through a pull request the repository's own check validates
and merges. Add "let me read it first" to your request and the pull request
opens as a draft that waits for you instead.

A chat with no sandbox cannot run the engine; ChatGPT Work, which runs commands
in one, can. [Integrations](../integrations/README.md) names the products that
have published from a fresh fork and walks through each.
