# Kernels

A course in writing fast GPU kernels, from the execution model up to
FlashAttention. The course assumes deep learning fluency and no prior CUDA or
Triton. Each article is one lesson that builds on the last. Triton is OpenAI's
open-source GPU language and the layer PyTorch's `torch.compile` lowers to, so
the payoff of every lesson is runnable code.

Recap the previous lesson concretely before building on it, and close the body
with a self-check note (nb-note) of exercises answerable from the lesson alone.
The two bookends the `lesson` package requires carry the reason to read and the
takeaway; nothing in the body repeats them.

Show real code with the nb-code furniture: Triton in Python, CUDA in C++. Escape
the code as HTML: an unescaped `kernel<<<blocks, threads>>>` is read as a tag
and silently eaten. Keep listings short, honest, and runnable as printed.

Emphases:

- Reuse one running example across the course, so each lesson's numbers are
  comparable with the last lesson's.
- Real numbers over hand-waving, each cited. Every lesson measures the kernel it
  teaches.
- nb-steps suits any mechanism walked in order: a kernel's phases, a memory
  access pattern, a tiling scheme.
