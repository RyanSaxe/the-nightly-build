# Draft handoff: NVIDIA OpenShell runtime controls

Article: `/workspace/scratch/53797a806fdc/nightly-build/.nb-work/technical/nvidia-openshell-runtime-controls/library/technical/nvidia-openshell-runtime-controls.html`

## Completed work

The article is an original 1,742-word technical walkthrough of NVIDIA OpenShell v0.1.0, organized around the boundary between agent choices and external enforcement. It covers Gateway policy delivery, Supervisor egress decisions, sandbox and Linux kernel controls, outbound/API policy, credential handling, and bounded log retention. Its YAML and request trace are explicitly illustrative and were not executed. It distinguishes the September 25 GitHub v0.1.0 release timestamp from the September 28 general-availability announcement, and separates OpenShell from the broader Open Agent Safety Platform and Sentry.

The piece cites 19 sources. Implementation claims are pinned to the v0.1.0 tag/commit where applicable. It includes versioned NVIDIA documentation, tagged source, Linux Landlock and seccomp documentation, OpenClaw's independently maintained integration documentation, and AP and Reuters reporting. OpenClaw documents a real integration surface but does not establish scale. The named Cadence, Slack, and Gecko Robotics deployment statements remain NVIDIA claims in the material reviewed.

## Limits stated in the article

- No independent adversarial evaluation, penetration test, error-rate measurement, or security-outcome study of v0.1.0 was found.
- The illustrative GET policy constrains method and path; HTTP GET is not guaranteed to be semantically side-effect-free, and the rule does not prove that a credential has read-only permissions.
- User filesystem rules may use `best_effort`; the article distinguishes them from the mandatory Landlock ABI v3 private-path baseline.
- Seccomp user notification delegates a syscall decision and is not, by itself, a security policy. The article describes it alongside Supervisor policy evaluation and the outer network fence.
- Credential isolation is protocol- and policy-dependent; the runtime does not establish model honesty, correctness, intent, or whether granted permissions are wise.
- Gateway logs are bounded and volatile unless exported. The default buffer is not described as a complete, durable, tamper-proof audit record.
- The article does not infer production scale, comparative security, or broad adoption from an architecture diagram, vendor demo, or integration documentation.

## Quote check

No direct quotations are used in the article. Exact implementation literals are limited to strings needed to reproduce or match configuration and source behavior, including `allow_network`, `best_effort`, and `no_new_privs`. No quotation exceeds source limits.

## Proof

Command: `/workspace/scratch/53797a806fdc/nightly-build/nb check /workspace/scratch/53797a806fdc/nightly-build/.nb-work/technical/nvidia-openshell-runtime-controls/library/technical/nvidia-openshell-runtime-controls.html --series technical --repo /workspace/scratch/53797a806fdc/nightly-build`

Result: **PUBLISHABLE**; 0 blocking findings. One non-blocking `W-CITE-ORDER` remains: source 17 is first cited before source 4 because the Open Agent Safety Platform distinction appears earlier in the article than subsequent network-rule sources. The source is cited at the claim it supports.

## Runtime deviation

The requested writer effort target was medium. The runtime model is inherited and reports only the GPT-6 family; a more precise model ID and independent effort setting are unavailable in this orchestrator. This deviation is recorded per brief.
