# writer brief: company-analysis/palantir (02)

Inputs:
  ../../editor/01/editorial-review.md       the three required fixes (read Skeptic + Required work)
  ../../researcher/01/evidence.md           the claim set (unchanged)
  ../../writer/01/draft-handoff.md          prior handoff
  the article: .nb-work/company-analysis/palantir/library/company-analysis/palantir.html
Output: writer/02/draft-handoff.md

Proof: ./nb check .nb-work/company-analysis/palantir/library/company-analysis/palantir.html --series company-analysis --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

Apply exactly the three editor/01 required fixes; the figures, both tables, the stat strip,
the chart, GAAP/adjusted separation, and sourcing are already verified clean — do not
disturb them, and do not expand the claim set.

1. Headline: it currently anchors the requirement on the U.S. commercial +149% quarter,
   which the body itself refutes. Reframe the headline to the requirement the article's
   arithmetic actually proves (roughly ~40% TOTAL revenue growth sustained ~4 years to grow
   into the multiple). State the requirement the piece establishes, not the 149% rate.
2. Dek: "U.S. commercial revenue to roughly triple" misattributes the tripling. The table,
   pull quote, and close all make it TOTAL revenue roughly tripling from the $8.15B guide.
   Fix the dekline and keep nb-meta `dek` byte-identical to it.
3. Closing coda: cut the self-grading / prompt-leaking sentences ("The commission was to
   weigh…", "is now stated as arithmetic", "is stated as its negation"). Keep the
   falsification handoff (the evidence that would change the paper's judgment). Relocate the
   orphaned CNBC citation (s11) to a sentence it actually supports, or drop it and update the
   source numbering/count so first-citation order stays correct and no source is unused.

Make the display-text pass again (headline, dek, subheads against the evidence). Keep
nb-meta harness "claude-code-routine" / model "Opus 4.8". Re-run the full proof to BLOCK: 0.
Note in the handoff exactly what you changed for each of the three items.
