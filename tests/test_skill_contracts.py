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
WRITER_BRIEFING_SURFACES = (
    REPO / "PROTOCOL.md",
    REPO / "skills/correspondent/SKILL.md",
    REPO / "skills/writer/SKILL.md",
    REPO / "spec/banned-terms.yaml",
    REPO / "spec/editorial.md",
    REPO / "templates/FURNITURE.md",
    REPO / "templates/article/identity.md",
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


def test_editorial_loop_settles_before_publishing() -> None:
    correspondent = (REPO / "skills/correspondent/SKILL.md").read_text(encoding="utf-8")
    editor = (REPO / "skills/editor/SKILL.md").read_text(encoding="utf-8")

    assert "no round cap" in correspondent
    assert "only `DONE editor`" in correspondent
    assert "recovery pass" in correspondent
    assert "correspondent's" in correspondent
    assert "model at high effort" in correspondent
    assert "optional polish" in editor
    assert "BLOCKED editor <reason>" in editor


def test_editor_audits_prompt_leakage_across_the_whole_article() -> None:
    editor = (REPO / "skills/editor/SKILL.md").read_text(encoding="utf-8")
    editor_prose = " ".join(editor.split())

    for surface in (
        "headline",
        "dek",
        "headings",
        "body",
        "captions",
        "notes",
        "bookends",
    ):
        assert surface in editor_prose
    for leak in (
        "near-copies",
        "selection criteria",
        "taxonomy names",
        "structural labels",
        "self-grading prose",
        "nouns substituted",
        "synonyms",
    ):
        assert leak in editor_prose
    assert "Fixed template chrome is exempt" in editor_prose
    assert "Prompt leakage:" in editor_prose


def test_article_identity_does_not_supply_the_known_leaked_phrase() -> None:
    identity = (REPO / "templates/article/identity.md").read_text(encoding="utf-8")
    identity_prose = " ".join(identity.split())

    assert "earns its place" not in identity_prose
    assert (
        "Outline the article's reasoning before naming its sections." in identity_prose
    )
    assert (
        "Remove any section whose deletion leaves that reasoning unchanged."
        in identity_prose
    )


def test_writer_briefing_removes_the_repeated_editorial_judgment() -> None:
    offenders = {
        path.relative_to(REPO): phrase
        for path in WRITER_BRIEFING_SURFACES
        for phrase in ("earns its place", "worth publishing")
        if phrase in path.read_text(encoding="utf-8").lower()
    }

    assert offenders == {}
