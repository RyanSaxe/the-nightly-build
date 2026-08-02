"""PR mode: the exact shape and contents of one proposed library change.

The library accepts one new article bundle, one reviewed revision, an
owner-authorized retraction, or an exact workflow sync from the fork's main
branch. New bundles include the complete role record; revisions preserve that
history and add one numbered explanation of the change.
"""

from __future__ import annotations

import datetime as _dt
import os
import pathlib
import subprocess
import tempfile

from nb import meta as nb_meta
from nb.artifacts import validate_artifacts, validate_revision_note
from nb.config import load_series
from nb.proof import check_article
from nb.report import Report
from nb.workflow_sync import classify_workflow_sync

__all__ = (
    "materialize_bundle",
    "pr_changed_files",
    "run_pr_mode",
)

PR_PATH_RE = nb_meta.PR_PATH_RE


def pr_changed_files(repo, *, base, head):
    out = subprocess.run(
        [
            "git",
            "-C",
            repo,
            "diff",
            "--name-status",
            "--no-renames",
            f"{base}...{head}",
        ],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    changes = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            changes.append((parts[0], parts[-1]))
    return changes


def materialize_bundle(repo, head, *, changes, dest, extra_paths=()):
    """Write the PR's files, as `head` has them, under dest.

    The proof reads the bundle from disk (the article, then its bundle assets
    by size and image header), but the checkout at --repo can be on any branch:
    the documented preflight runs it from the library checkout, where the new
    bundle does not exist yet. What the PR would merge is the blob at head, so
    that is what gets checked, whatever happens to be checked out.
    """
    paths = [relpath for status, relpath in changes if status != "D"]
    paths.extend(path for path in extra_paths if path not in paths)
    for relpath in paths:
        blob = subprocess.run(
            ["git", "-C", repo, "show", f"{head}:{relpath}"],
            capture_output=True,
            check=True,
        ).stdout
        target = os.path.join(dest, relpath)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as fh:
            fh.write(blob)


def _tree_paths(repo: str, *, ref: str, prefix: str) -> list[str]:
    result = subprocess.run(
        ["git", "-C", repo, "ls-tree", "-r", "--name-only", ref, "--", prefix],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.splitlines()


def _is_regular_blob(repo: str, *, ref: str, path: str) -> bool:
    result = subprocess.run(
        ["git", "-C", repo, "ls-tree", ref, "--", path],
        capture_output=True,
        text=True,
        check=True,
    )
    mode, _separator, _rest = result.stdout.partition(" ")
    return mode in {"100644", "100755"}


def run_pr_mode(
    *,
    repo: str,
    base: str,
    head: str,
    library: str | None,
    rep: Report,
    main: str | None = None,
    today: str | None = None,
    check_links: bool = True,
    deletions_by_owner: bool = False,
) -> None:
    try:
        changes = pr_changed_files(repo, base=base, head=head)
    except subprocess.CalledProcessError as e:
        rep.block("B-DIFF-SHAPE", f"git diff failed: {e.stderr or e}")
        return
    cfg_repo = main or repo
    workflow_sync = classify_workflow_sync(
        repo,
        cfg_repo,
        head=head,
        changes=changes,
    )
    if workflow_sync.attempted:
        if workflow_sync.valid:
            rep.outcome = "SYNC"
            rep.notes.append("workflow sync: exact copies from the fork's main branch")
        else:
            rep.block(
                "B-WORKFLOW-SYNC",
                workflow_sync.reason or "invalid workflow sync",
            )
        return
    if deletions_by_owner and changes and all(status == "D" for status, _ in changes):
        retracted = nb_meta.article_bundle_path(changes, status="D")
        if retracted is None:
            rep.block(
                "B-DIFF-SHAPE",
                "an owner curation PR deletes one article with its matching "
                f"local assets and agent-artifacts record; found {changes}",
            )
            return
        match = PR_PATH_RE.match(retracted)
        assert match is not None
        series_id, slug = match.groups()
        deleted = {path for _, path in changes}
        remaining = [
            path
            for prefix in (
                f"library/{series_id}/{slug}/",
                f"agent-artifacts/{series_id}/{slug}/",
            )
            for path in _tree_paths(repo, ref=base, prefix=prefix)
            if path not in deleted
        ]
        if remaining:
            rep.block(
                "B-DIFF-SHAPE",
                "a retraction deletes the article, its full asset directory, and "
                f"its full agent-artifacts record; still present: {remaining}",
            )
        else:
            rep.notes.append(
                "owner curation: retracts one published article with its assets "
                "and production record; nothing to proof"
            )
        return
    path = nb_meta.article_bundle_path(changes)
    revision = False
    if path is None:
        path = nb_meta.revision_bundle_path(changes)
        revision = path is not None
    if path is None:
        rep.block(
            "B-DIFF-SHAPE",
            "PR must add one article bundle or revise one article with matching "
            "assets and one new revision note; found "
            f"{[(status, path) for status, path in changes]}",
        )
        return
    for status, changed_path in changes:
        if status != "D" and not _is_regular_blob(repo, ref=head, path=changed_path):
            rep.block(
                "B-DIFF-SHAPE",
                f"every changed path must be a regular file: {changed_path}",
            )
            return
    m = PR_PATH_RE.match(path)
    assert m is not None
    series_id = m.group(1)
    series_cfg, _ = load_series(cfg_repo, series_id)
    rep.strict = bool(series_cfg and series_cfg.get("strict"))
    with tempfile.TemporaryDirectory() as bundle_dir:
        slug = m.group(2)
        asset_prefix = f"library/{series_id}/{slug}/"
        extra_paths = []
        if revision:
            extra_paths = [
                path,
                *_tree_paths(repo, ref=head, prefix=asset_prefix),
            ]
        materialize_bundle(
            repo,
            head,
            changes=changes,
            dest=bundle_dir,
            extra_paths=extra_paths,
        )
        if revision:
            artifact_prefix = f"agent-artifacts/{series_id}/{slug}/"
            added_paths = [
                changed_path for status, changed_path in changes if status == "A"
            ]
            issues = validate_revision_note(
                pathlib.Path(bundle_dir),
                series=series_id,
                slug=slug,
                added_paths=added_paths,
                base_paths=_tree_paths(repo, ref=base, prefix=artifact_prefix),
            )
        else:
            issues = validate_artifacts(
                pathlib.Path(bundle_dir), series=series_id, slug=slug
            )
        for issue in issues:
            rep.block(
                "B-REVISION-NOTE" if revision else "B-AGENT-ARTIFACTS",
                issue,
            )
        check_article(
            os.path.join(bundle_dir, path),
            series_id,
            repo=cfg_repo,
            library_dir=library,
            rep=rep,
            today=today and _dt.date.fromisoformat(today),
            check_links=check_links,
            revision=revision,
        )
