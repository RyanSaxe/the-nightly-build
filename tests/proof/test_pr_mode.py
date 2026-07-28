"""Exercise every diff shape accepted by Article PR validation.

Real Git branches cover one article bundle, owner-authorized retraction, and an
exact protected-workflow sync. The checks also prove that validation reads the
named head's committed blobs rather than a checkout or PR-body description.
"""

import pathlib

from conftest import PressRepo
from press import article


def test_pr_happy_path(pr_repo: PressRepo) -> None:
    result = pr_repo.run_pr()

    assert not result.blocks


def test_preflight_passes_from_the_library_checkout(pr_repo: PressRepo) -> None:
    """Proof reads proposed blobs even when the checkout lacks the new bundle.

    On 2026-07-16 two desks hit a false file-not-found block because preflight
    ran from the library checkout. The named head, not the working tree, is the
    exact content a merge would publish.
    """
    pr_repo.checkout("library")

    result = pr_repo.run_pr()

    assert not result.blocks


def test_pr_proofs_the_head_ref_not_the_working_tree(pr_repo: PressRepo) -> None:
    pr_repo.write("library/semiconductors/micron.html", "uncommitted garbage")

    result = pr_repo.run_pr()

    assert not result.blocks


def test_pr_touching_two_files(pr_repo: PressRepo) -> None:
    pr_repo.write("library/semiconductors/extra.txt", "x")
    pr_repo.commit("extra")

    result = pr_repo.run_pr()

    assert "B-DIFF-SHAPE" in result.blocks


def test_pr_accepts_matching_figure_assets(pr_repo: PressRepo) -> None:
    pr_repo.write("library/semiconductors/micron/figure-1.png", "image")
    pr_repo.commit("figure asset")

    result = pr_repo.run_pr()

    assert "B-DIFF-SHAPE" not in result.codes


def test_pr_requires_the_complete_matching_artifact_tree(pr_repo: PressRepo) -> None:
    pr_repo.git(
        "rm",
        "-q",
        "agent-artifacts/semiconductors/micron/editor/01/editorial-review.md",
    )
    pr_repo.commit("drop editor review")

    result = pr_repo.run_pr()

    assert "B-AGENT-ARTIFACTS" in result.blocks


def test_pr_accepts_numbered_revision_artifacts(pr_repo: PressRepo) -> None:
    for filename in ("brief.md", "draft-handoff.md"):
        pr_repo.write(
            f"agent-artifacts/semiconductors/micron/writer/02/{filename}",
            f"# Writer revision\n\nComplete {filename}.\n",
        )
    pr_repo.commit("record writer revision")

    result = pr_repo.run_pr()

    assert "B-AGENT-ARTIFACTS" not in result.codes


def test_pr_rejects_another_articles_figure_asset(pr_repo: PressRepo) -> None:
    pr_repo.write("library/semiconductors/tsmc/figure-1.png", "image")
    pr_repo.commit("wrong figure asset")

    result = pr_repo.run_pr()

    assert "B-DIFF-SHAPE" in result.blocks


def test_pr_modifying_engine_code(pr_repo: PressRepo) -> None:
    check_py = pathlib.Path(pr_repo.path, "engine", "check.py")
    pr_repo.write("engine/check.py", check_py.read_text() + "\n# sneak\n")
    pr_repo.commit("sneak")

    result = pr_repo.run_pr()

    assert "B-DIFF-SHAPE" in result.blocks


def prepare_workflow_sync(
    pr_repo: PressRepo,
    paths: tuple[str, ...] = (
        ".github/workflows/check.yml",
        ".github/workflows/publish.yml",
    ),
) -> str:
    workflows = {
        ".github/workflows/check.yml": "name: canonical check\n",
        ".github/workflows/publish.yml": "name: canonical publish\n",
    }
    pr_repo.checkout("library")
    pr_repo.checkout("nb/sync-library-workflows", new=True)
    for path in paths:
        pr_repo.write(path, workflows[path])
    pr_repo.commit("chore: sync library workflows from main abc123")
    return "nb/sync-library-workflows"


def test_pr_accepts_an_exact_workflow_sync(pr_repo: PressRepo) -> None:
    head = prepare_workflow_sync(pr_repo)

    result = pr_repo.run_pr(head=head)

    assert not result.blocks
    assert result.report.outcome == "SYNC"


def test_pr_accepts_one_stale_canonical_workflow(pr_repo: PressRepo) -> None:
    head = prepare_workflow_sync(pr_repo, (".github/workflows/check.yml",))

    result = pr_repo.run_pr(head=head)

    assert not result.blocks
    assert result.report.outcome == "SYNC"


def test_workflow_sync_rejects_an_extra_file(pr_repo: PressRepo) -> None:
    head = prepare_workflow_sync(pr_repo)
    pr_repo.write("unexpected.txt", "not part of a sync\n")
    pr_repo.commit("sneak in another file")

    result = pr_repo.run_pr(head=head)

    assert "B-WORKFLOW-SYNC" in result.blocks


def test_workflow_sync_rejects_a_noncanonical_blob(pr_repo: PressRepo) -> None:
    head = prepare_workflow_sync(pr_repo)
    pr_repo.write(".github/workflows/check.yml", "name: changed in the PR\n")
    pr_repo.commit("change canonical workflow")
    pr_repo.write(".github/workflows/check.yml", "name: canonical check\n")

    result = pr_repo.run_pr(head=head)

    assert "B-WORKFLOW-SYNC" in result.blocks


def retract_on_a_curation_branch(pr_repo: PressRepo) -> None:
    pr_repo.checkout("library")
    pr_repo.write("library/semiconductors/tsmc.html", article())
    pr_repo.commit("published")
    pr_repo.checkout("owner/curation", new=True)
    pr_repo.git("rm", "-q", "library/semiconductors/tsmc.html")
    pr_repo.git("commit", "-qm", "retract")


def test_deletion_only_pr_without_the_owner_flag(pr_repo: PressRepo) -> None:
    retract_on_a_curation_branch(pr_repo)

    result = pr_repo.run_pr(head="owner/curation", deletions_by_owner=False)

    assert "B-DIFF-SHAPE" in result.blocks


def test_owner_curation_deletion_only_pr(pr_repo: PressRepo) -> None:
    retract_on_a_curation_branch(pr_repo)

    result = pr_repo.run_pr(head="owner/curation", deletions_by_owner=True)

    assert not result.blocks


def test_owner_curation_deleting_engine_files(pr_repo: PressRepo) -> None:
    retract_on_a_curation_branch(pr_repo)
    pr_repo.git("rm", "-q", "engine/duty.py")
    pr_repo.git("commit", "-qm", "stray deletion")

    result = pr_repo.run_pr(head="owner/curation", deletions_by_owner=True)

    assert "B-DIFF-SHAPE" in result.blocks
