# draft-handoff: paper-of-the-day/instructgpt (writer/01)

## Original work (one sentence)

The article treats InstructGPT's Eq. 2 as the paper's real object and reads
Gao's over-optimization curves and DPO's closed-form derivation as two verdicts
on that one KL-regularized objective — over-optimization showing why its KL term
cannot be dropped, DPO showing its optimum needs neither the reward model nor the
RL loop — a durability read on the objective rather than the SFT→RM→PPO pipeline
that none of the three papers states about itself. The synthesis is visible in the
rl-objective → overoptimization → closed-form → verdict arc.

## Proof result

`nb check` (links included): **BLOCK: 0 — PUBLISHABLE**. Four warnings left
standing, each deliberately:

- **W-SENTENCE-DENSITY ×3.** Two are the required *displayed equations*
  themselves (the annotated Eq. 2 and the DPO loss): the density heuristic reads
  their TeX as prose, where `\;` thin-spaces register as semicolon clause-joins
  and the braces inflate the punctuation score. The third is a single-clause-join
  derivation sentence carrying two inline-math expressions (`log-ratio … is the
  KL divergence …, so β sets …`); its word/punctuation counts are inflated by the
  inline LaTeX the voice guide mandates be set in prose, and splitting it further
  would break the just-in-time notation. All genuine prose run-ons the heuristic
  found were split.
- **W-SOURCES-MIN (5 vs floor 8).** See the open question below; not paddable
  without inventing sources.

Independent check: every equation's TeX was validated against the real KaTeX
parser (6 displays, all inline spans, all legend terms) with zero parse errors —
the raw-TeX seen in any offline render is only the CDN being firewalled in the
build sandbox, not a defect. Both source assets (paper Fig. 2 pipeline → asset-1,
paper Fig. 1 win-rate → asset-2) were captured from the arXiv PDF and inspected;
crops retain every element the evidence record required (all three pipeline steps;
the win-rate y-axis labeled "vs 175B SFT", all five variant curves, error bars,
the 0.5 line).

## Open evidence / voice questions

1. **Source floor (evidence).** The commission set min 8; the evidence record
   supplies exactly 5 opened primaries (InstructGPT paper, OpenAI release, Gao,
   DPO/Rafailov, Saito). I cited only what the researcher opened and invented
   none, so the floor stands unmet. Honest routes to 8 would need the researcher
   to open sources the paper itself leans on but the record did not include —
   e.g. Christiano et al. 2017 (RLHF origin), Stiennon et al. 2020 (summarization
   RLHF), Askell et al. 2021 (the helpful/honest/harmless framing the orientation
   cites), Schulman et al. 2017 (PPO), or Park et al. 2024 (DPO length
   exploitation, flagged-but-unopened in the evidence's Discarded list). Needs a
   researcher decision, not a writer fix.
2. **Venue strings (evidence).** The record flagged Gao (ICML 2023) and DPO
   (NeurIPS 2023) venues as unconfirmed on the arXiv pages, so the source entries
   carry year only, and the InstructGPT entry likewise omits "NeurIPS 2022". If
   the editor wants venues printed, they need confirmation first.
3. **OpenAI release URL (source #2).** The researcher saw a 403 on
   `openai.com/index/instruction-following/` (gated, not dead). The links-included
   proof passed here, so it resolved through this run's proxy; the editor should
   still confirm the live URL at publication. The claim it carries is owned by the
   paper's abstract (#1), so #2 is never the sole support for any number.
