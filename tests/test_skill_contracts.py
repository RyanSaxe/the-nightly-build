"""Keep executable commands in the runtime instructions on the supported path.

The skills are operational inputs, not passive prose. This guard catches a raw
Python invocation before an agent copies it into a clean scheduled environment
where script-declared dependencies are available only through uv.
"""

import pathlib

REPO = pathlib.Path(__file__).parents[1]
RUNTIME_INSTRUCTIONS = (
    REPO / "PROTOCOL.md",
    *sorted((REPO / "skills").glob("*/SKILL.md")),
)


def test_engine_commands_use_uv() -> None:
    offenders = [
        path.relative_to(REPO)
        for path in RUNTIME_INSTRUCTIONS
        if "python3 engine/" in path.read_text(encoding="utf-8")
    ]

    assert offenders == []


def test_correspondent_launches_every_role_directly() -> None:
    correspondent = (REPO / "skills/correspondent/SKILL.md").read_text(encoding="utf-8")

    assert "Every role is your direct child" in correspondent
    assert "Never ask a child to spawn another child" in correspondent
    for role in ("writing-coach", "researcher", "writer", "editor", "publisher"):
        assert f"`{role}`" in correspondent


def test_runtime_has_no_nested_desk_skill() -> None:
    assert not (REPO / "skills/desk/SKILL.md").exists()

    nested_desk_references = [
        path.relative_to(REPO)
        for path in RUNTIME_INSTRUCTIONS
        if "skills/desk/SKILL.md" in path.read_text(encoding="utf-8")
    ]

    assert nested_desk_references == []


def test_publisher_is_delivery_only() -> None:
    publisher = (REPO / "skills/publisher/SKILL.md").read_text(encoding="utf-8")

    assert "deliberately cheap and operational" in publisher
    assert "You do not coach, research, draft" in publisher
    assert "edit, summarize artifacts, or make editorial judgment" in publisher
    assert "DONE publisher <PR URL> GREEN <WARN count>" in publisher
