# Editorial review: build-from-scratch/rotary-position-embeddings (editor/01)

## Skeptic

Thesis: RoPE makes the attention score between two tokens depend, by
construction, only on the gap between their positions, and the distance-decay
the literature bundles with it is a bound aligned content can exploit rather
than a decay RoPE imposes on all content. The context-extension work then turns
on one number, the frequency base.

Load-bearing claims, each tested:

1. The 2-D rotation (Eq. 13) and the relative-offset identity. The displayed
   rotation matrix is the standard `[[cos,-sin],[sin,cos]]`, correct. The
   identity `<R_m q, R_n k> = q^T R_m^T R_n k = q^T R_{n-m} k` is correct:
   `R_m^T = R_{-m}` and `R_{-m}R_n = R_{n-m}`, so only the difference survives.
   The equation is set up as an object the prose reasons from (its own approach,
   its own consequence), matching the voice guide's demand that this identity be
   the turn of the argument, not an aside. Correctly located at RoFormer Eq. 11.

2. The frequency schedule `theta_i = 10000^{-2(i-1)/d}`. Correct and correctly
   reconciled with the code: the listing's `i = arange(d//2)` runs 0..d/2-1,
   which is the paper's `i-1`, so `base**(-2i/d)` equals `10000^{-2(i-1)/d}`.
   For d=4 this gives theta_1=1, theta_2=0.01, exactly as the prose states
   (verified by running the code). Cited to Eq. 13/Eq. 15.

3. Every demonstration number is the real numpy run. I reran the exact `rope.py`
   from the listing and the committed `chart-1.py`. Reproduced to the digit:
   baseline dot product -0.85; gap-3 logit -1.314201 at (2,5),(7,10),(100,103);
   gap-4 -0.234807 at (3,7),(9,13); gap-2 -2.146777 at (0,2). The "at most
   1.1e-15" shift claim is honest: max deviation from the mean over the 200-shift
   sweep is 1.110e-15 (max-min is 1.78e-15, deviation-from-the-single-value is
   1.11e-15, which is what "stays a single value, deviating by at most" names).
   Wavelength stretch: slowest wavelength is 54,410 positions at base 10000 and
   2,559,196 at 500000, i.e. "roughly fifty-four thousand" to "over two and a
   half million," and 500000/10000 = 50 ("fifty times larger"). All correct.

4. Chart honesty. Reran chart-1.py: aligned (query=key) normalizes to 1.0 at
   distance 0 and reaches 0.219 at 512 ("roughly a fifth"), oscillating on the
   way down; the 2000-pair random mean |logit| stays in 0.97-1.04 ("barely
   moves"). Read as a reader: both axes labeled, linear scale (no scale note
   owed), legend distinguishes the two series, caption cites base, head dim, the
   distance-0 normalization, and the committed script. The visual matches the
   numbers. Honest.

5. Base constants in the wild. Fetched the configs firsthand: Mistral-7B-v0.1
   ships rope_theta 10000.0 (hidden 4096, 32 heads => head_dim 128, 64 pairs);
   Meta-Llama-3-8B ships rope_theta 500000.0. Both match the prose. The head
   arithmetic (4096/32 = 128, 64 pairs) is correct.

6. The two flagged attribution checks both hold. (a) The "why base-scaling
   works" passage stays bounded: it says YaRN motivates the base change through
   NTK theory for a result "whose success is measured, not derived," and calls
   the account "argued more than settled." It does not assert a community
   disagreement, so it needs none of the unread competing-cause sources. It does
   not overreach. (b) The NTK-aware origin (s10) is cited only for the "circulated
   as NTK-aware, extended LLaMA with no fine-tuning" claim, which matches the
   verified post title; the formula `b' = b*s^{|D|/(|D|-2)}` is attributed to
   YaRN Eq. 16 (s9), not the Reddit post. The piece does not overclaim usable
   long-context extrapolation: the honest-limit section states rotary keeps
   improving only ~200 tokens past a 512 training window (vs sinusoidal's 20-50)
   and that RoPE "does not give long context for free," cited to ALiBi (s8).

7. Display text. Headline "Two rotated vectors remember only the distance
   between them" is the piece's largest true claim (the relative-only property),
   states a finding in the piece's own nouns, and breaks the recent BFS
   mechanism-as-subject / "reproduction confirms X" shape. Dek makes world claims
   (index-to-angle, the mechanism behind open-weight models, the single-constant
   context edit), adds the extension angle the headline omits, does not restate
   it, and is not one of the banned dek molds (no semicolon reversal, suspended
   question, or comma triad). Section headings reconstruct the argument as steps
   in the piece's own nouns.

8. Citations and labels. Opened the load-bearing hrefs (RoFormer, ALiBi, YaRN,
   Mistral, Llama-3, and cross-checked the two configs' contents); each lands on
   the source's own page. All ten `data-nb-kind` labels are `primary` and
   defensible: the two NousResearch config links are open mirrors carrying the
   gated Meta configs verbatim, justified in the evidence record, and used only
   to read shipped hyperparameters. No sourcing failure found.

No break retired any claim. The premise survives citation-by-citation and as a
whole.

## Cut

Three self-referential tells removed, all pure cuts:

- "so the rest of this piece builds those lines and reads the numbers they
  print" (orientation) narrated the article's own plan ("what follows"). The
  intent framing survives in the retained "The claim is small enough to check in
  a dozen lines of array math."
- "That is the finding the rest of the piece spends." (phase-cancels) was a
  signpost at a paragraph end; the paragraph now closes harder on "...here it
  holds identically, before any training, for every query and key," which is the
  identity's earned consequence the voice guide asks for.
- The heading "Same gap, same logit, run and confirmed" -> "Same gap, same
  logit." "run and confirmed" graded the section and echoed the "confirms X"
  cadence the review brief flagged; the trimmed heading still states the step.

Worst tell: the "rest of this piece" self-narration, twice. It was the only
recurring pattern and both instances are gone. No prompt leakage: the concrete
worked instance and the report-from-the-run stance execute the voice guide
rather than copy the brief; no planning labels or assignment-fulfilled claims
survive in the prose. The one loose phrase left standing, "Average the same
score over two thousand random query-key pairs," describes a mean of magnitudes;
the figure caption and legend specify "mean |logit|," so the factual label is
correct and the body reads as intended. Not worth a change.

## Reader

What the piece gives beyond its sources: RoFormer proves the aligned-case decay
bound; the article's own run adds the contrast the papers do not draw, that the
decay is a property of aligned content and the mean over random query-key pairs
stays flat. That reframes RoPE's decay as a bound a model may exploit, not one
RoPE imposes, and it is the article's original work (the draft-handoff's
original-work sentence). Both that answer and the honest-limit framing survive
the straight-through read; the piece does not restate its sources.

The prose sits with the voice-guide exemplars, not a median summary:
intent-framed equations that let the symbols take the step, a code listing that
stands with one line of purpose and one of result, numbers pinned to the run
that produced them, and a candid statement of what the toy leaves out
(q/k-only, interleaved vs half-split, base as a tuning knob). The headline reads
as the largest claim and the piece defends it.

## Edits

- Cut "so the rest of this piece builds those lines and reads the numbers they print" from the orientation section.
- Cut "That is the finding the rest of the piece spends." from the phase-cancels section.
- Trimmed the-run heading to "Same gap, same logit".
- Ran `nb stamp` (words 1922 -> 1894, reading_minutes 8, sources 10).

## Required work

None. No researcher, writer, or orchestrator work remains.

## Decision

approve — the math is correct and correctly located, every displayed number
reproduces from the committed run, the chart and citations are honest, and the
only defects were self-referential tells that surgical cuts removed.
