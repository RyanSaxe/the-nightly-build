"""Prompt surfaces should request judgment without leaking stock copy."""

from pathlib import Path

REPO = Path(__file__).parents[1]


def test_unbiased_crux_does_not_offer_a_taxonomy() -> None:
    leaked_labels = ("unsettled fact", "clash of values", "forecast")
    prompt_paths = (
        REPO / "templates" / "unbiased" / "identity.md",
        REPO / "templates" / "unbiased" / "skeleton.html",
    )

    for path in prompt_paths:
        prompt = path.read_text(encoding="utf-8").lower()
        for label in leaked_labels:
            assert label not in prompt, f"{path.relative_to(REPO)} offers {label!r}"
