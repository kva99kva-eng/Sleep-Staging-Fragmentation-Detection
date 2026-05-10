from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_required_top_level_files_exist():
    required_files = [
        "README.md",
        "requirements.txt",
        "LICENSE",
        ".gitignore",
        ".gitattributes",
    ]

    for file_path in required_files:
        assert (PROJECT_ROOT / file_path).exists(), f"Missing required file: {file_path}"


def test_required_directories_exist():
    required_dirs = [
        "data",
        "data/processed",
        "data/raw",
        "figures",
        "notebooks",
    ]

    for dir_path in required_dirs:
        assert (PROJECT_ROOT / dir_path).exists(), f"Missing required directory: {dir_path}"


def test_expected_notebooks_exist():
    notebooks = [
        "notebooks/01_data_loading_and_epoching.ipynb",
        "notebooks/02_baseline_sleep_staging_clean.ipynb",
        "notebooks/03_fragmentation_metrics.ipynb",
    ]

    for notebook in notebooks:
        path = PROJECT_ROOT / notebook
        assert path.exists(), f"Missing notebook: {notebook}"
        assert path.stat().st_size > 0, f"Notebook is empty: {notebook}"
