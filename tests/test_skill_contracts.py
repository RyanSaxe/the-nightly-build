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


def test_librarian_treats_press_as_an_authorization_boundary() -> None:
    librarian = (REPO / "skills/librarian/SKILL.md").read_text(encoding="utf-8")

    assert "authorization boundary" in librarian
    assert "authorizes changes under `press/` only" in librarian
    assert "unless the human explicitly asks" in librarian


def test_publisher_is_delivery_only() -> None:
    publisher = (REPO / "skills/publisher/SKILL.md").read_text(encoding="utf-8")

    assert "deliberately cheap and operational" in publisher
    assert "You do not coach, research, draft" in publisher
    assert "edit, summarize artifacts, or make editorial judgment" in publisher
    assert "DONE publisher <PR URL> GREEN <WARN count>" in publisher


def test_editorial_loop_settles_before_publishing() -> None:
    correspondent = (REPO / "skills/correspondent/SKILL.md").read_text(encoding="utf-8")
    correspondent_prose = " ".join(correspondent.split())
    editor = (REPO / "skills/editor/SKILL.md").read_text(encoding="utf-8")

    assert "no round cap" in correspondent_prose
    assert "only `DONE editor`" in correspondent_prose
    assert "does not end the article" in correspondent_prose
    assert "Do not repeat an unchanged attempt." in correspondent_prose
    assert "take over the blocked role yourself" in correspondent_prose
    assert "does not waive `DONE editor`" in correspondent_prose
    assert "external constraint makes publication impossible" in correspondent_prose
    assert "repeated objections" in correspondent_prose
    assert "optional polish" in editor
    assert "BLOCKED editor <reason>" in editor


def test_editor_checks_prompt_leakage_during_the_cut() -> None:
    editor = (REPO / "skills/editor/SKILL.md").read_text(encoding="utf-8")
    cut = editor.split("## Second read: the cut", 1)[1].split(
        "## Third read: the reader", 1
    )[0]
    cut_prose = " ".join(cut.split())

    assert "prompt leakage: language drawn from instructions" in cut_prose
    assert "Compare all authored text with the briefing stack." in cut_prose
    assert "Fixed template labels, necessary names, and sourced facts" in cut_prose
    assert "Prompt leakage:" not in editor
    assert "the three required lines" in editor


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
    assert "summary lede is a table of contents" not in identity_prose


def test_writer_prompts_use_plain_directions() -> None:
    prompting = (REPO / "spec/prompting.md").read_text(encoding="utf-8")

    assert "Keep planning labels in working files." in prompting
    assert "Write prompts as directions, not sample article sentences." in prompting
    assert "keep its taxonomy" not in prompting
    assert "subject's nouns" not in prompting


def test_furniture_does_not_prompt_for_mechanisms() -> None:
    furniture = (REPO / "templates/FURNITURE.md").read_text(encoding="utf-8")

    assert "mechanism" not in furniture.lower()


def test_writer_briefing_removes_the_repeated_editorial_judgment() -> None:
    offenders = {
        path.relative_to(REPO): phrase
        for path in WRITER_BRIEFING_SURFACES
        for phrase in ("earns its place", "worth publishing")
        if phrase in path.read_text(encoding="utf-8").lower()
    }

    assert offenders == {}
