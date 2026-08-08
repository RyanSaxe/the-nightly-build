# Agent and scheduler integrations

The Nightly Build does not depend on one model provider or agent product. It
depends on capabilities in the actual unattended environment: repository
access, live web research, non-interactive tool use, and permission to push a
branch and open a pull request. Checkout-based runtimes also need a current
checkout of `main` and `library`. The connector-only ChatGPT route uses GitHub
as durable state instead. See [Schedule](../guides/operate/schedule.md) for the
ordinary contract and [ChatGPT](chatgpt.md) for the connector-only adapter.

A paper needs a product for two jobs: manual work in a session you watch
(setup, publishing now, revising), and scheduled publication while nobody is
present. Some products do both through different surfaces.

## Verified

| Product     | Manual publication             | Scheduled publication                                                    | Billing      |
| ----------- | ------------------------------ | ------------------------------------------------------------------------ | ------------ |
| ChatGPT     | ✓ (connected GitHub app)       | ✓ ([Scheduled Tasks](chatgpt.md), connector-only)                        | Subscription |
| Claude Code | ✓ (local CLI)                  | ✓ ([Routines](https://code.claude.com/docs/en/routines))                 | Subscription |
| Codex       | ✓ (local CLI)                  | TBD ([Cloud automations](https://openai.com/academy/codex-automations/)) | Subscription |

A ✓ means that path has passed the non-publishing smoke test and published at
least one real article in that exact environment, and Billing records what
the verified runs drew down. Scheduled publication on Claude Code Routines
runs a production paper nightly. The ChatGPT path has been exercised through a
connected GitHub app with GitHub Actions limited to validation, protected
merge, and Pages publication.

## Other candidates

These products advertise the needed capabilities and likely work, but no
end-to-end run has been verified:
[Jules](https://jules.google/docs/scheduled-tasks/),
[Cursor](https://cursor.com/automate),
[Devin](https://docs.devin.ai/product-guides/scheduled-sessions),
[GitHub Copilot](https://docs.github.com/en/copilot/how-tos/github-copilot-app/using-automations),
and [OpenCode](https://dev.opencode.ai/docs/github/). A product's existence
does not prove that it meets the contract, and provider behavior,
permissions, and billing change independently. Before relying on one, run the
[scheduled-runtime smoke test](../getting-started/first-run.md) in the same
environment that will publish the paper.

## Harness independence

The orchestrator does not require a provider-specific team feature. A harness
may isolate bounded editorial roles in child contexts or execute the same
recorded sequence in one context. See
[Architecture](../concepts/architecture.md).

Model names are harness-specific. Portable tiers and exact provider overrides
are defined in [Production reference](../reference/production.md).
