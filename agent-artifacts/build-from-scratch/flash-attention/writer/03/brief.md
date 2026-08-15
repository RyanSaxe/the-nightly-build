# writer brief: build-from-scratch/flash-attention (03)

One mechanical fix, overriding the round-02 instruction to keep source numbers
intact. That instruction conflicted with the house rule "number sources in
first-citation order," which is why the proof now warns W-CITE-ORDER.

Renumber all sources into strict first-citation order (the source cited first in
the body becomes source 1, and so on), reorder the Sources list to match, and
update every superscript number, href, and anchor accordingly. Change no content,
no data-nb-kind, no locator, and no citation's claim site — only the numbering and
list order. This clears W-CITE-ORDER honestly rather than by moving a citation off
its true claim site.

Rerun the full proof (links included) with `nb stamp` before the final check,
until BLOCK: 0 and W-CITE-ORDER is gone. Output: writer/03/draft-handoff.md.

Proof: ./nb check --series build-from-scratch .nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html --library /home/user/library-checkout
