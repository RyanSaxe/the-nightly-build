# review-brief: build-from-scratch/rotary-position-embeddings (editor/01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../writer/01/brief.md                  the exact writer brief (for prompt-leak detection)
  ../../writing-coach/01/voice-guide.md     craft standard and licenses (read first)
  ../../researcher/01/evidence.md           the evidence record (open as the skeptic requires)
  ../../writer/01/draft-handoff.md          original-work sentence (open on the third read)
  the article: .nb-work/build-from-scratch/rotary-position-embeddings/library/build-from-scratch/rotary-position-embeddings.html
  the .nb-context/ article template contract + furniture catalogs

Recent-pattern notes (break formulas):
- Recent BFS pieces (speculative-decoding, byte-pair-encoding) used a "from-scratch
  reproduction confirms X" dek and mechanism-as-subject headline. Confirm the headline/dek
  and section headings do not reuse those shapes.

This round's focus (skeptic read + code/chart audit, push hardest here):
- Verify the math against the evidence: the 2-D rotation, the relative-offset identity
  (<R_m q, R_n k> depends only on n-m), and theta_i = 10000^(-2(i-1)/d). Confirm the
  displayed equations are objects the prose reasons from, correct and correctly located.
- Audit the code demonstration as a reader would run it: the numbers shown must be the real
  numpy run (shift-invariance ~1e-15; the decay envelope). Confirm nothing is invented and
  the prose claims match the output. Inspect the committed chart-1.py provenance and read
  the rendered decay chart: labels, scale, and any implied trend must be honest and match
  the evidence.
- Verify the base constants in the wild (Mistral-7B = 10000, Llama-3-8B = 500000) and the
  YaRN one-line base change, each attributed to a resolvable source.
- Two attribution checks the writer flagged: (1) the "why base-scaling works" contention is
  presented conservatively as argued-not-settled, grounded only in YaRN's NTK framing —
  judge whether that honest, bounded statement stands (it should, unless it overreaches);
  do not demand citing unread competing-cause sources. (2) The NTK-aware origin (s10) is
  cited only for its verified title claim, with the formula attributed to YaRN Eq. 16 —
  confirm the piece does not overclaim usable long-context extrapolation (rotary degrades
  ~200 tokens past training length).
- Confirm the prototype-vs-real-system comparison says what the toy leaves out.
- Open every citation href as printed; it must land on the source's own page. Audit
  data-nb-kind labels.

After any direct cuts, run `nb stamp` (the writer runs the full proof). Route new-prose,
new-evidence, code, chart, or markup needs to the writer/researcher with the exact finding.
