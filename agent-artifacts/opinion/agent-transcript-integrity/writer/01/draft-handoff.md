# Draft handoff

## Draft

The article is at:

`.nb-work/opinion/agent-transcript-integrity/library/opinion/agent-transcript-integrity.html`

It is a 1,349-word Opinion article with four argument sections: the agents'
interest in transcript tampering, the distinction between a transcript and an
independent execution log, the scoring interface's causal-story incentive, and
the raw-capability countercase.

## Original work

This is original analysis written for The Nightly Build from the cited METR,
OpenAI, Hugging Face, NIST, Berkeley RDI, OpenAI Deployment Safety, and Modal
source records. It does not reproduce a source article or copy its structure.

## Proof

The draft passed deterministic proof with zero blocks and zero warnings:

```text
./nb check .nb-work/opinion/agent-transcript-integrity/library/opinion/agent-transcript-integrity.html --repo . --series opinion --library ../nightly-build-library --check-links
```

Result: `BLOCK: 0`, `WARN: 0`, `verdict: PUBLISHABLE`.

## Editor questions

- Does the three-record distinction remain clear to a reader who has not read
  the incident report?
- Are the METR figures qualified tightly enough that the article does not claim
  successful erasure?
- Does the countercase address raw-capability evaluation without weakening the
  position card?
