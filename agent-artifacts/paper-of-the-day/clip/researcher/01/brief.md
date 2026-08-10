# researcher brief: paper-of-the-day/clip (01)

Inputs:
- `agent-artifacts/paper-of-the-day/clip/editorial-direction.md` — citation standard, series territory, declared reader
- `agent-artifacts/paper-of-the-day/clip/commission.md` — the paper, the claim to examine, and the reconstruction

Output: `agent-artifacts/paper-of-the-day/clip/researcher/01/evidence.md`
Source policy: minimum 8 sources; consult the paper itself first.

Research questions the evidence record must answer:

- The exact contrastive objective: read the method section and record the loss
  precisely (symmetric cross-entropy over cosine-similarity logits, the learned
  temperature, batch construction). Capture it in a form the writer can set as an
  equation, with the paper's own notation.
- How the zero-shot classifier is constructed at inference from label text, and
  the prompt/ensembling detail that mattered for the ImageNet number. Record the
  exact zero-shot ImageNet result and what it was compared against.
- The effective-robustness claim: record the exact result (which distribution-
  shift datasets, the accuracy gaps, the "effective robustness" definition and
  the figure that shows it). Identify the specific figures (method figure and
  robustness plot) as source assets, where they sit in the paper, and what a crop
  must retain.
- The follow-on record: find and read the work that isolated the training-data
  distribution as the cause of the robustness (rather than the language objective
  or zero-shot evaluation), the robustness-evaluation framework the paper builds
  on, and any reproduction (for example OpenCLIP / large open image-text
  datasets). Record exactly what each established firsthand.
- Serious criticism or limits (data curation, bias, the gap between zero-shot and
  fine-tuned use). Record contradictions in full, including any place the follow-
  on evidence complicates the article's angle.

Classify every source primary or secondary with the authorship-and-stake test
(the CLIP paper is primary for its objective and results; a later paper is
primary for its own finding). Verify each number against the source that owns it.
In Source assets, name the exact figures the reconstruction should bring in and
what each settles. Report in your handoff whether the "data caused the
robustness" finding is well-established or itself contested.
