# Schedule publication

Read `docs/guides/operate/schedule.md` and the scheduled-runtime half of the
[capability audit](../references/capability-audit.md). A schedule is the second
thing a paper gets, after its first article, and only when the owner wants
articles to arrive without asking.

## Choose the runtime

The assistant in this chat and the runtime that runs overnight may be different
products, with different identities, tools, network rules, and approvals. Verify
only what the active environment can demonstrate; configuration shows intent,
not capability. Point the scheduler at the repository's own prompt,
`.agents/prompts/run-scheduled-publication.md`, in the form the schedule guide
shows, and never restate its steps in the scheduler's prompt.

## Decide main protection

A scheduled identity holds the same power over `main` the owner has. Offer the
choice once, plainly: unprotected keeps the owner's quick direct edits;
protected routes every change through a reviewed PR and keeps the scheduled
identity out of trusted configuration. The tradeoff lives in
`docs/concepts/publishing-and-security.md`. Either answer is valid. Record which
the owner chose.

## Offer the smoke test

Offer one on-demand run of `.agents/prompts/verify-scheduled-runtime.md` in the
exact scheduled environment: same repository, identity, network, and approval
mode. Do not turn the smoke into an article, a cadence change, or a production
run. Present its evidence and repair the narrow failed boundary when the owner
wants help. The owner may proceed with unverified capabilities; say which those
are.

## Give the paper a cadence

A schedule publishes what `nb duty` finds due. The scaffolded News Brief and
Feature are due daily and Dispatches never is, so a fresh paper has a morning
paper the first night the schedule runs. Adjust series or their cadence through
[update paper](./update-paper.md) or [create paper](./create-paper.md); one or
two daily series make a normal morning paper. Confirm the usage the owner can
sustain before multiplying cadence; `docs/reference/production.md` has the
observed per-role work.
