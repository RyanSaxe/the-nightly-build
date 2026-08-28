# editor review-brief: expert-tools/sqlglot (01)

Inputs (artifact root .nb-work/expert-tools/sqlglot/agent-artifacts/expert-tools/sqlglot/):
- editorial-direction.md, commission.md, writer/01/brief.md (with the performance-framing correction), writing-coach/01/voice-guide.md, researcher/01/evidence.md, writer/01/draft-handoff.md
- the article: .nb-work/expert-tools/sqlglot/library/expert-tools/sqlglot.html
- template context under .nb-work/expert-tools/sqlglot/.nb-context/

## Recent-pattern notes (compare display text for formula/catchphrase)
Recent expert-tools headlines:
- "Grapple.nvim tags a file by name, and the name points to a different file on every branch"
- "beartype type-checks a whole list by reading one random item of it"
- "Outlines masks every invalid token as a model decodes, so the output fits your schema by construction"
- "Atuin makes your shell history answer questions bash can't"
The construction "Tool + verb + one surprising specific mechanism" is the series' recurring headline shape. It is fine in kind, but flag a headline/dek that copies the exact rhythm of a recent one rather than finding SQLGlot's own specific.

## Round focus
Confirm the piece proves value with ONE worked example (runnable per the evidence's local run on release 30.17.0), not an install tutorial or feature tour, and that it names the tool and the work in the headline and section titles. Confirm adoption cost and maintenance are stated honestly, and that the speed cost is framed as pure Python vs. sqlglot[c] (mypyc) — NOT vs. the deprecated Rust sqlglotrs. Confirm inline <code> is used only for literal strings the reader would type/paste. Verify the code listing matches the evidence's verified outputs exactly.
