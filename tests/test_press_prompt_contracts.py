"""The dogfooded press templates keep their deliberately small contracts."""

from pathlib import Path

import yaml

REPO = Path(__file__).parents[1]


def test_policy_debate_uses_the_open_two_position_template() -> None:
    series = yaml.safe_load(
        (REPO / "press/series/policy-debate/series.yaml").read_text(encoding="utf-8")
    )
    manifest = yaml.safe_load(
        (REPO / "press/templates/debate/manifest.yaml").read_text(encoding="utf-8")
    )

    assert series["template"] == "debate"
    assert manifest["sections"] == ["orientation", "sources"]
    assert manifest["bands"]["flex_sections"] == [2, 2]


def test_debate_prompt_does_not_restore_the_rejected_outline() -> None:
    prompt_paths = (
        REPO / "press/series/policy-debate/prompt.md",
        REPO / "press/templates/debate/identity.md",
        REPO / "press/templates/debate/skeleton.html",
    )
    prompt = "\n".join(
        path.read_text(encoding="utf-8").lower() for path in prompt_paths
    )

    for stock_term in ("crux", "forecast", "what to watch"):
        assert stock_term not in prompt
