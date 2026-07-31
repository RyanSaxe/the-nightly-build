# Researcher brief — paper-of-the-day/emergent-abilities (01)

## Role
Load and follow `skills/researcher/SKILL.md`. High effort. Web access.

## Begin with these exact inputs
- `agent-artifacts/paper-of-the-day/emergent-abilities/editorial-direction.md`
- `agent-artifacts/paper-of-the-day/emergent-abilities/commission.md`

## Read and verify (open the primaries)
1. **Wei et al., arXiv:2206.07682.** Record: the paper title exactly as
   published, full author list, venue (TMLR) and year, the arXiv id and a
   resolving link, and the **abstract verbatim** (for the paper card). Capture
   their exact definition of an "emergent ability," the model families/benchmarks
   used (GPT-3, LaMDA, PaLM, BIG-Bench, few-shot prompting), and 1-2 specific
   tasks with the reported sharp curves. Note figure numbers.
2. **Schaeffer, Miranda, Koyejo, arXiv:2304.15004 (NeurIPS 2023).** Record the
   metric argument precisely: which metrics are "discontinuous/nonlinear"
   (exact string match, multiple-choice grade) vs "continuous/linear" (token
   edit distance, Brier score); the claim that emergence largely disappears
   under continuous metrics; the specific demonstration (which model, which
   tasks, e.g. the integer-arithmetic tasks on GPT-3/InstructGPT) and any
   quantitative result. Confirm the NeurIPS 2023 best-paper award with a source.
3. **The afterlife / what happened next (weigh the claim).** Find at least two
   credible follow-on sources: later analyses, defenses of emergence, critiques
   of the mirage argument, surveys on capability predictability, or notable
   citations. The point is to let the article judge where the debate landed, not
   to collect links. Note any place the two papers actually agree.
4. **Supporting primaries for the worked example:** BIG-Bench (Srivastava et al.,
   arXiv:2206.04615) and/or GSM8K (Cobbe et al., arXiv:2110.14168) as needed to
   present one concrete task with real numbers.

## Source floor & classification
Minimum 8 sources, all read and resolving. Classify each primary/secondary with
a one-line reason (the two focal papers are primary for their own claims).
Verify every number against the paper that owns it. Record exact locators
(section, figure, page/arXiv version). A 403/paywall is gated — use arXiv PDFs
/ abs pages / OpenReview; never record an unread URL.

## Output (write only this)
`agent-artifacts/paper-of-the-day/emergent-abilities/researcher/01/evidence.md`
Per the researcher skill: sources with URL + kind + why; the verbatim abstract
block ready to paste (clearly marked, with its citation); verified facts, quotes,
numbers with locators; the concrete worked example (task, metric, before/after
numbers); contradictions and points of agreement between the papers; candidate
excerpts (exact sentences worth `nb-excerpt` display); discarded sources with
reasons.

## Control signal
Return exactly one line:
`DONE researcher agent-artifacts/paper-of-the-day/emergent-abilities/researcher/01/evidence.md`
or `REQUEST <owner> <need>` / `BLOCKED researcher <reason>`.

## Scope discipline
`./nb` (after `export PATH="$HOME/.local/bin:$PATH"`) and web tools for focused
work only. Do not tour the repo or archive. Ask the correspondent for anything
missing.
