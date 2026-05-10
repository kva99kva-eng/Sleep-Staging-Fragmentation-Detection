# Sleep Staging and Fragmentation Detection

[![Tests](https://github.com/kva99kva-eng/Sleep-Staging-Fragmentation-Detection/actions/workflows/tests.yml/badge.svg)](https://github.com/kva99kva-eng/Sleep-Staging-Fragmentation-Detection/actions/workflows/tests.yml)

Exploratory sleep-staging and sleep-fragmentation analysis using open Sleep-EDF polysomnography data.

This project is designed as a portfolio-ready computational neuroscience / sleep-tech case study. It demonstrates how to transform Sleep-EDF annotations into epoch-level labels, train a baseline sleep-stage classifier, and translate predicted stage sequences into interpretable sleep-fragmentation metrics.

## Executive Summary

This project demonstrates an end-to-end sleep analysis workflow:

- load Sleep-EDF hypnogram and PSG files;
- map raw sleep annotations into standard sleep stages;
- construct 30-second epoch-level sleep-stage labels;
- prepare EEG-derived baseline features;
- train a baseline Random Forest sleep-stage classifier;
- evaluate stage-level classification with subject-aware validation;
- compute sleep-fragmentation metrics from true and predicted stage sequences;
- compare true vs predicted fragmentation patterns.

The strongest part of the project is the link between ML predictions and downstream sleep metrics: it does not stop at stage classification, but also shows how prediction errors affect fragmentation analysis.

## Project Goal

The goal is to build a reproducible mini-pipeline for sleep staging and fragmentation analysis.

The project focuses on:

- sleep-stage annotation processing;
- epoch-level feature and label construction;
- baseline sleep-stage classification;
- confusion matrix analysis;
- fragmentation metrics;
- true vs predicted sleep-sequence comparison;
- clear limitations for educational, non-clinical use.

## Dataset

This project uses a small subset of Sleep-EDF Expanded.

Raw Sleep-EDF PSG files are not included in the repository because they are large. Small example hypnogram files and generated processed tables may be used for demonstration.

Expected local structure:

```text
data/
├── raw/
│   └── sleep_edf/
│       └── sleep-cassette/
└── processed/
```

## Sleep Stages

The analysis maps raw Sleep-EDF annotations into common sleep-stage labels:

| Stage | Meaning |
|---|---|
| Wake | Wakefulness |
| N1 | Light non-REM sleep |
| N2 | Stable non-REM sleep |
| N3 | Deep non-REM sleep |
| REM | Rapid-eye-movement sleep |

## Notebooks

| Notebook | Description |
|---|---|
| `01_data_loading_and_epoching.ipynb` | Load Sleep-EDF annotations, map labels and create epoch-level data |
| `02_baseline_sleep_staging_clean.ipynb` | Train a baseline sleep-stage classifier using EEG-derived features |
| `03_fragmentation_metrics.ipynb` | Compute fragmentation metrics from true and predicted stage sequences |

## Methods

- Sleep-EDF hypnogram processing
- 30-second epoch label construction
- Sleep-stage mapping
- EEG spectral feature preparation
- Baseline Random Forest classification
- Subject-aware validation
- Confusion matrix analysis
- Sleep-fragmentation metrics
- True vs predicted fragmentation comparison

## Current Baseline Result

The current mini-baseline validates the end-to-end workflow on a small subset.

Observed pattern:

- best performance on Wake and N3;
- moderate performance on N2;
- weaker performance on REM;
- poorest performance on N1.

This pattern is expected for a baseline sleep-staging model because N1 is rare and often difficult to separate from neighboring stages.

## Key Visual Results

### Hypnogram Example

![Sleep hypnogram example](figures/SC4001_hypnogram.png)

### Baseline Confusion Matrix

![Baseline confusion matrix](figures/baseline_confusion_matrix_mini.png)

### Fragmentation Index: True vs Predicted

![Fragmentation true vs predicted](figures/fragmentation_index_true_vs_pred_mini.png)

### Fragmentation Metrics Scatter Plot

![Fragmentation scatter plot](figures/fragmentation_index_scatter_mini.png)

## Why This Project Matters

This project demonstrates skills relevant to sleep-tech, neurotechnology and computational neuroscience roles:

- working with physiological time-series data;
- building reproducible preprocessing workflows;
- converting raw annotations into modeling targets;
- extracting interpretable signal features;
- training and evaluating baseline ML models;
- translating predictions into sleep-quality and fragmentation metrics;
- communicating technical and clinical limitations clearly.

## Project Structure

```text
Sleep-Staging-Fragmentation-Detection/
|-- .github/
|   `-- workflows/
|       `-- tests.yml
|-- data/
|   |-- raw/
|   `-- processed/
|-- figures/
|   |-- SC4001_hypnogram.png
|   |-- baseline_confusion_matrix_mini.png
|   |-- fragmentation_index_true_vs_pred_mini.png
|   `-- fragmentation_index_scatter_mini.png
|-- notebooks/
|   |-- 01_data_loading_and_epoching.ipynb
|   |-- 02_baseline_sleep_staging_clean.ipynb
|   `-- 03_fragmentation_metrics.ipynb
|-- tests/
|   |-- test_artifacts.py
|   |-- test_notebooks.py
|   |-- test_project_structure.py
|   `-- test_readme_quality.py
|-- .gitattributes
|-- .gitignore
|-- LICENSE
|-- README.md
`-- requirements.txt
```


## Quality and Reproducibility

This repository is structured as a reproducible notebook-based sleep-tech analysis project.

| Component | Purpose |
|---|---|
| `notebooks/` | Step-by-step workflow for data loading, baseline modeling and fragmentation analysis |
| `data/processed/` | Generated epoch-level features, predictions and fragmentation metrics |
| `figures/` | Saved visual outputs used in the README |
| `tests/` | Automated checks for project structure, notebooks, figures, processed artifacts and README quality |
| GitHub Actions | Runs the test suite automatically on push and pull request |
| `.gitignore` | Keeps local caches and large generated files out of the repository |

Current local test status:

`11 passed`


## Installation

Clone the repository:

```bash
git clone https://github.com/kva99kva-eng/Sleep-Staging-Fragmentation-Detection.git
cd Sleep-Staging-Fragmentation-Detection
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Jupyter Lab:

```bash
jupyter lab
```

Then run notebooks in order from `01` to `03`.

## Reproducibility Notes

The notebooks are designed to be run from inside the project folder.

The project uses a portable project-root detector instead of hard-coded local paths.

Large raw PSG files are intentionally excluded from Git. Place local Sleep-EDF files in the expected `data/raw/sleep_edf/sleep-cassette/` folder.

## Validation and Interpretation

The current model is a baseline demonstration, not a production sleep-staging system.

The correct interpretation is:

- the pipeline demonstrates sleep-stage data preparation and baseline modeling;
- fragmentation metrics demonstrate downstream analysis from stage sequences;
- model scores from the mini-subset should not be treated as clinically validated;
- results are useful for portfolio demonstration and method explanation.

## Limitations

- The current modeling uses a mini-subset for pipeline validation.
- Only a baseline classical ML approach is included so far.
- No deep learning model has been added yet.
- Raw PSG files are not included because they are large.
- Sleep-stage classification is not clinically validated.
- The project is exploratory and not intended for clinical use.

## Future Work

- Scale the baseline to more Sleep-EDF subjects.
- Compare Random Forest with Logistic Regression and deep learning baselines.
- Improve performance on minority stages such as N1.
- Add subject-level error analysis.
- Add true-vs-predicted hypnogram comparisons.
- Extend fragmentation analysis to larger subject cohorts.
- Add dedicated Python modules for epoch mapping and fragmentation metrics if the project grows beyond notebook form.


## Tech Stack

- Python
- pandas
- NumPy
- Matplotlib
- SciPy
- scikit-learn
- MNE
- Jupyter Lab

## Resume Summary

Built an exploratory Sleep-EDF sleep-staging and fragmentation-analysis pipeline. Processed hypnogram annotations into epoch-level labels, trained a baseline sleep-stage classifier, evaluated confusion patterns and translated predicted stage sequences into fragmentation metrics with clear clinical limitations.

## License

This project is licensed under the MIT License.
