# writing-coach brief: feature/jepsen-particledb (01)

Inputs:
- `../../editorial-direction.md` — the full standing editorial standard.
- `../../commission.md` — the story, finding, and the visual the piece is built around.
Output: `voice-guide.md` (write it beside this brief).

Work from these inputs. Do not tour the repository or the archive. Where
something you need is missing, ask me (the orchestrator).

Set the voice for a five-minute illustrated feature that holds a database's
advertised guarantees against what Jepsen measured. The register:
- **Even and unmalicious.** The piece reports a gap between claims and evidence;
  it does not mock Orkes or crow. State each advertised claim in the vendor's own
  words, then give the measured result. The facts carry the weight, so the prose
  stays flat and exact.
- **Precise about correctness.** The reader builds systems and knows transactions
  and concurrency, but not necessarily the full anomaly taxonomy. Define each
  anomaly in the clause where it first appears, in plain words, then use its
  standard name. One word per idea.
- **Built around the visual.** Each section earns a table or diagram; the prose
  says how to read it and what follows, and does not restate it. The finding is a
  single legible matrix, so the voice points at cells, not at adjectives.
- **No generalizing.** The failure forbidden here is the sentence that leaves
  ParticleDB behind for "databases", "vendors", or "marketing" as a class. Every
  sentence stays about this report and these claims. Test the edges hardest.

Pick one or two short exemplar passages that show this register — Jepsen's own
reports (Kyle Kingsbury) are the natural model for stating a vendor claim and
then the measured contradiction without heat; another careful correctness writer
is fine too. If you quote a passage, fetch the page and record its URL and
retrieval date. Keep the guide short and usable. Your own prose meets
`spec/slop.md`.
