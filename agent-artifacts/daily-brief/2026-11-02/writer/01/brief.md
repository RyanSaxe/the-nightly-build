# writer brief: daily-brief/2026-11-02 (01)

Inputs (all absolute):
- Editorial direction: .../agent-artifacts/daily-brief/2026-11-02/editorial-direction.md
- Commission: .../commission.md (the item plan, hard exclusions, boundaries)
- Evidence: .../researcher/01/evidence.md (the candidate items and their sources; choose from these, do not invent)
- Voice guide: .../writing-coach/01/voice-guide.md
- Article to edit: /home/user/the-nightly-build/.nb-work/daily-brief/2026-11-02/library/daily-brief/2026-11-02.html
- Markup contract + furniture: .nb-context/template-contract.yaml and .nb-context/furniture/{engine,press}.md under /home/user/the-nightly-build/.nb-work/daily-brief/2026-11-02/

Output:
- The article HTML above, edited in place.
- draft-handoff.md in .../writer/01/

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-11-02/library/daily-brief/2026-11-02.html --series daily-brief --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive for background. Where the evidence does not settle something, ask me (the orchestrator).

This round's focus:
- READ the commission's "Query decisions (orchestrator, after research 01)" section and follow it. In short: word is **nocebo** (reopen Merriam-Webster and quote its one-sentence definition verbatim); three news are (lead) US reportedly planning to resume Iran strikes after the midterms — ATTRIBUTE to the reports (WSJ/NYT, Channel 12), note Rubio says no decision, do not state as fact — then the Learjet 60 crash in Greenacres FL (1 Nov, nine killed) and Sen. Chris Murphy's stroke (1 Nov), with Carney-Trump trade progress as the alternate; two tech are Microsoft's school-AI privacy terms (tech 1) and Google Project Suncatcher (tech 2, cite the Google Research blog). Every news item rests on secondary reporting, so attribute each claim to the outlet.
- Template `brief`, strict: exactly six items in order — Word of the Day, three News, two Technology. Word band 300-700 is a HARD limit. Each item cited; the word card takes two sources (definition authority + independent history). Min 6 sources. Each news/tech item is two or three sentences: what happened, who did it or claims it, what follows.
- Choose the six from the evidence record by importance, favoring the US, all from 1-2 November 2026. Honor the hard exclusions in the commission (no DOJ Alaska/California ballot litigation, no Q3 GDP/PCE, no VA loans, no DC arch, no Nordhaus; no Binance hack anywhere — the feature owns it; no Mistral Large 4 / robots.txt draft / VOLTA / Cursor extension). If the evidence does not supply six usable, excluded-free items, tell me rather than padding.
- Word of the Day: not eggcorn, not bafflegab. One-sentence cited definition in the rs-word-card, then the documented origin in 3-4 sentences. Attribute unverified claims to their source.
- The headline + dek are the newsstand card: a finding-stating headline (subject + verb + surprise) for the lead item, and a dek that adds what the headline left out. No colon-subtitle, no question-mark headline, no negative-parallelism dek molds. Do not open on the DOJ/election-litigation beat a third day running unless a genuinely new and dominant election-law development demands it; vary the lead.

Fill nb-meta dates/harness/model (writer model: Claude Sonnet via Claude Code; harness: Claude Code). Number sources in first-citation order, carry each source's kind into data-nb-kind (a repeat on another website is not an independent primary), add data-nb-locator/url where the record gives it, and land each citation on the passage. Run `nb stamp` then the full `nb check` (links included) until BLOCK: 0. In draft-handoff.md record which six items you chose and why, and any warning you left on purpose. Report the handoff path.
