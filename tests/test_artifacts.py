"""Article artifacts are semantic Markdown whose exactness comes from Git.

These tests exercise the complete structural contract without inspecting role
prose. They protect useful review properties—named inputs and outputs,
contiguous revisions, no placeholders, and no unrelated files—while allowing
the editorial language itself to evolve freely.
"""

from __future__ import annotations

import pathlib

from nb.artifacts import (
    ROLE_FILES,
    artifact_root,
    artifact_warnings,
    validate_artifacts,
)


def complete_tree(root: pathlib.Path) -> pathlib.Path:
    artifacts = artifact_root(root, series="the-wire", slug="example")
    artifacts.mkdir(parents=True)
    (artifacts / "editorial-direction.md").write_text(
        "# Editorial direction\n\nWrite clearly.\n"
    )
    (artifacts / "commission.md").write_text("# Commission\n\nInvestigate this.\n")
    for role, filenames in ROLE_FILES.items():
        invocation = artifacts / role / "01"
        invocation.mkdir(parents=True)
        for filename in filenames:
            (invocation / filename).write_text(f"# {role} {filename}\n\nComplete.\n")
    return artifacts


def test_complete_semantic_tree_passes(tmp_path: pathlib.Path) -> None:
    complete_tree(tmp_path)

    assert validate_artifacts(tmp_path, series="the-wire", slug="example") == []


def test_every_role_and_root_input_are_required(tmp_path: pathlib.Path) -> None:
    artifacts = complete_tree(tmp_path)
    (artifacts / "editorial-direction.md").unlink()
    (artifacts / "commission.md").unlink()
    for path in (artifacts / "researcher").rglob("*"):
        if path.is_file():
            path.unlink()
    (artifacts / "researcher" / "01").rmdir()
    (artifacts / "researcher").rmdir()

    errors = validate_artifacts(tmp_path, series="the-wire", slug="example")

    assert "missing regular file: editorial-direction.md" in errors
    assert "missing regular file: commission.md" in errors
    assert "missing role directory: researcher" in errors


def test_revisions_are_contiguous_and_keep_both_semantic_files(
    tmp_path: pathlib.Path,
) -> None:
    artifacts = complete_tree(tmp_path)
    writer = artifacts / "writer"
    (writer / "03").mkdir()
    (writer / "03" / "brief.md").write_text("Revise the opening.\n")
    (writer / "03" / "draft-handoff.md").write_text("Revised.\n")

    errors = validate_artifacts(tmp_path, series="the-wire", slug="example")

    assert errors == ["writer: invocations must be contiguous from 01; found 01, 03"]


def test_extra_or_empty_artifacts_fail(tmp_path: pathlib.Path) -> None:
    artifacts = complete_tree(tmp_path)
    (artifacts / "notes.txt").write_text("not part of the contract\n")
    (artifacts / "editor" / "01" / "editorial-review.md").write_text("")

    errors = validate_artifacts(tmp_path, series="the-wire", slug="example")

    assert "unexpected artifact entries: ['notes.txt']" in errors
    assert "editor/01: empty artifact: editorial-review.md" in errors


def test_a_voice_guide_without_three_studied_pieces_warns(
    tmp_path: pathlib.Path,
) -> None:
    artifacts = complete_tree(tmp_path)
    guide = artifacts / "writing-coach" / "01" / "voice-guide.md"
    guide.write_text("# Voice guide\n\nSource: https://example.org/only-one-piece\n")

    warnings = artifact_warnings(tmp_path, series="the-wire", slug="example")

    assert warnings == [
        "writing-coach/01/voice-guide.md cites 1 exemplar(s); expected at least 3"
    ]
