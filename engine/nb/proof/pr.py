"""PR mode: the exact shape and contents of one proposed library change.

The library accepts one article bundle, an owner-authorized retraction, or an
exact workflow sync from the fork's main branch. Article bundles include the
exact role inputs and outputs that produced the article.
"""

from __future__ import annotations

import datetime as _dt
import os
import pathlib
import subprocess
import tempfile

from nb import meta as nb_meta
from nb.artifacts import artifact_warnings, validate_artifacts
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


def materialize_bundle(repo, head, changes, dest):
    """Write the PR's files, as `head` has them, under dest.

    The proof reads the bundle from disk (the article, then its bundle assets
    by size and image header), but the checkout at --repo can be on any branch:
    the documented preflight runs it from the library checkout, where the new
    bundle does not exist yet. What the PR would merge is the blob at head, so
    that is what gets checked, whatever happens to be checked out.
    """
    for _status, relpath in changes:
        blob = subprocess.run(
            ["git", "-C", repo, "show", f"{head}:{relpath}"],
            capture_output=True,
            check=True,
        ).stdout
        target = os.path.join(dest, relpath)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as fh:
            fh.write(blob)


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
        if nb_meta.article_bundle_path(changes, status="D") is None:
            rep.block(
                "B-DIFF-SHAPE",
                "an owner curation PR deletes one article and only its matching "
                f"local article assets; found {changes}",
            )
        else:
            rep.notes.append(
                f"owner curation: retracts {len(changes)} published article(s); "
                "nothing to proof"
            )
        return
    path = nb_meta.article_bundle_path(changes)
    if path is None:
        rep.block(
            "B-DIFF-SHAPE",
            "PR must add one article and only its matching assets and agent artifacts; found "
            f"{[(status, path) for status, path in changes]}",
        )
        return
    m = PR_PATH_RE.match(path)
    assert m is not None
    series_id = m.group(1)
    series_cfg, _ = load_series(cfg_repo, series_id)
    rep.strict = bool(series_cfg and series_cfg.get("strict"))
    with tempfile.TemporaryDirectory() as bundle_dir:
        materialize_bundle(repo, head, changes, bundle_dir)
        for issue in validate_artifacts(
            pathlib.Path(bundle_dir), series=series_id, slug=m.group(2)
        ):
            rep.block("B-AGENT-ARTIFACTS", issue)
        for warning in artifact_warnings(
            pathlib.Path(bundle_dir), series=series_id, slug=m.group(2)
        ):
            rep.warn("W-VOICE-THIN", warning)
        check_article(
            os.path.join(bundle_dir, path),
            series_id,
            repo=cfg_repo,
            library_dir=library,
            rep=rep,
            today=today and _dt.date.fromisoformat(today),
            check_links=check_links,
        )
