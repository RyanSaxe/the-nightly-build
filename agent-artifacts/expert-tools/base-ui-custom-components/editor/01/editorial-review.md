# Editorial review: expert-tools/base-ui-custom-components (editor/01)

## Correct

The thesis is that Base UI is the strongest default behavior layer for a new, highly custom React interface, provided the product team owns the visible design and tests the assembled component. Four claims carry it: Base UI preserves switch and form behavior while the application changes markup and styling; the primitive does not supply labels, focus appearance, contrast, or product-level accessibility assurance; a durable stack assigns visual source, behavior, constraints, state fixtures, motion, and generation to separate tools; and React Aria is the better behavior default for collection-heavy and international products.

The Base UI claim held against its Switch documentation, composition contract, implementation, accessibility division of responsibility, and September 4 release notes. The draft initially put “focus ring” inside the behavior the primitive retains, which blurred the documented boundary. I changed it to focus order. I also narrowed the code caption from “every visible rule” to visible styling because the excerpt deliberately omits complete dimensions and finish.

The maintenance claim held as a dated record of 1.8.0 fixes. I removed the unsupported phrase that current maintenance “gives confidence” and left the release facts and the testing consequence. Issue 5659 still supports only the reporter's reproduction, not a maintainer-confirmed defect; the article says that explicitly and does not generalize from it.

React Aria's recommendation held. Adobe documents more than 50 style-free components, accessible drag and drop, keyboard multi-selection, table resizing, lower-level hooks, more than 30 languages, 13 calendars, five numbering systems, and right-to-left support. Those capabilities change the choice for data-dense and international products, so this is not a directory entry.

Both practitioner quotations match their first-party text word for word. Adam Wathan's sentence and shadcn's migration warning retain their original capitalization and punctuation. Every printed source URL landed on the intended document. All 16 `data-nb-kind="primary"` labels are correct for the claim made: product owners document their APIs and releases, the issue is primary for the reporter's observation, the essays are the speakers' own words, and the preprint is the authors' study.

## Reads well

I cut the empty sentence announcing that the switch example “makes the boundary visible”; the implementation now begins the section. I replaced an unsupported speed claim in the stack section with the exact ownership rule the table demonstrates. I also changed the AI sentence from a claim about speed to the narrower exploration loop supported by Vercel's workflow.

The heading “Base UI has a clear losing case” concealed the actual decision and repeated the subject pattern of the preceding headings. “React Aria wins on collections and internationalization” now lets a skim reader reconstruct the exception. The headline does not repeat the recent “Tool does X, and Y” mold, and the headings do not use the prohibited repeated “What” or “Where” construction.

## The experience

The code listing and decision table earn their space: the listing exposes the line between product-owned styling and retained switch behavior, while the table makes each named tool answer a distinct adoption question. The table is not a directory because every row includes the condition that changes the default.

The final verdict now ends with operational conditions for Motion and v0 instead of the vague phrase “after those boundaries are explicit.” What the article adds beyond the sources is a division-of-responsibility rule that turns separate product documents into one adoption decision, then identifies the requirements that overturn Base UI in favor of React Aria or an existing Radix system. That matches and sharpens the original-work statement in the draft handoff.

The final preview site built successfully. The environment had no Chrome, so the optional rendered-browser probe could not inspect layout and reported a skip. The repository proof, including link checks, completed with `BLOCK: 0`, `WARN: 0`, and `PUBLISHABLE`.

## Edits

Changed “focus ring” to “focus order” in the opening behavior definition.

Deleted the empty opener before the Switch documentation.

Narrowed the code caption from “every visible rule” to visible styling.

Removed the unsupported claim that recent maintenance itself gives confidence.

Rewrote the stack opener around dependency ownership and editable source.

Retitled the final section to name React Aria's winning requirements and aligned its section identifier.

Narrowed the AI claim from exploration speed to the exploration loop.

Replaced the vague last sentence with explicit conditions for adopting Motion and v0, and cited both sources.

Ran `nb stamp`; the computed metadata remains 1,461 words, six minutes, and 16 sources.

Ran the exact proof command from the brief; it returned no blocks or warnings.

## Decision

approve — the argument survives source audit, the accessibility boundary is explicit, React Aria earns its exception, and the article is publication-ready.
