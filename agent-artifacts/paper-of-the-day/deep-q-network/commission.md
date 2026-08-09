# Commission: paper-of-the-day/deep-q-network

## The paper and why rebuilding it clarifies something live

The paper is Mnih et al., "Human-level control through deep reinforcement
learning" (Nature, 2015), with its 2013 workshop precursor "Playing Atari with
Deep Reinforcement Learning" as the earlier record. Its central claim is that a
single network and a single algorithm, learning from raw pixels and the score
alone, reached human-level play across a large set of Atari games. Rebuilding it
clarifies an active technical problem, because the two tricks that made it work,
experience replay and a separate target network, are the paper's answer to why
naive Q-learning with a neural network diverges, and that stability question is
still central to deep reinforcement learning.

The reason this paper earns the night rather than a famous-result announcement
is its public record. A run of later work reopened not the model but the way the
field measured it: reproducibility studies that found results swinging on seeds
and implementation details, a re-examination of the Atari benchmark's evaluation
protocol, and a statistical re-analysis showing how thin the ground under many
reported gains was. The article should weigh the 2015 claim against what that
after-record established: what held, and what turned out to be an artifact of how
the score was computed.

## The reconstruction the template wants

- Set the objective honestly: the Q-learning update, the temporal-difference
  error the network descends, and the role of the target network and experience
  replay in it. Use the template's math furniture; do not paraphrase the update
  where the equation is the thing.
- Bring in the figures the claim turns on as source assets, not decoration. The
  per-game normalized-score comparison against a human tester is the figure the
  headline claim rests on; the low-dimensional embedding of the last hidden layer
  is the figure that shows what the network learned to represent. Caption each
  with what it settles.

## Template, sources, tags

- Template: `paper`. Required abstract card, reconstruction, and a verdict block.
  Source floor: 8.
- Sources must include the Nature paper and the 2013 precursor read firsthand,
  and the after-record studies (reproducibility, the Atari-evaluation
  re-examination, the statistical re-analysis) read to the passage, not to a
  summary. Numbers about scores, seeds, or protocols come from the primary that
  owns them.
- Tags: machine-learning, reinforcement-learning, reproducibility (metadata only).

## Production policy (resolved)

Run's model is Opus 4.8 across roles. Effort per `nb production-policy`:
writing-coach low, researcher high, writer medium, editor high (required).
Harness `claude-code-routine`; published `model` field reads `Opus 4.8`.

## Distinct value and habits not to inherit

The recent paper run is entirely language models and optimization; a
reinforcement-learning paper already reads as a change of subject, so let the
reconstruction lean into control and value estimation rather than borrowing the
framings those pieces used. The recent openers share a mold that names a
finding as a reversal or a "before it was asked to" turn ("Attention learned to
align long before it was asked to explain", "word2vec's most famous demo
predates word2vec"); do not open on that mold. The recent verdict sections tend
to a "A reviewer's verdict" heading; keep the required verdict block but name its
heading for this paper's own question. The abstract card and Sources heading are
fixed furniture.

## Boundaries

One paper, this slug. The after-record is here to weigh the 2015 claim, not to
become a full survey of deep-RL reproducibility. Rebuild the argument; do not
re-announce the result.
