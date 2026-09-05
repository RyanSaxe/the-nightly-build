# Commission

## Assignment

Publish a source-first Paper of the Day edition that identifies the strongest
foundational paper on looped Transformers, teaches its technical innovations,
and explains how the research could relate to the reported GPT-6 Astra
architecture. The article must keep the Astra connection at the level the
public record supports.

## Focal paper

Angeliki Giannou et al., “Looped Transformers as Programmable Computers,”
ICML 2023. The paper is the focal source because it gives the clearest explicit
construction: a shallow Transformer with fixed, programmed weights is placed in
a loop and uses its input as instructions, memory, and scratchpad.

## Thesis

Looping turns Transformer depth into an execution-time resource. Giannou et al.
show the idea as a programmable computer; later work shows how training,
input injection, stability choices, and variable recurrence can turn the same
weight-sharing pattern into a learned latent-computation budget. OpenAI’s public
Astra announcement and system card do not specify this architecture. Secondary
reporting makes the connection plausible but does not confirm it.

## Required treatment

- Establish Universal Transformer (2018 / ICLR 2019) as an early recurrent-depth
  predecessor without claiming it was the first recurrent neural model.
- Explain the focal paper’s punchcard, scratchpad, memory, FLEQ/SUBLEQ, pointers,
  branches, function calls, and constant-depth/program-length distinction.
- Explain the learned-loop bridge through Yang et al. (2024) and Geiping et al.
  (2025), including input injection and training across recurrence counts.
- Explain why loop count can increase effective depth and serial FLOPs while
  leaving the shared block’s parameter storage fixed.
- Distinguish latent reasoning from visible chain-of-thought and distinguish
  architecture evidence from Astra safety findings.
- State concrete limits: hard-coded weights in the focal construction, synthetic
  task boundaries in the learned-algorithm work, proof-of-concept status in the
  recurrent-depth language model, and the unconfirmed Astra report.

## Shape

Use the paper template’s abstract card, orientation, six flex sections, source
figures, one annotated equation, and a final verdict. Target 2,300–2,800 words
and at least eight directly read sources. Use direct inline citations for every
argument-bearing claim.
