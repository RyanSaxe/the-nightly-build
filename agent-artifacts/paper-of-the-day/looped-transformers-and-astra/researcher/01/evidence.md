# Evidence record

## Sources

1. **Primary focal:** Angeliki Giannou et al., “Looped Transformers as
   Programmable Computers,” ICML 2023,
   https://proceedings.mlr.press/v202/giannou23a.html. Abstract, Fig. 1,
   §§5.1–5.2, Informal Theorem 1, Lemma 4, and Table 1 were read. The input
   sequence is a punchcard with instructions, memory, and scratchpad. The
   Transformer output is fed back as the next input. FLEQ generalizes SUBLEQ
   with a selectable function block and conditional jump. The paper reports a
   9-layer/2-head SUBLEQ construction and 13-layer/1-head numerical and SGD
   constructions. The loop keeps network depth independent of program length;
   total execution still scales with executed instructions. Weights are
   explicitly programmed, so this is an expressivity construction, not evidence
   that ordinary pretraining discovers the same computer.

2. **Primary predecessor:** Mostafa Dehghani et al., “Universal Transformers,”
   ICLR 2019, https://arxiv.org/abs/1807.03819. Abstract and §§2.1–2.2 were
   read. The model recurs over representation depth, updates all positions in
   parallel with self-attention plus a transition shared across positions and
   time, and adds dynamic per-position halting. The paper states conditional
   computational universality and reports a 0.9 BLEU improvement on WMT14
   English–German over the comparison Transformer. This is an early precursor,
   not a claim of absolute historical priority.

3. **Primary learned algorithms:** Liu Yang et al., “Looped Transformers are
   Better at Learning Learning Algorithms,” ICLR 2024,
   https://arxiv.org/abs/2311.12424. Abstract, Fig. 1–2, §§3–5 were read. A
   one-layer looped GPT-2-style model has 0.79M parameters against a 12-layer
   9.48M comparison model. On controlled in-context function classes the looped
   model is comparable or better, with the paper’s abstract reporting less than
   10% of the parameter count. Input injection and training across loop outputs
   support stable fixed-point behavior. The experiments are synthetic and show
   distribution-shift limits; they do not establish a general solver for all
   input distributions.

4. **Primary language-model bridge:** Jonas Geiping et al., “Scaling up Test-Time
   Compute with Latent Reasoning: A Recurrent Depth Approach,” 2025,
   https://arxiv.org/abs/2502.05171. Abstract, Fig. 2, §§3.1–3.3, §5, §6, and
   §10 were read. The architecture is prelude P, shared recurrent core R, and
   coda C. It injects the input embedding every pass, initializes the latent
   state randomly, samples recurrence counts from a log-normal Poisson
   distribution, and backpropagates through the last eight iterations. The
   large model has shape (2,4,2), eight materialized layers, and effective depth
   132 at r=32. The proof-of-concept uses 3.5B parameters and 0.8T tokens; ARC-E
   is reported as 49.07 at r=4 and 69.91 at r=32. The paper calls the work a
   proof of concept and notes that recurrent depth spends more FLOPs per
   parameter.

5. **Primary reasoning analysis:** Nikunj Saunshi et al., “Reasoning with Latent
   Thoughts: On the Power of Looped Transformers,” ICLR 2025,
   https://arxiv.org/abs/2502.17416. Abstract, Fig. 1, and §§3–5 were read. A
   k-layer block looped L times is treated as effective depth kL; the analysis
   connects hidden intermediate states to latent thoughts and compares
   parameter-matched and compute-matched baselines. This supports plausibility
   for latent test-time computation, not a claim about Astra.

6. **Primary adaptive-compute follow-on:** Sangmin Bae et al.,
   “Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive
   Token-Level Computation,” NeurIPS 2025,
   https://arxiv.org/abs/2507.10524. The abstract and §§2–4 were read. Shared
   recursive stacks are paired with lightweight routers, active-token attention,
   and selective KV-cache reuse. This is a later design direction for uneven
   token difficulty.

7. **Official Astra announcement:** OpenAI, “GPT-6 Astra: A new generation of
   intelligence,” https://openai.com/index/gpt-6-astra/. The model description
   and evaluations were read. The page discusses capabilities, safeguards, and
   benchmarks, but does not specify a looped-Transformer or recurrent-depth
   architecture.

8. **Official Astra safety source:** OpenAI, “GPT-6 Astra System Card,”
   https://deploymentsafety.openai.com/gpt-6-astra. Sections on CoT control,
   monitorability, evaluation awareness, and covert sandbagging were read. The
   card supports claims about safety behavior and reduced monitorability in some
   settings; searches for “recurrent depth” and “architecture” did not yield a
   public looped-transformer specification.

9. **Secondary Astra report:** The Verge, “Researchers fear safety disaster ahead
   of OpenAI’s Astra release,”
   https://www.theverge.com/ai-artificial-intelligence/988334/openai-astra-ai-monitoring-safety.
   The article says The Information reported, citing an unnamed source, that
   Astra uses recurrent depth or looped-transformer cycles. It also says OpenAI
   did not confirm or deny the report and that the public announcement did not
   describe the technical foundation. Treat as reported and unconfirmed.

10. **Secondary technical caution:** Sebastian Raschka, “OpenAI Astra and Looped
    Transformers,” https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html.
    The discussion separates layer reuse from visible chain-of-thought: looping
    does not inherently make textual reasoning disappear. Use as an expert
    caution, not as primary evidence about Astra.

## Contradictions

- The Astra report says recurrent depth is used; OpenAI’s official announcement
  and system card do not confirm that architecture. The article must label the
  report as secondary and unconfirmed.
- “Same weights” means fewer distinct parameters, not zero added compute.
  Recurrent-depth work explicitly reports extra FLOPs and proof-of-concept
  limitations.
- Universal Transformer, Giannou’s programmed computer, learned algorithmic
  loops, and Geiping’s trained recurrent-depth LM share weight reuse but are not
  the same architecture or training regime.
- Latent thought depth may avoid emitting an intermediate token, but layer reuse
  alone does not erase visible chain-of-thought or establish safety.

## Numbers

- Giannou: 9 layers/2 heads for SUBLEQ; 13 layers/1 head for matrix inversion,
  power iteration, and SGD examples.
- Universal Transformer: 0.9 BLEU improvement on WMT14 En–De comparison.
- Yang et al.: 0.79M looped parameters vs 9.48M 12-layer baseline; 30-loop
  fixed-point illustration; abstract says under 10% of parameters.
- Geiping et al.: (2,4,2) architecture; effective depth 132 at r=32; 3.5B
  parameters; 0.8T tokens; ARC-E 49.07 at r=4 and 69.91 at r=32; eight-step
  truncated backpropagation.

## Source assets

- `asset-1.png`: bounded crop of Giannou et al. Fig. 1, showing the Transformer
  feedback loop and punchcard regions (scratchpad, memory, instructions).
- `asset-2.png`: bounded crop of Geiping et al. Fig. 2, showing prelude P,
  repeated recurrent core R, injected input e, and coda C.

## Discarded

- No claim that Giannou et al. invented all recurrent Transformer ideas.
- No claim that Astra definitely uses a looped Transformer.
- No claim that recurrent depth caused Astra’s benchmark or safety results.
- No claim that parameter reduction is equivalent to lower latency.
- No use of later training-free or scaling papers as evidence for the Astra
  architecture; they are outside the core argument.
