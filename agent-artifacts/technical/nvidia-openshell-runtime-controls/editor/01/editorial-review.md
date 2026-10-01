# Editorial review: NVIDIA OpenShell runtime controls

## Recommendation

**Approve.** The article has no required editorial changes remaining, and the exact `nb check` passes with zero blocks and zero warnings.

## Findings

- The task is explicitly illustrative and source-based, not a test run. Expected file and network outcomes are described as conditional or inferred rather than as observed execution.
- The article distinguishes the September 25, 2026 v0.1.0 GitHub tag and pinned commit from NVIDIA's September 28 general-availability announcement. It separates OpenShell, the broader Open Agent Safety Platform, and Sentry.
- Security language is scoped to configured controls and their failure boundaries: effective policy composition, optional Landlock `best_effort`, seccomp user notification plus the outer network fence, token permissions, and the limits of HTTP method filtering. The public GitHub request is described as not requiring credentials; provider credential substitution is described separately and conditionally.
- The adoption paragraph distinguishes a documented OpenClaw integration from NVIDIA's named deployment statements. Log claims describe a bounded, non-persistent Gateway buffer and direct operators to durable export for retention.
- Spot checks of the cited public v0.1.0 architecture, network-policy tutorial, release listing, and log documentation support the corresponding claims. The supplied local research and editorial input files were not opened under the requested file-inspection scope; no deployment or security test was performed.

## Edits made

- Kept the tag and commit pin in the opening and moved the dated GA/platform/Sentry context to the evidence section, where the announcement sources appear in citation order.
- Reordered and renumbered the source list to match first citation appearance, preserving each citation's source target. The check's citation-order warning is cleared.
- Left the walkthrough identified as illustrative and unexecuted; its existing caveats already cover policy composition, non-semantic `GET` behavior, conditional credential handling, and log retention.

## Proof

Command run exactly:

```text
/workspace/scratch/53797a806fdc/nightly-build/nb check /workspace/scratch/53797a806fdc/nightly-build/.nb-work/technical/nvidia-openshell-runtime-controls/library/technical/nvidia-openshell-runtime-controls.html --series technical --repo /workspace/scratch/53797a806fdc/nightly-build
```

Result:

```text
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

## Runtime editor-effort limit

Work stayed within the two authorized files. I used one focused editorial review, corrected citation ordering after proof surfaced warnings, and stopped after the exact check returned zero warnings. No other series or article files were inspected or changed.
