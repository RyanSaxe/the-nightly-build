# Agent and scheduler integrations

The Nightly Build does not depend on one model provider or agent product. It
depends on capabilities in the environment that does the work: a repository
checkout, access to `main` and `library`, live web research, non-interactive
tool use, and permission to push a branch and open a pull request. See
[Schedule](../guides/operate/schedule.md) for the scheduled contract.

A paper needs a product for two jobs. The first article, and every article you
ask for, happen in a session you watch. Scheduled publication happens while
nobody is present. Some products do both through different surfaces, and the two
can be different products.

## Verified

| Product      | First article                                     | Scheduled publication                                                    | Billing      |
| ------------ | ------------------------------------------------- | ------------------------------------------------------------------------ | ------------ |
| Claude Code  | ✓ ([walkthrough](./claude-code.md), local CLI)    | ✓ ([Routines](https://code.claude.com/docs/en/routines))                 | Subscription |
| ChatGPT Work | ✓ ([walkthrough](./chatgpt-work.md), no terminal) | TBD ([Cloud automations](https://openai.com/academy/codex-automations/)) | Subscription |
| Codex        | ✓ (local CLI, no walkthrough)                     | TBD ([Cloud automations](https://openai.com/academy/codex-automations/)) | Subscription |

A ✓ under "First article" means that product took a fresh fork to a published
article on 2026-09-18, and the walkthrough is written from that run. A ✓ under
"Scheduled publication" means the path passed the non-publishing smoke test and
published at least one real article in that exact environment. Scheduled
publication on Claude Code Routines runs a production paper nightly.

## Other products

Most products that pair a sandbox with a GitHub connection will work; only the
ones above are documented. [Jules](https://jules.google/docs/scheduled-tasks/),
[Cursor](https://cursor.com/automate),
[Devin](https://docs.devin.ai/product-guides/scheduled-sessions),
[GitHub Copilot](https://docs.github.com/en/copilot/how-tos/github-copilot-app/using-automations),
and [OpenCode](https://dev.opencode.ai/docs/github/) advertise the needed
capabilities, and no end-to-end run has been verified. A product's existence
does not prove that it meets the contract, and provider behavior, permissions,
and billing change independently. Before relying on one for a schedule, run the
[scheduled-runtime smoke test](../guides/operate/verify-scheduled-runtime.md) in
the same environment that will publish the paper.

## Harness independence

The orchestrator does not require a provider-specific team feature. A harness
may isolate bounded editorial roles in child contexts or execute the same
recorded sequence in one context. See
[Architecture](../concepts/architecture.md).

Model names are harness-specific. Portable tiers and exact provider overrides
are defined in [Production reference](../reference/production.md).
