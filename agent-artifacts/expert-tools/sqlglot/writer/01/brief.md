# writer brief: expert-tools/sqlglot (01)

Inputs:
- editorial-direction.md — house standard, citation rules, press voice, series prompt (artifact root)
- commission.md — assignment, angle, cost/trust questions, recent habits (artifact root)
- writing-coach/01/voice-guide.md — how this tool essay should sound
- researcher/01/evidence.md — the verified API details, costs, and maintenance record
- the initialized article: .nb-work/expert-tools/sqlglot/library/expert-tools/sqlglot.html
- template context under .nb-work/expert-tools/sqlglot/.nb-context/

Output: .nb-work/expert-tools/sqlglot/agent-artifacts/expert-tools/sqlglot/writer/01/draft-handoff.md
Proof: ./nb check .nb-work/expert-tools/sqlglot/library/expert-tools/sqlglot.html --series expert-tools --library /home/user/library-checkout

Show the one capability that changes the work with a minimal Python example that
proves value, not an installation tutorial. Name the tool and the work it changes
in the headline and section titles. State adoption cost and maintenance honestly
from the evidence. Use a code listing for the example (documented furniture only,
no article-authored scripts). Use inline <code> only for literal strings the
reader would type or paste.

Recent habits to break (detail in commission): find SQLGlot's own surprising
specific for the headline; do not copy the recent "Tool does one specific thing"
rhythm exactly, and vary the dek construction.

Correction to the commission (research finding): the commission's performance
framing ("performance vs. sqlglotrs") is out of date. As of the installed
release, the Rust `sqlglotrs` tokenizer is deprecated and no longer compatible;
the live accelerator is the mypyc-compiled `sqlglot[c]` build. Frame the speed
cost as pure Python vs. `sqlglot[c]`, treating `sqlglotrs` as a retired chapter,
per the evidence record.
