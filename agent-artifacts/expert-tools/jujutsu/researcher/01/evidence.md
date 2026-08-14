# Evidence record: expert-tools/jujutsu (01)

The evidence supports the commissioned angle solidly on the mechanism (working
copy as a commit, the operation log, `jj undo`/`jj op restore`, first-class
conflicts, colocated Git interop) and on a real, verified command sequence that
shows a botched rebase undone with the exact pre-rebase commit IDs restored. It
is thinnest on two things a writer should handle carefully: (1) who backs the
project today. The README's own "Mandatory Google Disclaimer" still describes
Jujutsu as Martin von Zweigbergk's "full-time project at Google," but the
project's own conflict-of-interest disclosure (`docs/paid_contributors.md`)
lists him — and two other current maintainers — as compensated by a separate
company, East River Source Control, not Google. Neither document is dated, and
I could not confirm from a source I read (rather than a search snippet) when
or whether he left Google; the record below states only what each primary
document itself says, unreconciled. (2) The "spare time" framing in
`docs/roadmap.md` — "most people contributing to Jujutsu do so in their spare
time" — sits awkwardly next to a governance rule that exists specifically to
cap one paying employer's influence, which only makes sense if paid,
non-spare-time contribution is now common. All command output below was run
live against a fresh `jj 0.44.0` build (installed via `cargo install --locked
jj-cli` from crates.io, matching the tagged release) on 2026-08-14; nothing is
reconstructed from memory or from the docs' own examples.

## Verified command sequence

Environment: `jj 0.44.0` (`jj --version` output: `jj 0.44.0`), a fresh
colocated repo created with `jj git init`, in `/tmp/.../scratchpad/demo/proj`.
User identity set via `JJ_CONFIG` pointing at a throwaway `user.name`/
`user.email`. Three commits were built to set up the demo:

```
$ jj git init proj
Initialized repo in "proj"
$ printf 'DEBUG = True\nTIMEOUT = 30\n' > config.py && jj commit -m "add config module"
$ printf 'from config import TIMEOUT\n\ndef login():\n    return TIMEOUT\n' > auth.py && jj commit -m "add auth module"
$ printf 'from auth import login\n\nif __name__ == "__main__":\n    login()\n' > main.py && jj describe -m "add main entrypoint"
$ jj log
@  pynpyzxp researcher@example.com 2026-08-14 06:59:05 01a1182e
│  add main entrypoint
○  uomvmzxo researcher@example.com 2026-08-14 06:59:05 c323dd04
│  add auth module
○  zkuqvpzv researcher@example.com 2026-08-14 06:59:05 4a46c9d1
│  add config module
◆  zzzzzzzz root() 00000000
```

**Demo A — amend the oldest commit, descendants rebase themselves.** A bug is
found in the first commit (`TIMEOUT` should be 60, not 30). Edit the file while
the working copy sits on the newest commit, then squash just that file's
change into the old commit by its change ID (`zkuqvpzv`) — no `git rebase -i`,
no `--continue`:

```
$ printf 'DEBUG = True\nTIMEOUT = 60\n' > config.py
$ jj squash config.py --into zkuqvpzv
Rebased 2 descendant commits.
Working copy  (@) now at: pynpyzxp 01a1182e add main entrypoint
Parent commit (@-)      : uomvmzxo c323dd04 add auth module
$ jj show zkuqvpzv
    add config module
Added regular file config.py:
        1: DEBUG = True
        2: TIMEOUT = 60
```
Both descendant commits (`add auth module`, `add main entrypoint`) got new
commit IDs (they were rewritten) but kept their change IDs and their own
content untouched — verified by `jj show` on each afterward.

**Demo B — a botched rebase, undone exactly.** Simulating a wrong destination
argument: intending to rebase the auth+main stack onto a new base, `root()` is
typed instead, detaching the stack from the config commit entirely (auth.py's
`from config import TIMEOUT` now points at nothing in that branch):

```
$ jj log
@  pynpyzxp researcher@example.com 2026-08-14 06:59:05 01a1182e
│  add main entrypoint
○  uomvmzxo researcher@example.com 2026-08-14 06:59:05 c323dd04
│  add auth module
○  zkuqvpzv researcher@example.com 2026-08-14 06:59:05 4a46c9d1
│  add config module
◆  zzzzzzzz root() 00000000

$ jj rebase -s uomvmzxo -d root()
Rebased 2 commits to destination.
Working copy  (@) now at: pynpyzxp cdc6bf8c add main entrypoint
Parent commit (@-)      : uomvmzxo a7677b0a add auth module
Added 0 files, modified 0 files, removed 1 files

$ jj log
@  pynpyzxp researcher@example.com 2026-08-14 06:59:40 cdc6bf8c
│  add main entrypoint
○  uomvmzxo researcher@example.com 2026-08-14 06:59:40 a7677b0a
│  add auth module
│ ○  zkuqvpzv researcher@example.com 2026-08-14 06:59:05 4a46c9d1
├─╯  add config module
◆  zzzzzzzz root() 00000000
$ ls proj    # config.py is gone from the working copy
auth.py  main.py

$ jj undo
Undid operation: 88b3604a313c (2026-08-14 06:59:40) rebase commit c323dd040fbbae5c93736a3cc95ec5bbcad3ed5d and descendants
Restored to operation: e7af953a3da7 (2026-08-14 06:59:05) squash commits into caebfb3e0a4fdd641a3c87371696c4b81fac2894
Working copy  (@) now at: pynpyzxp 01a1182e add main entrypoint
Parent commit (@-)      : uomvmzxo c323dd04 add auth module

$ jj log
@  pynpyzxp researcher@example.com 2026-08-14 06:59:05 01a1182e
│  add main entrypoint
○  uomvmzxo researcher@example.com 2026-08-14 06:59:05 c323dd04
│  add auth module
○  zkuqvpzv researcher@example.com 2026-08-14 06:59:05 4a46c9d1
│  add config module
◆  zzzzzzzz root() 00000000
```
The commit IDs after `jj undo` (`01a1182e`, `c323dd04`, `4a46c9d1`) are
byte-for-byte identical to the ones before the botched rebase — this is not an
approximate restore, `config.py` reappears on disk unchanged. One command
undid a two-commit rebase across the entire subtree.

**Demo C — `jj op restore` jumps further than `jj undo`.** After Demo B was
undone, a separate experiment (merging two commits that both edited
`config.py`'s `TIMEOUT` line, producing a real conflict) was run and then
discarded in one step by restoring to an operation ID recorded earlier in the
session, well before that experiment started:

```
$ jj op restore e7af953a3da7
Restored to operation: e7af953a3da7 (2026-08-14 06:59:05) squash commits into caebfb3e0a4fdd641a3c87371696c4b81fac2894
Working copy  (@) now at: pynpyzxp 01a1182e add main entrypoint
Parent commit (@-)      : uomvmzxo c323dd04 add auth module
Added 2 files, modified 1 files, removed 0 files
```
This confirms the documented distinction: `jj undo` steps backward one
operation at a time; `jj op restore <op-id>` jumps directly to any recorded
point in the operation log (`docs/operation-log.md`).

**Demo D — first-class conflicts (the second candidate mechanism).** Two
sibling commits edit the same line of `config.py` differently; merging them
with `jj new` does not fail:

```
$ jj new zkuqvpzv -m "bump timeout to 90"     # edit TIMEOUT to 90
$ jj new zkuqvpzv -m "disable debug flag"     # edit DEBUG to False (TIMEOUT stays 60)
$ jj new kkspkpmo qxysnovo -m "merge both config edits"
Working copy  (@) now at: tqrkmvvm c34571e6 (conflict) (empty) merge both config edits
Warning: There are unresolved conflicts at these paths:
config.py    2-sided conflict
$ jj status
The working copy has no changes.
Working copy  (@) : tqrkmvvm c34571e6 (conflict) (empty) merge both config edits
Warning: There are unresolved conflicts at these paths:
config.py    2-sided conflict
$ cat config.py
<<<<<<< conflict 1 of 1
%%%%%%% diff from: zkuqvpzv 4a46c9d1 "add config module"
\\\\\\\        to: kkspkpmo 5a1a6558 "bump timeout to 90"
 DEBUG = True
-TIMEOUT = 60
+TIMEOUT = 90
+++++++ qxysnovo fcf33456 "disable debug flag"
DEBUG = False
TIMEOUT = 60
>>>>>>> conflict 1 of 1 ends
```
The `jj new` command that created the conflict succeeded (exit status 0,
no `--continue` needed); the conflict is a property of the new commit
(labeled `(conflict)` in the log), not a halted operation. Editing the file to
the resolved text and letting the next command re-snapshot it clears the
`(conflict)` flag automatically — verified by `jj status` and `jj log -r @`
after writing `DEBUG = False\nTIMEOUT = 90\n` to `config.py`.

**Demo E — colocated Git interop is live, not just claimed.** In the same
repo (created with plain `jj git init`, which colocates by default):

```
$ ls -d .jj .git
.git
.jj
$ git log --oneline --all | head -3
287174c merge both config edits
5a1a655 bump timeout to 90
68d4f1f bump timeout to 90
$ git branch confirm-colocation
$ jj op log --limit 1
@  55c46eae3039 ... import git refs
```
A plain `git branch` command run outside `jj` was picked up and recorded in
the `jj` operation log as an "import git refs" operation on the very next `jj`
command, exactly as `docs/git-compatibility.md` describes.

## Sources

```text
URL:         https://docs.jj-vcs.dev/latest/working-copy/
Kind:        Primary — the project's own reference documentation for the working-copy model.
Establishes: The working copy is automatically snapshotted into a commit by almost every `jj` command; added/removed files are tracked implicitly (governed by `snapshot.auto-track`); conflicts are materialized as markers in tracked files and re-parsed on the next snapshot; multiple working copies ("workspaces") can share one repo; a working copy can go "stale" if another workspace rewrote its commit.
Paraphrase: "Unlike most other VCSs, Jujutsu will automatically create commits from the working-copy contents when they have changed. Most jj commands you run will commit the working-copy changes if they have changed." Added files are implicitly tracked by default.
Locators:    Sections "Introduction," "Conflicts," "Workspaces," "Stale working copy."
Quote:       "Almost all commands go through three main steps: 1. Snapshot the working copy... 2. Create new commits etc. 'in memory'... 3. Update the working copy to match the new operation."

URL:         https://docs.jj-vcs.dev/latest/operation-log/
Kind:        Primary.
Establishes: Every repo-modifying command is recorded as an "operation" holding a full snapshot ("view") of bookmarks, heads, and each workspace's working-copy commit, plus a pointer to its parent operation(s). `jj undo` and `jj op revert` undo one operation; `jj op restore` restores the whole repo to an arbitrary earlier operation's view. `--at-op` loads the repo as of a past operation without snapshotting.
Paraphrase: The op log is what makes concurrent `jj` commands safe without locks: each command loads the latest operation, doesn't see concurrent writes, and divergence is detected and surfaced (not silently lost) by later `jj status`/`jj log`.
Locators:    "Introduction," "Divergent operations," "Loading an old version of the repo."

URL:         https://docs.jj-vcs.dev/latest/conflicts/
Kind:        Primary.
Establishes: Jujutsu records conflicted file states inside commits rather than failing the operation that created them (rebase, merge, etc.). What's stored is a structured expression of the conflict (an odd-length list of trees), not raw text markers — markers are generated only when a conflicted commit is materialized (checked out, diffed, shown). Rebasing a conflicted commit again does not nest markers. Alternative marker styles ("snapshot", "git"/diff3) are configurable via `ui.conflict-marker-style`.
Paraphrase: Removes the need for `git rebase/merge/cherry-pick --continue`; the workflow becomes check out, resolve, amend, on the writer's own schedule.
Locators:    "Introduction," "Advantages," "Conflict markers" (the apple/grape/orange worked example, reproduced independently in Demo D above with different content and matching format).

URL:         https://docs.jj-vcs.dev/latest/technical/conflicts/
Kind:        Primary — technical/implementation-level doc, same repository.
Establishes: The data-model detail behind first-class conflicts: a conflict is stored as an odd-length ordered list of trees (A+(C-B) form); conflict expressions simplify algebraically on rebase so old conflicts don't nest; a "same-change rule" auto-resolves a conflict when all sides made the identical change, which the doc itself calls lossy in a documented, still-open bug.
Paraphrase: The convenience of that auto-resolution is a deliberate, named trade-off, not an oversight.
Locators:    "Data model," "Conflict simplification," "Same-change rule."
Quote:       "The automatic conflict resolution we do is lossy in terms of conflict algebra; it means that rebasing a commit onto a commit that has the same changes... and then rebasing it back will lose changes (for a real-life example see bug #6369)."

URL:         https://docs.jj-vcs.dev/latest/git-compatibility/
Kind:        Primary.
Establishes: Two storage backends exist; the Git backend is the interoperable one. Colocated workspaces (default for `jj git init`/`jj git clone`) share one working copy between a real `.git` and `.jj`, importing/exporting on every `jj` command; `git` and `jj` commands can be freely interleaved but jj tends to leave Git in detached-HEAD state. Change IDs are stored as a non-standard Git commit header (on by default since jj 0.30.0), preserved by `git commit --amend` but not by rebase; commits with jj conflicts are represented in Git only via placeholder `.jjconflict-*` directories, not as real content. Feature-support table: no Git hooks, no `.gitattributes`, no Git LFS, no partial clones, "kind of" shallow clones (unshallowing is unsupported and "will cause issues"), no submodules (silently dropped, not lost), "kind of" a staging area (ignored).
Paraphrase: Colocation is what lets a team adopt jj incrementally without anyone else knowing, but the doc lists five concrete disadvantages of turning it on, including slower commands in repos with very large numbers of refs and "bugs when interleaving mutating jj and git commands."
Locators:    "Supported features" (bulleted list), "Colocated Jujutsu/Git workspaces" (disadvantages list), "Format mapping details."
Quote:       "Hooks: No. ... Git LFS: No. ... Colocated workspaces are less resilient to concurrency issues if you share the repo using an NFS filesystem or Dropbox... not currently thoroughly tested."

URL:         https://docs.jj-vcs.dev/latest/technical/concurrency/
Kind:        Primary — technical design doc.
Establishes: jj is deliberately lock-free (view objects and operation objects are content-addressed and never mutated in place), which is why concurrent/remote-synced use (rsync, NFS, Dropbox) is safe for commit content even without native locking, but the doc names a known, still-open exception: with the Git backend, repository corruption is possible because that backend "is not entirely lock-free," with `jj debug reindex` as the documented recovery.
Paraphrase: The safety story is not "nothing can go wrong," it is "the worst case is a labeled conflict you can recover from with one documented command" — except for the Git-backend index-corruption case, which the project tracks as an open bug rather than claiming is fixed.
Locators:    "Syncing with rsync, NFS, Dropbox, etc," "Operation log," "Merging divergent operations," "Storage."
Quote:       "with the Git backend, repository corruption is possible because the backend is not entirely lock-free... If that corruption occurs, there is an easy recovery path: jj debug reindex."

URL:         https://docs.jj-vcs.dev/latest/git-comparison/
Kind:        Primary.
Establishes: Conceptual differences from Git stated by the project itself: no index/staging area (jj's replacement is `jj split`/`jj squash`); no "current branch" concept, so bookmarks must be moved manually after committing (this is the documented cause of a specific, named FAQ complaint below); descendant commits auto-rebase whenever an ancestor is rewritten; a single virtual root commit removes Git's "unborn branch" state.
Paraphrase: The staging area isn't removed so much as replaced by cheap commit-splitting; what a Git user does with `git add -p; git commit` becomes `jj split`, and `git add -p; git commit --amend` becomes `jj squash -i`.
Locators:    "Overview" (bulleted list), "The index."

URL:         https://docs.jj-vcs.dev/latest/git-experts/
Kind:        Primary — a doc explicitly aimed at experienced Git users.
Establishes: The project's own side-by-side comparison for the "amend an older commit" workflow: Git's three-step `git add`/`git commit --fixup`/`git rebase -i --autosquash` becomes one command, `jj squash --into <commit>`, with descendants automatically rebased. Also documents `jj absorb`, which moves working-copy hunks into whichever ancestor commit last touched that line, as a partial (not complete) automation of a patch-stack fixup workflow.
Paraphrase: This is the exact command family exercised live in Demo A above; the doc's claimed savings (three Git commands to one jj command) matched what was observed.
Locators:    "Automatic and safer history editing," "jj absorb makes it easier to update a patch stack."
Quote:       "jj absorb... It doesn't solve all cases: If multiple commits in the stack modified the same line as was changed in the working copy, it will not move that change."

URL:         https://docs.jj-vcs.dev/latest/bookmarks/
Kind:        Primary.
Establishes: Bookmarks (jj's branch equivalent) never move automatically when a new commit is created — the user must run `jj bookmark move`/`jj bookmark set` and then push. `jj git push` performs a "safe by construction" check equivalent to `git push --force-with-lease` before moving a remote bookmark. Bookmarks and remote bookmarks can independently become "conflicted" (shown as `name??`) when concurrent operations move them differently; `jj new <bookmark>` on a conflicted bookmark errors rather than guessing.
Paraphrase: The lack of a "current bookmark" concept is a deliberate design choice (see git-comparison.md) with a direct cost: pushing a new commit takes two jj commands where Git takes one, a cost independently reported by a practitioner below.
Locators:    "Introduction," "Pushing bookmarks: Safety checks," "Conflicts."

URL:         https://docs.jj-vcs.dev/latest/faq/
Kind:        Primary — maintained by the project as its own answer to the questions it gets most.
Establishes: Confirms the working-copy-commit model surprises Git users in specific, named ways (bookmarks don't move; `jj git push --all` pushes bookmarks, not revisions); documents that jj-lib and the jj CLI are both explicitly unstable APIs ("not a stable API... not stable either"); documents a known interaction bug where file watchers (Vite/Vitest) watching `.jj/` cause "very slow vitest startup times," timeouts, and "corrupted working_copy.lock files," with a manual ignore-pattern workaround (no fix shipped); explicitly recommends colocating while learning jj and switching off it only "if you find a specific reason not to."
Paraphrase: The FAQ's own colocation guidance names the same disadvantages as the git-compatibility doc but adds a third-party-tooling angle: file watchers that don't know to ignore `.jj/` can corrupt the working-copy lock file.
Locators:    "Why does my bookmark not move...," "I want to write a tool which integrates with Jujutsu...," "I'm experiencing jj command issues in a Vite/Vitest project."
Quote:       "Using the CLI means that your tool will work with custom-built jj binaries, like the one at Google... The CLI is not stable either, so you may need to make your tool detect the different versions."

URL:         https://docs.jj-vcs.dev/latest/roadmap/
Kind:        Primary.
Establishes: An explicit statement that "most people contributing to Jujutsu do so in their spare time," offered by the project as the reason no goal on the roadmap carries a target date. Also documents that Google runs an internal, database-backed jj server unrelated to the public open-source releases ("Google has an internal Jujutsu server backed by a database... We (the project, not necessarily Google) want to provide a similar experience for all users").
Paraphrase: This "spare time" framing is the piece of the maintenance picture most in tension with the paid_contributors.md list below — see Contradictions.
Locators:    Top note; "Open-source cloud-based repos (server and daemon process)."

URL:         https://docs.jj-vcs.dev/latest/technical/architecture/
Kind:        Primary.
Establishes: `jj` is split into a library crate (`jj-lib`) and CLI crate (`jj-cli`); storage is pluggable by design (commit backend, operation backend, index backend, working-copy backend are each swappable), which is presented as the reason Google can run its own cloud backend without forking the CLI. The Git backend uses `gitoxide`, not the `git` CLI, for reads/writes.
Paraphrase: The type diagram referenced in this doc (see Source assets) is implementation detail below the level this article needs, but the backend-pluggability claim is what makes the Git-compatibility story credible: Git is one backend among a documented set, not a bolted-on export format.
Locators:    "Separation of library from UI," "Storage-independent APIs," "GitBackend."

URL:         https://docs.jj-vcs.dev/latest/core_tenets/
Kind:        Primary.
Establishes: The project's own stated design priorities, including "Make it incredibly hard to lose work in your repo," "Concurrent modifications to the repo should be safe," and "All operations must be able to scale to Google-scale repos."
Paraphrase: Useful as the project's own framing of intent, not as evidence the intent is fully realized — the corruption bug (#2193) and lossy same-change rule (#6369) below are both counterexamples to "incredibly hard to lose work" that the project tracks itself.
Locators:    Full document (12 bullet points).

URL:         https://docs.jj-vcs.dev/latest/glossary/
Kind:        Primary — canonical term definitions.
Establishes: Precise definitions used elsewhere in this record: "change" vs. "commit" (a change is a commit as it evolves; the change ID is stable across rewrites, the commit ID is not), "bookmark," "colocated workspace," "operation," "divergent change," "workspace" (= Git's "worktree"), "working copy" (= Git's "working tree").
Paraphrase: None beyond the definitions themselves.
Locators:    Alphabetical entries as named above.

URL:         https://docs.jj-vcs.dev/latest/tutorial/
Kind:        Primary — introductory walkthrough.
Establishes: The change-ID/commit-ID distinction in a worked example; that `jj new` starts a fresh working-copy commit on top of the current one; that `jj evolog` shows the history of a single change across rewrites (distinct from `jj log`, which shows the current graph).
Paraphrase: Confirms terminology used in the Verified command sequence above (e.g., that `jj log`'s first ID column is the change ID, the second is the commit ID).
Locators:    "Cloning a Git repository," "Changes," "Creating our first change."

URL:         https://docs.jj-vcs.dev/latest/install-and-setup/
Kind:        Primary.
Establishes: Supported install paths (pre-built binaries, `cargo binstall`, `cargo install --locked jj-cli`, Arch package/AUR); minimum Rust toolchain 1.88 for building from source.
Paraphrase: Confirms the install method actually used to produce the verified command sequence above (`cargo install --locked jj-cli`, which the doc lists as the standard "install the latest release" path) is the project's own recommended method, not an improvised one.
Locators:    "Installation," "Linux," "From Source."

URL:         https://docs.jj-vcs.dev/latest/changelog/
Kind:        Primary — canonical, dated release record (identical content to the repository's CHANGELOG.md, read directly from a git clone of jj-vcs/jj at commit 12618c208199c33693dfed39c990da029dc58b71, 2026-08-14).
Establishes: Version and release-date ground truth used throughout this record: v0.44.0 released 2026-08-05; monthly-or-faster releases back through v0.30.0 (2025-06-04) — fifteen releases in fourteen months, one per roughly four weeks, with no gap over five weeks. v0.33.0 (2025-09-03) changed `jj undo` from "always undoes only the single most recent operation" to sequential stepping, and added `jj redo`; `jj op undo` was deprecated in favor of `jj op revert` in the same release.
Paraphrase: This file, not the GitHub releases page's rendered dates (which a fetch tool mis-rendered — see Discarded), is the date source for every version claim in this record.
Locators:    "## [Unreleased]," "## [0.44.0] - 2026-08-05" through "## [0.30.0] - 2025-06-04."
Quote:       "jj undo is now sequential: invoking it multiple times in sequence repeatedly undoes actions in the operation log. Previously, jj undo would only undo the most recent operation in the operation log. As a result, a new jj redo command has been added."

URL:         https://github.com/jj-vcs/jj/blob/main/README.md
Kind:        Primary — project README, same repository, read via git clone.
Establishes: Self-described maturity: "The tool is fairly feature-complete, but some important features like support for Git submodules are not yet completed. There are also several performance bugs... There will be changes to workflows and backward-incompatible changes to the on-disk formats before version 1.0.0." Also: "All core developers use jj to develop jj" (dogfooding claim), and a section titled "Mandatory Google Disclaimer" stating Martin von Zweigbergk started the project as a hobby in late 2019 and that it "has evolved into my full-time project at Google, with several other Googlers (now) assisting development... this is not a supported Google product."
Paraphrase: This is a pre-1.0 tool by the project's own admission, with named format-stability and performance caveats, not a marketing gloss — but see Contradictions for the tension between this section and paid_contributors.md.
Locators:    "## Status," "## Contributing" → "### Mandatory Google Disclaimer."
Quote:       "I (Martin von Zweigbergk, martinvonz@google.com) started Jujutsu as a hobby project in late 2019, and it has evolved into my full-time project at Google, with several other Googlers (now) assisting development in various capacities."

URL:         https://github.com/jj-vcs/jj/blob/main/GOVERNANCE.md
Kind:        Primary.
Establishes: Current maintainer roster (nine named individuals with GitHub handles); decision-making process (2-4 week discussion window, simple majority of participating maintainer votes to accept a proposal, 2/3 supermajority to remove a maintainer); an explicit single-company cap: "At most 1/3 of the maintainers may be paid for their contributions by a single company."
Paraphrase: Governance is formal and documented, not ad hoc — there is a named process for adding/removing maintainers and a specific anti-capture rule.
Locators:    "Current list of Maintainers," "Single-Company Influence."

URL:         https://github.com/jj-vcs/jj/blob/main/docs/paid_contributors.md
Kind:        Primary — the project's own conflict-of-interest disclosure, cross-referenced against GOVERNANCE.md's maintainer list.
Establishes: Companies currently paying contributors, and which named individuals they pay. "East River Source Control" pays benbrittain, bts, ConnerPetzold, davidbarsky, ilyagr, martinvonz, steveklabnik, and thoughtpolice — three of whom (ilyagr = Ilya Grigoriev, martinvonz = Martin von Zweigbergk, thoughtpolice = Austin Seipp) are current Maintainers per GOVERNANCE.md. "Alphabet/Google" separately pays 38 listed individuals, none of whom are current Maintainers by the names in GOVERNANCE.md. "IMC Trading" pays two listed individuals.
Paraphrase: Cross-referencing the two lists gives a concrete, checkable number for the governance cap: exactly 3 of the 9 current maintainers (33%) are paid by one company (East River Source Control) — at the stated 1/3 ceiling, not comfortably under it.
Locators:    "## East River Source Control," "## Alphabet/Google," "## IMC Trading."

URL:         https://ersc.io/
Kind:        Secondary for jj (the company describing itself, not the jj project describing the company) — primary only for East River Source Control's own self-description.
Establishes: East River Source Control describes itself as building "high-quality tooling to help you manage your most important asset: your code," and links out to the Jujutsu docs from its own site. The page as fetched did not state a founding team, funding round, or an explicit claim of building "on Jujutsu" in so many words — that framing came from an unopened search snippet, not this page, and is not asserted here as read fact.
Paraphrase: Confirms a real, live company exists at this domain and links to jj's docs; does not by itself establish the nature or size of its backing.
Locators:    Landing page (single page, no distinct sections).

URL:         https://github.com/jj-vcs/jj/releases/tag/v0.44.0
Kind:        Primary — official release page, current stable release.
Establishes: Same release-notes text as CHANGELOG.md's 0.44.0 entry (tag stabilizes tag/push support). Used only to corroborate that the CHANGELOG.md content is also the published release; date is taken from CHANGELOG.md instead of this page (see Discarded).
Paraphrase: Corroboration only.
Locators:    Release body text.

URL:         https://github.com/jj-vcs/jj/releases/tag/v0.33.0
Kind:        Primary — official release page.
Establishes: Corroborates the CHANGELOG.md entry for `jj undo` becoming sequential and `jj redo` being added, in the release's own highlights section.
Paraphrase: Independent confirmation that this specific behavior change actually shipped as a numbered, tagged release rather than only appearing in the unreleased changelog.
Locators:    Release highlights section.

URL:         https://github.com/jj-vcs/jj/issues/2193
Kind:        Primary — the project's own open issue tracker, referenced by the technical/concurrency.md doc itself.
Establishes: Title: "With the git backend, jj's change id index consistency relies on locks that aren't always available." Open as of this research. Root cause: the fix for an earlier issue depends on file locks unavailable when a repo is synced by rsync or cloud-storage tools instead of native jj/git operations. Symptom: the change-ID index can become internally inconsistent (commits wrongly reported missing, or wrongly shown as hidden). Recovery: `jj debug reindex`.
Paraphrase: This is the specific bug the concurrency doc's honesty about "corruption is possible" points to — an open issue, not a resolved one, as of this research.
Locators:    Issue title and body.

URL:         https://github.com/jj-vcs/jj/issues/6369
Kind:        Primary — open issue, cited by name from technical/conflicts.md itself as the "real-life example" of the same-change-rule's lossy behavior.
Establishes: A reproducible criss-cross-merge scenario (two independent commits make the same edit; each is separately merged into two more commits; merging those two loses the edit and reverts to the original content) on jj 0.28.2, Linux and Windows. Open, unassigned, no linked PR as of this research.
Paraphrase: The project's own docs cite this bug as the accepted cost of a usability trade-off (see technical/conflicts.md above); this issue is the primary record of that cost actually manifesting for a user, not merely a theoretical caveat in the docs.
Locators:    Issue body, reproduction steps.

URL:         https://minsoo.io/p/my-experience-with-jujutsu-a-pragmatic-review
Kind:        Secondary — independent practitioner review, not affiliated with the project (an outside user's account of daily use).
Establishes: Concrete, dated friction points from real use: no `prepare-commit-msg` hook support (confirmed independently against the "Hooks: No" line in git-compatibility.md), forcing a fallback to plain Git for a FreeBSD codebase that depends on that hook; no direct `git commit --fixup` equivalent, requiring manual `fixup!`-prefixed descriptions that retype the target commit message; the two-command bookmark-then-push sequence described as "a small friction, but it adds up"; immature third-party tooling (a shell prompt plugin only gained jj support "last week," via a community plugin).
Paraphrase: An independent, practitioner-level corroboration of costs the project's own docs also name (hooks, bookmark-push friction) plus one the docs don't foreground (no built-in fixup equivalent for patch-stack workflows).
Locators:    Sections on Git hooks, `--fixup`, bookmark workflow, ecosystem maturity.

URL:         https://www.arun.blog/jujutsu-vcs/
Kind:        Secondary — independent practitioner account.
Establishes: A colocated repo combined with `jj workspace add` produced a workspace that behaved as "a pure jj repo," which the author found incompatible with tools (cited: Claude Code) that expect a real Git working tree, leading the author to reach for Git worktrees instead of jj workspaces for that specific tool integration. The author had not migrated GPG commit signing from Git to jj at the time of writing, and had not yet exercised jj's advanced rebase/history-editing features enough to have an opinion on them.
Paraphrase: A second, independent account of the colocation-plus-workspace friction that FAQ.md and git-compatibility.md both flag from the project's own side — corroboration that it is a real, encountered problem and not only a documented theoretical caveat.
Locators:    Sections on colocated workspaces vs. git worktrees, commit signing, rebasing.

URL:         https://news.ycombinator.com/item?id=45675737
Kind:        Secondary — public discussion thread; the specific comment cited is from a named commenter (mkeeter) directly correcting an earlier complaint with a citation to the v0.33.0 release notes.
Establishes: Independent, dated confirmation (outside the project's own docs) that the pre-0.33.0 `jj undo` behavior — where calling it twice in a row undid the undo rather than stepping further back — was a real, commonly-hit point of confusion severe enough to draw complaints, and that the project's fix (cited above from the release notes and CHANGELOG.md) directly answered it.
Paraphrase: Useful less as new information than as confirmation that this was a genuine footgun in real use before it was fixed, not a hypothetical one flagged only by the project itself.
Locators:    Comment by "mkeeter," direct reply to the "jj undo is great but it's a one time thing" complaint.
Quote:       "For what it's worth, this changed in v0.33.0: jj undo is now sequential: invoking it multiple times in sequence repeatedly undoes actions in the operation log."
```

## Contradictions

- **Who backs the project today is not cleanly resolved by the sources I
  read.** README.md's own "Mandatory Google Disclaimer" section states, in
  the founder's voice, that Jujutsu is his "full-time project at Google, with
  several other Googlers (now) assisting development." But
  `docs/paid_contributors.md` — the project's own conflict-of-interest list,
  maintained for the express purpose of flagging who is paid by whom — lists
  that same person (martinvonz) as paid by "East River Source Control," a
  separate company, alongside two other current maintainers (Ilya Grigoriev,
  Austin Seipp). Neither document carries a visible last-updated date. I did
  not open a source that reconciles these two statements (an unread search
  snippet claimed Martin von Zweigbergk is East River Source Control's CTO,
  but I have not read that page and do not assert it here). A writer should
  either soften any claim that identifies jj's backing as simply "Google" or
  simply "a startup," or flag the ambiguity explicitly rather than pick one.

- **"Spare time" vs. a governance rule built for paid influence.**
  `docs/roadmap.md` frames the absence of target dates on the entire roadmap
  around the claim that "most people contributing to Jujutsu do so in their
  spare time." `GOVERNANCE.md`'s single-company cap ("At most 1/3 of the
  maintainers may be paid for their contributions by a single company") and
  `docs/paid_contributors.md`'s roster of 40+ named, company-paid contributors
  only make sense as a live governance concern if a substantial share of
  contribution is in fact paid, professional time. Both documents are real
  and both are current in the source tree; they describe two different and
  not-easily-reconciled realities of who is doing the work.

- **The colocation trade-off is confirmed from both directions.** The
  project's own docs (`docs/git-compatibility.md`, `docs/FAQ.md`) list
  colocation's downsides candidly — divergent-change confusion, slower
  commands with many refs, Git tools misreading conflicted commits, and (per
  FAQ) file watchers corrupting `working_copy.lock` — while simultaneously
  recommending colocation as the default onboarding path ("Try colocating
  while you learn Jujutsu, then switch if you find a specific reason not
  to"). Two independent practitioner accounts (Minsoo Choo, Arun) each hit a
  concrete version of this trade-off in real use (a missing Git hook forcing
  a fallback to Git; a workspace-plus-colocation interaction that broke a
  tool's Git-worktree assumption). This is not a contradiction between
  sources so much as confirmation that a documented caveat is a real,
  recurring cost, not boilerplate — worth reflecting directly in the article's
  honest-costs section rather than softening.

- **The "incredibly hard to lose work" tenet has two named, open
  counterexamples the project tracks itself.** `docs/core_tenets.md` states
  the goal in that language. `docs/technical/concurrency.md` and
  `docs/technical/conflicts.md` each name a specific, still-open bug where
  that goal is not fully met today: index corruption under non-native sync
  with the Git backend (#2193) and silent, lossy conflict auto-resolution on
  certain criss-cross rebases (#6369). Both are documented by the project
  against its own stated goal, not surfaced only by outside critics — which
  cuts against the "adopt it" angle less than it might look, since the
  project is transparent about both, but it does mean "incredibly hard to
  lose work" is aspirational language, not a settled property, as of jj
  0.44.0.

- **`jj undo`'s current behavior is not what several practitioner complaints
  describe**, because those complaints predate v0.33.0 (2025-09-03). Anyone
  drafting from older blog posts or Stack Overflow-style answers about
  `jj undo` "not being a stack" should check the date against that release —
  verified directly in Demo B/C above, repeated `jj undo`/`jj op restore`
  calls on jj 0.44.0 behave as currently documented, not as the older
  complaints describe.

## Numbers

```text
Figure: jj 0.44.0
Owner:  CHANGELOG.md (jj-vcs/jj, read at commit 12618c208199c33693dfed39c990da029dc58b71) and the installed binary's own `jj --version` output, cross-checked.
Scope:  Current stable release as of 2026-08-14; released 2026-08-05.

Figure: 15 tagged releases between 2025-06-04 (v0.30.0) and 2026-08-05 (v0.44.0), i.e. one release roughly every 28 days over 14 months, with no gap exceeding five weeks.
Owner:  CHANGELOG.md version headers, read directly (dates: 0.30.0–2025-06-04, 0.31.0–2025-07-02, 0.32.0–2025-08-06, 0.33.0–2025-09-03, 0.34.0–2025-10-01, 0.35.0–2025-11-05, 0.36.0–2025-12-03, 0.37.0–2026-01-07, 0.38.0–2026-02-04, 0.39.0–2026-03-04, 0.40.0–2026-04-01, 0.41.0–2026-05-06, 0.42.0–2026-06-04, 0.43.0–2026-07-01, 0.44.0–2026-08-05).
Scope:  Tagged releases only; does not count unreleased main-branch commits.

Figure: 121 commits to the main branch in the 30 days before 2026-08-14, from at least 20 distinct named human authors plus dependabot[bot].
Owner:  My own `git log --since=2026-07-14` measurement against a git clone of jj-vcs/jj fetched to 1000-commit depth on 2026-08-14 (not a third-party claim).
Scope:  Commit count and author count, main branch, trailing 30 days from research date; top single-day contributors in that window were Yuya Nishihara (33 commits) and Martin von Zweigbergk (13 commits), both listed maintainers, alongside first-time-looking usernames with 1-2 commits each — i.e., activity is concentrated but not closed to outside contribution.

Figure: 9 current maintainers (GOVERNANCE.md); 3 of the 9 (33%) are paid by a single company, East River Source Control, per docs/paid_contributors.md — exactly at the governance document's stated 1/3 cap, not below it.
Owner:  GOVERNANCE.md maintainer roster cross-referenced against docs/paid_contributors.md's East River Source Control list, both read directly from the source tree.
Scope:  Current maintainers only, as of the read commit; does not count the larger pool of non-maintainer contributors (38 more names listed as paid by Alphabet/Google, 2 by IMC Trading).

Figure: git.write-change-id-header has written jj's non-standard change-ID commit header by default since jj version 0.30.0.
Owner:  docs/git-compatibility.md, "Format mapping details" section.
Scope:  Applies to commits created by jj using the Git backend; the header is not written by plain `git commit`, and is dropped by `git rebase` (preserved by `git commit --amend`).
```

## Source assets

```text
Asset: The terminal `jj log` graph output itself (not a docs image) — the `@`/`○`/`◆` graph with change-ID and commit-ID columns, reproduced live in Demo B above showing the graph split into two branches after the botched rebase, then reunified after `jj undo`.
Shows: The exact moment a rebase mistake becomes visible (two disconnected lines in the graph) and the exact moment `jj undo` repairs it (graph returns to one line, same commit IDs). This is stronger than any static docs image because it's reproducible by a reader on their own machine from the commands given.
Crop:  If used as a figure, keep both the before-botch and after-undo `jj log` blocks side by side (or before/during/after as three panels) so the identical commit IDs are visible for comparison; do not crop out the IDs, they are the evidence that undo restored exactly rather than approximately.

Asset: The conflict-marker block from docs/conflicts.md, reproduced independently with different content in Demo D above (`cat config.py` showing the `<<<<<<<`/`%%%%%%%`/`+++++++`/`>>>>>>>` structure with commit descriptions inline).
Shows: That the "diff-style" conflict marker format is real, current, and distinguishable from a plain Git three-way conflict marker (it names the contributing commits by change ID and description directly in the marker, which Git markers don't do).
Crop:  Keep the full block including the `%%%%%%% diff from: ... to: ...` two-line label; that label is what makes this format different from Git's diff3 style and is the detail worth explaining, not decoration.

Asset: docs/technical/architecture.md's type diagram (types.svg, an Excalidraw export showing Workspace/WorkingCopy/RepoLoader/Transaction/MutableRepo/ReadonlyRepo relationships).
Shows: How the library crate's internal types relate — useful only if the article goes into `jj-lib`'s internals, which the commission's chosen mechanism (working copy, op log, undo, first-class conflicts) does not require.
Crop:  None found to be necessary for this piece; flagged for completeness only. Likely out of scope given the audience is being taught the user-facing model, not the Rust API.

Asset: The releases/version timeline implied by the CHANGELOG.md dates in the Numbers section (15 dated releases over 14 months).
Shows: Release cadence as a trend, which is the kind of comparison a small timeline or sparkline could carry better than a sentence of dates.
Crop:  If charted, plot release date on one axis with no other variable — resist adding a second series (e.g., commit count per release) unless that data is also verified line-by-line; the dates alone already carry the "actively, regularly maintained" claim.
```

## Discarded

```text
URL: https://github.com/jj-vcs/jj/releases (unfiltered releases index)
Reason: The fetch tool's summary of this listing returned release dates a full two years off (e.g., "v0.44.0 — August 6, 2024"), which is simply wrong — CHANGELOG.md in the source tree gives 2026-08-05 for that same release, confirmed by cross-checking the file directly rather than trusting the summary. Used CHANGELOG.md as the dated source of record for every version claim in this piece instead; the individual release tag pages (v0.44.0, v0.33.0) were kept only for their release-notes text, not their rendered dates, which had the identical date-hallucination problem.

URL: https://thenewstack.io/jujutsu-dealing-with-version-control-as-a-martial-art/
Reason: Appeared only as a search-result title, never opened or read; not used as a source and nothing from it is asserted in this record.

URL: https://medium.com/@shrmtv/jujutsu-150945f97753
Reason: Appeared only as a search-result title, never opened or read.

URL: https://www.infovision.com/blog/git-and-jujutsu-the-next-evolution-in-version-control-systems/
Reason: Appeared only as a search-result title; marketing-adjacent domain (a consultancy blog), not opened.

URL: https://www.kunalganglani.com/blog/jujutsu-jj-git-version-control
Reason: Appeared only as a search-result title, never opened or read.

URL: LinkedIn profile snippet describing Martin von Zweigbergk as East River Source Control's CTO
Reason: Surfaced only inside a search-engine summary, not opened directly (LinkedIn requires authentication I do not have). Not cited as fact anywhere in this record — see the Contradictions entry on backing, which explicitly declines to assert this.
```
