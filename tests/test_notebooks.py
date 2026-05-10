import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_notebooks_are_valid_json():
    notebook_paths = sorted((PROJECT_ROOT / "notebooks").glob("*.ipynb"))

    assert notebook_paths, "No notebooks found"

    for path in notebook_paths:
        with path.open("r", encoding="utf-8") as file:
            notebook = json.load(file)

        assert "cells" in notebook, f"Notebook has no cells field: {path.name}"
        assert len(notebook["cells"]) > 0, f"Notebook has no cells: {path.name}"
        assert "metadata" in notebook, f"Notebook has no metadata: {path.name}"


def test_notebooks_contain_markdown_explanations():
    notebook_paths = sorted((PROJECT_ROOT / "notebooks").glob("*.ipynb"))

    for path in notebook_paths:
        with path.open("r", encoding="utf-8") as file:
            notebook = json.load(file)

        markdown_cells = [
            cell for cell in notebook["cells"]
            if cell.get("cell_type") == "markdown"
        ]

        assert markdown_cells, f"Notebook should contain markdown explanations: {path.name}"
