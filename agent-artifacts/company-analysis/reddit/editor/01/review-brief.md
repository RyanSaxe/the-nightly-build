# editor review-brief: company-analysis/reddit (editor/01)

Inputs:
- editorial-direction.md (artifact root) — the standard to enforce
- writer/01/brief.md (the exact writer brief — for instruction-leakage detection)
- commission.md (artifact root) — includes the "Research correction" (the ~-21% figure and the DAU-durability cause)
- writing-coach/01/voice-guide.md — the voice, licenses, do-not-reuse list
- researcher/01/evidence.md — the evidence to open as an opponent (full quarterly series)
- writer/01/draft-handoff.md — open the original-work sentence only on the third read
- The article at `library/company-analysis/reddit.html` (workspace root), its charts in `library/company-analysis/reddit/`, and `.nb-context/` template context
Output: editor/01/editorial-review.md

Recent-pattern notes: recent company-analysis (apple, boeing, alphabet, vertiv,
coreweave) state a figure-led finding in the dek; the "masks / already exceeds"
dek molds are barred. Vary heading shapes.

Round focus:
- Verify the load-bearing numbers against their owning primary: revenue $804.9M
  (+61%), EPS $1.25, Q3 guide $860-870M, US DAUq 53.2M missing 53.98M consensus
  and falling sequentially from 53.5M (first decline in five quarters), and the
  ~-21% close-to-close move ($178.04->$140.67). Confirm consensus and the stock
  price are labeled/attributed as SECONDARY (Reddit owns financials/guidance,
  not "what the Street expected" or the tape). Audit every data-nb-kind.
- Inspect all THREE charts: open each committed chart-N.py, confirm the numbers
  match the evidence/primary, and read each image as a reader (axes labeled,
  scales honest, the sequential-dip and consensus markers truthful, data source
  cited in the caption). Request corrections; never edit assets yourself.
- Confirm NO buy/sell/allocation call anywhere, and that the transferable
  lesson (price moves on the change in expectations) is earned, both reads
  steelmanned.
- Confirm the Q3 implied ~48% YoY growth is correctly derived from the primary
  series (writer derived it rather than citing a gated figure).
- Open every citation href as printed; it must resolve. Make surgical cuts;
  route any redraft. After direct cuts run `./nb stamp <article-path>` (file arg).
