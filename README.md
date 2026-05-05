# Sleep Staging and Fragmentation Detection

An exploratory neurotech project for automatic sleep stage classification and sleep fragmentation analysis using open polysomnography data from sleep_edf.

This project builds an end-to-end baseline pipeline that loads sleep annotations, converts hypnogram data into 30-second epoch labels, trains a baseline sleep stage classifier, and derives sleep fragmentation metrics from true and predicted stage sequences.

The project is designed as a portfolio-quality computational neuroscience / neurotechnology case study rather than a clinical decision system.

## Project Goal

The goal of this project is to:

- load raw sleep_edf hypnogram files;
- convert sleep annotations into epoch-level labels;
- prepare EEG-derived sleep staging features;
- train a baseline sleep stage classifier;
- evaluate stage-level classification performance;
- compute sleep fragmentation metrics from true and predicted stage sequences;
- compare true and predicted sleep fragmentation patterns.

## Dataset

This project uses a small subset of sleep_edf Expanded.

For the current mini-version, the baseline experiments were run on a limited subset of subjects and sampled epochs to validate the full modeling pipeline before scaling to a larger sample.

Raw sleep_edf PSG files are not included in this repository. Small hypnogram EDF files used for annotation examples are stored in:

`data/raw/sleep_edf/`

Processed epoch-level tables and model outputs are stored in:

`data/processed/`

## Project Structure

- `notebooks/01_data_loading_and_epoching.ipynb` - data loading, annotation mapping, and epoch table creation.
- `notebooks/02_baseline_sleep_staging_clean.ipynb` - baseline sleep stage classification with EEG spectral features.
- `notebooks/03_fragmentation_metrics.ipynb` - sleep fragmentation metrics from true and predicted stage sequences.
- `data/raw/sleep_edf/` - small sleep_edf hypnogram files used in the mini-version.
- `data/processed/` - processed epoch tables, predictions, classification reports, and metrics.
- `figures/` - visual results used for reporting and README.
- `models/` - reserved for future trained model artifacts.
- `requirements.txt` - Python dependencies.
- `LICENSE` - MIT license.

## Methods

- sleep_edf hypnogram processing
- 30-second epoch label construction
- Sleep stage mapping
- EEG spectral feature preparation
- Baseline Random Forest classification
- Subject-aware cross-validation
- Confusion matrix analysis
- Sleep fragmentation metrics
- True vs predicted fragmentation comparison

## Notebooks

### 01 Data Loading and Epoching

Loads PSG / hypnogram-related sleep_edf files, maps annotations to sleep stages, and creates a 30-second epoch-level dataset.

Main outputs:

- epoch-level sleep stage labels;
- hypnogram visualization;
- processed epoch index tables.

### 02 Baseline Sleep Staging

Builds a baseline sleep staging model using EEG spectral features extracted from each epoch.

Main steps:

- EEG channel selection;
- bandpower feature extraction;
- subject-aware cross-validation;
- baseline Random Forest classifier;
- confusion matrix and classification report.

### 03 Fragmentation Metrics

Computes fragmentation-related sleep metrics from true and predicted stage sequences.

Main outputs:

- stage transition counts;
- wake intrusions;
- fragmentation index;
- true vs predicted fragmentation comparison plots.

## Current Baseline Result

The current mini-baseline was trained on a small subset of subjects and sampled epochs to validate the end-to-end pipeline.

Observed pattern:

- best performance on Wake and N3;
- moderate performance on N2;
- weaker performance on REM;
- poorest performance on N1.

This pattern is expected in baseline sleep staging because N1 is both rare and difficult to separate from neighboring stages.

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

This project demonstrates skills relevant to neurotechnology and computational neuroscience roles:

- working with raw physiological data;
- building reproducible preprocessing pipelines;
- extracting interpretable signal features;
- training and evaluating baseline ML models;
- translating predictions into sleep-quality and fragmentation metrics;
- communicating technical limitations clearly.

## Installation

Clone the repository:

`git clone https://github.com/kva99kva-eng/Sleep-Staging-Fragmentation-Detection.git`

Go to the project folder:

`cd Sleep-Staging-Fragmentation-Detection`

Create and activate a virtual environment:

`python -m venv .venv`

Windows PowerShell:

`.\.venv\Scripts\Activate.ps1`

Install dependencies:

`pip install -r requirements.txt`

Run Jupyter Lab:

`jupyter lab`

Then run the notebooks in order from `01` to `03`.

## Limitations

- The current modeling uses a mini-subset for pipeline validation.
- Only a baseline classical ML approach is included so far.
- No deep learning model has been added yet.
- Raw PSG files are not included because they are large.
- The project is exploratory and not intended for clinical use.

## Future Work

- Scale the baseline to more sleep_edf subjects.
- Compare Random Forest with logistic regression and deep learning baselines.
- Improve performance on minority stages such as N1.
- Extend fragmentation analysis to larger subject cohorts.
- Add subject-level error analysis.
- Add true-vs-predicted hypnogram comparisons.

## Tech Stack

- Python
- pandas
- NumPy
- Matplotlib
- SciPy
- scikit-learn
- MNE
- Jupyter Notebook

## License

This project is licensed under the MIT License.

