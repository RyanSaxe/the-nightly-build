"""Mechanical checks for cross-harness agent discovery.

Prompt language is reviewed as prompt language. These tests cover only the
filesystem and metadata interfaces a harness must resolve before it can load
the relevant instructions.
"""

from __future__ import annotations

import pathlib

import yaml

from nb.artifacts import ROLE_FILES

REPO = pathlib.Path(__file__).parents[1]
SKILLS = REPO / ".agents" / "skills"


def skill_metadata(path: pathlib.Path) -> dict[str, str]:
    parts = path.read_text(encoding="utf-8").split("---", 2)
    assert len(parts) == 3, f"missing YAML frontmatter: {path.relative_to(REPO)}"
    parsed = yaml.safe_load(parts[1])
    assert isinstance(parsed, dict), f"invalid frontmatter: {path.relative_to(REPO)}"
    return {str(key): str(value) for key, value in parsed.items()}


def test_required_entrypoints_resolve_to_named_skills() -> None:
    required = {"correspondent", "nb-user-assistant", *ROLE_FILES}

    for name in required:
        path = SKILLS / name / "SKILL.md"
        metadata = skill_metadata(path)
        assert metadata["name"] == name
        assert metadata.get("description", "").strip()


def test_harness_instructions_import_the_canonical_router() -> None:
    assert (REPO / "CLAUDE.md").read_bytes() == b"@AGENTS.md\n"
    assert (REPO / "GEMINI.md").read_bytes() == b"@./AGENTS.md\n"


def test_claude_user_assistant_adapter_resolves_the_canonical_skill() -> None:
    canonical = SKILLS / "nb-user-assistant" / "SKILL.md"
    adapter = REPO / ".claude" / "skills" / "nb-user-assistant" / "SKILL.md"

    assert skill_metadata(adapter) == skill_metadata(canonical)
    assert "../../../.agents/skills/nb-user-assistant/SKILL.md" in adapter.read_text(
        encoding="utf-8"
    )
