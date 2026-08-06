# draft-handoff: paper-of-the-day/instructgpt (writer/02)

Sourcing round. Four foundational primaries woven into the lineage the article
argues (InstructGPT assembled and scaled an existing method, it did not invent
it), sources renumbered in first-citation order, OpenAI-release URL swapped, and
venue strings brought in line with the evidence record's flags. All round-01
equations, the headline verification, and the central finding are intact.

## New source total: 9 (was 5). W-SOURCES-MIN cleared.

## Sources added (and where cited)

- **[2] Stiennon et al. 2020, "Learning to summarize from human feedback"
  (NeurIPS 2020)** — pipeline section: the same SFT → reward-model → PPO-with-KL
  sequence, run a year earlier on summarization by an overlapping OpenAI team;
  the load-bearing evidence that the pipeline predates InstructGPT. Reprised in
  the verdict note.
- **[3] Christiano et al. 2017, "Deep Reinforcement Learning from Human
  Preferences" (2017)** — reward-model section, at the Bradley-Terry
  introduction: the preference-to-reward device (BT predictor fit by
  cross-entropy, then optimized as the RL reward), originally on Atari and
  robotics, which shows the idea predates language models. Reprised in the
  verdict note.
- **[4] Schulman et al. 2017, "Proximal Policy Optimization Algorithms" (2017)**
  — rl-objective section, where PPO is first named: the clipped-surrogate method
  that bounds a single update, i.e. what "optimize with PPO" concretely means in
  Stage 3.
- **[5] Ziegler et al. 2019, "Fine-Tuning Language Models from Human
  Preferences" (2019)** — rl-objective section, at the KL penalty: the first use
  of a KL leash to fine-tune a pretrained LM (GPT-2) from preferences, the
  lineage of InstructGPT's Eq. 2 middle term. Reprised in the over-optimization
  section for its self-reported reward hacking ("may be exploiting the fact that
  labelers rely on simple heuristics"), which foreshadows Gao, and in the verdict
  note.

Renumbered in first-citation order: OpenAI release 2→**6**, Saito 3→**7**, Gao
4→**8**, DPO/Rafailov 5→**9** (source [1] unchanged). First appearance of every
source now runs 1→9 in order; all nine hrefs resolve to their `<li>` ids.

## Other required changes
- **Framing correction.** The verdict note previously credited InstructGPT with
  "the objective it introduced." Corrected: the note now states InstructGPT did
  not introduce the machinery (Christiano owns preference-to-reward, Ziegler the
  KL leash on an LM, Stiennon the full pipeline) and names its genuine
  contribution as assembly and scale — carrying the pipeline to the open-ended
  API distribution at 175B, adding PPO-ptx, and sweeping model size.
- **OpenAI-release URL** is `https://openai.com/index/instruction-following/`
  (the non-citable cdn.production transport is not used).
- **Venue strings.** Only the venue the evidence record confirms on the arXiv
  page is printed: Stiennon = NeurIPS 2020. All others are given as arXiv
  preprints with year only (InstructGPT 2022, Christiano 2017, Schulman 2017,
  Ziegler 2019, Gao 2022, DPO 2023, Saito 2023); no venue was invented.
- All added sources carry `data-nb-kind="primary"` (each owns the claim it is
  cited for).

## Final proof

`nb check` (links included): **BLOCK: 0 — PUBLISHABLE**, sources = 9, words =
3256 (band 1800–3400), 14 min. **W-SOURCES-MIN is gone.**

Three W-SENTENCE-DENSITY warnings remain, unchanged from round 01 and left
deliberately: two are the required *displayed equations* themselves (the
annotated Eq. 2 and the DPO loss), whose TeX the density heuristic reads as prose
(`\;` thin-spaces register as clause-joins, braces inflate the score); the third
is a single-clause-join derivation sentence carrying two inline-math expressions
the voice guide mandates be set in prose. None is a genuine prose run-on;
splitting the equations is not possible and splitting the derivation sentence
would break just-in-time notation.

No git run.
