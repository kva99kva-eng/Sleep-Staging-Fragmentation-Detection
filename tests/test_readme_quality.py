from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_readme_contains_key_sections():
    readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")

    expected_sections = [
        "## Executive Summary",
        "## Project Goal",
        "## Dataset",
        "## Notebooks",
        "## Methods",
        "## Current Baseline Result",
        "## Key Visual Results",
        "## Why This Project Matters",
        "## Project Structure",
        "## Installation",
    ]

    for section in expected_sections:
        assert section in readme, f"Missing README section: {section}"


def test_readme_mentions_sleep_staging_and_fragmentation():
    readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8").lower()

    assert "sleep-edf" in readme
    assert "sleep-stage" in readme or "sleep stage" in readme
    assert "fragmentation" in readme
    assert "subject-aware" in readme


def test_readme_has_no_common_encoding_artifacts():
    readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")

    bad_fragments = ["вЂ", "В±", "в”", "В·"]

    for fragment in bad_fragments:
        assert fragment not in readme, f"Encoding artifact found in README: {fragment}"
