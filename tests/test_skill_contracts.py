"""Guard the editorial capability and context boundaries.

These checks avoid coupling tests to incidental prose. They verify durable
interfaces instead: the semantic artifact names, the four-role topology,
purposeful context retrieval, and the preserved writer-editor quality gates.
"""

from __future__ import annotations

import pathlib

from nb.artifacts import ROLE_FILES

REPO = pathlib.Path(__file__).parents[1]
ROLE_SKILLS = {role: REPO / "skills" / role / "SKILL.md" for role in ROLE_FILES}
FORBIDDEN_ROLE_SURFACES = (
    "PROTOCOL.md",
    "spec/",
    "press/",
    "templates/",
    "engine/",
    "git log",
    "git grep",
    "uv run",
)
WRITER_BRIEFING_SURFACES = (
    REPO / "PROTOCOL.md",
    REPO / "skills" / "correspondent" / "SKILL.md",
    REPO / "skills" / "writer" / "SKILL.md",
    REPO / "spec" / "banned-terms.yaml",
    REPO / "spec" / "editorial.md",
    REPO / "templates" / "FURNITURE.md",
    REPO / "templates" / "article" / "identity.md",
)
AGENT_PROMPT_SURFACES = (
    REPO / "PROTOCOL.md",
    REPO / "skills" / "correspondent" / "SKILL.md",
    *ROLE_SKILLS.values(),
)


def test_runtime_has_exactly_four_editorial_roles() -> None:
    assert set(ROLE_FILES) == {"writing-coach", "researcher", "writer", "editor"}
    assert not (REPO / "skills" / "publisher" / "SKILL.md").exists()
    assert not (REPO / "skills" / "desk" / "SKILL.md").exists()


def test_each_role_uses_its_semantic_artifact_contract() -> None:
    for role, (brief, output) in ROLE_FILES.items():
        skill = ROLE_SKILLS[role].read_text(encoding="utf-8")
        assert brief in skill, role
        assert output in skill, role


def test_bounded_roles_do_not_receive_repository_exploration_instructions() -> None:
    offenders = {
        role: forbidden
        for role, path in ROLE_SKILLS.items()
        for forbidden in FORBIDDEN_ROLE_SURFACES
        if forbidden.casefold() in path.read_text(encoding="utf-8").casefold()
    }

    assert offenders == {}


def test_correspondent_owns_context_routing_and_publication() -> None:
    skill = (REPO / "skills" / "correspondent" / "SKILL.md").read_text(encoding="utf-8")
    prose = " ".join(skill.split())

    for role in ROLE_FILES:
        assert f"`{role}`" in skill
    assert "only role expected to hold a whole-paper view" in prose
    assert "nb start-article" in prose
    assert "available tools for focused questions" in prose
    assert "There is no round cap" in prose
    assert "Only an editor `DONE`" in prose
    assert "nb prepare-pr" in prose
    assert "Monitor every Article PR through CI" in prose
    assert "abandoned red PRs" in prose


def test_protocol_governs_the_scheduled_correspondent() -> None:
    agents = (REPO / "AGENTS.md").read_text(encoding="utf-8")
    protocol = (REPO / "PROTOCOL.md").read_text(encoding="utf-8")
    correspondent = (REPO / "skills/correspondent/SKILL.md").read_text(encoding="utf-8")

    assert agents.index("`PROTOCOL.md`") < agents.index(
        "`skills/correspondent/SKILL.md`"
    )
    assert "authoritative contract" in protocol
    assert "Read `PROTOCOL.md` first" in correspondent


def test_editor_preserves_three_reads_surgical_edits_and_prompt_leakage_gate() -> None:
    editor = ROLE_SKILLS["editor"].read_text(encoding="utf-8")
    skeptic = editor.index("## First read: the skeptic")
    cut = editor.index("## Second read: the cut")
    reader = editor.index("## Third read: the reader")

    assert skeptic < cut < reader
    assert "Make cuts and small prose fixes directly" in editor
    assert "past a word or clause" in editor
    assert "prompt leakage" in editor
    assert "writer `brief.md`" in editor
    assert "Fixed template labels" in editor
    assert '"the trap is"' in editor
    assert "A verdict block" in editor
    assert "deliberate emphasis" in editor
    assert "missed opportunities" in editor
    assert "optional polish" in editor
    assert "BLOCKED editor <reason>" in editor


def test_writer_proves_every_draft_and_records_original_work() -> None:
    writer = ROLE_SKILLS["writer"].read_text(encoding="utf-8")

    assert "nb check" in writer
    assert "BLOCK: 0" in writer
    assert "one act of original work" in writer
    assert "draft-handoff.md" in writer
    assert "editorial-review.md" in writer
    assert "editorial-direction.md" in writer
    assert ".nb-context" in writer
    assert "documented in the furniture" in writer
    assert "before drafting" in writer
    assert "rendered page" in writer


def test_writing_coach_cites_three_real_exemplars() -> None:
    coach = ROLE_SKILLS["writing-coach"].read_text(encoding="utf-8")

    assert "at least three exemplars" in coach
    assert "Source: <URL>" in coach


def test_librarian_treats_press_as_an_authorization_boundary() -> None:
    librarian = (REPO / "skills" / "librarian" / "SKILL.md").read_text(encoding="utf-8")

    assert "authorization boundary" in librarian
    assert "authorizes changes under `press/` only" in librarian
    assert "unless the human explicitly asks" in librarian


def test_article_identity_does_not_supply_the_known_leaked_phrase() -> None:
    identity = (REPO / "templates" / "article" / "identity.md").read_text(
        encoding="utf-8"
    )
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
    prompting = (REPO / "spec" / "prompting.md").read_text(encoding="utf-8")

    assert "Keep planning labels in working files." in prompting
    assert "Write prompts as directions, not sample article sentences." in prompting
    assert "keep its taxonomy" not in prompting
    assert "subject's nouns" not in prompting


def test_furniture_has_no_quota_and_preserves_deliberate_emphasis() -> None:
    furniture = (REPO / "templates" / "FURNITURE.md").read_text(encoding="utf-8")
    prose = " ".join(furniture.split())

    assert "mechanism" not in furniture.lower()
    assert "deliberate emphasis" in prose
    assert "There is no target count" in prose
    assert "continuous article rather than a stack of components" in prose
    assert "Two or three pieces" not in prose
    assert "Zero is fine" not in prose


def test_writer_briefing_removes_the_repeated_editorial_judgment() -> None:
    offenders = {
        path.relative_to(REPO): phrase
        for path in WRITER_BRIEFING_SURFACES
        for phrase in ("earns its place", "worth publishing")
        if phrase in path.read_text(encoding="utf-8").lower()
    }

    assert offenders == {}


def test_agent_prompts_do_not_teach_a_banned_stock_term() -> None:
    offenders = {
        path.relative_to(REPO)
        for path in AGENT_PROMPT_SURFACES
        if "load-bearing" in path.read_text(encoding="utf-8").lower()
    }

    assert offenders == set()
