"""Validate the exact editorial artifacts committed with one article.

Git already supplies immutable bytes, file identity, and commit provenance, so
the artifact contract is intentionally structural. Each role invocation has a
semantic brief and output filename; numbered directories preserve revisions
without a second manifest or metadata language.
"""

from __future__ import annotations

import pathlib
import re
from collections.abc import Mapping

__all__ = (
    "ROLE_FILES",
    "artifact_warnings",
    "artifact_root",
    "validate_artifacts",
)

ROLE_FILES: Mapping[str, tuple[str, str]] = {
    "writing-coach": ("brief.md", "voice-guide.md"),
    "researcher": ("brief.md", "evidence.md"),
    "writer": ("brief.md", "draft-handoff.md"),
    "editor": ("review-brief.md", "editorial-review.md"),
}
ROOT_FILES = ("editorial-direction.md", "commission.md")
INVOCATION_RE = re.compile(r"^[0-9]{2}$")
SOURCE_LINE_RE = re.compile(r"^\s*Source:\s*https?://\S+", re.IGNORECASE | re.MULTILINE)
VOICE_EXEMPLARS_MIN = 3


def artifact_root(root: pathlib.Path, *, series: str, slug: str) -> pathlib.Path:
    return root / "agent-artifacts" / series / slug


def _readable_markdown(path: pathlib.Path) -> str | None:
    if not path.is_file() or path.is_symlink():
        return f"missing regular file: {path.name}"
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return f"not UTF-8 Markdown: {path.name}"
    if not content.strip():
        return f"empty artifact: {path.name}"
    return None


def _role_errors(root: pathlib.Path, role: str) -> list[str]:
    role_root = root / role
    if not role_root.is_dir() or role_root.is_symlink():
        return [f"missing role directory: {role}"]

    children = sorted(role_root.iterdir(), key=lambda path: path.name)
    invalid = [path.name for path in children if not INVOCATION_RE.fullmatch(path.name)]
    if invalid:
        return [f"{role}: unexpected invocation entries: {', '.join(invalid)}"]
    invocations = [int(path.name) for path in children]
    if not invocations:
        return [f"{role}: no invocations"]
    expected = list(range(1, len(invocations) + 1))
    if invocations != expected:
        return [
            f"{role}: invocations must be contiguous from 01; found "
            + ", ".join(f"{number:02d}" for number in invocations)
        ]

    errors: list[str] = []
    expected_files = set(ROLE_FILES[role])
    for child in children:
        if not child.is_dir() or child.is_symlink():
            errors.append(f"{role}/{child.name}: must be a directory")
            continue
        actual_files = {path.name for path in child.iterdir()}
        if actual_files != expected_files:
            errors.append(
                f"{role}/{child.name}: expected {sorted(expected_files)}; "
                f"found {sorted(actual_files)}"
            )
            continue
        for filename in sorted(expected_files):
            issue = _readable_markdown(child / filename)
            if issue:
                errors.append(f"{role}/{child.name}: {issue}")
    return errors


def validate_artifacts(root: pathlib.Path, *, series: str, slug: str) -> list[str]:
    artifacts = artifact_root(root, series=series, slug=slug)
    if not artifacts.is_dir() or artifacts.is_symlink():
        return [f"missing artifact tree: agent-artifacts/{series}/{slug}"]

    allowed = {*ROOT_FILES, *ROLE_FILES}
    actual = {path.name for path in artifacts.iterdir()}
    errors = (
        [f"unexpected artifact entries: {sorted(actual - allowed)}"]
        if actual - allowed
        else []
    )
    for filename in ROOT_FILES:
        issue = _readable_markdown(artifacts / filename)
        if issue:
            errors.append(issue)
    for role in ROLE_FILES:
        errors.extend(_role_errors(artifacts, role))
    return errors


def artifact_warnings(root: pathlib.Path, *, series: str, slug: str) -> list[str]:
    """Return quality warnings that can be proven from semantic artifacts.

    Structure remains the publishing gate. This narrower audit preserves the
    writing coach's longstanding quality signal: a guide that names outlets or
    gestures at a voice without citing three pieces was not actually studied.
    """
    coach = artifact_root(root, series=series, slug=slug) / "writing-coach"
    if not coach.is_dir():
        return []
    warnings = []
    for invocation in sorted(coach.iterdir(), key=lambda path: path.name):
        guide = invocation / "voice-guide.md"
        if not guide.is_file():
            continue
        count = len(SOURCE_LINE_RE.findall(guide.read_text(encoding="utf-8")))
        if count < VOICE_EXEMPLARS_MIN:
            warnings.append(
                f"writing-coach/{invocation.name}/voice-guide.md cites "
                f"{count} exemplar(s); expected at least {VOICE_EXEMPLARS_MIN}"
            )
    return warnings
