# writer brief: opinion/hack-back-authorization (02)

Apply the required items in editor/01/editorial-review.md using researcher/02's
findings (single-owner-style repair; inputs and standard unchanged from
writer/01/brief.md; the editor's direct edits are already in the article and must
be preserved).

Two fixes:
1. Wysopal line: CNN carries it as indirect reported speech, not a verbatim
   quotation ("...could, for example, inadvertently affect a hospital, he said" —
   verb "affect," no quotation marks). Drop the quotation marks and render it as
   paraphrase/reported speech; do not present it as a direct quote.
2. "Active Cyber Defense Certainty Act": source s7 (CyberScoop) does not name the
   Act. Either generalize the clause to "earlier congressional proposals" (which
   s7 supports), or keep the Act's name and re-cite that clause to the verified
   TechTimes source researcher/02 records (adding it as a numbered source with the
   correct data-nb-kind). Pick one and make the citation land.

Do not expand the argument. Rerun the full proof (links included) with `nb stamp`
before the final check, until BLOCK: 0. Output: writer/02/draft-handoff.md (one
line per fix).

Proof: ./nb check --series opinion .nb-work/opinion/hack-back-authorization/library/opinion/hack-back-authorization.html --library /home/user/library-checkout
