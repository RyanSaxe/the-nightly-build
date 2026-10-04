# Commission: feature/thomson-reuters-ross-appeal

## The assignment

On September 30, 2026 the U.S. Court of Appeals for the Third Circuit issued its
opinion in *Thomson Reuters Enterprise Centre GmbH v. ROSS Intelligence Inc.*,
affirming the district court's holding that ROSS's use of Westlaw headnotes to
build a competing legal-research tool was not fair use. Reporting describes it as
the first federal appellate ruling on whether using copyrighted material to train
an AI system is fair use.

Write the feature from the opinion itself. The reason to read it now is that an
appeals court has, for the first time, decided a fair-use question that every
pending AI-training case turns on, and the opinion's own reasoning both settles
less and says more than the one-line summary ("AI training is not fair use")
suggests.

## The original work this piece owes

The summary circulating is "a court ruled AI training is not fair use." The piece
does what the summary does not: read what the court actually decided, and mark the
exact line between what it holds and what it leaves open. Candidate spine (the
writer confirms against the opinion and the evidence record, and is free to find a
better one):

- What the court held, and on which fair-use factors it turned (the commercial
  and minimally-transformative use; the market harm, including harm to a market
  for licensing the material as AI training data).
- The limit the court drew itself. ROSS's system returned existing judicial
  passages rather than generating new text, and the opinion confines its holding
  and the intermediate-copying line of software cases (Sega, Sony, Google v.
  Oracle) to that situation. Pin down whether the opinion expressly reserves the
  generative-AI question and where.
- What that means for the generative-AI cases people are reading this to
  understand: the piece says plainly what this opinion does and does not control,
  separating what the court established from what is inference.

One sentence of original work, for the writer to confirm or replace: *this piece
separates what the Third Circuit actually decided from the "AI training is not
fair use" headline, by reading the opinion's own limits on its holding.*

## Boundaries

- Work from the opinion as the governing primary source. Where the opinion and
  secondary coverage disagree, the opinion governs.
- Be precise about the court, the posture (interlocutory appeal certified under
  the relevant procedure; affirmance of a summary-judgment ruling on fair use),
  the parties' exact names, the dates, and the docket number. Any of these in the
  headline, dek or a subhead must match the opinion.
- Fair to ROSS: state ROSS's fair-use argument in terms ROSS or the dissent (if
  any) would recognize before taking it apart.
- Audience: strong CS/math readers, not necessarily lawyers. Define every legal
  term of art (headnote, fair use and its four factors, transformative use,
  intermediate copying, interlocutory appeal) at first use.
- This is the edition's legal/copyright piece. The daily brief and the technical
  article do not cover it; do not stray into the OpenCode plugin API or the
  edition's AI-model news.

## Furniture available and encouraged

The press ships `rs-docket` (case docket) for exactly this kind of piece: parties,
court · docket no., stage/question/stakes. Use it to carry the standing case facts
so the prose can argue. A table contrasting the four fair-use factors as the
district court and the Third Circuit treated them may earn its place; the writer
decides. See `.nb-context/furniture/engine.md` and `press.md`.

## Template, sources, production

- Template: `article` (longread; 2–6 flex sections; 800–6000 words; per-section
  citations; `article` min 8 sources).
- `nb-meta`: series `feature`, slug `thomson-reuters-ross-appeal`, mode `open`,
  date `2026-10-04`.
- Source policy: `article` min 8 sources (`nb source-policy --series feature`).
- Production (`nb production-policy --series feature`): editor required, high
  effort, model inherit (run on the orchestrator's model). researcher capable/high,
  writer capable/medium, writing-coach capable/low. Recorded actual assignment:
  coach/researcher/writer on a capable model (sonnet-class), editor on the
  orchestrator's model (opus-class) at high effort. Reasoning effort is set by the
  run harness; no `required` directive was traded down.

## Neighbouring articles in this edition

- daily-brief/2026-10-04: Word of the Day + three news items + two technology
  developments (GPT-6.1 Sol launch; DeepMind SynthID Bio).
- technical/opencode-v2-plugin-api: a walkthrough of OpenCode V2's new plugin API.

No shared ground with either. Keep this piece on the ruling and its reasoning.

## Orchestrator decision (after researcher/01) — corrected spine

The researcher read the opinion in full (No. 25-2153, 3d Cir., filed Sept. 29, 2026;
canonical PDF https://www2.ca3.uscourts.gov/opinarch/252153p.pdf) and corrected my
initial spine. Adopt these corrections as decided:

- Date: the opinion was FILED Sept. 29, 2026 (under seal), unsealed later. Use Sept. 29.
- The opinion does NOT confine the software intermediate-copying cases (Sega, Sony,
  Google v. Oracle) to non-generative AI. It distinguishes them on NECESSITY: ROSS did
  not need the headnotes because the judicial opinions themselves were free (pp. 19–21,
  n.8). The piece must say this, not the "cabined to non-generative" line.
- Generative AI appears only in footnote 7 (p. 17), which says the DOJ/OpenAI concerns
  "do not apply here." The opinion does not say it reserves/declines/leaves open the
  generative question. Do not call it an express reservation; report exactly what the
  footnote does (sets those concerns aside as not presented), and treat any broader
  reading as the writer's clearly-marked inference.
- Factor outcomes: factors 1, 3, 4 against ROSS; factor 2 slightly for ROSS. The Third
  Circuit moved factor 3 AGAINST ROSS, reversing the district court's factor-3 finding
  for ROSS, without flagging the change. This factor-3 flip is a strong, underreported
  spine element — use it.
- The licensing-market-for-training-data harm is the third of three factor-4 market
  findings and rests on thin evidence (about two sentences, no license or price cited).
  Report its thinness; do not inflate it.
- Internal inconsistency worth a line: p. 22 references "25,000 headnotes" while
  liability covers 2,243.

Revised original-work sentence (writer confirms/sharpens): this piece separates what
the Third Circuit actually held in Thomson Reuters v. ROSS — a fair-use loss that turns
on the necessity distinction from the software-copying cases, a factor-3 flip made
without flagging, and a thin licensing-market finding — from the "AI training is not
fair use" headline, and shows the opinion touches generative AI only in a footnote that
sets those concerns aside rather than deciding them.

Fairness-to-ROSS note: ROSS's briefs were gated; ROSS's position is available only
through the opinion's recounting and one amicus (CCIA, Chamber of Progress, NetChoice).
State ROSS's argument from those sources and do not quote ROSS directly.
