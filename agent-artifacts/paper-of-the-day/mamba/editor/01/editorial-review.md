# Editorial review: paper-of-the-day/mamba (editor/01)

## Skeptic

Thesis: making a linear-time state-space model's parameters input-dependent
closes the language-modeling gap to attention, a hardware-aware scan makes that
selection practical once it forecloses the convolution, and the fixed-size state
that buys the cheap inference is the same thing that caps recall from long
context. The piece stands on four claims, and each derives rather than asserts.

1. Selection is the cause, not the block it sits in. Rests on the
   selective-copying ablation. The table's numbers (S4 no-gate 18.3; S6 no-gate
   97.0; H3+S4 57.0, H3+S6 99.7; Mamba+S4 56.4, Mamba+S6 99.8) match the evidence
   and the paper's Table 1 at pixel level, which I re-read from the PDF. The
   reading is correct: swap the inner layer and the score moves, change only the
   surrounding block and it does not. Held.

2. Selectivity forecloses the global convolution, so the scan is required. This
   is derived from the math, which is the round's whole point. I checked every
   equation against the evidence: the continuous SSM, the ZOH discretization
   (A-bar = exp(ΔA), B-bar = (ΔA)^{-1}(exp(ΔA) − I)·ΔB), the discrete recurrence,
   the convolution kernel, and the selection assignment (B, C = Linear_N(x); Δ =
   softplus(Parameter + Broadcast_D(Linear_1(x))); A learned per-channel,
   selective only through Δ; shapes (D,N) → (B,L,D,N)). All correct. The prose
   earns each equation in the sentence after it, and the shape change is named as
   exactly what kills the single kernel. Held.

3. Mamba matches a Transformer twice its size. Rests on the scaling curves and
   the zero-shot table. Numbers verified against the evidence and the PDF's Table
   3 (Mamba-2.8B 6.22 / 69.2 / 63.3; Pythia-2.8B 6.73 / 64.7 / 59.1; Mamba-1.4B
   6.80 / 64.9 / 59.7). The sharp reading is the writer's own: Mamba-1.4B edging
   Pythia-2.8B on the average (59.7 vs 59.1) is the "twice the size" claim made
   concrete, and the direction is right. Held.

4. The scan pays and the throughput is real, with the limit stated. Crossover at
   ~2K, faster than FlashAttention-2 beyond it, 20–40x over a naive scan, 4–5x
   inference throughput from the absent KV cache. All match the evidence and the
   paper's Figure 8. The piece keeps the crossover honest rather than hiding it.
   Held.

I pushed hardest on the claim the piece most wants to keep, the million-length
induction-head win, because over-reading it is the failure the brief named. The
article does not over-read it. It states plainly that induction heads is a single
lookup a fixed state can hold, that the figure says nothing about many items at
once or verbatim copying, and it routes those to the later critical record. The
verdict repeats the boundary and never presents Figure 2/Table 2 as general
recall parity. This is the reconstruction's hardest requirement and it is met.

Display text checked descriptor by descriptor. Authors (Gu, Dao), arXiv id,
version, task names, model sizes, sequence lengths, and the Chinchilla/Pile
framing all check against the paper. Every `data-nb-kind` is primary and is
correct for what each source is cited for: Zoology, Jelassi, Waleffe, and Merrill
own their own theorems and measurements, so each is primary for the finding the
article spends it on, and the recall study is correctly attributed as framing
(its models predate Mamba) rather than a measurement of Mamba. All eight source
hrefs resolve to the papers themselves.

One miscitation found and fixed. The induction-heads asset carried
`data-nb-locator="Fig. 2 (right) / Table 2"`. I read the PDF: the extrapolation
plot the asset shows is Table 2 (p.11, "trained on 2^8=256 ... tested up to
2^20=1048576, full numbers in Table 11"), which matches the image exactly.
Figure 2 (p.6) is a different object, the task-schematic illustration whose
panels are the copying, selective-copying, and induction-heads task diagrams, not
the accuracy plot. The correct label (Table 2) was already in the locator, so I
removed the wrong "Fig. 2 (right)" cross-reference. Everything the citation is
cited for is unchanged. The other three PDF labels the writer corrected are right
as printed: Table 1 (Selective Copying, p.11), Figure 4 (Scaling Laws, p.11),
Table 3 (Zero-shot, p.12), Figure 8 (Efficiency, p.15).

## Cut

The piece is disciplined; the slop pass turned up two sentences, both at the
positions slop collects.

- "Time-invariance is the whole reason the identity holds" is the "X is the whole
  Y" construction, and the sentence after it ("One kernel serves every position
  because the dynamics are the same at every position") carries the actual
  mechanism, restating time-invariance in working terms. The topic label added
  nothing the mechanism sentence did not. Cut.
- "The absent cache is what frees the memory" closed the throughput paragraph by
  restating its opening ("no key-value cache, it can run at batch sizes a
  same-size Transformer cannot fit") and the "batch-size effect" attribution one
  sentence earlier. It fails the delete test: no new fact, claim, or step. Cut.
  The paragraph now ends on "a batch-size effect, not faster arithmetic," which
  corrects a real misreading of where the speed comes from and earns the close.

I checked the three surviving negative-parallelism constructions ("a batch-size
effect, not faster arithmetic"; "never SSM against attention as rival species,
but a dial"; "match that recipe rather than merely beat weaker ones"). Each
corrects a misconception the piece actually names, so each is an earned contrast
rather than an invented one, and all three stay.

Furniture pulls its weight: the equation blocks with legends carry the math, the
two nb-tables carry the copying and zero-shot numbers as numbers, the nb-steps
split the scan into its two real ideas, and the holds-up/verdict pair states the
bounded judgment the template requires. No component is decoration or a repeat of
a prior article's shape. Headings each name a step of the argument and
reconstruct it in order; none is a scaffolding slot. Against the recent-pattern
notes, the headline keeps the series' claim-first shape but finds Mamba's own hook
("a state that never grows") rather than copying the FlashAttention or DPO
rhythm, and the dek does not reuse a recent mold. No prompt or brief language
leaked into the prose, and the piece never narrates itself.

## Reader

What the article gives that the sources alone would not: a single mechanistic
thread from the recurrence through discretization, selection, the lost
convolution, and the scan that recovers it, ending in one property — a state of
fixed size — that explains both the throughput win and the recall ceiling, so the
induction-head result and the copying failures stop looking contradictory. That
is the writer's original synthesis in the draft handoff, and it survives the read.
flash-attention is used only as a benchmark curve and a one-clause analogy, never
re-explained. The prose sits with the voice-guide exemplars, not a median
summary: it sets the equations and spends the sentence after each on what it now
makes possible, and it refuses the loose "learns to attend to what matters" telling
in favor of the precise input-dependent-parameters version, the Gundersen move the
guide asks for. The headline reads true as the largest claim.

## Edits

- Cut "Time-invariance is the whole reason the identity holds." from the
  convolution section (slop, "X is the whole Y"; the next sentence carries it).
- Cut "The absent cache is what frees the memory." from the scan section
  (restatement, fails the delete test).
- Corrected the induction-heads asset locator from "Fig. 2 (right) / Table 2" to
  "Table 2 · §4.1.2 · p. 11" (verified against the PDF; the asset is Table 2, and
  Figure 2 is the unrelated task-schematic illustration).

## Required work

None blocking.

- writer (informational, non-blocking): the draft handoff records the induction
  result's PDF label as "Fig. 2 / Table 2." Only Table 2 is right; Figure 2 is the
  task-schematic illustration on p.6, not the extrapolation plot. The article is
  already corrected; noting it so the belief does not carry into a later capture.
  The "untrained Mamba-6.9B" qualifier is the paper's own word (§4.5, verified),
  so it correctly stands.

## Decision

approve — the reconstruction derives the mechanism and weighs the record to a
bounded verdict, the math and numbers check against the paper, and the two slop
cuts and the one locator fix are done in place with nothing left that blocks
publication.
