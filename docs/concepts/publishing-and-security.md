# Publishing and security

Every publication crosses a pull request to `library`. That PR is both the
review record and the security boundary.

The scheduled runtime is trusted to browse arbitrary pages, invoke models,
push generated work branches, and request a merge. It should receive the
narrowest repository and network authority that still permits those jobs.
Web content can prompt-inject an agent, so prose instructions are not a
sufficient containment mechanism.

The validation workflow uses `pull_request`, never `pull_request_target`. It
checks untrusted article bytes with read-only contents and no scheduler
secrets. The proof restricts the diff shape, validates article metadata and
source contracts, rejects active article content, preserves artifact history,
and requires rendered-browser success.

New articles auto-merge only when their series explicitly sets
`autopublish: true`. Revisions and owner curation never auto-merge. A revision
may change one published article and its matching assets, but it can only add
fresh numbered role artifacts; it cannot rewrite the historical record.

Protect `main` as well as `library` if the scheduled identity should not be
able to change trusted engine or press configuration directly. Review
`press/site.yaml` changes carefully because owner-declared, integrity-pinned
page assets run for readers.
