# Writer handoff: technical/github-taskflow-fuzzing (01)

## Completed

Wrote the complete, source-grounded walkthrough in the initialized article HTML. It explains the reported C/C++ taskflow architecture, paired AFL/coverage builds, coverage-driven iteration, crash triage, setup and host-execution risks. It distinguishes GitHub Security Lab's September 28 Android count from the fuzzing workflow and states the evidence limits around confirmation, remediation, and comparative performance. The article includes an explanatory sequence derived from the September 24 post, nine distinct linked sources, and citations ordered by first appearance. It does not claim to have executed or independently reproduced the taskflow.

The proof initially found the wrong series mode, a missing required `orientation` section, and unstamped counts; I corrected the mode and section and used `nb stamp`. I also resolved the citation-order warning. Final proof:

```text
/workspace/scratch/53797a806fdc/nightly-build/nb check /workspace/scratch/53797a806fdc/nightly-build/.nb-work/technical/github-taskflow-fuzzing/library/technical/github-taskflow-fuzzing.html --series technical --repo /workspace/scratch/53797a806fdc/nightly-build
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

Stamped counts: 1,231 words, 5-minute read, 9 sources.

## Runtime policy

The requested writer policy was capable/medium. This run used inherited GPT-6 at medium effort; the effort matched, but the runtime exposes no per-role model selector, so the requested capable model could not be selected. This is the policy deviation.

## Output

`/workspace/scratch/53797a806fdc/nightly-build/.nb-work/technical/github-taskflow-fuzzing/library/technical/github-taskflow-fuzzing.html`
