# writer brief: opinion/vaccine-schedule-order (02)

Inputs:
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/agent-artifacts/opinion/vaccine-schedule-order/researcher/02/evidence.md  — the [02] additions: the Lancet 1998 source and the CRS reclassification
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/agent-artifacts/opinion/vaccine-schedule-order/editor/01/editorial-review.md  — the editor's routed items (the editor already applied its 9 direct edits to the article; do not undo them)
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/library/opinion/vaccine-schedule-order.html  — the editor-edited article; edit it in place

Output:
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/agent-artifacts/opinion/vaccine-schedule-order/writer/02/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/opinion/vaccine-schedule-order/library/opinion/vaccine-schedule-order.html --series opinion --library /home/user/library-checkout

Apply exactly the two routed sourcing fixes, nothing else. Preserve the editor's
direct edits already in the article.

1. Re-cite the descriptor "a case series of twelve children" to the source that owns
   it: Wakefield et al., The Lancet, 28 February 1998; 351(9103):637-641
   (https://www.thelancet.com/journals/lancet/article/PIIS0140673697110960/fulltext,
   now under a RETRACTED banner), classified primary for what the paper itself
   reported, with the retraction noted. If you judge the Lancet page's reader access
   too weak, the PubMed record (https://pubmed.ncbi.nlm.nih.gov/9500320/) is the
   fallback own-page. Keep Quackwatch (s12) only for the verbatim retraction/GMC
   statements it legitimately reproduces. If for any reason neither Lancet nor
   PubMed can anchor it, cut the twelve-children descriptor rather than leave it on
   Quackwatch.
2. Reclassify the CRS source (s4) from data-nb-kind="primary" to "secondary". Where
   the passage needs a primary statutory cite, cite the U.S. Code section directly
   (Section 222 of the PHS Act / 42 U.S.C. 217a; PHSA Section 2713 / 42 U.S.C.
   300gg-13; SSA Section 1928 / 42 U.S.C. 1396s), per the evidence record.

Renumber sources in first-citation order if the additions shift numbering. Keep
nb-meta harness "claude-code-routine", model "claude-opus-4-8", dek identical to the
rendered dekline. Run nb stamp, then the full proof (links included) until BLOCK: 0.
Write the draft-handoff with one line per routed item resolved and the final proof
result.
