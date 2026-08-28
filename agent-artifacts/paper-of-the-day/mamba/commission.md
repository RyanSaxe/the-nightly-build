# Commission: paper-of-the-day/mamba

## Assignment

A Paper of the Day reconstruction of **Mamba: Linear-Time Sequence Modeling with
Selective State Spaces** (Gu and Dao, 2023; arXiv:2312.00752). Rebuild the
central claim: making the state-space model's parameters input-dependent
(selective, the S6 mechanism) lets a recurrent linear-time model match
Transformer quality on sequence modeling, and a hardware-aware parallel scan
makes it fast in practice. Reconstruct the mechanism and the math the argument
turns on, not just the headline result.

## Why this paper, and what to examine

Mamba clarifies an active technical problem: attention's quadratic cost in
sequence length, and whether a sub-quadratic architecture can replace it without
losing what attention buys. It has a rich public record to weigh the claim
against: Mamba-2 and the state-space-duality framing, hybrid models (attention +
SSM, e.g. Jamba), and documented criticism of pure SSMs on tasks that need exact
recall or copying from context. Examine the selectivity mechanism (why prior
linear-time SSMs like S4 were time-invariant and what input-dependence changes),
the hardware-aware selective scan (why selectivity breaks the convolution
shortcut and how the scan recovers speed), and the recall/in-context tradeoff the
later record exposes.

flash-attention was this series' reconstruction on 2026-08-21. Assume the reader
knows attention is memory- and compute-bound at long sequence length; do not
re-litigate that. This piece's work is the selective-SSM alternative and where it
wins and loses, weighed against what happened after publication.

## Angle and boundaries

- Set the math the reconstruction leans on (the SSM recurrence and its
  discretization, the selection that makes A/B/C or the step size
  input-dependent, the scan) using the paper's own formulation, rather than
  paraphrasing it. The paper template owns the abstract card, the reconstruction,
  the evidence review, and the verdict.
- Bring the paper's own figures the claim turns on into the article as source
  assets, captured from the paper with `nb asset`: e.g. the induction-heads /
  associative-recall result, the language-modeling scaling curves, and the
  throughput/benchmark figure. Each asset needs a caption and prose that say what
  it settles.
- State a verdict on the claim before the sources: what Mamba established, what
  the public record since has confirmed or qualified, and where the claim stops.

## Neighboring articles this edition

No overlap with the other six articles. Within the series, this is distinct from
flash-attention (an exact-attention kernel) and from the build-from-scratch
series' engineering reconstructions.

## Sources

Template floor (paper): at least 8 sources. The focal paper is the primary; the
figures and math come from it. Additional sources earn space only when they
change the interpretation: the follow-on and critical record (Mamba-2, hybrid
architectures, recall/copying analyses). Cite only what you open, at resolvable
URLs; quote the paper's exact sentence in a note where it earns display space.

## Production

Profile balanced. Researcher: effort high, model claude-opus-4-8. Writer: effort
medium, model claude-opus-4-8. Editor: effort high, model claude-opus-4-8.
Writing coach: effort low, model claude-opus-4-8. Harness: claude-code-routine.

## Recent habits to break

Recent reconstructions headline the paper's finding as a claim, often naming the
authors in the dek (FlashAttention computes exact attention without building the
full matrix; DPO makes the policy its own reward model). Keep the claim-first
headline but find Mamba's own; do not copy the last one's rhythm. Do not let the
piece become a description of the paper's figures; the reconstruction must derive
and weigh, using the figures as evidence.

## Required contribution

The reader finishes understanding how selective state spaces work, why the scan
is what makes selectivity practical, and an earned judgment of where Mamba
replaces attention and where the record says it does not, grounded in the paper's
own math and figures.
