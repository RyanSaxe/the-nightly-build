# writer brief: company-analysis/super-micro (02)

Apply the required items in editor/01/editorial-review.md, using researcher/02 for
the conduct-window citation (inputs and standard unchanged from writer/01/brief.md;
the editor's direct edits are already in the article and must be preserved).

Fixes:
1. DOJ passage citation (the blocker): source 15's href (Exhibit 99.1, a991.htm)
   does not contain the Liaw resignation / "not the result of a disagreement with
   the Company" language, which lives in the same 8-K's Item 5.02 body
   (smci-20260320.htm). Split source 15 into two entries (or add the Item 5.02
   body as its own source) and repoint that clause so the citation lands on the
   document that owns it. Keep the passage's careful attribution to the named
   individuals, the company's victim statement, and the disclaimer that nothing
   ties it to the reported numbers.
2. Conduct-window citation: the "2024-2025" window is not on the Al Jazeera page
   (source 14). researcher/02 verified Gizmodo states verbatim "between 2024 and
   2025." Repoint that citation from Al Jazeera to the Gizmodo source (add it as a
   numbered source with the correct data-nb-kind), or soften the claim to what the
   record supports if you prefer, but do not leave it cited to a source that does
   not own it.
3. Chart 1 label consistency: the Q4 FY25 point is labeled 9.4% while the stat
   strip and prose say 9.5% (both round 9.45%). Fix the chart script and re-render
   so the label matches, and re-inspect the PNG.

Update the nb-meta sources count for any added source. Rerun the full proof (links
included) with `nb stamp` before the final check, until BLOCK: 0. No buy/sell/
allocation call. Output: writer/02/draft-handoff.md (one line per fix).

Proof: ./nb check --series company-analysis .nb-work/company-analysis/super-micro/library/company-analysis/super-micro.html --library /home/user/library-checkout
