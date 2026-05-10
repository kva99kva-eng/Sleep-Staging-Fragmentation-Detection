from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_key_processed_files_exist_and_are_not_empty():
    processed_files = [
        "data/processed/SC4001_epoch_index.csv",
        "data/processed/fragmentation_metrics_mini.csv",
        "data/processed/sleep_edf_epoch_features.csv",
        "data/processed/sleep_edf_epoch_index.csv",
        "data/processed/sleep_staging_baseline_results_mini.csv",
        "data/processed/sleep_staging_classification_report_mini.csv",
        "data/processed/sleep_staging_cv_predictions_mini.csv",
    ]

    for file_path in processed_files:
        path = PROJECT_ROOT / file_path
        assert path.exists(), f"Missing processed file: {file_path}"
        assert path.stat().st_size > 0, f"Processed file is empty: {file_path}"


def test_key_figures_exist_and_are_not_empty():
    figures = [
        "figures/SC4001_hypnogram.png",
        "figures/baseline_confusion_matrix_mini.png",
        "figures/fragmentation_index_scatter_mini.png",
        "figures/fragmentation_index_true_vs_pred_mini.png",
        "figures/fragmentation_true_vs_pred_transitions_mini.png",
        "figures/fragmentation_true_vs_pred_wake_intrusions_mini.png",
        "figures/sleep_edf_epoch_stage_distribution.png",
    ]

    for file_path in figures:
        path = PROJECT_ROOT / file_path
        assert path.exists(), f"Missing figure: {file_path}"
        assert path.stat().st_size > 0, f"Figure is empty: {file_path}"


def test_example_raw_hypnograms_exist():
    raw_files = [
        "data/raw/sleep_edf/SC4001EC-Hypnogram.edf",
        "data/raw/sleep_edf/SC4002EC-Hypnogram.edf",
        "data/raw/sleep_edf/SC4011EH-Hypnogram.edf",
        "data/raw/sleep_edf/SC4012EC-Hypnogram.edf",
    ]

    for file_path in raw_files:
        path = PROJECT_ROOT / file_path
        assert path.exists(), f"Missing raw hypnogram file: {file_path}"
        assert path.stat().st_size > 0, f"Raw hypnogram file is empty: {file_path}"
