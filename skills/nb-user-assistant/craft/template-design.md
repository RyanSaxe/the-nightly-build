# Template design

Read `docs/reference/templates.md`,
`docs/guides/customize/templates.md`, current shipped templates, and
`spec/prompting.md` before designing.

## Establish necessity

A template is proof-enforced structure. Create one only when a recurring
article type needs invariant sections, citation geometry, chrome, or required
furniture that a series prompt cannot safely leave flexible. Test this claim
with several article ideas. If the same manifest would distort one of them,
the proposed template is too broad or the genre belongs in prose.

## Specify the reading experience

Write a brief naming:

- the reader's job and the article's distinctive contribution;
- fixed anchors and why each is invariant;
- where subject-specific reasoning must remain flexible;
- citation behavior and any justified exemptions;
- required furniture and what understanding it enables;
- headline, opener, transition, and ending character without sample copy;
- accessibility, responsive behavior, both themes, and long-content risks;
- representative cases, a counterexample, and acceptance criteria.

Choose fixed or flexible outline deliberately. Manifest bands are proof
recommendations, not a substitute for editorial identity. Put machine facts in
the manifest, instructional placeholders in the skeleton, editorial character
in `identity.md`, and bespoke components in furniture files.

## Rehearse the contract

Validate configuration, then fill the skeleton for at least two materially
different representative subjects. Run the full article proof and browser
preview. Inspect narrow and wide widths, both themes, source-heavy content,
long headings, and optional sections at their bounds.

Review the output as a reader and as an adversarial writer. If weak content can
satisfy the manifest, strengthen the smallest enforceable contract. If strong
content is forced into filler or repeated geometry, loosen it. Iterate the
brief, manifest, skeleton, identity, and furniture together until their
responsibilities are clean.
