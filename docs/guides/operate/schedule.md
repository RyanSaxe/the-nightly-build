# Schedule publication

The setup assistant and the scheduled runtime may be different products. Audit
the scheduled environment independently: it is the one that must check out the
paper, browse sources, push a branch, and open a PR while nobody is present.

## Runtime requirements

The scheduled runtime needs:

1. A schedule or on-demand trigger.
2. Current `main` plus access to `origin/main` and `origin/library`.
3. Outbound web access for research.
4. Permission to push generated branches and open PRs against `library`.
5. `uv` on `PATH`, or permission to install it.
6. Non-interactive permission to use every required tool.

Every run begins with `nb sync`, then asks `nb duty` for the deterministic work
list. One schedule can run the whole paper because series own their cadence.
`cadence: manual` series never appear as due.

Choose a scheduler only after its actual unattended environment meets all six
requirements. Candidate provider entrypoints are listed in
[Integrations](../../integrations/README.md), but a link to an automation
product is not proof that it satisfies this contract.

## Canonical prompt

Keep the external schedule prompt deliberately small:

> Work in The Nightly Build repository `<repo>` on current `main`. Read
> `.agents/prompts/run-scheduled-publication.md` and follow it in this agent.
> This paragraph is the entire assignment. If that file is unavailable, stop
> and report the missing repository entrypoint.

The repository owns the workflow; the scheduler only owns location and
authority. The scheduled agent itself becomes the orchestrator; it never
launches an orchestrator subagent. Replace prompts that restate commands, role
sequences, validation rules, or branch mechanics because those copies drift.

## Verification prompt

To test the exact scheduled environment without publishing, trigger an
on-demand task with this assignment:

> Work in The Nightly Build repository `<repo>` on current `main`. Read
> `.agents/prompts/verify-scheduled-runtime.md` and follow it in this agent.
> This paragraph is the entire assignment. If that file is unavailable, stop
> and report the missing repository entrypoint.

The smoke prompt opens and cleans up a draft PR against `main`. It never loads
the orchestrator or touches `library`.

Keep scheduler credentials out of the `library` PR workflow. Article validation
intentionally runs on `pull_request` with no scheduler secrets. See
[Publishing and security](../../concepts/publishing-and-security.md).

## Prove it before relying on it

Use [Verify the scheduled runtime](../../getting-started/first-run.md) for the
complete smoke-test boundary and result interpretation.
