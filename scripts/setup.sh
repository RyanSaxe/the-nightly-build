#!/usr/bin/env sh
# The Nightly Build scripts/setup.sh
# Idempotent bootstrap: scaffolds the press, creates the library branch, enables
# Pages and Actions, validates configuration. Safe to re-run; callable by the
# user-assistant skill.
# POSIX sh so it runs on any shell (dash, bash, zsh, ...), not just zsh.
set -eu

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH='' cd -- "$SCRIPT_DIR/.." && pwd)
cd "$ROOT"

say() { printf '→ %s\n' "$1"; }
ok() { printf '✓ %s\n' "$1"; }
warn() { printf '⚠ %s\n' "$1"; }
die() {
	printf '✗ %s\n' "$1" >&2
	exit 1
}
seed_root=
seed_worktree=
cleanup_seed() {
	if [ -n "$seed_worktree" ]; then
		git worktree remove --force "$seed_worktree" >/dev/null 2>&1 || true
		seed_worktree=
	fi
	if [ -n "$seed_root" ] && [ -d "$seed_root" ]; then
		rmdir "$seed_root" 2>/dev/null || true
	fi
}
trap cleanup_seed EXIT HUP INT TERM

# 1. Preconditions -----------------------------------------------------------
command -v gh >/dev/null 2>&1 || die "gh (GitHub CLI) is required: https://cli.github.com"
command -v git >/dev/null 2>&1 || die "git is required"
command -v uv >/dev/null 2>&1 || die "uv is required: https://docs.astral.sh/uv/"
gh auth status >/dev/null 2>&1 || die "gh is not authenticated. Run: gh auth login"
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || die "run this from your fork's checkout"

origin_url=$(git remote get-url origin 2>/dev/null) ||
	die "no 'origin' remote. Is this your fork's checkout?"
repo=$(gh repo view "$origin_url" --json nameWithOwner -q .nameWithOwner 2>/dev/null) ||
	die "no GitHub repo detected at origin ($origin_url)"
ok "repo: $repo"

# 1b. This repo is a press; the canonical repo is engine-only ------------------
UPSTREAM_REPO="${UPSTREAM_REPO:-the-nightly-build/the-nightly-build}"
if [ "$repo" = "$UPSTREAM_REPO" ]; then
	die "this is the engine repo; it runs no press. Fork it, then run setup there."
fi

# 1c. Scaffold press/ (your side of the repo) ---------------------------------
if [ ! -d press ]; then
	say "scaffolding press/ (your side of the repo)"
	mkdir -p press/series press/themes press/templates
	cat >press/site.yaml <<'YAML'
title: "The Nightly Build"
theme: engine/assets/themes/newspaper.css   # or press/themes/<yours>.css
appearance: auto   # auto | light | dark
front: compact     # compact | comfortable (deks on front-page story cells)
YAML
	cat >press/editorial.md <<'MD'
# Voice

Your editorial voice, composed into every article's instructions after the
house style (spec/editorial.md). Tone, register, language, assumed
background: make the paper yours. Ask your agent to interview you and fill
this in, or write it by hand.
MD
	cat >press/production.yaml <<'YAML'
# Portable role guidance. See docs/reference/production.md.
profile: balanced
required: false
YAML
	mkdir -p press/series/dispatches
	cat >press/series/dispatches/series.yaml <<'YAML'
# Articles you asked for, on any subject, whenever you ask. nb duty never
# schedules this series; every article in it started as a request.
name: Dispatches
mode: open
cadence: manual
template: article
prompt: prompt.md
strict: false
min_sources: 5
bands:
  words: [800, 2500]
YAML
	cat >press/series/dispatches/prompt.md <<'MD'
Someone asked for this article. The request is the commission: find the
question it raises and establish the answer rather than mention it. Whatever
the request supplied, a link, a document, a claim, is starting material, not
the evidence: read it, then read past it until the piece stands on sources the
reader can check. Cover what was asked and nothing that was not.
MD
	cat >press/README.md <<'MD'
# press/ is your side of the repo

Everything here is yours; everything outside is the engine. Dispatches, under
series/, takes the articles you ask for. Add a series when a kind of request
recurs, your voice in editorial.md, role cost in production.yaml, and your look
via site.yaml and themes/. Working examples live under examples/.
MD
	ok "press/ scaffolded. Configure it, or ask your agent to set you up"
else
	ok "press/ exists"
fi

# 2. Configuration validates before anything else ----------------------------
say "validating press/ configuration and the template packages"
"$ROOT/nb" validate || die "fix the configuration above, then re-run"

# 3. The library branch (orphan, empty press) --------------------------------
library_created=false
if git ls-remote --exit-code --heads origin library >/dev/null 2>&1; then
	ok "library branch already exists on origin"
else
	say "creating orphan library branch"
	# Plumbing instead of 'git checkout --orphan' on purpose: an orphan
	# checkout starts from the current working tree, so it would need the
	# tree emptied and risks committing strays. Building the two-object
	# commit directly touches no checkout and is deterministic.
	blob=$(printf '' | git hash-object -w --stdin)
	subtree=$(printf '100644 blob %s\t.gitkeep\n' "$blob" | git mktree)
	tree=$(printf '040000 tree %s\tlibrary\n' "$subtree" | git mktree)
	commit=$(git commit-tree "$tree" -m "library: initialize the empty press")
	git branch --force library "$commit"
	git push -u origin library
	library_created=true
	ok "library branch pushed (contains only library/.gitkeep)"
fi

# 3b. Seed a new library before protecting it --------------------------------
# GitHub only fires pull_request triggers from workflow files present on the
# PR's base branch, and push triggers from files present on the pushed branch.
# Recurring updates take the protected PR path in sync.sh. Only a branch made
# moments ago is seeded directly, before protection exists.
if [ "$library_created" = true ]; then
	say "seeding trigger workflows onto the new library"
	git fetch -q origin main library
	seed_root=$(mktemp -d)
	seed_worktree="$seed_root/worktree"
	git worktree add -q --detach "$seed_worktree" origin/library
	mkdir -p "$seed_worktree/.github/workflows"
	for path in .github/workflows/check.yml .github/workflows/publish.yml; do
		git show "origin/main:$path" >"$seed_worktree/$path" ||
			die "origin/main does not contain $path"
	done
	git -C "$seed_worktree" add .github
	git -C "$seed_worktree" -c user.name="The Nightly Build" \
		-c user.email="nightly-build@users.noreply.github.com" \
		commit -qm "chore: seed library workflows [skip ci]"
	git -C "$seed_worktree" push -q origin HEAD:refs/heads/library
	git worktree remove --force "$seed_worktree"
	seed_worktree=
	rmdir "$seed_root"
	seed_root=
	ok "trigger workflows seeded onto library"
fi

# 4. GitHub Pages (Actions-based deploy; publish.yml uploads site/) ----------
# The deploy runs on the main ref and reads library at build time, so the
# github-pages environment needs no branch policy for library.
if gh api "repos/$repo/pages" >/dev/null 2>&1; then
	gh api -X PUT "repos/$repo/pages" -f build_type=workflow >/dev/null 2>&1 ||
		true
	ok "GitHub Pages already enabled"
else
	if gh api -X POST "repos/$repo/pages" -f build_type=workflow >/dev/null 2>&1; then
		ok "GitHub Pages enabled (workflow deploy)"
	else
		warn "could not enable Pages via API (a private repo on the free plan"
		warn "  has no Pages: make it public, or use Pro). Then enable it at:"
		warn "  https://github.com/$repo/settings/pages, Source: GitHub Actions"
	fi
fi

# 4c. Actions run the publishing gate; forks start with workflows disabled ---
if [ "$(gh api "repos/$repo/actions/permissions" -q .enabled 2>/dev/null)" = "true" ]; then
	ok "GitHub Actions enabled"
elif gh api -X PUT "repos/$repo/actions/permissions" -F enabled=true >/dev/null 2>&1; then
	ok "GitHub Actions enabled (forks start with workflows disabled)"
else
	warn "could not enable GitHub Actions. Without it the 'validate' check never"
	warn "  runs and no article can merge. Enable workflows at:"
	warn "  https://github.com/$repo/actions"
fi

# 5. Auto-merge + library protection -----------------------------------------
if gh api -X PATCH "repos/$repo" -F allow_auto_merge=true >/dev/null 2>&1; then
	ok "repository auto-merge enabled"
else
	warn "could not enable auto-merge. Flip it at https://github.com/$repo/settings"
fi
# enforce_admins:true is deliberate: the scheduled runtime holds your (admin) token,
# so the required 'validate' check must bind admins too, or a prompt-injected
# run could merge past the proof. Auto-merge still works (it merges only after
# 'validate' passes). See docs/concepts/publishing-and-security.md.
if gh api -X PUT "repos/$repo/branches/library/protection" --input - >/dev/null 2>&1 <<'JSON'; then
{
  "required_status_checks": { "strict": false, "contexts": ["validate"] },
  "enforce_admins": true,
  "required_pull_request_reviews": null,
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
JSON
	ok "library branch protected (the editor's check gates every merge, incl. admins)"
else
	warn "could not protect library (needs admin / paid plan on private repos)"
	warn "  recommended: require the 'validate' check (enforce for admins) at"
	warn "  https://github.com/$repo/settings/branches"
fi

# 6. Existing libraries synchronize through the protected PR path ------------
if [ "$library_created" = false ]; then
	sync_rc=0
	"$ROOT/nb" sync || sync_rc=$?
	if [ "$sync_rc" -eq 3 ]; then
		warn "the publishing workflows need a protected update: open and merge"
		warn "  the sync PR described above, then re-run nb setup"
	elif [ "$sync_rc" -ne 0 ]; then
		die "nb sync failed; fix the failure above, then re-run nb setup"
	fi
fi

# 7. Status ------------------------------------------------------------------
echo
ok "The presses are ready."
printf '%s\n' "
Next steps:
  1. Ask for an article: open this checkout in your AI tool and say what you
                 want to read. The Dispatches series takes it; see
                 docs/getting-started/ask-your-ai.md.
  2. Morning paper, when you want one: add series with a cadence and schedule
                 the run; see docs/guides/operate/schedule.md.
  3. Your site:  the Pages URL for $repo.
"
